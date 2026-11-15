"""Run one XGBoost adapter in its own interpreter using the file-based worker protocol."""

import csv
import ctypes
import hashlib
import json
import os
import resource
import sys
from collections.abc import Callable, Iterator
from contextlib import contextmanager, nullcontext
from functools import partial
from importlib.metadata import distributions
from pathlib import Path
from typing import Any

import numpy as np
from threadpoolctl import threadpool_info, threadpool_limits

from .timing import measure

DISTRIBUTIONS = {"cpu": "xgboost", "metal": "xgboost-metal"}


def engine_distribution(engine: str) -> tuple[str, str]:
    expected = DISTRIBUTIONS[engine]
    installed = [
        (dist.metadata["Name"], dist.version)
        for dist in distributions()
        if dist.metadata["Name"].lower().replace("_", "-") in DISTRIBUTIONS.values()
    ]
    if len(installed) != 1 or installed[0][0].lower().replace("_", "-") != expected:
        raise RuntimeError(
            f"{engine} requires an isolated {expected} environment, found {installed}"
        )
    return installed[0]


def load_engine(engine: str) -> tuple[Any, dict[str, Any]]:
    distribution, version = engine_distribution(engine)
    import xgboost as xgb

    build = xgb.build_info()
    if bool(build.get("USE_METAL")) != (engine == "metal"):
        raise RuntimeError(f"The loaded XGBoost native library does not match {engine}")
    build.pop("libxgboost", None)
    return xgb, {
        "distribution": distribution,
        "distribution_version": version,
        "api_version": xgb.__version__,
        "build": build,
        "python": sys.version.split()[0],
        "numpy": np.__version__,
    }


def no_sync() -> None:
    pass


class MetalObserver:
    def __init__(self, library: Path, directory: Path):
        self.probe = ctypes.CDLL(str(library))
        self.probe.trace_begin.argtypes = [ctypes.c_char_p]
        self.probe.trace_begin_dispatch.argtypes = [ctypes.c_char_p]
        self.probe.trace_end.restype = None
        self.probe.trace_end_dispatch.restype = None
        if not self.probe.trace_install() or not self.probe.trace_install_dispatch():
            raise RuntimeError("Unable to install the Metal completion and dispatch observers")
        self.directory = directory

    @contextmanager
    def observe(self, operation: str) -> Iterator[None]:
        path = self.directory / f"{operation}.tsv"
        dispatch_path = self.directory / f"{operation}-dispatch.tsv"
        if not self.probe.trace_begin_dispatch(os.fsencode(dispatch_path)):
            raise OSError(f"Cannot open {dispatch_path}")
        try:
            if not self.probe.trace_begin(os.fsencode(path)):
                raise OSError(f"Cannot open {path}")
            try:
                yield
            finally:
                self.probe.trace_end()
        finally:
            self.probe.trace_end_dispatch()

    def summarize(self, operation: str) -> dict[str, Any]:
        with (self.directory / f"{operation}.tsv").open() as stream:
            buffers = list(csv.DictReader(stream, delimiter="\t"))
        with (self.directory / f"{operation}-dispatch.tsv").open() as stream:
            dispatches = list(csv.DictReader(stream, delimiter="\t"))
        for buffer in buffers:
            if buffer["status"] != "4" or not (
                0 < float(buffer["gpu_start_s"]) < float(buffer["gpu_end_s"])
            ):
                raise RuntimeError(f"Invalid Metal completion for {operation}: {buffer}")
        return {
            "completed_buffers": len(buffers),
            "dispatches": len(dispatches),
            "devices": sorted({row["device"] for row in buffers}),
            "pipelines": sorted({row["pipeline"] for row in dispatches}),
        }


def run(request: dict[str, Any], output: Path) -> None:
    observer = (
        MetalObserver(Path(request["probe"]), output) if request.get("probe") is not None else None
    )
    engine = request["engine"]
    xgb, metadata = load_engine(engine)
    threads = request["threads"]
    parameters = {**request["parameters"], "device": engine, "nthread": threads}
    with np.load(request["dataset"], allow_pickle=False) as archive:
        arrays = dict(archive)
    digest = hashlib.sha256()
    for key in ("train", "test", "y_train", "y_test"):
        digest.update(memoryview(arrays[key]).cast("B"))
    metadata["dataset_sha256"] = digest.hexdigest()

    def call(operation: str, action: Callable[[], Any], trace: bool) -> tuple[Any, float]:
        with observer.observe(operation) if observer is not None and trace else nullcontext():
            return measure(action, no_sync)

    def predict() -> Any:
        return np.asarray(booster.inplace_predict(arrays["test"]))

    predictions = []
    with threadpool_limits(limits=threads):
        metadata["threadpools"] = threadpool_info()
        with (output / "measurements.jsonl").open("w") as stream:
            for index in range(2 if observer is not None else 1 + request["fit_repeats"]):
                train_matrix, train_ingest = measure(
                    lambda: xgb.DMatrix(arrays["train"], label=arrays["y_train"], nthread=threads),
                    no_sync,
                )
                booster, training = call(
                    "train",
                    partial(xgb.train, parameters, train_matrix, num_boost_round=request["rounds"]),
                    trace=index == 1,
                )
                first, first_prediction = measure(predict, no_sync)
                if index > 0:
                    predictions.append(first.copy())
                stream.write(
                    json.dumps(
                        {
                            "phase": "warmup" if index == 0 else "steady_fit",
                            "repetition": index,
                            "train_ingest_s": train_ingest,
                            "train_s": training,
                            "first_prediction_s": first_prediction,
                            "end_to_end_s": train_ingest + training + first_prediction,
                        },
                        allow_nan=False,
                    )
                    + "\n"
                )
                stream.flush()
                del train_matrix
            predict()
            prediction, elapsed = call("predict", predict, trace=True)
            np.testing.assert_array_equal(prediction, predictions[-1])
            if observer is None:
                times = [elapsed]
                for _ in range(request["predict_repeats"] - 1):
                    repeated, elapsed = measure(predict, no_sync)
                    np.testing.assert_array_equal(repeated, prediction)
                    times.append(elapsed)
                for index, elapsed in enumerate(times):
                    stream.write(
                        json.dumps(
                            {"phase": "steady_predict", "repetition": index, "predict_s": elapsed},
                            allow_nan=False,
                        )
                        + "\n"
                    )

    np.save(output / "prediction.npy", np.stack(predictions), allow_pickle=False)
    metadata["parameters"] = parameters
    metadata["process_peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * (
        1 if sys.platform == "darwin" else 1024
    )
    if observer is not None:
        metadata["metal_trace"] = {
            operation: observer.summarize(operation) for operation in ("train", "predict")
        }
    (output / "metadata.json").write_text(json.dumps(metadata, indent=2, allow_nan=False) + "\n")


if __name__ == "__main__":
    request_file, destination = map(Path, sys.argv[1:])
    run(json.loads(request_file.read_text()), destination)

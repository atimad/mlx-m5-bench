"""Replay one standard SVC or PCA case with operation-scoped Metal evidence."""

import argparse
import csv
import ctypes
import hashlib
import json
import os
import plistlib
import re
from collections.abc import Callable
from importlib.metadata import version
from pathlib import Path

import mlx.core as mx
import mlxlearn
from threadpoolctl import threadpool_limits

from mlx_m5_bench.config import Case, load_profile
from mlx_m5_bench.correctness import compare, extract
from mlx_m5_bench.datasets import generate
from mlx_m5_bench.estimators import create, parameters

CASES = {
    "svc": "svc-4000x256-c3",
    "pca": "pca-12000x256-c2-p8",
    "pca-small": "pca-2000x32-c2-p3",
}


def sync() -> None:
    mx.synchronize(mx.gpu)
    mx.synchronize(mx.cpu)


def observe(probe: ctypes.CDLL, path: Path, operation: Callable):
    sync()
    if not probe.trace_begin(os.fsencode(path)):
        raise OSError(f"Cannot open {path}")
    try:
        return operation()
    finally:
        probe.trace_end()


def summarize(path: Path) -> dict:
    with path.open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    intervals = []
    for row in rows:
        start, end = float(row["gpu_start_s"]), float(row["gpu_end_s"])
        if row["status"] != "4" or not 0 < start < end or row["device"] != "Apple M5 Pro":
            raise RuntimeError(f"Unexpected Metal completion in {path.name}: {row}")
        intervals.append(end - start)
    return {"completed_buffers": len(rows), "sum_gpu_buffer_ms": sum(intervals) * 1000}


def capture_operation(path: Path, operation: Callable) -> dict:
    sync()
    mx.metal.start_capture(str(path.resolve()))
    try:
        operation()
        sync()
    finally:
        mx.metal.stop_capture()
    metadata = plistlib.loads((path / "metadata").read_bytes())
    kernels = set()
    for artifact in path.iterdir():
        if not re.fullmatch(r"[A-F0-9]{16}", artifact.name) or not artifact.is_file():
            continue
        with artifact.open("rb") as stream:
            for word in re.findall(
                rb"(?:custom_kernel_mlxlearn_[A-Za-z0-9_]+)",
                stream.read(),
            ):
                kernels.add(word.decode("ascii"))
    with (path / "capture").open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    return {
        "captured_frames": metadata["DYCaptureEngine.captured_frames_count"],
        "capture_stream_sha256": digest,
        "selected_shader_symbols": sorted(kernels)[:20],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=CASES)
    parser.add_argument("output", type=Path)
    parser.add_argument("probe", type=Path)
    args = parser.parse_args()
    if os.environ.get("MTL_CAPTURE_ENABLED") != "1":
        parser.error("Start Python with MTL_CAPTURE_ENABLED=1")
    if os.environ.get("MLXLEARN_FORCE_BACKEND") != "mlx":
        parser.error("Set MLXLEARN_FORCE_BACKEND=mlx to match the benchmark")
    args.output.mkdir(parents=True, exist_ok=False)
    probe = ctypes.CDLL(str(args.probe.resolve()))
    probe.trace_begin.argtypes = [ctypes.c_char_p]
    probe.trace_end.restype = None
    if not probe.trace_install():
        raise RuntimeError("Unable to install Metal command buffer observer")

    profile = load_profile("standard")
    case: Case = next(case for case in profile.cases if case.key == CASES[args.case])
    data = generate(case, profile.seed)
    inference = "predict" if case.algorithm == "svc" else "transform"
    outputs = {}
    captures = {}
    with (
        threadpool_limits(limits=profile.threads),
        mlxlearn.config_context(
            device="gpu", fallback_policy="raise", deterministic=True, random_state=profile.seed
        ),
    ):
        for implementation in ("sklearn", "mlxlearn"):
            warm_model = create(case, implementation, profile.threads).fit(data.train, data.y_train)
            getattr(warm_model, inference)(data.test)
            model = create(case, implementation, profile.threads)
            observe(
                probe,
                args.output / f"{implementation}-fit.tsv",
                lambda model=model: model.fit(data.train, data.y_train),
            )
            result = observe(
                probe,
                args.output / f"{implementation}-{inference}.tsv",
                lambda model=model: getattr(model, inference)(data.test),
            )
            outputs[implementation] = extract(model, case.algorithm, data, result)

        # Capture separate replays. Fit and the first inference on the new model are isolated.
        captured_model = create(case, "mlxlearn", profile.threads)
        for name, operation in (
            ("fit", lambda: captured_model.fit(data.train, data.y_train)),
            (inference, lambda: getattr(captured_model, inference)(data.test)),
        ):
            if summarize(args.output / f"mlxlearn-{name}.tsv")["completed_buffers"]:
                captures[name] = capture_operation(args.output / f"{name}.gputrace", operation)
            else:
                operation()

    result = compare(case.algorithm, outputs["sklearn"], outputs["mlxlearn"], data)
    if result["status"] != "PASS":
        raise RuntimeError(f"Traced replay failed numerical parity: {result}")
    traces = {path.stem: summarize(path) for path in sorted(args.output.glob("*.tsv"))}
    if any(
        trace["completed_buffers"] for name, trace in traces.items() if name.startswith("sklearn")
    ):
        raise RuntimeError("The scikit-learn control submitted Metal commands")
    print(
        json.dumps(
            {
                "case": case.key,
                "dataset_sha256": data.fingerprint(),
                "seed": profile.seed,
                "threads": profile.threads,
                "parameters": parameters(case, profile.threads),
                "device": mx.device_info(),
                "dependencies": {
                    name: version(name) for name in ("mlx", "mlx-learn", "scikit-learn")
                },
                "correctness": result,
                "completion_traces": traces,
                "captures": captures,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

"""Capture Metal commands and independently measure command completion for one KNN case."""

import argparse
import ctypes
import hashlib
import json
import os
import plistlib
from importlib.metadata import version
from pathlib import Path

import mlx.core as mx
import mlxlearn
import numpy as np
from threadpoolctl import threadpool_limits

from mlx_m5_bench.config import Case
from mlx_m5_bench.datasets import generate
from mlx_m5_bench.estimators import create


def sync() -> None:
    mx.synchronize(mx.gpu)
    mx.synchronize(mx.cpu)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
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

    case = Case(algorithm="knn", samples=8000, features=128, classes=3)
    data = generate(case, 42)
    predictions = {}
    with (
        threadpool_limits(limits=4),
        mlxlearn.config_context(
            device="gpu", fallback_policy="raise", deterministic=True, random_state=42
        ),
    ):
        for implementation in ("sklearn", "mlxlearn"):
            model = create(case, implementation, 4).fit(data.train, data.y_train)
            warm = model.predict(data.test)
            sync()
            if not probe.trace_begin(os.fsencode(args.output / f"{implementation}.tsv")):
                raise OSError("Cannot open command completion trace")
            try:
                predictions[implementation] = model.predict(data.test)
            finally:
                probe.trace_end()
            sync()
            np.testing.assert_array_equal(warm, predictions[implementation])

        capture = args.output / "predict.gputrace"
        sync()
        mx.metal.start_capture(str(capture.resolve()))
        try:
            captured = model.predict(data.test)
            sync()
        finally:
            mx.metal.stop_capture()

    np.testing.assert_array_equal(captured, predictions["mlxlearn"])
    np.testing.assert_array_equal(captured, predictions["sklearn"])
    metadata = plistlib.loads((capture / "metadata").read_bytes())
    votes = b"custom_kernel_mlxlearn_neighbor_votes__2000_5_3"
    shaders = sorted(
        path.name
        for path in capture.iterdir()
        if len(path.name) == 16 and path.is_file() and votes in path.read_bytes()
    )
    print(
        json.dumps(
            {
                "case": case.key,
                "dataset_sha256": data.fingerprint(),
                "dependencies": {
                    name: version(name) for name in ("mlx", "mlx-learn", "scikit-learn")
                },
                "device": mx.device_info(),
                "matching_predictions": int(captured.size),
                "predictions_sha256": hashlib.sha256(captured.astype("<i8").tobytes()).hexdigest(),
                "captured_frames": metadata["DYCaptureEngine.captured_frames_count"],
                "vote_shader_artifacts": shaders,
                "capture_stream_sha256": hashlib.sha256(
                    (capture / "capture").read_bytes()
                ).hexdigest(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

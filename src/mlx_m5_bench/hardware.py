"""Host metadata and functional Metal probe."""

import inspect
import os
import platform
import re
import subprocess
import sys
from importlib.metadata import distributions
from typing import Any

import numpy as np
import psutil
from threadpoolctl import threadpool_info

from .estimators import ESTIMATORS


def command(*args: str) -> str | None:
    try:
        return subprocess.check_output(
            args, text=True, stderr=subprocess.DEVNULL, timeout=12
        ).strip()
    except (OSError, subprocess.SubprocessError):
        return None


def manifest() -> dict[str, Any]:
    import sklearn  # noqa: F401

    info: dict[str, Any] = {
        "system": platform.system(),
        "machine": platform.machine(),
        "os_version": platform.mac_ver()[0] or platform.release(),
        "logical_cpu": psutil.cpu_count(),
        "physical_cpu": psutil.cpu_count(logical=False),
        "memory_bytes": psutil.virtual_memory().total,
        "available_memory_bytes": psutil.virtual_memory().available,
        "load_average": os.getloadavg() if hasattr(os, "getloadavg") else None,
        "python": platform.python_version(),
        "dependencies": {d.metadata["Name"]: d.version for d in distributions()},
        "numpy_build": np.show_config(mode="dicts"),
        "threadpools": threadpool_info(),
        "thread_environment": {
            key: value
            for key, value in os.environ.items()
            if key
            in {
                "OMP_NUM_THREADS",
                "OPENBLAS_NUM_THREADS",
                "MKL_NUM_THREADS",
                "VECLIB_MAXIMUM_THREADS",
                "BLIS_NUM_THREADS",
            }
            or key.startswith("MLXLEARN_")
        },
        "git_commit": command("git", "rev-parse", "HEAD"),
        "git_dirty": bool(command("git", "status", "--porcelain")),
    }
    if sys.platform == "darwin":
        display = command("system_profiler", "SPDisplaysDataType") or ""
        cores = re.search(r"Total Number of Cores:\s*(\d+)", display)
        metal = re.search(r"Metal Support:\s*([^\n]+)", display)
        info.update(
            os_build=command("sw_vers", "-buildVersion"),
            chip=command("sysctl", "-n", "machdep.cpu.brand_string"),
            cpu_topology=command(
                "sysctl", "hw.perflevel0.physicalcpu", "hw.perflevel1.physicalcpu"
            ),
            gpu_cores=int(cores[1]) if cores else None,
            metal=metal[1].strip() if metal else None,
            power=(command("pmset", "-g", "batt") or "").splitlines()[:1],
            thermal=command("pmset", "-g", "therm"),
        )
    return info


def doctor() -> dict[str, Any]:
    from importlib import import_module

    info = manifest()
    info["metal_compute_probe"] = False
    info["host_compatible"] = sys.platform == "darwin" and platform.machine() == "arm64"
    info["python_compatible"] = sys.version_info[:2] == (3, 13)
    try:
        import mlx.core as mx
        import mlxlearn

        info["mlxlearn_gpu_available"] = mlxlearn.gpu_available()
        info["metal_available"] = mx.metal.is_available()
        info["estimator_signatures"] = {
            algorithm: str(inspect.signature(getattr(import_module(f"mlxlearn.{module}"), name)))
            for algorithm, (module, name) in ESTIMATORS.items()
        }
        if not info["metal_available"]:
            raise RuntimeError("Metal device unavailable")
        info["mlx_device"] = mx.device_info()
        with mx.stream(mx.gpu):
            x = mx.arange(4, dtype=mx.float32).reshape(2, 2)
            output = x @ x
            mx.eval(output)
            mx.synchronize(mx.gpu)
            np.testing.assert_array_equal(np.asarray(output), [[2, 3], [6, 11]])
        info["metal_compute_probe"] = True
    except (ImportError, RuntimeError, AttributeError, AssertionError) as error:
        info["gpu_probe_error"] = str(error)
        info["gpu_guidance"] = "Use native arm64 Python 3.13 on macOS and run uv sync --locked."
    return info

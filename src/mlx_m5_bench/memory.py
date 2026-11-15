"""Conservative admission checks and separate process and MLX allocator counters."""

import resource
import sys
from typing import Any

import psutil

from .config import Case
from .estimators import SVC_CACHE_MIB

MIB = 1024**2


def estimate_bytes(case: Case) -> int:
    train = case.samples - (case.samples + 3) // 4
    test = case.samples - train
    base = 512 * MIB + case.samples * (case.source_features or case.features) * 64
    if case.algorithm == "svc":
        base += min(4 * train**2, SVC_CACHE_MIB * MIB) * 4 + train * test * 16
    if case.algorithm == "pca":
        base += case.features**2 * 64
    if case.algorithm == "knn":
        base += min(train * test * 4, 256 * MIB) * 6
    return base


def admission(case: Case) -> tuple[int, int, str | None]:
    memory = psutil.virtual_memory()
    budget = int(min(memory.total * 0.35, memory.available * 0.6))
    estimate = estimate_bytes(case)
    if estimate > budget:
        return estimate, budget, "working-set estimate exceeds current memory budget"
    if case.algorithm == "svc" and (
        case.samples > 12_000 or case.samples**2 * case.features > 12_000_000_000
    ):
        return estimate, budget, "SVC quadratic work exceeds the configured safety ceiling"
    if case.algorithm == "knn" and case.samples**2 * case.features > 250_000_000_000:
        return estimate, budget, "brute-force KNN work exceeds the configured safety ceiling"
    return estimate, budget, None


def snapshot(mx: Any = None) -> dict[str, int]:
    counters = {
        "rss_bytes": psutil.Process().memory_info().rss,
        "process_peak_rss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        * (1 if sys.platform == "darwin" else 1024),
    }
    if mx is not None:
        counters.update(
            mlx_active_bytes=mx.get_active_memory(),
            mlx_peak_bytes=mx.get_peak_memory(),
            mlx_cache_bytes=mx.get_cache_memory(),
        )
    return counters

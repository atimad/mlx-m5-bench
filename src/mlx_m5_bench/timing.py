"""Synchronized wall-clock timings and robust summaries."""

from collections.abc import Callable, Iterable
from statistics import median
from time import perf_counter
from typing import Any


def measure(call: Callable[[], Any], synchronize: Callable[[], None]) -> tuple[Any, float]:
    synchronize()
    start = perf_counter()
    result = call()
    synchronize()
    return result, perf_counter() - start


def statistics(values: Iterable[float]) -> dict[str, float]:
    samples = list(values)
    center = median(samples)
    return {
        "median": center,
        "min": min(samples),
        "max": max(samples),
        "mad": median(abs(value - center) for value in samples),
    }

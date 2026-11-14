"""Operation-level backend classification for the pinned mlx-learn release."""

from typing import Any

CPU = "CPU_BASELINE"
FALLBACK = "CPU_FALLBACK"
MIXED = "MIXED_CPU_GPU_REPORTED"
GPU = "GPU_REPORTED_UNVERIFIED"
VERIFIED = "GPU_VERIFIED"
UNKNOWN = "UNKNOWN"
UNSUPPORTED = "UNSUPPORTED"


def classify(
    algorithm: str, operation: str, events: list[dict[str, Any]], *, pca_device: bool | None = None
) -> str:
    """Use final dispatch and source-audited exceptions to sticky-fit labels."""
    recorded_operation = (
        "kneighbors" if algorithm == "knn" and operation == "predict" else operation
    )
    decisions = [
        event["backend"]
        for event in events
        if event["operation"] in {operation, recorded_operation}
    ]
    if not decisions:
        return UNKNOWN
    if decisions[-1] in {"cpu", "sklearn"}:
        return FALLBACK
    if decisions[-1] != "mlx":
        return UNKNOWN
    if algorithm == "logistic":
        return MIXED if operation == "fit" else FALLBACK
    if algorithm == "pca":
        if operation == "fit":
            return MIXED
        if pca_device is None:
            return UNKNOWN
        return GPU if pca_device else FALLBACK
    if algorithm == "knn" and operation == "fit":
        return UNKNOWN  # Index construction and array staging do not prove GPU computation.
    if algorithm == "svc":
        return MIXED
    return GPU

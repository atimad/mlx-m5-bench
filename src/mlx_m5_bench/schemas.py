"""Version-one persisted measurement contract."""

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .diagnostics import CPU, FALLBACK, GPU, MIXED, UNKNOWN, UNSUPPORTED, VERIFIED

Backend = Literal[
    "CPU_BASELINE",
    "CPU_FALLBACK",
    "MIXED_CPU_GPU_REPORTED",
    "GPU_REPORTED_UNVERIFIED",
    "GPU_VERIFIED",
    "UNKNOWN",
    "UNSUPPORTED",
]
BACKENDS = {CPU, FALLBACK, GPU, MIXED, UNKNOWN, UNSUPPORTED, VERIFIED}


class Correctness(BaseModel):
    model_config = ConfigDict(extra="allow")
    status: Literal["PASS", "FAIL", "INCONCLUSIVE", "UNSUPPORTED"]


class Measurement(BaseModel):
    model_config = ConfigDict(extra="allow", allow_inf_nan=False)
    status: Literal["ok", "error", "timeout", "skipped", "unsupported"]
    phase: Literal["cold", "warmup", "steady"] | None = None
    backend: Backend | None = None
    fit_backend: Backend | None = None
    predict_backend: Backend | None = None
    transform_backend: Backend | None = None
    correctness: Correctness | None = None
    fit_s: float | None = Field(default=None, ge=0)
    predict_s: float | None = Field(default=None, ge=0)
    transform_s: float | None = Field(default=None, ge=0)
    pipeline_s: float | None = Field(default=None, ge=0)
    after: dict[str, Any] | None = None

    @model_validator(mode="after")
    def measured_operations(self) -> "Measurement":
        if self.status == "ok" and (
            self.fit_s is None
            or (self.predict_s is None and self.transform_s is None)
            or self.fit_backend is None
            or self.after is None
        ):
            raise ValueError("successful measurements require fit, inference and memory fields")
        return self

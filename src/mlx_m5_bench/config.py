"""Validated, packaged benchmark profiles."""

from importlib.resources import files
from pathlib import Path
from typing import Annotated, Literal, Self

import yaml
from pydantic import BaseModel, ConfigDict, Field, model_validator

Algorithm = Literal["logistic", "knn", "svc", "pca"]
Positive = Annotated[int, Field(gt=0)]


class Settings(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)


class Case(Settings):
    algorithm: Algorithm
    samples: Annotated[int, Field(ge=100, le=10_000_000)]
    features: Annotated[int, Field(ge=4, le=8192)]
    classes: Literal[2, 3] = 2
    neighbors: Positive = 5
    components: Positive = 3
    query_rows: Positive | None = None

    @model_validator(mode="after")
    def dimensions(self) -> Self:
        train = self.samples - (self.samples + 3) // 4
        if self.query_rows is not None and (
            self.algorithm != "knn" or self.query_rows > self.samples - train
        ):
            raise ValueError("query_rows requires KNN and must fit within the test set")
        if self.algorithm == "knn" and self.neighbors > train:
            raise ValueError("neighbors must fit within the training set")
        if self.algorithm == "pca" and self.components > min(train, self.features):
            raise ValueError("components must fit within the training dimensions")
        return self

    @property
    def key(self) -> str:
        return f"{self.algorithm}-{self.samples}x{self.features}-c{self.classes}" + {
            "knn": f"-k{self.neighbors}" + (f"-q{self.query_rows}" if self.query_rows else ""),
            "pca": f"-p{self.components}",
        }.get(self.algorithm, "")


class Profile(Settings):
    seed: Annotated[int, Field(ge=0, le=2**32 - 1)] = 42
    repeats: Annotated[int, Field(ge=1, le=30)]
    warmups: Annotated[int, Field(ge=0, le=10)] = 1
    threads: Annotated[int, Field(ge=1, le=128)] = 4
    timeout_s: Positive = 180
    reuse_model: bool = False
    force_mlx: bool = True
    mlx_device: Literal["gpu", "auto", "cpu"] = "gpu"
    cases: Annotated[list[Case], Field(min_length=1)]

    @model_validator(mode="after")
    def unique_cases(self) -> Self:
        if self.reuse_model and any(case.algorithm != "knn" for case in self.cases):
            raise ValueError("reuse_model currently requires KNN workloads")
        if self.force_mlx and self.mlx_device != "gpu":
            raise ValueError("force_mlx requires mlx_device=gpu")
        if len({case.key for case in self.cases}) != len(self.cases):
            raise ValueError("duplicate workload")
        return self


def load_profile(name: str, path: Path | None = None) -> Profile:
    source = path or files("mlx_m5_bench").joinpath("configs", f"{name}.yaml")
    return Profile.model_validate(yaml.safe_load(source.read_text(encoding="utf-8")))

"""Deterministic inputs with train-only preprocessing."""

import hashlib
from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from .config import Case


@dataclass(frozen=True)
class Dataset:
    train: NDArray[np.float32]
    test: NDArray[np.float32]
    y_train: NDArray[np.int64]
    y_test: NDArray[np.int64]

    def fingerprint(self) -> str:
        digest = hashlib.sha256()
        for array in (self.train, self.test, self.y_train, self.y_test):
            digest.update(memoryview(array).cast("B"))
        return digest.hexdigest()


def generate(case: Case, seed: int) -> Dataset:
    if case.algorithm == "pca":
        rng = np.random.default_rng(seed)
        # An anisotropic spectrum with cross-feature correlation and a rank cutoff.
        X = rng.standard_normal((case.samples, case.features))
        X *= np.geomspace(4.0, 0.3, case.features)
        X[:, 1:] += 0.4 * X[:, :-1]
        y = np.zeros(case.samples, dtype=np.int64)
        stratify = None
    else:
        source_features = case.source_features or case.features
        X, y = make_classification(
            n_samples=case.samples,
            n_features=source_features,
            n_informative=max(3, source_features // 2),
            n_redundant=0,
            n_classes=case.classes,
            n_clusters_per_class=1,
            random_state=seed,
        )
        X = X[:, : case.features]
        stratify = y
    train, test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed, stratify=stratify
    )
    if case.train_rows is not None:
        train = train[: case.train_rows]
        y_train = y_train[: case.train_rows]
    if case.algorithm != "pca":
        scaler = StandardScaler(copy=False).fit(train)
        train, test = scaler.transform(train), scaler.transform(test)
    if case.query_rows is not None:
        test = test[: case.query_rows]
        y_test = y_test[: case.query_rows]
    return Dataset(
        np.ascontiguousarray(train, dtype=np.float32),
        np.ascontiguousarray(test, dtype=np.float32),
        np.ascontiguousarray(y_train, dtype=np.int64),
        np.ascontiguousarray(y_test, dtype=np.int64),
    )

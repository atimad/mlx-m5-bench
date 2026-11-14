"""Explicit estimator adapters. Each comparison uses shared public parameters."""

from importlib import import_module
from typing import Any

from .config import Case

ESTIMATORS = {
    "logistic": ("linear_model", "LogisticRegression"),
    "knn": ("neighbors", "KNeighborsClassifier"),
    "svc": ("svm", "SVC"),
    "pca": ("decomposition", "PCA"),
}
SVC_CACHE_MIB = 64


def parameters(case: Case, threads: int) -> dict[str, Any]:
    return {
        "logistic": dict(solver="lbfgs", C=1.0, tol=1e-5, max_iter=300, class_weight=None),
        "knn": dict(
            n_neighbors=case.neighbors,
            algorithm="brute",
            metric="euclidean",
            weights="uniform",
            n_jobs=threads,
        ),
        "svc": dict(
            kernel="rbf",
            gamma=1 / case.features,
            C=1.0,
            tol=1e-3,
            cache_size=SVC_CACHE_MIB,
            max_iter=100_000,
            shrinking=False,
            decision_function_shape="ovo",
            class_weight=None,
        ),
        "pca": dict(n_components=case.components, svd_solver="covariance_eigh", whiten=False),
    }[case.algorithm]


def create(case: Case, implementation: str, threads: int) -> Any:
    module, name = ESTIMATORS[case.algorithm]
    estimator = getattr(import_module(f"{implementation}.{module}"), name)
    return estimator(**parameters(case, threads))

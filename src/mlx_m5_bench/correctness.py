"""Compare aligned predictions and PCA subspaces outside timed operations."""

from typing import Any

import numpy as np

from .datasets import Dataset


def extract(model: Any, algorithm: str, data: Dataset, output: Any) -> dict[str, Any]:
    result: dict[str, Any] = {"output": np.asarray(output)}
    if algorithm == "pca":
        result.update(
            components=np.asarray(model.components_),
            variance=np.asarray(model.explained_variance_ratio_),
            reconstruction=np.asarray(model.inverse_transform(output)),
        )
    else:
        result["classes"] = np.asarray(model.classes_)
    if algorithm in {"logistic", "knn"}:
        result["probabilities"] = np.asarray(model.predict_proba(data.test))
    if algorithm == "svc":
        result["decision"] = np.asarray(model.decision_function(data.test))
        result["support_count"] = np.asarray(len(model.support_))
    if hasattr(model, "n_iter_"):
        result["iterations"] = np.asarray(model.n_iter_)
    return result


def compare(
    algorithm: str, cpu: dict[str, Any], candidate: dict[str, Any], data: Dataset
) -> dict[str, Any]:
    if (
        cpu.keys() != candidate.keys()
        or any(
            not np.isfinite(value).all()
            for results in (cpu, candidate)
            for value in results.values()
        )
        or any(cpu[key].shape != candidate[key].shape for key in cpu if key not in {"iterations"})
    ):
        return {"status": "FAIL", "reason": "non-finite, missing or incompatible outputs"}

    if algorithm == "pca":
        # QR normalizes the basis. Singular values are invariant to signs and rotations.
        lhs = np.linalg.qr(cpu["components"].astype(np.float64).T)[0]
        rhs = np.linalg.qr(candidate["components"].astype(np.float64).T)[0]
        cosine = float(np.linalg.svd(lhs.T @ rhs, compute_uv=False).min())
        rmse_cpu = float(np.sqrt(np.mean((data.test - cpu["reconstruction"]) ** 2)))
        rmse_candidate = float(np.sqrt(np.mean((data.test - candidate["reconstruction"]) ** 2)))
        variance_error = abs(float(cpu["variance"].sum() - candidate["variance"].sum()))
        passed = (
            cosine >= 0.99
            and abs(rmse_cpu - rmse_candidate) <= max(1e-6, 0.01 * rmse_cpu)
            and variance_error <= 0.005
        )
        return {
            "status": "PASS" if passed else "FAIL",
            "min_principal_cosine": cosine,
            "cpu_rmse": rmse_cpu,
            "candidate_rmse": rmse_candidate,
            "cpu_retained_variance": float(cpu["variance"].sum()),
            "candidate_retained_variance": float(candidate["variance"].sum()),
        }

    cpu_accuracy = float(np.mean(cpu["output"] == data.y_test))
    candidate_accuracy = float(np.mean(candidate["output"] == data.y_test))
    agreement = float(np.mean(cpu["output"] == candidate["output"]))
    passed = (
        np.array_equal(cpu["classes"], candidate["classes"])
        and agreement >= 0.99
        and abs(cpu_accuracy - candidate_accuracy) <= 0.01
    )
    metrics: dict[str, Any] = {
        "cpu_accuracy": cpu_accuracy,
        "candidate_accuracy": candidate_accuracy,
        "agreement": agreement,
    }
    if "probabilities" in cpu:
        difference = np.abs(cpu["probabilities"] - candidate["probabilities"])
        metrics.update(
            probability_mae=float(difference.mean()), probability_max=float(difference.max())
        )
        passed = passed and difference.mean() <= 0.005 and difference.max() <= 0.05
        for values in (cpu["probabilities"], candidate["probabilities"]):
            passed = passed and bool(
                np.all((values >= 0) & (values <= 1))
                and np.allclose(values.sum(axis=1), 1, atol=1e-5)
            )
    if "decision" in cpu:
        discrepancy = float(np.max(np.abs(cpu["decision"] - candidate["decision"])))
        metrics.update(
            decision_max_error=discrepancy,
            cpu_support_count=int(cpu["support_count"]),
            candidate_support_count=int(candidate["support_count"]),
        )
        passed = passed and discrepancy <= 0.05
    return {"status": "PASS" if passed else "FAIL", **metrics}

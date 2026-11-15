"""Run one implementation in an isolated process, optionally reusing the fitted model."""

import json
import os
import sys
import traceback
import warnings
from contextlib import ExitStack
from importlib import import_module
from pathlib import Path
from time import perf_counter
from typing import Any

import numpy as np
from sklearn.exceptions import ConvergenceWarning
from threadpoolctl import threadpool_info, threadpool_limits

from .config import Case, Profile
from .correctness import extract
from .datasets import generate
from .diagnostics import CPU, UNKNOWN, UNSUPPORTED, classify
from .estimators import create
from .memory import snapshot
from .timing import measure


def no_sync() -> None:
    pass


def bench(
    case: Case,
    profile: Profile,
    implementation: str,
    output: Path,
) -> None:
    candidate = implementation == "mlxlearn"
    mx: Any = None
    mlxlearn: Any = None
    synchronize = no_sync
    with ExitStack() as stack:
        if candidate:
            try:
                mx = import_module("mlx.core")
                mlxlearn = import_module("mlxlearn")

                if not mx.metal.is_available():
                    raise RuntimeError("Metal unavailable")
            except (ImportError, RuntimeError) as error:
                write_row(
                    output, {"status": "unsupported", "backend": UNSUPPORTED, "error": str(error)}
                )
                return
            stack.enter_context(
                mlxlearn.config_context(
                    device=profile.mlx_device,
                    fallback_policy="raise",
                    diagnostics=True,
                    deterministic=True,
                    random_state=profile.seed,
                )
            )

            def synchronize() -> None:
                mx.synchronize(mx.gpu)
                mx.synchronize(mx.cpu)

        # Discover estimator-linked runtimes before applying limits.
        model = create(case, implementation, profile.threads)
        del model
        stack.enter_context(threadpool_limits(limits=profile.threads))
        pools = threadpool_info()
        data, prep_s = measure(lambda: generate(case, profile.seed), no_sync)
        fingerprint = data.fingerprint()
        fitted_model = None
        predictions: dict[int, Any] = {}
        for index in range(1 + profile.warmups + profile.repeats):
            phase = "cold" if index == 0 else "warmup" if index <= profile.warmups else "steady"
            row: dict[str, Any] = {
                "repetition": index,
                "phase": phase,
                "prep_s": prep_s,
                "dataset_sha256": fingerprint,
            }
            if index == 0:
                row["threadpools"] = pools
            events: list[dict[str, Any]] = []
            try:
                before = snapshot(mx)
                if candidate:
                    mx.reset_peak_memory()
                with warnings.catch_warnings(record=True) as notes:
                    warnings.simplefilter("always")
                    start = perf_counter()
                    model = (
                        fitted_model
                        if profile.reuse_model and fitted_model is not None
                        else create(case, implementation, profile.threads)
                    )
                    operations = {
                        "fit": lambda model=model: model.fit(data.train, data.y_train),
                        "transform" if case.algorithm == "pca" else "predict": (
                            lambda model=model: (
                                model.transform(data.test)
                                if case.algorithm == "pca"
                                else model.predict(data.test)
                            )
                        ),
                    }
                    if profile.reuse_model and fitted_model is not None:
                        del operations["fit"]
                    row["reused_model"] = "fit" not in operations
                    for operation, call in operations.items():
                        if candidate:
                            mlxlearn.clear_backend_diagnostics()
                        result, elapsed = measure(call, synchronize)
                        row[f"{operation}_s"] = elapsed
                        if candidate:
                            scoped = [e.as_dict() for e in mlxlearn.get_backend_diagnostics()]
                            events.extend(scoped)
                            pca_device = None
                            if operation == "transform":
                                from mlxlearn._solvers.pca import pca_transform_uses_gpu

                                pca_device = pca_transform_uses_gpu(
                                    data.test, model.mean_, model.explained_variance_
                                )
                            row[f"{operation}_backend"] = classify(
                                case.algorithm,
                                operation,
                                scoped,
                                pca_device=pca_device,
                            )
                        else:
                            row[f"{operation}_backend"] = CPU
                    if profile.reuse_model:
                        fitted_model = model
                    row["pipeline_s"] = perf_counter() - start
                    row["before"] = before
                    row["after"] = snapshot(mx)
                    if profile.reuse_model and phase in {"cold", "steady"}:
                        predictions[index] = result
                    elif phase in {"cold", "steady"}:
                        values = extract(model, case.algorithm, data, result)
                        synchronize()
                        np.savez(output.parent / f"{implementation}-{index}.npz", **values)
                        if "iterations" in values:
                            row["iterations"] = values["iterations"].tolist()
                row["warnings"] = [str(note.message) for note in notes]
                row["converged"] = not any(
                    issubclass(note.category, ConvergenceWarning) for note in notes
                ) and not bool(getattr(model, "fit_status_", 0))
                row["status"] = "ok"
                del model, result, operations
            except Exception as error:
                unsupported = candidate and isinstance(error, mlxlearn.CapabilityError)
                row.update(
                    status="unsupported" if unsupported else "error",
                    backend=UNSUPPORTED if unsupported else UNKNOWN,
                    error=traceback.format_exc(),
                )
                if candidate:
                    row["failed_operation_events"] = [
                        e.as_dict() for e in mlxlearn.get_backend_diagnostics()
                    ]
            row["events"] = events
            write_row(output, row)
        if profile.reuse_model and predictions:
            # Defer ancillary inference so steady calls only warm the measured operation.
            values = extract(fitted_model, case.algorithm, data, next(iter(predictions.values())))
            synchronize()
            for index, prediction in predictions.items():
                values["output"] = np.asarray(prediction)
                np.savez(output.parent / f"{implementation}-{index}.npz", **values)


def write_row(path: Path, row: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, default=str, allow_nan=False) + "\n")


def main() -> None:
    request = json.loads(Path(sys.argv[1]).read_text())
    profile = Profile.model_validate(request["profile"])
    implementation = request["implementation"]
    # Set before mlxlearn is first imported. Explicit config alone leaves size-based CPU routing.
    if implementation == "mlxlearn" and profile.force_mlx:
        os.environ["MLXLEARN_FORCE_BACKEND"] = "mlx"
    output = Path(sys.argv[2])
    try:
        bench(Case.model_validate(request["case"]), profile, implementation, output)
    except Exception:
        write_row(output, {"status": "error", "backend": UNKNOWN, "error": traceback.format_exc()})


if __name__ == "__main__":
    main()

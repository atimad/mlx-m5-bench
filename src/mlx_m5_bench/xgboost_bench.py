"""Benchmark CPU XGBoost and xgboost-metal without importing either in the coordinator."""

import argparse
import json
import os
import subprocess
from itertools import product
from pathlib import Path
from typing import Any

import numpy as np
from sklearn.datasets import make_classification, make_friedman1
from sklearn.metrics import log_loss, roc_auc_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

from .datasets import Dataset
from .diagnostics import CPU, GPU, VERIFIED
from .hardware import manifest
from .runner import write_json
from .timing import statistics

TASKS = {"classification": "binary:logistic", "regression": "reg:squarederror"}
SEED = 42
SAMPLES = 100_000
TRAIN_ROWS = SAMPLES * 3 // 4
TEST_ROWS = SAMPLES - TRAIN_ROWS
FEATURES = 32
ROUNDS = 100
FIT_REPEATS = 3
PREDICT_REPEATS = 10
BATCH_REPEATS = 30
PARAMETERS = {
    "tree_method": "hist",
    "max_depth": 6,
    "max_bin": 256,
    "eta": 0.1,
    "min_child_weight": 1,
    "lambda": 1,
    "alpha": 0,
    "gamma": 0,
    "subsample": 1,
    "colsample_bytree": 1,
    "seed": SEED,
}
THRESHOLDS = {
    "classification": {"log_loss": 0.02, "roc_auc": 0.01},
    "regression": {"rmse": 0.05},
}


def dataset(task: str, samples: int = SAMPLES) -> Dataset:
    if task == "classification":
        x, y = make_classification(
            n_samples=samples,
            n_features=FEATURES,
            n_informative=16,
            n_redundant=4,
            random_state=SEED,
        )
    else:
        x, y = make_friedman1(n_samples=samples, n_features=FEATURES, noise=1, random_state=SEED)
    train, test, y_train, y_test = train_test_split(
        x, y, test_size=0.25, random_state=SEED, stratify=y if task == "classification" else None
    )
    return Dataset(
        np.ascontiguousarray(train, dtype=np.float32),
        np.ascontiguousarray(test, dtype=np.float32),
        np.ascontiguousarray(y_train, dtype=np.float32 if task == "regression" else np.int64),
        np.ascontiguousarray(y_test, dtype=np.float32 if task == "regression" else np.int64),
    )


def with_features(data: Dataset, features: int) -> Dataset:
    """Append nested, independent noise columns to the original feature matrix."""
    if features == FEATURES:
        return data

    def extend(values: np.ndarray, seed: int) -> np.ndarray:
        extra = np.random.default_rng(seed).standard_normal(
            (features - FEATURES, len(values)), dtype=np.float32
        )
        result = np.empty((len(values), features), dtype=np.float32)
        result[:, :FEATURES] = values
        result[:, FEATURES:] = extra.T
        return result

    return Dataset(
        extend(data.train, SEED + 1), extend(data.test, SEED + 2), data.y_train, data.y_test
    )


def quality(task: str, labels: np.ndarray, cpu: np.ndarray, metal: np.ndarray) -> dict[str, Any]:
    for name, values in (("cpu", cpu), ("metal", metal)):
        if values.shape != labels.shape or not np.isfinite(values).all():
            return {"status": "FAIL", "reason": f"{name} predictions have invalid shape or values"}
        if task == "classification" and not ((0 <= values) & (values <= 1)).all():
            return {"status": "FAIL", "reason": f"{name} probabilities outside [0, 1]"}
    if task == "classification":
        scores = {
            name: {"log_loss": log_loss(labels, values), "roc_auc": roc_auc_score(labels, values)}
            for name, values in (("cpu", cpu), ("metal", metal))
        }
        differences = {
            metric: abs(scores["cpu"][metric] - scores["metal"][metric])
            for metric in THRESHOLDS[task]
        }
    else:
        scores = {
            name: {"rmse": root_mean_squared_error(labels, values)}
            for name, values in (("cpu", cpu), ("metal", metal))
        }
        baseline = scores["cpu"]["rmse"]
        differences = {"rmse": abs(baseline - scores["metal"]["rmse"]) / max(baseline, 1e-12)}
    passed = all(
        difference <= THRESHOLDS[task][metric] for metric, difference in differences.items()
    )
    result = {"status": "PASS" if passed else "FAIL", **scores, "differences": differences}
    return result


def worker(
    executable: Path, request: dict[str, Any], directory: Path
) -> tuple[dict[str, Any], list[dict[str, Any]], np.ndarray]:
    directory.mkdir()
    request_path = directory / "request.json"
    write_json(request_path, request)
    env = dict(os.environ)
    env.pop("MTL_CAPTURE_ENABLED", None)
    if request["probe"]:
        env["MTL_CAPTURE_ENABLED"] = "1"
    for variable in (
        "OMP_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS",
        "OPENBLAS_NUM_THREADS",
        "MKL_NUM_THREADS",
        "BLIS_NUM_THREADS",
    ):
        env[variable] = str(request["threads"])
    log_path = directory / "worker.log"
    with log_path.open("w") as log:
        try:
            subprocess.run(
                [
                    str(executable),
                    "-E",
                    "-s",
                    "-m",
                    "mlx_m5_bench.xgboost_worker",
                    str(request_path),
                    str(directory),
                ],
                cwd=Path(__file__).resolve().parents[1],
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=300,
                env=env,
                check=True,
            )
        except (subprocess.SubprocessError, OSError) as error:
            raise RuntimeError(f"XGBoost worker failed. See {log_path}") from error
    metadata = json.loads((directory / "metadata.json").read_text())
    rows = [
        json.loads(line) for line in (directory / "measurements.jsonl").read_text().splitlines()
    ]
    predictions = np.load(directory / "prediction.npy", allow_pickle=False)
    (directory / "prediction.npy").unlink()
    return metadata, rows, predictions


def verify_trace(
    engine: str,
    metadata: dict[str, Any],
    chip: str,
    operations: tuple[str, ...] = ("train", "predict"),
) -> str:
    for operation in operations:
        trace = metadata["metal_trace"][operation]
        if engine == "cpu":
            valid = trace["completed_buffers"] == trace["dispatches"] == 0
        else:
            valid = (
                trace["completed_buffers"] > 0
                and trace["dispatches"] > 0
                and trace["devices"] == [chip]
                and any(name != "<unlabeled>" for name in trace["pipelines"])
            )
        if not valid:
            raise RuntimeError(f"Unexpected Metal trace for {engine} {operation}: {trace}")
    return VERIFIED if engine == "metal" else CPU


def run(
    output: Path,
    interpreters: dict[str, Path],
    threads: int,
    probe: Path | None = None,
    train_sizes: tuple[int, ...] = (TRAIN_ROWS,),
    query_sizes: tuple[int, ...] = (),
    feature_counts: tuple[int, ...] = (),
) -> bool:
    if not train_sizes or len(set(train_sizes)) != len(train_sizes):
        raise ValueError("Training sizes must be nonempty and distinct")
    if any(not 2 <= size <= TRAIN_ROWS for size in train_sizes):
        raise ValueError(f"Training sizes must be between 2 and {TRAIN_ROWS}")
    if len(set(query_sizes)) != len(query_sizes) or any(
        not 1 <= size <= TEST_ROWS for size in query_sizes
    ):
        raise ValueError(f"Query sizes must be distinct and between 1 and {TEST_ROWS}")
    if query_sizes and train_sizes != (TRAIN_ROWS,):
        raise ValueError("The prediction batch sweep uses the full training split")
    if len(set(feature_counts)) != len(feature_counts) or any(
        count < FEATURES for count in feature_counts
    ):
        raise ValueError(f"Feature counts must be distinct and at least {FEATURES}")
    if feature_counts and (query_sizes or train_sizes != (TRAIN_ROWS,)):
        raise ValueError("The feature sweep uses the full training and prediction splits")
    widths = feature_counts or (FEATURES,)
    predict_repeats = BATCH_REPEATS if query_sizes else PREDICT_REPEATS
    operations = tuple(f"predict-q{size}" for size in query_sizes) or ("train", "predict")
    output = output.resolve()
    output.mkdir(parents=True)
    experiment = manifest()
    experiment.update(
        experiment="xgboost",
        mode="metal_trace" if probe is not None else "timing",
        seed=SEED,
        threads=threads,
        samples=SAMPLES,
        features=FEATURES,
        train_sizes=train_sizes,
        query_rows=TEST_ROWS,
        boosting_rounds=ROUNDS,
        fit_repeats_per_block=0 if query_sizes else 1 if probe is not None else FIT_REPEATS,
        predict_repeats_per_block=1 if probe is not None else predict_repeats,
        quality_thresholds=THRESHOLDS,
        blocks=[],
        state="running",
    )
    if query_sizes:
        experiment["query_sizes"] = query_sizes
    if feature_counts:
        experiment.pop("features")
        experiment.update(base_features=FEATURES, feature_counts=feature_counts)
    write_json(output / "manifest.json", experiment)
    measurements: list[dict[str, Any]] = []
    comparisons: list[dict[str, Any]] = []
    orders = [("cpu", "metal")] if probe is not None else [("cpu", "metal"), ("metal", "cpu")]
    datasets = {task: dataset(task) for task in TASKS}
    for task, size, width in product(TASKS, train_sizes, widths):
        full = with_features(datasets[task], width)
        data = Dataset(full.train[:size], full.test, full.y_train[:size], full.y_test)
        if task == "classification" and np.unique(data.y_train).size != 2:
            raise ValueError(f"The {size}-row training prefix requires both classes")
        fingerprint = data.fingerprint()
        task_path = output / task
        if train_sizes != (TRAIN_ROWS,):
            task_path /= f"train-{size}"
        if feature_counts:
            task_path /= f"features-{width}"
        task_path.mkdir(parents=True)
        data_path = task_path / "data.npz"
        np.savez(
            data_path,
            train=data.train,
            test=data.test,
            y_train=data.y_train,
            y_test=data.y_test,
        )
        try:
            for pass_index, order in enumerate(orders, start=1):
                block = {"task": task, "train_rows": size, "pass": pass_index}
                if feature_counts:
                    block["features"] = width
                outputs: dict[str, np.ndarray] = {}
                for engine in order:
                    print(
                        f"{task} train={size} features={width} pass {pass_index} {engine}",
                        flush=True,
                    )
                    request = {
                        "engine": engine,
                        "dataset": str(data_path),
                        "threads": threads,
                        "parameters": {**PARAMETERS, "objective": TASKS[task]},
                        "rounds": ROUNDS,
                        "fit_repeats": FIT_REPEATS,
                        "predict_repeats": predict_repeats,
                        "probe": str(probe.resolve()) if probe is not None else None,
                    }
                    if query_sizes:
                        request["query_sizes"] = (
                            query_sizes if pass_index == 1 else query_sizes[::-1]
                        )
                    directory = task_path / f"pass-{pass_index}-{engine}"
                    metadata, rows, outputs[engine] = worker(
                        interpreters[engine], request, directory
                    )
                    if metadata["dataset_sha256"] != fingerprint:
                        raise RuntimeError(f"Input fingerprint mismatch for {task} {engine}")
                    backend = GPU if engine == "metal" else CPU
                    if probe is not None:
                        backend = verify_trace(engine, metadata, experiment["chip"], operations)
                    experiment["blocks"].append(
                        {**block, "engine": engine, "backend": backend, **metadata}
                    )
                    if probe is None:
                        measurements.extend({**block, "engine": engine, **row} for row in rows)
                        write_json(output / "measurements.json", measurements)
                    write_json(output / "manifest.json", experiment)
                for index, (cpu, metal) in enumerate(
                    zip(outputs["cpu"], outputs["metal"], strict=True), start=1
                ):
                    comparisons.append(
                        {**block, "repetition": index, **quality(task, data.y_test, cpu, metal)}
                    )
                write_json(output / "correctness.json", comparisons)
        except BaseException:
            experiment["state"] = "interrupted"
            write_json(output / "manifest.json", experiment)
            raise
        finally:
            data_path.unlink()

    metrics = (
        ("predict_s",)
        if query_sizes
        else ("train_ingest_s", "train_s", "first_prediction_s", "end_to_end_s", "predict_s")
    )
    summary = [
        {
            "task": task,
            "train_rows": size,
            "engine": engine,
            **({"query_rows": query_rows} if query_rows is not None else {}),
            **({"features": width} if feature_counts else {}),
            **{
                metric: statistics(
                    row[metric]
                    for row in measurements
                    if row["task"] == task
                    and row["train_rows"] == size
                    and row["engine"] == engine
                    and row.get("query_rows") == query_rows
                    and row.get("features", FEATURES) == width
                    and row["phase"] != "warmup"
                    and metric in row
                )
                for metric in metrics
            },
        }
        for task in TASKS
        for size in train_sizes
        for engine in interpreters
        for width in widths
        for query_rows in query_sizes or (None,)
        if probe is None
    ]
    write_json(output / "summary.json", summary)
    experiment["state"] = "complete"
    write_json(output / "manifest.json", experiment)
    return all(row["status"] == "PASS" for row in comparisons)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cpu-python", required=True, type=Path)
    parser.add_argument("--metal-python", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--threads", type=int, default=4)
    parser.add_argument(
        "--probe", type=Path, help="Run a separate replay using a compiled observer"
    )
    sweep = parser.add_mutually_exclusive_group()
    sweep.add_argument(
        "--train-rows",
        type=int,
        nargs="+",
        default=[TRAIN_ROWS],
        help="Training-prefix sizes, with the original test batch fixed",
    )
    sweep.add_argument(
        "--query-rows", type=int, nargs="+", default=[], help="Prediction sizes on one fitted model"
    )
    sweep.add_argument(
        "--features", type=int, nargs="+", default=[], help="Feature counts with fixed row splits"
    )
    args = parser.parse_args()
    if args.threads < 1:
        parser.error("--threads must be positive")
    # Keep virtualenv symlinks intact so Python locates each environment's pyvenv.cfg.
    interpreters = {"cpu": args.cpu_python.absolute(), "metal": args.metal_python.absolute()}
    if not run(
        args.output,
        interpreters,
        args.threads,
        args.probe,
        tuple(args.train_rows),
        tuple(args.query_rows),
        tuple(args.features),
    ):
        raise SystemExit("Quality checks failed. See correctness.json in the output directory.")


if __name__ == "__main__":
    main()

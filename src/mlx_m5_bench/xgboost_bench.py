"""Benchmark CPU XGBoost and xgboost-metal without importing either in the coordinator."""

import argparse
import json
import os
import subprocess
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
FEATURES = 32
ROUNDS = 100
FIT_REPEATS = 3
PREDICT_REPEATS = 10
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


def verify_trace(engine: str, metadata: dict[str, Any], chip: str) -> str:
    for operation in ("train", "predict"):
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
    output: Path, interpreters: dict[str, Path], threads: int, probe: Path | None = None
) -> bool:
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
        boosting_rounds=ROUNDS,
        fit_repeats_per_block=1 if probe is not None else FIT_REPEATS,
        predict_repeats_per_block=1 if probe is not None else PREDICT_REPEATS,
        quality_thresholds=THRESHOLDS,
        blocks=[],
        state="running",
    )
    write_json(output / "manifest.json", experiment)
    measurements: list[dict[str, Any]] = []
    comparisons: list[dict[str, Any]] = []
    orders = [("cpu", "metal")] if probe is not None else [("cpu", "metal"), ("metal", "cpu")]
    for task, objective in TASKS.items():
        data = dataset(task)
        fingerprint = data.fingerprint()
        task_path = output / task
        task_path.mkdir()
        data_path = task_path / "data.npz"
        np.savez(
            data_path, train=data.train, test=data.test, y_train=data.y_train, y_test=data.y_test
        )
        try:
            for pass_index, order in enumerate(orders, start=1):
                block = {"task": task, "pass": pass_index}
                outputs: dict[str, np.ndarray] = {}
                for engine in order:
                    print(f"{task} pass {pass_index} {engine}", flush=True)
                    request = {
                        "engine": engine,
                        "dataset": str(data_path),
                        "threads": threads,
                        "parameters": {**PARAMETERS, "objective": objective},
                        "rounds": ROUNDS,
                        "fit_repeats": FIT_REPEATS,
                        "predict_repeats": PREDICT_REPEATS,
                        "probe": str(probe.resolve()) if probe is not None else None,
                    }
                    directory = task_path / f"pass-{pass_index}-{engine}"
                    metadata, rows, outputs[engine] = worker(
                        interpreters[engine], request, directory
                    )
                    if metadata["dataset_sha256"] != fingerprint:
                        raise RuntimeError(f"Input fingerprint mismatch for {task} {engine}")
                    backend = GPU if engine == "metal" else CPU
                    if probe is not None:
                        backend = verify_trace(engine, metadata, experiment["chip"])
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

    metrics = ("train_ingest_s", "train_s", "first_prediction_s", "end_to_end_s", "predict_s")
    summary = [
        {
            "task": task,
            "engine": engine,
            **{
                metric: statistics(
                    row[metric]
                    for row in measurements
                    if row["task"] == task
                    and row["engine"] == engine
                    and row["phase"] != "warmup"
                    and metric in row
                )
                for metric in metrics
            },
        }
        for task in TASKS
        for engine in interpreters
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
    args = parser.parse_args()
    if args.threads < 1:
        parser.error("--threads must be positive")
    # Keep virtualenv symlinks intact so Python locates each environment's pyvenv.cfg.
    interpreters = {"cpu": args.cpu_python.absolute(), "metal": args.metal_python.absolute()}
    if not run(args.output, interpreters, args.threads, args.probe):
        raise SystemExit("Quality checks failed. See correctness.json in the output directory.")


if __name__ == "__main__":
    main()

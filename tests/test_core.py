import json
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
from pydantic import ValidationError
from threadpoolctl import threadpool_limits

from mlx_m5_bench.config import Case, Profile, load_profile
from mlx_m5_bench.correctness import compare, extract
from mlx_m5_bench.datasets import generate
from mlx_m5_bench.diagnostics import (
    CPU,
    FALLBACK,
    GPU,
    MIXED,
    UNKNOWN,
    UNSUPPORTED,
    classify,
)
from mlx_m5_bench.estimators import create
from mlx_m5_bench.memory import admission, estimate_bytes, snapshot
from mlx_m5_bench.reporting import aggregate, report
from mlx_m5_bench.runner import read_rows, run, write_json
from mlx_m5_bench.timing import measure, statistics


@pytest.mark.parametrize("name", ["quick", "standard", "full"])
def test_profiles(name):
    assert load_profile(name).cases


@pytest.mark.parametrize(
    "settings",
    [
        {"repeats": 0, "cases": []},
        {"repeats": 1, "cases": [{"algorithm": "bad", "samples": 100, "features": 8}]},
        {"repeats": 1, "threads": 0, "cases": []},
        {"repeats": 1, "mystery": 1, "cases": []},
    ],
)
def test_invalid_profile(settings):
    with pytest.raises(ValidationError):
        Profile.model_validate(settings)


def test_duplicate_and_invalid_dimensions():
    case = Case(algorithm="knn", samples=100, features=8)
    with pytest.raises(ValidationError):
        Profile(repeats=1, cases=[case, case])
    with pytest.raises(ValidationError):
        Case(algorithm="knn", samples=100, features=8, neighbors=100)
    with pytest.raises(ValidationError):
        Case(algorithm="pca", samples=100, features=8, components=9)


@pytest.mark.parametrize("algorithm", ["logistic", "knn", "svc", "pca"])
def test_dataset_and_cpu_adapter(algorithm):
    case = Case(algorithm=algorithm, samples=120, features=8)
    data = generate(case, 42)
    again = generate(case, 42)
    assert data.fingerprint() == again.fingerprint()
    assert data.fingerprint() != generate(case, 43).fingerprint()
    assert data.train.dtype == np.float32
    with threadpool_limits(limits=2):
        model = create(case, "sklearn", 2).fit(data.train, data.y_train)
        result = model.transform(data.test) if algorithm == "pca" else model.predict(data.test)
        output = extract(model, algorithm, data, result)
    assert compare(algorithm, output, output, data)["status"] == "PASS"


def event(backend, operation="fit"):
    return {"backend": backend, "operation": operation}


@pytest.mark.parametrize(
    "algorithm,operation,events,pca_device,expected",
    [
        ("knn", "predict", [event("mlx", "predict")], None, GPU),
        ("knn", "fit", [event("mlx")], None, UNKNOWN),
        ("logistic", "fit", [event("mlx")], None, MIXED),
        ("logistic", "predict", [event("mlx", "predict")], None, FALLBACK),
        ("svc", "fit", [event("mlx"), event("cpu")], None, FALLBACK),
        ("svc", "fit", [event("mlx")], None, MIXED),
        ("pca", "fit", [event("mlx")], None, MIXED),
        ("pca", "transform", [event("mlx", "transform")], False, FALLBACK),
        ("pca", "transform", [event("mlx", "transform")], True, GPU),
        ("pca", "transform", [event("mlx", "transform")], None, UNKNOWN),
        ("knn", "predict", [], None, UNKNOWN),
        ("knn", "predict", [event("mlx", "kneighbors")], None, GPU),
        ("pca", "fit", [event("mlx"), event("cpu")], None, FALLBACK),
    ],
)
def test_backend_classification(algorithm, operation, events, pca_device, expected):
    assert classify(algorithm, operation, events, pca_device=pca_device) == expected


def test_rotation_invariance():
    data = generate(Case(algorithm="pca", samples=120, features=8), 42)
    basis = np.eye(8)[:3]
    reference = {
        "output": np.ones((30, 3)),
        "components": basis,
        "variance": np.array([0.2, 0.2, 0.2]),
        "reconstruction": data.test * 0.9,
    }
    rotation = np.linalg.qr(np.random.default_rng(1).normal(size=(3, 3)))[0]
    rotated = {**reference, "components": rotation @ basis}
    assert compare("pca", reference, rotated, data)["status"] == "PASS"
    wrong = {**reference, "components": np.eye(8)[3:6]}
    assert compare("pca", reference, wrong, data)["status"] == "FAIL"


def test_non_finite_predictions_and_wrong_probabilities():
    data = generate(Case(algorithm="logistic", samples=120, features=8), 42)
    base = {"output": data.y_test, "classes": np.arange(2)}
    assert (
        compare("logistic", base, {**base, "output": data.y_test * np.nan}, data)["status"]
        == "FAIL"
    )
    probability = np.tile([0.4, 0.6], (30, 1))
    base["probabilities"] = probability
    assert (
        compare("logistic", base, {**base, "probabilities": probability + 0.2}, data)["status"]
        == "FAIL"
    )


def test_timing():
    order = []
    value, seconds = measure(lambda: order.append("operation"), lambda: order.append("sync"))
    assert value is None and seconds >= 0
    assert order == ["sync", "operation", "sync"]
    assert statistics([1, 2, 9]) == {"median": 2, "min": 1, "max": 9, "mad": 1}


def test_memory(monkeypatch):
    from types import SimpleNamespace

    from mlx_m5_bench import memory

    case = Case(algorithm="svc", samples=20000, features=128)
    monkeypatch.setattr(
        memory.psutil,
        "virtual_memory",
        lambda: SimpleNamespace(total=24 * 1024**3, available=20 * 1024**3),
    )
    assert "SVC" in admission(case)[2]
    monkeypatch.setattr(
        memory.psutil, "virtual_memory", lambda: SimpleNamespace(total=100, available=50)
    )
    assert admission(case)[2]
    assert estimate_bytes(case) > 0
    assert snapshot()["process_peak_rss_bytes"] > 0


def row(implementation, status="PASS", backend=CPU):
    return {
        "case": "knn-100x8-c2-k5",
        "algorithm": "knn",
        "implementation": implementation,
        "samples": 100,
        "features": 8,
        "phase": "steady",
        "status": "ok",
        "fit_s": 0.2,
        "predict_s": 0.1,
        "fit_backend": backend,
        "predict_backend": backend,
        "correctness": {"status": status},
        "after": {"process_peak_rss_bytes": 123, "mlx_peak_bytes": 5},
    }


@pytest.mark.parametrize(
    "status,backend,eligible",
    [
        ("PASS", GPU, True),
        ("FAIL", GPU, False),
        ("INCONCLUSIVE", GPU, False),
        ("PASS", FALLBACK, False),
        ("PASS", UNKNOWN, False),
        ("PASS", UNSUPPORTED, False),
    ],
)
def test_summary_gating(status, backend, eligible):
    rows = aggregate([row("sklearn"), row("mlxlearn", status, backend)])
    candidate = [item for item in rows if item["implementation"] == "mlxlearn"]
    assert all(("cpu_over_candidate_ratio" in item) == eligible for item in candidate)


def test_reporting(tmp_path):
    write_json(
        tmp_path / "measurements.json",
        [
            row("sklearn"),
            row("mlxlearn", "FAIL", GPU),
            {
                "case": "svc-large",
                "algorithm": "svc",
                "samples": 20000,
                "features": 128,
                "implementation": "mlxlearn",
                "status": "skipped",
                "correctness": {"status": "INCONCLUSIVE"},
            },
        ],
    )
    report(tmp_path)
    assert "FAIL" in (tmp_path / "summary.md").read_text()
    assert len(list((tmp_path / "charts").glob("*.png"))) == 7
    assert (tmp_path / "summary.csv").exists()
    assert json.loads((tmp_path / "summary.json").read_text())


def test_cli(tmp_path):
    response = subprocess.run(
        [sys.executable, "-m", "mlx_m5_bench.cli", "--help"], capture_output=True, text=True
    )
    assert response.returncode == 0 and "doctor" in response.stdout
    response = subprocess.run(
        [sys.executable, "-m", "mlx_m5_bench.cli", "report", "--latest", "--root", str(tmp_path)],
        capture_output=True,
        text=True,
    )
    assert response.returncode == 2 and "No saved runs" in response.stderr


def test_failure_preserved(tmp_path, monkeypatch):
    from mlx_m5_bench import runner

    monkeypatch.setattr(runner, "manifest", lambda: {})
    monkeypatch.setattr(runner, "admission", lambda case: (1, 2, None))

    # A zero exit with an empty output must still create an explicit error record.
    class EmptyWorker:
        pid = 999
        returncode = 0

        def __init__(self, *args, **kwargs):
            pass

        def wait(self, timeout=None):
            return 0

    monkeypatch.setattr(runner.subprocess, "Popen", EmptyWorker)
    profile = Profile(repeats=1, cases=[Case(algorithm="knn", samples=100, features=8)])
    path = run(profile, "quick", tmp_path, ("sklearn",))
    records = json.loads((path / "measurements.json").read_text())
    assert records[0]["status"] == "error"


def test_cpu_only_end_to_end(tmp_path):
    profile = Profile(repeats=1, warmups=0, cases=[Case(algorithm="knn", samples=100, features=8)])
    path = run(profile, "quick", tmp_path, ("sklearn",))
    records = json.loads((path / "measurements.json").read_text())
    assert len(records) == 2
    assert all(record["status"] == "ok" for record in records)
    assert all(record["correctness"]["status"] == "INCONCLUSIVE" for record in records)
    assert (path / "manifest.json").exists()


def test_read_rows(tmp_path):
    assert read_rows(tmp_path / "missing") == []
    path = tmp_path / "raw.jsonl"
    path.write_text('{"status":"error"}\n')
    assert read_rows(path) == [{"status": "error"}]
    path.write_text('{"status":')
    assert read_rows(path)[0]["status"] == "error"


@pytest.mark.apple_gpu
@pytest.mark.parametrize("algorithm", ["logistic", "knn", "svc", "pca"])
def test_apple_estimator_pair(algorithm, tmp_path):
    from mlx_m5_bench.worker import bench

    case = Case(algorithm=algorithm, samples=120, features=8)
    profile = Profile(repeats=1, warmups=0, cases=[case])
    data = generate(case, profile.seed)
    for implementation in ("sklearn", "mlxlearn"):
        bench(case, profile, implementation, tmp_path / f"{implementation}.jsonl")
        records = read_rows(tmp_path / f"{implementation}.jsonl")
        assert len(records) == 2
        assert all(record["status"] == "ok" for record in records)
    with np.load(tmp_path / "sklearn-1.npz") as cpu, np.load(tmp_path / "mlxlearn-1.npz") as gpu:
        assert compare(algorithm, dict(cpu), dict(gpu), data)["status"] == "PASS"


def test_measurement_schema():
    from mlx_m5_bench.schemas import Measurement

    assert Measurement(status="error").status == "error"
    assert Measurement.model_validate(row("sklearn")).fit_s == 0.2
    with pytest.raises(ValidationError):
        Measurement(status="ok")
    with pytest.raises(ValidationError):
        Measurement(status="error", fit_s=-1)
    with pytest.raises(ValidationError):
        Measurement(status="error", fit_s=float("nan"))
    with pytest.raises(ValidationError):
        Measurement(status="error", backend="GPU")


def test_dashboard_load_and_filters(tmp_path, monkeypatch):
    from streamlit.testing.v1 import AppTest

    run_path = tmp_path / "saved"
    run_path.mkdir()
    write_json(
        run_path / "manifest.json",
        {
            "profile": "quick",
            "timestamp": "2026-11-14T00:00:00Z",
            "state": "complete",
            "machine": "arm64",
        },
    )
    raw = [row("sklearn"), row("mlxlearn", "FAIL", GPU)]
    write_json(run_path / "summary.json", aggregate(raw))
    write_json(run_path / "measurements.json", raw)
    monkeypatch.setattr(sys, "argv", ["dashboard", str(tmp_path)])
    import mlx_m5_bench

    script = str(Path(mlx_m5_bench.__file__).with_name("dashboard.py"))
    app = AppTest.from_file(script).run()
    assert not app.exception
    assert len(app.dataframe[0].value) == 4
    app.multiselect[0].set_value([]).run()
    assert not app.exception
    assert len(app.dataframe[0].value) == 0


def test_admission_skip_records(tmp_path, monkeypatch):
    from mlx_m5_bench import runner

    monkeypatch.setattr(runner, "manifest", lambda: {})
    monkeypatch.setattr(runner, "admission", lambda case: (100, 20, "memory limit"))
    profile = Profile(repeats=1, cases=[Case(algorithm="knn", samples=100, features=8)])
    path = run(profile, "quick", tmp_path)
    records = json.loads((path / "measurements.json").read_text())
    assert len(records) == 2 and all(record["status"] == "skipped" for record in records)


def test_timeout_records(tmp_path, monkeypatch):
    from mlx_m5_bench import runner

    monkeypatch.setattr(runner, "manifest", lambda: {})
    monkeypatch.setattr(runner, "admission", lambda case: (1, 2, None))
    signals = []
    monkeypatch.setattr(runner.os, "killpg", lambda pid, sig: signals.append((pid, sig)))

    class TimedOut:
        pid = 999
        returncode = -9

        def __init__(self, *args, **kwargs):
            pass

        def wait(self, timeout=None):
            if timeout is not None:
                raise subprocess.TimeoutExpired("worker", timeout)

    monkeypatch.setattr(runner.subprocess, "Popen", TimedOut)
    profile = Profile(repeats=1, cases=[Case(algorithm="knn", samples=100, features=8)])
    path = run(profile, "quick", tmp_path, ("sklearn",))
    assert signals
    assert json.loads((path / "measurements.json").read_text())[0]["status"] == "timeout"


def test_knn_query_prefix_preserves_training_set():
    common = {"algorithm": "knn", "samples": 100, "features": 8}
    small = Case.model_validate({**common, "query_rows": 4})
    large = Case.model_validate({**common, "query_rows": 5})
    lhs, rhs = generate(small, 42), generate(large, 42)
    assert small.key != large.key
    np.testing.assert_array_equal(lhs.train, rhs.train)
    np.testing.assert_array_equal(lhs.y_train, rhs.y_train)
    np.testing.assert_array_equal(lhs.test, rhs.test[:4])
    np.testing.assert_array_equal(lhs.y_test, rhs.y_test[:4])
    with pytest.raises(ValidationError, match="query_rows"):
        Case.model_validate({**common, "query_rows": 26})
    with pytest.raises(ValidationError, match="query_rows"):
        Case.model_validate({**common, "algorithm": "svc", "query_rows": 4})


def test_explicit_mlx_cpu_profile():
    case = Case(algorithm="knn", samples=100, features=8)
    assert Profile(repeats=1, cases=[case], force_mlx=False, mlx_device="cpu").mlx_device == "cpu"
    with pytest.raises(ValidationError, match="force_mlx requires mlx_device=gpu"):
        Profile(repeats=1, cases=[case], mlx_device="cpu")


def test_warmed_knn_reuses_one_fit(tmp_path):
    profile = Profile(
        repeats=2,
        warmups=1,
        reuse_model=True,
        cases=[Case(algorithm="knn", samples=100, features=8)],
    )
    path = run(profile, "quick", tmp_path, ("sklearn",))
    records = json.loads((path / "measurements.json").read_text())
    assert [r["phase"] for r in records] == ["cold", "warmup", "steady", "steady"]
    assert all(record["status"] == "ok" for record in records)
    assert "fit_s" in records[0] and all("fit_s" not in r for r in records[1:])
    assert [r["reused_model"] for r in records] == [False, True, True, True]


def test_knn_explicit_training_prefix():
    common = {"algorithm": "knn", "samples": 100, "features": 8, "query_rows": 4}
    lhs = Case.model_validate({**common, "train_rows": 20})
    rhs = Case.model_validate({**common, "train_rows": 30})
    first, second = generate(lhs, 42), generate(rhs, 42)
    assert lhs.key != rhs.key
    assert first.train.shape == (20, 8)
    assert second.train.shape == (30, 8)
    np.testing.assert_array_equal(first.y_train, second.y_train[:20])
    np.testing.assert_array_equal(first.y_test, second.y_test)
    np.testing.assert_allclose(first.train.mean(axis=0), 0, atol=1e-6)
    with pytest.raises(ValidationError, match="train_rows"):
        Case.model_validate({**common, "train_rows": 76})
    with pytest.raises(ValidationError, match="neighbors"):
        Case.model_validate({**common, "train_rows": 4})


def test_knn_shared_source_feature_prefix():
    common = {"algorithm": "knn", "samples": 100, "query_rows": 5, "source_features": 33}
    narrow = Case.model_validate({**common, "features": 31})
    wide = Case.model_validate({**common, "features": 33})
    lhs, rhs = generate(narrow, 42), generate(wide, 42)
    np.testing.assert_array_equal(lhs.train, rhs.train[:, :31])
    np.testing.assert_array_equal(lhs.test, rhs.test[:, :31])
    np.testing.assert_array_equal(lhs.y_train, rhs.y_train)
    np.testing.assert_array_equal(lhs.y_test, rhs.y_test)
    assert narrow.key != Case(algorithm="knn", samples=100, features=31, query_rows=5).key
    with pytest.raises(ValidationError, match="source_features"):
        Case.model_validate({**common, "features": 34})

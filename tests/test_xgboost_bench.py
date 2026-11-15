import json
from io import StringIO
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pytest

from mlx_m5_bench import xgboost_bench, xgboost_worker
from mlx_m5_bench.datasets import Dataset
from mlx_m5_bench.xgboost_bench import dataset, quality, verify_trace


@pytest.mark.parametrize("task", ["classification", "regression"])
def test_paired_xgboost_inputs_and_quality(task):
    data = dataset(task, samples=80)
    assert data.train.shape == (60, 32)
    assert data.test.shape == (20, 32)
    assert data.fingerprint() == dataset(task, samples=80).fingerprint()
    expected = data.y_test.astype(float)
    assert quality(task, data.y_test, expected, expected)["status"] == "PASS"
    disagreement = 1 - expected if task == "classification" else expected + 1
    assert quality(task, data.y_test, expected, disagreement)["status"] == "FAIL"
    assert quality(task, data.y_test, expected, expected[:-1])["status"] == "FAIL"


def test_xgboost_worker_requires_an_isolated_distribution(monkeypatch):
    cpu = SimpleNamespace(metadata={"Name": "xgboost"}, version="3.4.1")
    metal = SimpleNamespace(metadata={"Name": "xgboost-metal"}, version="0.1.1")
    monkeypatch.setattr(xgboost_worker, "distributions", lambda: [metal])
    assert xgboost_worker.engine_distribution("metal") == ("xgboost-metal", "0.1.1")
    with pytest.raises(RuntimeError, match="isolated xgboost environment"):
        xgboost_worker.engine_distribution("cpu")
    monkeypatch.setattr(xgboost_worker, "distributions", lambda: [cpu, metal])
    with pytest.raises(RuntimeError, match="isolated xgboost-metal environment"):
        xgboost_worker.engine_distribution("metal")


def test_xgboost_trace_requires_gpu_work_in_both_operations():
    working = {
        "completed_buffers": 1,
        "dispatches": 1,
        "devices": ["Apple M5 Pro"],
        "pipelines": ["kernel"],
    }
    empty = {"completed_buffers": 0, "dispatches": 0}
    assert (
        verify_trace("metal", {"metal_trace": dict(train=working, predict=working)}, "Apple M5 Pro")
        == "GPU_VERIFIED"
    )
    with pytest.raises(RuntimeError, match="metal predict"):
        verify_trace("metal", {"metal_trace": dict(train=working, predict=empty)}, "Apple M5 Pro")
    with pytest.raises(RuntimeError, match="cpu train"):
        verify_trace("cpu", {"metal_trace": dict(train=working, predict=empty)}, "Apple M5 Pro")


def test_training_size_sweep_keeps_the_test_batch_fixed(tmp_path, monkeypatch):
    source = {task: dataset(task, samples=80) for task in xgboost_bench.TASKS}
    monkeypatch.setattr(xgboost_bench, "dataset", source.__getitem__)
    monkeypatch.setattr(xgboost_bench, "manifest", dict)

    def fake_worker(executable, request, directory):
        task = directory.parent.parent.name
        size = int(directory.parent.name.removeprefix("train-"))
        data = source[task]
        with np.load(request["dataset"], allow_pickle=False) as archive:
            np.testing.assert_array_equal(archive["train"], data.train[:size])
            np.testing.assert_array_equal(archive["y_train"], data.y_train[:size])
            np.testing.assert_array_equal(archive["test"], data.test)
            np.testing.assert_array_equal(archive["y_test"], data.y_test)
        subset = Dataset(data.train[:size], data.test, data.y_train[:size], data.y_test)
        timings = {
            "phase": "steady",
            "train_ingest_s": 0.1,
            "train_s": 0.2,
            "first_prediction_s": 0.3,
            "end_to_end_s": 0.6,
            "predict_s": 0.3,
        }
        predictions = data.y_test.astype(float)[None, :]
        return {"dataset_sha256": subset.fingerprint()}, [timings], predictions

    monkeypatch.setattr(xgboost_bench, "worker", fake_worker)
    interpreters = {"cpu": Path("cpu"), "metal": Path("metal")}
    output = tmp_path / "sweep"
    assert xgboost_bench.run(output, interpreters, 4, train_sizes=(20, 40))
    summary = json.loads((output / "summary.json").read_text())
    assert {(r["task"], r["train_rows"], r["engine"]) for r in summary} == {
        (task, size, engine) for task in source for size in (20, 40) for engine in interpreters
    }


def test_prediction_size_sweep_uses_prefixes_and_checks_warmed_outputs():
    test = np.arange(8).reshape(4, 2)
    calls = []

    def predict(batch):
        np.testing.assert_array_equal(batch, test[: len(batch)])
        calls.append(len(batch))
        return batch.sum(axis=1)

    stream = StringIO()
    full_prediction = test.sum(axis=1)
    xgboost_worker.predict_batches(predict, test, full_prediction, [4, 1], 3, stream, None)
    assert calls == [4] * 5 + [1] * 5
    assert [json.loads(line)["query_rows"] for line in stream.getvalue().splitlines()] == [
        4,
        4,
        4,
        1,
        1,
        1,
    ]
    with pytest.raises(AssertionError):
        xgboost_worker.predict_batches(predict, test, full_prediction + 1, [1], 1, stream, None)

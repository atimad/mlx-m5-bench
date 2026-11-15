from types import SimpleNamespace

import pytest

from mlx_m5_bench import xgboost_worker
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

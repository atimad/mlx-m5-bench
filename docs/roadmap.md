# Release roadmap

## v0.1.0 · Verified classical ML baseline

The first release established the four-family scikit-learn and mlx-learn benchmark with reproducible workloads, correctness checks, and operation-level CPU/GPU evidence. [v0.1.0 release](https://github.com/atimad/mlx-m5-bench/releases/tag/v0.1.0)

The release was validated against the locked dependencies, Linux CPU CI, and Apple Silicon smoke tests. [Methodology](methodology.md) · [Reproduction](reproducibility.md) · [Results](results.md) · [Limitations](limitations.md)

## v0.2.0 · XGBoost versus xgboost-metal

The second major experiment compares CPU XGBoost with xgboost-metal on Apple Silicon for tabular gradient boosting. Upstream reports promising timings for histogram training and prediction on an M4 Max. Treat xgboost-metal as an experimental backend and measure it independently on the M5 Pro. [Upstream benchmarks](https://pypi.org/project/xgboost-metal/#benchmarks) · [Compatibility guide](https://github.com/tabulai/xgboost-metal/blob/main/docs/compatibility.md)

- The opt-in adapters run in separate worker environments. Both distributions provide the `xgboost` import. The manifest records each distribution, version, and native build. [Environment setup](evidence/xgboost-baseline/README.md#reproduce)
- The dense classification and regression baseline records ingestion, training, warmed prediction, and held-out quality. Separate Metal replays verify training and prediction. [XGBoost baseline](evidence/xgboost-baseline/README.md)
- The scaling studies publish the workload grids, raw timings, correctness results, and traces. [Training rows](evidence/xgboost-training-sweep/README.md) · [Prediction batch size](evidence/xgboost-query-sweep/README.md) · [Feature count](evidence/xgboost-feature-sweep/README.md)

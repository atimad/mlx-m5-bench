# Release roadmap

## v0.1.0 · Verified classical ML baseline

Release the existing four-family scikit-learn and mlx-learn benchmark with reproducible workloads, correctness checks, and operation-level CPU/GPU evidence. The release should document what each timing includes, preserve raw measurements and environment manifests, and make it possible to repeat the benchmark from a clean install.

Review the release candidate against the locked dependencies, Linux CPU CI, and Apple Silicon smoke tests. Include the trace evidence for claims about GPU execution and carry forward known workload limitations. [Methodology](methodology.md) · [Reproduction](reproducibility.md) · [Results](results.md) · [Limitations](limitations.md)

## v0.2.0 · XGBoost versus xgboost-metal

The second major experiment compares CPU XGBoost with xgboost-metal on Apple Silicon for tabular gradient boosting. Upstream reports promising timings for histogram training and prediction on an M4 Max. Treat xgboost-metal as an experimental backend and measure it independently on the M5 Pro. [Upstream benchmarks](https://pypi.org/project/xgboost-metal/#benchmarks) · [Compatibility guide](https://github.com/tabulai/xgboost-metal/blob/main/docs/compatibility.md)

- Add independent, opt-in adapters using the isolated-worker protocol. Pin each distribution in its own environment because both provide the `xgboost` import. Record the installed distribution, version, and build information in the run manifest. [Upstream installation guidance](https://pypi.org/project/xgboost-metal/#installation)
- Start with dense tabular binary classification and regression using histogram trees. Share the exact splits and inputs and align the objective, boosting rounds, depth, histogram bins, and seed. Define acceptable held-out metric differences before interpreting speedups. Report log loss and ROC AUC for classification and RMSE for regression.
- Time ingestion, training, and warmed prediction separately. Report end-to-end latency, repeated-run dispersion, CPU thread settings, and memory use. Verify training and prediction dispatches in separate Metal trace runs.
- Scale training rows, feature count, and prediction batch size after the baseline cases pass. Publish the workloads, raw measurements, correctness outcomes, and trace evidence so readers can reproduce the comparisons.

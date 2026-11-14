# Automatic versus forced MLX timing on M5 Pro

This uninstrumented timing panel reruns the seven workloads from the [matched Metal traces](../metal-auto/README.md). It ran on AC power under the same locked environment. Automatic mode uses device=auto with the override absent. Forced mode uses device=gpu and MLXLEARN_FORCE_BACKEND=mlx. Worker launches strip inherited MLX tuning and Metal capture environment settings. No command-buffer observer or Metal capture is used.

The block order was auto → forced → forced → auto. Each block measured a dedicated scikit-learn baseline and the candidate in serial subprocesses, CPU first for each case. Each implementation ran five steady repetitions, one warmup, and a separately recorded first call. The input fingerprints match the previously traced workloads. All 140 steady timing pairs passed numerical checks (280 steady records total). The worker pins requested CPU threads to four and synchronizes mlx-learn operations before and after each measurement, including mlx-learn host paths. Scikit-learn operations are synchronous.

Values below are medians of the two block medians for each mode in milliseconds. The CPU columns are the controls from that mode’s blocks. CPU/candidate ratios are the median of the two block-level ratios. They are library timing comparisons. The Metal column gives completed GPU buffer counts from the separate matched traces, in auto / forced order.

| Workload | Operation | CPU (auto blocks), ms | Auto, ms | CPU / auto | CPU (forced blocks), ms | Forced, ms | CPU / forced | Trace buffers auto / forced |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| knn-8000x128-c3-k5 | fit | 0.456 | 0.418 | 1.10 | 0.444 | 0.428 | 1.04 | 0 / 0 |
| knn-8000x128-c3-k5 | predict | 13.066 | 1.988 | 6.75 | 12.572 | 2.002 | 6.40 | 1 / 1 |
| knn-30000x64-c2-k5 | fit | 0.720 | 0.763 | 0.95 | 0.709 | 0.836 | 0.85 | 0 / 0 |
| knn-30000x64-c2-k5 | predict | 112.078 | 15.176 | 7.39 | 112.572 | 14.913 | 7.55 | 7 / 7 |
| logistic-2000x32-c2 | fit | 1.110 | 4.973 | 0.22 | 1.147 | 3.301 | 0.35 | 0 / 14 |
| logistic-2000x32-c2 | predict | 0.058 | 0.126 | 0.46 | 0.060 | 0.122 | 0.49 | 0 / 0 |
| logistic-100000x256-c2 | fit | 43.211 | 43.390 | 1.00 | 43.288 | 17.775 | 2.44 | 0 / 18 |
| logistic-100000x256-c2 | predict | 1.030 | 1.823 | 0.57 | 1.051 | 1.810 | 0.58 | 0 / 0 |
| svc-4000x256-c3 | fit | 348.613 | 40.150 | 8.68 | 350.753 | 33.915 | 10.34 | 0 / 4 |
| svc-4000x256-c3 | predict | 166.061 | 3.595 | 46.19 | 166.218 | 2.363 | 70.34 | 0 / 1 |
| pca-12000x256-c2-p8 | fit | 4.001 | 2.837 | 1.41 | 4.134 | 3.758 | 1.11 | 0 / 3 |
| pca-12000x256-c2-p8 | transform | 0.209 | 0.219 | 0.95 | 0.221 | 0.800 | 0.28 | 0 / 2 |
| pca-2000x32-c2-p3 | fit | 0.177 | 0.239 | 0.75 | 0.190 | 1.221 | 0.18 | 0 / 3 |
| pca-2000x32-c2-p3 | transform | 0.040 | 0.091 | 0.44 | 0.041 | 0.098 | 0.42 | 0 / 0 |

Both KNN prediction workloads used GPU work in both matched trace modes. Prediction timing was similar across modes and about 6.4–7.5× faster than the respective CPU controls. KNN fit staged data with zero Metal submissions in the matched traces.

Automatic logistic fit was approximately even with scikit-learn for 100,000 × 256. Forced MLX was about 2.44× faster than scikit-learn in that case. On the smaller case both candidate modes were slower than scikit-learn. Logistic prediction ran on the host in both modes.

Automatic SVC prediction was around 46× faster than scikit-learn on this workload, with zero Metal submissions in the matched replay. Forced mode was around 70× faster against its CPU control and used mixed CPU/GPU execution. PCA automatic mode was faster than forced mode for both fits and both transforms in this timing panel. The 12,000 × 256 automatic transform was roughly even with scikit-learn.

Two blocks per mode give a small local sample. CPU-first ordering, warm caches, system load and candidate synchronization costs can affect the measurements, especially sub-millisecond calls. These measurements do not establish a general crossover. Original canonical timing tables and trace evidence remain separate.

## Raw evidence

Block manifests identify the benchmark source commit. The last two manifests report a dirty checkout because analysis and documentation were being drafted. The benchmark source was unchanged across all four blocks. Each block retains cold, warmup and steady records.

- routing-1-auto: [manifest](20261114T201045416655Z-79edec2ed1/manifest.json), [measurements](20261114T201045416655Z-79edec2ed1/measurements.json), [summary](20261114T201045416655Z-79edec2ed1/summary.md)
- routing-2-forced: [manifest](20261114T201107058867Z-7a94ee26dc/manifest.json), [measurements](20261114T201107058867Z-7a94ee26dc/measurements.json), [summary](20261114T201107058867Z-7a94ee26dc/summary.md)
- routing-3-forced: [manifest](20261114T201128483240Z-7a94ee26dc/manifest.json), [measurements](20261114T201128483240Z-7a94ee26dc/measurements.json), [summary](20261114T201128483240Z-7a94ee26dc/summary.md)
- routing-4-auto: [manifest](20261114T201149904416Z-79edec2ed1/manifest.json), [measurements](20261114T201149904416Z-79edec2ed1/measurements.json), [summary](20261114T201149904416Z-79edec2ed1/summary.md)

[Machine-readable comparison and block statistics](comparison.json)

## Reproduce

```sh
.venv/bin/python scripts/benchmark_routing.py results/routing-timing-replay
.venv/bin/python scripts/summarize_routing.py results/routing-timing-replay/*
```

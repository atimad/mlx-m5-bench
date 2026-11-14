# Automatic GPU crossover on the M5 Pro

This panel brackets one mlx-learn 0.1.2 fit-routing gate per algorithm, keeping features fixed at 256 and changing only total sample count within each pair. Routing uses training rows after the benchmark's 75/25 split. All inputs use seed 42 and the existing estimator parameters. SVC uses RBF and three classes. PCA uses covariance eigendecomposition and eight components.

| Gate | Training rows below / above | Training rows × features below / above | Other conditions |
|---|---:|---:|---|
| Logistic, 20 million elements | 77,400 / 78,900 | 19,814,400 / 20,198,400 | Both exceed 20,000 rows. The alternative tall branch requires 250,000 rows. |
| SVC, 1 million element-ops | 3,870 / 3,942 | 990,720 / 1,009,152 | Both exceed 2,048 rows. |
| PCA covariance, 8 million elements | 30,937 / 31,563 | 7,919,872 / 8,080,128 | Both are below the separate 512-feature gate. |

The thresholds are library routing rules. They do not predict the fastest backend on every workload. This panel isolates the work-size gates and leaves the alternative row-count and feature-count gates outside its scope. [Pinned crossover defaults](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_common/config.py)

Uninstrumented timing used four blocks ordered auto → forced → forced → auto, each with a fresh scikit-learn control, four requested CPU threads, one warmup, and five steady repetitions. Each implementation ran serially in its own process, with scikit-learn first for each pair. The first call was also recorded separately. Automatic mode sets device=auto without the override. Forced mode requests GPU and sets MLXLEARN_FORCE_BACKEND=mlx.

Separate automatic-mode Metal replays used the same inputs and parameters. The command observer records completed buffers in the fit and first-inference windows. Positive operations also have capture checksums. Raw capture bundles remain in the ignored local results directory. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

## Timings and verified automatic routing

All 120 steady timing pairs and all six traced pairs passed the numerical checks. All traced scikit-learn controls submitted zero Metal buffers. Times are milliseconds and show the median of the two block medians per mode. Each CPU column uses its corresponding control blocks. The Metal counts come from the separate auto replays. Forced timing rows retain the evidence available in their uninstrumented runs.

| Workload | Operation | CPU (auto blocks) | Auto | CPU (forced blocks) | Forced | Auto Metal buffers |
|---|---|---:|---:|---:|---:|---:|
| logistic-103200x256-c2 | fit | 41.784 | 42.851 | 41.552 | 15.597 | [0](metal/logistic-103200x256-c2/mlxlearn-fit.tsv) |
| logistic-103200x256-c2 | predict | 1.072 | 1.905 | 1.070 | 1.853 | [0](metal/logistic-103200x256-c2/mlxlearn-predict.tsv) |
| logistic-105200x256-c2 | fit | 40.839 | 16.383 | 40.100 | 15.850 | [16](metal/logistic-105200x256-c2/mlxlearn-fit.tsv) |
| logistic-105200x256-c2 | predict | 1.029 | 2.003 | 1.043 | 1.849 | [0](metal/logistic-105200x256-c2/mlxlearn-predict.tsv) |
| svc-5160x256-c3 | fit | 558.319 | 65.070 | 559.626 | 51.401 | [0](metal/svc-5160x256-c3/mlxlearn-fit.tsv) |
| svc-5160x256-c3 | predict | 272.341 | 5.346 | 272.280 | 3.076 | [0](metal/svc-5160x256-c3/mlxlearn-predict.tsv) |
| svc-5256x256-c3 | fit | 570.479 | 52.485 | 580.802 | 53.023 | [4](metal/svc-5256x256-c3/mlxlearn-fit.tsv) |
| svc-5256x256-c3 | predict | 278.372 | 3.102 | 280.257 | 3.266 | [1](metal/svc-5256x256-c3/mlxlearn-predict.tsv) |
| pca-41250x256-c2-p8 | fit | 6.456 | 4.539 | 6.433 | 4.415 | [0](metal/pca-41250x256-c2-p8/mlxlearn-fit.tsv) |
| pca-41250x256-c2-p8 | transform | 0.681 | 0.481 | 0.646 | 0.983 | [0](metal/pca-41250x256-c2-p8/mlxlearn-transform.tsv) |
| pca-42084x256-c2-p8 | fit | 6.517 | 4.789 | 6.508 | 4.806 | [3](metal/pca-42084x256-c2-p8/mlxlearn-fit.tsv) |
| pca-42084x256-c2-p8 | transform | 0.689 | 0.978 | 0.667 | 1.104 | [2](metal/pca-42084x256-c2-p8/mlxlearn-transform.tsv) |

Automatic fit submitted zero Metal buffers below each gate and 16, 4 and 3 above the logistic, SVC and PCA gates, respectively. Above the gate, SVC prediction and PCA transform also submitted GPU work. Logistic prediction submitted zero in both cases, including the above-gate run whose diagnostics inherited the fitted MLX label.

Forced MLX already improved logistic fit below the gate on this panel. Automatic SVC was much faster than scikit-learn even below the gate, where the trace shows the candidate used CPU. Above the PCA gate, automatic fit was faster than scikit-learn but changed little from the below-gate CPU path. Its GPU transform was slower than both the below-gate candidate and its paired scikit-learn control. The close shapes still use separately generated datasets. The timing differences describe this panel on this Mac.

## Evidence and reproduction

[Comparison JSON](comparison.json) includes paired ratios and per-block timing dispersion. Each linked run contains the full raw measurement rows and a reproducibility manifest.

- routing-1-auto: [manifest](20261114T201525106094Z-0a2448427a/manifest.json), [raw measurements](20261114T201525106094Z-0a2448427a/measurements.json), [summary](20261114T201525106094Z-0a2448427a/summary.md)
- routing-2-forced: [manifest](20261114T201559184153Z-fc68646b67/manifest.json), [raw measurements](20261114T201559184153Z-fc68646b67/measurements.json), [summary](20261114T201559184153Z-fc68646b67/summary.md)
- routing-3-forced: [manifest](20261114T201633091270Z-fc68646b67/manifest.json), [raw measurements](20261114T201633091270Z-fc68646b67/measurements.json), [summary](20261114T201633091270Z-fc68646b67/summary.md)
- routing-4-auto: [manifest](20261114T201706528344Z-0a2448427a/manifest.json), [raw measurements](20261114T201706528344Z-0a2448427a/measurements.json), [summary](20261114T201706528344Z-0a2448427a/summary.md)

Metal routing events, numerical comparisons, and capture checksums by case:

- [logistic-103200x256-c2](metal/logistic-103200x256-c2/metadata.json)
- [logistic-105200x256-c2](metal/logistic-105200x256-c2/metadata.json)
- [svc-5160x256-c3](metal/svc-5160x256-c3/metadata.json)
- [svc-5256x256-c3](metal/svc-5256x256-c3/metadata.json)
- [pca-41250x256-c2-p8](metal/pca-41250x256-c2-p8/metadata.json)
- [pca-42084x256-c2-p8](metal/pca-42084x256-c2-p8/metadata.json)

Replay sequentially so capture activity cannot affect timing. Use the locked Apple Silicon environment and fresh output directories.

```sh
.venv/bin/python scripts/benchmark_routing.py results/crossover-replay --config scripts/crossover.yaml
.venv/bin/python scripts/summarize_routing.py results/crossover-replay/*
out=results/crossover-metal-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for case in logistic-103200x256-c2 logistic-105200x256-c2 \
            svc-5160x256-c3 svc-5256x256-c3 pca-41250x256-c2-p8 pca-42084x256-c2-p8; do
  env -u MLXLEARN_FORCE_BACKEND MTL_CAPTURE_ENABLED=1 \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_fit_inference.py "$case" "$out/$case" "$out/probe.dylib" \
    --mode auto --config scripts/crossover.yaml > "$out/$case.json"
done
```

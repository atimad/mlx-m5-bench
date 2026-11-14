# Row-count and feature-count crossover gates on the M5 Pro

This panel isolates the three shape gates left open by the earlier [work-size crossover panel](../crossover/README.md). It uses mlx-learn 0.1.2 with binary L-BFGS logistic regression, three-class RBF SVC, and covariance-eigh PCA with eight components. Gate calculations use training rows after the benchmark's 75/25 split.

| Gate | Below | Above | Companion conditions |
|---|---:|---:|---|
| Tall logistic, 250,000 training rows | 247,500 × 33 | 252,501 × 33 | Both clear 8 million elements, at 8,167,500 and 8,332,533. Both stay below the wide branch's 20 million elements. |
| SVC, 2,048 training rows | 2,028 × 512 | 2,067 × 512 | Both clear 1 million element-ops, at 1,038,336 and 1,058,304. |
| Covariance PCA, 512 features | 9,000 × 511 | 9,000 × 512 | Both stay below 8 million elements, at 4,599,000 and 4,608,000. The upper case is exactly at the inclusive feature threshold. |

These gates determine library routing. The measured CPU and GPU latencies depend on model, shape, data and host. The paired inputs are separately generated with the same seed. [Pinned crossover defaults](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_common/config.py)

Timing was uninstrumented, with serial auto → forced → forced → auto blocks, separate scikit-learn controls, seed 42, four requested CPU threads, one warmup and five steady repeats per implementation. Each block also recorded the first call separately. Automatic mode uses device=auto with the override unset. Forced mode uses device=gpu and MLXLEARN_FORCE_BACKEND=mlx. Each scikit-learn control precedes its candidate. Small differences can reflect normal run variability and workload differences.

Separate automatic-mode Metal replays use the same inputs and parameters. They collect completed Metal buffers for fit and first inference on the fitted model. Synchronization is outside the trace windows. Positive operations also have capture checksums. Raw capture bundles stay in the ignored local results directory. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

## Timings and verified automatic routing

All 120 steady timing pairs and all six traced pairs passed numerical checks. Every scikit-learn trace control submitted zero Metal buffers. Timings are milliseconds and take the median of the two block medians for each mode. CPU columns come from their respective mode blocks. The counts come from separate auto traces.

| Workload | Operation | CPU (auto blocks) | Auto | CPU (forced blocks) | Forced | Auto Metal buffers |
|---|---|---:|---:|---:|---:|---:|
| logistic-330000x33-c2 | fit | 65.357 | 41.276 | 65.292 | 11.148 | [0](metal/logistic-330000x33-c2/mlxlearn-fit.tsv) |
| logistic-330000x33-c2 | predict | 0.722 | 1.053 | 0.696 | 1.018 | [0](metal/logistic-330000x33-c2/mlxlearn-predict.tsv) |
| logistic-336668x33-c2 | fit | 61.598 | 11.018 | 61.036 | 11.288 | [14](metal/logistic-336668x33-c2/mlxlearn-fit.tsv) |
| logistic-336668x33-c2 | predict | 0.705 | 1.031 | 0.708 | 1.035 | [0](metal/logistic-336668x33-c2/mlxlearn-predict.tsv) |
| svc-2704x512-c3 | fit | 333.791 | 24.731 | 338.568 | 22.085 | [0](metal/svc-2704x512-c3/mlxlearn-fit.tsv) |
| svc-2704x512-c3 | predict | 152.739 | 2.651 | 155.010 | 1.904 | [0](metal/svc-2704x512-c3/mlxlearn-predict.tsv) |
| svc-2756x512-c3 | fit | 345.848 | 22.555 | 346.201 | 22.660 | [4](metal/svc-2756x512-c3/mlxlearn-fit.tsv) |
| svc-2756x512-c3 | predict | 160.123 | 1.935 | 163.576 | 1.954 | [1](metal/svc-2756x512-c3/mlxlearn-predict.tsv) |
| pca-12000x511-c2-p8 | fit | 14.742 | 10.505 | 14.739 | 10.520 | [0](metal/pca-12000x511-c2-p8/mlxlearn-fit.tsv) |
| pca-12000x511-c2-p8 | transform | 0.381 | 0.371 | 0.393 | 0.850 | [0](metal/pca-12000x511-c2-p8/mlxlearn-transform.tsv) |
| pca-12000x512-c2-p8 | fit | 16.550 | 10.565 | 16.558 | 10.557 | [3](metal/pca-12000x512-c2-p8/mlxlearn-fit.tsv) |
| pca-12000x512-c2-p8 | transform | 0.400 | 1.134 | 0.434 | 1.071 | [2](metal/pca-12000x512-c2-p8/mlxlearn-transform.tsv) |

Automatic fit submitted zero buffers below each gate and 14, 4 and 3 on the eligible side for logistic regression, SVC and PCA respectively. Logistic prediction submitted zero on both sides, including the run with inherited MLX prediction diagnostics. SVC prediction and PCA transform submitted GPU work on the eligible side.

Tall logistic auto fit dropped from 41.28 to 11.02 ms. Forced fit on the below-gate shape was already 11.15 ms. SVC auto fit dropped from 24.73 to 22.55 ms and prediction from 2.65 to 1.94 ms. Below-gate SVC prediction was already much faster than scikit-learn on the CPU. PCA auto fit remained around 10.5 ms on both sides. At 512 features, GPU-assisted transform took 1.134 ms versus 0.371 ms at 511 features and 0.400 ms for the matched scikit-learn control.

## Evidence and reproduction

[Comparison JSON](comparison.json) gives per-block statistics and paired CPU/candidate ratios. Each timing run includes its reproducibility manifest and full measurements.

- routing-1-auto: [manifest](20261114T202046280477Z-f3f452de2b/manifest.json), [measurements](20261114T202046280477Z-f3f452de2b/measurements.json), [summary](20261114T202046280477Z-f3f452de2b/summary.md)
- routing-2-forced: [manifest](20261114T202110775169Z-036d19f5c1/manifest.json), [measurements](20261114T202110775169Z-036d19f5c1/measurements.json), [summary](20261114T202110775169Z-036d19f5c1/summary.md)
- routing-3-forced: [manifest](20261114T202134903408Z-036d19f5c1/manifest.json), [measurements](20261114T202134903408Z-036d19f5c1/measurements.json), [summary](20261114T202134903408Z-036d19f5c1/summary.md)
- routing-4-auto: [manifest](20261114T202158511061Z-f3f452de2b/manifest.json), [measurements](20261114T202158511061Z-f3f452de2b/measurements.json), [summary](20261114T202158511061Z-f3f452de2b/summary.md)

Metal routing events, correctness, and capture checksums by case:

- [logistic-330000x33-c2](metal/logistic-330000x33-c2/metadata.json)
- [logistic-336668x33-c2](metal/logistic-336668x33-c2/metadata.json)
- [svc-2704x512-c3](metal/svc-2704x512-c3/metadata.json)
- [svc-2756x512-c3](metal/svc-2756x512-c3/metadata.json)
- [pca-12000x511-c2-p8](metal/pca-12000x511-c2-p8/metadata.json)
- [pca-12000x512-c2-p8](metal/pca-12000x512-c2-p8/metadata.json)

Run timing and tracing sequentially in the locked Apple Silicon environment. Use fresh output directories.

```sh
.venv/bin/python scripts/benchmark_routing.py results/crossover-shape-replay --config scripts/crossover-shape.yaml
.venv/bin/python scripts/summarize_routing.py results/crossover-shape-replay/*
out=results/crossover-shape-metal-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for case in logistic-330000x33-c2 logistic-336668x33-c2 \
            svc-2704x512-c3 svc-2756x512-c3 pca-12000x511-c2-p8 pca-12000x512-c2-p8; do
  env -u MLXLEARN_FORCE_BACKEND MTL_CAPTURE_ENABLED=1 \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_fit_inference.py "$case" "$out/$case" "$out/probe.dylib" \
    --mode auto --config scripts/crossover-shape.yaml > "$out/$case.json"
done
```

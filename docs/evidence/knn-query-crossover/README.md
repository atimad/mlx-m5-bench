# KNN query-batch routing crossover on the M5 Pro

The dataset has 4,096 rows, 32 float32 features and two classes. Both cases use byte-identical 3,072 training rows, Euclidean distance, uniform voting and five neighbors. The four-row query is the prefix of the five-row query from the same held-out split. Scaling is fitted on the training set. Seed is 42. The crossover is specific to this shape and mlx-learn 0.1.2.

With at most 32 features and neighbors, this shape takes the small-query CPU branch when the batch has at most four rows and training rows times query rows is at most 16,384. Four queries give 12,288 products. Five give 15,360, so the batch count changes the decision while both stay below the product cap. The alternative small-training-set and data-dependent branches are outside this shape. [Pinned routing source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_kernels/distance.py#L151-L175)

Timing was uninstrumented in four serial blocks ordered auto → forced → forced → auto. Each block used its own scikit-learn controls, four requested CPU threads, one warmup and 15 steady fresh fits with one prediction per model. The first call is recorded separately. Scikit-learn runs before its corresponding candidate. All 120 steady timing pairs passed.

## Timings and Metal evidence

Times are milliseconds, summarized as the median of the two block medians for each mode. Each CPU column uses the matching scikit-learn controls. Buffers come from separate fit and first-prediction Metal replays of auto and forced MLX.

| Query rows | Operation | scikit-learn (auto blocks) | Auto | scikit-learn (forced blocks) | Forced | Metal buffers auto / forced |
|---:|---|---:|---:|---:|---:|---:|
| 4 | fit | 0.184 | 0.196 | 0.177 | 0.215 | 0 / 0 |
| 4 | predict | 0.256 | 0.128 | 0.250 | 0.656 | 0 / 1 |
| 5 | fit | 0.172 | 0.208 | 0.174 | 0.214 | 0 / 0 |
| 5 | predict | 0.236 | 0.566 | 0.254 | 0.677 | 1 / 1 |

Automatic prediction took the CPU path at four queries (0.128 ms) and the GPU path at five (0.566 ms). The five-row GPU call was slower than its scikit-learn control (0.236 ms). Forced MLX used the GPU at both sizes, with prediction at 0.656 and 0.677 ms. This is a routing boundary. It does not locate the latency break-even point. In particular, the measurements cover the first query on each fresh model, including any deferred preparation, and the two batches differ by one row.

All traced fit windows and all scikit-learn controls recorded zero Metal submissions. For both auto cases, fit diagnostics report CPU storage and the query event reports the routing actually selected. The GPU query replays produced one completed command buffer each, and separate captures record checksums and shader symbols. All four traced comparisons passed numerical parity. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

## Evidence and reproduction

[Comparison JSON](comparison.json) includes per-block medians, dispersion, backend classifications, and CPU/candidate ratios.

- routing-1-auto: [manifest](20261114T202539095633Z-864b74abea/manifest.json), [raw timings](20261114T202539095633Z-864b74abea/measurements.json), [summary](20261114T202539095633Z-864b74abea/summary.md)
- routing-2-forced: [manifest](20261114T202542981202Z-c2ecb6c8dd/manifest.json), [raw timings](20261114T202542981202Z-c2ecb6c8dd/measurements.json), [summary](20261114T202542981202Z-c2ecb6c8dd/summary.md)
- routing-3-forced: [manifest](20261114T202546679338Z-c2ecb6c8dd/manifest.json), [raw timings](20261114T202546679338Z-c2ecb6c8dd/measurements.json), [summary](20261114T202546679338Z-c2ecb6c8dd/summary.md)
- routing-4-auto: [manifest](20261114T202550286912Z-864b74abea/manifest.json), [raw timings](20261114T202550286912Z-864b74abea/measurements.json), [summary](20261114T202550286912Z-864b74abea/summary.md)

Trace metadata and TSVs:

- auto, 4 rows: [metadata](metal/auto-q4/metadata.json), [fit](metal/auto-q4/mlxlearn-fit.tsv), [predict](metal/auto-q4/mlxlearn-predict.tsv), [scikit-learn predict](metal/auto-q4/sklearn-predict.tsv)
- forced, 4 rows: [metadata](metal/forced-q4/metadata.json), [fit](metal/forced-q4/mlxlearn-fit.tsv), [predict](metal/forced-q4/mlxlearn-predict.tsv), [scikit-learn predict](metal/forced-q4/sklearn-predict.tsv)
- auto, 5 rows: [metadata](metal/auto-q5/metadata.json), [fit](metal/auto-q5/mlxlearn-fit.tsv), [predict](metal/auto-q5/mlxlearn-predict.tsv), [scikit-learn predict](metal/auto-q5/sklearn-predict.tsv)
- forced, 5 rows: [metadata](metal/forced-q5/metadata.json), [fit](metal/forced-q5/mlxlearn-fit.tsv), [predict](metal/forced-q5/mlxlearn-predict.tsv), [scikit-learn predict](metal/forced-q5/sklearn-predict.tsv)

Run sequentially with the locked Apple Silicon environment and fresh output directories. Raw capture bundles remain in the ignored local results directory.

```sh
config=scripts/knn-query-crossover.yaml
.venv/bin/python scripts/benchmark_routing.py results/knn-query-replay --config "$config"
.venv/bin/python scripts/summarize_routing.py results/knn-query-replay/*
out=results/knn-query-metal-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for q in 4 5; do
  case_key="knn-4096x32-c2-k5-q$q"
  env -u MLXLEARN_FORCE_BACKEND MTL_CAPTURE_ENABLED=1 \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_fit_inference.py "$case_key" "$out/auto-q$q" \
    "$out/probe.dylib" --mode auto --config "$config" > "$out/auto-q$q.json"
  MTL_CAPTURE_ENABLED=1 MLXLEARN_FORCE_BACKEND=mlx \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_fit_inference.py "$case_key" "$out/forced-q$q" \
    "$out/probe.dylib" --mode forced --config "$config" > "$out/forced-q$q.json"
done
```

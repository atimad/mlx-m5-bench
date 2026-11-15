# Warmed KNN at the small-query GPU shape cutoffs on M5 Pro

With 32 features and k=8, auto and forced GPU used the same search path at each shape. At 128 queries, the small-query kernel ran with 2,047 and 2,048 training rows, and fused screen search ran at 2,049. At 2,048 training rows, the small-query kernel ran with 255 and 256 queries, and fused screen search ran at 257. Auto selected the GPU at every tested shape. [Pinned device search rules](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn_device/_neighbors.py) · [Automatic routing rule](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_kernels/distance.py#L151-L175)

## Warmed prediction latency

| Training rows | Query rows | GPU search, auto and forced | Auto (ms) | Forced GPU (ms) | Pinned MLX CPU (ms) | scikit-learn (ms), auto / forced / CPU | Wins vs scikit-learn, auto / forced |
|---:|---:|---|---:|---:|---:|---:|---:|
| 2047 | 128 | Small-query | 0.484 | 0.851 | 11.733 | 0.438 / 0.443 / 0.488 | 0/2 / 0/2 |
| 2048 | 128 | Small-query | 0.870 | 0.834 | 11.688 | 0.456 / 0.449 / 0.449 | 0/2 / 0/2 |
| 2049 | 128 | Fused screen | 0.664 | 0.841 | 11.760 | 0.558 / 0.503 / 0.490 | 0/2 / 0/2 |
| 2048 | 255 | Small-query | 0.692 | 0.953 | 20.822 | 0.712 / 0.690 / 0.680 | 1/2 / 0/2 |
| 2048 | 256 | Small-query | 0.929 | 0.977 | 20.289 | 0.670 / 0.727 / 0.693 | 0/2 / 0/2 |
| 2048 | 257 | Fused screen | 1.035 | 1.000 | 20.457 | 0.718 / 0.673 / 0.730 | 0/2 / 0/2 |

Timings are the median of two block medians. Each scikit-learn value is paired with one mlx-learn mode. Wins count passes with a lower median. Both GPU modes beat pinned MLX CPU in both passes at every shape. Auto beat its scikit-learn control in one pass at 255 queries, and scikit-learn won the other pass. Every other scikit-learn comparison favored scikit-learn in both passes. The kernel switches did not produce a consistent change in end-to-end latency across modes.

The six blocks run auto → forced GPU → pinned MLX CPU → pinned MLX CPU → forced GPU → auto. Each block requests four CPU threads and includes a fresh scikit-learn control. Each shape and implementation fits once, predicts once, warms up once more, then times 15 steady predictions on that fitted model. All 540 steady timing pairs passed numerical checks.

The [benchmark profile](../../../scripts/knn-small-shape-sweep.yaml) reuses the seed-42 split of the 16,384-row, 33-feature source and selects the first 32 features. Each training size uses a prefix of the same split and fits its own scaler. At 2,048 training rows the standardized training data are identical and the query batches are nested prefixes. Every mode uses Euclidean distance and uniform votes.

## Metal dispatch verification

Separate replays trace one warmed prediction for every shape and mlx-learn mode, each with a scikit-learn control. In both GPU modes, the small-query path encoded three dispatches including `mlxlearn_small_neighbors` and voting. Fused screen search encoded five dispatches including `mlxlearn_screen_scan`, merge, finish, and voting. Each GPU prediction completed one Metal command buffer. All fit windows, pinned MLX CPU predictions, and scikit-learn predictions recorded zero Metal submissions. All 18 traced comparisons passed numerical parity. Dispatch logs identify the pipelines. Completion logs record GPU timestamps for the command buffer.

- Auto at 128 queries · [2,048 training rows](metal/auto-t2048-q128/mlxlearn-predict-dispatch.tsv) and [2,049 training rows](metal/auto-t2049-q128/mlxlearn-predict-dispatch.tsv)
- Auto at 2,048 training rows · [256 queries](metal/auto-t2048-q256/mlxlearn-predict-dispatch.tsv) and [257 queries](metal/auto-t2048-q257/mlxlearn-predict-dispatch.tsv)
- [All dispatch, completion, and control traces](metal/)

## Raw data and reproduction

[Comparison JSON](comparison.json) contains block-level medians, dispersion, and paired ratios. The [timing runs](runs/) contain manifests, measurements, and summaries. The trace metadata links each replay to its timing runs.

Use the locked Apple Silicon environment and fresh output directories. Run timing before tracing.

```sh
config=scripts/knn-small-shape-sweep.yaml
.venv/bin/python scripts/benchmark_routing.py results/knn-small-shape-timing-replay \
  --config "$config" --with-mlx-cpu
.venv/bin/python scripts/summarize_routing.py results/knn-small-shape-timing-replay/*

out=results/knn-small-shape-metal-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for mode in cpu auto forced; do
  if [ "$mode" = forced ]; then export MLXLEARN_FORCE_BACKEND=mlx; else unset MLXLEARN_FORCE_BACKEND; fi
  for shape in 2047:128 2048:128 2049:128 2048:255 2048:256 2048:257; do
    n="${shape%:*}"
    q="${shape#*:}"
    tag="$mode-t$n-q$q"
    MTL_CAPTURE_ENABLED=1 VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
      .venv/bin/python scripts/trace_fit_inference.py "knn-16384x32-c2-k8-t$n-s33-q$q" \
      "$out/$tag" "$out/probe.dylib" --mode "$mode" --reuse-model \
      --config "$config" --completion-only --dispatches > "$out/$tag.json"
  done
done
unset MLXLEARN_FORCE_BACKEND
```

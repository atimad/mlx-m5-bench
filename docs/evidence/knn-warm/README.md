# Warmed KNN prediction crossover on the M5 Pro

With the same fitted model reused across predictions, the forced-GPU versus pinned-MLX-CPU break-even fell **between three and four query rows**. At three rows, GPU lost in both passes (0.645 ms GPU versus 0.547 ms pinned CPU). At four rows, GPU won in both passes (0.669 versus 0.784 ms in the small-batch panel), and won again in the independent broad panel. Forced GPU beat pinned CPU in both passes at every larger size tested. In the [first-prediction sweep](../knn-explicit-cpu/README.md), forced GPU had won even at one row. That panel used a fresh fit before every measured prediction.

Automatic mode still used its separate host path through four rows. At four rows, it took 0.122 ms in the small-batch panel and beat both pinned modes and scikit-learn. At five rows it used GPU, with 0.616 ms versus 0.954 ms for pinned MLX CPU and 0.248 ms for the corresponding scikit-learn control.

Against scikit-learn, the broad warmed sweep found two-pass wins at 384 and 512 rows for forced GPU, with a split automatic result at each. The separate 384-row refinement produced split or losing results against scikit-learn. Both GPU modes beat scikit-learn in both broad-sweep passes at 768 and 1,024 rows. These are observed bounds for the tested workload and runtime conditions. Each mode has two blocks, so the study does not estimate a confidence interval or a general crossover.

## Workload and method

The broad sweep, refinement and small-batch profiles repeat the same 21 distinct query sizes and all dataset fingerprints from the [first-prediction panel](../knn-explicit-cpu/README.md). Training is fixed at 3,072 rows with 32 float32 features, binary labels, Euclidean distance, uniform voting and k=5. Query batches are ordered prefixes of the same held-out split.

Each panel repeats the six-block order auto → forced GPU → pinned CPU → pinned CPU → forced GPU → auto. Each block requests four CPU threads and runs its scikit-learn control first. For each batch size and implementation, a single fresh fit is followed by a separately recorded first prediction, one untimed-for-summary warmup prediction, and 15 steady predictions on the same model and query input. Fit cost, the first call, and warmup are excluded from steady medians. Probability checks run after all measured predictions. Timing uses the existing synchronization policy and no Metal instrumentation. All 2,160 steady scikit-learn/candidate pairs passed numerical checks.

Explicit `device="cpu"` uses MLX's fixed CPU implementation. Auto's one- to four-row queries use a distinct host implementation. Forced GPU requests `device="gpu"` with the MLX override. These comparisons concern the three public execution modes and the scikit-learn CPU control for this shape and release. [Pinned classifier source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/neighbors/_classification.py#L130-L178)

## Prediction timings

Times are milliseconds and summarize the median of the two block medians per mode. The three scikit-learn values are the controls for the auto, forced GPU and pinned CPU blocks. A win means the GPU mode had a lower median than pinned CPU in the same pass. Auto's host results are labeled CPU in that column.

### Sweep

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | Pinned MLX CPU | GPU wins vs MLX CPU, auto / forced |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.238 / 0.250 / 0.247 | 0.118 | 0.462 | 0.823 | CPU · 2/2 |
| 5 | 0.248 / 0.261 / 0.244 | 0.616 | 0.610 | 0.954 | 2/2 · 2/2 |
| 8 | 0.253 / 0.256 / 0.248 | 0.611 | 0.716 | 1.466 | 2/2 · 2/2 |
| 16 | 0.262 / 0.255 / 0.263 | 0.551 | 0.654 | 2.798 | 2/2 · 2/2 |
| 32 | 0.302 / 0.309 / 0.310 | 0.620 | 0.511 | 5.559 | 2/2 · 2/2 |
| 48 | 0.320 / 0.327 / 0.345 | 0.410 | 0.757 | 7.933 | 2/2 · 2/2 |
| 64 | 0.382 / 0.366 / 0.379 | 0.717 | 0.784 | 9.878 | 2/2 · 2/2 |
| 96 | 0.424 / 0.427 / 0.447 | 0.876 | 0.849 | 13.894 | 2/2 · 2/2 |
| 128 | 0.484 / 0.514 / 0.513 | 0.529 | 0.745 | 18.521 | 2/2 · 2/2 |
| 192 | 0.645 / 0.647 / 0.696 | 0.934 | 0.650 | 26.121 | 2/2 · 2/2 |
| 256 | 0.781 / 0.824 / 0.819 | 0.943 | 0.968 | 31.699 | 2/2 · 2/2 |
| 384 | 1.076 / 1.164 / 1.151 | 0.954 | 1.080 | 48.122 | 2/2 · 2/2 |
| 512 | 1.380 / 1.586 / 1.492 | 1.367 | 1.028 | 64.515 | 2/2 · 2/2 |
| 768 | 2.000 / 1.991 / 2.187 | 0.959 | 1.488 | 95.390 | 2/2 · 2/2 |
| 1024 | 2.655 / 2.545 / 2.868 | 1.650 | 0.944 | 126.870 | 2/2 · 2/2 |

### Refine

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | Pinned MLX CPU | GPU wins vs MLX CPU, auto / forced |
|---:|---:|---:|---:|---:|---:|
| 256 | 0.812 / 0.782 / 0.795 | 1.097 | 0.844 | 31.038 | 2/2 · 2/2 |
| 288 | 0.872 / 0.864 / 0.880 | 0.865 | 0.972 | 34.926 | 2/2 · 2/2 |
| 320 | 0.953 / 1.167 / 0.942 | 1.059 | 1.173 | 38.785 | 2/2 · 2/2 |
| 352 | 1.009 / 1.041 / 0.994 | 1.063 | 1.096 | 42.290 | 2/2 · 2/2 |
| 384 | 1.091 / 1.079 / 1.098 | 1.266 | 1.156 | 46.394 | 2/2 · 2/2 |

### Small

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | Pinned MLX CPU | GPU wins vs MLX CPU, auto / forced |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.221 / 0.219 / 0.217 | 0.091 | 0.631 | 0.297 | CPU · 0/2 |
| 2 | 0.231 / 0.234 / 0.266 | 0.100 | 0.673 | 0.414 | CPU · 0/2 |
| 3 | 0.233 / 0.239 / 0.248 | 0.106 | 0.645 | 0.547 | CPU · 0/2 |
| 4 | 0.263 / 0.235 / 0.238 | 0.122 | 0.669 | 0.784 | CPU · 2/2 |

## Independent Metal verification

Separate command-completion traces cover the warmed prediction path in all three modes at all 21 distinct batch sizes. Each replay fits a model, makes two predictions outside the observation window, then traces a further prediction on that model. All pinned CPU and scikit-learn predictions submitted zero Metal command buffers. Automatic mode submitted zero at 1–4 rows and one at every tested size from five rows upward. Forced GPU submitted one for every warmed prediction, including at three and four rows. All 63 trace pairs passed numerical checks. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

- Three rows: [pinned CPU](metal/cpu-q3/metadata.json), [forced GPU](metal/forced-q3/metadata.json), [auto](metal/auto-q3/metadata.json)
- Four rows: [pinned CPU](metal/cpu-q4/metadata.json), [forced GPU](metal/forced-q4/metadata.json), [auto](metal/auto-q4/metadata.json)
- Five rows: [pinned CPU](metal/cpu-q5/metadata.json), [forced GPU](metal/forced-q5/metadata.json), [auto](metal/auto-q5/metadata.json)
- [All trace directories](metal/)

## Raw data and reproduction

Each panel has six run directories with manifests, raw timings and correctness records. Comparison JSON contains each block's medians and dispersion, ratios against scikit-learn, and per-pass ratios against pinned MLX CPU.

- [Broad sweep comparison](sweep/comparison.json)
- [Refinement comparison](refine/comparison.json)
- [Small-batch comparison](small/comparison.json)

Run timing first, then tracing, in the locked Apple Silicon environment. Use fresh output directories.

```sh
for panel in sweep refine small; do
  .venv/bin/python scripts/benchmark_routing.py "results/knn-warm-$panel-replay" \
    --config "scripts/knn-query-$panel.yaml" --with-mlx-cpu --reuse-model
  .venv/bin/python scripts/summarize_routing.py "results/knn-warm-$panel-replay"/*
done

out=results/knn-warm-metal-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for mode in cpu auto forced; do
  if [ "$mode" = forced ]; then export MLXLEARN_FORCE_BACKEND=mlx; else unset MLXLEARN_FORCE_BACKEND; fi
  for q in 1 2 3 4 5 8 16 32 48 64 96 128 192 256 288 320 352 384 512 768 1024; do
    case "$q" in
      1|2|3) panel=small ;;
      288|320|352) panel=refine ;;
      *) panel=sweep ;;
    esac
    MTL_CAPTURE_ENABLED=1 VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
      .venv/bin/python scripts/trace_fit_inference.py "knn-4096x32-c2-k5-q$q" \
      "$out/$mode-q$q" "$out/probe.dylib" --mode "$mode" \
      --config "scripts/knn-query-$panel.yaml" --completion-only --reuse-model \
      > "$out/$mode-q$q.json"
  done
done
unset MLXLEARN_FORCE_BACKEND
```

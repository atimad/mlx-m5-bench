# Explicit MLX CPU versus GPU KNN on the M5 Pro

Forced GPU beat explicitly pinned MLX CPU in both passes at every tested batch size, including the one-row minimum. The one-row medians were **0.334 ms GPU and 0.360 ms pinned CPU**. The paired speed ratios were 1.07× and 1.08×, so the observed margin was small. The sweep found no CPU-to-GPU break-even within the tested range of 1–1,024 rows for those two modes.

Automatic mode used its own CPU path for batches of one through four rows. It was faster than forced GPU and pinned CPU at each of those sizes. At five rows, automatic mode used GPU and beat pinned CPU in both passes, as it did at every larger tested size. The automatic routing switch was at five rows. The earlier [scikit-learn comparison](../knn-query-sweep/README.md) measures a different baseline. For example, at five rows scikit-learn still beat both GPU modes in this repeat.

A follow-up repeats the panel with [warmed predictions on the same fitted model](../knn-warm/README.md).

## Workload and method

All modes use the same 3,072 training rows, 32 float32 features, binary labels, Euclidean distance, uniform voting and k=5. The query sets are nested prefixes of the same held-out pool. Training-feature and label fingerprints match across all sizes. The 18 shared query cases also match the complete dataset fingerprints from the [earlier sweep](../knn-query-sweep/README.md). The only new batch sizes are 1, 2 and 3, with 4 repeated as an anchor.

Each panel ran six blocks in the order auto → forced GPU → pinned CPU → pinned CPU → forced GPU → auto. This gives each mode one block in each pass and balances its average position. Blocks use four requested CPU threads, a fresh scikit-learn control run first and 15 steady repetitions per implementation. Each prediction is the first call on a freshly fitted model after runtime warmup and includes any lazy query preparation. Fit, cold calls, warmups and steady calls are recorded separately. All 2,160 steady scikit-learn/candidate pairs passed numerical checks. Runner code was unchanged across the runs. Some manifests record a dirty tree while evidence tooling and the small-batch profile were being drafted.

Pinned CPU sets `device="cpu"` with the forced-backend override unset. It takes the fixed MLX CPU search and voting path. Auto can use a distinct owned host search and NumPy voting on small queries. Forced GPU sets `device="gpu"` and `MLXLEARN_FORCE_BACKEND=mlx`. This is a same-library comparison of public execution modes, with different search implementations and preparation costs. It does not measure the speed of identical kernels on different processors. [Pinned KNN classifier source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/neighbors/_classification.py#L130-L178) · [Pinned device search source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn_device/_neighbors.py)

## Prediction timings

Times are milliseconds, summarized as the median of the two block medians per mode. The three scikit-learn values come from the controls for the auto, forced GPU and pinned CPU blocks respectively. A win means the GPU-mode median was lower than the pinned CPU median in the same pass. Auto's CPU results are labeled CPU in the wins column.

### Sweep

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | Pinned MLX CPU | GPU wins vs MLX CPU, auto / forced |
|---:|---:|---:|---:|---:|---:|
| 4 | 0.250 / 0.238 / 0.246 | 0.118 | 0.440 | 0.717 | CPU · 2/2 |
| 5 | 0.233 / 0.248 / 0.231 | 0.514 | 0.510 | 0.866 | 2/2 · 2/2 |
| 8 | 0.244 / 0.240 / 0.299 | 0.574 | 0.447 | 1.433 | 2/2 · 2/2 |
| 16 | 0.251 / 0.260 / 0.320 | 0.521 | 0.548 | 2.731 | 2/2 · 2/2 |
| 32 | 0.294 / 0.494 / 0.293 | 0.384 | 0.509 | 5.327 | 2/2 · 2/2 |
| 48 | 0.322 / 0.363 / 0.331 | 0.405 | 0.530 | 7.667 | 2/2 · 2/2 |
| 64 | 0.352 / 0.368 / 0.365 | 0.442 | 0.413 | 9.428 | 2/2 · 2/2 |
| 96 | 0.422 / 0.473 / 0.429 | 0.553 | 0.436 | 13.181 | 2/2 · 2/2 |
| 128 | 0.578 / 0.551 / 0.492 | 0.678 | 0.511 | 17.810 | 2/2 · 2/2 |
| 192 | 0.635 / 0.644 / 0.642 | 0.530 | 0.592 | 25.028 | 2/2 · 2/2 |
| 256 | 0.757 / 0.758 / 0.770 | 0.618 | 0.584 | 30.459 | 2/2 · 2/2 |
| 384 | 1.031 / 1.079 / 1.080 | 0.599 | 0.943 | 45.451 | 2/2 · 2/2 |
| 512 | 1.367 / 1.385 / 1.366 | 0.742 | 0.695 | 61.545 | 2/2 · 2/2 |
| 768 | 1.926 / 1.969 / 1.958 | 0.847 | 0.558 | 90.911 | 2/2 · 2/2 |
| 1024 | 2.560 / 2.587 / 2.579 | 0.822 | 0.599 | 120.652 | 2/2 · 2/2 |

### Refine

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | Pinned MLX CPU | GPU wins vs MLX CPU, auto / forced |
|---:|---:|---:|---:|---:|---:|
| 256 | 0.762 / 0.827 / 0.756 | 0.530 | 0.549 | 30.003 | 2/2 · 2/2 |
| 288 | 0.890 / 0.843 / 0.848 | 0.631 | 0.407 | 36.009 | 2/2 · 2/2 |
| 320 | 0.938 / 0.933 / 0.928 | 0.489 | 0.640 | 37.795 | 2/2 · 2/2 |
| 352 | 1.025 / 1.005 / 1.005 | 0.687 | 0.778 | 41.449 | 2/2 · 2/2 |
| 384 | 1.056 / 1.072 / 1.037 | 0.650 | 0.672 | 45.048 | 2/2 · 2/2 |

### Small

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | Pinned MLX CPU | GPU wins vs MLX CPU, auto / forced |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.277 / 0.244 / 0.249 | 0.097 | 0.334 | 0.360 | CPU · 2/2 |
| 2 | 0.282 / 0.333 / 0.262 | 0.101 | 0.346 | 0.514 | CPU · 2/2 |
| 3 | 0.259 / 0.257 / 0.264 | 0.116 | 0.410 | 0.641 | CPU · 2/2 |
| 4 | 0.266 / 0.257 / 0.251 | 0.125 | 0.315 | 0.813 | CPU · 2/2 |

## Independent Metal verification

Separate command-completion traces cover all three modes at all 21 distinct query sizes. Every pinned CPU fit and prediction submitted zero Metal buffers. Auto submitted zero in fit and during predictions of one through four rows, and one during predictions of five rows and above. Forced GPU submitted zero in fit and one in every prediction. Every scikit-learn control window recorded zero submissions. All 63 traced comparisons passed numerical parity. Completion-only traces retain operation-scoped Metal start and end times. The latency measurements ran without this instrumentation. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

- One row: [pinned CPU trace](metal/cpu-q1/metadata.json), [forced GPU trace](metal/forced-q1/metadata.json), [automatic trace](metal/auto-q1/metadata.json)
- Five rows: [pinned CPU trace](metal/cpu-q5/metadata.json), [forced GPU trace](metal/forced-q5/metadata.json), [automatic trace](metal/auto-q5/metadata.json)
- [All trace directories](metal/)

## Evidence and reproduction

Each panel directory has six run manifests, all timing and correctness records, and summaries. The comparison JSON includes timings per block, dispersion, and the same-library ratios for both passes.

- [Broad sweep comparison](sweep/comparison.json)
- [Refinement comparison](refine/comparison.json)
- [Small-batch comparison](small/comparison.json)

Run timing first, then tracing, in the locked Apple Silicon environment. Use fresh output directories.

```sh
for panel in sweep refine small; do
  .venv/bin/python scripts/benchmark_routing.py "results/knn-cpu-$panel-replay" \
    --config "scripts/knn-query-$panel.yaml" --with-mlx-cpu
  .venv/bin/python scripts/summarize_routing.py "results/knn-cpu-$panel-replay"/*
done

out=results/knn-cpu-metal-replay
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
      --config "scripts/knn-query-$panel.yaml" --completion-only > "$out/$mode-q$q.json"
  done
done
unset MLXLEARN_FORCE_BACKEND
```

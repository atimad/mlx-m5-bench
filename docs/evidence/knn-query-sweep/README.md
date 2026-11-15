# KNN query-batch latency sweep on the M5 Pro

With 3,072 fixed training rows, 32 features and five neighbors, the first size where automatic GPU prediction beat scikit-learn in both refinement blocks was **320 queries**. At 288 the automatic result split between blocks. Forced MLX won both refinement blocks at 288, but its 256-row result reversed between the broad and refinement panels. The data support a range for the latency crossover under this setup. The exact boundary varies with the run.

In the broad sweep, forced MLX beat scikit-learn in both blocks from 384 through all larger tested batches. Automatic GPU prediction did so from 512 through all larger tested batches. At 384, the broad automatic blocks split and the refinement automatic blocks both won. An isolated win at 96 in one block per mode did not persist at 128 or 192.

## Workload and method

This uses the same fixed 3,072 training rows, binary labels, 32 float32 features, Euclidean distance, uniform voting and k=5 as the [four-to-five routing experiment](../knn-query-crossover/README.md). Query batches are ordered prefixes of the same held-out pool. The combined training-feature and label SHA-256 is recorded in every trace. The 1,024-row batch uses the entire held-out split.

The broad sweep covers 15 sizes from 4 to 1,024. The follow-up adds 288, 320 and 352 and repeats 256 and 384 as anchors. Each panel ran uninstrumented auto → forced → forced → auto blocks on the M5 Pro, using independent scikit-learn controls run first and four requested CPU threads. Each block ran 15 steady repetitions per implementation, with a fresh fit before each prediction. First-prediction latency includes any deferred query preparation, and fit time is recorded separately in the raw data. There are 1,200 steady timing pairs across both panels. All passed the numerical checks.

The CPU comparison is scikit-learn brute force. The auto CPU result at four rows uses mlx-learn’s own search and is identified separately. The study does not establish a same-library CPU-versus-GPU break-even for larger queries.

## Prediction latency

Times are milliseconds, shown as the median of the two block medians for each mode. The paired CPU column shows the controls for auto and forced, respectively. Wins count how many of the two block-level candidate medians beat their paired scikit-learn median.

### Broad sweep

| Query rows | scikit-learn, auto / forced | Auto | Forced MLX | Wins, auto / forced |
|---:|---:|---:|---:|---:|
| 4 | 0.242 / 0.236 | 0.129 | 0.633 | 2/2 · 0/2 |
| 5 | 0.246 / 0.238 | 0.470 | 0.714 | 0/2 · 0/2 |
| 8 | 0.248 / 0.240 | 0.667 | 0.718 | 0/2 · 0/2 |
| 16 | 0.257 / 0.268 | 0.692 | 0.769 | 0/2 · 0/2 |
| 32 | 0.306 / 0.295 | 0.407 | 0.695 | 0/2 · 0/2 |
| 48 | 0.315 / 0.315 | 0.770 | 0.748 | 0/2 · 0/2 |
| 64 | 0.369 / 0.369 | 0.594 | 0.773 | 0/2 · 0/2 |
| 96 | 0.439 / 0.450 | 0.592 | 0.619 | 1/2 · 1/2 |
| 128 | 0.506 / 0.494 | 0.864 | 0.854 | 0/2 · 0/2 |
| 192 | 0.653 / 0.641 | 0.826 | 0.818 | 0/2 · 0/2 |
| 256 | 0.800 / 0.813 | 0.917 | 0.864 | 0/2 · 0/2 |
| 384 | 1.076 / 1.103 | 1.072 | 0.858 | 1/2 · 2/2 |
| 512 | 1.410 / 1.370 | 0.929 | 0.780 | 2/2 · 2/2 |
| 768 | 2.029 / 2.165 | 1.124 | 0.707 | 2/2 · 2/2 |
| 1024 | 2.605 / 2.712 | 0.842 | 0.816 | 2/2 · 2/2 |

### Refinement

| Query rows | scikit-learn, auto / forced | Auto | Forced MLX | Wins, auto / forced |
|---:|---:|---:|---:|---:|
| 256 | 0.805 / 1.003 | 0.878 | 0.761 | 0/2 · 2/2 |
| 288 | 0.905 / 0.906 | 0.913 | 0.830 | 1/2 · 2/2 |
| 320 | 0.956 / 0.960 | 0.683 | 0.666 | 2/2 · 2/2 |
| 352 | 1.057 / 1.046 | 0.745 | 0.849 | 2/2 · 2/2 |
| 384 | 1.087 / 1.130 | 0.485 | 0.647 | 2/2 · 2/2 |

## Independent Metal verification

Separate operation-scoped Metal command-buffer traces cover both modes at all 18 distinct batch sizes. Automatic mode submitted zero buffers at four rows and one at every larger tested size. Forced MLX submitted one at every tested size. All timed-shape fit replays and scikit-learn controls recorded zero buffers. All 36 traced pairs passed numerical checks. The observer records GPU start and completion times; capture bundles are omitted in this panel. [Metal timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

[Automatic 320-row trace](metal/auto-q320/metadata.json) · [Forced 288-row trace](metal/forced-q288/metadata.json) · [All operation traces](metal/)

## Raw evidence and reproduction

- [sweep comparison JSON](sweep/comparison.json)
  - routing-1-auto: [manifest](sweep/20261115T021017595701Z-928e4943e4/manifest.json), [measurements](sweep/20261115T021017595701Z-928e4943e4/measurements.json)
  - routing-2-forced: [manifest](sweep/20261115T021042452083Z-3830657d57/manifest.json), [measurements](sweep/20261115T021042452083Z-3830657d57/measurements.json)
  - routing-3-forced: [manifest](sweep/20261115T021105668480Z-3830657d57/manifest.json), [measurements](sweep/20261115T021105668480Z-3830657d57/measurements.json)
  - routing-4-auto: [manifest](sweep/20261115T021129434357Z-928e4943e4/manifest.json), [measurements](sweep/20261115T021129434357Z-928e4943e4/measurements.json)
- [refine comparison JSON](refine/comparison.json)
  - routing-1-auto: [manifest](refine/20261115T021221536880Z-8ca11f5d4c/manifest.json), [measurements](refine/20261115T021221536880Z-8ca11f5d4c/measurements.json)
  - routing-2-forced: [manifest](refine/20261115T021230551932Z-22655013c3/manifest.json), [measurements](refine/20261115T021230551932Z-22655013c3/measurements.json)
  - routing-3-forced: [manifest](refine/20261115T021239310618Z-22655013c3/manifest.json), [measurements](refine/20261115T021239310618Z-22655013c3/measurements.json)
  - routing-4-auto: [manifest](refine/20261115T021247634714Z-8ca11f5d4c/manifest.json), [measurements](refine/20261115T021247634714Z-8ca11f5d4c/measurements.json)

Run timing, then tracing, with the locked Apple Silicon environment and fresh output directories.

```sh
for panel in sweep refine; do
  config="scripts/knn-query-$panel.yaml"
  .venv/bin/python scripts/benchmark_routing.py "results/knn-$panel-replay" --config "$config"
  .venv/bin/python scripts/summarize_routing.py "results/knn-$panel-replay"/*
done
out=results/knn-sweep-metal-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for mode in auto forced; do
  if [ "$mode" = forced ]; then export MLXLEARN_FORCE_BACKEND=mlx; else unset MLXLEARN_FORCE_BACKEND; fi
  for q in 4 5 8 16 32 48 64 96 128 192 256 288 320 352 384 512 768 1024; do
    case "$q" in 288|320|352) panel=refine ;; *) panel=sweep ;; esac
    MTL_CAPTURE_ENABLED=1 VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
      .venv/bin/python scripts/trace_fit_inference.py "knn-4096x32-c2-k5-q$q" \
      "$out/$mode-q$q" "$out/probe.dylib" --mode "$mode" \
      --config "scripts/knn-query-$panel.yaml" --completion-only > "$out/$mode-q$q.json"
  done
done
unset MLXLEARN_FORCE_BACKEND
```

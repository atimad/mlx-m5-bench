# Warmed KNN crossover by training-set size on the M5 Pro

Increasing the training set shifted the warmed latency crossover toward smaller query batches. A two-pass win means the GPU candidate beat the corresponding CPU median in both matched passes.

| Training rows | First auto GPU batch | First forced-GPU two-pass win vs pinned MLX CPU | First auto-GPU two-pass win vs pinned MLX CPU | First batch where both GPU modes won both passes vs scikit-learn |
|---:|---:|---:|---:|---:|
| 1,536 | 5 | 12 | 12 | 768 |
| 3,072 | 5 | 5 | 8 | 768 |
| 8,192 | 3 | 2 | 3 | 256 |

At 1,536 training rows, both GPU modes lost at eight queries in the broad sweep and split the eight-query refinement passes. Both won at 12 queries and every larger tested size against pinned MLX CPU. At 3,072 training rows, forced GPU split at four and won both passes at five. Auto GPU split at five and won both at eight. At 8,192 training rows, forced GPU lost both passes at one query and won both at two. Auto still used its faster host path at two queries.

At the first forced-GPU two-pass wins, forced GPU versus pinned CPU was 0.689 versus 0.947 ms at 1,536 training rows, 0.746 versus 0.867 ms at 3,072, and 0.728 versus 1.096 ms at 8,192. These are tested break-even ranges for this Mac and workload. Intermediate untimed batches and repeat sessions could move the observed boundaries.

Separate Metal traces confirmed the automatic switch from four to five queries at 1,536 and 3,072 rows, and from two to three at 8,192 rows. The pinned routing rule admits CPU at no more than four query rows and 16,384 training/query row pairs for this setup. The 8,192-row case reaches that product cap at two queries. [Pinned routing source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_kernels/distance.py#L151-L175)

A follow-up holds training at 3,072 rows and [varies width across the 32-feature routing gate](../knn-feature-sweep/README.md).

## Workload and timing design

All cases start from one seed-42, 16,384-row synthetic binary dataset with 32 features and a fixed 75/25 split. The training sizes 1,536, 3,072, and 8,192 are prefixes of the same unscaled training split. Each prefix gets its own training-only standardization. The query batches are prefixes of the same held-out rows, standardized using the corresponding training prefix. Training is byte-identical across query sizes within each group. The 3,072-row reference is drawn from this new shared split. Its data differ from the earlier [single-training-size sweep](../knn-warm/README.md). All cases use Euclidean distance, uniform voting and k=5.

The 13 common query sizes span 1–1,024 rows and include both sides of the routing boundary. A focused 1,536-row refinement adds batches of 12, 16 and 24, with 8 and 32 repeated as anchors. The uninstrumented timings use six blocks in auto → forced GPU → pinned MLX CPU → pinned MLX CPU → forced GPU → auto order. Each block requests four CPU threads and includes a fresh scikit-learn control. For each case and implementation, one fit precedes one first prediction, one additional warmup and 15 steady predictions on that model. Fit, first prediction and warmup are excluded from the steady median. Probability checks run after timing. All 3,960 steady scikit-learn/candidate timing pairs passed the numerical checks. Timings include output materialization and the runner's normal MLX synchronization.

Each result is the median of two block medians, in milliseconds. The scikit-learn column lists the corresponding controls for the auto, forced GPU and pinned CPU blocks. The final columns count how many paired medians for a given GPU mode beat the named baseline. Auto entries that used the CPU are marked CPU. The same-library timing comparison is between different execution paths in mlx-learn, including its explicit CPU path and its separate automatic host path.

## Prediction latency

### 1,536 training rows — sweep

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | MLX CPU | GPU wins vs MLX CPU, auto / forced | GPU wins vs scikit-learn, auto / forced |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.212 / 0.210 / 0.213 | 0.070 | 0.690 | 0.236 | CPU / 0/2 | CPU / 0/2 |
| 2 | 0.231 / 0.221 / 0.224 | 0.078 | 0.803 | 0.283 | CPU / 0/2 | CPU / 0/2 |
| 3 | 0.222 / 0.220 / 0.220 | 0.084 | 0.735 | 0.336 | CPU / 0/2 | CPU / 0/2 |
| 4 | 0.226 / 0.221 / 0.231 | 0.090 | 0.736 | 0.414 | CPU / 0/2 | CPU / 0/2 |
| 5 | 0.222 / 0.224 / 0.227 | 0.723 | 0.701 | 0.508 | 0/2 / 0/2 | 0/2 / 0/2 |
| 8 | 0.225 / 0.236 / 0.238 | 0.758 | 0.763 | 0.648 | 0/2 / 0/2 | 0/2 / 0/2 |
| 32 | 0.259 / 0.269 / 0.265 | 0.559 | 0.785 | 2.431 | 2/2 / 2/2 | 0/2 / 0/2 |
| 128 | 0.401 / 0.394 / 0.400 | 0.818 | 0.789 | 8.496 | 2/2 / 2/2 | 0/2 / 0/2 |
| 256 | 0.581 / 0.615 / 0.597 | 0.852 | 0.888 | 15.304 | 2/2 / 2/2 | 0/2 / 0/2 |
| 384 | 0.812 / 0.808 / 0.823 | 0.978 | 0.958 | 22.886 | 2/2 / 2/2 | 0/2 / 0/2 |
| 512 | 0.981 / 1.004 / 1.011 | 1.038 | 1.033 | 30.263 | 2/2 / 2/2 | 0/2 / 0/2 |
| 768 | 1.435 / 1.428 / 1.413 | 1.028 | 1.211 | 45.803 | 2/2 / 2/2 | 2/2 / 2/2 |
| 1024 | 1.853 / 1.843 / 1.813 | 1.393 | 1.144 | 60.484 | 2/2 / 2/2 | 2/2 / 2/2 |

### 3,072 training rows — sweep

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | MLX CPU | GPU wins vs MLX CPU, auto / forced | GPU wins vs scikit-learn, auto / forced |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.220 / 0.221 / 0.218 | 0.087 | 0.669 | 0.294 | CPU / 0/2 | CPU / 0/2 |
| 2 | 0.234 / 0.230 / 0.232 | 0.097 | 0.716 | 0.394 | CPU / 0/2 | CPU / 0/2 |
| 3 | 0.237 / 0.234 / 0.233 | 0.107 | 0.745 | 0.584 | CPU / 0/2 | CPU / 0/2 |
| 4 | 0.241 / 0.233 / 0.236 | 0.118 | 0.765 | 0.784 | CPU / 1/2 | CPU / 0/2 |
| 5 | 0.239 / 0.239 / 0.235 | 0.707 | 0.746 | 0.867 | 1/2 / 2/2 | 0/2 / 0/2 |
| 8 | 0.247 / 0.239 / 0.240 | 0.798 | 0.758 | 1.421 | 2/2 / 2/2 | 0/2 / 0/2 |
| 32 | 0.289 / 0.292 / 0.284 | 0.612 | 0.797 | 5.292 | 2/2 / 2/2 | 0/2 / 0/2 |
| 128 | 0.499 / 0.499 / 0.499 | 0.865 | 0.884 | 17.447 | 2/2 / 2/2 | 0/2 / 0/2 |
| 256 | 0.786 / 0.779 / 0.767 | 1.125 | 1.100 | 30.224 | 2/2 / 2/2 | 0/2 / 0/2 |
| 384 | 1.084 / 1.383 / 1.093 | 1.238 | 1.128 | 45.350 | 2/2 / 2/2 | 0/2 / 1/2 |
| 512 | 1.385 / 1.347 / 1.392 | 1.270 | 1.444 | 60.393 | 2/2 / 2/2 | 1/2 / 0/2 |
| 768 | 1.991 / 1.955 / 1.931 | 1.606 | 1.374 | 90.679 | 2/2 / 2/2 | 2/2 / 2/2 |
| 1024 | 2.579 / 2.544 / 2.546 | 1.178 | 1.070 | 121.005 | 2/2 / 2/2 | 2/2 / 2/2 |

### 8,192 training rows — sweep

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | MLX CPU | GPU wins vs MLX CPU, auto / forced | GPU wins vs scikit-learn, auto / forced |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.245 / 0.245 / 0.242 | 0.138 | 0.784 | 0.604 | CPU / 0/2 | CPU / 0/2 |
| 2 | 0.285 / 0.279 / 0.286 | 0.164 | 0.728 | 1.096 | CPU / 2/2 | CPU / 0/2 |
| 3 | 0.279 / 0.283 / 0.282 | 0.790 | 0.731 | 1.579 | 2/2 / 2/2 | 0/2 / 0/2 |
| 4 | 0.279 / 0.282 / 0.283 | 0.661 | 0.761 | 2.077 | 2/2 / 2/2 | 0/2 / 0/2 |
| 5 | 0.284 / 0.285 / 0.287 | 0.824 | 0.676 | 2.569 | 2/2 / 2/2 | 0/2 / 0/2 |
| 8 | 0.296 / 0.293 / 0.290 | 0.791 | 0.777 | 3.954 | 2/2 / 2/2 | 0/2 / 0/2 |
| 32 | 0.415 / 0.401 / 0.422 | 0.869 | 0.810 | 14.325 | 2/2 / 2/2 | 0/2 / 0/2 |
| 128 | 0.929 / 0.921 / 0.882 | 0.927 | 1.076 | 46.529 | 2/2 / 2/2 | 1/2 / 0/2 |
| 256 | 1.531 / 1.546 / 1.541 | 1.055 | 1.447 | 80.772 | 2/2 / 2/2 | 2/2 / 2/2 |
| 384 | 2.253 / 2.238 / 2.241 | 1.583 | 1.498 | 120.960 | 2/2 / 2/2 | 2/2 / 2/2 |
| 512 | 2.971 / 2.902 / 2.920 | 1.192 | 1.470 | 161.392 | 2/2 / 2/2 | 2/2 / 2/2 |
| 768 | 4.253 / 4.268 / 4.373 | 1.254 | 1.213 | 241.612 | 2/2 / 2/2 | 2/2 / 2/2 |
| 1024 | 5.630 / 5.683 / 5.728 | 1.425 | 1.161 | 322.415 | 2/2 / 2/2 | 2/2 / 2/2 |

### 1,536 training rows — refine

| Query rows | scikit-learn, auto / forced / CPU blocks | Auto | Forced GPU | MLX CPU | GPU wins vs MLX CPU, auto / forced | GPU wins vs scikit-learn, auto / forced |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 0.235 / 0.231 / 0.231 | 0.664 | 0.649 | 0.648 | 1/2 / 1/2 | 0/2 / 0/2 |
| 12 | 0.239 / 0.232 / 0.232 | 0.760 | 0.689 | 0.947 | 2/2 / 2/2 | 0/2 / 0/2 |
| 16 | 0.237 / 0.255 / 0.237 | 0.720 | 0.655 | 1.286 | 2/2 / 2/2 | 0/2 / 0/2 |
| 24 | 0.252 / 0.249 / 0.257 | 0.739 | 0.650 | 1.880 | 2/2 / 2/2 | 0/2 / 0/2 |
| 32 | 0.258 / 0.264 / 0.266 | 0.756 | 0.665 | 2.463 | 2/2 / 2/2 | 0/2 / 0/2 |

## Independent Metal evidence

Separate warmed fit/prediction command-completion replays covered 42 unique shapes in each of the three mlx-learn modes. Every prediction had two calls on the same fitted model before the trace window. Every forced prediction submitted GPU work. Auto did so at and above the batch switches in the table. All pinned CPU predictions, scikit-learn controls and fit windows recorded zero Metal submissions. All 126 traced comparisons passed numerical checks. The individual traces record Metal start/end timestamps, diagnostics and input fingerprints. Timed calls are in separate uninstrumented runs. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

- [Automatic 8,192-row CPU trace at two queries](metal/auto-t8192-q2/metadata.json) and [GPU trace at three](metal/auto-t8192-q3/metadata.json)
- [Forced GPU at eight queries with 1,536 training rows](metal/forced-t1536-q8/metadata.json) and [forced GPU at 12](metal/forced-t1536-q12/metadata.json)
- [All Metal trace directories](metal/)

## Raw data and reproduction

Each panel directory contains six manifests, timing records and run summaries. Comparison JSON also reports per-block timing dispersion and paired CPU ratios.

- [Broad sweep comparison](sweep/comparison.json)
- [1,536-row refinement comparison](refine/comparison.json)

Use the locked Apple Silicon environment and fresh output directories. Run timing and replay serially.

```sh
for panel in sweep refine; do
  .venv/bin/python scripts/benchmark_routing.py "results/knn-training-$panel-replay" \
    --config "scripts/knn-training-$panel.yaml" --with-mlx-cpu
  .venv/bin/python scripts/summarize_routing.py "results/knn-training-$panel-replay"/*
done

out=results/knn-training-metal-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for mode in cpu auto forced; do
  if [ "$mode" = forced ]; then export MLXLEARN_FORCE_BACKEND=mlx; else unset MLXLEARN_FORCE_BACKEND; fi
  for n in 1536 3072 8192; do
    batches="1 2 3 4 5 8 32 128 256 384 512 768 1024"
    if [ "$n" = 1536 ]; then batches="$batches 12 16 24"; fi
    for q in $(printf '%s\n' "$batches"); do
      case "$q" in 12|16|24) panel=refine ;; *) panel=sweep ;; esac
      tag="$mode-t$n-q$q"
      MTL_CAPTURE_ENABLED=1 VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
        .venv/bin/python scripts/trace_fit_inference.py "knn-16384x32-c2-k5-t$n-q$q" \
        "$out/$tag" "$out/probe.dylib" --mode "$mode" --reuse-model \
        --config "scripts/knn-training-$panel.yaml" --completion-only > "$out/$tag.json"
    done
  done
done
unset MLXLEARN_FORCE_BACKEND
```

The shell snippet uses POSIX field splitting for the batch list. Run it with Bash or another POSIX shell.

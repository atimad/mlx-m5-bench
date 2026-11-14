# M5 Pro Metal traces for KNN fit and index construction

The replay used the benchmark's forced-MLX configuration, MLX 0.32.4, mlx-learn 0.1.2, scikit-learn 1.9.1, seed 42 and four requested CPU threads. Both workloads use five neighbors, Euclidean distance, brute-force search and uniform voting. Input fingerprints and estimator parameters match the archived steady records. Sample counts in the table are before the train/test split.

| Workload | Training / test rows | mlx-learn fit buffers | mlx-learn first predict buffers | scikit-learn fit / predict buffers |
|---|---:|---:|---:|---:|
| Standard, 8,000 × 128, 3 classes | 6,000 / 2,000 | 0 | 1 | 0 / 0 |
| Full, 30,000 × 64, 2 classes | 22,500 / 7,500 | 0 | 7 | 0 / 0 |

**Neither fit window submitted a GPU command buffer.** This includes construction of the brute-force index and staging of the training features and encoded labels in MLX arrays. Unified-memory storage and an index configured for GPU queries can exist without GPU compute during fit. The pinned source has no tree construction for this route and puts search work and any lazy preparation required by the chosen path in the query. Depending on the path, the query can prepare Gram arrays, inspect geometry or pack training data. The aggregate query trace cannot attribute those stages individually. [Index construction](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_kernels/distance.py#L308-L333) · [Lazy query preparation](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn_device/_neighbors.py#L241-L276) · [Classifier fit and target staging](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/neighbors/_classification.py#L82-L125)

The runtime was warmed with a separate model. Each fit trace covers a new estimator's `fit` call, and each positive control covers that estimator's first `predict` call. Model construction, warmup and explicit synchronization are outside the windows. All observed prediction command buffers completed on the M5 Pro with positive GPU execution intervals. Separate one-frame prediction captures contain neighbor-search and voting shader symbols. Capture checksums and command-buffer times are recorded as replay evidence, separate from benchmark medians. [Apple Metal command-buffer timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

All 2,000 and 7,500 test labels matched scikit-learn in the two replays. The maximum probability difference was about 2.38e-8 for each. The fit finding applies to these workloads and this release. The original fit timings remain ineligible for a GPU speedup ratio.

| Workload | Metadata | mlx-learn completion traces | scikit-learn controls |
|---|---|---|---|
| Standard | [Metadata and capture checksum](knn/metadata.json) | [Fit](knn/mlxlearn-fit.tsv), [first prediction](knn/mlxlearn-predict.tsv) | [Fit](knn/sklearn-fit.tsv), [prediction](knn/sklearn-predict.tsv) |
| Full | [Metadata and capture checksum](knn-full/metadata.json) | [Fit](knn-full/mlxlearn-fit.tsv), [first prediction](knn-full/mlxlearn-predict.tsv) | [Fit](knn-full/sklearn-fit.tsv), [prediction](knn-full/sklearn-predict.tsv) |

## Reproduce

Run from the repository root with the locked Apple Silicon environment and Xcode Command Line Tools.

```sh
out=results/metal-knn-fit-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for case in knn knn-full; do
  MTL_CAPTURE_ENABLED=1 MLXLEARN_FORCE_BACKEND=mlx \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_fit_inference.py "$case" "$out/$case" "$out/probe.dylib" \
    > "$out/$case.json"
done
```

Each case needs a fresh output directory. The raw prediction capture bundles stay in the ignored local results directory.

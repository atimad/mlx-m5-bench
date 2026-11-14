# M5 Pro Metal traces for SVC and PCA

These are separately instrumented replays of the standard benchmark. Input SHA-256 and estimator parameters matched all six corresponding steady records for each case in [the standard run](../20261114T184308448033Z-84f22b8ebf/summary.md). The replays used seed 42, four requested threads, forced MLX GPU configuration, MLX 0.32.4, mlx-learn 0.1.2, and scikit-learn 1.9.1 on the same Apple M5 Pro.

| Workload | Operation | Completed Metal buffers | Sum of GPU buffer intervals (ms) | Replay finding |
|---|---|---:|---:|---|
| SVC, 4,000 × 256, 3 classes | Fit | 4 | 4.726 | GPU work verified, mixed CPU/GPU |
| SVC, 4,000 × 256, 3 classes | Predict | 1 | 0.289 | GPU work verified, mixed CPU/GPU |
| PCA, 12,000 × 256, 8 components | Fit | 3 | 0.706 | GPU work verified, mixed CPU/GPU |
| PCA, 12,000 × 256, 8 components | Transform | 2 | 0.070 | GPU work verified |
| PCA, 2,000 × 32, 3 components | Fit | 3 | 0.166 | GPU work verified, mixed CPU/GPU |
| PCA, 2,000 × 32, 3 components | Transform | 0 | 0 | Consistent with the source-audited CPU path |

All scikit-learn control windows recorded zero GPU command buffers. SVC agreed on all 1,000 predictions with 94.3% accuracy for both implementations. Its maximum decision-output difference was 0.00126. Both PCA cases passed the reconstruction, retained variance and component subspace checks. The minimum principal cosine exceeded 0.99999999 in each case.

Each operation window excludes warmup, model construction and explicit synchronization. Fit uses a fresh model, and inference is its first query. The observer records Metal completion status and positive GPU start/end intervals on the M5 Pro. Interval sums describe completed buffers in the instrumented replay. They are kept separate from the original wall-clock benchmark medians. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

A separate one-frame Apple Metal capture was saved for each positive operation. The metadata records capture-stream checksums and selected mlx-learn shader symbols. The SVC captures include the kernel transform symbol. PCA captures include workload-specific statistics symbols. Capture bundles can retain shader artifacts from earlier operations, so symbol presence alone cannot attribute a dispatch to a specific window. GPU execution claims come from the scoped command completions. Full Xcode was unavailable for per-kernel inspection. [Apple Metal capture documentation](https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-programmatically)

The pinned source identifies host SMO optimization and class voting in SVC, and a host eigensolve in PCA fit. The smaller PCA projection follows the library's host path. Its zero-buffer trace corroborates that routing for this replay. [SVC source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/svm/_classes.py) · [PCA source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_solvers/pca.py)

## Evidence

| Workload | Summary and capture metadata | mlx-learn completion traces | scikit-learn controls |
|---|---|---|---|
| SVC 4,000 × 256 | [Metadata](svc/metadata.json) | [Fit](svc/mlxlearn-fit.tsv), [predict](svc/mlxlearn-predict.tsv) | [Fit](svc/sklearn-fit.tsv), [predict](svc/sklearn-predict.tsv) |
| PCA 12,000 × 256 | [Metadata](pca/metadata.json) | [Fit](pca/mlxlearn-fit.tsv), [transform](pca/mlxlearn-transform.tsv) | [Fit](pca/sklearn-fit.tsv), [transform](pca/sklearn-transform.tsv) |
| PCA 2,000 × 32 | [Metadata](pca-small/metadata.json) | [Fit](pca-small/mlxlearn-fit.tsv), [transform](pca-small/mlxlearn-transform.tsv) | [Fit](pca-small/sklearn-fit.tsv), [transform](pca-small/sklearn-transform.tsv) |

## Reproduce

Run from the repository root with the locked environment and Xcode Command Line Tools.

```sh
out=results/metal-svc-pca
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for case in svc pca pca-small; do
  MTL_CAPTURE_ENABLED=1 MLXLEARN_FORCE_BACKEND=mlx \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_svc_pca.py "$case" "$out/$case" "$out/probe.dylib" \
    > "$out/$case.json"
done
```

Each case requires a fresh output directory. The raw capture bundles stay in the ignored local results directory. The repository contains compact completion traces and capture metadata.

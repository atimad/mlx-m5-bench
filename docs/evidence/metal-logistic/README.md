# M5 Pro Metal traces for logistic regression

These are separate instrumented replays of the standard 2,000 × 32 and full 100,000 × 256 binary logistic regression cases. The input bytes and estimator parameters matched the archived steady records. Both replays used seed 42, four requested CPU threads, mlx-learn 0.1.2, MLX 0.32.4, scikit-learn 1.9.1, and the benchmark's forced-MLX GPU configuration. Sample counts are before the train/test split.

| Workload | Operation | mlx-learn completed Metal buffers | Sum of GPU buffer intervals (ms) | Replay finding |
|---|---|---:|---:|---|
| 2,000 × 32 | Fit | 14 | 2.972 | GPU work verified in a fit with host stages |
| 2,000 × 32 | Predict | 0 | 0 | Consistent with the source-audited CPU path |
| 100,000 × 256 | Fit | 18 | 23.089 | GPU work verified in a fit with host stages |
| 100,000 × 256 | Predict | 0 | 0 | Consistent with the source-audited CPU path |

The scikit-learn fit and prediction controls recorded zero Metal submissions for both cases. All 500 and all 25,000 test labels, respectively, matched scikit-learn. Maximum probability differences were 0.000479 and 0.000804, within the benchmark's tolerance. Probabilities were checked for numerical parity outside the trace windows.

The completion observer isolates fit and the first prediction on a freshly fitted model after warming the runtime. Model construction, warmup and explicit synchronization are outside these windows. Each counted buffer completed on the M5 Pro and had positive Metal GPU start and end timestamps. Buffer interval sums describe the instrumented replays. The original wall-clock medians come from separate uninstrumented runs. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

Separate one-frame fit captures include workload-specific centering and native L-BFGS shader symbols. Capture metadata includes checksums. The operation-scoped command completions establish GPU execution, and captured shader symbols provide context about the fit path. Full Xcode was unavailable for per-kernel timeline analysis. [Apple Metal capture documentation](https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-programmatically)

The pinned source uses host-side validation and bookkeeping during fit and calls inherited scikit-learn methods for prediction. The matching prediction windows corroborate CPU execution even after GPU-accelerated fits. The traces cover these two binary cases under the recorded configuration. [mlx-learn logistic source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/linear_model/_logistic.py)

| Workload | Metadata | mlx-learn completion traces | scikit-learn controls |
|---|---|---|---|
| 2,000 × 32 | [Summary and capture metadata](logistic/metadata.json) | [Fit](logistic/mlxlearn-fit.tsv), [predict](logistic/mlxlearn-predict.tsv) | [Fit](logistic/sklearn-fit.tsv), [predict](logistic/sklearn-predict.tsv) |
| 100,000 × 256 | [Summary and capture metadata](logistic-full/metadata.json) | [Fit](logistic-full/mlxlearn-fit.tsv), [predict](logistic-full/mlxlearn-predict.tsv) | [Fit](logistic-full/sklearn-fit.tsv), [predict](logistic-full/sklearn-predict.tsv) |

## Reproduce

Run from the repository root with the locked Apple Silicon environment and Xcode Command Line Tools.

```sh
out=results/metal-logistic-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for case in logistic logistic-full; do
  MTL_CAPTURE_ENABLED=1 MLXLEARN_FORCE_BACKEND=mlx \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_fit_inference.py "$case" "$out/$case" "$out/probe.dylib" \
    > "$out/$case.json"
done
```

Each case needs a fresh output directory. Raw capture bundles stay in the ignored local results directory. The repository contains the compact completion traces and capture metadata.

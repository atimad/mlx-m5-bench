# Automatic backend selection on the M5 Pro

These replays cover all seven distinct workloads from the forced-MLX trace panel. Automatic mode requests `device="auto"` and requires `MLXLEARN_FORCE_BACKEND` to be absent. Forced mode requests `device="gpu"` with `MLXLEARN_FORCE_BACKEND=mlx`. Both use direct mlx-learn imports, strict fallback policy, and the same input byte fingerprints, estimator parameters, seed 42, four requested CPU threads, M5 Pro, and locked MLX 0.32.4, mlx-learn 0.1.2 and scikit-learn 1.9.1 dependencies.

Counts are completed Metal command buffers from separate fit and first-inference windows on a fresh model after warmup. Fit and inference are separated by synchronization outside the observation windows. CPU controls recorded zero Metal buffers on every workload. All seven automatic replays passed numerical checks against their scikit-learn controls.

| Workload | Inference | Forced fit / inference | Auto fit / inference | Auto routing |
|---|---|---:|---:|---|
| [KNN 8,000 × 128, k=5](knn/metadata.json) | Predict | 0 / 1 | 0 / 1 | Fit stages arrays; GPU query |
| [KNN 30,000 × 64, k=5](knn-full/metadata.json) | Predict | 0 / 7 | 0 / 7 | Fit stages arrays; GPU query |
| [Logistic 2,000 × 32](logistic/metadata.json) | Predict | 14 / 0 | 0 / 0 | CPU fit below crossover; CPU prediction |
| [Logistic 100,000 × 256](logistic-full/metadata.json) | Predict | 18 / 0 | 0 / 0 | CPU fit below crossover; CPU prediction |
| [SVC 4,000 × 256, 3 classes](svc/metadata.json) | Predict | 4 / 1 | 0 / 0 | CPU fit below crossover; CPU prediction |
| [PCA 12,000 × 256, 8 components](pca/metadata.json) | Transform | 3 / 2 | 0 / 0 | CPU fit below crossover; CPU transform |
| [PCA 2,000 × 32, 3 components](pca-small/metadata.json) | Transform | 3 / 0 | 0 / 0 | CPU fit below crossover; CPU transform |

Dimensions are dataset sizes before the 75/25 split. Crossover decisions use the training dimensions. For example, logistic regression's 100,000 × 256 workload trains on 75,000 × 256, or 19.2 million elements, below its 20 million-element gate for this sample range. SVC's 3,000 × 256 training set falls below its one-million element-ops gate. Both PCA training sets fall below the covariance solver's size and feature thresholds.

The automatic events include initial `mlx/selected` entries followed by `cpu/below-crossover` for logistic and SVC fits. The final CPU event and empty fit traces agree. KNN fit also reports `mlx/selected` but emits zero Metal commands because it owns and stages its arrays during fit. Its subsequent `auto-query` reports MLX and has positive GPU completion intervals and a matching prediction capture. These observations apply to this panel; automatic routing depends on workload and library release.

Each case directory contains the command-completion TSVs, unmodified routing events, numerical metrics, and a relative reference to the forced evidence. Positive auto query captures also have capture checksums and selected shader symbols. Full captures stay in the ignored results directory. Metal buffer counts and intervals describe instrumented replays. The original benchmark wall-clock medians remain forced-run measurements. The separate [uninstrumented timing panel](../routing-timing/README.md) compares automatic and forced mode against paired scikit-learn controls. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

## Reproduce

```sh
out=results/metal-auto-replay
mkdir -p "$out"
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$out/probe.dylib"
for case in knn knn-full logistic logistic-full svc pca pca-small; do
  env -u MLXLEARN_FORCE_BACKEND MTL_CAPTURE_ENABLED=1 \
    VECLIB_MAXIMUM_THREADS=4 OMP_NUM_THREADS=4 \
    .venv/bin/python scripts/trace_fit_inference.py "$case" "$out/$case" \
    "$out/probe.dylib" --mode auto > "$out/$case.json"
done
```

Use the locked Apple Silicon environment and a fresh output directory for each case.

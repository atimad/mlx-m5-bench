# XGBoost versus xgboost-metal on M5 Pro

On two dense synthetic tabular workloads, xgboost-metal trained about twice as fast as the four-thread CPU XGBoost baseline and predicted a full 25,000-row batch about 3.4–3.5 times as fast. Separate Metal traces verified GPU work in training and warmed prediction for both tasks. The CPU controls submitted no Metal work. These measurements describe the pinned engines on one M5 Pro.

## Uninstrumented timing

Each cell shows median milliseconds as CPU / Metal. The CPU/Metal training ratios were 1.96× for classification and 2.05× for regression. The warmed prediction ratios were 3.53× and 3.41×, respectively.

| Workload | Training data ingestion | Training | First prediction | Warmed prediction | Ingestion + training + first prediction |
|---|---:|---:|---:|---:|---:|
| Binary classification | 4.501 / 0.774 | 243.080 / 123.973 | 3.557 / 1.293 | 3.385 / 0.959 | 251.245 / 126.005 |
| Regression | 4.580 / 0.770 | 243.637 / 118.767 | 3.455 / 1.247 | 3.290 / 0.966 | 251.689 / 120.891 |

Across the four CPU blocks, process peak RSS ranged from 150.5 to 169.9 MiB. Across the Metal blocks it ranged from 77.1 to 77.5 MiB. These are process high-water marks. They do not measure total Metal allocation. [Timing manifest](timing/manifest.json) · [Raw measurements](timing/measurements.json) · [Medians, MAD, and ranges](timing/summary.json)

## Workload and quality checks

Each task uses 100,000 float32 rows with 32 features and a seed-42 75/25 split. The classification case uses scikit-learn's synthetic classification generator with 16 informative and four redundant features and a stratified split. Regression uses the Friedman #1 generator with five informative features and Gaussian noise with standard deviation 1. The coordinator saves each split once for both worker environments and confirms each worker's input fingerprint.

Both adapters use native `DMatrix`, `train`, and `Booster.inplace_predict`, with 100 rounds of depth-six histogram trees, 256 bins, a learning rate of 0.1, and the same objective and seed per task. The CPU worker requested four threads and reported a four-thread OpenMP pool. The Metal worker reports a build without OpenMP. XGBoost 3.4.1 and xgboost-metal 0.1.1 are different implementations and use different upstream API baselines. [CPU XGBoost release](https://github.com/dmlc/xgboost/releases/tag/v3.4.1) · [Metal release and API baseline](https://github.com/tabulai/xgboost-metal/releases/tag/v0.1.1)

Each task runs CPU then Metal in the first pass and Metal then CPU in the second. Each subprocess warms the runtime with a train-and-predict cycle before timing three fresh training matrices and boosters. Each engine contributes six steady fits and 20 warmed predictions per task. First prediction is measured once per fit. Warmed predictions run on the final booster in each block, with one extra warmup. `inplace_predict` takes the NumPy test array and returns materialized predictions. It avoids repeated lookup of a cached prediction result. Timed ingestion is training matrix construction. The last table column sums ingestion, training, and first-prediction timings per repetition before taking the median. [XGBoost Python prediction API](https://xgboost.readthedocs.io/en/stable/python/python_api.html#xgboost.Booster.inplace_predict)

All 12 paired fits passed the declared quality gates. Both engines achieved log loss 0.123441 and ROC AUC 0.990512 on classification, and RMSE 1.068294 on regression, at the reported precision. The gates allow an absolute difference of 0.02 in log loss and 0.01 in ROC AUC, and a 5% relative difference in RMSE. They compare held-out quality without requiring identical trees. [Per-fit quality checks](timing/correctness.json)

## Metal trace evidence

A separate replay used the same data and parameters and scoped the observer around one training operation and one warmed prediction in each worker. Every counted Metal command buffer completed with positive GPU timestamps on the Apple M5 Pro. The training windows include gradient and quantization kernels and the tree-building driver. They also include internal work that `train` initiates after the training matrix is constructed.

| Task | Metal training buffers / direct dispatches | Metal prediction buffers / direct dispatches | CPU training and prediction |
|---|---:|---:|---:|
| Classification | 206 / 1,520 | 2 / 3 | 0 buffers, 0 dispatches |
| Regression | 206 / 1,720 | 2 / 2 | 0 buffers, 0 dispatches |

Both warmed predictions dispatched `predict_tree_cached`, which traverses trees using cached tree nodes, plus input staging. Classification also dispatched the probability transform. The counts cover observed direct compute dispatches and command-buffer completions. They establish GPU work inside the scoped operations. Both traced model pairs passed the quality gates. [Metal tree traversal source](https://github.com/tabulai/xgboost-metal/blob/v0.1.1/kernels/boost.metal#L1767-L1808) · [Trace manifest](trace/manifest.json) · [Trace quality checks](trace/correctness.json)

- Classification · [training dispatches](trace/classification/pass-1-metal/train-dispatch.tsv) · [prediction dispatches](trace/classification/pass-1-metal/predict-dispatch.tsv) · [CPU controls](trace/classification/pass-1-cpu/)
- Regression · [training dispatches](trace/regression/pass-1-metal/train-dispatch.tsv) · [prediction dispatches](trace/regression/pass-1-metal/predict-dispatch.tsv) · [CPU controls](trace/regression/pass-1-cpu/)

## Reproduce

Run from the checkout on Apple Silicon with Python 3.13, uv, and Xcode Command Line Tools for trace compilation. CPU XGBoost's macOS wheel needs `libomp`. The measured host used Homebrew libomp 23.1.5. Both engine distributions provide the `xgboost` import, so use two separate environments. [XGBoost installation guide](https://xgboost.readthedocs.io/en/stable/install.html) · [xgboost-metal release](https://github.com/tabulai/xgboost-metal/releases/tag/v0.1.1)

```sh
brew install libomp
uv sync --locked
envs=results/xgboost-envs
mkdir -p "$envs"
uv venv --python 3.13 "$envs/cpu"
uv venv --python 3.13 "$envs/metal"

wheel=xgboost_metal-0.1.1-py3-none-macosx_14_0_arm64.whl
curl -fsSL "https://github.com/tabulai/xgboost-metal/releases/download/v0.1.1/$wheel" \
  -o "$envs/$wheel"
(
  cd "$envs"
  printf '%s  %s\n' f2130593fe79f49c928078492999f55bd3c37154c2aa5d275f410e4362ee2f33 "$wheel" |
    shasum -a 256 -c -
)
uv pip install --python "$envs/cpu/bin/python" \
  xgboost==3.4.1 numpy==2.5.4 scipy==1.18.1 threadpoolctl==3.6.0
uv pip install --python "$envs/metal/bin/python" \
  "$envs/$wheel" numpy==2.5.4 scipy==1.18.1 threadpoolctl==3.6.0

uv run --locked python -m mlx_m5_bench.xgboost_bench \
  --cpu-python "$envs/cpu/bin/python" --metal-python "$envs/metal/bin/python" \
  --output results/xgboost-timing-replay

xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o "$envs/probe.dylib"
uv run --locked python -m mlx_m5_bench.xgboost_bench \
  --cpu-python "$envs/cpu/bin/python" --metal-python "$envs/metal/bin/python" \
  --output results/xgboost-trace-replay --probe "$envs/probe.dylib"
```

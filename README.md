# mlx-m5-bench

Reproducible CPU vs Apple Silicon GPU benchmarks for classical machine learning, starting with scikit-learn and mlx-learn.

A local-first benchmark lab measuring fit and inference latency, numerical agreement, process memory and backend dispatch. It includes deterministic synthetic datasets, isolated serial workers, raw measurements, reproducibility manifests, charts and a read-only Streamlit dashboard.

## Install

Use a native arm64 terminal on an Apple Silicon Mac. The project targets Python 3.13 and pins mlx-learn 0.1.2, MLX 0.32.4 and scikit-learn 1.9.1. A prebuilt MLX Metal wheel is required. Full Xcode is optional for this workload.

Install uv using its documented installation method, then run the following commands in the repository. uv creates an isolated .venv and downloads Python 3.13 if needed. [uv installation](https://docs.astral.sh/uv/getting-started/installation/)

```sh
uv sync --locked --extra dashboard
uv run mlx-m5-bench doctor
uv run mlx-m5-bench run --profile quick
uv run mlx-m5-bench report --latest
uv run mlx-m5-bench dashboard
```

The dashboard binds to 127.0.0.1. Its default port is 8501. It loads stored measurements and supports algorithm, sample count, backend, measurement phase and profile filters.

CPU-only installation and checks also run on Linux. MLX dependencies use platform markers. GPU diagnostics return a nonzero exit status when Metal is unavailable.

```sh
uv run mlx-m5-bench run --profile quick --cpu-only
uv run mlx-m5-bench run --profile standard
uv run mlx-m5-bench run --profile full
```

## Algorithms

| Family | Shared configuration | Additional checks |
|---|---|---|
| Logistic regression | L-BFGS, L2, C=1, tol=1e-5, max_iter=300, no class weights | Accuracy, predictions, probabilities, convergence and iteration counts |
| KNN classification | Exact brute-force Euclidean search, uniform voting, k=5/15/25 by case | Accuracy, predictions, probabilities, separate fit/query cost |
| SVC | RBF, gamma=1/features, C=1, tol=1e-3, 64 MiB cache, shrinking disabled | Accuracy, one-vs-one decisions, support counts, convergence |
| PCA | covariance_eigh, no whitening, 3/8/12 components by case | Reconstruction RMSE, retained variance, principal-angle agreement |

Both implementations receive identical contiguous float32 arrays and labels. Internal precision, optimization algorithms and CPU/GPU division differ. These differences are recorded in the methodology and upstream review.

## Evidence and interpretation

Every timed operation has a backend classification. Available categories include CPU baseline, CPU fallback/owned host path, reported GPU, reported mixed CPU/GPU, independently verified GPU, unknown and unsupported.

Current estimator results carry library diagnostics and source-audited exceptions. Separate Metal traces verify GPU work in matched standard KNN prediction, SVC fit and prediction, and PCA fit and transform replays. The smaller PCA transform took the host path. [KNN trace](docs/evidence/metal-knn-8000x128-c3-k5/README.md) · [SVC and PCA traces](docs/evidence/metal-svc-pca/README.md) A successful Metal matrix-multiplication probe establishes capability. Each estimator retains its own evidence status.

Speed ratios appear only for passing numerical comparisons with reported GPU or mixed paths. CPU paths and unknown execution retain their measured timings and an ineligible ratio. Charts label the evidence level and retain failed or missing cases. The dashboard displays raw failure details.

See the [measured local results](docs/results.md), [methodology](docs/methodology.md), [limitations](docs/limitations.md) and [upstream API review](docs/upstream.md).

## Profiles and outputs

Quick runs four small workloads with one steady repetition and a separately recorded first call. Standard runs 13 workloads with three steady repetitions and one warmup. Full expands sizes and repeats while enforcing memory and quadratic-work admission checks. Every skipped workload retains its requested dimensions and reason.

Packaged profiles live in src/mlx_m5_bench/configs. To customize one, copy its YAML and pass a path.

```sh
uv run mlx-m5-bench run --profile standard --config my-profile.yaml
uv run mlx-m5-bench run --profile quick --output results/custom
uv run mlx-m5-bench report --run results/RUN_ID
uv run mlx-m5-bench dashboard --root results/custom --port 8502
```

Each UTC timestamped run directory contains manifest.json, measurements.json and CSV, summary.json and CSV, summary.md, seven PNG charts, and per-worker JSONL logs and requests. Raw and aggregated records are separate. Generated outputs and environments are Git-ignored. A timestamp plus configuration hash identifies each execution. Dataset fingerprints identify the exact inputs.

## Development

```sh
uv sync --locked --extra dashboard
uv run pytest
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
uv run pytest -m apple_gpu
uv build
```

The default pytest selection excludes Apple GPU tests. Run GPU tests sequentially on the Mac. CI runs Linux CPU checks. See [reproducibility](docs/reproducibility.md) and [contribution guidelines](CONTRIBUTING.md).

## License and attribution

Original benchmark code is MIT licensed. This project calls upstream APIs and includes original tests and documentation. Dependency source and binaries retain their upstream licenses. mlx-learn is Apache-2.0, MLX is MIT and scikit-learn is BSD-3-Clause. This project is independently maintained. Official affiliation with Apple, scikit-learn, MLX or Tabul AI is absent. [mlx-learn license](https://github.com/tabulai/mlx-learn/blob/v0.1.2/LICENSE), [MLX license](https://github.com/ml-explore/mlx/blob/v0.32.4/LICENSE), [scikit-learn license](https://github.com/scikit-learn/scikit-learn/blob/1.9.1/COPYING)

Remote publication requires the owner's explicit approval. See the [publication checkpoint](docs/publication.md).

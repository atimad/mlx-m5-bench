# Reproducibility

Use native Apple Silicon Python 3.13 with the committed uv.lock. The lock contains package hashes and platform markers. uv sync --locked --extra dashboard installs the dashboard and development tooling in the project-local environment. uv sync --locked --no-dev installs the execution environment.

Run doctor and archive its JSON locally before benchmarking.

```sh
uv run mlx-m5-bench doctor > results/doctor.json
uv run mlx-m5-bench run --profile quick
uv run mlx-m5-bench run --profile standard
uv run mlx-m5-bench report --latest
uv run mlx-m5-bench dashboard
```

Each manifest includes OS/build, chip, core counts, memory, Python, dependencies, NumPy BLAS build, loaded thread pools, requested thread environment, seed, full configuration, timestamp, Git commit/dirty state, power, thermal output and load. Workers also capture thread limits after estimator imports. Host-derived fields can be unavailable and then retain null values.

Record the exact run directory and original manifest when sharing measurements. Input fingerprints establish data equivalence within the locked environment. RNG implementations and library behavior can change between dependency versions. Timing changes across runs are expected.

Raw worker JSONL and logs survive failures. measurements.json consolidates them and adds paired correctness results. summary.json/CSV are derived by report. report reads existing records and regenerates only derived outputs. The dashboard loads those stored files.

## Thread sensitivity

Make copies of standard.yaml and change threads to 1, 4 and the host's verified physical CPU count. Use --config for each run. CPU-only sweeps are allowed through --cpu-only and retain INCONCLUSIVE cross-library correctness because a paired candidate is absent. Compare CPU timings using the same profile and dataset fingerprints. The default four-thread setting is a declared baseline choice.

## Clean installation

Build a wheel and install it in a separate temporary virtual environment. Install the wheel's dashboard extra if testing Streamlit. Check the CLI, doctor and a quick run from a directory outside the checkout to verify packaged profiles.

```sh
uv build
uv venv /tmp/mlx-bench-clean --python 3.13
uv pip install --python /tmp/mlx-bench-clean/bin/python 'dist/mlx_m5_bench-0.1.0-py3-none-any.whl[dashboard]'
/tmp/mlx-bench-clean/bin/mlx-m5-bench --help
/tmp/mlx-bench-clean/bin/mlx-m5-bench doctor
```

GPU tests are deliberately separate from generic CI.

```sh
uv run pytest
uv run pytest -m apple_gpu
uv run ruff check src tests scripts
uv run ruff format --check src tests scripts
uv run mypy src
```

Local files can contain absolute library paths in runtime diagnostics and build metadata. Generated results are excluded from Git. The export script produces a redacted evidence bundle for deliberate inclusion in documentation. Review its output before committing.

```sh
uv run python scripts/export_results.py results/RUN_ID docs/evidence/RUN_ID
```

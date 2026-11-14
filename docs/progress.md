# Execution record

## Phase 1 — discovery and design

2026-11-14. The empty target directory was initialized as a local Git repository on main. The verified machine reports macOS 27.2.1 build 26B131, Apple M5 Pro, 5 performance and 10 efficiency CPU cores, 16 GPU cores, 24 GiB physical memory and Metal 4.

Homebrew 6.0.6, Git 2.54.0, gh 2.94.0 and Xcode Command Line Tools are available. Full Xcode is absent. The Homebrew default Python is 3.14.5 and system Python is 3.9.6. Python 3.13.18 was installed through uv for the isolated project environment. Homebrew inventory reported an unrelated untrusted cask tap while listing packages. Its trust settings were left as found.

GitHub CLI read-only authentication checks identified account atimad. The intended repository could not be resolved by a read-only lookup. Remote publication awaits explicit approval.

No mlx-m5-bench.zip was found in Downloads, Desktop, Documents, repos or CloudStorage. Implementation proceeded from the supplied requirements. Source review selected current stable mlx-learn 0.1.2. Source identities, public APIs, unsupported parameters and precision/dispatch differences are recorded in upstream.md.

The implementation plan used explicit estimator imports, validated packaged profiles, deterministic synthetic datasets, serial subprocess workers, synchronized timings, operation-level diagnostics, independent correctness analysis and persisted reports. Risks identified included silent host routing, mixed execution, float32 differences, asynchronous MLX work, kernel working memory and package import collisions in future XGBoost work.

## Phase 2 — implementation

Implemented all four families, CLI commands, metadata and functional Metal probe, memory/work admission, process deadlines, raw JSONL and consolidated JSON/CSV, robust summaries, seven PNG charts and a saved-results Streamlit dashboard. Added schemas, original MIT-licensed source, tests, CPU-only CI and reproducibility documentation.

Primary runs use explicit GPU configuration and the documented MLX diagnostic forcing environment override. Source review showed this override still permits internal host PCA solves. CPU fallback and unknown work retain timings and receive no GPU ratio.

## Phase 3 — verification

The initial quick pass passed numerical checks for all four families. KNN emits kneighbors diagnostics during predict, which required an operation-name mapping. Small PCA emitted a final host-solve event after an initial forced MLX event. Regression tests now cover final dispatch precedence and both behaviors.

A failure-path test exposed chart generation on an entirely empty timing series. Reporting now retains the failure and labels an empty plot. Truncated worker JSONL is preserved as an explicit error. Failed correctness takes precedence over a concurrent nonconvergence finding.

Unit/CPU/report/CLI/dashboard validation and separately marked local GPU integration tests pass. Ruff, formatting and mypy pass. The final validation counts and clean-wheel installation outcome are recorded in publication.md. The local Streamlit page was opened and observed rendering stored standard results with backend and phase filters.

## Phase 4 — expanded experiments

Quick, standard and memory-admitted full profiles executed locally. An early expanded run overlapped a few quality checks. Its outputs remain local exploratory artifacts. Canonical reruns executed sequentially after implementation verification and reference clean implementation commit 2da3300. Follow-up reporting changes retained the timing and correctness evidence.

The standard multiclass logistic case produced a repeatable line-search warning at tolerance 1e-5. Close predictions alone did not satisfy convergence. The case remains INCONCLUSIVE and ratio-ineligible. Its tolerance was retained.

Full includes two large memory-admission skips and one quadratic SVC skip. Requested sizes and reasons remain in outputs. Final canonical run identifiers and numerical findings are recorded in results.md.

## Phase 5 — publication readiness

Source and dependency review, installation commands, methodology, reproducibility guide, limitations, contributing guidance, issue template and least-privilege Linux workflow are present. Generated environments, datasets and large local results are excluded from Git.

Compact recursively redacted evidence is exported intentionally under docs/evidence. Actual raw timing and correctness values are preserved. Metadata paths are redacted. Canonical manifests identify the implementation commit and retain the dirty state of the measured checkout.

## Phase 6 — approval checkpoint

Prepared for public GitHub repository atimad/mlx-m5-bench under MIT for original source. Exact remote actions, file scope and validation results appear in publication.md. Human approval remains the gate for repository creation and push.

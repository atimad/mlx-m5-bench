# Upstream review

Reviewed on 2026-11-14 against release metadata, installed signatures and source. Local upstream review checkout was outside the repository. Benchmark implementation uses original code and public APIs, plus the explicitly documented private PCA dispatch predicate.

## Releases and provenance

| Project | Assessed version | Source identity |
|---|---|---|
| mlx-learn | 0.1.2, current stable PyPI release at review | v0.1.2 peeled commit fb884caad34f159dfb537e497137dd76a40153c1 |
| MLX | 0.32.4, pinned compatible stable | v0.32.4 ref 36969c094354086e15d2a327a9c50feb20b9cf11 |
| scikit-learn | 1.9.1, pinned | 1.9.1 peeled commit 866c0f51e7560ef0303cbcc5f159df5382ea9e3f |
| xgboost-metal | PyPI 0.1.0, GitHub v0.1.1 | v0.1.1 ref 718316676a75cdbdb262e1166f675d556967e6d6, reviewed HEAD 3a84667dc57c3517588b6e7794c003f98bbc47e3 |

mlx-learn requires Python >=3.10, scikit-learn >=1.7,<1.10 and MLX >=0.29,<1.0. Its support matrix includes Python 3.13 with scikit-learn 1.9. Python 3.13.18 was selected through uv because the Homebrew default was 3.14.5. mlx-learn 0.1.2 was retained because no newer stable release was found. It adds PCA to the requested initial estimator families. [PyPI metadata](https://pypi.org/pypi/mlx-learn/json), [release support matrix](https://github.com/tabulai/mlx-learn/blob/v0.1.2/docs/support_matrix.md)

MLX 0.32.4 provides Apple Metal wheels and mlx.core.synchronize, explicit streams and allocator counters. Installed wheel metadata and a functional GPU matrix multiplication were checked locally. The manifest records the actual Metal device and working-set limits. [MLX source](https://github.com/ml-explore/mlx/tree/v0.32.4), [synchronization API](https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.synchronize.html)

scikit-learn 1.9.1 requires Python >=3.11. Its logistic penalty defaults and SVC probability defaults contain deprecation sentinels handled by mlx-learn 0.1.2. Public parameters used by this repository were verified against installed signatures and exercised in tests. [scikit-learn release source](https://github.com/scikit-learn/scikit-learn/tree/1.9.1), [mlx-learn compatibility handling](https://github.com/tabulai/mlx-learn/blob/v0.1.2/docs/support_matrix.md)

## Direct API and constraints

Explicit imports use mlxlearn.linear_model.LogisticRegression, mlxlearn.neighbors.KNeighborsClassifier, mlxlearn.svm.SVC and mlxlearn.decomposition.PCA. config_context requests device="gpu", fallback_policy="raise", diagnostics=True, deterministic=True and a fixed random_state. NumPy input and output is the supported boundary. patch_sklearn is unused.

The public registry also contains NearestNeighbors and KNeighborsRegressor. Logistic regression supports L-BFGS with L2 or no penalty, dense inputs and class/sample weights. L1/elastic net, sparse input, dual and warm-start paths are unsupported. KNN supports exact Euclidean distance, uniform/distance voting and dense single-output classification. SVC supports linear, RBF, polynomial and sigmoid kernels with explicit cache control. Probability calibration, precomputed/callable kernels and sparse inputs are unsupported. PCA supports dense covariance and randomized paths with host fallbacks and float32 range constraints. [Upstream estimator support](https://github.com/tabulai/mlx-learn/blob/v0.1.2/docs/support_matrix.md)

BackendEvent includes estimator, operation, backend, reason, detail, shape, fallback and extra fields. execution_backend_ is estimator-level state. It can conceal host inference and internal dispatch. Final operation events take priority, and source-audited exceptions refine them. KNN reports query work as kneighbors. [Diagnostic source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_common/diagnostics.py), [dispatch source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_common/base.py)

Logistic predict and predict_proba delegate to inherited NumPy/scikit-learn methods. PCA covariance_eigh uses mx.linalg.eigh with stream=mx.cpu for GPU Gram solves, while smaller inputs can finish fully on the host. PCA projection uses a separate size/precision predicate. SVC kernel operations and native host optimization form a mixed path. [Logistic source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/linear_model/_logistic.py), [PCA solver source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/_solvers/pca.py), [SVC source](https://github.com/tabulai/mlx-learn/blob/v0.1.2/src/mlxlearn/svm/_classes.py)

## XGBoost comparison planned for v0.2.0

xgboost-metal's reviewed README recommends GitHub release wheels and deprecates its PyPI installation path. Its requirements include Apple Silicon, macOS >=14 and Python >=3.10. Source builds require full Xcode with Metal and CMake >=3.24. It exports the xgboost import name, so a future comparison must use separate CPU and Metal environments to avoid package collision. CPU and CUDA execution are unsupported in the Metal package. The explicit target is device="metal", tree_method="hist". [Reviewed README](https://github.com/tabulai/xgboost-metal/blob/3a84667dc57c3517588b6e7794c003f98bbc47e3/README.md)

The first XGBoost comparison uses native histogram training and in-place prediction in independent worker environments. Both engines receive identical datasets from the coordinator. The CPU worker records XGBoost 3.4.1 and its OpenMP pool. The Metal worker records xgboost-metal 0.1.1 and the separate API baseline it reports. [Benchmark and environment setup](evidence/xgboost-baseline/README.md) · [Release plan](roadmap.md#v020--xgboost-versus-xgboost-metal)

## License review

Original source was authored for this repository. Upstream source was inspected to determine behavior and API compatibility. Dependency code and native libraries are installed by the resolver. Their licenses and notices remain with those distributions. The MIT license covers this benchmark's original code. [mlx-learn notices](https://github.com/tabulai/mlx-learn/blob/v0.1.2/THIRD_PARTY_NOTICES.md)

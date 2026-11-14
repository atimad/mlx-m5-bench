# Limitations and unresolved verification

- Independent Metal tracing verified one matched KNN prediction replay. Original timing records retain their contemporaneous backend classifications. Other estimator paths retain their existing evidence levels. [KNN trace evidence](evidence/metal-knn-8000x128-c3-k5/README.md)
- CPU-first process ordering, background load, power policy and thermal drift can influence results. Full energy and frequency instrumentation is absent.
- Cold means the first estimator call after imports and input preparation. Native library loading can be partly warmed by module discovery.
- Shared float32 input does not ensure identical internal precision. Logistic and SVC optimizer implementations differ. PCA can use a CPU eigensolver after GPU Gram computation.
- The force_mlx environment override is experimental upstream configuration. It can bypass crossover heuristics and produce slower timings. Host-side stages and final host solves still occur.
- The private PCA dispatch predicate is pinned to mlx-learn 0.1.2. Updating that dependency requires a fresh source review and regression verification.
- RSS and MLX allocator counters overlap unified memory. They omit some allocations and cannot establish total device memory consumption. Process high-water RSS includes earlier phases.
- Working-set estimates and quadratic-work limits are heuristics. Process deadlines contain slow jobs. The admission calculation cannot guarantee an allocation will succeed.
- Three or five repetitions and synthetic datasets provide an initial local measurement panel. They provide limited statistical power and limited external validity.
- The dashboard displays one selected saved run. Its profile filter applies to that selected run. Missing comparison ratios stay empty and raw records retain failure information.
- CPU-only runs retain INCONCLUSIVE paired correctness. Unit tests separately check CPU adapter behavior.
- GitHub Actions is prepared locally. Remote CI execution awaits publication approval.
- Publication approval is required before creating or pushing the GitHub repository.

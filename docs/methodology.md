# Measurement methodology

## Experimental unit

One workload specifies algorithm, total samples, features, class count, KNN neighbors and PCA components. Every implementation uses the same seed and exact train/test array bytes. Split size is 75/25. Classification uses stratification and train-only StandardScaler. PCA uses correlated anisotropic Gaussian features and mean centering inside each estimator. Float32 conversion occurs after preprocessing. The SHA-256 fingerprint covers arrays and labels in a fixed order.

Each implementation executes in a fresh subprocess. Workloads run serially with CPU first, then the MLX candidate. This ordering can favor the second process through system caches and thermal drift. Each process regenerates deterministic inputs. Input generation, splitting and scaling are timed as preparation and excluded from model operations.

## Timing boundaries

The first model fit and prediction/transform are recorded as cold. Imports, estimator module discovery and dataset preparation precede this call. Cold therefore describes first estimator execution. OS filesystem caches and already initialized runtime components can persist.

The worker then fits and queries fresh model instances for the requested warmups and steady repetitions. Standard uses one warmup and three steady repeats. Full uses one warmup and five steady repeats. Quick uses zero additional warmups and one steady repeat, after the recorded first call.

perf_counter measures wall time. MLX candidate calls synchronize the default GPU and CPU streams before starting and after returning. Current pinned upstream paths evaluate results and use their device's default streams. Both synchronizations remain inside the completion boundary, including CPU paths. Creating NumPy outputs materializes lazy MLX work. CPU timings use synchronous public methods.

Fit includes estimator validation, internal dtype conversion and array staging. Inference includes validation, lazy query-index work, compute and NumPy output materialization. Internal transfer timing is unavailable through these APIs. Separate transfer duration is unmeasured. NumPy-to-MLX staging uses shared Apple unified memory and can still incur copies or scheduling costs.

Pipeline timing includes model construction, fit, inference, synchronization, diagnostic collection and per-operation bookkeeping. Memory snapshots and correctness evaluation follow this interval. Worker wall time includes imports, preparation, all repetitions, correctness extraction and process exit. Whole-run wall time is recorded in the manifest. Preparation time appears on each repetition as a shared worker-level value and must be counted once when reconstructing totals.

Correctness extraction, probabilities, SVC decision values and PCA reconstruction are outside measured inference. Subsequent calls may benefit from library allocator and compiled-kernel caches. Models are released between repetitions. Process allocator caches remain warm.

Median, minimum, maximum and median absolute deviation are reported separately for cold, warmup and steady phases. Warmup values remain in machine-readable records and are omitted from the Markdown summary. A single quick repeat has zero MAD and carries little statistical information.

## CPU baseline

The default requests four threads for both implementations. Thread environment variables are set before importing numerical runtimes in each worker. threadpoolctl limits discovered OpenMP/BLAS runtimes. KNN also receives n_jobs. Each first-call record captures effective discovered runtime pools.

NumPy and SciPy wheels on the verified Mac use Accelerate. Accelerate's scheduling is not fully observable or enforceable through threadpoolctl. VECLIB_MAXIMUM_THREADS is captured as a requested ceiling. Thread count never implies a verified exact CPU core utilization. System load and thermal pressure remain potential confounders.

## Solver and precision alignment

Logistic regression uses the same L2 objective, intercept policy, C, tolerance and iteration ceiling. The implementations use different L-BFGS execution paths and accumulation precision. mlx-learn performs GPU numerical work with host optimization/control in some paths. Its prediction and probabilities use inherited host-side scikit-learn operations even when the fitted estimator advertises MLX. Fit is classified mixed, while prediction is classified CPU.

KNN uses exact Euclidean brute force and uniform voting. Fit measures index/target construction and staging. GPU computation during index construction is unknown. Query includes exact search and voting. The diagnostics name for direct KNN prediction is kneighbors. Ties and nearly equal distances can diverge through float32 accumulation.

SVC uses the same RBF objective, explicit gamma, tolerance, cache and non-shrinking policy. scikit-learn uses LIBSVM and internal double-precision input. mlx-learn uses float32 kernel work and a host SMO optimizer with different scheduling. Support identities can differ within tolerance. Only support counts and decision values are compared. Probability calibration is unsupported by the direct MLX path. The MLX cache-size boundary can alter accumulation order.

PCA covariance_eigh includes a Gram matrix and host eigensolve in the MLX path. Small inputs can use a complete host solve even with forced MLX. Transform has a separate size/precision gate. An audited pinned private predicate supplies the transform classification. PCA fit is mixed only when final dispatch remains MLX.

The default force_mlx=true sets MLXLEARN_FORCE_BACKEND=mlx in each candidate worker. This is an upstream diagnostic environment override that bypasses crossover heuristics. It does not guarantee that every internal stage uses the GPU. Set force_mlx=false in a custom profile to evaluate public device selection including normal host routing. Direct imports, strict fallback configuration and operation diagnostics are always used. Inherited MLXLEARN tuning overrides are cleared in workers and their parent values remain in the manifest.

## Correctness gates

Each cold and steady candidate output is compared with its corresponding CPU repetition. Both rows receive the comparison result. A missing pair is INCONCLUSIVE. Unsupported capability is UNSUPPORTED. Any non-finite or incompatible output is FAIL.

Classification requires at least 99% label agreement and an absolute test-accuracy difference at most 0.01. Class order must match. Probabilities must lie in [0,1], normalize to one within 1e-5, differ by at most 0.005 mean absolute error and 0.05 maximum error. SVC one-vs-one decisions must differ by at most 0.05. Absolute accuracy values are reported. The synthetic tasks have no separate deployment-quality accuracy threshold.

PCA uses float64 QR-orthonormalized component subspaces and singular values of their cross-product. The minimum principal cosine must be at least 0.99. Reconstruction RMSE must agree within 1% of CPU RMSE or 1e-6, whichever is larger. Retained variance sums must agree within 0.005. This comparison handles signs and rotations within the retained subspace. Degeneracy crossing the selected rank boundary can still require further investigation.

A convergence warning or nonzero SVC fit_status_ makes the pair INCONCLUSIVE. Iteration counts are recorded where exposed. Candidate steady-repeat outputs must agree within atol=1e-6 and rtol=1e-5. A repeatability failure is FAIL.

## Backend evidence and ratios

The evidence classes are CPU_BASELINE, CPU_FALLBACK, GPU_REPORTED_UNVERIFIED, MIXED_CPU_GPU_REPORTED, GPU_VERIFIED, UNKNOWN and UNSUPPORTED. CPU_FALLBACK includes owned CPU paths and source-audited host inference. Diagnostics retain the distinction between owned CPU and actual delegation to scikit-learn.

GPU_VERIFIED is reserved for independent operation-level evidence. The current runner never assigns it. MLX dispatch logs, source review and allocator activity establish reported routing. Separate scoped Metal replays verify GPU work in selected KNN, SVC and PCA operations and are linked from the results. Timed rows preserve the evidence captured during measurement. A functional Metal probe has its own capability field.

CPU/candidate ratios require passing correctness for both rows, successful measurements, and reported GPU or mixed execution. Their labels preserve the evidence level. No GPU ratio is emitted for CPU fallback, unknown or unsupported work. A ratio below one indicates that the candidate took longer. Results describe complete library operations with mixed host work where applicable.

## Memory and reliability

Admission estimates include a 512 MiB reserve, 64 bytes per data element, algorithm-specific temporary budgets and dense-feature square terms for PCA. The limit is the smaller of 35% physical memory and 60% currently available memory. SVC has additional sample and quadratic-work ceilings. KNN has a brute-force work ceiling. These estimates are conservative heuristics and cannot guarantee against allocation failures.

The worker deadline covers the entire implementation process. A timed-out process group is killed and reaped. Completed JSONL rows are retained. Truncated records become explicit errors. Allocation failures, exceptions and unsupported parameters retain diagnostics and log files. Dataset sizes are never silently changed.

RSS snapshots measure the process. ru_maxrss is the process-lifetime high-water resident set, including imports, preprocessing and earlier repetitions. macOS reports it in bytes. Linux reports KiB, converted by the runner. MLX counters separately record active, cached and reset-peak allocator bytes. These counters overlap unified memory and must never be added to RSS or presented as total GPU usage. Native Metal allocations outside MLX may be absent. Memory plots show process high-water RSS for the fit-plus-inference pipeline.

Run metadata captures power source, reported thermal limits and load when available. Frequency, energy, fan speed, background GPU activity and memory pressure over time are unmeasured. A dedicated idle-machine repeated session is needed for tighter performance attribution.

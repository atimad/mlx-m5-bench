# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.00024099997244775295 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0013987499987706542 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.00019733404042199254 | 1.425005029886961e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0008102499996311963 | 3.125000512227416e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.003982750000432134 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.0029022920061834157 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.48194668068911656 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00021654204465448856 | 1.7667014617472887e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0007542090024799109 | 0.00039591698441654444 | GPU_REPORTED_UNVERIFIED | PASS | 1.0743043333704811 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.00028550002025440335 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0015485420008189976 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00020350003615021706 | 1.3166980352252722e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0009208749979734421 | 3.887503407895565e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.004054500022903085 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.0030377499642781913 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5097661160493013 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.0002276249579153955 | 1.604208955541253e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0008282089838758111 | 0.0002694160211831331 | GPU_REPORTED_UNVERIFIED | PASS | 1.1118872360741334 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00023962499108165503 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015750839957036078 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.0001906669931486249 | 9.792041964828968e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009712919709272683 | 4.029099363833666e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.004141375015024096 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.00338925002142787 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.46472936069792653 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.00022504100343212485 | 1.8208986148238182e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0004393329727463424 | 8.96669807843864e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.2108333113619105 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.0002531670033931732 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0017445419798605144 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.00020370801212266088 | 1.8499966245144606e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.001085124968085438 | 5.64999645575881e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.003920999995898455 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.0029978749807924032 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5819261947339093 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.00021012499928474426 | 1.879199407994747e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0007857500459067523 | 0.0003868750645779073 | GPU_REPORTED_UNVERIFIED | PASS | 1.3810052875443466 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.0002517919638194144 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.001756249985191971 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.0002079170080833137 | 1.333298860117793e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0011534170480445027 | 2.091703936457634e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.004000541986897588 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.0031797499977983534 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.55232329158204 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.00022287503816187382 | 2.2332940716296434e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0008584170136600733 | 0.00046145799569785595 | GPU_REPORTED_UNVERIFIED | PASS | 1.3436558568738333 | 0 |

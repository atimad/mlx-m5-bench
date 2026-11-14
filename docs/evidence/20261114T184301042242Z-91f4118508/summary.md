# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-600x16-c2 | fit | sklearn | cold | 0.001082208997104317 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-600x16-c2 | predict | sklearn | cold | 6.695801857858896e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-600x16-c2 | fit | sklearn | steady | 0.0008300420013256371 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-600x16-c2 | predict | sklearn | steady | 5.2749994210898876e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-600x16-c2 | fit | mlxlearn | cold | 0.029270166996866465 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.036973106344769864 | 0 |
| logistic-600x16-c2 | predict | mlxlearn | cold | 0.000194708991330117 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-600x16-c2 | fit | mlxlearn | steady | 0.006262041977606714 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.13255133138581585 | 0 |
| logistic-600x16-c2 | predict | mlxlearn | steady | 0.00012625003000721335 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-600x16-c3-k5 | fit | sklearn | cold | 0.0002068749745376408 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-600x16-c3-k5 | predict | sklearn | cold | 0.0009425839525647461 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-600x16-c3-k5 | fit | sklearn | steady | 0.000178125046659261 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-600x16-c3-k5 | predict | sklearn | steady | 0.00038883404340595007 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-600x16-c3-k5 | fit | mlxlearn | cold | 0.0037380409776233137 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-600x16-c3-k5 | predict | mlxlearn | cold | 0.0022227910230867565 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.424054237566514 | 0 |
| knn-600x16-c3-k5 | fit | mlxlearn | steady | 0.0002821250236593187 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-600x16-c3-k5 | predict | mlxlearn | steady | 0.0007147500291466713 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5440140294505099 | 0 |
| svc-600x16-c2 | fit | sklearn | cold | 0.0012969999806955457 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-600x16-c2 | predict | sklearn | cold | 0.0005564169841818511 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-600x16-c2 | fit | sklearn | steady | 0.019146875012665987 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-600x16-c2 | predict | sklearn | steady | 0.0006002080044709146 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-600x16-c2 | fit | mlxlearn | cold | 0.00636125000892207 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.20389074142289929 | 0 |
| svc-600x16-c2 | predict | mlxlearn | cold | 0.0008265839423984289 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.6731524236574726 | 0 |
| svc-600x16-c2 | fit | mlxlearn | steady | 0.0021699590142816305 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 8.823611361620394 | 0 |
| svc-600x16-c2 | predict | mlxlearn | steady | 0.0006852910155430436 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.8758439711854286 | 0 |
| pca-600x16-c2-p3 | fit | sklearn | cold | 0.00026474997866898775 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-600x16-c2-p3 | transform | sklearn | cold | 5.9624959249049425e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-600x16-c2-p3 | fit | sklearn | steady | 0.00017629197100177407 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-600x16-c2-p3 | transform | sklearn | steady | 4.254200030118227e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-600x16-c2-p3 | fit | mlxlearn | cold | 0.00316137500340119 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-600x16-c2-p3 | transform | mlxlearn | cold | 0.00014304200885817409 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-600x16-c2-p3 | fit | mlxlearn | steady | 0.00028237502556294203 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-600x16-c2-p3 | transform | mlxlearn | steady | 0.00012254196917638183 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |

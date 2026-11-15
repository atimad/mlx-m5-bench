# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q1 | fit | sklearn | cold | 0.00023966695880517364 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | cold | 0.0007704590098001063 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | steady | 0.0002181250019930303 | 3.7080026231706142e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | cold | 0.003881332988385111 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | cold | 0.0024875419912859797 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.30972703676925817 | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | steady | 0.0006474170368164778 | 3.9126083720475435e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.33691575845085747 | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | cold | 0.00024162500631064177 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | cold | 0.0007748749922029674 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | steady | 0.00023212499218061566 | 5.166977643966675e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | cold | 0.003936749999411404 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | cold | 0.002344458014704287 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.33051348641903683 | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | steady | 0.0006134160212241113 | 5.779101047664881e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3784136444910507 | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | cold | 0.0002908329479396343 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | cold | 0.0008270420366898179 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | steady | 0.00024270900757983327 | 1.0124989785254002e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | cold | 0.0038198749534785748 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | cold | 0.0022582089877687395 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.36623804137233124 | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | steady | 0.0006197500042617321 | 0.00013508298434317112 | GPU_REPORTED_UNVERIFIED | PASS | 0.39162405148985313 | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00024408299941569567 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.000811167003121227 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00023162498837336898 | 4.375004209578037e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0037727499729953706 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.0024544589687138796 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.33048709041824936 | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.0006544580101035535 | 5.6500022765249014e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3539187920348311 | 0 |

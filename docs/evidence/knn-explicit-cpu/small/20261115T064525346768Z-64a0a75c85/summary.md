# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q1 | fit | sklearn | cold | 0.00025995896430686116 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | cold | 0.0009089169907383621 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | sklearn | steady | 0.0001990000018849969 | 1.7457990907132626e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | steady | 0.0002734580193646252 | 4.195794463157654e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | cold | 0.0004272909718565643 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | cold | 0.0001829999964684248 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | steady | 0.00023258297005668283 | 2.0167033653706312e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | steady | 0.00010137498611584306 | 9.833020158112049e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | cold | 0.00042337499326094985 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | cold | 0.0009099169983528554 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | steady | 0.00020350003615021706 | 2.2166932467371225e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | steady | 0.00031095900340005755 | 5.116703687235713e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | cold | 0.0003528749803081155 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | cold | 0.00018166599329560995 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | steady | 0.00022204098058864474 | 1.587602309882641e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | steady | 0.00010279100388288498 | 5.541020072996616e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | cold | 0.00025750003987923265 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | cold | 0.0010565409902483225 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | steady | 0.00018983299378305674 | 8.625967893749475e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | steady | 0.00026287499349564314 | 2.2833002731204033e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | cold | 0.00035283295437693596 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | cold | 0.00017929199384525418 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | steady | 0.00021120900055393577 | 1.1918018572032452e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | steady | 0.00011620798613876104 | 9.083014447242022e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00028545898385345936 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0008935829973779619 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.000188209000043571 | 1.0834017302840948e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00027358403895050287 | 3.175105666741729e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0005038749659433961 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.00022304203594103456 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00020295800641179085 | 9.166018571704626e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.00012366700684651732 | 7.001042831689119e-06 | CPU_FALLBACK | PASS | ineligible | 0 |

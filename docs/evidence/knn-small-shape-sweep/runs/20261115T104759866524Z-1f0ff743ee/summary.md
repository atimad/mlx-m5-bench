# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | sklearn | cold | 0.00022983300732448697 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | cold | 0.0011169579811394215 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | steady | 0.0004390000249259174 | 1.2542062904685736e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | mlxlearn | cold | 0.012511332985013723 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | cold | 0.002482209005393088 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.4499854680700176 | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | steady | 0.000869459006935358 | 7.108296267688274e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.5049116996019064 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | sklearn | cold | 0.00024162500631064177 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | cold | 0.0010947499540634453 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | steady | 0.00045720802154392004 | 3.3333024475723505e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | mlxlearn | cold | 0.0041285420302301645 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | cold | 0.0024988329969346523 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.43810448933817825 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | steady | 0.0008338750340044498 | 5.329097621142864e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.548293212891034 | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | sklearn | cold | 0.0002353749587200582 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | cold | 0.0011300419573672116 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | steady | 0.0004944999818690121 | 1.0000017937272787e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | mlxlearn | cold | 0.0036936660180799663 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | cold | 0.003018292016349733 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3743978220947169 | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | steady | 0.0007574580376967788 | 1.1917029041796923e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.6528414212523909 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | sklearn | cold | 0.0002298750332556665 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | cold | 0.0013393340050242841 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | steady | 0.0006964170024730265 | 2.5749963242560625e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | mlxlearn | cold | 0.004274083999916911 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | cold | 0.002538125030696392 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.527686378261991 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | steady | 0.0009301659883931279 | 0.00021908199414610863 | GPU_REPORTED_UNVERIFIED | PASS | 0.7487018566181877 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | sklearn | cold | 0.00023283303016796708 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | cold | 0.0013619999517686665 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | steady | 0.0007167920120991766 | 5.537603283300996e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | mlxlearn | cold | 0.005064499971922487 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | cold | 0.0025957079487852752 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5247123245918508 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | steady | 0.0009963749907910824 | 3.8583006244152784e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7193998431555093 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | sklearn | cold | 0.00022804096806794405 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | cold | 0.0013251249911263585 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | steady | 0.0006767089944332838 | 1.8041988369077444e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | mlxlearn | cold | 0.0042059170082211494 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | cold | 0.003059374983422458 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.43313585235765023 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | steady | 0.0009886670159175992 | 8.649996016174555e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.6844660371371025 | 0 |

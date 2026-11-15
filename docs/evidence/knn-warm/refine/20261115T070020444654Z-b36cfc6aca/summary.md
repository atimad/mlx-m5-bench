# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.0002460419782437384 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0014213749673217535 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0007736249826848507 | 2.6583962608128786e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.00038487499114125967 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.0066263750195503235 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.21450264482890832 | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0010579579975456 | 0.00015908299246802926 | GPU_REPORTED_UNVERIFIED | PASS | 0.7312435696687534 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.00027304200921207666 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0015519580338150263 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008772080182097852 | 2.2666004952043295e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.0004379170131869614 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.009102707961574197 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.1704941035531843 | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.000812250014860183 | 4.037498729303479e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.0799729174037427 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00023674999829381704 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.001566625025589019 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009852920193225145 | 6.029097130522132e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.0004009590484201908 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.009177708998322487 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.17069892125315464 | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.000916499993763864 | 4.850002005696297e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.075059493755299 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.0002619169536046684 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0016770829679444432 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.0010305829928256571 | 2.5916029699146748e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.0003828330081887543 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.008858167042490095 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.18932618451424044 | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0009392500505782664 | 0.0002252499107271433 | GPU_REPORTED_UNVERIFIED | PASS | 1.0972402846197984 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.00025983399245887995 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.001774667005520314 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.001091625017579645 | 2.7541012968868017e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.00037349999183788896 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.0065224169520661235 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.27208732875596797 | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.001271958986762911 | 3.549997927621007e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8582234403310366 | 0 |

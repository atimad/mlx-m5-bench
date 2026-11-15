# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k5-t1536-q8 | fit | sklearn | cold | 0.000226958014536649 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | cold | 0.0008339170017279685 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | steady | 0.00022412498947232962 | 4.082976374775171e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | fit | mlxlearn | cold | 0.0009939580340869725 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | cold | 0.001615708984900266 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | steady | 0.0006235000328160822 | 4.233303479850292e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | sklearn | cold | 0.00022179196821525693 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | cold | 0.0008432500180788338 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | steady | 0.00023241696180775762 | 2.7080532163381577e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | mlxlearn | cold | 0.0009679159848019481 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | cold | 0.0021895000245422125 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | steady | 0.0009276249911636114 | 7.408298552036285e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | sklearn | cold | 0.00022350001381710172 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | cold | 0.0008638750296086073 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | steady | 0.0002357920166105032 | 3.7090503610670567e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | mlxlearn | cold | 0.0009955830173566937 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | cold | 0.002548249962273985 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | steady | 0.0012889160425402224 | 6.895704427734017e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | sklearn | cold | 0.0002185420016758144 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | cold | 0.0008487079758197069 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | steady | 0.0002477910020388663 | 6.665999535471201e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | mlxlearn | cold | 0.0009970419923774898 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | cold | 0.003562208032235503 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | steady | 0.0018754589837044477 | 5.083298310637474e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | sklearn | cold | 0.00023508397862315178 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | cold | 0.0009241669904440641 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | steady | 0.000269667012616992 | 1.0000017937272787e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | mlxlearn | cold | 0.0009197919862344861 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | cold | 0.004587416013237089 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | steady | 0.0024688749690540135 | 2.220796886831522e-05 | CPU_FALLBACK | PASS | ineligible | 0 |

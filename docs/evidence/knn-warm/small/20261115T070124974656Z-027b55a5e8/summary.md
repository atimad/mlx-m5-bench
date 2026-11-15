# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q1 | fit | sklearn | cold | 0.00023395800963044167 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | cold | 0.0007682919967919588 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | steady | 0.00022024998906999826 | 6.4159976318478584e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | cold | 0.0038804170326329768 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | cold | 0.005048749968409538 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.15217469702386288 | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | steady | 0.0006150840199552476 | 8.979096310213208e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3580811432656359 | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | cold | 0.0002401249948889017 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | cold | 0.0008181669982150197 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | steady | 0.00023545895237475634 | 7.291906513273716e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | cold | 0.004106333013623953 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | cold | 0.00231087498832494 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3540507393730008 | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | steady | 0.000731833977624774 | 8.15820530988276e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.32173820780904067 | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | cold | 0.0002565000322647393 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | cold | 0.0008393750176765025 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | steady | 0.00023608299670740962 | 7.958034984767437e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | cold | 0.003975666011683643 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | cold | 0.004786500008776784 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.17536300347589664 | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | steady | 0.0006696669734083116 | 0.00011320802150294185 | GPU_REPORTED_UNVERIFIED | PASS | 0.3525379122489057 | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00023829098790884018 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0008116670069284737 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.0002382080419920385 | 5.00003807246685e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0034748329780995846 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.002548791002482176 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.31845177032484046 | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.0006825830205343664 | 7.533299503847957e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3489803215520291 | 0 |

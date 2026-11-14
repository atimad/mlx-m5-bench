# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.0002989170025102794 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0008422079845331609 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.00017087499145418406 | 4.708010237663984e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00023391703143715858 | 6.834045052528381e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.003805041022133082 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.0022732910001650453 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3704796194028899 | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00020337500609457493 | 1.4750054106116295e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.000633042014669627 | 9.441602742299438e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.36951264847600296 | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | cold | 0.0002490829792805016 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | cold | 0.0008145410101860762 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | steady | 0.0001818329910747707 | 8.916947990655899e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | steady | 0.000280165986623615 | 4.512403393164277e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | cold | 0.0032503330148756504 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | cold | 0.0025136249605566263 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.32405033486208745 | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | steady | 0.00021962501341477036 | 2.216600114479661e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | steady | 0.0007111249724403024 | 0.00014050002209842205 | GPU_REPORTED_UNVERIFIED | PASS | 0.39397573911965866 | 0 |

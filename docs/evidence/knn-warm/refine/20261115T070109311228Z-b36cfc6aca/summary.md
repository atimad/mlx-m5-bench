# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.00026462500682100654 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0014422920066863298 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0008495840011164546 | 5.408399738371372e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.00039829203160479665 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.006118290999438614 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.23573445702707962 | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0011353329755365849 | 3.8833997678011656e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7483126267119312 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.00023725000210106373 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.001500708982348442 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008674999698996544 | 2.6499968953430653e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.0005802909727208316 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.007842542021535337 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.19135491760548423 | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0009175839950330555 | 0.0001121259992942214 | GPU_REPORTED_UNVERIFIED | PASS | 0.9454175035696902 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.000249749980866909 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015601659542880952 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.000920834019780159 | 2.666696673259139e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.00034958403557538986 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.006462083023507148 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.24143390739683668 | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0012012500083073974 | 7.075001485645771e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7665631745365362 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.00023529096506536007 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.001611042011063546 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.000988125044386834 | 3.0624913051724434e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.0003601659554988146 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.006049707997590303 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.2663007886835613 | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0011877089855261147 | 0.0001231240457855165 | GPU_REPORTED_UNVERIFIED | PASS | 0.8319588859127205 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.00027079094434157014 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0017654160037636757 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010901669738814235 | 3.083399496972561e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.00036266696406528354 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.006828207988291979 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.25854748519534776 | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0012598329922184348 | 7.533404277637601e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8653265794871373 | 0 |

# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00025870901299640536 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0008043749839998782 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.00018833298236131668 | 1.033296575769782e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00026050000451505184 | 2.2374966647475958e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0003862919984385371 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.0001852919813245535 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00019687501480802894 | 1.5792029444128275e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.00012737500946968794 | 8.333998266607523e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | cold | 0.0002473330241627991 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | cold | 0.000818458036519587 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | steady | 0.00017116597155109048 | 3.7080026231706142e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | steady | 0.00023416697513312101 | 7.125025149434805e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | cold | 0.00037604098906740546 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | cold | 0.17069591698236763 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.004794830778548331 | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | steady | 0.00021312502212822437 | 1.4290970284491777e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | steady | 0.0006997500313445926 | 0.0002852080506272614 | GPU_REPORTED_UNVERIFIED | PASS | 0.3346437508307953 | 0 |

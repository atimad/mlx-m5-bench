# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | sklearn | cold | 0.0002987500047311187 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | cold | 0.001173791999462992 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | steady | 0.00044695899123325944 | 1.8665974494069815e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | mlxlearn | cold | 0.004290624987334013 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | cold | 0.0026222090236842632 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.447634795266545 | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | steady | 0.0008327090181410313 | 8.945900481194258e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.5367529130776875 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | sklearn | cold | 0.00022845796775072813 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | cold | 0.001080874993931502 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | steady | 0.00043995800660923123 | 1.491600414738059e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | mlxlearn | cold | 0.0036643330240622163 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | cold | 0.00256529200123623 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.42134579354343354 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | steady | 0.0008337080362252891 | 0.00010412593837827444 | GPU_REPORTED_UNVERIFIED | PASS | 0.5277123255296815 | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | sklearn | cold | 0.00023916701320558786 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | cold | 0.0011359170312061906 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | steady | 0.0005118339904583991 | 2.3542961571365595e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | mlxlearn | cold | 0.004112624970730394 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | cold | 0.0026539170066826046 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.42801528018620544 | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | steady | 0.0009252920281141996 | 5.6999968364834785e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.5531594079563695 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | sklearn | cold | 0.00029495899798348546 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | cold | 0.0013419170281849802 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | steady | 0.000684124999679625 | 3.374996595084667e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | mlxlearn | cold | 0.004208208003547043 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | cold | 0.002582124958280474 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5196948443109465 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | steady | 0.0009757080115377903 | 6.662501255050302e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7011575098183235 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | sklearn | cold | 0.00025162496604025364 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | cold | 0.001377624983433634 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | steady | 0.0007372500258497894 | 4.133296897634864e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | mlxlearn | cold | 0.004765041987411678 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | cold | 0.0032867920235730708 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.41913968804634566 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | steady | 0.0009567909874022007 | 9.516801219433546e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7705444925348945 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | sklearn | cold | 0.00028325000312179327 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | cold | 0.0014677500003017485 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | steady | 0.0006698750075884163 | 1.5207973774522543e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | mlxlearn | cold | 0.00482008297694847 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | cold | 0.0030727090197615325 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.4776729559688857 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | steady | 0.0010116660268977284 | 6.654101889580488e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.6621503438665293 | 0 |

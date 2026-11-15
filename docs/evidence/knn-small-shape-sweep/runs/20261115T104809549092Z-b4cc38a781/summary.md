# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | sklearn | cold | 0.00024637498427182436 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | cold | 0.0011929160100407898 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | steady | 0.000454624998383224 | 2.7375004719942808e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | mlxlearn | cold | 0.0010423329658806324 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | cold | 0.027585792005993426 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | steady | 0.011728541983757168 | 0.00011487596202641726 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | sklearn | cold | 0.00024120899615809321 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | cold | 0.0010951249860227108 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | steady | 0.0004498339840210974 | 1.679197885096073e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | mlxlearn | cold | 0.0009674580069258809 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | cold | 0.016790041991043836 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | steady | 0.011696250003296882 | 0.00013174995547160506 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | sklearn | cold | 0.00023870798759162426 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | cold | 0.0011669170344248414 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | steady | 0.000497375032864511 | 1.3584038242697716e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | mlxlearn | cold | 0.0009735000203363597 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | cold | 0.01705966697772965 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | steady | 0.011762209003791213 | 6.212398875504732e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | sklearn | cold | 0.0002269999822601676 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | cold | 0.0014141250285319984 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | steady | 0.0006743749836459756 | 3.133405698463321e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | mlxlearn | cold | 0.0010613329941406846 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | cold | 0.03147020802134648 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | steady | 0.020833459042478353 | 0.00014612491941079497 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | sklearn | cold | 0.00024099997244775295 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | cold | 0.0013832090189680457 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | steady | 0.0006896249833516777 | 2.216600114479661e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | mlxlearn | cold | 0.0010509590501897037 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | cold | 0.025498417031485587 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | steady | 0.02030037500662729 | 8.233397966250777e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | sklearn | cold | 0.00023258297005668283 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | cold | 0.0014023749972693622 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | steady | 0.0007194579811766744 | 3.208301495760679e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | mlxlearn | cold | 0.0009983330382965505 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | cold | 0.02602058299817145 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | steady | 0.0203719999990426 | 0.00010879198089241982 | CPU_FALLBACK | PASS | ineligible | 0 |

# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-12000x32-c2 | fit | sklearn | cold | 0.0029183750157244503 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | predict | sklearn | cold | 9.674998000264168e-05 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | fit | sklearn | steady | 0.0026365420198999345 | 6.295798812061548e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | predict | sklearn | steady | 8.299999171867967e-05 | 1.0420335456728935e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | fit | sklearn | cold | 0.0002835000050254166 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | predict | sklearn | cold | 0.007262582948897034 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | fit | sklearn | steady | 0.00030808296287432313 | 2.4374981876462698e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | predict | sklearn | steady | 0.006558625027537346 | 0.0002113750670105219 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | cold | 0.3581538329599425 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | cold | 0.16872150002745911 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | steady | 0.3578827089513652 | 0.0004622080596163869 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | steady | 0.16891079198103398 | 6.162497447803617e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | cold | 0.004407207947224379 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | cold | 0.00023737497394904494 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | steady | 0.0040166249964386225 | 1.395895378664136e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | steady | 0.00020599999697878957 | 2.0830193534493446e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |

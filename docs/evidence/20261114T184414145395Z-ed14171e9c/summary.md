# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-12000x32-c2 | fit | sklearn | cold | 0.0030007080058567226 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | predict | sklearn | cold | 0.0001068339915946126 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | fit | sklearn | steady | 0.0025511669809930027 | 2.4170149117708206e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | predict | sklearn | steady | 8.000002708286047e-05 | 2.125045284628868e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | fit | sklearn | cold | 0.0003541670157574117 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | predict | sklearn | cold | 0.023811499995645136 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | fit | sklearn | steady | 0.00028137495974078774 | 9.416951797902584e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | predict | sklearn | steady | 0.024343458004295826 | 0.00020837498595938087 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | cold | 0.35340012499364093 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | cold | 0.16984916699584574 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | steady | 0.35189225000794977 | 7.591699250042439e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | steady | 0.16751166700851172 | 6.795796798542142e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | cold | 0.004339417035225779 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | cold | 0.00023745803628116846 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | steady | 0.004012291028629988 | 5.320704076439142e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | steady | 0.00020662497263401747 | 4.041008651256561e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |

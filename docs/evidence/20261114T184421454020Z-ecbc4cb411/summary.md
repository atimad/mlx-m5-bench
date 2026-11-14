# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-12000x32-c2 | fit | sklearn | cold | 0.0030052090296521783 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | predict | sklearn | cold | 0.00010062498040497303 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | fit | sklearn | steady | 0.002565415983553976 | 3.8790982216596603e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| logistic-12000x32-c2 | predict | sklearn | steady | 8.174998220056295e-05 | 2.833025064319372e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | fit | sklearn | cold | 0.000278000021353364 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | predict | sklearn | cold | 0.008588750031776726 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | fit | sklearn | steady | 0.0002946669701486826 | 1.8124061170965433e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| knn-8000x32-c2-k5 | predict | sklearn | steady | 0.00848429201869294 | 4.983297549188137e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | cold | 0.3541142920148559 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | cold | 0.1676749589969404 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | steady | 0.35551929101347923 | 0.00045470899203792214 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | steady | 0.168524292006623 | 0.00016133300960063934 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | cold | 0.004404916020575911 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | cold | 0.0002473330241627991 | 0.0 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | steady | 0.00406458304496482 | 2.7583912014961243e-05 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | steady | 0.00022466597147285938 | 3.958994057029486e-06 | CPU_BASELINE | INCONCLUSIVE | ineligible | 0 |

# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-8000x128-c3-k5 | fit | sklearn | cold | 0.0004171669716015458 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | cold | 0.013763749971985817 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | sklearn | steady | 0.0004262080183252692 | 3.9207981899380684e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | steady | 0.01245237496914342 | 8.016597712412477e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | cold | 0.004014457983430475 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | cold | 0.011487666983157396 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 1.1981327446352241 | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | steady | 0.00040716701187193394 | 3.554200520738959e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | steady | 0.002266415976919234 | 0.00018329202430322766 | GPU_REPORTED_UNVERIFIED | PASS | 5.4943025004924655 | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | cold | 0.0006908749928697944 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | cold | 0.11017445795005187 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | steady | 0.0007122090319171548 | 4.112598253414035e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | steady | 0.11471729096956551 | 0.0022584159742109478 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | cold | 0.005744708993006498 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | cold | 0.03649570798734203 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 3.0188332827592816 | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | steady | 0.0008756250026635826 | 8.79999715834856e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | steady | 0.014861166011542082 | 0.0008684580097906291 | GPU_REPORTED_UNVERIFIED | PASS | 7.7192658288366545 | 0 |
| logistic-2000x32-c2 | fit | sklearn | cold | 0.0014757090248167515 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | cold | 7.404200732707977e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | sklearn | steady | 0.0011430000304244459 | 4.1082967072725296e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | steady | 5.924998549744487e-05 | 1.7500133253633976e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | cold | 0.03075274999719113 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.04798624594390871 | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | cold | 0.00022200000239536166 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | steady | 0.002924000029452145 | 7.34590576030314e-05 | MIXED_CPU_GPU_REPORTED | PASS | 0.39090287924470507 | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | steady | 0.00012041704030707479 | 3.875058609992266e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | cold | 0.04513008298818022 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | cold | 0.0010081250220537186 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | steady | 0.043670249986462295 | 0.0012297080247662961 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | steady | 0.001040667004417628 | 1.7042038962244987e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | cold | 0.05435020802542567 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.8303571343658488 | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | cold | 0.0020347919780761003 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | steady | 0.017247583018615842 | 0.0002947500324808061 | MIXED_CPU_GPU_REPORTED | PASS | 2.5319634605803993 | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | steady | 0.0017891250317916274 | 1.487502595409751e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | cold | 0.3543222090229392 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | cold | 0.16494745900854468 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | steady | 0.3518142079701647 | 0.0034397909766994417 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | steady | 0.1670719159883447 | 0.001110876037273556 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | mlxlearn | cold | 0.04450224997708574 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 7.961894268388231 | 0 |
| svc-4000x256-c3 | predict | mlxlearn | cold | 0.0033022089628502727 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 49.95064239247044 | 0 |
| svc-4000x256-c3 | fit | mlxlearn | steady | 0.03384370799176395 | 0.00027908297488465905 | MIXED_CPU_GPU_REPORTED | PASS | 10.395261891982422 | 0 |
| svc-4000x256-c3 | predict | mlxlearn | steady | 0.00239387498004362 | 7.741706212982535e-05 | MIXED_CPU_GPU_REPORTED | PASS | 69.79141240922297 | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | cold | 0.004504000011365861 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | cold | 0.00025770801585167646 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | steady | 0.004062916967086494 | 7.204193389043212e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | steady | 0.0002210829989053309 | 1.2499047443270683e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | cold | 0.010514499968849123 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.4283608373873866 | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | cold | 0.0014351660502143204 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.1795666890344791 | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | steady | 0.0040314579964615405 | 5.887501174584031e-05 | MIXED_CPU_GPU_REPORTED | PASS | 1.0078033730359006 | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | steady | 0.0007556250202469528 | 2.1916988771408796e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.2925829518364502 | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | cold | 0.0003692079917527735 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | cold | 6.908300565555692e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | steady | 0.00018350000027567148 | 5.416979547590017e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | steady | 4.0000013541430235e-05 | 1.4170072972774506e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | cold | 0.007081666961312294 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.05213574625434745 | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | cold | 0.00016287504695355892 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | steady | 0.0016466670203953981 | 5.462497938424349e-05 | MIXED_CPU_GPU_REPORTED | PASS | 0.11143722319258535 | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | steady | 9.616697207093239e-05 | 5.166977643966675e-06 | CPU_FALLBACK | PASS | ineligible | 0 |

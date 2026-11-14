# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-8000x128-c3-k5 | fit | sklearn | cold | 0.00043162499787285924 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | cold | 0.013487707998137921 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | sklearn | steady | 0.00046191702131181955 | 1.2334028724581003e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | steady | 0.012691916024778038 | 3.787403693422675e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | cold | 0.004194999986793846 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | cold | 0.014844708028249443 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.9085869504789752 | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | steady | 0.000449208018835634 | 8.866697316989303e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | steady | 0.0017372500151395798 | 9.591702837496996e-05 | GPU_REPORTED_UNVERIFIED | PASS | 7.305750993911088 | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | cold | 0.0007129579898901284 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | cold | 0.10852416697889566 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | steady | 0.0007049999549053609 | 1.5417055692523718e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | steady | 0.11042608303250745 | 0.0003126250230707228 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | cold | 0.004377041012048721 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | cold | 0.0298477080068551 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 3.635929665151207 | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | steady | 0.0007960000075399876 | 0.00011316698510199785 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | steady | 0.014965582988224924 | 0.0003108749515376985 | GPU_REPORTED_UNVERIFIED | PASS | 7.378668984655783 | 0 |
| logistic-2000x32-c2 | fit | sklearn | cold | 0.0014475000207312405 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | cold | 8.012499893084168e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | sklearn | steady | 0.001150249969214201 | 2.59590451605618e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | steady | 6.116600707173347e-05 | 2.7070054784417152e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | cold | 0.028750625031534582 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.050346732258640545 | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | cold | 0.0002471660263836384 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | steady | 0.003678457986097783 | 0.000682291982229799 | MIXED_CPU_GPU_REPORTED | PASS | 0.31269895525826574 | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | steady | 0.00012395798694342375 | 1.3665994629263878e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | cold | 0.0445202499977313 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | cold | 0.0010754999821074307 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | steady | 0.042906083981506526 | 0.00023375096498057246 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | steady | 0.001061249990016222 | 1.020805211737752e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | cold | 0.0525004580267705 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.8479973636616652 | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | cold | 0.0021183330100029707 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | steady | 0.01830325002083555 | 0.0003339999821037054 | MIXED_CPU_GPU_REPORTED | PASS | 2.344178434576607 | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | steady | 0.001831499976105988 | 2.370803849771619e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | cold | 0.3507349999854341 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | cold | 0.16485208296217024 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | steady | 0.34969270799774677 | 0.001455708988942206 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | steady | 0.165364500018768 | 0.00027495797257870436 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | mlxlearn | cold | 0.044197707960847765 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 7.93559250394003 | 0 |
| svc-4000x256-c3 | predict | mlxlearn | cold | 0.005682249960955232 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 29.011761906802366 | 0 |
| svc-4000x256-c3 | fit | mlxlearn | steady | 0.03398591699078679 | 0.00028012500843033195 | MIXED_CPU_GPU_REPORTED | PASS | 10.289341555578583 | 0 |
| svc-4000x256-c3 | predict | mlxlearn | steady | 0.002332500007469207 | 1.4749995898455381e-05 | MIXED_CPU_GPU_REPORTED | PASS | 70.89581971671274 | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | cold | 0.004401999991387129 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | cold | 0.00028379098512232304 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | steady | 0.004204583005048335 | 8.529197657480836e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | steady | 0.00022074999287724495 | 1.2874952517449856e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | cold | 0.011278124991804361 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.39031310564353505 | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | cold | 0.0014306249795481563 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.19836853765265208 | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | steady | 0.0034845000482164323 | 0.0006648750277236104 | MIXED_CPU_GPU_REPORTED | PASS | 1.2066531631131652 | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | steady | 0.0008438749937340617 | 8.566700853407383e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.2615908689276933 | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | cold | 0.00033833301858976483 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | cold | 6.866699550300837e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | steady | 0.00019670900655910373 | 1.0834017302840948e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | steady | 4.2834028135985136e-05 | 2.7500209398567677e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | cold | 0.0063429580186493695 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.05333994290912986 | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | cold | 0.00017566699534654617 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | steady | 0.0007949999999254942 | 4.395801806822419e-05 | MIXED_CPU_GPU_REPORTED | PASS | 0.24743271267614955 | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | steady | 9.92499990388751e-05 | 1.2208009138703346e-05 | CPU_FALLBACK | PASS | ineligible | 0 |

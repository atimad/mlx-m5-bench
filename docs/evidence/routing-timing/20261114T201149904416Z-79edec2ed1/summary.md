# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-8000x128-c3-k5 | fit | sklearn | cold | 0.0004099169746041298 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | cold | 0.013463540992233902 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | sklearn | steady | 0.00048004096606746316 | 2.120796125382185e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | steady | 0.012646874994970858 | 1.8584018107503653e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | cold | 0.004283207992557436 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | cold | 0.011666333011817187 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 1.1540508040183892 | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | steady | 0.0003861250006593764 | 6.249989382922649e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | steady | 0.0016347920172847807 | 3.804202424362302e-05 | GPU_REPORTED_UNVERIFIED | PASS | 7.73607581958713 | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | cold | 0.0006894589751027524 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | cold | 0.11627324996516109 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | steady | 0.0007196670048870146 | 3.2957992516458035e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | steady | 0.11105437501100823 | 0.004315334022976458 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | cold | 0.004786250006873161 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | cold | 0.03038716595619917 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 3.8263933574049087 | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | steady | 0.0008333749719895422 | 5.9790967497974634e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | steady | 0.014896999986376613 | 0.00040929100941866636 | GPU_REPORTED_UNVERIFIED | PASS | 7.454814735353968 | 0 |
| logistic-2000x32-c2 | fit | sklearn | cold | 0.001506833010353148 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | cold | 7.866695523262024e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | sklearn | steady | 0.0011021249811165035 | 2.1082989405840635e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | steady | 5.7165976613759995e-05 | 7.509952411055565e-07 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | cold | 0.050317457993514836 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | cold | 0.00022899999748915434 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | steady | 0.004930666007567197 | 5.162501474842429e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | steady | 0.00012091605458408594 | 2.91608739644289e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | cold | 0.043875666975509375 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | cold | 0.0010969580034725368 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | steady | 0.043143499991856515 | 4.629202885553241e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | steady | 0.0010382499895058572 | 1.5457975678145885e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | cold | 0.09094070800347254 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | cold | 0.0017773750005289912 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | steady | 0.043618292023893446 | 0.0001063330564647913 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | steady | 0.001842374971602112 | 2.2957974579185247e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | cold | 0.35996462497860193 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | cold | 0.1739067499875091 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | steady | 0.3535587079823017 | 0.001454374985769391 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | steady | 0.1676599580096081 | 0.00038175005465745926 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | mlxlearn | cold | 0.0500071250135079 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | mlxlearn | cold | 0.004902833024971187 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | mlxlearn | steady | 0.04037104203598574 | 0.00011812505545094609 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | mlxlearn | steady | 0.0036127500352449715 | 6.541702896356583e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | cold | 0.0043088330421596766 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | cold | 0.00022799998987466097 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | steady | 0.004031791992019862 | 4.091695882380009e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | steady | 0.00021291698794811964 | 1.1165975593030453e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | cold | 0.0033043749863281846 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | cold | 0.00029329198878258467 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | steady | 0.002796459011733532 | 4.4248998165130615e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | steady | 0.00022479199105873704 | 2.2292020730674267e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | cold | 0.0003625419922173023 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | cold | 7.191597251221538e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | steady | 0.00017433299217373133 | 2.6659690774977207e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | steady | 3.97919793613255e-05 | 2.4994369596242905e-07 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | cold | 0.0005169999785721302 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | cold | 0.0001495840260758996 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | steady | 0.00026045902632176876 | 2.541701542213559e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | steady | 9.983294876292348e-05 | 5.875015631318092e-06 | CPU_FALLBACK | PASS | ineligible | 0 |

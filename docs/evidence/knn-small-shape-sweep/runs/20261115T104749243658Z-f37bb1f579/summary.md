# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | sklearn | cold | 0.000259542022831738 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | cold | 0.001149207993876189 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | steady | 0.00043412501690909266 | 2.0665989723056555e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | mlxlearn | cold | 0.0003796250093728304 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | cold | 0.20504783297656104 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.0056045849263257255 | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | steady | 0.0004925840185023844 | 0.00015816703671589494 | GPU_REPORTED_UNVERIFIED | PASS | 0.881321765632945 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | sklearn | cold | 0.00023570802295580506 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | cold | 0.0011678339797072113 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | steady | 0.00047720898874104023 | 3.770896000787616e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | mlxlearn | cold | 0.00039833300979807973 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | cold | 0.006265416042879224 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.18639368426849787 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | steady | 0.0008786669932305813 | 3.5541015677154064e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.5431056275216318 | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | sklearn | cold | 0.00024999998277053237 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | cold | 0.0016020420007407665 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | steady | 0.0006362079875543714 | 6.341701373457909e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | mlxlearn | cold | 0.00039125001057982445 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | cold | 0.008506499987561256 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.18833151155979239 | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | steady | 0.0008393339812755585 | 0.0003282929537817836 | GPU_REPORTED_UNVERIFIED | PASS | 0.7579914572117156 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | sklearn | cold | 0.00025058299070224166 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | cold | 0.001374749990645796 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | steady | 0.000719625037163496 | 3.870902583003044e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | mlxlearn | cold | 0.00038416701136156917 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | cold | 0.07460920803714544 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.018426009695228958 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | steady | 0.0005949999904260039 | 2.9582995921373367e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.2094538634332817 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | sklearn | cold | 0.0002282080240547657 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | cold | 0.0013983329990878701 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | steady | 0.0006892919773235917 | 1.9708008039742708e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | mlxlearn | cold | 0.0006571250269189477 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | cold | 0.01434404100291431 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.09748529014967036 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | steady | 0.0011146249598823488 | 0.00011337501928210258 | GPU_REPORTED_UNVERIFIED | PASS | 0.6184070894988284 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | sklearn | cold | 0.00023866695119068027 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | cold | 0.0014070000033825636 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | steady | 0.0007433749851770699 | 3.283302066847682e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | mlxlearn | cold | 0.00035200000274926424 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | cold | 0.07427033298881724 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.0189443071918691 | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | steady | 0.001035124994814396 | 4.804198397323489e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7181499711639766 | 0 |

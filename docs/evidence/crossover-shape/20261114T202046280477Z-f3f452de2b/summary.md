# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-330000x33-c2 | fit | sklearn | cold | 0.06506716704461724 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | cold | 0.0007187920273281634 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | sklearn | steady | 0.064875416981522 | 0.00022529199486598372 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | steady | 0.00072975002694875 | 1.625006552785635e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | cold | 0.0861686670104973 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | cold | 0.0010984159889630973 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | steady | 0.0410520420409739 | 7.983302930369973e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | steady | 0.0010430829715915024 | 1.091597368940711e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | cold | 0.06090100004803389 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | cold | 0.0007172079640440643 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | steady | 0.06045841600280255 | 9.837601101025939e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | steady | 0.0007089590071700513 | 1.2041011359542608e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | cold | 0.5943194580031559 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.10247182593121577 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | cold | 0.0011160839931108057 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | steady | 0.010857459041289985 | 0.00021458405535668135 | MIXED_CPU_GPU_REPORTED | PASS | 5.568376152549541 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | steady | 0.0010632920311763883 | 2.39989603869617e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | cold | 0.33431995898718014 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | cold | 0.15060325001832098 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | steady | 0.32901462499285117 | 0.002435542002785951 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | steady | 0.1504101250320673 | 0.0002064159489236772 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | mlxlearn | cold | 0.03140804101713002 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | mlxlearn | cold | 0.003635375003796071 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | mlxlearn | steady | 0.0247670829994604 | 4.8250018153339624e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | mlxlearn | steady | 0.0026016670162789524 | 1.7251004464924335e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | sklearn | cold | 0.3392340409918688 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | cold | 0.15729920897865668 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | sklearn | steady | 0.34388579201186076 | 0.002820208959747106 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | steady | 0.1585085410042666 | 0.0011995829991064966 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | mlxlearn | cold | 0.032047374988906085 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 10.585392441948905 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | cold | 0.002580291999038309 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 60.961786122378044 | 0 |
| svc-2756x512-c3 | fit | mlxlearn | steady | 0.0224382079904899 | 0.00020370801212266088 | MIXED_CPU_GPU_REPORTED | PASS | 15.325902681605038 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | steady | 0.001903541968204081 | 0.00011833303142338991 | MIXED_CPU_GPU_REPORTED | PASS | 83.2703158910719 | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | cold | 0.015390124986879528 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | cold | 0.00047741696471348405 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | steady | 0.014764874998945743 | 8.270901162177324e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | steady | 0.0003820000565610826 | 5.457957740873098e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | cold | 0.011408916965592653 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | cold | 0.00037937500746920705 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | steady | 0.010534083005040884 | 9.983399650081992e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | steady | 0.00038658297853544354 | 7.4169947765767574e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | cold | 0.01741124998079613 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | cold | 0.0004613329656422138 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | steady | 0.01654945802874863 | 5.249993409961462e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | steady | 0.0003986249794252217 | 1.554196933284402e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | cold | 0.08044966700254008 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.21642413983200692 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | cold | 0.0011425840202718973 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.4037628370930934 | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | steady | 0.010426375025417656 | 8.087500464171171e-05 | MIXED_CPU_GPU_REPORTED | PASS | 1.5872686325212726 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | steady | 0.0011169160134159029 | 1.1791940778493881e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.356897899785762 | 0 |

# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-103200x256-c2 | fit | sklearn | cold | 0.04395654203835875 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | cold | 0.0011171669466421008 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | sklearn | steady | 0.04178958403645083 | 0.00019270903430879116 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | steady | 0.0010493750451132655 | 1.3000040780752897e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | cold | 0.09677433298202232 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | cold | 0.0019565830007195473 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | steady | 0.0435481250169687 | 0.0003725829301401973 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | steady | 0.001937583030667156 | 3.9040984120219946e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | cold | 0.04343158402480185 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | cold | 0.0024459579726681113 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | steady | 0.041737916006240994 | 0.00012924900511279702 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | steady | 0.0010490830172784626 | 4.520895890891552e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | cold | 0.04958420805633068 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.8759156539408863 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | cold | 0.0035974160418845713 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | steady | 0.016067332995589823 | 0.00026937597431242466 | MIXED_CPU_GPU_REPORTED | PASS | 2.597687868776807 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | steady | 0.0018983340123668313 | 4.225003067404032e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | cold | 0.5739670839975588 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | cold | 0.2772015000227839 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | steady | 0.5663022910011932 | 7.60830007493496e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | steady | 0.27569291699910536 | 0.0003147090319544077 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | mlxlearn | cold | 0.07917095796437934 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | mlxlearn | cold | 0.00779358297586441 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | mlxlearn | steady | 0.0659786660107784 | 0.0001655840314924717 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | mlxlearn | steady | 0.00547916698269546 | 8.979206904768944e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | sklearn | cold | 0.6052723749889992 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | cold | 0.28071520902449265 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | sklearn | steady | 0.5800792920053937 | 0.0008340409840457141 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | steady | 0.2814448330318555 | 0.00037095899460837245 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | mlxlearn | cold | 0.06582416698802263 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 9.195291071425707 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | cold | 0.00470629200572148 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 59.646789592151265 | 0 |
| svc-5256x256-c3 | fit | mlxlearn | steady | 0.05230508401291445 | 0.0004606239963322878 | MIXED_CPU_GPU_REPORTED | PASS | 11.090304182709438 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | steady | 0.003180166007950902 | 4.7708977945148945e-05 | MIXED_CPU_GPU_REPORTED | PASS | 88.50004444051045 | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | cold | 0.006752333021722734 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | cold | 0.0006868340424261987 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | steady | 0.006497290974948555 | 2.4709035642445087e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | steady | 0.0006744580459780991 | 2.5167071726173162e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | cold | 0.004976500000339001 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | cold | 0.0008417500066570938 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | steady | 0.004596916027367115 | 8.666794747114182e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | steady | 0.0004909160197712481 | 7.4169947765767574e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | cold | 0.0068746249889954925 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | cold | 0.0006597500178031623 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | steady | 0.006489542021881789 | 5.8542005717754364e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | steady | 0.0006850000354461372 | 3.3294782042503357e-07 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | cold | 0.013520625012461096 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.5084546744443833 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | cold | 0.00181816698750481 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.36286546963905697 | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | steady | 0.00446924997959286 | 0.0006946669891476631 | MIXED_CPU_GPU_REPORTED | PASS | 1.452042748003318 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | steady | 0.0008677080040797591 | 6.608298281207681e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7894361147130463 | 0 |

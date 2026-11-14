# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-103200x256-c2 | fit | sklearn | cold | 0.04201729199849069 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | cold | 0.0010771250235848129 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | sklearn | steady | 0.04177770798560232 | 0.0005349990096874535 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | steady | 0.0010942500084638596 | 2.8041948098689318e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | cold | 0.09054495900636539 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | cold | 0.0019318749546073377 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | steady | 0.04215458297403529 | 0.00010691705392673612 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | steady | 0.0018719590152613819 | 3.075005952268839e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | cold | 0.04122966597788036 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | cold | 0.0010527499835006893 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | steady | 0.03994095895905048 | 0.0001987070427276194 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | steady | 0.0010079170460812747 | 1.354096457362175e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | cold | 0.4494116250425577 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.09174143186433162 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | cold | 0.004109458008315414 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | steady | 0.016699665982741863 | 0.00017020798986777663 | MIXED_CPU_GPU_REPORTED | PASS | 2.3917220260768777 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | steady | 0.0021081670420244336 | 7.345795165747404e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | cold | 0.5540405419887975 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | cold | 0.26791883300757036 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | steady | 0.5503363750176504 | 0.002072666015010327 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | steady | 0.26898849999997765 | 0.0006005000323057175 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | mlxlearn | cold | 0.07770208403235301 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | mlxlearn | cold | 0.007837957993615419 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | mlxlearn | steady | 0.06416104198433459 | 0.00045066699385643005 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | mlxlearn | steady | 0.005212790973018855 | 5.554093513637781e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | sklearn | cold | 0.5673782500089146 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | cold | 0.27547704201424494 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | sklearn | steady | 0.5608785839867778 | 0.0004516240442171693 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | steady | 0.27529983303975314 | 0.00011770805576816201 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | mlxlearn | cold | 0.07019645802211016 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 8.082719071526435 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | cold | 0.004496208042837679 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 61.26874899685111 | 0 |
| svc-5256x256-c3 | fit | mlxlearn | steady | 0.05266579199815169 | 0.0006512919790111482 | MIXED_CPU_GPU_REPORTED | PASS | 10.649770234281522 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | steady | 0.0030228340183384717 | 7.745897164568305e-05 | MIXED_CPU_GPU_REPORTED | PASS | 91.07342029684918 | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | cold | 0.006758541974704713 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | cold | 0.0007403329946100712 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | steady | 0.006413875031284988 | 4.51250234618783e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | steady | 0.000688083004206419 | 3.8790982216596603e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | cold | 0.00497858296148479 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | cold | 0.0007905420497991145 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | steady | 0.0044802919728681445 | 1.6666948795318604e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | steady | 0.00047079200157895684 | 2.8740032576024532e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | cold | 0.007025707978755236 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | cold | 0.0007757919956929982 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | steady | 0.006544541043695062 | 2.9791961424052715e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | steady | 0.0006935840356163681 | 1.4542019926011562e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | cold | 0.20665162499062717 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.03399783562831355 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | cold | 0.0017277500010095537 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.44901866313974226 | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | steady | 0.005108083016239107 | 0.0015371250337921083 | MIXED_CPU_GPU_REPORTED | PASS | 1.2812127412356675 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | steady | 0.001087374985218048 | 3.345799632370472e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.6378517485182774 | 0 |

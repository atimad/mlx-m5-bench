# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-330000x33-c2 | fit | sklearn | cold | 0.06569470802787691 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | cold | 0.0006898329593241215 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | sklearn | steady | 0.06561624997993931 | 0.00028787500923499465 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | steady | 0.000689542037434876 | 7.4160052463412285e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | cold | 0.04192262497963384 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 1.5670466260114113 | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | cold | 0.0010878749890252948 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | steady | 0.01122604199917987 | 0.0002467079902999103 | MIXED_CPU_GPU_REPORTED | PASS | 5.845003072742198 | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | steady | 0.0010216669761575758 | 2.833292819559574e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | cold | 0.06174395798007026 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | cold | 0.0007091659936122596 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | steady | 0.06102616700809449 | 0.00015575002180412412 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | steady | 0.0007135830237530172 | 2.541986759752035e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | cold | 0.045939499977976084 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 1.3440276452654256 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | cold | 0.0011528750183060765 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | steady | 0.011711625033058226 | 0.00017937493976205587 | MIXED_CPU_GPU_REPORTED | PASS | 5.210734363150874 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | steady | 0.0010383750195614994 | 1.1458003427833319e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | cold | 0.33654383395332843 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | cold | 0.15648950001923367 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | steady | 0.33507008297601715 | 0.00011912401532754302 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | steady | 0.1552650419762358 | 0.0004952079616487026 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | mlxlearn | cold | 0.030402292031794786 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 11.069686246068885 | 0 |
| svc-2704x512-c3 | predict | mlxlearn | cold | 0.0025465419748798013 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 61.451765399084024 | 0 |
| svc-2704x512-c3 | fit | mlxlearn | steady | 0.022235499985981733 | 0.0006830829661339521 | MIXED_CPU_GPU_REPORTED | PASS | 15.069149926345732 | 0 |
| svc-2704x512-c3 | predict | mlxlearn | steady | 0.0019249169854447246 | 1.9625003915280104e-05 | MIXED_CPU_GPU_REPORTED | PASS | 80.66064310839049 | 0 |
| svc-2756x512-c3 | fit | sklearn | cold | 0.3493261659750715 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | cold | 0.16398004197981209 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | sklearn | steady | 0.34803904202999547 | 0.00034558301558718085 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | steady | 0.16557220800314099 | 4.2417028453201056e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | mlxlearn | cold | 0.030272167001385242 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 11.53951634711471 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | cold | 0.002818875014781952 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 58.17215772956021 | 0 |
| svc-2756x512-c3 | fit | mlxlearn | steady | 0.022680249996483326 | 5.604204488918185e-05 | MIXED_CPU_GPU_REPORTED | PASS | 15.34546762420875 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | steady | 0.0019352090312168002 | 5.0956965424120426e-05 | MIXED_CPU_GPU_REPORTED | PASS | 85.55779005383943 | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | cold | 0.01578049996169284 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | cold | 0.0004259590059518814 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | steady | 0.014778417011257261 | 1.2415985111147165e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | steady | 0.0003880420117639005 | 4.874949809163809e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | cold | 0.01783020800212398 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.8850429540593707 | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | cold | 0.0015879159909673035 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.2682503409342215 | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | steady | 0.010464749997481704 | 0.00030912505462765694 | MIXED_CPU_GPU_REPORTED | PASS | 1.4122092754068298 | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | steady | 0.0008247080259025097 | 4.6042026951909065e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.4705204746119104 | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | cold | 0.017253708967473358 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | cold | 0.0004081249935552478 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | steady | 0.016541540971957147 | 1.8415972590446472e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | steady | 0.00044587498996406794 | 6.958027370274067e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | cold | 0.01672987500205636 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 1.031311289854384 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | cold | 0.0015474999672733247 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.263731826937844 | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | steady | 0.010319166991394013 | 0.0004504169919528067 | MIXED_CPU_GPU_REPORTED | PASS | 1.6029918874025852 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | steady | 0.0011225829948671162 | 6.691698217764497e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.39718665969712785 | 0 |

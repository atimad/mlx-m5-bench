# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-330000x33-c2 | fit | sklearn | cold | 0.06634737498825416 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | cold | 0.0006979999598115683 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | sklearn | steady | 0.06583791703451425 | 9.85830556601286e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | steady | 0.0007148340228013694 | 1.9957020413130522e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | cold | 0.08733974996721372 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | cold | 0.0011823750101029873 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | steady | 0.04149970901198685 | 3.8416008464992046e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | steady | 0.001063833013176918 | 1.4624965842813253e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | cold | 0.06344595801783726 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | cold | 0.0007081250078044832 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | steady | 0.06273720902390778 | 0.0001600819523446262 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | steady | 0.0007000830373726785 | 6.416987162083387e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | cold | 0.043366083002183586 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 1.4630317894895557 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | cold | 0.0011746250092983246 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | steady | 0.011178000015206635 | 0.0003081670147366822 | MIXED_CPU_GPU_REPORTED | PASS | 5.612561186129863 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | steady | 0.0009977089939638972 | 2.3626023903489113e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | cold | 0.3389689169707708 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | cold | 0.15526279096957296 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | steady | 0.3385672079748474 | 0.0002649999805726111 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | steady | 0.15506879199529067 | 0.0002922910498455167 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | mlxlearn | cold | 0.03181495802709833 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | mlxlearn | cold | 0.0035689580254256725 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | mlxlearn | steady | 0.024695417028851807 | 0.00013458298053592443 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | mlxlearn | steady | 0.002699957985896617 | 5.070905899628997e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | sklearn | cold | 0.35455516702495515 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | cold | 0.16359033301705495 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | sklearn | steady | 0.34780941699864343 | 0.00023966602748259902 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | steady | 0.1617365840356797 | 3.412499791011214e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | mlxlearn | cold | 0.03006720799021423 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 11.792088149333647 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | cold | 0.006111916969530284 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 26.765797675688525 | 0 |
| svc-2756x512-c3 | fit | mlxlearn | steady | 0.02267154201399535 | 0.00029437500052154064 | MIXED_CPU_GPU_REPORTED | PASS | 15.34123337459523 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | steady | 0.001966667012311518 | 6.7290966399014e-05 | MIXED_CPU_GPU_REPORTED | PASS | 82.23892658146684 | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | cold | 0.015390457992907614 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | cold | 0.0004775420529767871 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | steady | 0.014719082973897457 | 1.1458003427833319e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | steady | 0.00038045900873839855 | 1.6915961168706417e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | cold | 0.011332249967381358 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | cold | 0.0004442919744178653 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | steady | 0.010475250019226223 | 8.041597902774811e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | steady | 0.0003557090531103313 | 2.6749970857053995e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | cold | 0.01739866699790582 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | cold | 0.0004354999982751906 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | steady | 0.01655154098989442 | 0.0001163340057246387 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | steady | 0.00040208298014476895 | 4.87396027892828e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | cold | 0.017177750007249415 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 1.012860647672901 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | cold | 0.0023733749985694885 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.1834939689419838 | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | steady | 0.010702625033445656 | 0.00031254207715392113 | MIXED_CPU_GPU_REPORTED | PASS | 1.5464935880843182 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | steady | 0.001152042008470744 | 9.200000204145908e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3490176375412788 | 0 |

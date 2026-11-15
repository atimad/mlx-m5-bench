# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k5-t1536-q8 | fit | sklearn | cold | 0.00023033301113173366 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | cold | 0.0007983749965205789 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | steady | 0.00023262499598786235 | 7.874972652643919e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | fit | mlxlearn | cold | 0.00031329196644946933 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | cold | 0.005760542000643909 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.13859372892886418 | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | steady | 0.0006497499998658895 | 0.00016316695837303996 | GPU_REPORTED_UNVERIFIED | PASS | 0.3580223101744931 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | sklearn | cold | 0.00022912496933713555 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | cold | 0.0009304589475505054 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | steady | 0.00023537501692771912 | 4.667032044380903e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | mlxlearn | cold | 0.00034979102201759815 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | cold | 0.07425250002415851 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.012531011713380356 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | steady | 0.0007566669955849648 | 0.00010333402315154672 | GPU_REPORTED_UNVERIFIED | PASS | 0.31106816909036084 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | sklearn | cold | 0.00027129199588671327 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | cold | 0.0008950409828685224 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | steady | 0.00023608299670740962 | 3.6659766919910908e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | mlxlearn | cold | 0.0003558750031515956 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | cold | 0.0054742079810239375 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.16350145737449806 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | steady | 0.0007730000070296228 | 5.724997026845813e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.30541137718044353 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | sklearn | cold | 0.0002191669773310423 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | cold | 0.0008597910054959357 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | steady | 0.0002578329876996577 | 6.999995093792677e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | mlxlearn | cold | 0.0003528340021148324 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | cold | 0.07118883304065093 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.012077610613520936 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | steady | 0.0008353330194950104 | 4.39169816672802e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.30865892007420853 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | sklearn | cold | 0.00023345905356109142 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | cold | 0.0008552499930374324 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | steady | 0.00025587499840185046 | 1.7909915186464787e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | mlxlearn | cold | 0.0003505410277284682 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | cold | 0.005951167026069015 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.14371130725973916 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | steady | 0.0007624160498380661 | 8.095894008874893e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3356107186570865 | 0 |

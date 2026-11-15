# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k5-t1536-q8 | fit | sklearn | cold | 0.00027591700199991465 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | cold | 0.0011116249952465296 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | steady | 0.00023787497775629163 | 1.2582982890307903e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | fit | mlxlearn | cold | 0.00036587496288120747 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | cold | 0.005342707969248295 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.20806396337678407 | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | steady | 0.0006788749597035348 | 4.966708365827799e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.35039586356252084 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | sklearn | cold | 0.00022774998797103763 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | cold | 0.0008386659901589155 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | steady | 0.00024170795222744346 | 9.541923645883799e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | mlxlearn | cold | 0.00035129202296957374 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | cold | 0.005183542030863464 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.16179399822850712 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | steady | 0.0007641249685548246 | 8.683401392772794e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3163199243241341 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | sklearn | cold | 0.0002359579666517675 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | cold | 0.0008445410057902336 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | steady | 0.00023733300622552633 | 7.874972652643919e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | mlxlearn | cold | 0.0003326250007376075 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | cold | 0.005932500003837049 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.14235836582283987 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | steady | 0.0006665420369245112 | 5.7124008890241385e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3560660739727738 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | sklearn | cold | 0.00022633298067376018 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | cold | 0.0009036249830387533 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | steady | 0.0002469589817337692 | 3.2919924706220627e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | mlxlearn | cold | 0.0003553330316208303 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | cold | 0.005854459013789892 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.15434816110426408 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | steady | 0.0006430000066757202 | 4.962499951943755e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.38407306247248035 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | sklearn | cold | 0.00022316700778901577 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | cold | 0.000952333037275821 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | steady | 0.0002597909769974649 | 5.208014044910669e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | mlxlearn | cold | 0.00031345797469839454 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | cold | 0.005833374976646155 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.16325592664426247 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | steady | 0.0007502079824917018 | 5.4540985729545355e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.34629193911614836 | 0 |

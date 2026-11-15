# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.00024304201360791922 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0013809580123052 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.00019070797134190798 | 1.129199517890811e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0008089999901130795 | 2.9540969990193844e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.00037587498081848025 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.006963790976442397 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.1983054943746592 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00024024996673688293 | 2.8709066100418568e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0008452920010313392 | 0.0002169579965993762 | GPU_REPORTED_UNVERIFIED | PASS | 0.9570657111696552 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.000283417000900954 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0019240410183556378 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00020054104970768094 | 2.6374065782874823e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0009326669969595969 | 5.554204108193517e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.0003879580181092024 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.09928791702259332 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.019378400474629912 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.00020474998746067286 | 9.917013812810183e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0008576670079492033 | 0.00031599897192791104 | GPU_REPORTED_UNVERIFIED | PASS | 1.0874465128252149 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00023937498917803168 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015409999759867787 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.00019704102305695415 | 9.20804450288415e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009737089858390391 | 3.604101948440075e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.00038745900383219123 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.07180420798249543 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.02146113743587906 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.0002014580531977117 | 1.4083052519708872e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0008027080330066383 | 0.00043454195838421583 | GPU_REPORTED_UNVERIFIED | PASS | 1.2130300754458585 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.00025154202012345195 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.001808041997719556 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.00019166601123288274 | 7.499009370803833e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.001060499984305352 | 3.412499791011214e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.00039020803524181247 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.07133058301405981 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.02534736043532936 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.00024741701781749725 | 2.624996704980731e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0008999580168165267 | 0.0003845830215141177 | GPU_REPORTED_UNVERIFIED | PASS | 1.178388285329931 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.00024283298989757895 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.00168299995129928 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.0001942919916473329 | 1.4792021829634905e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0011066669831052423 | 3.091699909418821e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.00045420799870043993 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.007626541017089039 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.22067670619329616 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.00020220904843881726 | 1.4418037608265877e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0004444579826667905 | 6.787496386095881e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.4899248663847464 | 0 |

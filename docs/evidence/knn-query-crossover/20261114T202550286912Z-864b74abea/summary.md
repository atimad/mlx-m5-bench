# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00024891598150134087 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0007899579941295087 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.0001801659818738699 | 1.1791009455919266e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00025104195810854435 | 2.424995182082057e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0003720420063473284 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.00017787504475563765 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00019562500528991222 | 6.292015314102173e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.00012858398258686066 | 3.708992153406143e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | cold | 0.00024608400417491794 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | cold | 0.0007922910153865814 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | steady | 0.00017270899843424559 | 5.876005161553621e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | steady | 0.00023812497965991497 | 1.0624993592500687e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | cold | 0.00037579197669401765 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | cold | 0.005936041998211294 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.1334712617642062 | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | steady | 0.00020341703202575445 | 2.1583051420748234e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | steady | 0.00043179100612178445 | 0.00015837501268833876 | GPU_REPORTED_UNVERIFIED | PASS | 0.5514820278418514 | 0 |

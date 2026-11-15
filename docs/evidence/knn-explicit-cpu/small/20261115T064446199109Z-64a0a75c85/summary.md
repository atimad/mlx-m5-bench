# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q1 | fit | sklearn | cold | 0.00040433299727737904 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | cold | 0.0009600000339560211 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | sklearn | steady | 0.00019950000569224358 | 2.520898124203086e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | steady | 0.00028137501794844866 | 5.8458943385630846e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | cold | 0.000370624999050051 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | cold | 0.0001403330243192613 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | steady | 0.00019537500338628888 | 8.040980901569128e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | steady | 9.1959023848176e-05 | 7.542024832218885e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | cold | 0.0002481670235283673 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | cold | 0.0008418750367127359 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | steady | 0.00018716702470555902 | 1.0375049896538258e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | steady | 0.0002532500075176358 | 2.2625026758760214e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | cold | 0.0003869999782182276 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | cold | 0.00017587497131899 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | steady | 0.00019624998094514012 | 1.3834040146321058e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | steady | 9.933300316333771e-05 | 6.541959010064602e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | cold | 0.0002502080169506371 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | cold | 0.0008727919775992632 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | steady | 0.00019116699695587158 | 1.5666999388486147e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | steady | 0.0002555829705670476 | 2.424995182082057e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | cold | 0.0005672909901477396 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | cold | 0.0001727920025587082 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | steady | 0.00021129101514816284 | 1.708301715552807e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | steady | 0.00011620903387665749 | 8.126022294163704e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00025158299831673503 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0008453329792246222 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.00019170797895640135 | 1.308403443545103e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.0002584169851616025 | 1.912500010803342e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.00039833300979807973 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.00019816699204966426 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00021008303156122565 | 2.1291023585945368e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.00012687500566244125 | 7.3750270530581474e-06 | CPU_FALLBACK | PASS | ineligible | 0 |

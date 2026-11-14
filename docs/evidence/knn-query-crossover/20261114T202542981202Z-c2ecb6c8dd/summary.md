# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00024037499679252505 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0007728749769739807 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.00018274999456480145 | 1.0374991688877344e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00026533298660069704 | 2.0915991626679897e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0036806659772992134 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.16809925000416115 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.004597730072887588 | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.0002269170363433659 | 1.9332976080477238e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.0006782920099794865 | 4.541699308902025e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.39117811016043297 | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | cold | 0.00024520797887817025 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | cold | 0.0008219580049626529 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | sklearn | steady | 0.00016537500778213143 | 2.874992787837982e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | sklearn | steady | 0.0002277909661643207 | 4.917033948004246e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | cold | 0.0035774169955402613 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | cold | 0.00396716600516811 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.207190221909512 | 0 |
| knn-4096x32-c2-k5-q5 | fit | mlxlearn | steady | 0.00020904099801555276 | 7.2909751906991005e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q5 | predict | mlxlearn | steady | 0.0006434170063585043 | 0.0002197919529862702 | GPU_REPORTED_UNVERIFIED | PASS | 0.35403317586137645 | 0 |

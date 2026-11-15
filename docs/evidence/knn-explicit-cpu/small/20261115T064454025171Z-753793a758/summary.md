# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q1 | fit | sklearn | cold | 0.00026308302767574787 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | cold | 0.0008281670161522925 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | sklearn | steady | 0.00017662503523752093 | 7.708033081144094e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | steady | 0.00023366697132587433 | 1.4582998119294643e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | cold | 0.004764249955769628 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | cold | 0.10316254099598154 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.008027788072654703 | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | steady | 0.00023045798297971487 | 2.079096157103777e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | steady | 0.0003525000065565109 | 0.00010899995686486363 | GPU_REPORTED_UNVERIFIED | PASS | 0.6628850127082596 | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | cold | 0.0002987500047311187 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | cold | 0.0008585419855080545 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | steady | 0.0001829169923439622 | 1.4207966160029173e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | steady | 0.0002737090107984841 | 4.204304423183203e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | cold | 0.004300582979340106 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | cold | 0.07360983401304111 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.01166341423016863 | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | steady | 0.0002138750278390944 | 1.3624958228319883e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | steady | 0.00038312497781589627 | 0.00010845798533409834 | GPU_REPORTED_UNVERIFIED | PASS | 0.7144118150657616 | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | cold | 0.00039770896546542645 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | cold | 0.0010180000099353492 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | steady | 0.00017716700676828623 | 8.957984391599894e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | steady | 0.00024099997244775295 | 1.4624965842813253e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | cold | 0.00440833397442475 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | cold | 0.07875333400443196 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.012926436992217495 | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | steady | 0.00023383402731269598 | 2.1167041268199682e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | steady | 0.0005055409856140614 | 0.0001567500294186175 | GPU_REPORTED_UNVERIFIED | PASS | 0.4767169810277983 | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.0002863749978132546 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.00091608299408108 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.00017433299217373133 | 8.209026418626308e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00024158303858712316 | 1.3582990504801273e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0035289579536765814 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.0022922499920241535 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3996435804421751 | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00022966699907556176 | 2.68329749815166e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.0002987500047311187 | 2.475001383572817e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8086461414604931 | 0 |

# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q1 | fit | sklearn | cold | 0.0002678749733604491 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | cold | 0.0008561249705962837 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | sklearn | steady | 0.00018708297284319997 | 1.1666968930512667e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | steady | 0.00023770902771502733 | 1.9793049432337284e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | cold | 0.001316834008321166 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | cold | 0.0011511659831739962 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | steady | 0.00023787503596395254 | 2.6500027161091566e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | steady | 0.00034249998861923814 | 3.4791999496519566e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | cold | 0.0003012089873664081 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | cold | 0.0008921250118874013 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | steady | 0.00017262500477954745 | 6.999995093792677e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | steady | 0.00023762497585266829 | 1.3791956007480621e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | cold | 0.001511832990217954 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | cold | 0.0022074999869801104 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | steady | 0.00028216600185260177 | 4.412501584738493e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | steady | 0.0005450830212794244 | 9.420892456546426e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | cold | 0.00024404202122241259 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | cold | 0.0008445410057902336 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | steady | 0.0001871669664978981 | 1.0707997716963291e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | steady | 0.0002704579965211451 | 3.204098902642727e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | cold | 0.0016327910125255585 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | cold | 0.0017847499693743885 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | steady | 0.00028304202714934945 | 5.46250375919044e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | steady | 0.0006273749750107527 | 0.000106374965980649 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.0002906250301748514 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.0009250410366803408 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.00018091598758473992 | 9.373994544148445e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.00025329197524115443 | 2.49580480158329e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.00116395897930488 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.002377042022999376 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00025441701291128993 | 1.675001112744212e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.0007948330021463335 | 7.349898805841804e-05 | CPU_FALLBACK | PASS | ineligible | 0 |

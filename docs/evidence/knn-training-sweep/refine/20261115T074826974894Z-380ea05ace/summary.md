# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k5-t1536-q8 | fit | sklearn | cold | 0.00025762501172721386 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | cold | 0.0008769580163061619 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | steady | 0.000226958014536649 | 4.582980182021856e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | fit | mlxlearn | cold | 0.0038894169847480953 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | cold | 0.0023287080111913383 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3765856483902939 | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | steady | 0.0006445830222219229 | 4.137400537729263e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3521005157013115 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | sklearn | cold | 0.00023558299290016294 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | cold | 0.0008421249804086983 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | steady | 0.00023016700288280845 | 4.04199818149209e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | mlxlearn | cold | 0.0038795829750597477 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | cold | 0.0023824170348234475 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.35347504995954887 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | steady | 0.0006856250111013651 | 0.0001491669681854546 | GPU_REPORTED_UNVERIFIED | PASS | 0.3357039185502814 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | sklearn | cold | 0.00021837500389665365 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | cold | 0.0008667500223964453 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | steady | 0.0002673339913599193 | 2.2167980205267668e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | mlxlearn | cold | 0.0033159999875351787 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | cold | 0.0018321250099688768 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.47308454263782423 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | steady | 0.0006745419814251363 | 8.5124047473073e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.39631927844596165 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | sklearn | cold | 0.0002709999680519104 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | cold | 0.0008935000514611602 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | steady | 0.00024804199347272515 | 3.5830307751893997e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | mlxlearn | cold | 0.004042915999889374 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | cold | 0.002408707980066538 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.37094577626486636 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | steady | 0.000657666998449713 | 5.5541982874274254e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3771543867297929 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | sklearn | cold | 0.0002334170276299119 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | cold | 0.000938582990784198 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | steady | 0.00026304100174456835 | 5.583977326750755e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | mlxlearn | cold | 0.0037419580039568245 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | cold | 0.0023779580369591713 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.39470124207255436 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | steady | 0.0006687500281259418 | 4.758400609716773e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.393332322514731 | 0 |

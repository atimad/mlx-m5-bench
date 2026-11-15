# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k5-t1536-q8 | fit | sklearn | cold | 0.00021725002443417907 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | cold | 0.0008429170120507479 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | sklearn | steady | 0.0002354159951210022 | 1.312600215896964e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | fit | mlxlearn | cold | 0.003920834045857191 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | cold | 0.0023076659999787807 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3652682026161925 | 0 |
| knn-16384x32-c2-k5-t1536-q8 | predict | mlxlearn | steady | 0.000652582966722548 | 1.816597068682313e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.360744927657745 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | sklearn | cold | 0.00023187499027699232 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | cold | 0.0008294169674627483 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | sklearn | steady | 0.0002330829738639295 | 3.832974471151829e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | fit | mlxlearn | cold | 0.003920416987966746 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | cold | 0.0023693330003879964 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3500634850934524 | 0 |
| knn-16384x32-c2-k5-t1536-q12 | predict | mlxlearn | steady | 0.0006930829840712249 | 6.679096259176731e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.33629879714371497 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | sklearn | cold | 0.00022208300651982427 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | cold | 0.000922334031201899 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | sklearn | steady | 0.00024229101836681366 | 8.750997949391603e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | fit | mlxlearn | cold | 0.0037931249826215208 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | cold | 0.002345957967918366 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.39315880498076944 | 0 |
| knn-16384x32-c2-k5-t1536-q16 | predict | mlxlearn | steady | 0.0006346250302158296 | 0.0002122079604305327 | GPU_REPORTED_UNVERIFIED | PASS | 0.3817861049136573 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | sklearn | cold | 0.00023224996402859688 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | cold | 0.0008432920440100133 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | sklearn | steady | 0.0002509579644538462 | 7.1249669417738914e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | fit | mlxlearn | cold | 0.0037709579919464886 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | cold | 0.002319500024896115 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.363566300909086 | 0 |
| knn-16384x32-c2-k5-t1536-q24 | predict | mlxlearn | steady | 0.0006420420249924064 | 3.100099274888635e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.3908746697022121 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | sklearn | cold | 0.00022124999668449163 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | cold | 0.0009421659633517265 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | sklearn | steady | 0.0002641670289449394 | 1.0583025868982077e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | fit | mlxlearn | cold | 0.003958291024900973 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | cold | 0.0022090839920565486 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.42649621596081383 | 0 |
| knn-16384x32-c2-k5-t1536-q32 | predict | mlxlearn | steady | 0.0006609999691136181 | 9.779201354831457e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.39964756624600106 | 0 |

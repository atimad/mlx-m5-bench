# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.0002442499971948564 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0013944160309620202 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.00018974998965859413 | 1.0791001841425896e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0008014169870875776 | 2.4499953724443913e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.0003921660245396197 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.006400833022780716 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.2178491496340024 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.000202000024728477 | 1.4915945939719677e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0009097910369746387 | 0.00023874995531514287 | GPU_REPORTED_UNVERIFIED | PASS | 0.8808802840623257 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.00025033397832885385 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0014862499665468931 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00019237498054280877 | 6.542017217725515e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008771250140853226 | 1.6667007002979517e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.00033662503119558096 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.006321333989035338 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.23511650691529132 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.00020670902449637651 | 1.7665966879576445e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0009683750104159117 | 0.00021662499057129025 | GPU_REPORTED_UNVERIFIED | PASS | 0.9057699802771679 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.0002731670392677188 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015717079513706267 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.00018512504175305367 | 8.832954335957766e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009381670388393104 | 1.870904816314578e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.00036345800617709756 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.0066093329805880785 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.23780129643744788 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.00019316701218485832 | 9.375042282044888e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.000563582987524569 | 8.65840120241046e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.66464754899723 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.00024129200028255582 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0016137079801410437 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.00019366602646186948 | 1.1582043953239918e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.0010540839866735041 | 4.112400347366929e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.0003469169605523348 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.006369625043589622 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.2533442658080912 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.0002014170167967677 | 1.2417032849043608e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0005903330165892839 | 0.00022604101104661822 | GPU_REPORTED_UNVERIFIED | PASS | 1.7855751873130763 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.00026954198256134987 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0017132919747382402 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.00018287496641278267 | 5.917041562497616e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010673750075511634 | 2.1874962840229273e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.00041329197119921446 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.0063342920038849115 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.27047884336362354 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.00019633397459983826 | 7.166003342717886e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0005248329835012555 | 0.00015804101713001728 | GPU_REPORTED_UNVERIFIED | PASS | 2.0337422401132494 | 0 |

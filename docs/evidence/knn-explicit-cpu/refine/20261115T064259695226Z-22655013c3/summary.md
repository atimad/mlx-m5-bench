# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.0002365419641137123 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.001365375006571412 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.000179541006218642 | 5.581998266279697e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0007644589641131461 | 8.957984391599894e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.0037899159942753613 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.0029902499518357217 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.45660898873460565 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00019112502923235297 | 7.708033081144094e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0007163750124163926 | 0.00010329193901270628 | GPU_REPORTED_UNVERIFIED | PASS | 1.0671212016937364 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.00024279096396639943 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0015202909708023071 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00017345900414511561 | 6.126007065176964e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008322079665958881 | 1.3373966794461012e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.003940791997592896 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.00301929097622633 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5035258220466209 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.00019650004105642438 | 1.0417017620056868e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0004240840207785368 | 6.9500005338341e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.9623657714528224 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.0002423339756205678 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015527079813182354 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.00017862499225884676 | 4.916975740343332e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009102920303121209 | 8.04202863946557e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.004061957995872945 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.0029455830226652324 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5271309514519502 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.00019904098007827997 | 7.291033398360014e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0008700420148670673 | 5.791598232463002e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.0462621514332309 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.00024120800662785769 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0016050830017775297 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.00018495897529646754 | 6.416055839508772e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.001008792023640126 | 2.7959002181887627e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.004132916976232082 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.003149040974676609 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5097053403512363 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.0001935840118676424 | 6.626010872423649e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0006823329604230821 | 0.00012920796871185303 | GPU_REPORTED_UNVERIFIED | PASS | 1.4784453956534978 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.0002597499988041818 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0016876250156201422 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.00017787498654797673 | 5.915993824601173e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010433749994263053 | 2.862501423805952e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.004111958027351648 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.0030884169973433018 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5464369018406064 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.00021762499818578362 | 2.1209008991718292e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0004356250283308327 | 7.216702215373516e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.395121794136035 | 0 |

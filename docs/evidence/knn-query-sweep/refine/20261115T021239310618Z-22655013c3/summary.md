# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.00024391704937443137 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0014676250284537673 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.00021283305250108242 | 8.70897201821208e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0011956249945797026 | 7.850001566112041e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.0037562500219792128 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.002941249986179173 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.4989800375180906 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00025287497555837035 | 2.441596006974578e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0007682919967919588 | 4.1416031308472157e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.5562117002026494 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.0002585829934105277 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0014873340260237455 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00018974998965859413 | 5.750043783336878e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008905840222723782 | 4.350004019215703e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.0038093329640105367 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.00299595802789554 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.4964468834927231 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.00020879099611192942 | 1.5623983927071095e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0008313329890370369 | 0.0004610830219462514 | GPU_REPORTED_UNVERIFIED | PASS | 1.0712723229039351 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00024816696532070637 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015558329760096967 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.0001877500326372683 | 6.417045369744301e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009494160185568035 | 2.5833025574684143e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.003986417024862021 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.0031004169723019004 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5018141075568202 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.00022062496282160282 | 9.999959729611874e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0008927910239435732 | 0.0004545010160654783 | GPU_REPORTED_UNVERIFIED | PASS | 1.0634246907670626 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.00026287505170330405 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.001708333962596953 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.0001800830359570682 | 1.0041054338216782e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.0010075830505229533 | 2.191605744883418e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.003900374984368682 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.0030770410085096955 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5551872587568636 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.000203833042178303 | 1.3041018974035978e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0009115830180235207 | 0.00034358398988842964 | GPU_REPORTED_UNVERIFIED | PASS | 1.1053113436750701 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.00025054102297872305 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0016739999991841614 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.00018862501019611955 | 5.667039658874273e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0011069580214098096 | 2.5040993932634592e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.003996499988716096 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.0031004170305095613 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5399273654838089 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.0002103339647874236 | 8.12596408650279e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.00043579202610999346 | 7.425103103742003e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.5401061861797687 | 0 |

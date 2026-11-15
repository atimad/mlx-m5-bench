# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.00024158402811735868 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0014063749695196748 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.00018237496260553598 | 6.666930858045816e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0007696250104345381 | 2.458400558680296e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.0009333750349469483 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.035072917002253234 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00033949996577575803 | 7.958034984767437e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.030023417028132826 | 9.070901433005929e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.0002359579666517675 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0014432920143008232 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.0001757919671945274 | 6.041955202817917e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008523330325260758 | 1.9874947611242533e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.0012750420137308538 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.04342075000749901 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.00040679197991266847 | 2.925097942352295e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.038228124962188303 | 0.0005219170707277954 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00024683302035555243 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.001561917015351355 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.00018637499306350946 | 9.790994226932526e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009300420060753822 | 2.2833992261439562e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.0010161660029552877 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.044195541995577514 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.0003451249795034528 | 9.207986295223236e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.03815433301497251 | 0.00015054101822897792 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.00023158302064985037 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0016814580303616822 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.00019412499386817217 | 7.082941010594368e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.0010350000229664147 | 1.4125020243227482e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.0009898330317810178 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.04953600000590086 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.0003339999821037054 | 1.1457945220172405e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.04176733299391344 | 0.00012479204451665282 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.0002466249861754477 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.001686000032350421 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.00018620904302224517 | 1.1084077414125204e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010520420037209988 | 2.5250017642974854e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.0010327500058338046 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.05360529205063358 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.0003429580247029662 | 5.833047907799482e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.04538945900276303 | 0.00021283398382365704 | CPU_FALLBACK | PASS | ineligible | 0 |

# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.00024287501582875848 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.001421833992935717 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.000171584018971771 | 3.167020622640848e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0007361249881796539 | 7.4169947765767574e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.00038554100319743156 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.006421708036214113 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.22141056318934618 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00018933298997581005 | 1.0000017937272787e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.00042333302553743124 | 9.070802479982376e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.7388791891327777 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.00023941602557897568 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0014678750303573906 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00018183403881266713 | 7.376016583293676e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008695420110598207 | 1.0083022061735392e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.0003421669825911522 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.00702837499557063 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.20884984527468495 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.0001984169939532876 | 7.957976777106524e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.00039141601882874966 | 5.316606257110834e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.2215289340016975 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00024737499188631773 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015674580354243517 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.0001870840205810964 | 1.0584015399217606e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009125830256380141 | 2.1498999558389187e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.00036158302100375295 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.009059167001396418 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.17302452148003644 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.0002078750403597951 | 1.875002635642886e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0004669170011766255 | 0.0001163340057246387 | GPU_REPORTED_UNVERIFIED | PASS | 1.9544866075519103 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.000238874985370785 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0016253749490715563 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.0001823339844122529 | 7.958034984767437e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.000992499990388751 | 1.937500201165676e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.00036287499824538827 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.009346125007141382 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.17390896738804648 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.00019975000759586692 | 1.1416967026889324e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.00047749996883794665 | 3.854196984320879e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.0785341469322365 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.00024941598530858755 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0016735829995013773 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.00017608300549909472 | 4.500034265220165e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010243330034427345 | 2.437399234622717e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.0003813750226981938 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.007009082997683436 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.23877346010234313 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.00019812502432614565 | 7.584050763398409e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.000441958021838218 | 7.091602310538292e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.317715603808407 | 0 |

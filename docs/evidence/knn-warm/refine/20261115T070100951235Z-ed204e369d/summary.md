# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.0002489579492248595 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0014668749645352364 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0007739580469205976 | 3.195804310962558e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.004005082999356091 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.0027523330063559115 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5329569354971979 | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.000873749959282577 | 0.00023512501502409577 | GPU_REPORTED_UNVERIFIED | PASS | 0.8857889361804181 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.00024058402050286531 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0014802920049987733 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008425000123679638 | 1.3208016753196716e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.003633041982538998 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.0031117090256884694 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.47571671797662923 | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0008489169995300472 | 6.533297710120678e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.9924409722438875 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.0002567499759607017 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015841670101508498 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0013947919942438602 | 0.0001532500027678907 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.0034175830078311265 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.003010083979461342 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5262866487978646 | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0011661250027827919 | 0.00012020801659673452 | GPU_REPORTED_UNVERIFIED | PASS | 1.1960913203261976 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.0002448749728500843 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0017020420054905117 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.0010327500058338046 | 4.9458001740276814e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.0034762080176733434 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.003157542028930038 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5390401742545495 | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0012227919651195407 | 0.00012391601921990514 | GPU_REPORTED_UNVERIFIED | PASS | 0.8445835720983352 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.0002513749641366303 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0016992919845506549 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010794169502332807 | 2.4499953724443913e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.004116374999284744 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.0030230830307118595 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5621056276944252 | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0010035000159405172 | 5.512498319149017e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.0756521505598695 | 0 |

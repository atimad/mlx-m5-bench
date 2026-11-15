# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.0005073749925941229 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0020100410329177976 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.00020641699666157365 | 2.4875975213944912e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0008903749985620379 | 7.29589955881238e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.0036044170265085995 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.002922374987974763 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.6878107844437779 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00021437503164634109 | 9.66701190918684e-06 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.00038070796290412545 | 6.312498589977622e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.3387348974002498 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.0002452919725328684 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0014971659984439611 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00018287502462044358 | 1.1458061635494232e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008544579613953829 | 9.415962267667055e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.0038671669899486005 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.0030451249913312495 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.49165994916663147 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.00020820897771045566 | 1.604104181751609e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0003904170007444918 | 4.733400419354439e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.1885777508817617 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00024154200218617916 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.001613624976016581 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.00019991694716736674 | 1.4542019926011562e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009565409854985774 | 1.7417012713849545e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.0037434169789776206 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.003075874992646277 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5246068126547386 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.00021229201229289174 | 1.7624988686293364e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0004094169707968831 | 7.18749943189323e-05 | GPU_REPORTED_UNVERIFIED | PASS | 2.336349134811828 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.00031733402283862233 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0017309169634245336 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.00018366699805483222 | 8.875969797372818e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.0010011670528911054 | 1.6332953236997128e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.0034887079964391887 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.003263042017351836 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5304611323482993 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.00021708302665501833 | 1.7458980437368155e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0008732909918762743 | 0.00040179200004786253 | GPU_REPORTED_UNVERIFIED | PASS | 1.1464300699358962 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.0002377500059083104 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0017264579655602574 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.00018937501590698957 | 8.29098280519247e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0011008749715983868 | 2.1915999241173267e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.003888999985065311 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.0031854590051807463 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5419809084820718 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.00021833297796547413 | 1.8832972273230553e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0009085829951800406 | 0.00047387497033923864 | GPU_REPORTED_UNVERIFIED | PASS | 1.2116394181251902 | 0 |

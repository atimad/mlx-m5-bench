# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.00024341698735952377 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.0014075409853830934 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.0007902910001575947 | 1.9291008356958628e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.003933708998374641 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.002944916021078825 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.4779562389244167 | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0008136249962262809 | 7.799995364621282e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.9713209449354273 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.0002655419521033764 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0015515410341322422 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0008858750225044787 | 2.7833040803670883e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.004028624971397221 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.0029848330304957926 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5198083170081126 | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0010944160167127848 | 0.00016199902165681124 | GPU_REPORTED_UNVERIFIED | PASS | 0.8094499796935676 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.0002512499922886491 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0015713750035502017 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009392080246470869 | 2.8083042707294226e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.0036468339967541397 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.003166540991514921 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.4962433796880779 | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0011805409449152648 | 4.804210038855672e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.7955742904914661 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.0002639999729581177 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0016619579982943833 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.0010501249926164746 | 4.21669683419168e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.004032458004076034 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.0030610839603468776 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5429312033983063 | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0009689999860711396 | 0.00023845897521823645 | GPU_REPORTED_UNVERIFIED | PASS | 1.0837203381955252 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.0002608330105431378 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0017266249633394182 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010794170084409416 | 2.6416964828968048e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.0037886250065639615 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.003159790998324752 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.5464364460354608 | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0013087500119581819 | 8.583301678299904e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8247694353988146 | 0 |

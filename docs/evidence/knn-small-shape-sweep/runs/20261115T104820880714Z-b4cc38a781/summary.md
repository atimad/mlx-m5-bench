# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | sklearn | cold | 0.0003149170079268515 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | cold | 0.0011911659967154264 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | sklearn | steady | 0.0005207079811953008 | 5.012494511902332e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | fit | mlxlearn | cold | 0.0009969579987227917 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | cold | 0.023427917039953172 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2047-s33-q128 | predict | mlxlearn | steady | 0.011737374996300787 | 7.983401883393526e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | sklearn | cold | 0.0002384160179644823 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | cold | 0.001074999978300184 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | sklearn | steady | 0.0004486250109039247 | 1.429201802238822e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | fit | mlxlearn | cold | 0.0009835420059971511 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | cold | 0.01672449999023229 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q128 | predict | mlxlearn | steady | 0.011679249990265816 | 4.900002386420965e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | sklearn | cold | 0.00022654200438410044 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | cold | 0.0011082919663749635 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | sklearn | steady | 0.0004826249787583947 | 1.4332996215671301e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | fit | mlxlearn | cold | 0.00114341703010723 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | cold | 0.017372499976772815 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2049-s33-q128 | predict | mlxlearn | steady | 0.011758040986023843 | 5.545897874981165e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | sklearn | cold | 0.000258374959230423 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | cold | 0.0013651250046677887 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | sklearn | steady | 0.0006859999848529696 | 4.2249972466379404e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | fit | mlxlearn | cold | 0.001039166992995888 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | cold | 0.030396250018384308 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q255 | predict | mlxlearn | steady | 0.020810334011912346 | 8.845899719744921e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | sklearn | cold | 0.00023733294801786542 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | cold | 0.001345750002656132 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | sklearn | steady | 0.0006967089721001685 | 2.7499976567924023e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | fit | mlxlearn | cold | 0.0010199579992331564 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | cold | 0.025651165982708335 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q256 | predict | mlxlearn | steady | 0.02027766703395173 | 0.00017929199384525418 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | sklearn | cold | 0.00022379204165190458 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | cold | 0.0013472499558702111 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | sklearn | steady | 0.0007400420145131648 | 4.8666028305888176e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | fit | mlxlearn | cold | 0.0010527499835006893 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | cold | 0.026231875002849847 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-16384x32-c2-k8-t2048-s33-q257 | predict | mlxlearn | steady | 0.02054100000532344 | 5.508400499820709e-05 | CPU_FALLBACK | PASS | ineligible | 0 |

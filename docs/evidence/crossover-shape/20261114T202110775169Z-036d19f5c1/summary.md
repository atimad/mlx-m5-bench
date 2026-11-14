# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-330000x33-c2 | fit | sklearn | cold | 0.06508058297913522 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | cold | 0.0006907919887453318 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | sklearn | steady | 0.06496729201171547 | 0.00028720899717882276 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | predict | sklearn | steady | 0.0007024999940767884 | 7.833994459360838e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | cold | 0.4185772920027375 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.15548044345107376 | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | cold | 0.0011066250153817236 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-330000x33-c2 | fit | mlxlearn | steady | 0.011069124971982092 | 9.950000094249845e-05 | MIXED_CPU_GPU_REPORTED | PASS | 5.869234666349793 | 0 |
| logistic-330000x33-c2 | predict | mlxlearn | steady | 0.0010138750076293945 | 1.533300383016467e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | cold | 0.0623358340235427 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | cold | 0.0007119170040823519 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | sklearn | steady | 0.06104666698956862 | 5.124998278915882e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | predict | sklearn | steady | 0.0007024579681456089 | 1.1239317245781422e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | cold | 0.043883665988687426 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 1.4204791832936652 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | cold | 0.001143332978244871 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-336668x33-c2 | fit | mlxlearn | steady | 0.010863790987059474 | 0.00025183300022035837 | MIXED_CPU_GPU_REPORTED | PASS | 5.619278487802742 | 0 |
| logistic-336668x33-c2 | predict | mlxlearn | steady | 0.0010318749700672925 | 1.0917021427303553e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | cold | 0.3441708749742247 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | cold | 0.1558722920017317 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | sklearn | steady | 0.34206633403664455 | 0.00802858400857076 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | predict | sklearn | steady | 0.1547552080010064 | 0.0005786250112578273 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2704x512-c3 | fit | mlxlearn | cold | 0.02997087495168671 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 11.48351109298714 | 0 |
| svc-2704x512-c3 | predict | mlxlearn | cold | 0.0027674169978126884 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 56.324107326409454 | 0 |
| svc-2704x512-c3 | fit | mlxlearn | steady | 0.021934708987828344 | 5.187594797462225e-05 | MIXED_CPU_GPU_REPORTED | PASS | 15.594751415505831 | 0 |
| svc-2704x512-c3 | predict | mlxlearn | steady | 0.0018824999569915235 | 3.962503978982568e-05 | MIXED_CPU_GPU_REPORTED | PASS | 82.2072836847896 | 0 |
| svc-2756x512-c3 | fit | sklearn | cold | 0.3470516669913195 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | cold | 0.1610815409803763 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | sklearn | steady | 0.34436233300948516 | 0.0007618750096298754 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | predict | sklearn | steady | 0.16157895798096433 | 0.0004921670188196003 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-2756x512-c3 | fit | mlxlearn | cold | 0.030663374986033887 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 11.318117041890842 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | cold | 0.006118500023148954 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 26.32696582020668 | 0 |
| svc-2756x512-c3 | fit | mlxlearn | steady | 0.022640250041149557 | 0.00010583305265754461 | MIXED_CPU_GPU_REPORTED | PASS | 15.210182413338762 | 0 |
| svc-2756x512-c3 | predict | mlxlearn | steady | 0.0019732920336537063 | 2.8207956347614527e-05 | MIXED_CPU_GPU_REPORTED | PASS | 81.8829424258041 | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | cold | 0.015490166959352791 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | cold | 0.0003987089730799198 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | sklearn | steady | 0.014700166007969528 | 8.999899728223681e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | transform | sklearn | steady | 0.00039820896927267313 | 1.8749968148767948e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | cold | 0.08159237500512972 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.18984821753722603 | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | cold | 0.0014095830265432596 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.28285596915683603 | 0 |
| pca-12000x511-c2-p8 | fit | mlxlearn | steady | 0.010575916967354715 | 0.0001444999361410737 | MIXED_CPU_GPU_REPORTED | PASS | 1.389966094982153 | 0 |
| pca-12000x511-c2-p8 | transform | mlxlearn | steady | 0.0008744170190766454 | 0.0001700000138953328 | GPU_REPORTED_UNVERIFIED | PASS | 0.45539938105638456 | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | cold | 0.01747141598025337 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | cold | 0.0004438330070115626 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | sklearn | steady | 0.01657504099421203 | 6.229197606444359e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | transform | sklearn | steady | 0.0004213749780319631 | 2.8082984499633312e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | cold | 0.018483791034668684 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.9452290359420057 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | cold | 0.0015854170196689665 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.27994716942311776 | 0 |
| pca-12000x512-c2-p8 | fit | mlxlearn | steady | 0.010794000001624227 | 0.00026779196923598647 | MIXED_CPU_GPU_REPORTED | PASS | 1.5355791172612472 | 0 |
| pca-12000x512-c2-p8 | transform | mlxlearn | steady | 0.0010197500232607126 | 0.0001325419871136546 | GPU_REPORTED_UNVERIFIED | PASS | 0.4132139920767945 | 0 |

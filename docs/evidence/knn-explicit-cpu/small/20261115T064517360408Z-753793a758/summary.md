# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q1 | fit | sklearn | cold | 0.0002604160108603537 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | cold | 0.0010743749444372952 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | sklearn | steady | 0.00019679201068356633 | 1.895899185910821e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | sklearn | steady | 0.00025462498888373375 | 2.462498378008604e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | cold | 0.003550541994627565 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | cold | 0.0024992499966174364 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.429878942039167 | 0 |
| knn-4096x32-c2-k5-q1 | fit | mlxlearn | steady | 0.0002418750082142651 | 1.8499966245144606e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q1 | predict | mlxlearn | steady | 0.00031637499341741204 | 2.5500019546598196e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8048202107673917 | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | cold | 0.00039183301851153374 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | cold | 0.001000832999125123 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | sklearn | steady | 0.00023245898773893714 | 2.1625019144266844e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | sklearn | steady | 0.0003932499676011503 | 6.024999311193824e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | cold | 0.003895415982697159 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | cold | 0.0024161249748431146 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.41423064185250175 | 0 |
| knn-4096x32-c2-k5-q2 | fit | mlxlearn | steady | 0.00022833299590274692 | 1.025001984089613e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q2 | predict | mlxlearn | steady | 0.0003089170204475522 | 2.9375019948929548e-05 | GPU_REPORTED_UNVERIFIED | PASS | 1.2729954698883807 | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | cold | 0.0002560830325819552 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | cold | 0.0008355000172741711 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | sklearn | steady | 0.0001907089608721435 | 1.145701389759779e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | sklearn | steady | 0.00027249997947365046 | 4.187499871477485e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | cold | 0.003917416033800691 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | cold | 0.00256433297181502 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3258157292587511 | 0 |
| knn-4096x32-c2-k5-q3 | fit | mlxlearn | steady | 0.00024316698545590043 | 1.3499986380338669e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q3 | predict | mlxlearn | steady | 0.0003147500101476908 | 3.674998879432678e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8657663882068971 | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | cold | 0.00025195901980623603 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | cold | 0.000852417026180774 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | sklearn | steady | 0.00019658298697322607 | 2.466695150360465e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | sklearn | steady | 0.0002731669810600579 | 3.9499951526522636e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | cold | 0.0038729170337319374 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | cold | 0.0025957079487852752 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3283948128986095 | 0 |
| knn-4096x32-c2-k5-q4 | fit | mlxlearn | steady | 0.00024170801043510437 | 2.1665997337549925e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q4 | predict | mlxlearn | steady | 0.00033175002317875624 | 6.091600516811013e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8234120933666607 | 0 |

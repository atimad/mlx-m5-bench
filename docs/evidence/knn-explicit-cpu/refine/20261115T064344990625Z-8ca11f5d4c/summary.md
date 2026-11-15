# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-4096x32-c2-k5-q256 | fit | sklearn | cold | 0.000257709005381912 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | cold | 0.001392750011291355 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | sklearn | steady | 0.00018104200717061758 | 6.416987162083387e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | sklearn | steady | 0.000788707984611392 | 2.3582950234413147e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | cold | 0.0003454579855315387 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | cold | 0.006576082960236818 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.21179021306647253 | 0 |
| knn-4096x32-c2-k5-q256 | fit | mlxlearn | steady | 0.00025158299831673503 | 3.079103771597147e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q256 | predict | mlxlearn | steady | 0.0006370419869199395 | 0.0001881259959191084 | GPU_REPORTED_UNVERIFIED | PASS | 1.2380784953041302 | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | cold | 0.0002626669593155384 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | cold | 0.0016464590444229543 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | sklearn | steady | 0.00018900004215538502 | 1.3666925951838493e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | sklearn | steady | 0.0009097079746425152 | 4.6459026634693146e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | cold | 0.00038220902206376195 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | cold | 0.006326542003080249 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.2602462836129644 | 0 |
| knn-4096x32-c2-k5-q288 | fit | mlxlearn | steady | 0.0002155420370399952 | 1.2084085028618574e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q288 | predict | mlxlearn | steady | 0.0008697500452399254 | 0.00041366700315847993 | GPU_REPORTED_UNVERIFIED | PASS | 1.0459418537788834 | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | cold | 0.00023604196030646563 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | cold | 0.0017575829988345504 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | sklearn | steady | 0.00018912501400336623 | 9.041978046298027e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | sklearn | steady | 0.0009625829989090562 | 2.3126020096242428e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | cold | 0.0003488329821266234 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | cold | 0.0062705830205231905 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.2802902047675792 | 0 |
| knn-4096x32-c2-k5-q320 | fit | mlxlearn | steady | 0.00021741597447544336 | 1.6707985196262598e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q320 | predict | mlxlearn | steady | 0.0005117910332046449 | 0.0001420410699211061 | GPU_REPORTED_UNVERIFIED | PASS | 1.8808125513292404 | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | cold | 0.0002453750348649919 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | cold | 0.0016259999829344451 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | sklearn | steady | 0.00019470800179988146 | 7.08398874849081e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | sklearn | steady | 0.00105720799183473 | 4.070799332112074e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | cold | 0.0003845830215141177 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | cold | 0.0057406669948250055 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.28324234525364783 | 0 |
| knn-4096x32-c2-k5-q352 | fit | mlxlearn | steady | 0.00020404101815074682 | 8.540984708815813e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q352 | predict | mlxlearn | steady | 0.0008958340040408075 | 0.0003875409602187574 | GPU_REPORTED_UNVERIFIED | PASS | 1.1801382701103311 | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | cold | 0.0002487919991835952 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | cold | 0.0016979589709080756 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | sklearn | steady | 0.00019175000488758087 | 6.583984941244125e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | sklearn | steady | 0.0010875830193981528 | 1.6166013665497303e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | cold | 0.0003809169866144657 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | cold | 0.00682912499178201 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.2486349236470785 | 0 |
| knn-4096x32-c2-k5-q384 | fit | mlxlearn | steady | 0.0001925410469993949 | 1.3749056961387396e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| knn-4096x32-c2-k5-q384 | predict | mlxlearn | steady | 0.0008587079937569797 | 0.00040637602796778083 | GPU_REPORTED_UNVERIFIED | PASS | 1.2665341737880065 | 0 |

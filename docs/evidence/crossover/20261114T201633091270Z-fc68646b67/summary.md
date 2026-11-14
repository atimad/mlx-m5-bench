# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-103200x256-c2 | fit | sklearn | cold | 0.043990125006530434 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | cold | 0.0011028340086340904 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | sklearn | steady | 0.04153612500522286 | 0.0001413749996572733 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | steady | 0.0010642500128597021 | 3.7499703466892242e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | cold | 0.05094716604799032 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.863445966064008 | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | cold | 0.0018939999863505363 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | steady | 0.015674125053919852 | 0.0003314170753583312 | MIXED_CPU_GPU_REPORTED | PASS | 2.6499804526464033 | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | steady | 0.001906124991364777 | 5.749985575675964e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | cold | 0.042040541011374444 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | cold | 0.0010227910242974758 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | steady | 0.040019750013016164 | 0.00025816698325797915 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | steady | 0.001034832966979593 | 1.0125047992914915e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | cold | 0.04768704203888774 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.8815925503848887 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | cold | 0.003427875053603202 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | steady | 0.01583808398572728 | 0.0004792509716935456 | MIXED_CPU_GPU_REPORTED | PASS | 2.526805013098841 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | steady | 0.0018240829813294113 | 2.700003096833825e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | cold | 0.5636132920044474 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | cold | 0.2739271249738522 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | steady | 0.563490875007119 | 0.0008525000303052366 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | steady | 0.2741767499828711 | 0.00017291598487645388 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | mlxlearn | cold | 0.06381395796779543 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 8.832131871351443 | 0 |
| svc-5160x256-c3 | predict | mlxlearn | cold | 0.004503500007558614 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 60.82538570314124 | 0 |
| svc-5160x256-c3 | fit | mlxlearn | steady | 0.05146712501300499 | 0.00042266701348125935 | MIXED_CPU_GPU_REPORTED | PASS | 10.94855939329685 | 0 |
| svc-5160x256-c3 | predict | mlxlearn | steady | 0.0029255410190671682 | 0.00011345697566866875 | MIXED_CPU_GPU_REPORTED | PASS | 93.7183065272127 | 0 |
| svc-5256x256-c3 | fit | sklearn | cold | 0.5784356669755653 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | cold | 0.27949045901186764 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | sklearn | steady | 0.5784607920213602 | 0.001135542057454586 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | steady | 0.28048970794770867 | 0.00026195793179795146 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | mlxlearn | cold | 0.06459333299426362 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 8.955036691277948 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | cold | 0.004519541980698705 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 61.84043874478171 | 0 |
| svc-5256x256-c3 | fit | mlxlearn | steady | 0.053028583992272615 | 0.00022620701929554343 | MIXED_CPU_GPU_REPORTED | PASS | 10.908471403001336 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | steady | 0.0032200420391745865 | 4.4874963350594044e-05 | MIXED_CPU_GPU_REPORTED | PASS | 87.10746770859188 | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | cold | 0.006743750011082739 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | cold | 0.0006796250236220658 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | steady | 0.006382416991982609 | 1.8041988369077444e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | steady | 0.0006497920257970691 | 2.700003096833825e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | cold | 0.012394083954859525 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.544110402644047 | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | cold | 0.002023415989242494 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.3358800302237885 | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | steady | 0.004921292013023049 | 0.00023108301684260368 | MIXED_CPU_GPU_REPORTED | PASS | 1.2968986548843342 | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | steady | 0.0011697500012814999 | 9.545899229124188e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.5554964950503957 | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | cold | 0.0068685419973917305 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | cold | 0.0007091250154189765 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | steady | 0.006542999995872378 | 6.0166988987475634e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | steady | 0.000683374993968755 | 2.2000051103532314e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | cold | 0.010935083031654358 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.628119784505431 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | cold | 0.0027612080448307097 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.25681694530281335 | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | steady | 0.004375707998406142 | 0.0006265840493142605 | MIXED_CPU_GPU_REPORTED | PASS | 1.4953008743398042 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | steady | 0.0009425419848412275 | 0.00024508300703018904 | GPU_REPORTED_UNVERIFIED | PASS | 0.7250340090514593 | 0 |

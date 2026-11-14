# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| logistic-103200x256-c2 | fit | sklearn | cold | 0.04347595799481496 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | cold | 0.0010384590132161975 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | sklearn | steady | 0.041567208943888545 | 0.00017300096806138754 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | predict | sklearn | steady | 0.001075749984011054 | 2.300000051036477e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | cold | 0.4164806249900721 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.10438890883783927 | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | cold | 0.001984165981411934 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-103200x256-c2 | fit | mlxlearn | steady | 0.015519040985964239 | 0.0001800829777494073 | MIXED_CPU_GPU_REPORTED | PASS | 2.6784650534451737 | 0 |
| logistic-103200x256-c2 | predict | mlxlearn | steady | 0.0018008750048466027 | 7.750000804662704e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | cold | 0.042564833944197744 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | cold | 0.001061249990016222 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | sklearn | steady | 0.040179750008974224 | 0.00027795799542218447 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | predict | sklearn | steady | 0.001051458006259054 | 2.5334011297672987e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | cold | 0.053803915972821414 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.7911103341566997 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | cold | 0.001998124993406236 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-105200x256-c2 | fit | mlxlearn | steady | 0.01586141699226573 | 0.0001629159669391811 | MIXED_CPU_GPU_REPORTED | PASS | 2.533175316465514 | 0 |
| logistic-105200x256-c2 | predict | mlxlearn | steady | 0.0018742079846560955 | 6.665999535471201e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | cold | 0.5587552919751033 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | cold | 0.2708618330070749 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | sklearn | steady | 0.5557617910089903 | 0.001221626007463783 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | predict | sklearn | steady | 0.2703840419999324 | 0.00038420798955485225 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5160x256-c3 | fit | mlxlearn | cold | 0.0631772080087103 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 8.844254274390652 | 0 |
| svc-5160x256-c3 | predict | mlxlearn | cold | 0.004610500007402152 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 58.74890631649638 | 0 |
| svc-5160x256-c3 | fit | mlxlearn | steady | 0.051335499971173704 | 0.0004645419539883733 | MIXED_CPU_GPU_REPORTED | PASS | 10.826071457783907 | 0 |
| svc-5160x256-c3 | predict | mlxlearn | steady | 0.0032269999501295388 | 8.554192027077079e-05 | MIXED_CPU_GPU_REPORTED | PASS | 83.78805273581692 | 0 |
| svc-5256x256-c3 | fit | sklearn | cold | 0.5816115420311689 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | cold | 0.2796872499748133 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | sklearn | steady | 0.5831441659829579 | 0.0004675009986385703 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | predict | sklearn | steady | 0.28002470795763656 | 0.00041245907777920365 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-5256x256-c3 | fit | mlxlearn | cold | 0.06601933302590623 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 8.809715508682016 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | cold | 0.004556625033728778 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 61.380352323162214 | 0 |
| svc-5256x256-c3 | fit | mlxlearn | steady | 0.05301795795094222 | 0.0015326659777201712 | MIXED_CPU_GPU_REPORTED | PASS | 10.99899333208088 | 0 |
| svc-5256x256-c3 | predict | mlxlearn | steady | 0.0033122909953817725 | 0.00011212500976398587 | MIXED_CPU_GPU_REPORTED | PASS | 84.54109507530183 | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | cold | 0.0066766669624485075 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | cold | 0.0007266249740496278 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | sklearn | steady | 0.006483415956608951 | 3.625004319474101e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | transform | sklearn | steady | 0.0006412499933503568 | 3.3292046282440424e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | cold | 0.20961749996058643 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.03185166774579363 | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | cold | 0.0015959999873302877 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.45527880940969884 | 0 |
| pca-41250x256-c2-p8 | fit | mlxlearn | steady | 0.003907834005076438 | 7.458397885784507e-05 | MIXED_CPU_GPU_REPORTED | PASS | 1.6590817184626383 | 0 |
| pca-41250x256-c2-p8 | transform | mlxlearn | steady | 0.0007964579854160547 | 2.1457963157445192e-05 | GPU_REPORTED_UNVERIFIED | PASS | 0.8051272070746831 | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | cold | 0.006780249997973442 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | cold | 0.0006760419928468764 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | sklearn | steady | 0.00647283298894763 | 6.041600136086345e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | transform | sklearn | steady | 0.0006507500074803829 | 1.1208001524209976e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | cold | 0.011315375042613596 | 0.0 | MIXED_CPU_GPU_REPORTED | PASS | 0.599206828977306 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | cold | 0.0018882090225815773 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 0.358033451149696 | 0 |
| pca-42084x256-c2-p8 | fit | mlxlearn | steady | 0.005236207973212004 | 0.00031562504591420293 | MIXED_CPU_GPU_REPORTED | PASS | 1.2361680479580062 | 0 |
| pca-42084x256-c2-p8 | transform | mlxlearn | steady | 0.0012663750094361603 | 0.00011079199612140656 | GPU_REPORTED_UNVERIFIED | PASS | 0.5138683270211738 | 0 |

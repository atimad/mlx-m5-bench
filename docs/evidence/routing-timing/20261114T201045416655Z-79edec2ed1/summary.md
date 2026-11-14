# Stored benchmark results

Ratios require passing correctness and a reported GPU or mixed path. GPU execution is independently unverified. CPU fallback, missing and invalid measurements remain in the tables. Cold denotes the first estimator call after imports.

| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness | CPU/candidate | Failures |
|---|---|---|---|---:|---:|---|---|---:|---:|
| knn-8000x128-c3-k5 | fit | sklearn | cold | 0.000450249994173646 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | cold | 0.013683749944902956 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | sklearn | steady | 0.0004319580039009452 | 7.08969309926033e-07 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | sklearn | steady | 0.013484624971169978 | 0.0005078339600004256 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | cold | 0.003992082958575338 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | cold | 0.011269374983385205 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 1.214242135440283 | 0 |
| knn-8000x128-c3-k5 | fit | mlxlearn | steady | 0.00044949998846277595 | 3.1374976970255375e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-8000x128-c3-k5 | predict | mlxlearn | steady | 0.0023414589813910425 | 0.00022125098621472716 | GPU_REPORTED_UNVERIFIED | PASS | 5.759069485453411 | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | cold | 0.0006950420211069286 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | cold | 0.11317587498342618 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | sklearn | steady | 0.0007209579925984144 | 9.499955922365189e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | sklearn | steady | 0.11310233297990635 | 0.0019388329819776118 | CPU_BASELINE | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | cold | 0.004283957998268306 | 0.0 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | cold | 0.032255833968520164 | 0.0 | GPU_REPORTED_UNVERIFIED | PASS | 3.5086947401167587 | 0 |
| knn-30000x64-c2-k5 | fit | mlxlearn | steady | 0.0006928329821676016 | 3.754097269847989e-05 | UNKNOWN | PASS | ineligible | 0 |
| knn-30000x64-c2-k5 | predict | mlxlearn | steady | 0.01545512501616031 | 0.0006360409897752106 | GPU_REPORTED_UNVERIFIED | PASS | 7.318111814795635 | 0 |
| logistic-2000x32-c2 | fit | sklearn | cold | 0.0014983749715611339 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | cold | 9.074999252334237e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | sklearn | steady | 0.0011183750466443598 | 3.804202424362302e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | sklearn | steady | 5.925004370510578e-05 | 2.1670712158083916e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | cold | 0.05092233303003013 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | cold | 0.00021579198073595762 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | fit | mlxlearn | steady | 0.005016000010073185 | 8.345796959474683e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-2000x32-c2 | predict | mlxlearn | steady | 0.0001318749855272472 | 9.833020158112049e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | cold | 0.04430020897416398 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | cold | 0.0010504999663680792 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | sklearn | steady | 0.04327779199229553 | 0.0006401250138878822 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | sklearn | steady | 0.0010223750141449273 | 4.0584011003375053e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | cold | 0.0940441670245491 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | cold | 0.0018438749830238521 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | fit | mlxlearn | steady | 0.04316125001059845 | 0.00010708399349823594 | CPU_FALLBACK | PASS | ineligible | 0 |
| logistic-100000x256-c2 | predict | mlxlearn | steady | 0.001803541963454336 | 5.491694901138544e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | cold | 0.34570137498667464 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | cold | 0.1643085409887135 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | sklearn | steady | 0.3436664590262808 | 0.0002449160092510283 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | sklearn | steady | 0.16446233302121982 | 0.00026545801665633917 | CPU_BASELINE | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | mlxlearn | cold | 0.0536387920146808 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | mlxlearn | cold | 0.00532308395486325 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | fit | mlxlearn | steady | 0.03992991702398285 | 0.0001782919862307608 | CPU_FALLBACK | PASS | ineligible | 0 |
| svc-4000x256-c3 | predict | mlxlearn | steady | 0.0035777499433606863 | 2.5834073312580585e-05 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | cold | 0.004271624959073961 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | cold | 0.00024120899615809321 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | sklearn | steady | 0.003969457990024239 | 4.758295835927129e-05 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | sklearn | steady | 0.0002042920095846057 | 3.374996595084667e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | cold | 0.0033195840078406036 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | cold | 0.00025174999609589577 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | fit | mlxlearn | steady | 0.00287687499076128 | 0.00010983296670019627 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-12000x256-c2-p8 | transform | mlxlearn | steady | 0.00021316698985174298 | 7.374968845397234e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | cold | 0.0003534999559633434 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | cold | 6.88750296831131e-05 | 0.0 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | sklearn | steady | 0.00017866701819002628 | 5.498994141817093e-06 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | sklearn | steady | 3.966700751334429e-05 | 5.41971530765295e-07 | CPU_BASELINE | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | cold | 0.0005308330291882157 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | cold | 0.00014941697008907795 | 0.0 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | fit | mlxlearn | steady | 0.0002174580004066229 | 8.500006515532732e-06 | CPU_FALLBACK | PASS | ineligible | 0 |
| pca-2000x32-c2-p3 | transform | mlxlearn | steady | 8.249998791143298e-05 | 3.2500247471034527e-06 | CPU_FALLBACK | PASS | ineligible | 0 |

# Metal verification of KNN prediction

**GPU_VERIFIED for a separately instrumented replay of knn-8000x128-c3-k5 prediction.**

The replay matched the standard benchmark's dataset SHA-256, seed 42, 6,000 training rows, 2,000 query rows, 128 features, three classes, five Euclidean neighbors, uniform voting, four requested CPU threads, and forced MLX GPU configuration. It used macOS 27.2.1 build 26B131, Python 3.13.18, MLX 0.32.4, mlx-learn 0.1.2 and scikit-learn 1.9.1. All 2,000 captured labels matched both the completion-traced replay and scikit-learn.

The prediction-only Metal completion trace logged one command buffer with status 4 (completed) on Apple M5 Pro. Metal reported GPU start 419099.788726750 s and end 419099.792097542 s, giving about 3.371 ms of GPU command-buffer elapsed time. The scikit-learn prediction window recorded zero Metal commits. Both windows excluded fit, warmup and synchronization calls. The observer hooks commit in the isolated process and reads Apple's GPUStartTime and GPUEndTime in a completion callback. These timestamps come from the Metal runtime. [Apple Metal GPU timestamps](https://developer.apple.com/documentation/metal/mtlcommandbuffer/gpustarttime)

A separate Apple Metal capture around the same warmed prediction and its final synchronization produced one frame. Its shader artifacts contain the workload-specific symbol prefix `custom_kernel_mlxlearn_neighbor_votes__2000_5_3`. Captured shader presence and completed command-buffer execution are separate observations. Full Xcode is absent, so the capture was inspected through its metadata and shader artifacts. Per-kernel timeline analysis remains open. [Apple Metal capture documentation](https://developer.apple.com/documentation/xcode/capturing-a-metal-workload-programmatically)

The trace confirms GPU compute during the replayed predict operation. Host orchestration still occurs. The original benchmark timings were collected without instrumentation. The 3.371 ms command-buffer interval is evidence of execution and is excluded from benchmark medians. KNN fit, other shapes, cold prediction and automatic routing are outside this verification.

## Reproduce

With the project's locked Apple Silicon environment and Xcode Command Line Tools, run from the repository root.

```sh
mkdir -p results/metal-knn
xcrun clang -dynamiclib -fobjc-arc -framework Foundation -framework Metal \
  scripts/metal_command_trace.m -o results/metal-knn/probe.dylib
MTL_CAPTURE_ENABLED=1 MLXLEARN_FORCE_BACKEND=mlx \
  .venv/bin/python scripts/trace_knn.py results/metal-knn/replay \
  results/metal-knn/probe.dylib > results/metal-knn/replay.json
```

The local capture bundle is `results/metal-knn/prediction-only/predict.gputrace`. The repository evidence contains the compact Metal command-completion traces and the capture stream checksum. The raw capture stays in the ignored results directory.

- [mlx-learn Metal completion trace](mlxlearn.tsv)
- [scikit-learn control trace](sklearn.tsv)
- [Capture metadata and dataset fingerprint](metadata.json)

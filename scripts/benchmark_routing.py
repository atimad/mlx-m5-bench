"""Run matched workloads without tracing in balanced timing blocks."""

import argparse
from pathlib import Path

from mlx_m5_bench.config import Profile, load_profile
from mlx_m5_bench.runner import run

CASE_KEYS = (
    "knn-8000x128-c3-k5",
    "knn-30000x64-c2-k5",
    "logistic-2000x32-c2",
    "logistic-100000x256-c2",
    "svc-4000x256-c3",
    "pca-12000x256-c2-p8",
    "pca-2000x32-c2-p3",
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--config", type=Path, help="Use a custom workload profile")
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    cases = {case.key: case for name in ("standard", "full") for case in load_profile(name).cases}
    base = (
        load_profile("custom", args.config)
        if args.config
        else Profile(cases=[cases[key] for key in CASE_KEYS], repeats=5, warmups=1)
    )
    for block, mode in enumerate(("auto", "forced", "forced", "auto"), start=1):
        profile = Profile(
            **base.model_dump(exclude={"force_mlx", "mlx_device"}),
            force_mlx=mode == "forced",
            mlx_device="auto" if mode == "auto" else "gpu",
        )
        print(run(profile, f"routing-{block}-{mode}", args.output), flush=True)


if __name__ == "__main__":
    main()

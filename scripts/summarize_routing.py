"""Summarize matched, uninstrumented timing blocks using each block's CPU control."""

import argparse
import json
from pathlib import Path
from statistics import median

from mlx_m5_bench.timing import statistics


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runs", nargs=4, type=Path, metavar="RUN")
    args = parser.parse_args()
    blocks = []
    for run in args.runs:
        manifest = json.loads((run / "manifest.json").read_text())
        if manifest["state"] != "complete":
            raise ValueError(f"Incomplete run {run}")
        mode = "forced" if manifest["config"]["force_mlx"] else "auto"
        if mode == "auto" and manifest["config"]["mlx_device"] != "auto":
            raise ValueError(f"Run {run} did not use automatic routing")
        raw = json.loads((run / "measurements.json").read_text())
        if any(row["status"] != "ok" for row in raw):
            raise ValueError(f"Run {run} contains a failed or skipped row")
        blocks.append((mode, manifest, [row for row in raw if row.get("phase") == "steady"]))
    if [mode for mode, _, _ in blocks] != ["auto", "forced", "forced", "auto"]:
        raise ValueError("Expected chronological auto, forced, forced, auto blocks")

    first = blocks[0][1]["config"]
    output = []
    for case in dict.fromkeys(row["case"] for row in blocks[0][2]):
        fingerprints = set()
        operations = ("fit", "transform" if case.startswith("pca-") else "predict")
        for operation in operations:
            by_mode = {"auto": [], "forced": []}
            for mode, manifest, rows in blocks:
                config = manifest["config"]
                if any(
                    config[key] != first[key]
                    for key in ("seed", "threads", "repeats", "warmups", "cases")
                ):
                    raise ValueError("Blocks use different workload settings")
                pair = {}
                for implementation in ("sklearn", "mlxlearn"):
                    selected = [
                        row
                        for row in rows
                        if row["case"] == case and row["implementation"] == implementation
                    ]
                    if len(selected) != config["repeats"] or any(
                        row["status"] != "ok" or row["correctness"]["status"] != "PASS"
                        for row in selected
                    ):
                        raise ValueError(f"Incomplete or invalid timing pair: {case}, {mode}")
                    fingerprints.update(row["dataset_sha256"] for row in selected)
                    pair[implementation] = {
                        "stats_s": statistics(row[f"{operation}_s"] for row in selected),
                        "backends": sorted({row[f"{operation}_backend"] for row in selected}),
                    }
                by_mode[mode].append(
                    {
                        "run_id": manifest["run_id"],
                        **pair,
                        "cpu_over_candidate": (
                            pair["sklearn"]["stats_s"]["median"]
                            / pair["mlxlearn"]["stats_s"]["median"]
                        ),
                    }
                )
            if len(fingerprints) != 1:
                raise ValueError(f"Dataset fingerprint mismatch: {case}")
            result = {"case": case, "operation": operation, "dataset_sha256": fingerprints.pop()}
            for mode, values in by_mode.items():
                result[mode] = {
                    "cpu_ms": 1000
                    * median(item["sklearn"]["stats_s"]["median"] for item in values),
                    "candidate_ms": 1000
                    * median(item["mlxlearn"]["stats_s"]["median"] for item in values),
                    "cpu_over_candidate": median(item["cpu_over_candidate"] for item in values),
                    "blocks": values,
                }
            output.append(result)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()

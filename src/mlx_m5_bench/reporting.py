"""Derived tables and charts. Raw measurements remain immutable."""

import csv
import json
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from .diagnostics import GPU, MIXED, VERIFIED  # noqa: E402
from .runner import write_json  # noqa: E402
from .timing import statistics  # noqa: E402

ELIGIBLE = {GPU, MIXED, VERIFIED}


def aggregate(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[Any, ...], list[dict[str, Any]]] = {}
    for row in rows:
        operation = "transform" if row["algorithm"] == "pca" else "predict"
        for op in ("fit", operation):
            key = (row["case"], row["implementation"], row.get("phase", "unmeasured"), op)
            groups.setdefault(key, []).append(row)
    output = []
    for (case, implementation, phase, op), group in groups.items():
        valid = [row for row in group if row["status"] == "ok" and f"{op}_s" in row]
        statuses = {row.get("correctness", {}).get("status", "INCONCLUSIVE") for row in group}
        correctness = next(
            status
            for status in ("FAIL", "INCONCLUSIVE", "UNSUPPORTED", "PASS")
            if status in statuses
        )
        backends = {row.get(f"{op}_backend", row.get("backend", "UNKNOWN")) for row in group}
        item = {
            "case": case,
            "algorithm": group[0]["algorithm"],
            "samples": group[0]["samples"],
            "features": group[0]["features"],
            "implementation": implementation,
            "phase": phase,
            "operation": op,
            "correctness": correctness,
            "backend": "|".join(sorted(backends)),
            "measured_repeats": len(valid),
            "failure_count": sum(row["status"] != "ok" for row in group),
        }
        if valid:
            item.update(
                {
                    f"time_{key}_s": value
                    for key, value in statistics(row[f"{op}_s"] for row in valid).items()
                }
            )
            item["process_peak_rss_bytes"] = max(
                row["after"]["process_peak_rss_bytes"] for row in valid
            )
            item["mlx_peak_bytes"] = max(row["after"].get("mlx_peak_bytes", 0) for row in valid)
        output.append(item)
    failed_cases = {row["case"] for row in rows if row["status"] != "ok"}
    for item in output:
        item["case_has_failure"] = item["case"] in failed_cases
        if (
            item["implementation"] != "mlxlearn"
            or item["correctness"] != "PASS"
            or item["backend"] not in ELIGIBLE
            or item["failure_count"]
            or item["case_has_failure"]
        ):
            continue
        cpu = next(
            (
                peer
                for peer in output
                if peer["case"] == item["case"]
                and peer["implementation"] == "sklearn"
                and peer["phase"] == item["phase"]
                and peer["operation"] == item["operation"]
                and peer["correctness"] == "PASS"
                and not peer["failure_count"]
            ),
            None,
        )
        if cpu and cpu.get("time_median_s") and item.get("time_median_s"):
            item["cpu_over_candidate_ratio"] = cpu["time_median_s"] / item["time_median_s"]
            item["ratio_evidence"] = item["backend"]
    return output


def csv_file(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("")
        return
    fields = sorted({key for row in rows for key in row})
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(
            {
                key: json.dumps(value) if isinstance(value, (dict, list)) else value
                for key, value in row.items()
            }
            for row in rows
        )


def report(directory: Path) -> list[dict[str, Any]]:
    rows = json.loads((directory / "measurements.json").read_text())
    summary = aggregate(rows)
    write_json(directory / "summary.json", summary)
    csv_file(directory / "summary.csv", summary)
    csv_file(directory / "measurements.csv", rows)
    lines = [
        "# Stored benchmark results",
        "",
        "Ratios require passing correctness and a reported GPU or mixed path. "
        "GPU execution is independently unverified. CPU fallback, missing and invalid "
        "measurements remain in the tables. Cold denotes the first estimator call after imports.",
        "",
        "| Case | Operation | Implementation | Phase | Median s | MAD | Backend | Correctness "
        "| CPU/candidate | Failures |",
        "|---|---|---|---|---:|---:|---|---|---:|---:|",
    ]
    for row in summary:
        if row["phase"] == "warmup":
            continue
        lines.append(
            f"| {row['case']} | {row['operation']} | {row['implementation']} | {row['phase']} | "
            f"{row.get('time_median_s', 'missing')} | {row.get('time_mad_s', 'missing')} | "
            f"{row['backend']} | {row['correctness']} | "
            f"{row.get('cpu_over_candidate_ratio', 'ineligible')} | {row['failure_count']} |"
        )
    (directory / "summary.md").write_text("\n".join(lines) + "\n")
    charts(directory, summary, rows)
    return summary


def charts(directory: Path, summary: list[dict[str, Any]], raw: list[dict[str, Any]]) -> None:
    chart_dir = directory / "charts"
    chart_dir.mkdir(exist_ok=True)
    steady = [row for row in summary if row["phase"] == "steady"]
    labels = sorted({row["case"] for row in steady})
    positions = {case: index for index, case in enumerate(labels)}

    for operation, filename in (("fit", "training_speedup"), ("inference", "prediction_speedup")):
        fig, ax = plt.subplots(figsize=(12, max(3, len(labels) * 0.45)))
        for row in steady:
            if row["implementation"] != "mlxlearn":
                continue
            if (row["operation"] == "fit") != (operation == "fit"):
                continue
            ratio = row.get("cpu_over_candidate_ratio")
            position = positions[row["case"]]
            if ratio is None:
                ax.text(
                    0.03,
                    position,
                    f"{row['correctness']} / {row['backend']} / ineligible",
                    fontsize=7,
                    va="center",
                )
            else:
                ax.barh(position, ratio, color="#187d91", alpha=0.8)
        ax.set_yticks(range(len(labels)), labels, fontsize=7)
        ax.axvline(1, color="black", linewidth=0.8)
        ax.set_xlabel("CPU / candidate median ratio")
        ax.set_title(f"{operation.title()} • reported GPU and mixed paths • unverified")
        save(fig, chart_dir / f"{filename}.png")

    for metric, filename, ylabel in (
        ("time_median_s", "execution_time", "Median seconds"),
        ("process_peak_rss_bytes", "memory", "Process high-water RSS bytes"),
    ):
        fig, ax = plt.subplots(figsize=(13, 5))
        for implementation, color in (("sklearn", "#444444"), ("mlxlearn", "#187d91")):
            group = [
                row
                for row in steady
                if row["implementation"] == implementation
                and row["operation"] == "fit"
                and metric in row
            ]
            ax.scatter(
                [positions[row["case"]] for row in group],
                [row[metric] for row in group],
                label=implementation,
                color=color,
            )
            for row in group:
                if row["correctness"] != "PASS":
                    ax.annotate(
                        row["correctness"],
                        (positions[row["case"]], row[metric]),
                        fontsize=7,
                        color="red",
                    )
        ax.set_xticks(range(len(labels)), labels, rotation=70, ha="right", fontsize=7)
        if any(row.get(metric, 0) > 0 for row in steady):
            ax.set_yscale("log")
        else:
            ax.text(0.5, 0.5, "No measured values", transform=ax.transAxes, ha="center")
        ax.set_ylabel(ylabel)
        ax.legend()
        save(fig, chart_dir / f"{filename}.png")

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    for ax, algorithm in zip(axes.flat, ("logistic", "knn", "svc", "pca"), strict=True):
        group = [
            row for row in steady if row["algorithm"] == algorithm and row["operation"] == "fit"
        ]
        combinations = sorted({(row["implementation"], row["features"]) for row in group})
        for implementation, features in combinations:
            subset = sorted(
                (
                    row
                    for row in group
                    if row["implementation"] == implementation
                    and row["features"] == features
                    and "time_median_s" in row
                ),
                key=lambda row: row["samples"],
            )
            ax.plot(
                [row["samples"] for row in subset],
                [row["time_median_s"] for row in subset],
                "o-",
                label=f"{implementation} d={features}",
            )
        ax.set_title(algorithm)
        ax.set_xlabel("Total samples")
        ax.set_ylabel("Fit seconds")
        if combinations:
            ax.legend(fontsize=7)
    save(fig, chart_dir / "scaling.png")

    fig, ax = plt.subplots(figsize=(12, 4))
    for implementation in ("sklearn", "mlxlearn"):
        group = [
            row
            for row in raw
            if row.get("phase") == "steady"
            and row["implementation"] == implementation
            and "cpu_accuracy" in row.get("correctness", {})
        ]
        key = "cpu_accuracy" if implementation == "sklearn" else "candidate_accuracy"
        ax.scatter(
            [positions[row["case"]] for row in group],
            [row["correctness"][key] for row in group],
            label=implementation,
        )
        for row in group:
            if row["correctness"]["status"] != "PASS":
                ax.annotate(
                    row["correctness"]["status"],
                    (positions[row["case"]], row["correctness"][key]),
                    color="red",
                    fontsize=7,
                )
    ax.set_xticks(range(len(labels)), labels, rotation=70, ha="right", fontsize=7)
    ax.set_ylabel("Test accuracy")
    ax.legend()
    save(fig, chart_dir / "accuracy.png")

    fig, ax = plt.subplots(figsize=(10, 5))
    candidates = [row for row in steady if "cpu_over_candidate_ratio" in row]
    for algorithm in ("logistic", "knn", "svc", "pca"):
        group = [row for row in candidates if row["algorithm"] == algorithm]
        if group:
            ax.scatter(
                [row["samples"] for row in group],
                [row["cpu_over_candidate_ratio"] for row in group],
                label=algorithm + " (fit/inference)",
            )
    ax.axhline(1, color="black", linewidth=0.8)
    ax.set_xlabel("Total samples")
    ax.set_ylabel("CPU / candidate median ratio")
    ax.set_title("Measured crossover samples • GPU/mixed reported, independently unverified")
    if candidates:
        ax.legend(fontsize=8)
    save(fig, chart_dir / "crossover.png")


def save(fig: Any, path: Path) -> None:
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)

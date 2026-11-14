"""Serial isolated workers with timeouts, memory admission and incremental records."""

import hashlib
import json
import os
import signal
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from time import perf_counter
from typing import Any

import numpy as np
from threadpoolctl import threadpool_limits

from .config import Profile
from .correctness import compare
from .datasets import generate
from .estimators import parameters
from .hardware import manifest
from .memory import admission
from .schemas import Measurement


def write_json(path: Path, value: Any) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, default=str, allow_nan=False) + "\n")
    temporary.replace(path)


def read_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for index, line in enumerate(path.read_text().splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = Measurement.model_validate_json(line)
            rows.append(row.model_dump(exclude_unset=True))
        except ValueError:
            rows.append(
                {
                    "status": "error",
                    "backend": "UNKNOWN",
                    "error": f"Invalid or truncated worker record at line {index}",
                }
            )
    return rows


def run(
    profile: Profile,
    name: str,
    root: Path,
    implementations: tuple[str, ...] = ("sklearn", "mlxlearn"),
) -> Path:
    start_run = perf_counter()
    timestamp = datetime.now(UTC)
    digest = hashlib.sha256(profile.model_dump_json().encode()).hexdigest()[:10]
    run_id = timestamp.strftime("%Y%m%dT%H%M%S%fZ") + "-" + digest
    directory = root / run_id
    directory.mkdir(parents=True)
    info = manifest()
    info.update(
        schema_version=1,
        run_id=run_id,
        timestamp=timestamp.isoformat(),
        profile=name,
        config=profile.model_dump(),
        implementations=implementations,
        state="running",
    )
    write_json(directory / "manifest.json", info)
    all_rows: list[dict[str, Any]] = []
    try:
        for case in profile.cases:
            estimate, budget, reason = admission(case)
            common = {
                "case": case.key,
                "algorithm": case.algorithm,
                "samples": case.samples,
                "features": case.features,
                "classes": case.classes,
                "neighbors": case.neighbors,
                "components": case.components,
                "profile": name,
                "estimated_bytes": estimate,
                "memory_budget_bytes": budget,
                "parameters": parameters(case, profile.threads),
            }
            work = directory / "workers" / case.key
            work.mkdir(parents=True)
            case_rows: list[dict[str, Any]] = []
            for implementation in implementations:
                print(
                    f"{case.key} {implementation}" + (f" SKIP {reason}" if reason else ""),
                    flush=True,
                )
                base = {**common, "implementation": implementation}
                if reason:
                    case_rows.append(
                        {
                            **base,
                            "status": "skipped",
                            "reason": reason,
                            "correctness": {"status": "INCONCLUSIVE"},
                        }
                    )
                    continue
                request = work / f"{implementation}-request.json"
                write_json(
                    request,
                    {
                        "case": case.model_dump(),
                        "profile": profile.model_dump(),
                        "implementation": implementation,
                    },
                )
                raw = work / f"{implementation}.jsonl"
                env = os.environ.copy()
                # No inherited tuning overrides may silently change the benchmark.
                for key in list(env):
                    if key.startswith("MLXLEARN_") or key == "MTL_CAPTURE_ENABLED":
                        del env[key]
                for key in (
                    "OMP_NUM_THREADS",
                    "OPENBLAS_NUM_THREADS",
                    "MKL_NUM_THREADS",
                    "VECLIB_MAXIMUM_THREADS",
                    "BLIS_NUM_THREADS",
                ):
                    env[key] = str(profile.threads)
                env["MPLBACKEND"] = "Agg"
                start = perf_counter()
                with (work / f"{implementation}.log").open("w") as log:
                    process = subprocess.Popen(
                        [sys.executable, "-m", "mlx_m5_bench.worker", str(request), str(raw)],
                        stdout=log,
                        stderr=subprocess.STDOUT,
                        env=env,
                        start_new_session=True,
                    )
                    try:
                        process.wait(timeout=profile.timeout_s)
                    except (subprocess.TimeoutExpired, KeyboardInterrupt):
                        os.killpg(process.pid, signal.SIGKILL)
                        process.wait()
                        case_rows.extend({**base, **row} for row in read_rows(raw))
                        case_rows.append(
                            {
                                **base,
                                "status": "timeout",
                                "error": "worker killed at wall-time limit",
                                "correctness": {"status": "INCONCLUSIVE"},
                            }
                        )
                        if sys.exc_info()[0] is KeyboardInterrupt:
                            raise
                        continue
                rows = read_rows(raw)
                case_rows.extend(
                    {**base, **row, "worker_wall_s": perf_counter() - start} for row in rows
                )
                if process.returncode or not rows:
                    case_rows.append(
                        {
                            **base,
                            "status": "error",
                            "error": f"worker exit {process.returncode}",
                            "correctness": {"status": "INCONCLUSIVE"},
                        }
                    )
            with threadpool_limits(limits=profile.threads):
                data = None
                for row in case_rows:
                    row.setdefault("correctness", {"status": "INCONCLUSIVE"})
                    if row["status"] == "unsupported":
                        row["correctness"] = {"status": "UNSUPPORTED"}
                    if row.get("status") != "ok" or row.get("phase") == "warmup":
                        continue
                    index = row["repetition"]
                    cpu_path = work / f"sklearn-{index}.npz"
                    candidate_path = work / f"mlxlearn-{index}.npz"
                    if cpu_path.exists() and candidate_path.exists():
                        if data is None:
                            data = generate(case, profile.seed)
                        with np.load(cpu_path) as cpu, np.load(candidate_path) as candidate:
                            row["correctness"] = compare(
                                case.algorithm, dict(cpu), dict(candidate), data
                            )
                        paired = [
                            peer
                            for peer in case_rows
                            if peer.get("repetition") == index and peer["status"] == "ok"
                        ]
                        if (
                            any(peer.get("dataset_sha256") != data.fingerprint() for peer in paired)
                            or len(paired) != 2
                        ):
                            row["correctness"] = {
                                "status": "FAIL",
                                "reason": "input fingerprints differ",
                            }
                        if any(not peer.get("converged", False) for peer in paired):
                            row["correctness"] = {
                                **row["correctness"],
                                "status": (
                                    "FAIL"
                                    if row["correctness"]["status"] == "FAIL"
                                    else "INCONCLUSIVE"
                                ),
                                "convergence_reason": "at least one estimator did not converge",
                            }
                # Compare repeated candidate outputs to expose nondeterminism.
                steady = [
                    row
                    for row in case_rows
                    if row.get("phase") == "steady"
                    and row["status"] == "ok"
                    and row["implementation"] == "mlxlearn"
                ]
                for row in steady:
                    if steady:
                        with (
                            np.load(work / f"mlxlearn-{steady[0]['repetition']}.npz") as first,
                            np.load(work / f"mlxlearn-{row['repetition']}.npz") as current,
                        ):
                            repeatable = all(
                                np.allclose(first[key], current[key], atol=1e-6, rtol=1e-5)
                                for key in first.files
                            )
                        row["repeatable_within_tolerance"] = repeatable
                        if not repeatable:
                            row["correctness"] = {
                                **row["correctness"],
                                "status": "FAIL",
                                "reason": "candidate repeats differed beyond declared tolerances",
                            }
            all_rows.extend(case_rows)
            write_json(directory / "measurements.json", all_rows)
            # Prediction arrays are transient correctness inputs, never published as datasets.
            for array_file in work.glob("*.npz"):
                array_file.unlink()
        info["state"] = "complete"
    except BaseException:
        info["state"] = "interrupted"
        raise
    finally:
        write_json(directory / "measurements.json", all_rows)
        info["run_wall_s"] = perf_counter() - start_run
        write_json(directory / "manifest.json", info)
    from .reporting import report

    report(directory)
    return directory

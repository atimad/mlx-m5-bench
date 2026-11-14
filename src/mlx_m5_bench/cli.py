"""Command-line entry point."""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def latest(root: Path) -> Path:
    runs = sorted(path.parent for path in root.glob("*/manifest.json"))
    if not runs:
        raise ValueError(f"No saved runs under {root}")
    return runs[-1]


def main() -> None:
    parser = argparse.ArgumentParser(prog="mlx-m5-bench")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("doctor")
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--profile", choices=("quick", "standard", "full"), default="quick")
    run_parser.add_argument("--config", type=Path)
    run_parser.add_argument("--output", type=Path, default=Path("results"))
    run_parser.add_argument("--cpu-only", action="store_true")
    report_parser = sub.add_parser("report")
    report_parser.add_argument("--latest", action="store_true")
    report_parser.add_argument("--run", type=Path)
    report_parser.add_argument("--root", type=Path, default=Path("results"))
    dashboard_parser = sub.add_parser("dashboard")
    dashboard_parser.add_argument("--root", type=Path, default=Path("results"))
    dashboard_parser.add_argument("--port", type=int, default=8501)
    dashboard_parser.add_argument("--headless", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "doctor":
            from .hardware import doctor

            info = doctor()
            print(json.dumps(info, indent=2, default=str))
            sys.exit(0 if info["metal_compute_probe"] else 1)
        if args.command == "run":
            from .config import load_profile
            from .runner import run

            profile = load_profile(args.profile, args.config)
            implementations = ("sklearn",) if args.cpu_only else ("sklearn", "mlxlearn")
            print(run(profile, args.profile, args.output, implementations))
        elif args.command == "report":
            from .reporting import report

            if not args.run and not args.latest:
                parser.error("report requires --run PATH or --latest")
            directory = args.run or latest(args.root)
            report(directory)
            print(directory / "summary.md")
        elif args.command == "dashboard":
            import importlib.util

            if importlib.util.find_spec("streamlit") is None:
                parser.error("Install the dashboard extra with uv sync --extra dashboard")
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "streamlit",
                    "run",
                    str(Path(__file__).with_name("dashboard.py")),
                    "--server.address",
                    "127.0.0.1",
                    "--server.port",
                    str(args.port),
                    "--server.headless",
                    str(args.headless).lower(),
                    "--browser.gatherUsageStats",
                    "false",
                    "--",
                    str(args.root.resolve()),
                ],
                check=True,
            )
    except (ValueError, OSError) as error:
        parser.exit(2, f"{error}\n")


if __name__ == "__main__":
    main()

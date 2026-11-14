"""Export compact, recursively redacted evidence. Preserve raw timings and correctness."""

import json
import re
import sys
from pathlib import Path
from typing import Any

FILES = (
    "manifest.json",
    "measurements.json",
    "summary.json",
    "summary.md",
    "summary.csv",
)


def redact(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: redact(item) for key, item in value.items()}
    if isinstance(value, list):
        return [redact(item) for item in value]
    if isinstance(value, str):
        value = re.sub(r"/Users/[^/\s\"']+", "/Users/REDACTED", value)
        value = re.sub(r"/(?:private/)?var/folders/[^\s\"']+", "<temporary-path>", value)
        value = re.sub(r"/home/[^/\s\"']+", "/home/REDACTED", value)
        return value
    return value


def main() -> None:
    source, target = map(Path, sys.argv[1:])
    target.mkdir(parents=True, exist_ok=False)
    for name in FILES:
        text = (source / name).read_text()
        if name.endswith(".json"):
            text = json.dumps(redact(json.loads(text)), indent=2) + "\n"
        else:
            text = redact(text)
        (target / name).write_text(text)


if __name__ == "__main__":
    main()

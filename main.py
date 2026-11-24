#!/usr/bin/env python3
"""Write the make.fun bounty entry text to <output>/entry.txt (no trailing newline)."""

import os
import sys
from pathlib import Path

TEXT = (
    "My sister, who has never written code, sent make.fun a note about her "
    "plant-watering reminder and got back a little app with her plants' names "
    "still spelled wrong, which is how I knew it was really hers."
)

FILENAME = "entry.txt"


def output_dir() -> Path:
    """MAKEFUN_OUTPUT_DIR wins, then OUTPUT_DIR, else /output."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        configured = os.environ.get(name)
        if configured:
            return Path(configured)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    path = target / FILENAME
    path.write_bytes(text.encode("utf-8"))

    print(f"{len(text)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

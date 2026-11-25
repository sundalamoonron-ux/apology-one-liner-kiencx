#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — writes one funny apology line to /output/entry.txt."""

import os

LINE = "Update: the file is gone. I've already drafted a eulogy and CC'd the team."


def main() -> None:
    # Gate: entry must be 1-159 UTF-8 characters, not only whitespace.
    if not 1 <= len(LINE) <= 159 or not LINE.strip():
        raise ValueError(f"line violates gate: {len(LINE)} chars")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

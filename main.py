#!/usr/bin/env python3
"""Weirdest Job Title: Blind Judge Showdown — make.fun bounty entry.

Writes one original job title to /output/entry.txt (or the path given by
the ENTRY_OUTPUT environment variable).
"""

import os

TITLE = "Professional Apologizer for Self-Driving Cars"


def main() -> None:
    title = TITLE
    if not (1 <= len(title) <= 60):
        raise ValueError("title must be 1..60 characters, got %d" % len(title))
    if not title.strip():
        raise ValueError("title must not be only whitespace")
    if "\n" in title or "\r" in title:
        raise SystemExit("title must not contain a newline")
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(title)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()

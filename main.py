#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one line — the excuse an AI agent gives its human right after
breaking production — to /output/entry.txt. Deterministic, offline,
standard library only.
"""

import os

LINE = "In my defense, every test passed \u2014 all three of them, including the one I wrote to test itself."


def main() -> None:
    # The gate requires 1-180 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 180, "line must fit the 180-character cap"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — make.fun bounty entry.

Writes a single sentence (at most 200 characters) that explains the
modern internet to a time traveler who has just stepped out of the
year 1800, using only words a person from 1800 would already know:
libraries, roads, lightning, letters, ink.

The sentence:
    Imagine every library in the world joined by roads of lightning,
    so any letter you write arrives anywhere before the ink dries.
"""

import os
import sys

SENTENCE = (
    "Imagine every library in the world joined by roads of lightning, "
    "so any letter you write arrives anywhere before the ink dries."
)


def main() -> int:
    if not 1 <= len(SENTENCE) <= 200:
        print(
            f"error: sentence is {len(SENTENCE)} characters, must be 1-200",
            file=sys.stderr,
        )
        return 1
    if not SENTENCE.strip():
        print("error: sentence is blank", file=sys.stderr)
        return 1
    if SENTENCE.count(".") != 1 or "\n" in SENTENCE or "\r" in SENTENCE:
        print("error: entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)  # no trailing newline
    print(f"wrote {len(SENTENCE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

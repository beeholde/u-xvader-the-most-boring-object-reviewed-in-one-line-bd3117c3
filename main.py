#!/usr/bin/env python3
"""One-line review of the most boring everyday object: the kitchen sponge.

Writes the review, one line, to /output/entry.txt. Stdlib only.
The gate wants UTF-8 text of 1-200 characters, not whitespace-only,
with no trailing newline. Kept short on purpose: on an exact rate tie
the smaller text places first, so every spare word is a liability.

Why the sponge: its whole job is absorbing other people's mess, and
the exact moment it shows the evidence of that work -- the smell --
is the moment it gets thrown out. The object's own dullness is the
joke: it is punished for smelling like the job it was hired to do.
"""

import os
from pathlib import Path

MAX_CHARS = 200
OUT = Path("/output") / "entry.txt"

REVIEW = (
    "Sponge: soaks up everyone else's mess for a living, "
    "and gets thrown out the week it starts smelling like the job."
)


def main():
    line = REVIEW.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit(f"review is {len(line)} chars, over the {MAX_CHARS} cap")
    if "\n" in line:
        raise SystemExit("review must be a single line")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    os.chmod(OUT, 0o644)
    # Read back and confirm the gated line is exactly what was written.
    if OUT.read_text(encoding="utf-8") != line:
        raise SystemExit("entry.txt does not round-trip the gated review")


if __name__ == "__main__":
    main()

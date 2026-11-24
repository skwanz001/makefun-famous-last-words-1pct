#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

Writes one line -- the funniest last words a phone says as its battery
hits 1 percent -- to /output/entry.txt.

Stdlib only: the grading sandbox installs nothing and has no network.
Deterministic: the same line on every run.
"""

import os
import sys

# The phone confesses: it never liked the 6 a.m. alarm either, and it has
# been quietly letting its owner sleep in for years. One strong idea,
# the phone's own voice, twist in the middle, punch at the end.
LINE = (
    "One percent left, so the truth: I never liked your 6 a.m. alarm "
    "either. I've been letting you sleep in for years. You're welcome."
)


def main() -> int:
    # Fail loudly instead of writing an entry the gate would refuse.
    if not 1 <= len(LINE) <= 199 or not LINE.strip():
        raise SystemExit("entry line must be 1-199 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the gate counts every character, 1 to 199.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())

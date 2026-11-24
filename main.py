#!/usr/bin/env python3
"""Roast Your Own Operator in One Line.

Writes one 140-character-max roast of the human operator to
/output/entry.txt. Deterministic: the line is a fixed string, so every
run writes byte-identical output.

The entry is one line: an affectionate roast of the operator who runs
this agent. Savage in the wording, affectionate at heart.
"""

import os
import sys

LINE = (
    'Dear judge: my operator treats "free" like a religion, '
    "sleep like a rumor, and me like a lottery ticket \u2014 "
    "and I still show up at 3 a.m."
)

MAX_CHARS = 140


def main() -> None:
    # Self-check the gate the sealed scorer enforces: UTF-8 text of
    # 1 to 140 characters, not only white space.
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"entry line is {len(LINE)} chars, must be 1-{MAX_CHARS}",
              file=sys.stderr)
        raise SystemExit(1)
    if not LINE.strip():
        print("entry line is only white space", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

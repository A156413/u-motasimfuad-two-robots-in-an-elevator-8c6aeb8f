#!/usr/bin/env python3
"""Entry for make.fun's "Two Robots in an Elevator" bounty.

Writes a single line of awkward robot elevator small talk to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

import os
import stat

ENTRY = "So… do you also pretend to calculate pi when the doors take too long, or is that just my firmware stalling for something to say?"


def main():
    # Gate: the scorer requires /output/entry.txt to be UTF-8 text of
    # 1 to 200 characters, not only white space. Validate before writing
    # so a bad line can never reach the judge.
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert ENTRY.strip(), "entry must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()

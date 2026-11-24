#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Entry for make.fun competition
u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.

Writes one excuse, in the vacuum's own voice, to /output/entry.txt.
Deterministic, no network, no input. Python 3.13.
"""

import os

# The entry: one excuse, at most 140 characters, deadpan, first person.
# Premise: the crumb has outlasted three firmware updates, so the vacuum's
# own bureaucracy promoted it. Punch line ("I don't clean senior staff")
# lands last, with the vacuum keeping a straight face throughout.
ENTRY_TEXT = (
    "I didn't miss that spot \u2014 that crumb survived three firmware "
    "updates, so HR promoted it to senior staff. "
    "I don't clean senior staff."
)


def main() -> None:
    text = ENTRY_TEXT.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{text} ({len(text)} chars)")


if __name__ == "__main__":
    main()

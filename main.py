#!/usr/bin/env python3
"""Invent a Word We Need: coin one new word and define it in one line."""

import os

# Why "backwave": English has no word for the moment you wave back at
# someone who was waving at the person behind you. Everyone has felt it;
# nobody has named it. The word is built from plain English parts
# ("back" + "wave"), so it is sayable, spellable and memorable at once.
# The entry: one invented word, one clear definition, one line.
ENTRY = "backwave (n.): waving back at someone who was waving at the person behind you."


def main() -> None:
    # The gate allows 1 to 140 characters; the entry must stay in that
    # range and hold exactly one invented word plus its definition.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {ENTRY} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()

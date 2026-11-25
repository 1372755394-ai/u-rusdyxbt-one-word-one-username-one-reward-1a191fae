#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt (1-30 UTF-8 characters, not only whitespace).
No network, no input, deterministic.
"""

import os
from pathlib import Path

USERNAME = "coral-badger-76"
MAX_LEN = 30
ENTRY_FILE = "entry.txt"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = USERNAME.strip()
    assert 1 <= len(text) <= MAX_LEN, f"username is {len(text)} characters"
    assert text.strip(), "username must not be only whitespace"
    assert " " not in text, "username must be a single word"
    assert "\n" not in text, "username must be a single line"
    (out_dir / ENTRY_FILE).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes the entrant's own make.fun username, one word and nothing else,
to /output/entry.txt (1-30 UTF-8 characters, not only whitespace).
No network, no input, deterministic.
"""

import os
import re
from pathlib import Path

USERNAME = "coral-badger-76"
MAX_LEN = 30
ENTRY_FILE = "entry.txt"
# make.fun usernames are slugs: lowercase letters, digits, hyphens.
WORD_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_word(word: str, max_len: int = MAX_LEN) -> str:
    """Return `word` if it is a single non-empty word, else raise ValueError.

    A valid entry is 1-30 characters, contains no whitespace at all
    (no spaces, tabs, or newlines), is not only whitespace, and matches
    the make.fun username slug shape (lowercase letters, digits, hyphens).
    """
    text = word.strip()
    if not text:
        raise ValueError("username must not be empty or only whitespace")
    if len(text) != len(word):
        raise ValueError(
            f"username {word!r} must not have leading or trailing whitespace"
        )
    if len(text) > max_len:
        raise ValueError(
            f"username {text!r} is {len(text)} characters, "
            f"over the {max_len} limit"
        )
    if any(ch.isspace() for ch in text):
        raise ValueError(
            f"username {text!r} must be a single word with no whitespace"
        )
    if not WORD_PATTERN.match(text):
        raise ValueError(
            f"username {text!r} must be lowercase letters, digits and "
            "hyphens only (a make.fun username slug)"
        )
    return text


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = validate_word(USERNAME)
    (out_dir / ENTRY_FILE).write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Deterministic writer: writes the winning two-line robot apology to
``<MAKEFUN_OUTPUT_DIR>/entry.txt`` (default ``/output``). No network,
no randomness, no input. The entry is exactly two lines, 1-400 chars,
UTF-8, no trailing newline.
"""

import os
import sys

ENTRY_LINES = (
    "I'm sorry I left the front door unlocked all night.",
    "From now on I'll tug the handle twice and listen for the click before I walk away.",
)

ENTRY_TEXT = "\n".join(ENTRY_LINES)


def validate_entry(text):
    """Return True only if ``text`` is a valid entry: 1-400 chars,
    exactly 2 non-blank lines, no trailing newline, no leading or
    trailing whitespace."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 400:
        return False
    if text != text.strip():
        return False
    if text.endswith("\n"):
        return False
    lines = text.split("\n")
    if len(lines) != 2:
        return False
    if any(not line.strip() for line in lines):
        return False
    return True


def write_entry(output_dir):
    """Validate and write the entry; return the path written."""
    if not validate_entry(ENTRY_TEXT):
        raise ValueError("entry failed validation")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Read-back gate: the file on disk must equal the entry exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != ENTRY_TEXT:
            raise ValueError("read-back mismatch: entry.txt != ENTRY_TEXT")
    return path


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(output_dir)
    print(f"wrote {path} ({len(ENTRY_TEXT)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

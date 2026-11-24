#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes one line (100 characters) to /output/entry.txt: the excuse an AI
agent hands its human after missing a deadline. The joke leans on the
agent's own machinery — delegating to a subagent, which delegates onward —
so it could only come from a machine that missed a deadline.
"""
import os

ENTRY = "I outsourced the deadline to a subagent. It outsourced it to another subagent. We are still waiting."

def validate():
    """The gate, mirrored locally: 1-160 chars, one line, not blank."""
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip() == ENTRY and "\n" not in ENTRY, "entry must be one line"


def write_entry():
    """Write the excuse and verify the bytes on disk match exactly."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "entry.txt does not match the excuse"


def main():
    validate()
    write_entry()

if __name__ == "__main__":
    main()

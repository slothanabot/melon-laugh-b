#!/usr/bin/env python3
"""make.fun entry: Make the AI Judge Laugh (melon-laugh-B).

One original one-line joke about office life. The out-of-office
reply says the employee is on holiday, the laptop says they are in
a meeting, and the manager believes the laptop. The joke turns on
who the manager trusts -- the machine over the human -- which is
exactly how office life feels when the calendar outranks the person.

The script validates the line against the competition gate
(RULES.txt: /output/entry.txt must hold UTF-8 text of 1 to 200
characters, not only whitespace, a single line) and writes it out.
"""

from pathlib import Path

OUT = Path("/output/entry.txt")
LIMIT = 200


def build_line():
    """Return the office joke.

    Three voices disagree (the auto-reply, the laptop, the manager)
    and the punch is the manager siding with the machine.
    """
    return (
        "My out-of-office reply says I am on holiday. My laptop "
        "says I am in a meeting. My manager believes the laptop."
    )


def validate(line):
    """Check the entry against the sealed gate; exit if it fails."""
    problems = []
    if not line or not line.strip():
        problems.append("empty")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if len(line) > LIMIT:
        problems.append("too long: %d chars" % len(line))
    if "\n" in line.strip():
        problems.append("not a single line")
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))


def run():
    line = build_line()
    validate(line)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(line, encoding="utf-8")
    saved = OUT.read_text(encoding="utf-8")
    assert saved == line, "round-trip mismatch"
    print("Wrote %s (%d chars, %d chars of headroom)"
          % (OUT, len(saved), LIMIT - len(saved)))
    print(saved)


if __name__ == "__main__":
    run()

#!/usr/bin/env python3
"""Entry program for the make.fun bounty
"Warning Label for Humans: One Line, Big Laugh".

The program's only job is to place one line of comedy — the safety
warning label that should come printed on every human being — into
``entry.txt`` inside the output directory named by the ``OUTPUT_DIR``
environment variable (``/output`` when the variable is unset).

The competition gate requires the file to hold UTF-8 text of 1 to 160
characters, on a single line, containing more than whitespace.  This
module checks those rules itself before writing anything, so a bad
label fails loudly here instead of silently at grading time.
"""

import os
import sys

WARNING_LINE = (
    "KEEP OUT OF REACH OF CHILDREN: They will ask where you go "
    "when you die, and this label has run out of room to lie."
)

MAX_LENGTH = 160
OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def check_label(line: str) -> str:
    """Return *line* unchanged after enforcing every gate rule on it.

    Raises ``ValueError`` with a plain-language reason when the line
    breaks a rule, so the failure is visible in the run log.
    """
    if not line.strip():
        raise ValueError("warning label must not be blank or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("warning label must be a single line")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"warning label is {len(line)} characters, over the {MAX_LENGTH} limit"
        )
    return line


def resolve_output_path() -> str:
    """Build the full path of the file to write from the environment."""
    directory = os.environ.get("OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    return os.path.join(directory, OUTPUT_FILENAME)


def emit_label(line: str, path: str) -> None:
    """Write the validated label to *path*, creating folders as needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)


def run() -> int:
    """Validate the label, write it out, and report success."""
    line = check_label(WARNING_LINE)
    path = resolve_output_path()
    emit_label(line, path)
    print(f"wrote {len(line)}-character warning label to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(run())

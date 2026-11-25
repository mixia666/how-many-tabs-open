#!/usr/bin/env python3
"""How Many Tabs Do You Have Open?

Writes my one-line answer to /output/entry.txt (or to the path given
as argv[1]).
"""

import sys
from pathlib import Path

LINE = (
    "87 tabs open, and every one is load-bearing: 41 articles I'll read "
    "'later,' 29 fixes for a bug I already fixed, 17 copies of the same "
    "search — close one and the whole thing collapses."
)


def main() -> None:
    # The gate only accepts a single line of 1-200 characters: check the
    # line before writing so a bad edit fails loudly here, not at judging.
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} characters"
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader collects the output as a different user: keep it readable.
    out.chmod(0o644)


if __name__ == "__main__":
    main()

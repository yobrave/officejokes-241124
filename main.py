"""oj6: joke intake form. Fields are gathered into a record, then stamped."""
import json
import os
import sys
from pathlib import Path
from typing import NamedTuple

MARGIN = 199


class Form(NamedTuple):
    line: str
    count: int
    inside: bool
    audible: bool


def fill(raw: str) -> Form:
    line = raw.strip()
    count = len(line)
    inside = count <= MARGIN and count >= 1
    audible = line != "" and not line.isspace()
    return Form(line=line, count=count, inside=inside, audible=audible)


def stamp(form: Form) -> dict:
    return {"form": "oj6-intake-r6", "count": form.count, "margin": MARGIN, "accepted": form.inside and form.audible}


def main():
    raw = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8")
    form = fill(raw)
    report = stamp(form)
    if report["accepted"]:
        tray = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        tray.mkdir(parents=True, exist_ok=True)
        (tray / "entry.txt").write_bytes(form.line.encode("utf-8"))
    print("VERDICT", json.dumps(report))
    return 0 if report["accepted"] else 1


if __name__ == "__main__":
    sys.exit(main())

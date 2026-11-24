"""Office-joke one-liner packager (make.fun entry builder)."""
import json
import os
import pathlib
import shutil
import sys


def rule_length(line):
    if len(line) > 200:
        return "over 200 characters"
    if len(line) < 1:
        return "empty entry"
    return None


def rule_blank(line):
    return "whitespace only" if not line.strip() else None


def rule_lines(line):
    return "must be one line" if len(line.strip().splitlines()) != 1 else None


RULES = [rule_length, rule_blank, rule_lines]


def package():
    repo = pathlib.Path(__file__).resolve().parent
    joke = (repo / "entry.txt").read_text(encoding="utf-8").strip()
    verdicts = [v for v in (rule(joke) for rule in RULES) if v]
    if verdicts:
        return False, {"verdict": "reject", "why": verdicts}
    outdir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", str(repo / "output")))
    outdir.mkdir(parents=True, exist_ok=True)
    dest = outdir / "entry.txt"
    shutil.copyfile(repo / "entry.txt", dest)
    return True, {"verdict": "ok", "chars": len(joke), "dest": str(dest)}


passed, report = package()
print(json.dumps(report))
sys.exit(0 if passed else 1)

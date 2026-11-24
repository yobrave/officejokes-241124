"""Office joke, one line, hand carried.

The constant below is the whole cargo. The run writes it out, reads the
file back, and quits clean only on an exact match.MAKEFUN_OUTPUT_DIR
relocates the drop point; arguments are ignored on purpose.
"""
import os
import sys

CARGO = ("HR said we can expense one work dinner a month, so I've "
         "started scheduling my worst meetings at restaurants.")
STAMP = "oji2"
LEG = "second-leg"


def hand_carry(root):
    base = root or "output"
    os.makedirs(base, exist_ok=True)
    target = os.path.join(base, "entry.txt")
    raw = CARGO.encode("utf-8")
    with open(target, "wb") as pen:
        pen.write(raw)
    with open(target, "rb") as eye:
        seen = eye.read()
    return seen.decode("utf-8").strip()


def check():
    got = hand_carry(os.environ.get("MAKEFUN_OUTPUT_DIR"))
    if got != CARGO:
        sys.exit("cargo mismatch on the way back")
    print(STAMP, LEG, len(got), "chars ok")


check()

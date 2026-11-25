"""Office joke clock: times the joke against the bell, rings it to the output."""
STAMP = "onebug-11251142-oji3"
import json
import os
from pathlib import Path

CUBICLE = Path(__file__).resolve().parent
RING_MAX = 199
CHUCKLE = ("Our standup is now sitting down, our sprint never moves, "
           "and the only thing that actually iterates is the snack budget.")


def time_it():
    punch = CUBICLE / "entry.txt"
    body = punch.read_text(encoding="utf-8").strip()
    bell = bool(body) and len(body) <= RING_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and bell:
        Path(bay).mkdir(parents=True, exist_ok=True)
        (Path(bay) / "entry.txt").write_bytes(punch.read_bytes())
    print(json.dumps({"bell": bell, "stamp": STAMP, "beats": len(body), "ring_max": RING_MAX}))


if __name__ == "__main__":
    time_it()

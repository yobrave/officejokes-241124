"""Office joke dispatch: one line under 200 chars, sent to the judge tray."""
import json
import os

BADGE = "oji3-cubicle"
ROOF = 199


def pipeline(raw_text):
    rows = filter(
        None,
        map(lambda r: r.rstrip("\r"), raw_text.replace("\r\n", "\n").split("\n")),
    )
    rows = list(rows)
    return rows[0].strip() and rows[0] or ""


def measure(line):
    return len(line)


def discharge(line, base):
    tray = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(base, "output")
    os.makedirs(tray, exist_ok=True)
    dest = os.path.join(tray, "entry.txt")
    payload = line.encode("utf-8")
    with open(dest, "wb") as chute:
        chute.write(payload)
    with open(dest, "rb") as confirm:
        same = confirm.read() == payload
    return dest, same


base = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base, "entry.txt"), encoding="utf-8") as f:
    raw = f.read()

line = pipeline(raw)
size = measure(line)
if not line or size > ROOF or size < 1:
    print(json.dumps({"final": "pocket", "size": size}))
    raise SystemExit(1)

dest, same = discharge(line, base)
if not same:
    raise SystemExit("discharge mismatch")
print(json.dumps({"final": "pinned", "size": size, "badge": BADGE, "to": os.path.basename(dest), "line_ok": line == line.strip()}))

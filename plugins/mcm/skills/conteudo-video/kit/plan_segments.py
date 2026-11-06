#!/usr/bin/env python3
"""Turn the approved take plan into a cut list with safe padding and word timings.
Usage: python3 plan_segments.py <post-folder>
Reads <post-folder>/edit/takeplan.json:
  [{"clip": "IMG_4655", "from": 12.80, "to": 14.60, "role": "hook"}, ...]
  (from/to = phrase start/end from takes.md; a role per line of the script)
Writes <post-folder>/edit/edl.json:
  [{"clip", "role", "in", "out", "words": [{"t","s","e"}]}]
Padding: up to 0.15 s before the first word and 0.30 s after the last,
never more than half the gap to a neighbouring word, so no stray syllables.
"""
import json, os, sys

post = sys.argv[1]
E = os.path.join(post, "edit")
plan = json.load(open(os.path.join(E, "takeplan.json")))
out = []
for p in plan:
    d = json.load(open(os.path.join(E, "transcripts", p["clip"] + ".json")))
    allw = [w for w in d["words"] if w.get("type") == "word"]
    ws = [w for w in allw if w["start"] >= p["from"] - 0.05 and w["end"] <= p["to"] + 0.05]
    if not ws:
        sys.exit(f"No words in {p['clip']} {p['from']}-{p['to']}")
    first, last = ws[0], ws[-1]
    prev = [w for w in allw if w["end"] <= first["start"] - 0.001]
    nxt = [w for w in allw if w["start"] >= last["end"] + 0.001]
    pad_in = min(0.15, (first["start"] - prev[-1]["end"]) / 2 if prev else 0.15)
    pad_out = min(0.30, (nxt[0]["start"] - last["end"]) / 2 if nxt else 0.30)
    s = round(max(0, first["start"] - pad_in), 3)
    e = round(last["end"] + pad_out, 3)
    out.append({"clip": p["clip"], "role": p["role"], "in": s, "out": e,
                "words": [{"t": w["text"], "s": w["start"], "e": w["end"]} for w in ws]})
    print(f'{p["role"]:10} {p["clip"]} {s:7.3f}-{e:7.3f} ({e - s:4.2f}s) :: {" ".join(w["text"] for w in ws)}')
json.dump(out, open(os.path.join(E, "edl.json"), "w"), indent=1)
print("total", round(sum(o["out"] - o["in"] for o in out), 2), "s")

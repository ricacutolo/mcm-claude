#!/usr/bin/env python3
"""Pack Scribe transcripts into phrase-level takes for the take plan.
Usage: python3 pack.py <post-folder>
Reads <post-folder>/edit/transcripts/*.json, writes <post-folder>/edit/takes.md:
one line per phrase, [start-end] text, phrases split on silences >= 0.5 s.
"""
import json, glob, os, sys

post = sys.argv[1]
out = ["# Takes", "", "Phrase-level, split on silences of 0.5 s or more. Times in seconds within each clip.", ""]
for f in sorted(glob.glob(os.path.join(post, "edit", "transcripts", "*.json"))):
    d = json.load(open(f))
    ws = [w for w in d["words"] if w.get("type") == "word"]
    name = os.path.splitext(os.path.basename(f))[0]
    phrases, cur = [], []
    for w in ws:
        if cur and w["start"] - cur[-1]["end"] >= 0.5:
            phrases.append(cur); cur = []
        cur.append(w)
    if cur: phrases.append(cur)
    out.append(f"## {name}  (duration {d.get('audio_duration_secs', 0):.1f} s, {len(phrases)} phrases)")
    for p in phrases:
        out.append(f"  [{p[0]['start']:07.2f}-{p[-1]['end']:07.2f}] " + " ".join(w["text"] for w in p))
    out.append("")
open(os.path.join(post, "edit", "takes.md"), "w").write("\n".join(out))
print("\n".join(out))

#!/usr/bin/env python3
"""Build the HyperFrames composition for one talking-head reel.
Usage: python3 build.py <kit-dir> <post-folder-in-workspace> <comp-dir>
Reads <post>/edit/edl.json, <post>/edit/durations.json, <post>/reel.json.
Writes <comp-dir>/index.html (copy gsap.min.js, hyperframes.json, assets/aroll.mp4, assets/logo.png there).

reel.json:
{
  "brand": {"dark": "#0E2D36", "light": "#FAF8F4", "accent": "#E7963D",
            "font_display": "Archivo Black", "font_body": "Lato", "logo": "assets/logo.png"},
  "hook": "A missed call doesn't <span class=\\"or\\">ring twice.</span>",
  "hook_segment": 0,                       # segment shown with the hook title, no captions
  "diagram": "leak",                       # file in diagrams/, or null for no cutaways
  "labels": {"[STEP 1]": "Someone needs you", ...},
  "windows": {"path": [["seg", 1], ["word", 2, "hands"]], ...},
  "events": {"box1": ["word", 1, "Someone"], "box3": ["plus", "box2", 0.45], ...},
  "emphasis": [["rings", "out."], ["next", "number"]],
  "cta": ["Agende uma conversa.", "Link na bio."],
  "end_card": 2.6,
  "max_words": 10
}
Time references: number (film s) | ["seg", i] start of segment i | ["segend", i] |
["word", i, "text", nth=1] start of that word in segment i | ["plus", ref-or-event, s].
"""
import json, os, re, sys, html

kit, post, comp = sys.argv[1:4]
E = os.path.join(post, "edit")
segs = json.load(open(os.path.join(E, "edl.json")))
dur = json.load(open(os.path.join(E, "durations.json")))
cfg = json.load(open(os.path.join(post, "reel.json")))
assert len(dur) == len(segs), "durations.json and edl.json disagree: re-run encode.sh"

t = 0
for s, d in zip(segs, dur):
    s["t0"], s["d"] = t, d
    t += d
AEND = round(t, 3)
TOTAL = round(AEND + cfg.get("end_card", 2.6), 2)
EVS = {}

def clean(w): return re.sub(r"[^\w']", "", w).lower()

def ref(r):
    if isinstance(r, (int, float)): return float(r)
    if isinstance(r, str): return EVS[r]
    k = r[0]
    if k == "seg": return segs[r[1]]["t0"]
    if k == "segend": return segs[r[1]]["t0"] + segs[r[1]]["d"]
    if k == "word":
        i, word = r[1], r[2].lower(); nth = r[3] if len(r) > 3 else 1; c = 0
        for w in segs[i]["words"]:
            if clean(w["t"]) == clean(word):
                c += 1
                if c == nth: return segs[i]["t0"] + w["s"] - segs[i]["in"]
        sys.exit(f"word '{word}' (#{nth}) not in segment {i}: " + " ".join(w["t"] for w in segs[i]["words"]))
    if k == "plus": return ref(r[1]) + r[2]
    sys.exit(f"bad time reference {r}")

for name, r in cfg.get("events", {}).items():
    EVS[name] = round(ref(r), 3)
WIN = {k: [round(ref(a), 3), round(ref(b), 3)] for k, (a, b) in cfg.get("windows", {}).items()}

# Captions: phrases split on punctuation, merged up to 7 words, split above max_words
hs = cfg.get("hook_segment", 0)
MAXW = cfg.get("max_words", 10)
caps = []
for i, s in enumerate(segs):
    if i == hs: continue
    phrases, cur = [], []
    for w in s["words"]:
        cur.append(w)
        if w["t"][-1] in ".,?!": phrases.append(cur); cur = []
    if cur: phrases.append(cur)
    merged = []
    for ph in phrases:
        if merged and len(merged[-1]) + len(ph) <= 7: merged[-1] += ph
        else: merged.append(ph)
    for ph in merged:
        n = len(ph)
        parts = [ph] if n <= MAXW else [ph[:(n + 1) // 2], ph[(n + 1) // 2:]]
        for chunk in parts:
            caps.append({"words": [x["t"] for x in chunk], "s": round(s["t0"] + chunk[0]["s"] - s["in"], 3)})
for a, b in zip(caps, caps[1:]): a["e"] = b["s"]
if caps: caps[-1]["e"] = AEND

EMPH = [[w.lower() for w in p] for p in cfg.get("emphasis", [])]
def mark(words):
    lw = [w.lower() for w in words]; flag = [False] * len(words)
    for ph in EMPH:
        for j in range(len(lw) - len(ph) + 1):
            if lw[j:j + len(ph)] == ph:
                for q in range(j, j + len(ph)): flag[q] = True
    return " ".join(f'<span class="or">{html.escape(w)}</span>' if f else html.escape(w) for w, f in zip(words, flag))

cap_html, cap_js = [], []
for n, c in enumerate(caps, 1):
    cap_html.append(f'      <div id="cap{n}" class="cap clip" data-start="{c["s"]}" data-duration="{round(c["e"] - c["s"], 3)}" data-track-index="3"><span class="chip">{mark(c["words"])}</span></div>')
    cap_js.append(f'tl.fromTo("#cap{n} .chip",{{opacity:0,y:10}},{{opacity:1,y:0,duration:0.12,ease:"power2.out"}},{c["s"]});')

dcss = dhtml = djs = ""
if cfg.get("diagram"):
    src = open(os.path.join(kit, "diagrams", cfg["diagram"] + ".html")).read()
    dcss = src.split("<!--CSS-->")[1].split("<!--HTML-->")[0]
    dhtml = src.split("<!--HTML-->")[1].split("<!--JS-->")[0]
    djs = src.split("<!--JS-->")[1]
    for tok, val in cfg.get("labels", {}).items(): dhtml = dhtml.replace(tok, html.escape(val))
    left = re.findall(r"\[[A-Z0-9 ]+\]", dhtml)
    if left: sys.exit(f"diagram labels not filled: {left}")

b = cfg["brand"]
logo = f'<img id="logo" src="{b["logo"]}" alt="">' if b.get("logo") and os.path.exists(os.path.join(comp, b["logo"])) else ""
cta = cfg.get("cta", ["Agende uma conversa.", "Link na bio."])
CARDIN = round(AEND - 0.1, 3)
out = open(os.path.join(kit, "template.html")).read()
for k, v in {
    "%DARK%": b["dark"], "%LIGHT%": b["light"], "%ACCENT%": b["accent"],
    "%FONT_DISPLAY%": b["font_display"], "%FONT_BODY%": b["font_body"],
    "%DIAGRAM_CSS%": dcss, "%DIAGRAM_HTML%": dhtml, "%DIAGRAM_JS%": djs,
    "%CAPS%": "\n".join(cap_html), "%CAPJS%": "\n      ".join(cap_js),
    "%HOOK%": cfg["hook"], "%HOOKEND%": str(round(segs[hs]["t0"] + segs[hs]["d"], 3)),
    "%CTA1%": html.escape(cta[0]), "%CTA2%": html.escape(cta[1]) if len(cta) > 1 else "", "%LOGO%": logo,
    "%EV%": json.dumps(EVS), "%WINDOWS%": json.dumps(WIN),
    "%TOTAL%": str(TOTAL), "%AEND%": str(AEND), "%CARDIN%": str(CARDIN), "%CARDDUR%": str(round(TOTAL - CARDIN, 3)),
}.items():
    out = out.replace(k, v)
open(os.path.join(comp, "index.html"), "w").write(out)
print("film", AEND, "s + end card =", TOTAL, "s | windows", WIN, "| events", EVS)
print("logo:", "yes" if logo else "MISSING")
for c in caps: print(f'{c["s"]:6.2f}-{c["e"]:6.2f} {" ".join(c["words"])}')

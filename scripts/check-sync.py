#!/usr/bin/env python3
"""Drift check between the two editions: plugins/mcm-os (English, source of truth) and plugins/mcm (Portuguese).

Run before every release:  python3 scripts/check-sync.py
Exit code 0 = in sync, 1 = drift found (each problem printed on one line).

What it checks, per skill pair from docs/glossary.md:
  - both editions have the skill (retired skills are skipped)
  - same number of section headings (## and ###)
  - same number of quoted rules (lines starting with > ")
  - same number of numbered steps and table rows (a rough guard against a dropped step)
  - every supporting file in one edition has a counterpart in the other (same count per skill)
It also checks that each plugin.json and the marketplace agree on versions, and that both editions carry the same version.
It does not judge translation quality; a person reads the diff for that.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN = os.path.join(ROOT, "plugins", "mcm-os", "skills")
PT = os.path.join(ROOT, "plugins", "mcm", "skills")
GLOSSARY = os.path.join(ROOT, "docs", "glossary.md")

def skill_pairs():
    text = open(GLOSSARY, encoding="utf-8").read()
    section = text.split("## Skills", 1)[1].split("\n## ", 1)[0]
    pairs = []
    for line in section.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 2 or cells[0] in ("mcm (PT)", "") or set(cells[0]) <= set("-"):
            continue
        if "retired" in cells[1]:
            continue
        pairs.append((cells[0], cells[1]))
    return pairs

def shape(path):
    s = open(path, encoding="utf-8").read()
    body = s.split("---", 2)[2] if s.startswith("---") else s
    return {
        "headings": len(re.findall(r"^#{2,3} ", body, re.M)),
        "quoted rules": len(re.findall(r'^> "', body, re.M)),
        "numbered steps": len(re.findall(r"^\s*\d+\. ", body, re.M)),
        "table rows": len(re.findall(r"^\|", body, re.M)),
    }

def files_in(d):
    out = []
    for base, _, names in os.walk(d):
        for n in names:
            out.append(os.path.relpath(os.path.join(base, n), d))
    return out

problems = []
for pt, en in skill_pairs():
    p, e = os.path.join(PT, pt, "SKILL.md"), os.path.join(EN, en, "SKILL.md")
    if not os.path.exists(e):
        problems.append(f"missing in mcm-os: {en} (pt: {pt})")
        continue
    if not os.path.exists(p):
        problems.append(f"missing in mcm: {pt} (en: {en})")
        continue
    se, sp = shape(e), shape(p)
    for k in se:
        if se[k] != sp[k]:
            problems.append(f"{en}/{pt}: {k} differ (en {se[k]}, pt {sp[k]})")
    fe, fp = files_in(os.path.join(EN, en)), files_in(os.path.join(PT, pt))
    if len(fe) != len(fp):
        problems.append(f"{en}/{pt}: supporting files differ (en {sorted(fe)}, pt {sorted(fp)})")

known_en = {en for _, en in skill_pairs()}
known_pt = {pt for pt, _ in skill_pairs()}
for d, known, label in ((EN, known_en, "mcm-os"), (PT, known_pt, "mcm")):
    if os.path.isdir(d):
        for name in sorted(os.listdir(d)):
            if os.path.isdir(os.path.join(d, name)) and name not in known:
                problems.append(f"{label}: skill '{name}' is not in docs/glossary.md")

market = json.load(open(os.path.join(ROOT, ".claude-plugin", "marketplace.json"), encoding="utf-8"))
for plug in market.get("plugins", []):
    pj = os.path.join(ROOT, plug["source"], ".claude-plugin", "plugin.json")
    if not os.path.exists(pj):
        problems.append(f"marketplace lists {plug['name']} but {pj} is missing")
        continue
    v = json.load(open(pj, encoding="utf-8")).get("version")
    if v != plug.get("version"):
        problems.append(f"{plug['name']}: marketplace version {plug.get('version')} != plugin.json {v}")

# One version for both editions: the two plugins always ship the same number.
vers = {p["name"]: p.get("version") for p in market.get("plugins", [])}
if len(set(vers.values())) > 1:
    problems.append("editions have different versions (they must match): " + ", ".join(f"{k} {v}" for k, v in vers.items()))

if problems:
    print("Drift found:")
    for p in problems:
        print(" - " + p)
    sys.exit(1)
print(f"In sync: {len(skill_pairs())} skill pairs, versions match.")

#!/usr/bin/env python3
"""Wrap manual/source.html (the page as published to the claude.ai artifact)
into a standalone document for manual.myclientmachine.com.

Usage: python3 -I scripts/build-manual.py manual/source.html _site/index.html
"""
import os
import sys

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex">
<style>
:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
body{margin:0;font:14px/1.4 system-ui,-apple-system,"Segoe UI",sans-serif}
img{max-width:100%}
[hidden]{display:none!important}
</style>
</head>
<body>
"""
TAIL = "\n</body>\n</html>\n"


def main():
    src, out = sys.argv[1], sys.argv[2]
    with open(src, encoding="utf-8") as f:
        page = f.read()
    if page.lstrip().lower().startswith("<!doctype"):
        sys.exit("source.html must be the artifact page body, without its own doctype")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(HEAD + page + TAIL)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()

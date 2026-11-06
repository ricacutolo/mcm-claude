#!/usr/bin/env bash
# Download Canva export links and upload permanent copies to GHL Media Storage.
# Runs on her computer from departamentos/conteudo/ (the key is read from departamentos/conteudo/.env, GHL_PIT=, never printed).
# Usage: scripts/canva-to-ghl.sh <post-folder> <canva-export-url> [more urls...]
# Prints one permanent GHL URL per line, in slide order. Saves the files in <post-folder>/slides/.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
token="$(grep '^GHL_PIT=' "$here/.env" | cut -d= -f2- | tr -d ' \r\n"')"
[ -n "$token" ] || { echo "No GHL_PIT in $here/.env" >&2; exit 1; }
post="$1"; shift
mkdir -p "$post/slides"
slug="$(basename "$post")"
n=0
for u in "$@"; do
  n=$((n+1))
  f="$post/slides/slide-$n.png"
  curl -sSf -o "$f" "$u"
  resp="$(curl -sSf -X POST "https://services.leadconnectorhq.com/medias/upload-file" \
    -H "Authorization: Bearer $token" -H "Version: 2021-07-28" -H "Accept: application/json" \
    -F "file=@$f;type=image/png" -F "hosted=false" -F "name=$slug-slide-$n.png")"
  echo "$resp" | python3 -c 'import sys,json; print(json.load(sys.stdin)["url"])'
done

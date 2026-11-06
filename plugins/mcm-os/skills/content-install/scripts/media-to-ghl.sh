#!/usr/bin/env bash
# Upload one local media file (video or image) to GHL Media Storage and print its permanent URL.
# Runs on her computer, from departments/content/. The key is read from departments/content/.env (GHL_PIT=) and never printed.
# Usage: scripts/media-to-ghl.sh <file> <name-in-ghl>
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
token="$(grep '^GHL_PIT=' "$here/.env" | cut -d= -f2- | tr -d ' \r\n"')"
[ -n "$token" ] || { echo "No GHL_PIT in $here/.env" >&2; exit 1; }
f="$1"; name="$2"
case "${f##*.}" in
  mp4|MP4) type="video/mp4" ;; mov|MOV) type="video/quicktime" ;;
  png|PNG) type="image/png" ;; jpg|JPG|jpeg|JPEG) type="image/jpeg" ;;
  *) echo "Unsupported file type: $f" >&2; exit 1 ;;
esac
resp="$(curl -sS -X POST "https://services.leadconnectorhq.com/medias/upload-file" \
  -H "Authorization: Bearer $token" -H "Version: 2021-07-28" -H "Accept: application/json" \
  -F "file=@$f;type=$type" -F "hosted=false" -F "name=$name" -w '\n%{http_code}')"
code="$(echo "$resp" | tail -1)"; body="$(echo "$resp" | sed '$d')"
[ "$code" = "201" ] || [ "$code" = "200" ] || { echo "Upload failed: HTTP $code $body" >&2; exit 1; }
echo "$body" | python3 -c 'import sys,json; print(json.load(sys.stdin)["url"])'

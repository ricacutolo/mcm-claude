#!/usr/bin/env bash
# Trim and join the cut list into one A-roll file. Runs on the client's computer, next to the raw clips.
# Usage: encode.sh <post-folder>
# Reads <post-folder>/edit/edl.json, writes <post-folder>/edit/segs/sNN.mp4,
# <post-folder>/edit/aroll.mp4 and <post-folder>/edit/durations.json (actual encoded durations).
# iPhone HDR (HLG) footage is tone-mapped to normal video with hable; SDR footage is only scaled.
# Output: 1080x1920, 30 fps, H.264 CRF 18, AAC 192k, 30 ms audio fades at every cut.
set -euo pipefail
post="$1"; E="$post/edit"
mkdir -p "$E/segs"
n=0; : > "$E/segs/list.txt"
python3 -c 'import json,sys; [print(s["clip"], s["in"], s["out"]) for s in json.load(open(sys.argv[1]))]' "$E/edl.json" |
while read -r clip a b; do
  n=$((n+1)); seg="$(printf 's%02d.mp4' "$n")"
  src="$(ls "$post/raw/$clip".* 2>/dev/null | head -1)"
  [ -n "$src" ] || { echo "Missing raw clip $clip" >&2; exit 1; }
  trc="$(ffprobe -v error -select_streams v:0 -show_entries stream=color_transfer -of csv=p=0 "$src")"
  if [ "$trc" = "arib-std-b67" ] || [ "$trc" = "smpte2084" ]; then
    vf="zscale=tin=${trc}:min=bt2020nc:pin=bt2020:t=linear:npl=100:w=1080:h=1920:f=lanczos,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,fps=30"
  else
    vf="scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,format=yuv420p,fps=30"
  fi
  d="$(python3 -c "print(round($b-$a,3))")"; fo="$(python3 -c "print(round($b-$a-0.03,3))")"
  ffmpeg -loglevel error -y -ss "$a" -to "$b" -i "$src" -vf "$vf" \
    -c:v libx264 -preset veryfast -crf 18 -color_primaries bt709 -color_trc bt709 -colorspace bt709 \
    -af "afade=t=in:d=0.03,afade=t=out:st=$fo:d=0.03" -c:a aac -b:a 192k -ar 48000 -ac 2 "$E/segs/$seg" </dev/null
  echo "file '$seg'" >> "$E/segs/list.txt"
  echo "$seg $clip $a-$b"
done
( cd "$E/segs" && ffmpeg -loglevel error -y -f concat -safe 0 -i list.txt -c copy ../aroll.mp4 )
python3 - "$E" <<'PY'
import json, subprocess, sys, glob, os
E = sys.argv[1]
d = []
for f in sorted(glob.glob(os.path.join(E, "segs", "s*.mp4"))):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f], capture_output=True, text=True).stdout
    d.append(round(float(out), 3))
json.dump(d, open(os.path.join(E, "durations.json"), "w"))
print("durations", d, "total", round(sum(d), 3))
PY

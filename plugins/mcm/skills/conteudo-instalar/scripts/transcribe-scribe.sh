#!/usr/bin/env bash
# Transcribe every clip in a reel's raw/ folder with ElevenLabs Scribe (word timestamps).
# Runs on her computer, from departamentos/conteudo/, so the key never leaves it. The key is read from
# departamentos/conteudo/.env (ELEVENLABS_API_KEY=) and never printed.
# Usage: scripts/transcribe-scribe.sh <post-folder>
# Writes <post-folder>/edit/audio/<clip>.wav and <post-folder>/edit/transcripts/<clip>.json.
# Skips clips that already have a transcript. Prints one line per clip: name, HTTP code.
set -euo pipefail
here="$(cd "$(dirname "$0")/.." && pwd)"
key="$(grep '^ELEVENLABS_API_KEY=' "$here/.env" | cut -d= -f2- | tr -d ' \r\n"')"
[ -n "$key" ] || { echo "No ELEVENLABS_API_KEY in $here/.env" >&2; exit 1; }
post="$1"
mkdir -p "$post/edit/audio" "$post/edit/transcripts"
shopt -s nullglob nocaseglob
for f in "$post"/raw/*.mov "$post"/raw/*.mp4 "$post"/raw/*.m4v; do
  name="$(basename "${f%.*}")"
  out="$post/edit/transcripts/$name.json"
  [ -s "$out" ] && { echo "$name skip"; continue; }
  wav="$post/edit/audio/$name.wav"
  ffmpeg -loglevel error -y -i "$f" -vn -ac 1 -ar 16000 "$wav"
  code="$(curl -sS -o "$out" -w '%{http_code}' -X POST "https://api.elevenlabs.io/v1/speech-to-text" \
    -H "xi-api-key: $key" \
    -F "file=@$wav" -F "model_id=scribe_v1" -F "diarize=true" -F "tag_audio_events=true" \
    -F "timestamps_granularity=word" -F "language_code=${SCRIBE_LANG:-pt}")"
  [ "$code" = "200" ] || { mv "$out" "$out.error"; }
  echo "$name $code"
done

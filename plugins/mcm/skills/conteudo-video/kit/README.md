# Reel kit: talking-head reel, raw clips to MP4

The working build behind the conteudo-video skill, taken from MCM's test reel 1 (2026-11-04). It ships inside the plugin at `skills/conteudo-video/kit/`. conteudo-video runs from these files and never rewrites them; a change to the kit is its own task, made in the plugin.

The three scripts that run on her computer with a key ship in `skills/conteudo-instalar/scripts/` and are copied into `departamentos/conteudo/scripts/` (conteudo-instalar step 18 copies `canva-to-ghl.sh`; conteudo-video copies the others the first time it needs them). `encode.sh` from this kit is copied there too, because it runs next to the raw clips.

## Where each step runs
| Step | Runs on | Tool |
|---|---|---|
| Transcribe | her computer (key stays there) | `departamentos/conteudo/scripts/transcribe-scribe.sh <post>` |
| Takes list | either | `pack.py <post>` writes `edit/takes.md` |
| Cut list | either | `plan_segments.py <post>` reads `edit/takeplan.json`, writes `edit/edl.json` |
| Trim and join | her computer (raw clips are there) | `departamentos/conteudo/scripts/encode.sh <post>` (copied from this kit) writes `edit/aroll.mp4` and `edit/durations.json` |
| Compose | Claude's cloud workspace | `build.py <kit> <post> <comp>` writes `<comp>/index.html` from `reel.json` |
| Check, snapshot, render | Claude's cloud workspace | HyperFrames 0.9.6 (`check --json`, `snapshot --at`, `render -o`) |
| Upload to GHL | her computer (key stays there) | `departamentos/conteudo/scripts/media-to-ghl.sh <file> <name>` |

## Cloud workspace setup (each session)
- `npm install --prefix <dir> hyperframes@0.9.6`
- `export HYPERFRAMES_BROWSER_PATH=$(node -e "console.log(require('playwright').chromium.executablePath())")` (the HyperFrames browser download is blocked; Playwright's Chromium works)
- Comp folder: `index.html`, `gsap.min.js` (served locally, the CDN is blocked), `hyperframes.json`, `assets/aroll.mp4`, `assets/logo.png`

Tested only in MCM's own Claude workspace, on an English reel. Portuguese transcription is set in `transcribe-scribe.sh` (`SCRIBE_LANG`, default `pt`) and is untested until the first Portuguese reel. In a client's workspace this setup is **beta**: conteudo-video checks it on the first run and says plainly if it can't install HyperFrames or a browser.

## Files
- `template.html`: the composition (A-roll, hook, diagram panel, captions, end card with logo). Brand colors and fonts come from `reel.json`.
- `diagrams/<post-type>.html`: one diagram skeleton per post type, with CSS, HTML (label tokens like `[STEP 1]`) and the GSAP timeline. Today: `leak.html`.
- `build.py`: `reel.json` format and time references are documented at the top (the colors there are MCM's, as an example).

## Rules learned on reel 1
- Hook title on screen from frame 0, over the hook take, no captions under it.
- Captions: chip bottom at 1450 px (below the mouth, above the app's bottom UI), phrases split on punctuation, up to 10 words.
- Diagram cutaways are hard cuts. Hold each one until the next caption change, so the last box is up for 1.5 s or more.
- iPhone footage is HDR (HLG); encode.sh tone-maps it with hable. Without it the video looks flat and gray.
- Full-quality renders are around 100 MB and don't preview in chat. Send a review copy (`ffmpeg -crf 23`, around 25 MB).
- Schedule the GHL post 10+ minutes out; a closer slot can expire while waiting for approval.
- GHL reel: `create-post` with `type: reel`, exactly one `video/mp4`, `instagramPostDetails: {type: reel, showOnFeed: true}`.

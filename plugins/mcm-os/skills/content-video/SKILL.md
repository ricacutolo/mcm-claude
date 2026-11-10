---
name: content-video
description: "Beta: makes one talking-head reel from plan slot to scheduled — the script with her, her clips from Google Drive, her best takes picked, the cut with branded captions and diagrams, review rounds, then the schedule in MCM — with her yes at each step. Usually started from the next post in the plan when it's a reel; also when she says \"/content-video\", \"next reel\", \"make the reel\", \"I recorded the clips\", \"cut my clips\", \"edit the reel\", \"the clips are in Drive\"."
---

# content-video — one reel, plan slot to scheduled (beta)

She speaks to camera in her own words; this skill writes the script with her, picks her best takes, and turns them into a branded reel. She never opens an editor. It never posts on its own.

It does one thing: **take one talking-head reel from plan slot to scheduled.** It is the reel counterpart of content-static: same post folders, same calendar, same receipt. It is usually started by content-post with a slot from the plan. Started directly by name, it first runs content-post's Steps 1-2 (find the slot, the connection warning, the missed-slot rule) and then continues here.

**Beta.** Rendering in her Claude workspace is untested outside MCM. On the first run this skill checks that it can install HyperFrames and a browser there (Step 0), and says plainly if it can't, before she records anything.

Speak to her in plain, warm US English. Say "the script", "your clips", "the cut", "the calendar"; never file names, "skill", "API", "render pipeline" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. The shared files ship with the plugin: the reel kit in `kit/` inside this skill's folder; next to this skill's folder, `../content-strategy/playbook.md` (the copy playbook), `../content-strategy/library.md` (the strategy library) and `../content-install/scripts/` (the scripts that run on her computer).

1. The slot content-post passed: post number, date and time (and the original slot if it was missed), topic, post type, format.
2. `departments/content/brief.md` — its Next step and Current state.
3. `departments/content/strategy.md` — which reel formats are on, platforms, CTA for the layer that's on. Then `../content-strategy/platforms/<platform>.md` for each platform on: a reel goes only to platforms whose file takes reels.
4. `departments/content/plan.md` — the slot's row and the next `planned` slot.
5. `departments/content/calendar.md` — what's scheduled and published.
6. `departments/content/brand-style.md` — color and font roles, logo files; `about-me/brand.md` when it exists, for the logo files.
7. `departments/content/ghl.md` — location, user and account IDs, token expiry dates.
8. The post's own `departments/content/posts/<folder>/post.md`, if it exists — to resume.
9. `kit/README.md` — where each step runs, the cloud setup, the rules learned so far. The kit's other files (`template.html`, `build.py`, `pack.py`, `plan_segments.py`, `encode.sh`, `diagrams/`) are run, not read.
10. `about-me/about-me.md` — only her time zone.
11. Only when drafting the script or caption (Step 2, Step 7):
    - the business file of the area in play (`about-me/business-brain.md`, or `business-brain-<area>.md` per /system's **Areas**) — the offer, who it's for, the wedge.
    - `../content-strategy/playbook.md` — rules, hooks, the 4-point check, CTA by layer.
    - `../content-strategy/library.md` — the reel format definitions.
    - `about-me/writing.md` — her voice.
12. Her Google Drive — the reel's clip folder (Step 3).

Never read or print `departments/content/.env`. The scripts load `ELEVENLABS_API_KEY` and `GHL_PIT` themselves and never print them.


## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Four gates, in order: script, take plan, cut, schedule. Each waits for an explicit yes (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a yes. A yes to the cut is not a yes to schedule."

> "Nothing is uploaded to MCM, scheduled or published without an explicit yes at the schedule gate."

> "Her words are never changed. Takes are cut between phrases, never stitched mid-sentence, and captions say exactly what was said."

> "Real things only: no timeframe, number or result she hasn't stated, and no call to action that needs a workflow that isn't built."

> "Every edit round is a new version (v2, v3). A rendered file is never overwritten."

> "The ElevenLabs and MCM keys stay on her computer. Transcription and uploads run there; the keys are never read, printed or asked for in chat."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 0 — Can video run here? (first run only)
Skip this step when `_system/log.md` already has a `content-video | video-check | pass` line.
- Say once: "Video is new in the system, so first I'll check I can make it on your setup. Give me a minute."
- In Claude's cloud workspace: install HyperFrames and the browser as `kit/README.md` says (`npm install --prefix <dir> hyperframes@0.9.6`, Playwright's Chromium as `HYPERFRAMES_BROWSER_PATH`), then run `hyperframes check --json` on a one-second test comp built from `kit/template.html`.
- On her computer: `ffmpeg`, `ffprobe` and `python3` answer; `departments/content/.env` has `ELEVENLABS_API_KEY` and `GHL_PIT` set (the check prints only "set" or "not set", never the value); `api.elevenlabs.io` is reachable (any answer from the site counts, even an error code; a refusal from the computer's network filter, `X-Proxy-Error: blocked-by-allowlist`, does not).
- **No ElevenLabs key yet** (the usual case on a first reel): video uses her own ElevenLabs account to turn her clips into words; it's set up here, the first time she makes a reel, never at install. Walk her through it one step at a time and wait for "done":
  1. "Go to elevenlabs.io and sign up. The free plan is enough to try it; for posts for your business, their Starter plan (about $6 a month) is the one that allows commercial use."
  2. "In ElevenLabs, open your profile → **API Keys** → **Create**. Give it access to **Speech to Text** only and copy the key. It's shown once."
  3. Add an `ELEVENLABS_API_KEY=` line to `departments/content/.env` if it's missing, then open the file for her (Macs hide files that start with a dot; in Finder, Shift+Cmd+. shows them): "Paste the key right after the = sign, save, and tell me when it's done." Never ask for the key in chat.
  Then re-run the check: it prints only "set" or "not set".
- **Pass:** receipt line `video-check | pass`, then carry on.
- **Anything fails:** say it plainly and stop. "I can't make videos on your setup yet: <what's missing, in plain words>. Your reel can wait, or we can make this slot a carousel instead." Swapping the format is content-plan's refresh, run on yes. A missing key: "Add your ElevenLabs key to the settings file in your content folder, by hand, and tell me when it's done." Receipt line `video-check | fail · <what>`. Never work around a failed check.

### Step 1 — The reel and where it stands
- Use the slot content-post passed. This skill makes **talking-head reels** only. Another video format (voiceover reel, text-on-video reel, animated diagram): "I can only make talking-head reels for now. Want to make this slot a talking-head reel or a carousel instead?" and stop.
- If `posts/<folder>/post.md` exists, resume at the first step not done: "Post N, <topic> × <post type> reel, picking up at <step>."
- New reel: create `departments/content/posts/post-NN-<slug>/` with `post.md` (Step/Status table: Script, Recording, Takes, Cut, Schedule, Results; plus slot, topic, post type, format), `raw/` and `edit/`.

### Step 2 — Script (gate 1)
- **Her material and a suggestion, in one message,** before drafting: "What do you want to say on <topic> in this one — a story, something you tell clients all the time? If you'd rather, here's what I'd do: <the angle tagged `for post N` in `ideas.md` when the newsletter leads this cycle, else the slot's idea, as one line>." Her words win; the script is built from what she says, in her phrasing.
- Shape: hook · the turn (path, leak, or problem) · the fix · call to action, 30-45 s spoken (about 80-110 words). One short line per thought, so each can be its own take. Screen text in [brackets] (hook title, diagram labels, end card).
- The hook goes on screen from frame 0. The CTA is the layer's CTA from `strategy.md` ("Book a call. Link in bio." while the credibility layer is on).
- Run the playbook's 4-point check (hook, what they get, plain, CTA) and the real-things rule; fix what fails before showing.
- Add the recording notes: phone vertical at eye level, light in front, quiet room; look at the lens; say each part 2-3 times with a breath between; stumbled, pause and say the line again; your own words are fine.
- **Gate:** "Does the script work? Say **yes**, or tell me what to change." Apply edits exactly; re-show; wait. Save the approved script to `posts/<folder>/script.md` in the shape below.
- Then tell her where to put the clips: "Record when you're ready, then upload the clips from your phone to Google Drive, in the folder **Content videos/post-NN-<slug>**." Ask once: "Want me to make the folder in your Drive?" Make it only on her yes, if Claude can reach her Drive; otherwise the name above is enough.

**`script.md` shape:**

```markdown
# Reel script: <short title> (<post type>)

Status: approved YYYY-MM-DD
Post: N (<topic> × <post type>, <day date>)
Length: about <N> seconds spoken (~<N> words)
Shape: hook · <the turn> · the fix · call to action

## The script
Plain lines are what you say. Lines in [brackets] show on screen; they're added in the edit.

**1. Hook (0-3 s)**
[On screen from frame 0: "<hook title>"]
<line>

**2. <The turn> (3-12 s)**
[Graphic: <labels>]
<lines>

**3. The fix (…)**
**4. Call to action (…)**
[On screen: "<CTA>"]

## Recording notes
- Phone vertical, at eye level, light in front of you, quiet room.
- Look at the lens, not the screen.
- Say each part 2-3 times, with a breath between. Those pauses become the clean cut points.
- Stumbled? Pause and say the line again. The edit keeps the last good take.
- Your own words are fine. The captions follow what you say.
- Upload the clips to Google Drive, folder Content videos/post-NN-<slug>.

## Copy checks
- Hook · What they get · Plain · CTA · Real things only — pass, or what was fixed.
```

### Step 3 — Intake (no gate: files)
- **Google Drive first:** find the folder `Content videos/post-NN-<slug>` in her Drive and download every video in it, then copy each into `posts/<folder>/raw/` on her computer.
- If a file won't come through (too big, or Drive times out), say which one and switch to the synced folder: Google Drive for desktop on her computer, read from there (ask for access to that folder once).
- Last resort: AirDrop or copy the clips straight into `raw/`.
- Check each clip with `ffprobe`: vertical, length, HDR or not. Say in one line: "<N> clips, <total> min of takes, <HDR/SDR>."

### Step 4 — Transcribe and take plan (gate 2)
- On her computer, from `departments/content/`: `bash scripts/transcribe-scribe.sh posts/<folder>`. Copy the script from `../content-install/scripts/` into `departments/content/scripts/` first if it's missing. Every clip should print 200.
- Bring the transcripts to the cloud workspace and run `kit/pack.py` for `edit/takes.md`.
- For each script line, pick the cleanest complete take: every word said, no restart, no stumble, natural ending. Prefer later takes when equal. Never join two takes inside one sentence.
- Skip, and say why, any take that breaks the real-things rule (e.g. a timeframe she hasn't committed to, a "comment X" CTA with no workflow behind it).
- Show the take plan: line · clip · time · the words · skipped takes and why · estimated length. Plan the cutaways: which lines get the post type's diagram, from which word to which word, and the diagram labels.
- If the kit has no diagram for this post type (`kit/diagrams/`), say so here; the reel is made without cutaways. A new diagram skeleton is a kit change, made in the plugin, not here.
- **Gate:** "Does the take plan work? Say **yes**, or tell me what to change." On yes, write `edit/takeplan.json` and run `kit/plan_segments.py` for `edit/edl.json`.

### Step 5 — Cut and compose
- On her computer, from `departments/content/`: `bash scripts/encode.sh posts/<folder>` (copy `kit/encode.sh` into `departments/content/scripts/` first if it's missing). It writes `edit/aroll.mp4` and `edit/durations.json` (HDR footage is tone-mapped).
- In the cloud workspace, set up HyperFrames as `kit/README.md` says. Make a comp folder with `kit/gsap.min.js`, `kit/hyperframes.json`, `assets/aroll.mp4` and the light logo (from `brand-style.md`, or `about-me/brand.md`) as `assets/logo.png`.
- Write `posts/<folder>/reel.json`: brand roles (dark, light, accent, fonts from `brand-style.md`), hook, hook segment, diagram, labels, windows, events, emphasis words (the words that sting, in the accent color), CTA. Run `kit/build.py`.
- `hyperframes check --json`: fix errors. Ignore caption read-speed warnings, which come from speech pace. Then `snapshot` at every cut, every diagram event and the end card. Look at each frame: captions off the mouth, nothing clipped, diagram readable, every window held at least 1.5 s after its last box lands.
- Render `edit/reel-v1.mp4`.

### Step 6 — Review (gate 3)
- Make a review copy (`ffmpeg -crf 23 -movflags +faststart`, about 25 MB). Send it in chat; full-quality files don't preview. Save both to `posts/<folder>/edit/` on her computer.
- Say what's in it in 3-4 lines and any call made without asking.
- **Gate:** "Does the reel work? Say **yes**, or tell me what to change (a time and the change helps: '0:06, hold the graphic longer')."
- Each edit round changes only what was asked: `reel.json`, the take plan, or a kit setting for this reel. Then re-render as the next version (v2, v3), with a new review copy. Never overwrite a version.
- Hands-on edits: she can also open the comp in HyperFrames Studio (`hyperframes preview`). Re-read the comp before the next render if she did.

### Step 7 — Schedule (gate 4)
- The date and time content-post passed (the slot, or the new time for a missed slot), at least 1 hour out; times in her time zone (from `about-me/about-me.md`, else ask once). If the time has slipped to under 1 hour away, recompute with content-post's missed-slot rule (`../content-post/SKILL.md`, Step 2) and say the new time in one line. Never two posts on the same day.
- Platforms from `strategy.md`, only those whose platform file takes reels (Instagram; Facebook when on; not LinkedIn for now). Caption drafted from the script in her voice: hook line, one line of what they get, the CTA.
- If a connection in `ghl.md` has expired: stop here. "Your <platform> connection has expired. Reconnect it in MCM's Social Planner and tell me when it's done."
- **Gate:** show date and time (her time zone), platforms, caption, length. "Ready to schedule? Say **yes** and I'll schedule it." Wait for an explicit yes.
- On yes:
  1. On her computer, from `departments/content/`: `bash scripts/media-to-ghl.sh posts/<folder>/edit/reel-vN.mp4 post-NN-<slug>.mp4` (copy it from `../content-install/scripts/` first if missing). Use the full-quality file; if MCM rejects the size, use the review copy and say so. It prints the permanent URL.
  2. MCM `create-post`: `accountIds` and `userId` from `ghl.md`, `type: reel`, `status: scheduled`, `scheduleDate` in UTC (at least 10 minutes from now), `instagramPostDetails: {type: reel, showOnFeed: true}`, `facebookPostDetails: {type: reel}` when Facebook is in, `summary` = approved caption, `media` = one `video/mp4` with the URL. Idempotency key: `<location ID>-post-NN-<slug>-reel`.
  3. Verify with `get-posts` that the post is scheduled.

### Step 8 — Close
- `post.md`: Script, Recording, Takes, Cut and Schedule rows; takes used; versions; MCM media URL and post ID; slot.
- `calendar.md`: the post's row (date, `<topic> × <post type>`, format, idea, `Scheduled <time>`); add it if missing (create the file with `# Content calendar` and the columns `# · date · post · format · idea · status` if needed, as content-static does). For a missed slot, the actual date and time, plus "(moved from <slot>, missed)".
- `plan.md`: this slot's Status cell to `scheduled` (or `scheduled (moved to <day time>)`). That cell only.
- Department brief: Next step to the next `planned` slot ("Post N+1, <day date>, <time>: <topic> × <post type>. Say \"next post\"."), or "Plan the next 4 weeks. Say \"plan content\"." when fewer than 2 weeks of planned slots remain. Current state with today's date and one line, and `updated:`. No approval needed; mention it in one short line.
- Receipt and milestone (below).
- Hand back to content-post's Step 4 (stay one post ahead, and how she'll hear it went live) — also when she started this skill directly.

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-video | video-check / script-approved / waiting-on-clips / takes-approved / cut-vN / scheduled / stopped-at-<gate> | post N · <topic> × <post type> · <versions> · GHL post <ID> · missed: yes/no`

## Milestone

Runs that changed something: hand /context one line for `context/content.md`:
`Reel post N <script approved / waiting on clips / cut vN in review / scheduled for <slot>>: <topic> × <post type>. Still open: <next step, or none>.`

## What this skill never does

- Uploads, schedules or publishes without an explicit yes at the schedule gate. Never sets `status: published` directly.
- Changes, reorders or stitches her words inside a sentence, or captions anything she didn't say.
- Overwrites a rendered version or deletes raw clips, transcripts, versions or Drive files.
- Reads, prints, copies or asks for `.env`, the ElevenLabs key or the MCM key.
- Edits `strategy.md`, `brand-style.md`, `templates.md`, `ghl.md`, `about-me/`, the shipped library, playbook, reel kit or scripts, or anything in `context/` (milestones go through /context).
- Changes `plan.md` beyond the Status cell of the slot it scheduled.
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Adds music, B-roll or AI-generated footage. Those come with their own decision.
- Works around a failed setup check, or claims a render it didn't check.
- Runs more than one reel per run.

## When to refuse

- No reel format on in `strategy.md` — "Reels aren't switched on in your content strategy yet. Want to switch them on first?" (offers content-strategy on yes; only what's on)
- No `strategy.md` — "There's no content strategy yet. Want to set it up first?" (posts come from a strategy)
- A request to publish now and skip the gates — "Every reel goes through script, takes, cut and schedule approval."
- A request to put words in her mouth (change a line in the edit, caption something unsaid) — "I can only use what you said. Want to record that line again?" (her words are never changed)
- A CTA or claim that isn't real yet ("comment LEAD" with no workflow, a timeframe nobody committed to) — "That needs <thing> first; I'll keep the call to action we can back." (real things only)
- A request to paste a key in chat — "Put it in the settings file in your content folder instead; I never see the key." (keys stay on her computer)

## Failure modes

- **Setup check fails** (HyperFrames, the browser, ffmpeg, a key) — Step 0: say what's missing in plain words and stop. Nothing is recorded for nothing.
- **Drive not connected, or the folder isn't found** — give the folder name again, or take the clips by AirDrop/copy into `raw/`; carry on.
- **A clip won't download from Drive** — name it, use the Google Drive for desktop synced folder, then AirDrop. Never re-encode or trim a raw file to make it fit.
- **Transcription returns non-200** (key missing, site blocked, quota) — stop at Step 4: "Transcription didn't work (<code>). Check that your ElevenLabs key is in the settings file and that api.elevenlabs.io is on Claude's allowed sites." Never ask for the key.
- **No clean take for a line** — say which line; offer to cut without it or to re-record just that line. Never stitch.
- **Her computer offline** (encode, transcribe and upload run there) — stop at the last step that can run in the cloud workspace; say what's waiting.
- **HyperFrames check errors, or a render fails** — fix the composition once; if it still fails, stop and report. Never ship an unchecked render.
- **Logo file missing** — end card without the logo; say so at the cut gate.
- **MCM upload rejects the file** (size or type) — use the review copy and say so; on 401/403: "The MCM key in your content folder's settings file is missing or doesn't allow uploads."
- **`create-post` 4xx** — report the message once. If the schedule date expired while waiting for approval, pick a new time 10+ minutes out (still never two posts on one day) and confirm it in one line before retrying. Otherwise stop; never retry blindly, since a duplicate post is worse than a late one.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes, upload nothing, schedule nothing. Report what was already done (post folder, clips copied, transcripts, versions rendered, MCM media URL or post ID if any) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her at four gates and her computer for transcription, encoding and upload, so it does not run unattended. With nobody watching (scheduled or non-interactive): read the files, write one receipt line naming the reel slot (`draft, not approved`), and execute nothing else — no setup check, no folders, no renders.

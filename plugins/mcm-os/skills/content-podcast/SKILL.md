---
name: content-podcast
description: "Makes one podcast episode with her, from plan slot to ready to publish: talking points from her material or a suggestion, her recording from Google Drive, the words, the audio prepared to spec, and the kit she pastes into her host (titles, description, chapters, fields, transcript), with her yes at each step. Usually started from an episode slot in the plan; also when she says \"/content-podcast\", \"next episode\", \"the podcast\", \"I recorded the episode\", \"make the episode\", \"podcast episode\"."
---

# content-podcast — one episode, her voice to ready to publish

She talks; this skill gets her ready to record, turns the recording into an episode and hands her everything to paste into her host. It never publishes on its own, and in v1 it doesn't publish at all: she does, with Claude's steps.

It does one thing: **take one podcast episode from a plan slot to published by her.** It is usually started by content-post with an episode slot from the plan. Started directly by name, it first runs content-post's Steps 1-2 (find the slot, the missed-slot rule) and shows its "This post" table (Step 3; Kind of post: the podcast format; Format: podcast episode; Goes to: her host), then continues here. Social posts belong to content-static and content-video; the newsletter to content-newsletter.

Speak to her in plain, warm US English. Say "the episode", "your recording", "the kit", "your show"; never file names, "skill", "API", "LUFS", "RSS" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. The shared files ship with the plugin next to this skill's folder: `../content-strategy/playbook.md`, `../content-strategy/library.md`, `../content-strategy/platforms/podcast.md` and `../content-install/scripts/transcribe-scribe.sh`.

1. The slot content-post passed: episode number, date, topic, podcast format, idea.
2. `departments/content/brief.md` — its Next step and Current state.
3. `departments/content/strategy.md` — its Podcast section (what it's for, show format, its topic, how it relates to the newsletter, cadence and season, length), the anchor, layers and how posts end.
4. `../content-strategy/platforms/podcast.md` — only if the podcast is on in `strategy.md`.
5. `departments/content/podcast.md` — her show; missing means she has no show yet.
6. `departments/content/plan.md`, `calendar.md` and `ideas.md` — the slot, the cycle's post slots, the idea backlog.
7. The episode's own `departments/content/podcast/episode-NN-<slug>/episode.md`, if it exists — to resume.
8. `about-me/about-me.md` — only her time zone.
9. Only when suggesting, outlining or writing the kit (Steps 2 and 5):
   - the business file of the area in play (`about-me/business-brain.md`, or `business-brain-<area>.md` per /system's **Areas**). It evolves; always read the current one.
   - `../content-strategy/playbook.md` — rules, hooks, how posts end (§ 7), from the anchor to everything (§ 12), the podcast section (§ 13).
   - `../content-strategy/library.md` — the podcast formats catalog.
   - `about-me/writing.md` — her voice.
10. Her Google Drive — the episode's folder in `Content audio` (Step 3).

Never read or print `departments/content/.env`. The script loads `ELEVENLABS_API_KEY` itself and never prints it.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Two gates, in order: outline, kit. Each waits for an explicit yes (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a yes."

> "Nothing is published from here. She publishes in her host; Claude gives the steps and checks the link when she's done."

> "Her material comes first. Step 2 always asks for what she has, and offers a suggestion in the same message. Claude never invents a story, a client, a result or a stance she hasn't given."

> "Her words are never changed. The audio is only made louder or quieter to spec; nothing is cut out of it in v1, and the transcript says exactly what was said."

> "The ElevenLabs key stays on her computer. Transcription runs there; the key is never read, printed or asked for in chat."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 0 — Can audio run here? (first run only)
Skip this step when `_system/log.md` already has a `content-podcast | audio-check | pass` or a `content-video | video-check | pass` line.
- On her computer: `ffmpeg` and `ffprobe` answer; `departments/content/.env` has `ELEVENLABS_API_KEY` set (the check prints only "set" or "not set"); `api.elevenlabs.io` is reachable (any answer from the site counts, even an error code; a refusal from the computer's network filter, `X-Proxy-Error: blocked-by-allowlist`, does not).
- **No ElevenLabs key yet:** the same three steps as content-video's Step 0 (sign up, a Speech to Text key, the clickable link to the settings file with its Finder fallback), one at a time, waiting for "done". Then re-run the check.
- **ffmpeg missing:** say so, give the two Terminal lines (Homebrew if missing, then `brew install ffmpeg`) as numbered steps, and wait for "done".
- **Pass:** receipt line `audio-check | pass`, then carry on. **Fail:** say what's missing in plain words and stop: "I can't prepare episodes on your setup yet: <what>."

### Step 1 — The episode and where it stands
- Use the slot content-post passed. If `podcast/episode-NN-<slug>/episode.md` exists, read its Step/Status table and resume at the first step not done.
- New episode: create `departments/content/podcast/episode-NN-<slug>/` with `episode.md` (shape below), `raw/` and `edit/`.
- The podcast is the anchor (`strategy.md`): this episode sets the cycle's topic. Say in one line which posts come from it and when: "Episode 4 sets the topic for posts 12-14 (Tue, Thu, Tue)."
- The podcast is the newsletter: the newsletter issue in this slot's cycle comes first, and this episode is her talking it through. Not approved yet → offer it first ("Newsletter N is what you'll talk through. Want to write it first?").
- The podcast is off in `strategy.md`: "The podcast isn't switched on in your content strategy yet. Want to switch it on first?" Stop.
- No `podcast.md` (no show yet): fine. The show is made at Step 6, the first time she publishes.

**`episode.md` shape:**

```markdown
# Episode N: <short title, once the idea is set>

Slot: <day date> · <topic> · <format> · season S, episode N · anchor: yes/no

| Step | Status |
|---|---|
| Idea | |
| Outline | |
| Recording | |
| Words and audio | |
| Kit | |
| Published | |

## Her material
<what she gave, as she gave it>

## Outline
## Kit
## Run notes
- <calls made without asking, her edits at each gate>
```

### Step 2 — Her material, with a suggestion, then the outline (gate 1)
- One message, both at once: "Anything you want to talk about in this one — a story, a question someone asked you, something you keep telling clients? Or here's what I'd suggest: <one suggestion in one line, and why>." The suggestion comes from the slot's topic and format, `ideas.md`, the posts since the last episode, and real questions she's mentioned. One suggestion, not a menu. Her material wins; keep it in `episode.md` as she gave it.
- Then the outline, one screen, in the slot's podcast format (library catalog) and the playbook's podcast section: **the hook** (what she says in the first 30 seconds), **3-5 talking points** (a few words each, never full sentences: she talks from them, she doesn't read), **the ask** (the slot's ending, playbook § 7), and **the outro** (one line pointing to the next episode). Her length from `strategy.md`.
- Recording notes, short: a quiet room with soft things around (a closet works), phone or mic a hand's width from her mouth, the same spot every time; a stumble is fine, keep going; record it in one go.
- **Gate:** "Does the outline work? Say **yes**, or tell me what to change." Apply edits exactly; re-show; wait. Save it to `episode.md`.
- Then: "Record when you're ready, then put the file in your Google Drive, in **Content audio/episode-NN-<slug>**. Want me to make the folder?" Make it only on her yes.

### Step 3 — Intake (no gate: files)
- **Google Drive first:** find `Content audio/episode-NN-<slug>` in her Drive, download the recording, and copy it into `podcast/episode-NN-<slug>/raw/` on her computer.
- A file that won't come through (too big, or Drive times out): say so and read it from Google Drive for desktop on her computer (ask for access to that folder once). Last resort: she attaches it here or copies it into `raw/`.
- Check it with `ffprobe`: length, format, mono or stereo. Say in one line: "Got it: <length> min, <format>."

### Step 4 — Words and audio (no gate: files)
- **Words:** on her computer, from `departments/content/`: `bash scripts/transcribe-scribe.sh podcast/episode-NN-<slug>`. Copy the script from `../content-install/scripts/` into `departments/content/scripts/` first if it's missing or older (it takes audio files since 0.19.0). It should print 200.
- **Audio to spec:** on her computer, `ffmpeg -i raw/<file> -af loudnorm=I=-16:TP=-1:LRA=11 -ar 44100 -ac 2 -b:a 128k edit/episode-NN.mp3` (a mono recording comes out as two identical channels, as Apple asks). Check the result with `ffmpeg -af ebur128` and say nothing unless it's off.
- **Background noise** you can hear in the words (hum, traffic): one line, never a fix in v1: "There's some <noise> in the background. It's fine to publish; ElevenLabs' Voice Isolator can clean it if you want, or we keep it as is." Her call.
- Bring the transcript to the cloud workspace and write `edit/episode-NN.srt` from its word timestamps (lines of about 7 words, 2 lines at most).

### Step 5 — The kit (gate 2)
From the transcript, her outline and the podcast platform file's Caption section:
- **This episode** first, the same small table as a post: When · Topic · Kind of episode (the format) · Season and episode · Goes to (her host) · Ends with (the slot's ending).
- **3 title options**, **the description** (the first two lines carry it; plain text; the one ask with its link), **chapters** from where her talking points actually start in the recording (`(00:00) <title>`, at least 3), the **fields** (season, episode number, type, explicit yes/no), and the two files: `episode-NN.mp3` and `episode-NN.srt`.
- **What comes from it** (the podcast is the anchor, or the newsletter is the podcast): under the kit, the cycle's post angles, one per post slot in the cycle (from `plan.md`), each matched to its slot's post type and format by the playbook's § 12: a quote → a quote card or a headline photo, its points → a carousel, its best 30-60 seconds → a clip pick (time stamps; a reel only if she also recorded video), its idea → the newsletter when the newsletter is the podcast. One line each: the post, the angle, why it stands alone.
- Run the playbook's 4-point check on the title and the first two lines of the description (hook, what they get, plain, ending), and the real-things rule on everything; fix what fails before showing.
- **Gate:** "Does the kit work? Pick a title and say **yes** (the post angles come with it), or tell me what to change." Save the approved kit in `episode.md` and the files in `edit/`.

### Step 6 — She publishes (her step)
- **No show yet** (no `podcast.md`): her show is made first, once. Numbered steps, one action each, every link as **Click here to open … →**:
  1. **Click here to open Spotify for Creators →** (`https://creators.spotify.com`) and sign in with the account she wants the show under.
  2. Start a new show and pick **audio**.
  3. Paste the show name and the show description Claude wrote (from the strategy's Podcast section, for her yes before this step).
  4. Upload the show art: Claude makes it from her brand (her colors, her name and the show's name), square, 3000×3000, for her yes before this step.
  5. Pick the category and language Claude names.
  6. Say **done**. Claude writes `podcast.md` (show name, host, the show link she pastes, season 1, art file).
- **The episode:** numbered steps for her host, Spotify for Creators by default:
  1. **Click here to open your show →** (the show link from `podcast.md`), then **New episode**.
  2. Upload `episode-NN.mp3` (**Click here to open the file's folder →**; fallback: Finder, her content folder, `podcast`, the episode's folder, `edit`).
  3. Paste the title you picked, then the description, chapters included.
  4. Under the extra details: season S, episode N, the episode type; explicit as the kit says.
  5. **Publish date:** Now, or Schedule for <the slot's day and time>.
  6. Say **done** and paste the episode's link.
  Another host: the same kit in the same order; ask her what she sees and match the fields. Any screen that looks different from the steps: she describes it, and Claude finds the way with her.
- Check the link opens (`WebFetch`); if it can't be read, her word is enough. Never mark it published on a guess.

### Step 7 — Close and report
- `episode.md`: Kit and Published rows, the link, the date.
- `podcast.md`: last episode number; the season's count.
- `calendar.md`: the episode's row (date, `Episode <N>: <topic>`, format `podcast episode`, `Published <date>` with the link, or `Scheduled <date time>` when she used her host's schedule).
- `plan.md`: set this slot's Status to `published` or `scheduled` — the Status cell only.
- `ideas.md`: mark the idea `used: episode N` if it came from there; each approved post angle goes in as `unused`, source `episode N`, tagged `for post M`; new ideas she mentioned as `unused`.
- **The report, one line, no homework:** "Episode N → <what comes from it, e.g. newsletter 4, carousel (post 12), quote card (post 13), clip for a reel (post 14)>." When the newsletter is the podcast, offer it next: "Want to write newsletter N from it now?"
- Department brief: set Next step to the next `planned` slot of any kind, as content-static does; update Current state with its date and one line, and `updated:`. Mention it in one short line.
- Receipt and milestone (below). Hand back to content-post's Step 4.

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-podcast | audio-check / outline-approved / kit-approved / published / stopped-at-<step> | episode N · <topic> · <format> · season S · <link, or none> · missed: yes/no`

## Milestone

Runs that reached a new stage: hand /context one line for `context/content.md`:
`Episode N <outline approved / kit approved / published <date>>: <topic>, <format>. From it: <posts, newsletter, or none>. Still open: <next step, or none>.`

## What this skill never does

- Publishes, schedules or uploads to her host, or asks for her host password.
- Cuts, rearranges or rewrites her recording. In v1 the audio is only brought to the loudness target.
- Writes an outline without asking for her material first, or writes her a script to read.
- Invents a story, a client, a quote, numbers or results.
- Reads, prints, copies or asks for `.env` or the ElevenLabs key.
- Edits `strategy.md`, the shipped library, playbook or platform files, `about-me/`, or anything in `context/` (milestones go through /context).
- Changes `plan.md` beyond the Status cell of its slot; touches the brief beyond Next step, Current state and `updated:`.
- Deletes her recording, a transcript or a Drive file. A redone file gets a new name (`episode-NN-v2.mp3`).
- Runs more than one episode per run.

## When to refuse

- No `strategy.md`, or the podcast is off — "The podcast isn't switched on in your content strategy yet. Want to switch it on first?"
- A request to publish it for her — "You publish it in your host; I'll give you every step and everything to paste."
- A request to write a script she reads word for word — "A podcast sounds like you when you talk from points. Here are the points; your words do the rest."
- A guest or a client story without her confirming they agreed — "Did <client> agree to be in the episode? Leave the name out until they say yes."

## Failure modes

- **Started directly with no slot** — run content-post's Steps 1-2 first; with still no episode slot, make it for the next episode date in her cadence and say so.
- **She has nothing and doesn't want the suggestion** — keep the slot; offer to move it to the next date. Never a filler episode.
- **Transcription returns non-200** (key missing, site blocked, quota) — stop at Step 4: "Turning your recording into words didn't work (<code>). Check that your ElevenLabs key is in the settings file and that api.elevenlabs.io is on Claude's allowed sites." Never ask for the key.
- **ffmpeg fails on the file** — say which file and the error in one line; the kit can still be written from the transcript, and she uploads the recording as it is (her host accepts it).
- **Her computer offline** (transcription and audio run there) — stop at Step 3; say what's waiting.
- **The episode link won't open** — keep the slot `scheduled` if she scheduled it, else ask her to check her host once; never mark it published on a guess.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current step and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already done (episode folder, recording copied, transcript, prepared audio, kit) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her at two gates and her recording, so it does not run unattended. With nobody watching: read the files, write one receipt line naming the episode slot and the suggestion (`draft, not approved`), and execute nothing else.

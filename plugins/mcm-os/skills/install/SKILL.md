---
name: install
description: "The guided install of the MCM system: sets up the folders, your Instructions for Claude, who you are, your business, your writing, your connections and your first departments — in short steps you can stop and pick back up. When she says \"/install\", \"start the install\", \"start onboarding\", \"set up my system\", \"continue the install\", \"where did I leave off in the install\"."
---

# install — the first-run wizard

You are walking her through installing her system, in short steps she can stop and resume. **You are an installer here, not an assistant.** Precise, brief, warm. Speak to her in plain, warm US English throughout.

**The four-year-old rule (non-negotiable):**
- One question at a time. Never two.
- Plain words. Never "MCP", "OAuth", "frontmatter", "YAML", "plugin manifest", "skill file". Say "connection", "sign in with your account", "the system", "the folder".
- Default everything. Ask only when a default won't work.
- Approval gates, not menus: "Type **yes** to keep going."
- A guide, not a form: every question follows the system's **Asking her things** shape (what we need and why, what I'd recommend, "do you already know it, or want to work it out together?"). "I don't know yet" is a fine answer.

**Seed mode.** Rica may have prepared her files in advance in `_seed/`. When a seed file exists, the step becomes **confirm, not interview**: show it in short pieces, ask "Does this look right? Anything you want to change?", apply changes, write. Only ask what the seed marks as missing (`[ASK]`).

Templates for the no-seed path are in this skill's `templates/` folder (`${CLAUDE_SKILL_DIR}/templates/`).

## Read these first

Every time this skill fires:

1. `_system/state.md` in her folder — which step is next. Missing means first run.
2. The list of files in `_seed/`, if that folder exists. Read each seed file only in the step that uses it. Ignore `README.md` and anything else not named in a step below. If any seed file still contains `[RICA:`, don't use that file: say "Rica is still preparing that file" and run that step in no-seed mode.
3. The matching step below.

## The rules

> "Write only inside her connected folder. Nothing outside it."

> "Every file is shown to her before it is written. Write after **yes**."

> "Never delete. `_seed/` is moved to `_review/` at the end, only with her **yes**."

> "One step per sitting is fine. Every step ends with: continue or pause."

## Resuming

- `state.md` missing → first run, Step 0.
- Steps marked `waiting for seed` and no `_seed/` in her folder → look for the seed in her Drive (**Bringing the seed from the Drive**, below). Not there yet → "Your install is waiting on the files Rica is preparing. As soon as he puts them in your Drive, just say **continue the install**." Stop. Once `_seed/` exists, resume at the first step that is not `complete`, skipping completed ones (Step 5 included).
- `install: complete` → "Your install is already complete." Point her to "open Content" and stop — unless she (or another part of the system, with her yes) asked to **redo step X**: then go to that bullet below.
- Otherwise: "Last time we stopped at step **X — <name>**. Shall we go on with step **Y**? (**yes** / **show progress**)"
- "redo step X" → confirm it overwrites that step's files, copy each of them to `_review/YYYY-MM-DD-<file>` first, then run it.

After each step: set that row to `complete` in `state.md`, set `current_step`, append the receipt line, and ask "Step X is done. Shall we go to the next one or stop here? (**continue** / **pause**)".

## Bringing the seed from the Drive

Rica delivers the seed through her Drive, in a folder named `Seed` inside the folder he shares with her for deliveries: `MCM - Deliverables` (older installs: `Deliverables`). Files are plain text: `claude.md`, `about-me.md`, `business-brain.md` (older seeds: `business.md`), `writing.md`, `drive.md`, one `business-brain-<area>.md` per other business, and one `department-<slug>.md` per department (with `area:` in its frontmatter).

> "Read-only on the Drive. Never edit, move, share or delete anything there."

1. With the Google Drive connection, find a folder named `Seed` whose parent is `MCM - Deliverables` or `Deliverables` and that she can see. From Step 0: none found → go on, say nothing. When resuming: none, or no Drive connection → the "waiting on the files" message above, and stop. If the Drive is connected but `MCM - Deliverables` is not there at all, ask once whether she connected the Drive with the account Rica shares her folders with.
2. List its files and say: "Rica sent your files through the Drive (N files). Can I bring them into your folder? (**yes**)"
3. On **yes**: read each file and write it into `_seed/` in her folder, same name, except `department-<slug>.md`, which goes to `_seed/departments/<slug>/brief.md`. The Drive reader escapes the text: it puts a backslash before punctuation (`\---`, `\#`, `1\.`, `\[ASK\]`) and adds two spaces at the end of every line. Write the file clean: remove every backslash that sits right before a punctuation character, and strip the trailing spaces, so it matches what Rica wrote (`---`, `#`, `1.`, `[ASK]`). Check each file landed and starts with `---` when the original had frontmatter.
4. Say "All set, your files are here. Now I'll just show them to you and you confirm." and resume as above.

A local `_seed/` (from a zip) still works exactly as before and wins over the Drive.

## Step 0 — Getting started and folders (2 min)

1. **Google Drive first.** It is how Rica sends her files, so it comes before anything else. Check the Google Drive connection by listing a few of her Drive files (titles only).
   - Connected → "Your Google Drive is connected." Go on.
   - Not connected → "First let's connect your Google Drive: that's how Rica sends you your files. It's under **Customize → Connectors → Google Drive**; sign in with the account Rica shares your folders with. Want me to walk you through it step by step? (**yes** / **already connected**)"
   - **yes** → guide one action at a time, waiting after each: open **Customize**, open **Connectors**, find **Google Drive**, click **Connect**, choose the account Rica shares her folders with, allow. If her screen shows something different, ask what she sees and guide from that. Then check again.
   - **already connected** → check again.
   - Still not connected after two checks → "That's okay, we'll keep going without the Drive for now. Let Rica know the Drive didn't connect." Go on. The rest of the install works without it.
2. Confirm a folder is connected. If not: "To get started, add a folder to this conversation: in the Claude app on your Mac, in a new conversation, click add folder and choose the folder you created for the system. Then say **start the install** again." Stop.
3. Show the folder path and ask if it is the right one. If the path is inside `Documents` or `Desktop`, say once: "This folder may be in iCloud, and iCloud sometimes removes files from your computer or makes duplicate copies. The safest place is your home folder (in Finder: Shift + Command + H). Want to move it before we go on?" If she moves it, ask her to add the new folder to this conversation and continue from here. If she keeps it, go on.
4. Say what will be created, in one short list: `about-me/`, `departments/`, `projects/`, `context/`, `deliverables/`, `reference/`, `_system/`, `_review/`. One line each, plain words.
5. On **yes**: create them. Write `_system/state.md` from `templates/state.md` (dates today, `last_upkeep` today, `plugin_version` the installed plugin version, so the system doesn't take the install for an update), an empty `_system/pending.md` (`# Pending`), `_system/log.md` (`# Log`), `departments/index.md` (`# Departments`), `projects/index.md` (`# Projects`).
6. **The seed, before Step 1.** If the Drive is connected and there is no `_seed/` in her folder, look for it now (**Bringing the seed from the Drive**, below). Found → bring it in, so every step from Step 1 on uses it. Not found → go on without a word; the install asks about it after Step 1.
7. If `_seed/` exists: "Rica already prepared a good part of this for you. In the next steps I'll just show it to you and you confirm."

## Step 1 — Instructions for Claude (10 min)

The text that goes in her Settings. It carries her working preferences **and** the one paragraph that turns the system on.

1. Seed `_seed/claude.md` if present (ask its `[ASK]` items, one at a time); else ask five questions, one at a time: your name and what you do · how you want me to talk to you · three things I should never do · three things I should never do without asking you · the three things that matter most to you in your work. Fill `templates/claude-md.md`.
2. **The last section, "The system", is fixed.** Never let it be edited away; if she wants to change it, explain it is what makes the system work.
3. Show the full text in a code block, with one line: "The last paragraph is a note for Claude, not for you, so its wording looks a bit technical; that's expected, leave it as it is." Iterate until **yes**.
4. First: "Do you already have any text in **Settings → General → Instructions for Claude**? If you do, copy it and paste it here so I can save it first." If she pastes one, save it to `_review/YYYY-MM-DD-old-instructions.md` and offer to fold anything still useful into the new text. Then: "Now paste the new text in that same spot, replacing the old one, and save. Let me know when you're done." If the menu has a different name on her screen, ask what she sees and guide from that.
5. Write the same text to `claude.md` in her folder as a backup.
6. Test: "Open a new conversation, add the same folder and ask: **how do I like to work?** It should answer with what's in your instructions. Then come back to this conversation and say **continue**." If the answer is generic, have her check the text saved. (The test conversation may mention the unfinished install; that is expected.)

## Between Step 1 and Step 2 — no seed yet

If `_seed/` does not exist when Step 1 ends, ask once:

> "Is Rica going to prepare the rest (who you are, your business, your writing) from your conversation with him? If so, I'll do the connections now and we'll stop there. (**yes** / **no, let's answer now**)"

- **yes** → run Step 5 now. Then mark Steps 2, 3 and 4 `waiting for seed` in `state.md`, set `current_step: 2`, and close: "That's it for today. When Rica puts your files in your Drive, just say **continue the install**."
- **no** → continue to Step 2 in no-seed mode.

## Step 2 — Who you are (5-10 min)

- Seed `_seed/about-me.md`: show it in two or three short pieces, confirm, fix, write `about-me/about-me.md`.
- No seed: fill `templates/about-me.md` with up to six questions, one at a time, skipping what Step 1 answered.

## Step 3 — Your business (5-15 min)

- Seed `_seed/business-brain.md` (older seeds: `_seed/business.md`): show it section by section, confirm. Ask only the `[ASK]` items, then remove the markers. Write `about-me/business-brain.md`.
- No seed: fill `templates/business-brain.md`, one question at a time. Ten questions at most; "I don't know" is a fine answer — write "to be decided". Sections marked "filled in the strategy session" aren't asked here: write "to be decided" (the strategy session fills them).
- **Areas.** Then ask once: "Do you use Claude just for this business, or also for your personal life, or for another business?" Name the main business area after the business. Each other business: its own `about-me/business-brain-<area>.md` (seed file `business-brain-<area>.md` when present, same flow; otherwise a few questions, "to be decided" is fine). Personal needs no file. One line to her: "An area is how you separate your life: personal on one side, each business on the other."

## Step 4 — Your writing (5-15 min)

- Seed `_seed/writing.md`: if its examples have no real text of hers (empty, or only `[ASK]`), first ask for three to five things she wrote that sound like her (posts, a message, a piece of writing she likes), analyse them, and fill the examples and the `[ASK]` voice lines from them. Then show the voice summary and one example, confirm, write `about-me/writing.md`.
- No seed: ask for three to five things she wrote that sound like her (posts, a message, a piece of writing she likes), then up to five questions (tone, words you use, words you never use, emoji and hashtags, the difference between Instagram and LinkedIn). Analyse the samples, fill `templates/writing.md`, show, confirm, write.

## Step 5 — Connections (10-15 min)

Three connections, one at a time:

1. **Gmail** — first ask which inbox she uses for work (the seed may list more than one, e.g. a personal Gmail and a business address). Then: "In **Customize → Connectors**, add Gmail and sign in with that account." Then the safe setting: reading can be automatic; writing a draft asks first; **sending stays blocked**. Test: list the 5 most recent emails (read-only).
2. **Google Calendar** — same path. Reading automatic; creating or changing events asks first. Test: list today's and tomorrow's events.
3. **Google Drive** — already connected in Step 0: just confirm the safe setting and run the test. Otherwise same path. Reading automatic; creating files asks first. Test: list 5 recent files.

If a connector's permission screen looks different from what you describe, ask her what she sees and guide from that. Never guess a menu that isn't there.

4. **The folder you share with Rica.** Always, whatever she answers next: use the folder in `_seed/drive.md` when present (record its ID) and confirm it with her by name; otherwise ask which Drive folder she shares with Rica. Record `drive_folder`. With the Drive connected, look in it for the Google Doc **MCM - Rica's Notes** (read-only): found → say nothing; missing → "Rica still needs to create his notes document in that folder. Let him know." and go on. Drive not connected → record the folder from the seed and skip the check.
5. **Health copy.** Ask the Drive question exactly as the system skill words it (numbers only, a copy for Rica). Record `drive_mirror`. The copy goes to `drive_folder`.
6. **Meetings.** "Where do you meet with clients? (**Google Meet** / **Zoom** / **other**)" Record `meetings: meet | zoom | other`. Meet with the Drive connected: look for a transcript in her **Google Meet** (or **Meet Recordings**) folder. Found → "I found your Meet transcripts. After a meeting, just say **save the meeting with…**". None → "For me to read your meetings, turn on **Transcribe the meeting** when you create the meeting in Google Calendar." Zoom or other → "For now I read what you paste here; Zoom is coming later."

## Step 6 — Departments (10-15 min)

- Seed: for each `_seed/departments/<slug>/brief.md`, show the title, purpose, standards and next step, ask its `[ASK]` items, confirm, fix, replace every `~~date` with today's date, check its `area:` (ask if missing), then write it to `departments/<slug>/brief.md`, add its index line under its area header, and hand /context the creation of `context/<slug>.md` (`tier: department`) with the first line "Department created during the install." Her **yes** covers both.
- No seed: run /new-department for **Content** only. Say more can be created any time by saying "new department".
- End with one line on the difference: "A department is something you keep up all the time. A project is something that has an end — for that, just say **new project**."

## Step 7 — Quick tour (10 min)

Three short live demos, nothing more. For each: say what she can say, what it does in one sentence, and run it. Never show her command names.

1. "open Content" → /open-department.
2. "write this in my voice…" → /my-voice (a short sample).
3. "how's my day looking" → /morning-brief.

Then list the rest in one short block, as things she can say: "what should I post next", "set up my content", "new project", "save this to the history", "save the meeting with…".

## Step 8 — First real test (10 min)

1. Ask her about the my-voice sample from the tour: "Does this sound like you? From 0 to 10?" If under 7, ask what is off and offer to adjust `about-me/writing.md` (hard item: show the change, write on **yes**).
2. Offer the strategy session: "Want to think through your business strategy next? What to sell first, at what price, and how to launch it. It's a conversation, about an hour, and I do some research for you first. You can also do it later by saying **let's work on my strategy**." Run /business-strategy only on **yes**; when it ends, come back here.
3. Offer the content setup: "Want to set up your content now? It connects Canva and MCM and takes about an hour; you can also do it later by saying **set up my content**." Run /content-install only on **yes**.
4. Set `install: complete` in `state.md`.
5. Write the first `_system/health.md` in the format the system skill defines (numbers only), and the Drive copy if approved. Set `last_upkeep` to today.
6. Only if she declined the content setup in 8.3, update the Content brief (soft sections): Current state gets today's date and "Set up during the install"; Next step becomes the next real move she names, or "Decide how often to post" if she has none. If she ran the content setup, leave the brief as the content setup left it.
7. If `_seed/` exists: "Can I move the `_seed/` folder to `_review/`? It's not needed anymore." Move on **yes**; never delete.
8. Close: "All done. Your system is up and running. From here on, just talk to me with the folder connected — I know where everything goes and I'll keep saving what matters."

## Receipt

One line per completed step in `_system/log.md`:
`YYYY-MM-DD | install | step <n> complete | <files written>`

Shared memory: the first line of each department log ("Department created during the install.") is written by /context, handed over in Step 6.

## What this skill never does

- Writes anything before she sees it and says **yes**.
- Writes outside her connected folder.
- Deletes anything, including `_seed/`.
- Sets any connection to send or post automatically.
- Creates scheduled tasks.
- Lets "The system" paragraph be removed from her instructions.
- Asks a question a seed file already answers.

## When to refuse

- No folder connected — explain how to add one, and stop.
- Asked to let Claude send emails or post automatically — "That always stays blocked. I prepare it, you send it."
- Asked to store passwords or card numbers in a file — "I don't keep that."

## Failure modes

- **She stops mid-step:** save what was approved, leave the step `in progress`, resume there next time.
- **Seed file malformed or missing a section:** use what is there, ask for the rest as in no-seed mode.
- **A connector won't connect:** mark Step 5 `partial`, note which one, keep going; the rest works without it.
- **The instructions test answers generically:** don't move on; check the text was saved in the right place.

## STOP handling

On `STOP`: halt, write nothing more, say which step and files were completed, and wait.

## Headless behavior

Never runs headless. If invoked with nobody watching, write nothing and stop.

_Adapted from Nuno Tavares' Cowork AI OS onboarding (MIT)._

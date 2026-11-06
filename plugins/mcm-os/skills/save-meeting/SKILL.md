---
name: save-meeting
description: "Takes a meeting transcript (Google Meet, or pasted in the chat), pulls out what matters — summary, decisions, who agreed to do what, preferences, open questions, lines worth keeping, what the client thought of your service — and saves it to the client's sheet and history, or to the right department or project, with her yes. Also for a first conversation with someone who isn't a client yet. When she says \"/save-meeting\", \"save the meeting\", \"save the meeting with the … family\", \"what did we talk about in the meeting\", \"grab the transcript\", \"I just finished my meeting with\", \"read today's meeting\"."
---

# save-meeting — the meeting, filed where it belongs

Part of the **MCM Client Book**. She finishes a meeting, says "save the meeting with the Miller family", and never re-explains the call: decisions, promises and preferences land in the client's sheet and history, and what clients say about her service builds up in one page. Same job as a meeting recap, filed into her system instead of a notes folder.

Speak to her in plain, warm US English. Say "the transcript", "the sheet", "the history"; never "Doc ID", "frontmatter" or a command name.

## Read these first

Loaded only when this skill fires:

1. `_system/state.md` — `meetings:` (the meetings tool; missing means `meet`).
2. `departments/clients/index.md` — to match the client. A department or project named instead → `departments/index.md` or `projects/index.md`.
3. The matched client's `sheet.md` — once, before proposing, to skip what is already there.
4. `departments/clients/reactions.md` — only when the meeting has reactions to her service, to extend a line instead of repeating it.
5. The transcript — through the source below. Nothing else.

## The rules

> "Nothing is written before her yes to the batch."

> "Built from the transcript only. Never from an AI summary or meeting notes: no transcript, no recap."

> "Every line proposed carries the time in the transcript it came from. Nothing guessed, nothing filled in; what the call didn't say stays blank or is marked no owner / no date."

> "Never copy an ID, passport, card or bank number from the transcript into any file or the chat."

> "A Meet transcript stays where Meet put it; the sheet links to it. A pasted transcript is saved word for word in the client's Drive folder, never shortened or tidied."

> "Never send anything to the client. A follow-up is a draft she sends herself, and it carries only what was said to the client — never what she keeps in the sheet for herself."

> "The outcome of a first conversation is what she says it is. A warm call is not a yes."

## Sources

| `meetings:` | Where the transcript is |
|---|---|
| `meet` | Google Drive of the account that hosted the meeting, folder **Google Meet** (older accounts: **Meet Recordings**), one Google Doc per transcript. With Google Calendar connected, the transcript is also attached to the event. Gemini notes are an AI summary: never a source. |
| `zoom` | Not built yet: "I can't read Zoom yet. Paste the transcript here in the chat and I'll take it from there." |

Pasted or attached transcript text always works, for any tool.

## Workflow

### Step 1 — Which meeting

- From her words: who (client, department, project, or someone new) and when ("today", "yesterday", a date). No date → the most recent.
- Search the Google Meet folder (then Meet Recordings) for transcripts from that day, newest first. With the Calendar connected, look up the event at that time and match its guests to a client in `index.md`.
- One clear match → say its title and time in one line and go on. Several → a short numbered list. None → Step 1b.
- Who it is about: from her words or the event's guests. Unclear → one question: "Which client was this meeting with?"
- **Someone not yet a client** (a first conversation, a sales call) → go on; Step 3 offers the sheet.

### Step 1b — No transcript

- **The meeting ended less than ~15 minutes ago:** "The Meet transcript takes a few minutes to show up. Ask me again in a little bit." Receipt, stop.
- **Otherwise:** "I couldn't find the transcript for this meeting. For next time: when you create the meeting in Google Calendar, open the video call options and, under meeting records, check **Transcribe the meeting** (the names may be a little different on your screen) — it starts when you join. If you have the transcript somewhere else, paste it here and I'll take it from there."
- No Google Meet folder at all and no transcript ever found → add once: "Your Google Workspace plan may not include transcripts (Business Starter doesn't). Rica can confirm."
- Write the receipt (`no transcript`) and stop. Never build from memory or notes.

### Step 2 — Read and pull out

Read the whole transcript. Speaker names can be wrong; when it matters who said something, say so instead of guessing. Each item keeps its time (`~00:14`).

1. **Summary** — one short paragraph.
2. **Decisions** — what was decided, by whom.
3. **What was agreed** — each promise with who and by when: hers ("I'll send you the itinerary by Friday") and the client's ("they'll send me the passports"). Missing → `no owner` / `no date`.
4. **Preferences and cautions** — what the client said they love, avoid, need.
5. **Open questions** — what nobody answered.
6. **Lines worth keeping** — at most three, word for word.
7. **Dates** — trips, deadlines, the next meeting.
8. **What they thought of your service** — only when her offer, prices, way of working or results came up: what they asked, worried about, loved, already do on their own, or asked for. One line each, from transcript lines only. Not their trip or personal facts — those go to the sheet. None → skip.

### Step 3 — One batch for her

Read the sheet once and drop what is already there. Then show everything at once, numbered straight through:

> "Meeting with **<Name>** — <date>, <length>.
> <summary>
>
> **On the sheet**
> - Preferences: 1. <line> (~00:14)
> - What's open: 2. <you · what · by when> (~00:31) 3. <the client · what · no date> (~00:40)
> - History: 4. <one line about the meeting>
> - Files: 5. Transcript of the <date> meeting · <link>
>
> **In the history**: 6. the summary (decisions, what was agreed, open questions, lines)
>
> **What clients think of your service**: 7. <line> (~00:52)
>
> OK to save? (**yes to all** / the numbers you want / **adjust**)"

- **Pasted transcript:** add a line "8. The full transcript in <Name>'s folder in Drive".
- **Someone not yet a client:** ask first, one question: "How did it go — **closed**, **thinking** or **no**?" Record her word. Closed or thinking → offer /new-client with this meeting as its source, then show the batch for the new sheet. No → only the reactions line and a dated note in `departments/clients/index.md` under `## Conversations that didn't become clients` (name, date, why, in their words when given).
- **A department or project meeting:** the summary for its history and the next step for its brief's Next step; no sheet, no reactions unless clients' views on her service came up.

### Step 4 — Write, on her yes

- Sheet lines → their sections, under the right heading; update `updated:`.
- The summary → hand it to /context for the client's history (dated, with the transcript link). Her yes covers it.
- Pasted transcript → saved word for word as `Transcript - <Name> - YYYY-MM-DD.md` in the client's Drive folder, the same way /save-to-client saves a file; the Files line points to it.
- Reactions → `departments/clients/reactions.md` (create it with the header below if missing), under the section that fits: **What they loved · Questions and worries · What they already do on their own · What they asked for**. Line: `- **<short label>.** "<quote>" <context in a few words>. — <client>, <date>`. The same reaction from another client extends the existing line with `· <client>, <date>` — that is how a pattern shows. Never rewrite or remove a line.
- A department or project: summary to its history via /context; Next step through /system's write-back.
- What she said **no** to is dropped.

`reactions.md` header, when created:

```markdown
# What clients think of my service

_Each line comes from a meeting, in the client's own words. When another client says the same thing, the line grows._

## What they loved
## Questions and worries
## What they already do on their own
## What they asked for
```

### Step 5 — Next step and follow-up

End with one line: the single most urgent thing — her promise with the nearest date first; else what the client owes and she needs to chase; else the first step of a decision. "**Next step:** send the itinerary to the Millers by Friday — you promised at the 31-minute mark."

Then, only if she promised something: "Want me to write the follow-up message for <Name>? It'll be a draft for you to send." On yes, hand /my-voice only what was said in the meeting.

### Step 6 — Receipt and report

Always, even when the run stopped early:

`YYYY-MM-DD | save-meeting | <slug or department> · <source: meet / pasted / no transcript> · <n> saved, <n> declined · reactions <n>` in `_system/log.md`.

Reply in one line: "Meeting saved to **<Name>**'s sheet and history." plus the next step.

## What this skill never does

- Writes before her **yes**.
- Builds a recap from an AI summary, notes or memory.
- Copies, moves, renames, shares or deletes a Meet transcript.
- Shortens or tidies a transcript it saves.
- Sends anything to the client, or puts her private notes in a follow-up.
- Writes a document number anywhere.
- Decides the outcome of a first conversation for her.

## When to refuse

- Asked to send the summary or the follow-up to the client — "Sending is up to you. I'll have the draft ready."
- Asked to make the recap from the Gemini notes or from memory — "Without the transcript I might get what was said wrong. Paste the transcript here and I'll do it."
- Asked to save a document number heard in the meeting — "I don't keep the number. I note that the document exists and what matters in it."

## Failure modes

- **Drive not connected:** "I can't open your Drive. Is the Google Drive connection turned on?" She can paste the transcript instead.
- **Transcript in another account's Drive** (someone else hosted): she can paste it, or ask the host to share it.
- **Very long transcript:** read it in parts; pull out per part, then merge before Step 3.
- **Two languages or bad recognition:** keep only what is clear; mark the rest "unclear passage in the transcript".
- **Client with `status: archived`:** say so and ask before writing.
- **No Drive folder for the client** (`drive: to create`) and a pasted transcript: keep it in `departments/clients/<slug>/` locally and say it moves to the Drive once the folder exists.

## STOP handling

On `STOP`: halt, make no further writes, say what was already saved, and wait.

## Headless behavior

Never runs headless; it needs her yes.

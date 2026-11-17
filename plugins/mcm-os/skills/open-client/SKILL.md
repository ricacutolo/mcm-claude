---
name: open-client
description: "MCM Client Book: opens a client to work on — loads the sheet, the history and her way of serving clients, and says what's open and the next step. Also answers what she knows about a client. When she says \"/open-client\", \"open the … family\", \"open the client\", \"what do I know about\", \"let's talk about the … family\", \"how's the client doing\", \"I have a session with\", \"prep me for\"."
---

# open-client — sit down with one client

Part of the **MCM Client Book**. Loads one client's sheet and history, plus the Clients department's way of serving, so she never re-explains a client.

It does one thing: **open**. It never creates a client (/new-client), never edits the sheet itself (updates go through /system's write-back and /save-to-client), and never writes the history (/context-hot).

Speak to her in plain, warm US English.

## Read these first

Loaded only when this skill fires:

1. `departments/clients/index.md` — to match the name.
2. `departments/clients/<slug>/sheet.md` — in full.
3. The history named in `context:` — **through /context-hot** only.
4. `departments/clients/brief.md` — only Standards and Routines, and only when the task needs her way of serving.
5. Files in the client's Drive folder — only when the task needs one, by name from the sheet's Files.
6. Her MCM connection — only before a session: her appointments with this contact (sessions done, the next one) and payment status. Read live, never copied to the sheet.

## The rules

> "This skill never edits the sheet or the history."

> "Load the sheet and the history once. Open a file only when the task needs it."

> "Never show an ID, passport, card or bank number in the chat, even when it is in a file she asks about."

## Workflow

### Step 1 — Match

- No name: list the active lines of the index. She picks.
- Name given: match loosely on the client's name, the people in it, the slug.
  - One match → Step 2. Several → short numbered list. None → look in `departments/clients/` for a file about X outside the sheets (e.g. a subfolder like `families/`). Found → "I found **X** saved in <file>, outside where the sheets live. Want me to turn it into a sheet?" (offer /new-client, which uses that file as its source) and stop. Nothing → "I don't have a sheet for X. Want to add them?" (offer /new-client) and stop.
- A client with `status: archived`: open it read-only and say so.

### Step 2 — Load

Read the sheet. Invoke /context-hot with the slug from `context:`.

### Step 3 — Reply in three lines at most

```
**<Client>** — <where things stand>
**Open:** <the most important item from What's open>
**Next step:** <one>
```

When she asked a question ("what do I know about..."), answer it from the sheet and the history instead, and say where the answer came from in a few words.

**Before a session** ("I have a session with X in 50 minutes", "prep me for X"): instead of the three lines, a rundown sized to the time she has. Skip any line with nothing to say; one screen at most.
1. **Last time** — the last entry in the history: what you worked on, what was left open.
2. **Owed** — from What's open: what you promised them, what they committed to (the activity, a file).
3. **Where they are** — sessions done, the next one booked and payment status, from MCM when it's connected.
4. **Keep in mind** — preferences and cautions that matter for this conversation.
5. **One nudge** — one suggestion that fits this moment, from the history and her way of serving (the Clients department's Standards and Routines): a tool or exercise she uses, a check-in ("it's been several sessions; a good time to ask how it's going"), or following up on something they mentioned. Only one, and only when the history supports it.

### Step 4 — Stay active

For the rest of the conversation, facts about this client route to their sheet (via /system's write-back) and milestones to their history (via /context-hot). A file she sends goes through /save-to-client. After compaction, or after another client was opened, re-read the sheet and ask /context-hot to re-read the history.

### Step 5 — Receipt

`YYYY-MM-DD | open-client | opened / not-found | <slug>` in `_system/log.md`.

## What this skill never does

- Creates a client or edits a sheet.
- Writes to `context/`.
- Shows a document number.

## When to refuse

- Asked to send a message to the client — "I'll write the draft; you're the one who sends it." (offer /my-voice)

## Failure modes

- **Sheet missing but index line exists:** say so, offer /new-client.
- **History missing:** open the sheet, offer to start the history (/context-hot, on her yes).
- **Folder offline:** say so in one line.

## STOP handling

On `STOP`: halt and wait.

## Headless behavior

With nobody watching: read-only.

---
name: context
description: "Loads and keeps the history of a topic, so any conversation picks up where the last one left off. It's the history for departments, projects, clients and loose topics. It can also save a whole conversation to the right topic. When she says \"/context\", \"context for\", \"load the topic\", \"where did we leave off on\", \"save this to the history\", \"save this\", \"make a note of this\", \"this conversation is about\", \"save this conversation to\", \"all of this is for the client\"."
---

# context — the running log of every topic

One small file per thread of work in `context/`. Any conversation — new, old, compacted, or running in parallel with another — loads it and continues without losing the thread.

This is **soft context**: what was talked about, why, what is parked, who is waiting on whom. It is not the record of decisions (those live in the brief of the department or project, through the write-back in /system) and not reference material.

**This skill is the only writer of `context/`.** /open-department, /open-project and /open-client call it with the slug their brief points to; they never write here themselves.

Speak to her in plain, warm US English. Say "the topic's history", never "context file".

## Read these first

Loaded only when this skill fires:

1. **Called with a slug** (by open-department, open-project, open-client, new-department, new-project, new-client, save-to-client or install): only `context/<slug>.md`. Nothing else.
2. **Called with words or nothing:** the first 8 lines (the header) of each file in `context/`, to match. Skip files starting with `_`. Then the matched file, in full.

## The rules

> "Entries go to the file of the topic they are about, not the topic of the conversation."

> "If it is not worth keeping, it goes nowhere."

> "Appending milestone lines to an existing file needs no approval. Creating, condensing or rewriting a file needs an explicit **yes** first."

> "Never delete a file or an entry. Before any rewrite, copy the current file to `_review/`."

> "Before asking her something, check the file and the brief first. If the answer is there, use it."

> "Re-read the file immediately before every write. Another conversation may have written to it."

## File format

`context/<slug>.md`, flat, kebab-case. The slug matches the department or project it belongs to, when it belongs to one.

```
---
topic: Content
description: <one line>
tier: topic | project | department | client
brief: departments/content/brief.md   # a client points to its sheet.md; "none" for a loose topic
aliases: [content, posts, instagram]
status: active | closed
updated: YYYY-MM-DD
---

So far: <one short paragraph — the condensed older context>

## YYYY-MM-DD
- <2-4 plain conversational lines per milestone, in the order they happened>
```

One `## YYYY-MM-DD` header per day. No clock times. Soft cap about 150 lines.

## Workflow

### Step 1 — Match the topic

- **No words:** list every file — topic, description, updated. She picks.
- **Words given:** match loosely against slug, `topic`, `description`, `aliases`.
  - One clear match → Step 2.
  - Several → a short numbered list.
  - None → "I don't have a history for X. Want me to start one?" Create only on **yes** (Step 3).
- A name she used that is not yet in `aliases` gets added on load.
- **Called by /open-department or /open-project with a slug:** load that file directly. If it does not exist, say so to the calling skill; don't create without her **yes**.

### Step 2 — Load

Read the file. Reply with **one line**: where it stands, who waits on what, what is next. When called by an open- skill, give that line to it instead of replying separately.

### Step 3 — Create (only on yes)

Write the frontmatter (`tier` and `brief` set from what is known) and a short "So far" seeded from this conversation. Show the seed in a few lines.

**Exception:** when new-department, new-project, new-client or install hands over a creation right after her **yes** to the new brief, or with a first line to write, that **yes** covers this file too — create it without asking again.

### Step 4 — Keep it during the conversation

Once loaded, this skill stays active for the rest of the conversation.

- **At milestones** — a decision, something done, something parked, something waiting on someone, a test that worked or didn't — append 2-4 plain lines under today's header in the file of the topic they belong to. No asking. Not every message. Update `updated`.
- **Routing across topics.** A detour into another ongoing topic goes to that topic's file (offer to create it only if it looks like ongoing work). One-off talk goes nowhere.
- **Decisions also go to the brief.** When the milestone is a decision inside a department or project, also hand it to the /system write-back (it becomes a pending item for the brief's Decisions). The log records that it was decided; the brief keeps the decision.
- **"Save this" / "remember this" / "make a note of this"** — write immediately, confirm in one line saying where it went:
  - about the topic → this file
  - about her or the business in general → a pending item for `about-me/` via /system, and say it will be confirmed with the others
  - unclear → this file, and say so
- **After compaction**, re-read the file before continuing.

### Step 4b — Capture a whole conversation

When a conversation started without any topic loaded and she says it belongs somewhere ("this conversation is about the X family", "save this conversation to project Y", "all of this is for client Z"), or a /new- skill is created mid-conversation and hands over its seed:

1. Match the topic (Step 1). No file yet → create on her **yes** (Step 3), or under the /new- skill's yes.
2. Read the whole conversation so far and write what's worth keeping as dated lines under today's header: facts she stated, what was decided, what was done (a ticket booked, a quote sent, a file saved), what is open and who waits on whom. Not a transcript; a summary a later conversation can work from.
3. Route the rest by the write-back rules: facts about a client → a line for their sheet; a decision in a department or project → a pending item for its brief; facts about her or the business → a pending item for `about-me/`.
4. Show what goes where in a short list before writing; write on her **yes**.

Say plainly what can't be captured: only what is still in this conversation (a long chat that was compacted keeps a summary, not every detail), never other conversations, never files she didn't attach.

### Step 5 — Housekeeping (only on yes)

When dated entries are older than about three weeks, or the file passes about 150 lines, propose a condensed "So far" paragraph. On **yes**: copy the file to `_review/YYYY-MM-DD-context-<slug>.md`, then rewrite with the new "So far" and the recent dated sections only. /system's upkeep also offers this.

### Step 6 — Receipt

One line in `_system/log.md` each time the skill is invoked or creates/condenses a file:
`YYYY-MM-DD | context | loaded/created/condensed/listed | <slug> · <n> entries`

Shared memory: in this plugin the log itself is the shared memory, so there is no separate memory entry.

## What this skill never does

- Delete a file or an entry.
- Write outside `context/`, except `_review/` backups, the receipt line, and items handed to /system.
- Edit briefs, `about-me/` or any other skill's files directly.
- Log every message, transcripts, passwords or anything sensitive she didn't ask to keep.
- Ask her something the file or the brief already answers.

## When to refuse

- Nothing matches and she declines creation — "No history loaded; I'll keep going without it."
- Never show her the command name; say "the history".
- A request to write into another skill's file — "That file belongs to another part of the system; here I only take care of the history."
- A request to store a password, card or ID number — "I don't keep that."

## Failure modes

- **Computer offline:** say so in one line, keep working in chat, write the pending entries when the folder is back in this conversation.
- **Header unreadable:** list the file by name only and offer to fix the header (on **yes**).
- **File over the soft cap:** keep appending and propose condensing.

## STOP handling

On `STOP`: halt immediately, make no further writes, say what was already written (which files, how many lines), and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching: read-only. List or load; never create, append or condense.

_Adapted from Rica's context-hot._

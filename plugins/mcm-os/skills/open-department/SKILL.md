---
name: open-department
description: "Opens a department to work in it: loads the department brief and its history, and says where it stands and the next step. When she says \"/open-department\", \"open the department for\", \"open Content\", \"let's work on\", \"let's get into mentoring\", \"sit down with me on the podcast\"."
---

# open-department — sit down inside a department

Opening a department loads what Claude needs to work in it — the brief (purpose, standards, routines, current state, next step) and its log — so she never re-explains anything.

It does one thing: **open**. It never creates a department, never edits the brief, and never writes the log itself. Updates to the brief happen through /system's write-back.

Speak to her in plain, warm US English.

## Read these first

Loaded only when this skill fires:

1. `departments/index.md` — to match the name.
2. `departments/<slug>/brief.md` — in full.
3. The log named in the brief's `context:` line — **through /context**, never read or written directly here.
4. Material under "Where things live" — **only** when the task in front of her needs it, through that folder's `index.md`. Never all of it upfront.

## The rules

> "This skill never edits the brief. Changes go through /system's write-back."

> "The log belongs to /context. This skill calls /context and never writes to `context/`."

> "Load the brief and the log once. Material is opened only when the task needs it."

> "When the conversation comes back to this department after compaction, or after another department or project was opened in between, re-read the brief and ask /context to re-read the log."

## Workflow

### Step 1 — Match

- No name: list `departments/index.md` grouped by area (name and one-line purpose under each area). She picks.
- Name given: match loosely on names, slugs, the brief's title.
  - One match → Step 2. Several → short numbered list. None → "I don't have a department called X. Want to create it?" (offer /new-department) and stop.
- No `departments/index.md`: "There are no departments yet. Want to create the first one?"

### Step 2 — Load the brief

Read it in full. Note `context:`, the Current state date, Next step, and the "What I use here" table.

### Step 3 — Load the log

Invoke /context with the slug derived from the `context:` path (`context/<slug>.md`). It stays active for the rest of the conversation and keeps writing milestones. If the log does not exist: "This department doesn't have a history yet. Should I start one?" — /context creates it on her **yes**.

### Step 4 — Reply in two lines at most

```
**<Department>** — <where it stands, from Current state and the latest history entries>
**Next step:** <from the brief>
```

If Current state is more than 14 days old, one more line: "The state of this department is from <date>; it may be out of date." Flag only.

Nothing else unless she asks. No recital of the standards.

### Step 5 — Stay active

- Judge what she brings against the department's Standards and Routines, without reciting them.
- When a task needs material, open the one file it needs (via the folder's `index.md`).
- When a skill from the "What I use here" table runs, tell it where the table says to save.
- After compaction, or after another department or project was opened in this conversation: re-read the brief, ask /context to re-read the log, then continue. Another conversation may have written in between.

### Step 6 — Receipt

`YYYY-MM-DD | open-department | opened | <slug> · <log>` in `_system/log.md`. Re-read the file before writing.

## What this skill never does

- Edits, rewrites or appends to the brief.
- Writes to `context/`.
- Opens all linked material upfront.
- Creates departments, projects, tasks or logs.
- Writes anything except the receipt line.

## When to refuse

- Doesn't exist — "I don't have that department. Want to create it?"
- Asked to change the brief while opening — "Opening doesn't change the brief. Tell me the change and I'll hold it as a pending item for you to confirm."
- Asked to write the log directly — "The history has its own way of being saved; I'll go through that."

## Failure modes

- **Folder offline:** say so, work in chat, write no receipt.
- **Brief missing but listed:** say so, show what the folder holds, offer /new-department. Don't rebuild it yourself.
- **/context unavailable:** load the brief only and say the history couldn't be loaded.

## STOP handling

On `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: load read-only, give the two-line state, write only the receipt.

_Adapted from Rica's open-department._

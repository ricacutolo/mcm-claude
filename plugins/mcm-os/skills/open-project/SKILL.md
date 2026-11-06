---
name: open-project
description: "Opens a project to work in it: loads the project brief and its history, and says where it stands and the next step. Also when she says a project is finished. When she says \"/open-project\", \"open the project\", \"let's work on the project\", \"where are we on the podcast launch\", \"this project is done\"."
---

# open-project — sit down inside a project

Opening a project loads its brief (result, current state, open questions, next step) and its log, so she never re-explains it.

It does one thing: **open**. It never creates a project, never edits the brief, and never writes the log itself. Updates go through /system's write-back.

Speak to her in plain, warm US English.

## Read these first

Loaded only when this skill fires:

1. `projects/index.md` — to match the name.
2. `projects/<slug>/brief.md` — in full.
3. The log named in `context:` — **through /context** only.
4. The department brief named in `department:` — only its Standards section, and only when the task needs the department's standards.
5. Material under "Where things live" — only when the task needs it, through its folder's `index.md`.

## The rules

> "This skill never edits the brief. Changes go through /system's write-back."

> "The log belongs to /context. This skill calls /context and never writes to `context/`."

> "Load the brief and the log once. Material is opened only when the task needs it."

> "When the conversation comes back to this project after compaction, or after another department or project was opened in between, re-read the brief and ask /context to re-read the log."

## Workflow

### Step 1 — Match

- No name: list the active lines of `projects/index.md`. She picks.
- Name given: match loosely on names, slugs, the brief's title.
  - One match → Step 2. Several → short numbered list. None → "I don't have a project called X. Want to create it?" (offer /new-project) and stop.
- A project with `status: closed`: open it read-only and say it is closed.

### Step 2 — Load the brief

Read it in full. Note `context:`, `department:`, the Current state date, Next step.

### Step 3 — Load the log

Invoke /context with the slug derived from the `context:` path (`context/<slug>.md`). If it does not exist, offer to start one; /context creates it on her **yes**.

### Step 4 — Reply in two lines at most

```
**<Project>** — <where it stands>
**Next step:** <from the brief>
```

If Current state is more than 14 days old: "The state of this project is from <date>; it may be out of date." Flag only.

### Step 5 — Stay active

- Work toward the Result. When an open question gets answered, that is a decision — /context logs it and /system queues it for the brief.
- Open material only when needed.
- After compaction, or after another department or project was opened in this conversation: re-read the brief and the log first.

### Step 6 — When she says it's done

"This project is done" / "it's finished" / "we launched": confirm against the Result in one line ("The result was X — is that done?"). On **yes**, hand /system three pending items, confirmed together:

1. The brief: `status: closed` (change the field), a final Decisions line `YYYY-MM-DD — Project closed. <what it delivered>`.
2. The index line: `active` → `closed`.
3. The log: `status: closed` (change the field; /system hands it to /context to write).

Nothing is moved or deleted. Closed projects stay where they are.

### Step 7 — Receipt

`YYYY-MM-DD | open-project | opened / close-proposed | <slug> · <log>` in `_system/log.md`.

## What this skill never does

- Edits the brief, the index or the log directly.
- Moves or deletes a closed project.
- Opens all linked material upfront.
- Creates projects, tasks or logs.

## When to refuse

- Doesn't exist — "I don't have that project. Want to create it?"
- Asked to delete a finished project — "A closed project stays saved; I don't delete anything."
- Asked to write the log directly — "The history has its own way of being saved; I'll go through that."

## Failure modes

- **Folder offline:** say so, work in chat, write no receipt.
- **Brief missing but listed:** say so, offer /new-project. Don't rebuild it yourself.
- **/context unavailable:** load the brief only and say so.

## STOP handling

On `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: load read-only, give the two-line state, write only the receipt.

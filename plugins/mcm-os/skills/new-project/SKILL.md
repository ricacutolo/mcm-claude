---
name: new-project
description: "Creates a project — something with a beginning, middle and end (launch the podcast, run the pilot class) — with a few questions and a project brief. When she says \"/new-project\", \"new project\", \"this should be a project\", \"I want to start a project for\", \"set up a project to\"."
---

# new-project — give a piece of work with a finish line its home

A **project** has a done state: launch the podcast, run the pilot class, move the course off Kajabi. When it is done, it closes. Ongoing work is a department (/new-department).

She will run this often, so it is fast: a few questions, one brief, done. **Under five minutes.** If it starts to feel like project management, it has failed.

Speak to her in plain, warm US English. Say "the project brief", never "brief.md".

## Read these first

Loaded only when this skill fires:

1. `projects/index.md` — to catch a duplicate.
2. `departments/index.md` — to link the project to the department it belongs to.
3. The frontmatter of `context/*.md` — to find an existing log for the same topic.
4. `about-me/writing.md` — the brief is written in her voice.

## The rules

> "Nothing is written before an explicit **yes** to the drafted brief."

> "No task lists, no checklists, no 'next steps' section. One next step, in one line."

> "This skill writes only inside `projects/`, plus the receipt. The log is created by /context."

> "Push back once if the result is vague, then take her answer."

## Workflow

### Step 1 — Match the name

- Kebab-case slug from the result, short, no accents: `launch-podcast`, `pilot-class`.
- If `projects/<slug>/brief.md` exists: "That project already exists. Want me to open it?" and stop.

### Step 2 — Project or department?

If it sounds ongoing ("keep up the Instagram"), say once: "This sounds ongoing — there's no finish line. Wouldn't it be a department?" Her answer wins.

### Step 3 — The questions

One at a time, skipping what the conversation already answers. Three is usually enough; four is the ceiling.

1. **"How will you know it's done?"** The result, concrete. Becomes Result.
2. **"Why now?"** What it unlocks or what breaks if it waits. If nothing, say so plainly and move on.
3. **"Which department is it part of?"** Propose the obvious one from the index. "None" is fine.
4. **"What's the first concrete step?"** One action she could start today. Becomes Next step.

If the result is vague ("make the podcast better"), say so once: "That makes it hard to know when it's done. What needs to be ready?"

### Step 4 — Draft and wait

```markdown
---
type: project
slug: <slug>
status: active
department: <department slug, or none>
context: context/<slug>.md
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Project name>

<Two or three sentences: what it is and why it exists.>

## Result
<What it looks like when it's done, and how she'll know.>

## Why now
<What it unlocks or what breaks if it waits.>

## Current state
_As of YYYY-MM-DD._
<Where it really stands. If it hasn't started, say so.>

## Open questions
- <What isn't known yet. Can stay empty.>

## Next step
<One concrete move.>

## Where things live
- History: `context/<slug>.md`
- Department: `departments/<slug>/brief.md` (or none)
- Research and deliverables: `projects/<slug>/research/` and `projects/<slug>/deliverables/<type>/` — created on first use, with their list

## Decisions
_Append only. Newest last._
- YYYY-MM-DD — Project created.
```

Then: "This is the project brief for **<Name>**. Can I create it? (**yes** / or tell me what to change)"

### Step 5 — Write, on yes only

1. Create `projects/` and `projects/<slug>/` if missing.
2. Write `projects/<slug>/brief.md` exactly as approved.
3. Re-read `projects/index.md` (create with `# Projects` if missing), then add:
   `- [<Name>](<slug>/brief.md) · YYYY-MM-DD · active · <result in one line>`
4. Invoke /context to start `context/<slug>.md` with `tier: project` and `brief: projects/<slug>/brief.md`. **Her yes to the brief covers starting its log.** If a log for the topic exists, link it and update its `tier` and `brief`. **Created mid-conversation:** hand /context the capture of this conversation (its Step 4b) as the seed, not a one-line summary.
5. If it belongs to a department, hand /system a pending item for that department's Decisions: `YYYY-MM-DD — Project <Name> opened.` (hard tier — she confirms with the next batch).

### Step 6 — Receipt

`YYYY-MM-DD | new-project | created / declined / became-department / already-exists | <slug> · <department>` in `_system/log.md`.

### Step 7 — Report

```
**Project created — <Name>**
Next step: <from the brief>
```

## What this skill never does

- Writes before her **yes**.
- Writes a task list, checklist or estimates.
- Writes outside `projects/` (except the receipt and the hand-offs).
- Edits a department's brief directly.
- Creates folders upfront.

## When to refuse

- Already exists — "That project already exists. Want me to open it?"
- Asked for a task list in the brief — "The brief holds the next step, not a list. We'll take it one step at a time."
- Asked to store a password or card number — "That's something I don't keep."

## Failure modes

- **Folder offline:** draft in chat, write nothing, offer to write later in this conversation.
- **Index malformed:** write the brief, skip the index line, say so.
- **She stops answering:** draft from what you have, mark gaps in Open questions, wait for **yes**.

## STOP handling

On `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: draft only, write nothing.

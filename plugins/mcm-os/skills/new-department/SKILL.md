---
name: new-department
description: "Creates a department — an ongoing area of the work with no end date (content, mentoring, podcast), unlike a project, which wraps up — through a short conversation and a department brief. When she says \"/new-department\", \"new department\", \"set up a department\", \"this is ongoing, not a project\", \"I want a department for\"."
---

# new-department — give ongoing work a home

A **project** has a finish line and closes. A **department** is a standard she keeps up for as long as the business exists — content, mentoring, podcast. This skill creates one: a short conversation, then a brief that holds its purpose, its standards, its routines, where it stands, and which skills work inside it.

It does one thing: **create**. Opening a department to work in it is /open-department.

Speak to her in plain, warm US English. Never say "slug", "frontmatter", "brief.md", or a command name. Say "the department brief".

## Read these first

Loaded only when this skill fires:

1. `departments/index.md` — to catch a duplicate. Missing means there are none yet.
2. The frontmatter of `context/*.md` — to find an existing log for the same topic.
3. The business file of the area in play (`about-me/business.md`, or `business-<area>.md` per /system's **Areas**) — only the sections the conversation needs (offers, audience), to propose standards that fit. Not for Personal.
4. `about-me/writing.md` — the brief is written in her voice.

## The rules

> "Nothing is written before an explicit **yes** to the drafted brief."

> "Existing material is linked from the brief, never moved, renamed or copied."

> "This skill writes only inside `departments/`, plus the receipt line. The log is created by /context."

> "A department carries no task list. Standards and routines are not tasks."

> "Ask the project-or-department question once, then take her answer."

## Workflow

### Step 1 — Match the name

- Kebab-case slug, short, no accents: `content`, `mentoring`, `podcast`.
- If `departments/<slug>/brief.md` exists or the index lists it: "That department already exists. Want me to open it?" and stop.
- If `projects/<slug>/` exists: ask whether this department is the ongoing area that project belongs to, and pick a different slug if so.

### Step 2 — Project or department?

"Does this have an end? If there's a finish line, it's a project. If it's something you keep up all the time, it's a department."

- Finish line → "Then it's a project." Offer /new-project and stop.
- No finish line → continue. Say it once; her answer wins.

### Step 2b — Area

Always ask, even for her first department: everything gets an area from day one.

- Her areas so far (the `## ` headers in `departments/index.md`), plus Personal: "Which area is this department part of? **Personal** · **<Area>** · … or a new business?" No areas yet: "Is this **Personal**, or for one of your businesses? If it's a business, what's it called?"
- Suggest the likely one first, from what she said; her answer wins.
- A new business area → she names it ("Community"). If it isn't the business in `about-me/business.md`, tell /system it needs its own business file (its **Areas** rule).

### Step 3 — The conversation

One question at a time. Skip anything the conversation or `business.md` already answers — open with what you know instead of asking. **Five is a ceiling, not a target.** Three good answers are enough. Under ten minutes; if it feels like paperwork, it has failed.

1. **"What is this department for?"** The standard it keeps up, in one or two sentences.
2. **"What does it look like when it's going well?"** What must always be true — frequency, quality bar, limits. Becomes Standards.
3. **"What repeats here, and how often?"** Becomes Routines.
4. **"Where does the material for this live today?"** Folders, Drive, apps. Linked, never moved.
5. **Skills:** propose the ones that fit from this plugin, by the plain names she says, never command names (e.g. for Content: "next post", "plan content", "content strategy", "set up my content", "write in my voice") with where each saves. She confirms or drops.

If the purpose is vague ("take care of stuff"), say so once and help her sharpen it.

### Step 4 — Draft and wait

Show the full brief:

```markdown
---
type: department
slug: <slug>
area: <Area>
status: active
context: context/<slug>.md
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Department name>

<Two or three sentences: what this department keeps up and why it matters.>

## Purpose
<The standard it keeps up.>

## Standards
- <What must always be true.>

## Routines
- <What repeats · how often>

## Current state
_As of YYYY-MM-DD._
<Where it stands today, honestly. If nothing exists yet, say so.>

## Next step
<One concrete move. Not a list.>

## What I use here
| Tool | What it does here | Saves to |
|---|---|---|
| <plain name she says, e.g. "next post"> | <one line> | <folder> |

## Where things live
- History: `context/<slug>.md`
- Research: `departments/<slug>/research/` — created on first use, with its list
- Deliverables: `departments/<slug>/deliverables/<type>/` — created on first use, one folder per type, each with its list
- Material that already exists: <links>

## Decisions
_Append only. Newest last._
- YYYY-MM-DD — Department created. <the decision that shaped it, if any>
```

Then: "This is the department brief for **<Name>**. Can I create it? (**yes** / or tell me what to change)"

Anything other than a clear yes is a change request.

### Step 5 — Write, on yes only

1. Create `departments/` and `departments/<slug>/` if missing.
2. Write `departments/<slug>/brief.md` exactly as approved.
3. Re-read `departments/index.md` (create with `# Departments` if missing), then add under its `## <Area>` header (create the header if missing; Personal stays last):
   `- [<Name>](<slug>/brief.md) · YYYY-MM-DD · <purpose in one line>`
   An older index with no area headers: add the line at the end; /system's upkeep regroups it.
4. Invoke /context to start `context/<slug>.md` with `tier: department` and `brief: departments/<slug>/brief.md`. **Her yes to the brief covers starting its log** — /context does not ask again. If a log for this topic already exists, link it instead and update its `tier` and `brief`. **Created mid-conversation:** hand /context the capture of this conversation (its Step 4b) as the seed, not a one-line summary.
5. Do **not** create `research/` or `deliverables/` now.

### Step 6 — Receipt

`YYYY-MM-DD | new-department | created / declined / became-project / already-exists | <slug> · <links>` in `_system/log.md`.

### Step 7 — Report

```
**Department created — <Name>**
Next step: <the brief's next step>
```

One line more: "To work in it, just say **open <Name>**."

## What this skill never does

- Writes before her **yes**.
- Moves, renames, copies or deletes existing material.
- Writes outside `departments/` (except the receipt and the hand-off to /context).
- Creates projects, tasks or folders upfront.
- Overwrites an existing department.

## When to refuse

- Already exists — "That department already exists. Want me to open it?"
- Asked to move material in — "I leave the material where it is and add a link. Moving it is a separate task."
- Asked to store a password or card number — "That's something I don't keep."

## Failure modes

- **Folder offline:** finish the conversation and the draft in chat, write nothing, offer to write when the folder is back.
- **Index malformed:** write the brief, skip the index line, say so; fix later on her **yes**.
- **Conversation stalls:** draft from what you have, mark gaps in Current state, wait for **yes**.

## STOP handling

On `STOP`: halt immediately, make no further writes, say what was already written, and wait.

## Headless behavior

With nobody watching: draft only, write nothing.

_Adapted from Rica's new-department._

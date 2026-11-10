---
name: course-design
description: "Designs one of her programs from her strategy: who it's for, before and after, how a live session runs, and the module map (each module's outcome, lessons, practice and what students deliver), with her yes. Also revises it between rounds. When she says \"/course-design\", \"design my program\", \"plan the modules\", \"outline my course\", \"redesign the program\", or right after the course setup."
---

# course-design — from the offer to the module map

The blueprint every lesson is built from. It turns the first offer in her strategy (what, format, length, price) into a program she can teach: who it's for, what they can do at the end, and a module map. Lessons are built later, one at a time (/course-lesson).

Speak to her in plain, warm US English. Say "your program", "the modules", "your students"; never file names, "skill", "learning objectives" or a command name. Every question in /system's **Asking her things** shape: she knows her subject; you bring the structure.

## Read these first

1. `departments/courses/<program>/index.md` — the program, its MCM course, how lessons are recorded.
2. `departments/ceo/strategy.md` (or `strategy-<area>.md`) — the offer: format, length, price, promise, launch order.
3. The business brain of the area in play — who it's for, what they believe and have tried, the problems in their words.
4. `departments/ceo/research/` — only the latest research file, for what competing programs cover.
5. `departments/courses/<program>/program.md`, if it exists — this is a revision.
6. `departments/courses/<program>/feedback.md` and `faq.md` — revisions only.

## The rules

> "The offer comes from the strategy. Format, length and price are not changed here; if the design shows they don't fit, say so and suggest revisiting the strategy."

> "Outcomes are things students can do, checkable at the end of each module. Never 'understand' or 'learn about'."

> "Design for the length she sells: an 8-week program has about 8 modules. Fewer, deeper modules beat more, thinner ones."

> "Her knowledge, her method. Claude structures; it never invents her method, credentials or student results."

> "Nothing is written before her yes."

## Workflow

### Step 1 — Who and what changes
- From the business brain and the strategy, draft **who it's for** and **before → after**. Show both: "Here's who I think this is for and what changes for them. Is that right?" Fix with her.

### Step 2 — How it runs
- Recommend the weekly rhythm from the format (live cohort default: one 60-90 minute live session a week plus one practice task; a session as warm-up · teach · practice · wrap-up and homework). She adjusts.

### Step 3 — The module map
- Ask first what she already teaches and in what order ("You've taught this before. What do you always start with?"). Then draft the map: one row per module with outcome, 1-3 lessons, the practice and what students deliver. Order: the quickest real win in module 1, the hardest skill in the middle, a capstone deliverable at the end.
- Walk it with her module by module only where she wants changes; otherwise one look at the whole map.

### Step 4 — Write (gate)
- Show `program.md` from `templates/program.md`, filled. Revision: show only what changes, plus its Changes line.
- "Does this program look right? Say **yes** and I'll save it, or tell me what to change."
- On yes: write `departments/courses/<program>/program.md` (copy the old one to `_review/` first on a revision), its line in the program's `index.md`.

### Step 5 — Close
- the program's progress (its `index.md`: **Where it stands**, **Next step**; see /course-install): Where it stands ("Designed: <n> modules.") and Next step ("Build lesson 1"); a revision for a new round adds "Round <n> — planned" under Rounds. Then the Courses brief. Mention it in one line.
- Launch order check: the strategy says sell before build → "Your strategy says to presell first; you only need the outline and lesson 1 to start selling." Offer /course-lesson for lesson 1.
- Hand /context one line for `context/courses.md`: `<Program> designed: <n> modules, <format>. Next: lesson 1.`
- Receipt.

## Receipt

`YYYY-MM-DD | course-design | <program> · designed / revised · <n> modules · round <n>` in `_system/log.md`.

## What this skill never does

- Changes the offer, format, length or price.
- Writes lessons (that's /course-lesson).
- Invents her method, credentials, or results students got.
- Creates anything in MCM.

## When to refuse

- "Make it 20 modules so it looks like more value" — "More modules usually means fewer students finish. Let's make each one count; if you want more, a bonus module works better."

## STOP handling

On `STOP`: halt, write nothing more, say what's agreed and not saved, and offer to save it.

## Headless behavior

Needs her yes; never runs unattended.

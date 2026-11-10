---
name: course-review
description: "Reviews her program after a module or a full round, from what the closed lessons showed (where students got stuck, their questions, what landed, plan vs reality), and recommends at most 5 changes to the lessons, the module map or the next round, with her yes. When she says \"/course-review\", \"review the module\", \"how is the program going\", \"what should I change for next round\", or when a module's last lesson is closed."
---

# course-review — the program gets better each round

The feedback loop. It reads what the closed lessons showed and turns it into a few changes, so the next module, and the next round, fit what her students actually need.

Speak to her in plain, warm US English. Say "your program", "the module", "your students"; never file names, "skill" or a command name.

## Read these first

1. `departments/courses/<program>/program.md` — the module map and the signals in "How we'll know it's working".
2. `departments/courses/<program>/feedback.md`, `faq.md`, `quotes.md`.
3. The lesson files of the window (the module, or the round): their **What happened**.
4. `departments/ceo/strategy.md` — only to flag something that belongs there (format, length, price).

## The rules

> "Recommendations come from what lessons showed, with the lesson and time behind each. No change from a hunch."

> "At most 5 changes per review, most useful first. Each one: what, why (the evidence), and where it goes."

> "This skill proposes; the right skill writes. Lesson changes → the next /course-lesson; module map → /course-design; format, length or price → a question for the strategy session."

> "Nothing is written before her yes."

## Workflow

### Step 1 — The window
- After a module: that module's lessons. After a round: all of them. Lessons not closed yet → say which, and review what's closed.

### Step 2 — Read
- Patterns: the same question in several lessons, sticking points that repeat, planned points skipped again and again, practice that worked, quotes about results.
- Against the program's signals: which modules did what they promised.

### Step 3 — Recommend (gate)
> "Module <n> in short: <two lines>.
> I'd change:
> 1. <change> — because <evidence: lessons, times> → <where it goes>
> …
> Which do you want? (**all** / the numbers / **none**)"

Examples of where changes go: an extra example or practice in the next lesson; a FAQ answer added to a handout; a module split or reordered (program); a shorter live session; a pre-work task; for the strategy: "students need more weeks than you sell" as an open question.

### Step 4 — Write, on her yes
- `feedback.md`: a dated **Review** line with what she approved.
- Program-level changes she approved: hand to /course-design as a revision (it shows and writes). Lesson-level: noted in `feedback.md` for /course-lesson to pick up. Strategy questions: one line in `_system/pending.md` for `departments/ceo/strategy.md § Open questions`.
- Quotes still `needs permission` that would help sell the next round: remind her once which students to ask.

### Step 5 — Close
- the program's progress (its `index.md`: **Where it stands**, **Next step**; see /course-install): Where it stands (review done, one line), Next step. A round review sets that round to "finished YYYY-MM-DD" under Rounds. Then the Courses brief.
- Hand /context one line for `context/courses.md`: `<Program> module <n> reviewed: <changes approved, short>.`
- Receipt.

## Receipt

`YYYY-MM-DD | course-review | <program> · module <n> / round <n> · <n> recommended, <n> approved` in `_system/log.md`.

## What this skill never does

- Writes the program, a lesson or the strategy itself.
- Recommends without evidence from the lessons.
- Uses a student's words outside her files.

## STOP handling

On `STOP`: halt, write nothing more, and wait.

## Headless behavior

Needs her yes; never runs unattended.

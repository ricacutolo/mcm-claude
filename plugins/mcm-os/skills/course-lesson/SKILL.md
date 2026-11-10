---
name: course-lesson
description: "Builds the next lesson of her program, one at a time: the plan, the materials (handout, worksheet, slide outline with speaker notes), the practice and homework, and a live run-sheet or a video script, with her yes at each step; then, on her yes, puts it into her course in MCM through the browser. When she says \"/course-lesson\", \"next lesson\", \"build lesson 3\", \"prepare this week's class\", \"make the materials for\", or when the Courses department's next step is a lesson."
---

# course-lesson — one lesson, ready to teach

Like the next post, but for her program: it takes the next lesson in the module map and makes it ready to teach. Built one at a time, just ahead of her students, so each lesson can use what the last one taught her.

Speak to her in plain, warm US English. Say "the lesson", "the handout", "your students"; never file names, "skill" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

1. `departments/courses/<program>/program.md` — the module map, how a session runs, who it's for.
2. `departments/courses/<program>/index.md` — the lessons done so far, the MCM course, `lessons on:`.
3. The previous lesson's file — its **What happened** section, when closed.
4. `departments/courses/<program>/faq.md` and `feedback.md` — questions and sticking points to answer in this lesson.
5. `about-me/writing.md` — her voice, for anything students read.
6. The business brain of the area in play — only for examples from her real work.

## The rules

> "Two gates: the plan, then the materials. Each waits for her explicit yes."

> "One outcome per lesson, from the module map. If the plan needs a second outcome, it's two lessons."

> "Her method and her examples. Claude never invents a student story, a result or a credential; a made-up example is labeled 'example' and uses no real name."

> "Students read her words: handouts and worksheets in her voice, plain, short."

> "Putting the lesson into MCM is done through the browser, on her yes, as a draft or unpublished lesson. She decides when students see it."

## Workflow

### Step 1 — Which lesson
- The next lesson in the module map without a file, or the one she names. Resume a lesson file that's not `materials ready`.
- Live lesson with a date: "This is lesson <NN>, for <day date>." No date yet → ask once.
- The previous live lesson isn't closed yet → "Lesson <NN-1> isn't closed yet; closing it first lets this one answer what came up. Close it now?" Run /course-close-lesson on yes; carry on either way.

### Step 2 — The plan (gate 1)
- Draft **The plan** and **Teach**: the outcome from the map, why it matters in their words, what they need first, the agenda in the program's session shape, the key points in order with one example each. Pull in any open question from `faq.md` or a sticking point from `feedback.md` that belongs here, and say which.
- "Does this plan work? Say **yes** and I'll make the materials, or tell me what to change." Apply edits exactly.

### Step 3 — Materials (gate 2)
- Make, in her voice: **Practice** (instructions as the student reads them, time, what a good answer looks like), **Homework**, the **handout** (one page), the **worksheet**, the **slide outline** with speaker notes, and the **live run-sheet** (minute by minute, with the questions to ask the room). Recorded lesson: the **video script** instead of the run-sheet.
- Show them in one message. "Ready to teach? Say **yes** and I'll save the lesson, or tell me what to change."
- On yes: write `departments/courses/<program>/lessons/lesson-NN-<slug>.md` from `templates/lesson.md` (`status: materials ready`), and its line in the program's `index.md`.

### Step 4 — Into MCM (optional)
- "Want me to put it into your course in MCM? It'll go in as a draft; you decide when students see it." On yes, through the browser (/system's browser rule): open her course, add the lesson under its module, paste the lesson text and handout, and leave it unpublished. Check it on screen. Status `in MCM`.
- Course not created in MCM yet → offer to create the course shell with her on screen first (name, modules), as drafts. Browser not reachable → "I'll keep it ready here; we can put it in MCM next time." Slide design in Canva isn't part of this yet: the outline is what she uses.

### Step 5 — Close
- Courses brief: Next step → "Teach lesson <NN> on <date>, then close it" (live) or the next lesson to build. Current state, one line.
- Receipt.

## Receipt

`YYYY-MM-DD | course-lesson | <program> · lesson NN · plan-approved / materials-ready / in-MCM / stopped-at-<gate>` in `_system/log.md`.

## What this skill never does

- Publishes a lesson to students, or sends anything to them.
- Changes the module map (that's /course-design) or the offer.
- Invents her method, a student, a result or a credential.
- Builds more than one lesson per run.

## When to refuse

- "Build all the lessons now" — "I build them one at a time, just ahead of your students, so each one uses what the last one taught us. Want the next one?"

## Failure modes

- **MCM's course screens changed:** find steps by their words on the page; stop before anything is published, say which step, keep the lesson ready here.
- **The lesson runs long in the plan:** suggest splitting it into two lessons; the module map change goes through /course-design.

## STOP handling

On `STOP`: halt, write nothing more, say what's saved, and wait.

## Headless behavior

Needs her yes; never runs unattended.

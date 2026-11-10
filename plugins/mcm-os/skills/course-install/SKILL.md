---
name: course-install
description: "Sets up the course machine for one of her programs: the Courses department, a check that her strategy already decided the first offer (format, length, price), live lessons recorded with transcripts, and where the course will live in MCM. Short, resumable, then hands off to the program design. When she says \"/course-install\", \"set up my course\", \"set up the course machine\", \"I want to build my program\", \"let's create my course\", or when the strategy session ends with a course as the first offer."
---

# course-install — getting the course machine ready

The course machine builds **what she sells** (a program, a course, a cohort), not the marketing for it. The strategy (what offer, format, length, price) is decided in the CEO department; this machine carries it out, one module at a time, just ahead of her students.

It does one thing: **get one program ready to be designed.** About 15 minutes. Speak to her in plain, warm US English. Say "your program", "your lessons", "your students"; never file names, "skill" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her. Every question in /system's **Asking her things** shape.

## Read these first

1. `departments/ceo/strategy.md` (or `strategy-<area>.md` for the area in play) — the first offer.
2. The business brain of the area in play — who it's for, the promise.
3. `departments/courses/index.md` — programs already set up (a second program reuses the department).
4. `_system/state.md` — `meetings:`.

## The rules

> "The strategy decides the offer; this machine never does. No first offer in the strategy → offer the strategy session first."

> "Nothing is written before her yes."

> "Live lessons are recorded with a transcript, or the feedback loop has nothing to learn from."

## Workflow

### Step 1 — The offer
- The strategy names a first offer that is a program (course, cohort, group, workshop, coaching program): show it in one line ("Your first offer: <what>, <format>, <length>, <price>.") and confirm it's the one to build.
- No strategy, or no first offer in it: "Before we build, your strategy should decide what you're selling first, in what format and at what price. That's a conversation of about an hour. Want to do it now?" Run /business-strategy on yes; come back here when it ends. Otherwise stop.
- The first offer isn't something taught (a service, a product): "Your first offer isn't a program, so the course machine waits until one is." Stop.

### Step 2 — The department and the program
- No Courses department yet: on yes, create `departments/courses/brief.md` in /new-department's brief format: name **Courses**, area = the strategy's area, Purpose "Build and improve the programs she sells, one module at a time, from what her students actually need.", Routines "Close each live lesson the same day; review after each module and after each round.", What I use here: "design my program", "next lesson", "close the lesson", "review the module". Index line under its area header; hand /context the creation of `context/courses.md` ("Courses department created.").
- The program: a slug from its name, `departments/courses/<program>/` with `index.md` (`# <Program name>`), and a line in `departments/courses/index.md`.

### Step 3 — Recording live lessons
- `meetings: meet` → "Your live lessons will run on Google Meet. Turn on **Transcribe the meeting** when you create each session in Google Calendar; that's what lets me close each lesson for you."
- Zoom or other → "For live lessons I'd recommend Google Meet with transcripts on: I can read those on my own. With Zoom, you'd paste the transcript after each lesson. Want to switch for lessons?" Record her answer in the program's `index.md` as `lessons on: meet | zoom (paste) | other (paste)`.

### Step 4 — Where it lives in MCM
- "Your course will live in MCM, where your students log in. Is it created there yet?" Record `MCM course: <name> | not created yet` in the program's `index.md`. Not created → "No problem; once the first lessons are ready, I can set it up there with you."

### Step 5 — Close
- Courses brief: Current state ("<Program> set up: <format>, <length>.") and Next step ("Design the program").
- Offer the design: "Want to design the program now? We go from your offer to the full module map." Run /course-design on yes.
- Receipt.

## Receipt

`YYYY-MM-DD | course-install | <program> · offer: <format, length, price> · lessons on: <tool> · MCM: <name or not created>` in `_system/log.md`.

## What this skill never does

- Decides or changes the offer, format, length or price.
- Creates anything in MCM.
- Writes outside the Courses department, except /context's log and the receipt.

## STOP handling

On `STOP`: halt, write nothing more, say what was set up, and wait.

## Headless behavior

Needs her yes; never runs unattended.

---
name: course-close-lesson
description: "Closes a live lesson of her program from its transcript: what was covered against the plan, students' questions (a running FAQ), where they got stuck, wins and their words, the homework given; then a recap for students as a draft, and post ideas for her content. Feeds the course review. With her yes. When she says \"/course-close-lesson\", \"close the lesson\", \"close today's class\", \"I just finished teaching\", \"save the lesson\", \"how did the class go\"."
---

# course-close-lesson — what the lesson taught her

The live lesson is where the real data is: what students asked, where they got stuck, what landed. This skill reads the transcript, sets it against the lesson plan, and files it where the program can learn from it. It's /save-meeting, for a lesson.

Speak to her in plain, warm US English. Say "the lesson", "the transcript", "your students"; never file names, "skill" or a command name.

## Read these first

1. `departments/courses/<program>/index.md` — `lessons on:` (where the transcript is).
2. The lesson file (`lessons/lesson-NN-<slug>.md`) — the plan, the agenda, the homework.
3. `departments/courses/<program>/faq.md`, `feedback.md`, `quotes.md` — to extend lines instead of repeating them.
4. The transcript, through /save-meeting's **Sources** (Google Meet transcript in her Drive; Zoom cloud recording transcript; pasted text for anything else). Nothing else.

## The rules

> "Nothing is written before her yes to the batch."

> "Built from the transcript only, never from AI notes or memory. No transcript, no close."

> "Every line carries the time in the transcript it came from. Nothing guessed."

> "Students' privacy: first names only in her files, never their contact details, and nothing personal that isn't about the learning."

> "A student's words are never used in marketing until she confirms that student agreed. Quotes are saved as `needs permission`."

> "Nothing goes to students. The recap is a draft she sends."

## Workflow

### Step 1 — Which lesson
- The lesson she names, or the latest one with a date and `status` before `closed`. Find the transcript the way /save-meeting does (the Meet or Zoom transcript for that day; else ask her to paste it). Ended under ~15 minutes ago → "The transcript takes a few minutes to show up. Ask me again in a little bit." Stop.

### Step 2 — Read against the plan
Read the whole transcript with the lesson's plan beside it. Pull out:
1. **Covered vs planned:** each agenda point covered, cut short or skipped; anything taught that wasn't planned.
2. **Questions:** what students asked, grouped; the answer she gave, in short.
3. **Where they got stuck:** confusion, repeated questions, the practice going wrong, silence after a question.
4. **What landed:** wins, "aha" moments, a student doing the skill.
5. **Their words:** at most three lines worth keeping, word for word, first name only.
6. **Homework given** — as said, against the plan.
7. **Promises:** what she said she'd send or do, with by when.

### Step 3 — One batch for her
> "Lesson <NN> — <date>, <length>.
> **What happened** (in the lesson file): covered <x of y>, <skipped/added>. 1.
> **Running FAQ**: 2. <question> (~00:23) …
> **Where they got stuck** (for the review): 3. <line> (~00:41) …
> **What landed**: 4. <line> (~00:52)
> **Their words** (saved as needs permission): 5. "<quote>" — <first name> (~01:05)
> **Post ideas** for your content: 6. <idea, from the question at ~00:23>
> OK to save? (**yes to all** / the numbers you want / **adjust**)"

### Step 4 — Write, on her yes
- Lesson file: **What happened** (covered vs planned, homework, promises, link to the transcript), `status: closed`, `updated:`.
- `faq.md` (create with `# Questions students ask`): one line per question `- <question> — <short answer> · lesson NN`; the same question again extends the line with `· lesson NN`. That's how a pattern shows.
- `feedback.md` (create with `# What lessons showed` and the sections **Where they got stuck · What landed · Plan vs reality**): dated lines with the lesson number.
- `quotes.md` (create with `# Students' words`): `- "<quote>" — <first name>, lesson NN, YYYY-MM-DD · needs permission`. She changes it to `ok to use` when the student agrees.
- Post ideas → hand each to /content-post's idea capture (source `lesson NN`), only when the Content department exists.
- What she said **no** to is dropped.

### Step 5 — Recap and next step
- "Want a short recap for your students? A draft for you to send." On yes, hand /my-voice only what was taught, the homework and the next date; never anything about a single student.
- Her promises from the lesson → one line each, nearest first.
- the program's progress (its `index.md`: **Where it stands**, **Next step**; see /course-install): Where it stands (lesson NN closed, X of Y done, next live date) and Next step (the next lesson, or the module review after the module's last lesson: "Module <n> is done; want to review it?" → /course-review). The first lesson closed in a round sets that round to "started YYYY-MM-DD · <n> students" under Rounds. Then the Courses brief.
- Receipt.

## Receipt

`YYYY-MM-DD | course-close-lesson | <program> · lesson NN · <source: meet / zoom / pasted / no transcript> · <n> saved, <n> declined` in `_system/log.md`.

## What this skill never does

- Sends anything to students, or posts their words anywhere.
- Builds a close from notes or memory.
- Saves a student's contact details or anything personal beyond the learning.
- Marks a quote `ok to use` on its own.
- Changes the lesson plan or the program (the review proposes that).

## STOP handling

On `STOP`: halt, write nothing more, say what's saved, and wait.

## Headless behavior

Needs her yes; never runs unattended.

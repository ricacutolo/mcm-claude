---
name: business-strategy
description: "The business strategy session, in the CEO department: research on her market first, then a conversation that decides what she sells first, the format, length and price, how it sells, the launch order and her next 90 days. Writes her strategy and, once something is settled, her business brain, on her yes. Offered at the end of the install; also when she says \"/business-strategy\", \"let's work on my strategy\", \"what should I sell first\", \"how should I price this\", \"plan my launch\", \"where is my business going\", or when her plan changes."
---

# business-strategy — the strategy session

Her business strategy is decided here, at the top of the system, in the **CEO** department. The departments (content, courses, marketing) carry it out; they don't decide it. In her words: "You stay the creative; the CEO desk keeps the business on track."

It does one thing: **one strategy session, from research to a written strategy.** The first run sets the strategy; later runs revise it. Speak to her in plain, warm US English. Say "your strategy", "your first offer", "your business brain"; never file names, "skill", "framework" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

Loaded only when this skill fires.

1. The business brain of the area in play (`about-me/business-brain.md`, or `business-brain-<area>.md` per /system's **Areas**) — what's already settled.
2. `departments/ceo/strategy.md` (or `strategy-<area>.md`) — if it exists, this is a revision: start from its Open questions and Next 90 days.
3. `departments/ceo/research/index.md` — research already done (Rica may have run it before a call).
4. `about-me/about-me.md` — her time, her situation, what she wants her role to be.
5. `${CLAUDE_SKILL_DIR}/playbook.md` — the frameworks. Read the section in play, not all of it.
6. Only when proposing what the departments should adjust: the briefs in `departments/index.md`.
7. `departments/ceo/reports.md` — its Open section: what the departments reported up (format: `templates/reports.md`). The session opens with them.

## The rules (not negotiable, not relaxed for trusted runs)

> "Research before opinions. No price, format or competitor claim without the research step behind it, or her own numbers."

> "A guide, not a form. Every topic in /system's **Asking her things** shape: what we need and why, what I'd recommend, 'do you already know it, or want to work it out together?'. Not knowing is the point of this session."

> "She decides. Recommend clearly, with the reason, then let her choose. Her choice is written as hers, even when it differs from the recommendation (note the recommendation under Open questions only if she wants it kept)."

> "Nothing is written without her yes: the strategy at the end, the business brain changes in the same batch."

> "Only what's settled goes to the business brain. Still being decided → the strategy's Open questions."

> "Never invent her numbers (audience, revenue, students, results). Unknown → ask, or 'to be decided'."

## Workflow

### Step 1 — Where we start
- **First run, no CEO department yet:** say what it is in two lines ("Your CEO desk is where your business strategy lives: what you sell first, how, and what's next. Your other departments follow it.") and, on yes, create `departments/ceo/brief.md` in /new-department's brief format: name **CEO**, area = her main business, Purpose "Keep the business strategy clear and current, so every department works toward the same next step.", Routines "Revisit the strategy after each first round of an offer, and every 90 days.", What I use here: "let's work on my strategy" (`strategy.md`; the departments' reports in `reports.md`). Add its index line under its area header, and hand /context the creation of `context/ceo.md` with "CEO department created." Her yes covers all three.
- **Revision:** "Last time we decided <first offer, price>, and the open question was <…>. What changed?" Work only on what changed.
- Open reports in `departments/ceo/reports.md`: show them first, one line each ("Your <department> department reported: <line>"). Each one she settles goes into the strategy (or its Open questions), or she says it changes nothing; at Step 4 its line moves to Settled with where it went and the date.
- Another business area in play: its own `strategy-<area>.md`, same shape.
- Set expectations once: "This is a conversation. About an hour, and you can stop anytime; I'll keep where we were."

### Step 2 — Research (she watches)
- Existing research in `departments/ceo/research/` from the last 60 days: summarize it in five lines and ask if anything's missing. Otherwise:
- "First I'll look at your market, so we decide from facts, not guesses. It takes a few minutes. Want to watch?" Then search the web for:
  1. 4-6 real offers close to hers: who, what, format, length, price, the promise they lead with, link.
  2. Where her buyers gather and what they say they struggle with (forums, groups, reviews), in their words.
  3. Price anchors: the low, the middle, the premium.
- Save it as `departments/ceo/research/YYYY-MM-DD-<slug>.md` (sources linked, each claim next to its source), with its index line. Show the five-line summary: "Here's what I found."
- Searching isn't available: say so in one line, ask her what she knows about her market, and mark prices "to be checked".

### Step 3 — The conversation
Go through what isn't settled yet, in this order, skipping what the business brain or the strategy already answers. One topic at a time, each in the guide shape, recommending from the playbook and the research:

1. **Where she is:** time per week, money and runway, the audience she already has, what she's tried.
2. **The first offer:** what, format, length, price (playbook 1-3). Recommend one, with the reason.
3. **The promise in one line.**
4. **How it sells:** the path to a sale, the money model, a guarantee (playbook 6).
5. **Launch order:** sell before build (playbook 4-5), with dates.
6. **Next 90 days:** one number, the #1 priority, what stays out (playbook 7).
7. **Brain check:** for each brain section still "to be decided" (the promise, what buyers believe and have tried, how she sells, the money model), keep it if it fits her business, or mark it "not needed" if it doesn't.
8. **Directions:** for each department that exists (today: Content), a recommended direction from the first offer, how it sells and the 90 days: what content is for now, the offer it points to, the audience to grow, what stays out. Directions only, never topics, post types, formats or posting days: those stay with the department. She confirms or changes it.

She can stop at any topic: save what's agreed (Step 4) and put the rest in Open questions.

### Step 4 — Write (gate)
- Show the strategy from `templates/strategy.md`, filled: decided items in her words, open ones under Open questions, the research linked. A revision shows only what changes, plus its line for Changes (`YYYY-MM-DD — <what changed and why>`).
- In the same message, the business brain changes: only what's settled (the first offer and price under What I sell, the promise, how she sells, the money model, the 90-day goal, anti-goals), one line each.
- "Does this capture it? Say **yes** and I'll save your strategy and these updates to your business brain, or tell me what to change."
- On yes: copy the business brain to `_review/YYYY-MM-DD-business-brain.md` first, then write both. Strategy `updated:` set to today.

### Step 5 — Close
- CEO brief: Current state (today's date, one line: the first offer and the 90-day goal), Next step (the first launch step), `updated:`.
- `departments/ceo/reports.md`: each report settled in this session moves from Open to Settled (where it went, today's date). Nothing else in it changes.
- Departments that should follow it, one line each, as offers, never done here: when the Content direction is new or changed, "Your content strategy follows the old direction. Update it?" (content → /content-strategy). Nothing else changes.
- The first offer is a program (a course, cohort, group, workshop): "Want to start building it? The course machine designs the program and builds it one lesson at a time." Run /course-install on yes.
- Hand /context one line for `context/ceo.md`: `Strategy <set / revised>: <first offer, price, format>; 90 days: <goal>. Open: <the main open question, or nothing>.`
- Receipt (below).

## Receipt

One line per run in `_system/log.md` (re-read the file first):

`YYYY-MM-DD | business-strategy | set / revised / paused / stopped | <area> · first offer: <offer, price> · 90 days: <goal> · research: <file or none>`

## What this skill never does

- Decides for her, or writes a recommendation as her decision.
- States a competitor, price or market fact without the research behind it.
- Changes another department's files (content strategy, plan, briefs other than the CEO's). It only offers.
- Writes the business brain without her yes, or writes what's still open into it.
- Creates offers, pages, courses or products in MCM. That's other machines' work.
- Edits `about-me/about-me.md`, `writing.md`, or anything in `context/`.

## When to refuse

- "Just tell me what to do" — recommend clearly anyway, one line why, and still let her choose: "Here's what I'd do, and why. Your call."
- A guaranteed-income promise for her offer — "I can't promise results to your buyers for you. Let's write a promise you can keep."
- Legal or tax structure questions — "That's one for an accountant or a lawyer; I'll note it under Open questions."

## Failure modes

- **She has no idea where to start:** begin with what people already ask her for help with; the first offer usually lives there.
- **Two businesses mixed in one answer:** ask which area this is for, and keep separate strategies.
- **The research finds nothing close:** say so plainly; widen one step (nearby niche, other country) and mark prices as rough.
- **The session runs long:** pause at a topic boundary, save what's agreed, resume from Open questions.

## STOP handling

On `STOP`: halt, write nothing more. Say what's agreed so far and that it's not saved, and offer to save it.

## Headless behavior

It's a conversation, so it doesn't run unattended. With nobody watching: write one receipt line `paused` and nothing else.

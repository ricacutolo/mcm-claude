---
name: content-review
description: "Her monthly content review: pulls each post's results from MCM, reads them by topic, post type and format, and recommends at most 5 changes for her yes — what we learned, lines worth keeping, strategy or plan changes, business file suggestions. When she says \"/content-review\", \"monthly content review\", \"how did my posts do\", \"review the content\", \"what's working\", for the Content department's monthly routine, or before planning the next 4 weeks."
---

# content-review — what the results say, once a month

Turns a month of posts into decisions. It pulls the numbers, reads them honestly, and recommends a few changes. The other skills make the changes; this one only recommends and records what we learned.

It does one thing: **review one window of results and turn them into approved learnings and hand-offs.** It never edits the strategy, the plan, her business file or a post.

Speak to her in plain, warm US English. Say "your posts", "the results", "what we learned", "your content strategy"; never file names, "skill", "API" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. The shared reference files ship with the plugin next to this skill's folder: `../content-strategy/library.md` (the strategy library) and `../content-strategy/playbook.md` (the copy playbook). Both are read-only; what's learned for her business goes into her own files.

1. `departments/content/performance-log.md` — results so far and what we learned.
2. `_system/log.md` — the last `content-review` line (where the window starts).
3. `departments/content/calendar.md` — what was published and when.
4. `departments/content/posts/*/post.md` — per post: topic, post type, format, template, hook pattern, MCM post ID.
5. `departments/content/strategy.md` — layers on, topics, post types, formats, cadence, platforms. Then `../content-strategy/platforms/<platform>.md` for each platform on: its Results section says what counts most there.
6. `departments/content/plan.md` — what's coming, so recommendations can say which slots they'd change.
7. `departments/content/ghl.md` — location, account and profile IDs.
8. `../content-strategy/library.md` — entries and statuses (unproven, working, dropped); then `departments/content/library-notes.md` and `departments/content/swipe.md`, if they exist.
9. `about-me/business.md` — for business file suggestions only. Never edited here.
10. `departments/content/brief.md` — its Next step and Current state.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Numbers are copied from MCM as they are. Nothing is estimated, rounded up or invented; a number MCM doesn't give is written as n/a."

> "Nothing is called working or not working until that kind has at least 3 posts and the account reaches more than about 100 people per post. Below that, say 'not enough to judge' and what would make it judgeable."

> "At most 5 recommendations per review, each with what, why (the numbers) and where it goes."

> "Learnings, library notes and swipe lines are written only after an explicit yes to each item. Silence or an edit request is not a yes."

> "This skill recommends; other skills change. It never edits the strategy, the plan, her business file or a post, and never the shipped library or playbook. Hand-offs run only on a yes."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 1 — Window
- From the date of the last `content-review` line in `_system/log.md` to today. First run: everything published.
- Say in one line: "Looking at <first date> to <last date>: <N> posts published."

### Step 2 — Pull the numbers (no gate: facts)
- MCM `get-posts` for the window (body: `type: all`, `accounts` as a comma-separated string, `skip`/`limit` as strings): for each published post, each platform's likes, comments and shares.
- MCM `get-statistics` with the profile IDs (not the account IDs): impressions, reach and new followers per day for the window.
- In `performance-log.md`: fill or refresh each post's row (numbers 7+ days after posting count as settled; mark fresher ones `early`), with the day's reach as the post's reach, and note the pull date. Add one line under "Account totals" for the window. If the file is missing, create it in content-post's format (Posts · Account totals · What we learned).

### Step 3 — Read
- Group by topic, post type, format, hook pattern, dark/light and platform (weigh each platform by its file's Results section); and the account trend (reach, followers) across the window.
- Apply the small-numbers rule to every group. Say plainly where the numbers are too small to mean anything.
- Note anything unusual worth a look (a post that got comments, a day reach jumped).

### Step 4 — Recommend (gate)
At most 5 items, ranked. Each: what · why (the numbers) · where it goes · our recommendation (do it, or not yet):
- **Library note** — a new or changed entry for her business, with status unproven / working / dropped and the evidence → `departments/content/library-notes.md`. A new post type or format for her catalogs only as its own item.
- **Swipe line** — a line or post that worked, with why and the evidence → `departments/content/swipe.md`.
- **Strategy change** — hand-off to content-strategy (revise).
- **Plan change** — hand-off to content-plan (refresh), naming the slots it would change.
- **Layer** — switch audience or leads on when the numbers support it (a strategy change).
- **Business file** — a suggested update to `about-me/business.md`, which waits in `_system/pending.md` for her yes.

> "Which of these do you want? Say **yes** to the ones you want (or **yes to all**), or tell me what to change."

Apply edits exactly, re-show, wait for yes.

### Step 5 — Write
On yes, for the approved items only:
1. `performance-log.md`: under "What we learned", one dated line per approved learning.
2. `library-notes.md`: approved entries under her type of business, with date, status and evidence. Create the file if missing:
   ```
   # Library notes: <business>

   Her additions to the shipped strategy library. They win over the library for her business.

   ## Catalog additions
   | Date | Post type or format | What it is | Fits | Status |
   |---|---|---|---|---|

   ## Entries
   | Date | What | Status | Evidence | Notes |
   |---|---|---|---|---|
   ```
3. `swipe.md`: approved swipe lines. Create the file if missing with `# Swipe file: <business>` and the columns `Date · Line or post · Why it worked · Evidence`.
4. Business file items: one line each in `_system/pending.md` (re-read it first), in the system's format: `- [ ] YYYY-MM-DD · add · about-me/business.md § <section> · <the exact proposed line> · (from: content review <first date> to <last date>)`.
5. Offer each approved hand-off ("Want me to update your content strategy now?" / "Want me to update the plan now?"); run it only on yes.
6. Department brief: Current state with today's date and one line on the review, and `updated:`. If a strategy or plan hand-off was approved and not run, set Next step to it ("Update the content strategy: <change>. Say \"revise the strategy\"."). Mention it in one short line.
7. Receipt and milestone (below).

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-review | reviewed / numbers-only / draft-not-approved | <first date> to <last date> · <N> posts · approved: <items or none> · hand-offs: <run / offered / none>`

## Milestone

Each review: hand /context one line for `context/content.md`:
`Content review <first date> to <last date>: <one-line read>. Approved: <changes>. Still open: <hand-offs not run, or none>.`

## What this skill never does

- Invents, estimates or rounds a number; fills a gap MCM doesn't cover with a guess.
- Calls something working or not working below the small-numbers rule.
- Writes learnings, library notes or swipe lines without an explicit yes.
- Edits `strategy.md`, `plan.md`, `calendar.md`, `ideas.md`, `posts/`, `about-me/` (business suggestions only wait in `_system/pending.md`), the shipped library or playbook, or anything in `context/` (milestones go through /context).
- Changes a library note to working without her own numbers behind it.
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Runs a hand-off without a yes.
- Deletes rows or entries. A dropped entry is marked dropped, not removed.
- Makes more than 5 recommendations.

## When to refuse

- A request to make the numbers look better, or to call something working early — "The numbers are what they are; I'll tell you what would make them worth judging." (numbers as they are, small-numbers rule)
- A request to change the strategy or plan directly from here — "That happens in the strategy or the plan. Want me to take it there?" (one owner per concern)
- MCM not connected — "MCM isn't connected right now, so I can't pull the numbers." Review only what's already in the log, and say so.
- No published posts in the window — "Nothing was published since the last review, so there's nothing to read yet."

## Failure modes

- **`get-statistics` rejects the IDs** — use the profile IDs from `ghl.md` (not the account IDs); if it still fails, review the per-post numbers only and say the account line is missing.
- **A post's child posts aren't found** — mark that row "not found in MCM", don't guess; continue with the rest.
- **A post folder has no post type or format** (older posts) — use the calendar row; if that's missing too, group it as "unknown".
- **Library notes missing a section for her type of business** — propose the section as an item; don't create it without a yes.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, recommend "not yet" and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already written (numbers pulled, learnings, library notes, swipe lines, pending items) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): read the files and the numbers and draft the read and the recommendations, then write only one receipt line marked `draft-not-approved`. Never write `performance-log.md`, library notes, swipe lines, pending items or the brief, and never start a hand-off.

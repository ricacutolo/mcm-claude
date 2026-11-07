---
name: content-plan
description: "Plans her next 4 weeks of posts — one topic, one post type and one format per slot — and flags any design template that needs building first. When she says \"/content-plan\", \"plan content\", \"plan the next 4 weeks\", \"what are we posting this month\", \"refresh the plan\", \"add formats to the plan\", \"shift the plan\", or when the Content department's next step says the plan is running out."
---

# content-plan — the next 4 weeks

Decides what gets posted when: one topic, one post type and one format per slot, for the next 4 weeks, so the account rotates instead of repeating itself and the department always knows what's next.

It does one thing: **fill the next 4 weeks of slots.** It never drafts copy, designs or schedules — that's content-post and its makers.

Speak to her in plain, warm US English. Say "the plan", "the calendar", "a template"; never file names, "skill" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. The shared reference files ship with the plugin next to this skill's folder: `../content-strategy/library.md` (the strategy library).

1. `departments/content/strategy.md` — topics, which post types and formats are on (and any format to lean on), which layers are on, cadence and slot time, idea rules.
2. `../content-strategy/library.md` — the post types catalog and the formats catalog (which post types each format fits). Then `departments/content/library-notes.md`, if it exists — her own additions to the catalogs.
3. `departments/content/calendar.md` — what's already scheduled or published, and the last topics and post types used.
4. `departments/content/plan.md` — the current plan, if any (to roll it forward).
5. `departments/content/ideas.md` — unused ideas.
6. `departments/content/templates.md` — which templates exist (a template is format × post type).
7. `departments/content/brief.md` — its Next step and Current state.
8. `about-me/about-me.md` — only her time zone.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is written to the plan before an explicit yes to the 4 weeks shown. Silence or an edit request is not a yes."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

> "Only topics in the strategy, and only post types and formats that are on. Never invent a topic or switch a type or format on."

> "A suggested angle is marked 'suggestion'. Never present it as her idea or as decided."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 1 — Find the slots
- Cadence and slot time from `strategy.md` (e.g. Tue and Thu, 12:30 PM), in her time zone (from `about-me/about-me.md`, else ask once).
- Start after the last post that is scheduled in `calendar.md` or planned in `plan.md`, whichever is later. Never re-plan a slot that's already scheduled.
- Fill 4 weeks of slots from there. Number them as post numbers, continuing from the calendar.

### Step 2 — Fill the matrix
For each slot, pick one topic, one post type and one format:
- No topic twice in a row.
- No post type repeated within 2 weeks.
- Only post types marked on in `strategy.md`.
- Format: only formats marked on in `strategy.md` that fit the post type (formats catalog, "Fits post types"). Where `strategy.md` names a format to lean on, pick it wherever it fits. No format more than 2 slots in a row unless only one fits.
- Template: the template for that format × post type in `templates.md`, or "to build: <format> × <post type>". Reels need no Canva template: write "reel". Photo posts and photo carousels need none either: write "photo". For a photo slot's idea, suggest from unused photos in `departments/content/photos.md` when it exists.
- Spread the topics: every topic appears before any topic appears a third time.
- First 2 weeks: prefer format × post type pairs that already have a template, so new templates have lead time.
- Match unused ideas from `ideas.md` to slots first (by topic, then type). Where none fits, write one suggested angle, marked "suggestion", following the idea rules in `strategy.md` (what the reader gets, never technical).
- Use the last 4 posts in `calendar.md` for the "in a row" and "within 2 weeks" checks across the plan boundary.

### Refresh (keep the slots, change one thing)
When asked to refresh the current plan for one thing (e.g. "add formats to the plan", or content-post asking to swap one slot's format), keep its slots, topics, post types and ideas exactly as approved, change only what was asked, and show the result at the gate. The approved version moves under Past plans when the refresh is written.

### Refresh: shift after a missed slot
When content-post moved a missed post onto the next slot (or she asks to shift the plan): every `planned` slot from that point moves one slot later in the cadence, keeping its topic, post type, format, template and idea. The plan keeps its 4 weeks: the last slot moves past the horizon and goes to the top of the next plan. Recompute the template build-by dates (3 days before the first slot that uses each). Re-check "no topic twice in a row" and "no post type within 2 weeks" across the shifted slots and say if one now breaks. Show it at the gate as a refresh.

### Step 3 — Templates to build
- List every format × post type in the plan whose template is "to build", with a build-by date 3 days before its first slot.

### Step 4 — Gate
Show the plan as a table: post # · date · topic · post type · format · template · idea (or suggestion). Then the templates to build.

> "Does the plan work? Say **yes**, or tell me what to change."

Apply edits exactly, re-show, wait for yes.

### Step 5 — Write
On yes:
1. `plan.md`: create it if missing (header: "# Content plan: <business>" and one line on how it works). Move the previous current plan, if any, under `## Past plans` with its dates. Write the approved plan under `## Current plan (<first date> to <last date>)`, columns: # · date · slot · topic · post type · format · template · idea · status (`planned`). Keep any slot's status other than `planned` as it is. Then `### Templates to build`.
2. Department brief: set Next step to the next unscheduled slot ("Post N, <day date>, <time>: <topic> × <post type>, <format>. Say \"next post\"."), or "Build the <format> × <post type> template by <date>. Say \"build the next template\"." if one is due first. Update Current state with its date and one line on the plan, and `updated:`. Touch nothing else; mention it in one short line.
3. Receipt and milestone (below).

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-plan | planned / refreshed / shifted / draft-not-approved | <first date> to <last date> · posts <first #>-<last #> · templates to build: <list or none>`

## Milestone

Each approved run: hand /context one line for `context/content.md`:
`Content plan <first date> to <last date> approved: <N> posts. Next: <the brief's new Next step>. Templates to build: <list, or none>.`

## What this skill never does

- Writes `plan.md` without an explicit yes.
- Re-plans or moves a slot that's already scheduled in GoHighLevel or the calendar. A shift after a missed slot moves only `planned` slots.
- Edits `strategy.md`, `calendar.md`, `ideas.md`, `templates.md`, `library-notes.md`, the shipped library, or anything in `context/`. It only reads them.
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Invents topics, switches post types or formats on, or presents a suggested angle as decided.
- Drafts copy, designs, builds templates or schedules posts.
- Deletes a past plan — it moves under Past plans.

## When to refuse

- No `strategy.md`, or one without topics or post types — "There's no content strategy with topics yet, so there's nothing to plan from. Want to set it up first?" (the plan fills a strategy, it doesn't make one)
- No cadence or slot time in `strategy.md` — "The strategy doesn't say when you post yet. Let's set that first." (no slots to fill; offers content-strategy on yes)
- A request to plan more than 4 weeks — "The plan is 4 weeks at a time; we plan the next 4 when it runs low."

## Failure modes

- **Fewer topics or post types than the rotation rules need** (e.g. 2 topics) — relax "spread the topics" first, then "within 2 weeks"; never relax "no topic twice in a row" unless only 1 topic exists. Say which rule was relaxed.
- **Calendar and plan disagree** (a planned slot already scheduled with something else) — the calendar wins; re-number and say so.
- **Catalog missing a post type that the strategy lists** — plan it with template "to build" and flag it.
- **No format that's on fits a post type** — say so and leave the slot's format blank for her to pick at the gate; never switch a format on.
- **Department brief missing** — write `plan.md` only, skip the brief, say so.
- Prefer doing less: when unsure, stop at the gate and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already written (`plan.md`, brief lines, receipt) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): read the files and build the draft plan, then write only one receipt line marked `draft-not-approved`. Never write `plan.md` or the department brief without her yes.

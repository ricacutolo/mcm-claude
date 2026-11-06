---
name: content-strategy
description: "Sets up or revises her content strategy — who she posts for, what content is for right now, topics, post types, formats, when she posts and the one call to action — starting from what's already known about her business, then offers to plan the next 4 weeks. When she says \"/content-strategy\", \"set up my content strategy\", \"revise the strategy\", \"update the content strategy\", \"change what I post about\", after the monthly content review recommends it, or during the content setup."
---

# content-strategy — set up or revise

Decides how her content works: who it's for, what it's for right now, and what it picks from (topics, post types, formats). It starts from what's already known about her business, so she answers as few questions as possible.

It does one thing: **set or revise her content strategy.** It never plans slots (that's content-plan), makes posts (content-post) or edits her business file.

Speak to her in plain, warm US English. Say "your content strategy", "your business file", "the plan"; never file names, "skill", "layer" without explaining it, or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. Two reference files ship with the plugin in this skill's own folder, and other skills read them from here: `library.md` (the strategy library: post types, formats, entries by type of business) and `playbook.md` (the copy playbook). Both are read-only.

1. `about-me/business.md` — what she sells, who she sells to, what those people believe, objections, pains, why customers pick her, how she sells, booking, goals, what's off-limits. Always the current file, never a remembered copy.
2. `library.md` — the post types and formats catalogs, and entries for her type of business. Then `departments/content/library-notes.md`, if it exists — her own entries and catalog additions; they win for her business.
3. `playbook.md` — CTA by layer, awareness levels.
4. `departments/content/strategy.md` — if it exists (revise mode), including its "Deliberate differences from the business file".
5. Revise mode only: `departments/content/performance-log.md` ("What we learned") and the last `content-review` line in `_system/log.md`.
6. `about-me/writing.md` — for the voice of the strategy's own wording.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is written to the strategy before an explicit yes to the full draft shown. Silence or an edit request is not a yes."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

> "Her business file is read, never edited. Where the strategy differs from it, say so as a suggestion; she decides, and a change to the business file waits in `_system/pending.md` for her yes."

> "A difference she has marked as deliberate is never flagged again."

> "Only post types and formats from the library catalogs or her library notes. A new one goes into her library notes first, through the monthly content review."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 1 — Mode
- No `strategy.md` → **setup** (round 1).
- `strategy.md` exists → **revise** (next round). Say what triggered it: her request, or a content-review recommendation (quote it).

### Step 2 — Draft from what's known
From her business file and the library, draft every section:
- **Who we post for** — from who she sells to.
- **Topics** — 4-8, from her customers' pains, objections and what they believe about the problem, in her customers' words.
- **Wedge** — from why customers pick her.
- **CTA** — from her booking flow, matched to the layer that's on (playbook).
- **Idea rules** — from how she sells and what's off-limits, plus the playbook's rules.
- **Library entries for her type of business** — anything marked working; unproven ones only as options.
In revise mode, start from the current strategy and change only what the trigger calls for.

### Step 3 — Ask only what the business file doesn't answer
At most 6 questions, one message, each with a recommended answer:
1. What is content for right now — which layers are on: credibility (people checking you out trust what they see), audience (more people find you), leads (posts bring in inquiries)?
2. Face on camera: yes, no or sometimes?
3. Which photos exist (her own work, team, place), and are customer photos OK?
4. How much time per week for content?
5. Cadence, days, time and platforms.
6. Any format to lean on, or post types to switch off?
Skip any question the business file, the current strategy or the conversation already answers. If her time zone isn't in `about-me/about-me.md`, ask it with question 5.

### Step 4 — Business file check
List where the draft differs from her business file (audience, offer, CTA, tone). For each: one line, and a choice — "update the business file" (a suggested line) or "keep as a deliberate difference". Skip differences already listed under "Deliberate differences from the business file".

### Step 5 — Gate
Show the full strategy draft, the business file check, and in revise mode what changed from the last round.

> "Does the strategy work? Say **yes**, or tell me what to change."

Apply edits exactly, re-show, wait for yes. Differences she keeps go under "Deliberate differences from the business file". Business file updates she picks go to `_system/pending.md` (below).

### Step 6 — Write
On yes:
1. Revise mode: copy the current `strategy.md` to `departments/content/past-rounds/strategy-round-<N>.md` (create the folder if missing) before writing.
2. Write `departments/content/strategy.md`, headed "# Strategy: <business>, round <N>" and "Status: CONFIRMED round <N> (<her name>, <date>)", with sections: Who we post for · Deliberate differences from the business file · What content is for right now (layers) · The one CTA · Wedge · How posts are picked: topic × post type × format (Topics, Post types on, Formats on) · Idea rules · Cadence (days, time, time zone, platforms) · Templates · Voice.
3. Each business file update she picked: one line in `_system/pending.md` (re-read it first), in the system's format: `- [ ] YYYY-MM-DD · add · about-me/business.md § <section> · <the exact proposed line> · (from: content strategy round <N>)`. The time zone, if she gave one and it isn't in `about-me/about-me.md`: the same, for that file.
4. Department brief: update Current state (date, one line on the round) and `updated:`. If there's no current plan, or the change affects planned slots, set Next step to "Plan the next 4 weeks. Say \"plan content\"." Touch nothing else; mention it in one short line.
5. Receipt and milestone (below).

### Step 7 — Hand off
> "Want me to plan the next 4 weeks now?"

Run content-plan only on yes.

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-strategy | setup / revised / draft-not-approved | round <N> · trigger: <request / content-review / content setup> · business file suggestions: <N pending, or none>`

## Milestone

Each approved run: hand /context one line for `context/content.md`:
`Content strategy round <N> approved: layers <list>, <count> topics, formats <list>. Still open: <plan the next 4 weeks / business file suggestions pending / none>.`

## What this skill never does

- Writes `strategy.md` without an explicit yes.
- Edits `about-me/business.md` or any `about-me/` file. Changes there only wait in `_system/pending.md`.
- Re-flags a difference marked as deliberate.
- Edits `library.md`, `playbook.md`, `library-notes.md`, `swipe.md`, `plan.md`, `calendar.md`, `ideas.md` or anything in `context/` (milestones go through /context).
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Invents post types or formats outside the catalogs, or claims something "works" without the library or her notes marking it working.
- Deletes an old strategy round — it goes to `past-rounds/`.
- Runs content-plan without a yes.

## When to refuse

- No business file and no answers to work from — "There's nothing to build the strategy from yet. Let's fill in your business file first, or you can answer a few setup questions." (the strategy starts from what's known)
- A request to make up results or proof — "The strategy only uses what's real; results go in once we have them." (real things only)
- A request to switch on a post type or format that isn't in the catalogs — "Let's add it to your library notes first (the monthly review does that), then switch it on." (one owner per concern)

## Failure modes

- **Business file thin or out of date** — draft what it supports, ask the gaps in Step 3, and add "update the business file" as a suggestion.
- **Library missing a catalog** — use what exists, flag the gap, never invent entries.
- **She stops mid-questions** — keep the answers in the conversation; write nothing to `strategy.md`; receipt `draft-not-approved`.
- **Department brief missing** — write `strategy.md` only; say so.
- **`_system/pending.md` can't be read** — keep the suggestions in the conversation and say they weren't saved.
- Prefer doing less: when unsure, stop at the gate and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already written (past-rounds copy, `strategy.md`, pending items, brief lines, receipt) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): read the files and draft the strategy and the business file check, then write only one receipt line marked `draft-not-approved`. Never write `strategy.md`, `past-rounds/`, pending items or the department brief without her yes.

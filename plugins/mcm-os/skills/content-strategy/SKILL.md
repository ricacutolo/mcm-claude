---
name: content-strategy
description: "Sets up or revises her content strategy — who she posts for, what content is for right now, topics, post types, formats, when she posts and the one call to action — starting from what's already known about her business, then offers to plan the next 4 weeks. When she says \"/content-strategy\", \"set up my content strategy\", \"revise the strategy\", \"update the content strategy\", \"change what I post about\", after the monthly content review recommends it, or during the content setup."
---

# content-strategy — set up or revise

Decides how her content works: who it's for, what it's for right now, and what it picks from (topics, post types, formats). It starts from what's already known about her business, so she answers as few questions as possible.

It does one thing: **set or revise her content strategy.** It never plans slots (that's content-plan), makes posts (content-post) or edits her business file.

Speak to her in plain, warm US English. Say "your content strategy", "your business file", "the plan"; never file names, "skill", "layer" without explaining it, or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. Two reference files ship with the plugin in this skill's own folder, and other skills read them from here: `library.md` (the strategy library: post types, formats, entries by type of business) and `playbook.md` (the copy playbook). Both are read-only. A third set ships in `platforms/`: one read-only file per platform (`platforms/README.md` explains them). The platforms line in her strategy is the switch: every content skill reads only the files for the platforms on it.

1. the business file of the area in play (`about-me/business-brain.md`, or `business-brain-<area>.md` per /system's **Areas**) — what she sells, who she sells to, what those people believe, objections, pains, why customers pick her, how she sells, booking, goals, what's off-limits. Always the current file, never a remembered copy.
2. `library.md` — the post types and formats catalogs, and entries for her type of business. Then `departments/content/library-notes.md`, if it exists — her own entries and catalog additions; they win for her business.
3. `playbook.md` — CTA by layer, awareness levels. Then `platforms/README.md` and the file for each platform she has or might use (each file's "When to recommend it").
4. `departments/content/strategy.md` — if it exists (revise mode), including its "Deliberate differences" and its `Follows:` line.
4b. the CEO strategy (`departments/ceo/strategy.md`, or `strategy-<area>.md` for the area in play) — if it exists: its **Directions → Content**, first offer, how it sells and next 90 days. The CEO decides what content is for; this skill decides how. Never written here.
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
From the CEO's direction for content (when there is one), her business file and the library, draft every section. With a direction, "What content is for right now" (the layers) and the CTA come from it; without one, from the business file as below. In revise mode, a CEO strategy newer than the `Follows:` date is a trigger on its own: say what changed in the direction, in one line.
- **Who we post for** — from who she sells to.
- **Topics** — 4-8, from her customers' pains, objections and what they believe about the problem, in her customers' words.
- **Wedge** — from why customers pick her.
- **How posts end** — the business ask, from her booking flow and matched to the layer that's on (playbook § 7), plus the ask rhythm: about 1 post in 3 carries the ask; the rest end lightly (save it, a question to answer in the comments) or with nothing at all. The plan marks which slots carry the ask.
- **Idea rules** — from how she sells and what's off-limits, plus the playbook's rules.
- **Library entries for her type of business** — anything marked working; unproven ones only as options.
In revise mode, start from the current strategy and change only what the trigger calls for.

### Step 3 — Ask only what the business file doesn't answer
At most 6 questions, one message, each with a recommended answer:
1. (Skipped when the CEO's direction says it.) What is content for right now — which layers are on: credibility (people checking you out trust what they see), audience (more people find you), leads (posts bring in inquiries)?
2. Face on camera: yes, no or sometimes? (Skipped when the content setup already asked about reels: its answer in `setup.md` decides whether reels are on.)
3. Which photos exist (her own work, team, place), and are customer photos OK? (Photos go in a Google Drive folder, Content photos, whenever she has them; posts pick from there.)
4. How much time per week for content?
5. Cadence, days, time and platforms. Recommend platforms from each platform file's "When to recommend it": Instagram always, Facebook when she has a Page, LinkedIn when she sells to professionals, the newsletter (`platforms/newsletter.md`) when she sells something people decide on over time and has a list, Substack (`platforms/substack.md`) only with the newsletter on, when her expertise is what she sells or she already has a Substack (light: each issue goes there too, plus 2-3 Notes a week from what she's already making). If the content setup already noted her platforms, start from those. Newsletter on: how often (every two weeks for a new list, weekly once she's keeping up), day and time (Tuesday morning by default), and how often an issue is an offer (one in four or five), and whether the newsletter leads the theme (recommend yes: each issue sets the topic for the posts until the next one).
6. Any format to lean on, or post types to switch off?
Skip any question the business file, the current strategy or the conversation already answers. If her time zone isn't in `about-me/about-me.md`, ask it with question 5.

### Step 4 — Business file and direction check
List where the draft differs from her business file (audience, offer, CTA, tone). For each: one line, and a choice — "update the business file" (a suggested line) or "keep as a deliberate difference". Skip differences already listed under "Deliberate differences from the business file".
Then, with a CEO direction: where the draft goes against it (she wants it so), one line each with her reason, kept under "Deliberate differences from the CEO's direction". Never silently; never an edit to the CEO strategy.

### Step 5 — Gate
Show the draft so she sees the thinking behind it, not a preset. In this order:

1. **What your content is for:** the three options (trust, audience, leads) and the pick, in a short paragraph with the reason tied to her business (or the CEO's direction).
2. **Kinds of posts:** a short paragraph first ("Here's my pick: I turned these on because …"), then every post type in the library catalog (and her library notes), each with a few-word gloss and its mark: **[On]** or **[Off]**.
3. **Formats:** the same: the paragraph, then every format in the catalog, **[On]** or **[Off]**. The reason names what drives it (face, photos, time).
4. **Where:** the same, every platform file: **[On]** or **[Off]**.
5. **How your posts end:** the paragraph, then the list, each line with its rhythm: **[On]** The ask ("<her ask, in her words>") · about 1 post in 3 / **[On]** Save it for later · about 1 in 3 / **[On]** A question to answer in the comments · about 1 in 4 / **[On]** No ask, just value · the rest / **[Off]** Share it with someone who needs it / **[Off]** Follow for more / **[Off]** Comment a word to get something (comes with leads). The rhythm is her strategy's own; these are the defaults for credibility.
6. **When:** a short paragraph with the pick and why.
7. "Want something on or off? Just tell me."
8. **Changing things later:** "change the plan", "review my strategy", and "make this a post" for an idea in the middle of the plan.

Then the business file check, and in revise mode what changed from the last round.

> "Reply with **1** or **2**: 1. This works 2. Change something. Or tell me what you're thinking." (one option per line, as in /system's reply rules)

Apply edits exactly, re-show, wait for yes. Differences she keeps go under "Deliberate differences from the business file" (or "from the CEO's direction"). Business file updates she picks go to `_system/pending.md` (below).

### Step 6 — Write
On yes:
1. Revise mode: copy the current `strategy.md` to `departments/content/past-rounds/strategy-round-<N>.md` (create the folder if missing) before writing.
2. Write `departments/content/strategy.md`, headed "# Strategy: <business>, round <N>", "Status: CONFIRMED round <N> (<her name>, <date>)" and "Follows: CEO strategy of <its `updated:` date>" (or "Follows: no CEO strategy yet (business file)"), with sections: Who we post for · Deliberate differences from the business file · Deliberate differences from the CEO's direction (only when there is one) · What content is for right now (layers) · How posts end (the ask, in her words, and the rhythm: each ending, on or off, and how often) · Wedge · How posts are picked: topic × post type × format (Topics, Post types on, Formats on) · Idea rules · Cadence (days, time, time zone, platforms: the switch the other content skills read; reels on or off; a separate LinkedIn time only if it differs; the newsletter line when it's on: how often, day and time, offer issues, newsletter leads the theme: yes/no; the Substack line when it's on: Notes a week, 2 or 3) · Templates · Voice.
3. Each business file update she picked: one line in `_system/pending.md` (re-read it first), in the system's format: `- [ ] YYYY-MM-DD · add · about-me/business-brain.md § <section> · <the exact proposed line> · (from: content strategy round <N>)`. The time zone, if she gave one and it isn't in `about-me/about-me.md`: the same, for that file.
4. Department brief: update Current state (date, one line on the round) and `updated:`. If there's no current plan, or the change affects planned slots, set Next step to "Plan the next 4 weeks. Say \"plan content\"." Touch nothing else; mention it in one short line.
5. Receipt and milestone (below).

### Step 7 — Hand off
> "Want me to plan the next 4 weeks now?"

Run content-plan only on yes.

No CEO strategy, and none offered yet (no `CEO session offered` line in `strategy.md`): offer it once, after the plan question: "Your content gets sharper once your business strategy is set. Want to do that session?" Run /business-strategy only on yes. Either way, add `CEO session offered: YYYY-MM-DD` under the strategy's header so it isn't offered again.

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-strategy | setup / revised / draft-not-approved | round <N> · trigger: <request / content-review / content setup> · business file suggestions: <N pending, or none>`

## Milestone

Each approved run: hand /context one line for `context/content.md`:
`Content strategy round <N> approved: layers <list>, <count> topics, formats <list>. Still open: <plan the next 4 weeks / business file suggestions pending / none>.`

## What this skill never does

- Writes `strategy.md` without an explicit yes.
- Edits `about-me/business-brain.md` or any `about-me/` file. Changes there only wait in `_system/pending.md`.
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

---
name: content-template
description: "Builds one Canva design template for her posts — one format for one post type, like an illustrated carousel for Leak posts — layout first, then the design in Canva with native diagrams, then the fill guide, with her yes at each step. When she says \"/content-template\", \"build the next template\", \"build the illustrated template\", \"make a template for post 5\", when the plan has a template due, or when a post stops because its template isn't built yet."
---

# content-template — one Canva template, format × post type

Builds the templates content-static fills. A template is one format × one post type (e.g. illustrated carousel × Leak). It is built once, the first time the plan schedules that pair, and copied for every post after.

It does one thing: **build one Canva template and its fill guide.** It never makes posts, writes copy for a real post, or changes the plan beyond its template cells.

Speak to her in plain, warm US English. Say "the template", "the layout", "the plan"; never file names, "skill", "API", "token" or a command name. To her, placeholders are "the spots where each post's words go".

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. The shared reference files ship with the plugin next to this skill's folder: `../content-strategy/library.md` (the strategy library), `../content-strategy/playbook.md` (the copy playbook) and `../content-install/guides.md` (Guide B: hand fixes in Canva).

1. `departments/content/plan.md` — "Templates to build": what's due, by when, and which slots use it.
2. `departments/content/templates.md` — the templates that exist, their Canva IDs and fill guides.
3. `departments/content/brand-style.md` — color roles, font roles, logo; `about-me/brand.md` when it exists, for the logo files.
4. `departments/content/strategy.md` — which formats and post types are on.
5. `../content-strategy/library.md` — the format and post type definitions; then `departments/content/library-notes.md`, if it exists.
6. `../content-strategy/playbook.md` — structure per post type (slide count, what each slide holds).
7. `departments/content/brief.md` — its Next step and Current state.
8. Canva: the existing TEMPLATE designs, read only, to pick the one to copy.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Two gates, in order: layout, then design. Nothing is built in Canva before the layout gets a yes; nothing is committed, titled TEMPLATE or written to templates.md or plan.md before the design gets a yes. Silence or an edit request is not a yes."

> "Never edit an existing TEMPLATE design. Always build on a copy."

> "Diagrams are native Canva shapes, lines and text in brand colors — no AI-generated images, no stock illustrations."

> "Every placeholder is a unique token in square brackets ([HOOK], [POINT 1 TITLE]), so content-static can fill it with find-and-replace."

> "Only formats and post types that are on in the strategy and defined in the library or her library notes."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 1 — Pick the template
- The first line in the plan's "Templates to build" not marked built, or the template she names.
- Say in one line: "Building the <format> template for <post type> posts, due <date>, for posts <N, M>."
- If an existing template can serve with no new layout (same format, same structure), say so and recommend reusing it instead of building.

### Step 2 — Layout (gate 1)
- From the playbook's structure for the post type and the library's format definition, draft the template slide by slide, as one table: slide · what it holds · tokens · which regions are in the accent color · diagram (if any) · light or dark.
- Diagrams are a fixed skeleton per post type, built from rounded boxes, simple icons (SVG paths) and arrows, with label tokens ([STEP 1], [BREAK]). Name the skeleton in one line (e.g. Leak: lead → step → step, a break marked between two steps).
- Recommend which existing template to copy and why (fonts and logo carry over; fonts can't be set from here).
- Note what will need a hand fix (e.g. a new text box Canva adds without the brand font).

> "Does the layout work? Say **yes**, or tell me what to change."

Apply edits exactly, re-show, wait for yes.

### Step 3 — Build in Canva
- `copy-design` the chosen template; title the copy "DRAFT - <Format> - <Post type>".
- Open an editing transaction and read every page.
- Restructure to the approved layout: add, reorder or delete pages; reposition, resize, recolor or delete elements; set page backgrounds from the brand-style color roles.
- Text: reuse existing styled text elements wherever possible (move, resize, `find_and_replace_text` with the tokens). Use `add_text` only where no styled element can serve, and list each one as a hand fix.
- Accent regions: keep the template's two-region pattern (a light or dark region + an accent region) so content-static can move where the accent starts. Never recolor part of a one-color text box with `format_text`.
- Diagrams: `insert_shape` for boxes and icons (paths use only M/L/H/V/C/S/A/Z), lines with arrow markers connected to the boxes, label tokens inside. Brand colors only. Group each diagram.
- Check every slide's thumbnail: overflow, collisions, text off the canvas, arrows not meeting their boxes, a box that jumped after a resize. Fix by resizing or repositioning.

### Step 4 — Design (gate 2)
- Send the previews, and list the hand fixes only she can do in Canva (fonts on new text, logo placement, anything that can't be styled from here), with Guide B's clicks.

> "Does the design work? Say **yes** and I'll save it, or tell me what to change."

- On yes: commit the transaction **immediately** (open transactions expire), then retitle to "TEMPLATE - <Format> - <Post type>".
- If she then makes the hand fixes in Canva, re-read the design before Step 5 so the fill guide matches.

### Step 5 — Write
On the design yes:
1. `templates.md`: add one row (template, Canva ID, format, slides, use for) and a fill guide under it: the token map by slide, where the accent starts in each two-region text, how to fill the diagram labels, light or dark, hand fixes still open.
2. `plan.md`: in the current plan, set the Template cell of each slot this template serves; in "Templates to build", mark the line built with the date and Canva ID. Touch no other cell.
3. Department brief: if the next post needed this template, set Next step to that post ("Post N, <day date>, <time>: <topic> × <post type>. Say \"next post\"."); otherwise leave Next step as it is. Update Current state with today's date and one line, and `updated:`. Mention it in one short line.
4. Receipt and milestone (below).

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-template | layout-approved / built / stopped-at-<gate> / draft-not-approved | <format> × <post type> · Canva <design ID> · serves posts <N, M> · hand fixes: <list or none>`

## Milestone

Each template built: hand /context one line for `context/content.md`:
`Template built: <format> × <post type> (Canva <design ID>), serves posts <N, M>. Still open: <hand fixes, or none>.`

## What this skill never does

- Builds in Canva before the layout gets a yes, or commits, titles TEMPLATE, or writes files before the design gets a yes.
- Edits an existing TEMPLATE design.
- Uses AI-generated images or stock illustrations for diagrams.
- Writes copy for a real post, drafts captions, or schedules anything — that's content-static.
- Edits `strategy.md`, `brand-style.md`, `calendar.md`, `ideas.md`, `posts/`, `about-me/`, the shipped library, playbook or guides, or anything in `context/` (milestones go through /context).
- Changes `plan.md` beyond the Template cells of the slots it serves and its line in "Templates to build".
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Deletes Canva designs or files. A draft without a yes stays titled DRAFT for her to keep or delete.
- Builds more than one template per run.

## When to refuse

- A format or post type that's off in the strategy, or missing from the library — "That one isn't switched on in your content strategy. Want to switch it on first?" (only what's on; offers content-strategy on yes)
- A request to edit an existing TEMPLATE in place — "I'll build on a copy; the original stays as it is." (never edit a template)
- A request to skip the layout step — "One look at the layout first; it's cheap to change before anything is built."
- A request for AI-drawn or stock illustrations — "Diagrams are built from Canva shapes so they stay editable and every post can fill them in."
- Canva not connected — "Canva isn't connected right now, so I can't build the template." Stop after the layout gate.

## Failure modes

- **No closer template to copy** — copy the nearest one anyway for fonts and logo; more of the build becomes hand fixes; say so at the layout gate.
- **A Canva operation is rejected** (e.g. a shape path it won't take) — simplify the shape once; if it still fails, leave it as a hand fix.
- **Canva transaction expired before commit** — open a new transaction, re-apply only the approved edits, re-show the previews, commit on yes. Never claim it saved.
- **Canva 409 / `polled_too_early`** — wait and retry once; then report and stop.
- **`plan.md` missing or has no "Templates to build"** — build the named template; skip the plan writes; say so.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, commit no open Canva transaction. Report what was already done (draft design ID, files written) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): pick the template and draft the layout table, then write only one receipt line marked `draft-not-approved`. Never touch Canva, `templates.md`, `plan.md` or the brief.

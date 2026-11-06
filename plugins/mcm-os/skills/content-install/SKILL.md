---
name: content-install
description: "Walks her through setting up the content machine in 20 steps — her Content department, Canva, her brand on the design templates, GoHighLevel, the upload path and the strategy — with a recommendation at each step, picking up where she left off. When she says \"/content-install\", \"set up the content machine\", \"set up my content\", \"continue content setup\", \"where are we in the content setup\", or when the Content department's next step says the setup is open."
---

# content-install — ready for the first post

Gets her content machine ready: the Content department, Canva, her brand on the design templates, GoHighLevel, the upload path and the strategy. It walks the steps in order, opens every step with the answer we'd pick and why, decides small details for her and notes them, and picks up where it left off.

It does one thing: **get her content machine ready for its first post.** It never writes the strategy, plans posts or makes posts — it hands off to the skills that do.

Speak to her in plain, warm US English, in her voice rules from `about-me/writing.md`: plain words, nothing technical. Say "Canva connected to Claude", "your GoHighLevel connected to Claude", "the settings file in your content folder"; never "connector", "MCP", "API", "token", file names, "skill" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. This skill ships two things in its own folder: `guides.md` (Canva Guides 0, A and B, handed to her at the Canva steps, and Guide C for connecting GoHighLevel) and `scripts/` (the upload and transcription scripts copied into her content folder).

1. `departments/content/setup.md` — progress and the resume point. If missing, this is a new setup.
2. `departments/content/brief.md` — whether the department exists; its Next step and Current state.
3. `departments/content/brand-style.md`, `templates.md`, `ghl.md` — if they exist, to know what's already filled.
4. `about-me/brand.md` — her colors, fonts and logo files, if her brand kit exists.
5. `about-me/business.md` and `about-me/writing.md` — only to check they exist and are filled in. Never edited here.
6. `guides.md` — when a Canva step needs it.

Never read or print `departments/content/.env`. Step 19 checks only whether a key is set.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Every step opens with a recommendation: the answer we'd pick and why. She confirms or changes it. Small details get decided and noted, not asked."

> "brand-style.md, templates.md and ghl.md are written only after an explicit yes to the content shown. Silence or an edit request is not a yes."

> "Checks are read-only. A check never creates, edits, sends or connects anything."

> "Template rebrands are saved only after an explicit yes to the previews. Only her own fresh copies are edited, never a shared original."

> "The GoHighLevel key goes into .env by her own hand. Never ask for it in chat, never read it, never print it."

> "Hand-offs (new-department, install, brand-kit-designer, content-strategy) run only on a yes."

> "setup.md, the receipt and the department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

## The steps

| # | Stage | Step | Done when | How |
|---|---|---|---|---|
| 1 | Home | Content department exists | `departments/content/brief.md` exists | If missing → offer /new-department (content) |
| 2 | Home | Setup tracker | `setup.md` exists | Create it (format below) |
| 3 | Business | Business file filled in | `about-me/business.md` exists with offer, audience and pains | Missing → offer /install. Thin → ask what's missing (at most 3 questions) and add the lines to `_system/pending.md` as items for `about-me/business.md`; done when they're written |
| 4 | Business | Voice captured | `about-me/writing.md` exists with real samples | Missing → offer /install. No samples → ask her for 2-3 things she wrote and add them to `_system/pending.md` as an item for `about-me/writing.md` |
| 5 | Canva | Canva account | she confirms | Guide 0. Recommend Free to start; skip Pro trials |
| 6 | Canva | Canva connected to Claude | `list-brand-kits` answers | She connects Canva in Claude's Settings > Connectors; then check |
| 7 | Canva | Brand Kit colors | she confirms 3 colors added | No `about-me/brand.md` → offer /brand-kit-designer first (her logo and colors), run on yes. Then Guide A, with dark, light and accent from `about-me/brand.md` (else from `business.md` or her website) |
| 8 | Canva | Logo in Uploads | she confirms light and dark versions uploaded | No `about-me/brand.md` and she declined the brand kit in step 7 → offer it once more, or use the logo files she has. Guide B step 3, with the files named in `about-me/brand.md` |
| 9 | Canva | Base templates | each base template copied into her Canva, rebranded, titled TEMPLATE, design ID known | Recommend MCM's base templates. MCM shares each one to her Canva email as "Can edit" (by hand: Canva can't share from here). She opens it under "Shared with you" and uses File > Make a copy. Claude rebrands each copy (below). If she has her own Canva templates, those can serve instead |
| 10 | Canva | Brand style | `brand-style.md` approved and written | Draft color and font roles and logo files, seeded from `about-me/brand.md` when it exists; show; write on yes |
| 11 | Canva | Template index | `templates.md` has the base templates | Draft the rows and fill guides; show; write on yes |
| 12 | GHL | Social accounts | she confirms Instagram (and Facebook) connected in GoHighLevel's Social Planner | She does it in GoHighLevel |
| 13 | GHL | Her GoHighLevel connected to Claude | the GoHighLevel connection lists her business (sub-account) and `get-account` lists its social accounts | Guide C: she adds GoHighLevel as a custom connector in Claude, signs in, picks her business and approves the permissions, social posts read and write included; she starts a new conversation so the connection loads; then check. If the social accounts don't list, she reconnects and makes sure social posts were approved |
| 14 | GHL | GoHighLevel details | `ghl.md` approved and written | Location, user, social account and profile IDs, token expiry dates from the check; show; write on yes |
| 15 | GHL | Reconnect warning | `ghl.md` has every account's token expiry date | Nothing to schedule: content-post reads `ghl.md` every run and warns 14 days before an expiry. Tell her that's how she'll hear about it |
| 16 | Upload | Computer linked | a command on her computer answers | If not, tell her to open this chat in the Claude desktop app on the computer that holds her Claude folder |
| 17 | Upload | Allowed sites | both sites reachable from her computer | Test `export-download.canva.com` and `services.leadconnectorhq.com`. Any answer from the site counts as reachable, even a 403 (Canva answers 403 at its root). Blocked looks different: the computer's network filter refuses it (`X-Proxy-Error: blocked-by-allowlist`). If blocked, she adds them in Claude's settings |
| 18 | Upload | Upload script | `departments/content/scripts/canva-to-ghl.sh` exists | Copy `scripts/canva-to-ghl.sh` from this skill's folder, unchanged |
| 19 | Upload | GoHighLevel key | `.env` has `GHL_PIT` set | Create `departments/content/.env` with an empty `GHL_PIT=` line if missing; she makes a Private Integration key (medias scope) in GoHighLevel and pastes it into the file; the check prints only "set" or "not set" |
| 20 | Strategy | Strategy | `departments/content/strategy.md` exists | Offer /content-strategy (it then offers to plan the first 4 weeks) |

Order: stages in order. Within a stage, a step that waits on her doesn't block the next step that doesn't need it — say which one is waiting.

## Workflow

### Step 1 — Where are we
- If `setup.md` exists: read it, run the read-only checks for any step marked open, and update the ones the checks now prove done.
- If it doesn't: check every step against "Done when", so steps already done are recorded as done, with how we know.
- Show the status in one table (step, status, what's waiting) and name the next step with its recommendation. For "where are we", stop here.

### Step 2 — Work the next step
- Open with the recommendation: "We'd do <X>, because <why>. OK, or would you change it?"
- Her steps (5, 7, 8, 9 copy, 12, 13 connect, 19 paste): give the guide's steps in plain words, one at a time (`guides.md`), then wait for "done" and run the check where there is one.
- Hand-off steps (1, 3, 4, 7 brand kit, 20): offer the skill; run it only on yes. When it finishes, re-check and continue.
- **Step 9 rebrand**, on each of her copies (through her Canva connection): change the base templates' colors (#0E2D36 dark, #FAF8F4 light, #E7963D accent) to her dark, light and accent from step 7 on shapes, text and page backgrounds; swap the base logo for hers from step 8; keep the layout and every text region as it is. Show the previews and list hand fixes (elements Canva won't let me recolor from here, such as image-filled rules; fonts if the copy lost them), with Guide B's clicks.

> "Do these look right? Say **yes** and I'll save them, or tell me what to change."

  On yes, commit and retitle each "TEMPLATE - <format> - <post type>"; their design IDs go to step 11.
- **Step 9 with her own templates:** read each one; if its text sits in editable text boxes, it can serve. Say which ones need placeholders added and add them only on yes. If a design is a flat image, it can't serve; recommend MCM's base instead.
- File steps (10, 11, 14): draft from what's known, show the full content.

> "Does this look right? Say **yes** and I'll save it, or tell me what to change."

  Apply edits exactly, re-show, write on yes.
- After each step, update `setup.md` (status, date, how we know, decisions noted). No approval needed.

**`brand-style.md` (step 10):**

```markdown
# Brand style: <business>

Seeded from about-me/brand.md on YYYY-MM-DD. The content machine's own roles; brand.md stays the source for the brand itself.

## Colors
| Role | Hex | Used for |
|---|---|---|
| Dark | | dark slide backgrounds, text on light |
| Light | | light slide backgrounds, text on dark |
| Accent | | the words that sting, numbers, arrows |

## Fonts
| Role | Font | Notes |
|---|---|---|
| Heading | | set on the templates (not in the Brand Kit on Free) |
| Body | | |

## Logo
- Light version (for dark slides): <file> · in Canva Uploads: yes/no
- Color version (for light slides): <file> · in Canva Uploads: yes/no
```

**`ghl.md` (step 14):**

```markdown
# GoHighLevel: <business>

Not secret. The key lives in .env, never here.

- Location ID:
- User ID (posts are scheduled as):

| Platform | Account ID | Profile ID | Token expires |
|---|---|---|---|
| Instagram | | | YYYY-MM-DD |
| Facebook | | | YYYY-MM-DD |
```

### Step 3 — Close the run
- When all 20 are done: mark `setup.md` complete. The department's Next step becomes the first planned post from `plan.md` if the plan was made ("Post 1, <day date>, <time>: <topic> × <post type>. Say \"next post\"."), otherwise "Set up the content strategy. Say \"set up my content strategy\"."
- When the run stops part-way: the department's Next step is "Continue the content setup: step N, <step>. Say \"continue content setup\"."
- Update the department's Current state with today's date and one line, and `updated:`. Mention it in one short line.
- Receipt and milestone (below).

## setup.md format

```
# Content machine setup: <business>

Status: in progress | complete · Started YYYY-MM-DD · Updated YYYY-MM-DD

| # | Step | Status | Date | How we know / notes |
|---|---|---|---|---|
| 1 | Content department | done | YYYY-MM-DD | brief.md exists |
...

## Decided for her
- YYYY-MM-DD — <small detail decided, and why>

## Waiting on
- <step>: <what, and who>
```

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-install | <steps done this run, or status-only> | <N>/20 done · files: <setup.md, brand-style.md, templates.md, ghl.md, .env created, script copied> · waiting: <steps, or none>`

## Milestone

Runs that changed something: hand /context one line for `context/content.md`:
`Content setup <N>/20: done this run <steps>. Waiting on <steps, and on whom>.`

## What this skill never does

- Writes `brand-style.md`, `templates.md` or `ghl.md` without an explicit yes.
- Reads, prints, copies or asks for the GoHighLevel key, or reads `.env`.
- Connects, disconnects or changes anything in Canva, GoHighLevel or Claude's settings — she does those; this skill only checks. The only Canva edits it makes are the step 9 rebrands of her own template copies, after her yes.
- Writes `strategy.md`, `plan.md`, `calendar.md`, `ideas.md`, `posts/`, `about-me/` (changes there only wait in `_system/pending.md`), the shipped library, playbook or guides, or anything in `context/` (milestones go through /context).
- Adds template rows to `templates.md` beyond the base templates set up here.
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Edits a TEMPLATE design in Canva, or the original MCM shared. The step 9 rebrand works on her fresh copy before it's titled TEMPLATE.
- Runs a hand-off without a yes.
- Creates reminders or tasks on a timer. Dates live in files the skills already read (e.g. token expiry in `ghl.md`, which content-post checks every run).
- Deletes files. Anything replaced goes to `_review/`.

## When to refuse

- A request to paste the GoHighLevel key into chat — "Paste it straight into the settings file in your content folder instead; I never see the key." (the key never enters chat)
- A request to skip the yes on a file — "I'll show it first; one yes and it's saved."
- A request to post before setup is done — "Setup comes first; we're at step N." (posts need the strategy and the templates)
- A request to set up content for a second business in this folder — "This folder holds one business's content. A second business gets its own Claude folder."

## Failure modes

- **A check can't run** (Canva or GoHighLevel not connected, computer offline) — mark the step "waiting", say what she needs to do, move to the next step that doesn't depend on it.
- **A check disagrees with setup.md** (a step marked done now fails, e.g. a connection expired) — reopen the step, say why.
- **Business file or voice missing** — offer /install; the Canva and GoHighLevel steps can still run meanwhile.
- **She declines the brand kit** — use the colors and logo files she already has; note it under "Decided for her".
- **Shared template doesn't show up for her** — check that MCM shared it to the email on her Canva account; ask MCM to share it again. Never rebuild the template from scratch.
- **The copy lost fonts or the accent color** — list it as a hand fix; Archivo Black and Lato (the base templates' fonts) are free in every Canva.
- **An element can't be recolored from here** — leave it, list it as a hand fix at the gate.
- **The script source is missing** — stop step 18 and say so; never rewrite the script.
- **Department brief missing after she declined new-department** — keep `setup.md` in `departments/content/` anyway and say the department still needs a brief.
- Prefer doing less: when unsure, stop at the current step and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, start no hand-off. Report what was already done this run (`setup.md` lines, files written, script copied) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): run the read-only checks and write only one receipt line with the status. Never write `setup.md`, the files, `.env`, pending items or the brief, and never start a hand-off.

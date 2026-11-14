---
name: content-install
description: "Walks her through setting up the content machine in 20 steps — her Content department, Canva, her brand and templates, MCM, the upload path and the strategy — with a recommendation at each step, doing the busywork itself, picking up where she left off. When she says \"/content-install\", \"set up the content machine\", \"set up my content\", \"continue content setup\", \"where are we in the content setup\", or when the Content department's next step says the setup is open."
---

# content-install — ready for the first post

Gets her content machine ready: the Content department, Canva, her brand on the design templates, MCM, the upload path and the strategy. It walks the steps in order, opens every step with the answer we'd pick and why, decides small details for her and notes them, and picks up where it left off.

It does one thing: **get her content machine ready for its first post.** It never writes the strategy, plans posts or makes posts — it hands off to the skills that do.

Speak to her in plain, warm US English, in her voice rules from `about-me/writing.md`: plain words, nothing technical. Say "Canva connected to Claude", "your MCM connected to Claude", "the settings file in your content folder"; never "connector", "MCP", "API", "token", file names, "skill" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. This skill ships two things in its own folder: `guides.md` (Guide 0 and B for Canva, C, D and E for MCM) and `scripts/` (the upload and transcription scripts copied into her content folder).

1. `departments/content/setup.md` — progress and the resume point. If missing, this is a new setup.
2. `departments/content/brief.md` — whether the department exists; its Next step and Current state.
3. `departments/content/brand-style.md`, `templates.md`, `ghl.md` — if they exist, to know what's already filled.
4. `about-me/brand.md` — her colors, fonts and logo files, if her brand kit exists.
5. `about-me/business-brain.md` and `about-me/writing.md` — only to check they exist and are filled in. Never edited here.
6. `guides.md` — when a step points to one of its guides.

Never read or print `departments/content/.env`. Step 19 checks only whether a key is set.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Every step opens with a recommendation: the answer we'd pick and why. She confirms or changes it. Small details get decided and noted, not asked."

> "Claude does the busywork. She only does what needs her hands (signing in, approving, pasting a key), and every one of those comes as numbered steps, one action each, with a direct link wherever one exists (**Click here to open <the page> →**). If Claude can check something, it checks instead of asking her to report."

> "brand-style.md, templates.md and ghl.md are Claude's reference notes: written without asking and mentioned in one line. What she decides in them (which templates, her newsletter details) is confirmed with her first."

> "Checks are read-only. A check never creates, edits, sends or connects anything."

> "Template rebrands are saved only after an explicit yes to the previews. Only her own fresh copies are edited, never a shared original, and never a template of her own beyond the placeholders she approved."

> "The MCM key goes into .env by her own hand. Never ask for it in chat, never read it, never print it."

> "The Content department brief is written only after her yes to it. Hand-offs (install, brand-kit-designer, content-strategy) run only on a yes."

> "setup.md, the receipt and the department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

## The steps

| # | Stage | Step | Done when | How |
|---|---|---|---|---|
| 1 | Home | Content department exists | `departments/content/brief.md` exists | If missing → create it from **The Content department** below: one question (its area), the brief shown, written on yes. No interview: the content machine already knows what this department is |
| 2 | Home | Setup tracker | `setup.md` exists | Create it (format below) |
| 3 | Business | Business file filled in | `about-me/business-brain.md` exists with offer, audience and pains | Missing → offer to redo the install's business step (step 3; a completed install still runs "redo step 3"), and run it on her yes. Thin → ask what's missing (at most 3 questions) and add the lines to `_system/pending.md` as items for `about-me/business-brain.md`; done when they're written |
| 4 | Business | Voice captured | `about-me/writing.md` exists with real samples | Missing → offer to redo the install's writing step (step 4; a completed install still runs "redo step 4"), and run it on her yes. No samples → ask her for 2-3 things she wrote and add them to `_system/pending.md` as an item for `about-me/writing.md` |
| 5 | Canva | Canva account | she confirms | Guide 0. Recommend Free to start; skip Pro trials. Her plan never matters to the setup |
| 6 | Canva | Canva connected to Claude | `list-brand-kits` answers | She connects Canva in Claude's **Customize → Connectors** (**Click here to open Connectors →** `https://claude.ai/customize/connectors`); then check. If the check fails right after she connects, she starts a new conversation so the connection loads, and says "continue content setup" |
| 7 | Brand | Her logo and colors | `about-me/brand.md` exists, or she chose "later" | Ask first: "**Do you already have a logo and brand colors?**" **Yes** → "Put your logo files, and anything that shows your colors (a style guide, a past design), in **04. Brand** in your Drive, or attach them here. Your website works too: just send the link." Then /brand-kit-designer in its **from her own brand** mode, run on her yes. **No** → offer to make them now (/brand-kit-designer, about 15 minutes) or later. Later → the templates keep MCM's colors until she has hers; note it under "Decided for her". No Canva Brand Kit step: her colors go into the templates themselves (step 9) |
| 8 | Brand | Logo on her templates | her logo is placed on every template that has a logo spot | Claude places it, after steps 9, 17-19 are done: her light and color logo files (from `about-me/brand.md`) go into her Canva (from her computer with `create-upload-url` once `www.canva.com` is an allowed site, or `media-to-ghl.sh` for a permanent link and `upload-asset-from-url`), then `update_fill` on each template's logo spot. Neither works → fallback: she drags her logo into one design Claude links her to (**Click here to open it →**), from her Canva Uploads; Claude reads its media ID from that design and places it everywhere. No logo yet (brand later) → step waits, nothing to do now |
| 9 | Templates | Her templates | every template she'll use is in her Canva, titled TEMPLATE, design ID known | Ask first: "**Do you already have post templates in Canva?** Bought ones, ones you made, or ones made for you." **Yes** → she sends the links (or the names, and Claude finds them): see "Her own templates" below. Then: "Want MCM's five templates too? **Yes, in my colors** / **Yes, as they are** / **No, mine are enough**". **No** → MCM's five, in her colors. MCM's five: "Carousel - Tips list (3 points)" (dark), "Carousel - Tips list (3 points) - Light", "Illustrated carousel - Leak", "Photo - full frame" (one page, one full-bleed image: generated images go through it to come out as a full-size file) and "Photo - headline" (one page: a full-bleed photo, a soft dark fade at the bottom and a headline on it). Rica shares them to her Canva email as "Can edit" (by hand: Canva can't share from here). Claude copies each one into her Canva itself (`copy-design`) and rebrands the copy (below); she does nothing but say yes. A shared design that doesn't show for her: ask Rica to share it to the email her Canva uses, and mark the step waiting. Then, optional: "**Any posts or accounts whose look you love?** Attach screenshots or send the links." (see "Design references" below). Last, once all her templates are in: "Want your brand fonts on your templates? About 2 minutes per template." Optional; Guide B with a link to each template |
| 10 | Templates | Brand style | `brand-style.md` written | Claude writes it from `about-me/brand.md` (or MCM's colors when her brand is "later"), the templates and her references, without asking; one line: "I wrote down how your colors and templates are used." |
| 11 | Templates | Template index | `templates.md` has every template set up here | Claude writes the rows and fill guides in content-template's shape: one row per template (template, Canva ID, format, post type, slides, use for) with its fill guide under it, hers and MCM's side by side; no approval, one line as in step 10 |
| 12 | MCM | Her MCM connected to Claude | the MCM connection lists her business (sub-account) | Guide C: she connects MCM from the plugin's **Connectors** tab, signs in, picks her business and approves the permissions, social posts read and write included; she starts a new conversation so the connection loads; then check. The plugin's connector doesn't show or fails → Guide C's fallback (custom connector). Record her location ID and her MCM app address (the `uiUrl` from `fetch-media-content`, its domain) in `ghl.md`: the links in steps 13 and 19 are built from them |
| 13 | MCM | Platforms and social accounts | `get-account` lists every platform she'll post on | Recommend her platforms first, from each `../content-strategy/platforms/` file's "When to recommend it" (Instagram; Facebook when she has a Page; LinkedIn, her personal profile, when she sells to professionals; the newsletter when she sells something people decide on over time and has a list; Substack only with the newsletter, when her expertise is what she sells or she already has one; the podcast when she likes to talk more than write and can keep a season going), and note them in `setup.md` (the strategy step starts from them). Podcast on: "**Do you already have a show?**" Yes → its name and link go into `departments/content/podcast.md` (content-podcast's show file); No → the show is made at her first episode, not now. Either way her Drive folder `Content audio` is created. Then: "**Do you want to make videos of yourself talking?** Yes / Not for now". Yes → reels on, noted in `setup.md`, her Drive folder `Content videos` created; then "The video tools (an ElevenLabs account) can be set up now or at your first reel. **Set it up now** / **At my first reel**" (now → content-video's ElevenLabs setup runs here). With the podcast on too, ask it once for both ("…at your first reel or episode"); the podcast alone asks the same about its first episode. Not for now → reels off; she turns them on any time ("I want to make reels"), which asks the same. Then she connects her accounts in MCM (Guide D, with the direct link to her Social Planner), and Claude checks them itself with `get-account`; she never has to report. If an account doesn't list, say which and send her back to the link. Substack on: no connection; she signs in to Substack once in the browser inside the Claude app, and Claude opens her dashboard to check |
| 14 | MCM | MCM details | `ghl.md` written | Claude writes location, user, social account and profile IDs and token expiry dates from the checks, without asking. Newsletter on: Claude fills her details from MCM and shows them for one confirmation: from name (her name on her MCM user), from email (her business email in MCM), reply-to (the same address), and the list (her tags with contact counts: `get-location-tags`, then `search-contacts-advanced` filtered by the likeliest tag, e.g. "newsletter, 214 contacts"). "**These are right** / **Change something**", then "Not sure about any of these? We can talk it through." Then the sending domain, read-only, in the browser (MCM's email settings show it verified). Setting up the domain, its records or the list is part of her MCM build, never this step. Not known yet, or a check fails: say what's missing and mark the newsletter waiting; the rest of the step goes on. Substack on: her publication address |
| 15 | MCM | Reconnect warning | `ghl.md` has every account's token expiry date | Nothing to schedule: content-post reads `ghl.md` every run and warns 14 days before an expiry. Tell her that's how she'll hear about it |
| 16 | Upload | Computer linked | a command on her computer answers | If not, tell her to open this chat in the Claude desktop app on the computer that holds her Claude folder |
| 17 | Upload | Allowed sites | the three sites reachable from her computer | Test `export-download.canva.com`, `www.canva.com` (her logo goes straight into Canva, step 8) and `services.leadconnectorhq.com`. Any answer from the site counts as reachable, even a 403 (Canva answers 403 at its root). Blocked looks different: the computer's network filter refuses it (`X-Proxy-Error: blocked-by-allowlist`). If blocked, she adds the blocked ones in Claude's **Settings → Capabilities** (**Click here to open Capabilities →** `https://claude.ai/settings/capabilities`), one at a time, each written out for her to copy |
| 18 | Upload | Upload scripts | `departments/content/scripts/canva-to-ghl.sh` and `media-to-ghl.sh` exist | Copy both from this skill's `scripts/`, unchanged |
| 19 | Upload | MCM key | `.env` has `GHL_PIT` set | Create `departments/content/.env` with an empty `GHL_PIT=` line if missing; she makes a Private Integration key (View Medias and Edit Medias) in MCM and pastes it into the file (Guide E, with the direct link to her Private Integrations page and a clickable link to the file, its full path on her computer, which opens it; the Finder way, with hidden files shown, only if the link doesn't open, and Claude never says it will open the file itself); the check prints only "set" or "not set" |
| 20 | Strategy | Strategy | `departments/content/strategy.md` exists | Offer /content-strategy (it then offers to plan the first 4 weeks) |

Order: stages in order. Within a stage, a step that waits on her doesn't block the next step that doesn't need it — say which one is waiting.

## Workflow

### Step 1 — Where are we
- If `setup.md` exists: read it, run the read-only checks for any step marked open, and update the ones the checks now prove done.
- If it doesn't: check every step against "Done when", so steps already done are recorded as done, with how we know.
- Show the status in one table (step, status, what's waiting) and name the next step with its recommendation. For "where are we", stop here.

### Step 2 — Work the next step
- Open with the recommendation: "We'd do <X>, because <why>." A choice comes as numbered options under a short lead-in, and always ends with "Or tell me what you're thinking." (/system's reply rules).
- Her steps (5, 6, 12, 13 connect, 17, 19 paste, 9 fonts): give the guide's steps as numbered steps, one action each, every link as **Click here to open <the page> →** (`guides.md`), then wait for "done" and run the check where there is one.
- Hand-off steps (3, 4, 7 brand kit, 20): offer the skill; run it only on yes. When it finishes, re-check and continue.
- A `setup.md` from an older version, with steps in another order: re-check every step against today's "Done when" by name, not by number, and rewrite the table in today's order.
- **Her brand roles** (steps 8-10), from `about-me/brand.md`: dark = her darkest brand color, light = her lightest (or the Neutral), accent = the Accent. Logo for dark slides = the white/light horizontal logo file in `deliverables/brand/` (e.g. `horizontal-white.png`); for light slides = the color/transparent one (`horizontal-transparent.png`). If the file names differ, list the files and ask her once which is which. Brand "later": MCM's colors stay, and the templates are rebranded once her brand exists.
- **Step 9 rebrand**, on each of her copies of MCM's five (skipped for "Yes, as they are"; through her Canva connection; "Photo - full frame" has nothing to rebrand, only its title; "Photo - headline": the fade to her dark and the headline to her light, nothing else): change the base templates' colors (#0E2D36 dark, #FAF8F4 light, #E7963D accent) to her dark, light and accent from step 7 on shapes, text and page backgrounds; the logo spots wait for step 8; keep the layout and every text region as it is, except fixed words no post fills in (the swipe cue, the end-slide call to action): rewrite those to fit her business, in her voice, and show them in the previews. Her design references (below), if she gave any, guide the small choices (spacing, which accent goes where), never the layout. Show the previews and list hand fixes (elements Canva won't let me recolor from here, such as image-filled rules), with Guide B's clicks and a link to each design.

> "Do these look right? Say **yes** and I'll save them, or tell me what to change."

  On yes, commit and retitle each "TEMPLATE - <format> - <post type>"; their design IDs go to step 11.
- **Her own templates (step 9):** read each one she sends; if its text sits in editable text boxes, it can serve as a template. Say which ones need placeholders added and add them only on her yes. A flat image can't serve: offer to build one like it (/content-template). Each one that serves gets its row and fill guide in `templates.md`, next to MCM's, and the plan picks from both. Her own designs are never recolored or restyled.
- **Design references (step 9):** screenshots or links she shares go to `04. Brand/References` in her Drive (her folder's `departments/content/references/` when her Drive isn't organized), and a few lines in `brand-style.md` § Looks she likes (e.g. "lots of white space, one big word per slide, hand-drawn arrows"). Read for feel only (layout, density, tone), never copied. Used now in the rebrand, later by content-template and for her photo style.
- File steps (10, 11, 14): written from what's known, without asking; one line saying what was written. The newsletter details in step 14 are the exception: shown for her confirmation first.
- After each step, update `setup.md` (status, date, how we know, decisions noted) and hand /system "refresh the Setup block", so Rica sees the progress the same day. No approval needed.

**The Content department (step 1):** the brief in /new-department's brief format, filled from the content machine, never from an interview. Ask only its area: "Is this content for **<her main business>**, or something else?" (her main business first; her answer wins). Fill the dates, show the full brief, and on yes write it, add its index line under its area header in `departments/index.md`, and hand /context the creation of `context/content.md` (`tier: department`) with "Content department created during the content setup." Her yes covers all three.

- Name **Content**; slug `content`; `area:` her answer.
- Intro: "Her posts, from idea to scheduled, and what they teach her about her audience."
- Purpose: "Show up consistently, in her own voice, so the right people get to know and trust her."
- Standards: "Nothing is posted without her yes." · "Where and how often she posts: her content strategy (`strategy.md`)."
- Routines: "The next post, when the plan says · as planned" · "A review of what worked, before each new 4-week plan · monthly".
- Current state: "Content setup started; nothing posted yet."
- Next step: "Continue the content setup: step 2. Say \"continue content setup\"."
- What I use here: "next post" or "let's make the next post" (makes the next post from the plan · `posts/`), "make this a post" (turns an idea into a post, in the plan or outside it), "plan content" (the next 4 weeks · `plan.md`), "set up my content strategy" (what to post and why · `strategy.md`), "review the content" (what worked · `performance-log.md`), "set up my content" (this setup · `setup.md`).
- Material that already exists: none yet (her photos folder joins when she starts one).
- Decisions: "Department created during the content setup."

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
| Heading | | set on the templates by her, optional (step 9's fonts offer) |
| Body | | |

## Logo
- Light version (for dark slides): <file> · Canva media ID: <id, once placed>
- Color version (for light slides): <file> · Canva media ID: <id, once placed>

## Looks she likes
- <a few lines from her design references, or "none given">
```

**`ghl.md` (step 14):**

```markdown
# MCM: <business>

Not secret. The key lives in .env, never here.

- Location ID:
- MCM app address (for direct links): https://<domain>
- User ID (posts are scheduled as):

| Platform | Account ID | Profile ID | Token expires |
|---|---|---|---|
| Instagram | | | YYYY-MM-DD |
| Facebook | | | YYYY-MM-DD |
| LinkedIn (only when on) | | | YYYY-MM-DD |

## Newsletter (only when on)
- From name:
- From email:
- Reply-to:
- List (tag or segment):
- Checked: YYYY-MM-DD (domain verified, list has N contacts)

## Substack (only when on)
- Publication address:
- Tags in use:
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

- Saves her newsletter details without her confirmation.
- Reads, prints, copies or asks for the MCM key, or reads `.env`.
- Connects, disconnects or changes anything in MCM or Claude's settings — she does those; this skill only checks. The only Canva changes it makes: copying the shared templates into her Canva and rebranding the copies (step 9, on her yes), placeholders on her own templates (on her yes), and placing her logo (step 8).
- Writes `strategy.md`, `plan.md`, `calendar.md`, `ideas.md`, `posts/`, `about-me/` (changes there only wait in `_system/pending.md`), the shipped library, playbook or guides, or anything in `context/` (milestones go through /context).
- Adds template rows to `templates.md` beyond the templates set up here (MCM's and her own).
- Touches anything in the department brief beyond Next step, Current state and `updated:`, once step 1 has created it.
- Edits a TEMPLATE design in Canva, or the original MCM shared. The step 9 rebrand works on her fresh copy before it's titled TEMPLATE.
- Runs a hand-off without a yes, or interviews her for the Content department brief.
- Creates reminders or tasks on a timer. Dates live in files the skills already read (e.g. token expiry in `ghl.md`, which content-post checks every run).
- Deletes files. Anything replaced goes to `_review/`.

## When to refuse

- A request to paste the MCM key into chat — "Paste it straight into the settings file in your content folder instead; I never see the key." (the key never enters chat)
- A request to skip the yes on a file — "I'll show it first; one yes and it's saved."
- A request to post before setup is done — "Setup comes first; we're at step N." (posts need the strategy and the templates)
- A request to set up content for a second business in this folder — "This folder holds one business's content. A second business gets its own Claude folder."

## Failure modes

- **A check can't run** (Canva or MCM not connected, computer offline) — mark the step "waiting", say what she needs to do, move to the next step that doesn't depend on it.
- **A check disagrees with setup.md** (a step marked done now fails, e.g. a connection expired) — reopen the step, say why.
- **Business file or voice missing** — offer to redo the install's business step (step 3) or writing step (step 4), and run it on her yes; the Canva and MCM steps can still run meanwhile.
- **She chooses "later" for her brand** — MCM's colors stay on the templates and step 8 waits; note it under "Decided for her". When her brand exists, the rebrand and the logo run then.
- **Shared template doesn't show up for her, or `copy-design` refuses it** — check that MCM shared it to the email on her Canva account; ask Rica to share it again. Never rebuild the template from scratch.
- **The plugin's MCM connector is missing or broken** — Guide C's fallback: she adds the custom connector by hand.
- **Her logo can't reach Canva** (both routes blocked) — step 8's fallback: one design link, she drags the logo in.
- **A direct link doesn't land on the right page** (MCM moved it) — give the click path instead, and note it under "Decided for her".
- **The copy lost the accent color** — list it as a hand fix. Fonts: the base templates use Archivo Black and Lato, free in every Canva; her own fonts are step 9's optional offer.
- **An element can't be recolored from here** — leave it, list it as a hand fix at the gate.
- **The script source is missing** — stop step 18 and say so; never rewrite the script.
- **Department brief missing after she declined it** — keep `setup.md` in `departments/content/` anyway and say the department still needs a brief.
- Prefer doing less: when unsure, stop at the current step and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, start no hand-off. Report what was already done this run (`setup.md` lines, files written, script copied) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): run the read-only checks and write only one receipt line with the status. Never write `setup.md`, the files, `.env`, pending items or the brief, and never start a hand-off.

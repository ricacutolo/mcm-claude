---
name: content-static
description: "Makes one image post — a carousel, illustrated carousel or text post — from idea to scheduled: the idea, the copy, the design in Canva and the schedule in GoHighLevel, with her yes at each step. Usually started from the next post in the plan; also when she says \"/content-static\", \"make this carousel\", \"make the carousel for post 5\", \"design the next carousel\", \"let's make a text post\"."
---

# content-static — one image post, idea to scheduled

She leads with her voice and her ideas; this skill drafts, designs and schedules around them. It never posts on its own.

It does one thing: **take one image post from idea to scheduled.** It is usually started by content-post with a slot from the plan. Started directly by name, it first runs content-post's Steps 1-2 (find the slot, the connection warning, the missed-slot rule) and then continues here. Reels belong to content-video.

Speak to her in plain, warm US English. Say "the copy", "the design", "the calendar", "the department brief"; never file names, "skill", "API" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. The shared reference files ship with the plugin next to this skill's folder: `../content-strategy/playbook.md` (the copy playbook) and `../content-strategy/library.md` (the strategy library).

1. The slot content-post passed: post number, date and time (and the original slot if it was missed), topic, post type, format, template, idea.
2. `departments/content/brief.md` — its Next step and Current state.
3. `departments/content/strategy.md` — who we post for, which layers are on, topics, post types, idea rules, cadence, CTA, wedge.
4. `departments/content/plan.md` — the slot's row and the next `planned` slot.
5. `departments/content/calendar.md` — what's scheduled and published.
6. `departments/content/ideas.md` — the idea backlog.
7. `departments/content/templates.md` and `brand-style.md` — which template, which color and font roles. `about-me/brand.md` when it exists, for her logo files.
8. `departments/content/ghl.md` — location, user and account IDs (not secret).
9. The post's own `departments/content/posts/<folder>/post.md`, if it exists — to resume.
10. `about-me/about-me.md` — only her time zone.
11. Only when recommending ideas or drafting copy (Steps 2-3):
    - `about-me/business.md` — the offer, who it's for, the wedge, current positioning. It evolves; always read the current one, never a remembered copy.
    - `../content-strategy/playbook.md` — rules, awareness levels, hooks, frameworks, structure per post type, caption formula, CTA by layer, the 4-point check.
    - `departments/content/swipe.md` — lines that worked for her, if it exists.
    - `about-me/writing.md` — her voice.

Never read or print `departments/content/.env`. The script reads it; this skill never does.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is scheduled or published without an explicit yes at the schedule gate. A yes to the copy or the design is not a yes to schedule."

> "Three gates, in order: copy, design, schedule. Each waits for an explicit yes (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a yes."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "Her point of view leads. Claude may recommend an idea and angles; it never invents a stance she hasn't taken and never presents a recommendation as decided."

> "Never edit a TEMPLATE design. Always work on a copy."

> "A missed slot moves; it is never skipped silently or doubled up. Never two posts on the same day."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 1 — The post and where it stands
- Use the slot content-post passed. If the slot's format is a reel or video: "Post N is a reel; that's made in the video steps. Want me to start those?" and hand back to content-post on yes.
- If `posts/<folder>/post.md` exists, read its Step/Status table and resume at the first step not done.
- New post: create `departments/content/posts/post-NN-<slug>/post.md` in the shape below, with the slot's topic, post type, format and template — the slug once the idea is picked.
- If the slot's template is "to build": stop. "Post N needs the <post type> template, which isn't built yet. Want to build it first, or swap this slot's post type?" Building it is content-template, run on yes. Never improvise a template.

**`post.md` shape:**

```markdown
# Post N: <short title, once the idea is picked>

Slot: <day date time> · <topic> × <post type> · <format> · template: <name>

| Step | Status |
|---|---|
| Idea | |
| Copy | |
| Design | |
| Schedule | |
| Results | |

## Her direction
- <what she said she wants this post to say or avoid>

## Slides ([brackets] = accent words)
1. ...

## Caption

## Run notes
- <calls made without asking, her edits at each gate, size changes, hand fixes>

## Final slides (permanent links)
```

### Step 2 — Idea
- The slot gives the topic and post type. If the slot has an idea from `ideas.md`, offer it first. If it has a suggestion, offer it plus 2 other angles on the same topic × post type, and the option to bring her own.
- Ideas follow the idea rules in `strategy.md` and the rules in the playbook: what the reader gets, never technical, real things only. Read `business.md` for the offer, the audience and the wedge.
- She picks. If she changes the topic or post type, say the plan will show it changed and note it in `post.md`. Record topic, post type, idea and who chose it in `post.md`.

### Step 3 — Copy (gate 1)
- Read the playbook and her voice. Choose the awareness level for the post type, pick a hook pattern, use the structure for the post type and the caption formula, and the CTA for the layer that's on.
- For the 5-slide tips list: slide 1 hook (accent color on the words that sting) + "Swipe through →"; slides 2-4 one point each (number, short title, 2-4 lines, the turn in the accent color); slide 5 reframe line, promise in the accent color, the CTA.
- Run the playbook's 4-point check (hook, what they get, plain, CTA) and fix what fails before showing.
- Show slides and caption, accent words in [brackets], and one line naming the hook pattern used.
- **Gate:** "Does the copy work? Say **yes**, or tell me what to change." Apply edits exactly; re-show; wait for yes. Record the approved copy, caption and hook pattern in `post.md`.

### Step 4 — Design (gate 2)
- Use the slot's template from `templates.md`. Where a post type has a dark and a light version, alternate against the last published post.
- `copy-design` the template; title the copy `Post N - <hook>`. Record the new design ID in `post.md`.
- Open an editing transaction, read every page, and fill with `find_and_replace_text` on each placeholder region — it keeps each region's color and weight. To move where the accent color starts, empty a region and put the words in the next one; never recolor with `format_text` (it recolors the whole element). Font size changes with `format_text` are fine. `add_text` comes in unstyled — don't use it. Fonts can't be set from here.
- Check every slide's thumbnail: overflow, a heading wrapping into the big number, a word alone on the last line, text off the canvas, a text box that jumped after a resize. Fix by shrinking the font, resizing or repositioning the box. Keep body sizes the same across the point slides.
- Send the previews. List anything only a hand edit can do (the accent color on part of a one-color text box, fonts, logo) — `../content-install/guides.md` Guide B has the clicks.
- **Gate:** "Does the design work? Say **yes** and I'll save it, or tell me what to change." On yes, commit the transaction **immediately** — open transactions expire.
- If she then edits by hand in Canva, that is fine: Step 5 re-reads the design before export.

### Step 5 — Schedule (gate 3)
- The date and time content-post passed (the slot, or the new time for a missed slot), at least 1 hour out. Platforms and accounts from `strategy.md` + `ghl.md`. Times are in her time zone (from `about-me/about-me.md`, else ask once).
- If the time has slipped to under 1 hour away while we worked, it's now a missed slot: recompute with content-post's missed-slot rule (`../content-post/SKILL.md`, Step 2) and say the new time in one line. Never schedule two posts on the same day.
- If a connection in `ghl.md` has expired: stop here. "Your <platform> connection has expired. Reconnect it in GoHighLevel's Social Planner and tell me when it's done."
- **Gate:** show date and time (her time zone), platforms, caption, slide count. "Ready to schedule? Say **yes** and I'll schedule it." Wait for an explicit yes.
- On yes:
  1. Re-read the design so hand edits are in; export PNG 1080x1440, all pages.
  2. Run on her computer, from `departments/content/`: `bash scripts/canva-to-ghl.sh posts/<folder> <export url 1> ... <export url N>`. It saves local copies to `posts/<folder>/slides/` and prints one permanent GoHighLevel URL per slide. Canva export links expire within hours — never schedule with them. If `scripts/canva-to-ghl.sh` is missing, copy it from `../content-install/scripts/` first.
  3. GoHighLevel `create-post`: `accountIds` from `ghl.md`, `userId` from `ghl.md`, `type: post`, `status: scheduled`, `scheduleDate` in UTC, `instagramPostDetails: {type: post}`, `facebookPostDetails: {type: post}` when Facebook is in, `summary` = approved caption, `media` = the permanent URLs as `image/png`, in slide order. Idempotency key: `<location ID>-post-NN-<slug>-schedule`.
  4. Verify with `get-posts` (body: `type: all` or `scheduled`, `accounts` as a comma-separated string, `skip`/`limit` as strings, dates bracketing the slot). The parent record may show `platform: google` until publish, and the list may show only the first image — ignore both; per-platform child posts are created at publish time.

### Step 6 — Close
- `post.md`: Design and Schedule rows, design ID, permanent URLs, GoHighLevel post ID, slot.
- `calendar.md`: the post's row (date, `<topic> × <post type>`, format, idea, `Scheduled <time>`); add the row if missing (create the file with `# Content calendar` and the columns `# · date · post · format · idea · status` if needed). For a missed slot, the actual date and time, plus "(moved from <slot>, missed)".
- `plan.md`: set this slot's Status to `scheduled` — the Status cell only; the plan's other cells belong to content-plan. For a missed slot: `scheduled (moved to <day time>)`.
- `ideas.md`: mark the idea `used: post N` if it came from there; add any new ideas she mentioned during the run as `unused`.
- Department brief: set Next step to the next `planned` slot ("Post N+1, <day date>, <time>: <topic> × <post type>. Say \"next post\"."). If fewer than 2 weeks of planned slots remain, the Next step is "Plan the next 4 weeks. Say \"plan content\"." instead. Update Current state with its date and one line, and `updated:`. No approval needed; mention it in one short line.
- Receipt and milestone (below).
- Hand back to content-post's Step 4 (stay one post ahead, and how she'll hear it went live) — also when she started this skill directly.

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-static | idea / copy-approved / design-approved / scheduled / stopped-at-<gate> | post N · <topic> × <post type> · design <ID> · GHL post <ID> · missed: yes/no`

## Milestone

Runs that reached a new stage: hand /context one line for `context/content.md`:
`Post N <copy approved / design approved / scheduled for <slot>>: <topic> × <post type>, <format>. Still open: <hand fixes, or none>.`

## What this skill never does

- Schedules or publishes without an explicit yes at the schedule gate. Never sets `status: published` directly.
- Reads, prints, copies or asks for `.env` or the GoHighLevel key.
- Edits a TEMPLATE design, `strategy.md`, `brand-style.md`, `templates.md`, `ghl.md`, the shipped library or playbook, `about-me/`, or anything in `context/` (milestones go through /context).
- Changes `plan.md` beyond the Status cell of the slot it scheduled.
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Improvises a template for a post type that has none.
- Makes a reel or any video post. Those go to content-video.
- Invents her point of view, numbers or results, or presents a recommended idea as decided.
- Schedules with Canva export links (they expire).
- Deletes posts, designs, files or ideas. A dropped idea is marked `dropped`, not removed.
- Runs more than one post per run.
- Schedules two posts on the same day, or lets a missed slot pass without moving it.

## When to refuse

- No `strategy.md` — "There's no content strategy yet. Want to set it up first?" (the post comes from a strategy; it doesn't make one)
- The slot's template is "to build" or missing — "Post N needs the <post type> template. Want to build it first, or swap the post type?" (never edit or improvise a template)
- Canva or GoHighLevel not connected — "Canva isn't connected right now, so I can't make the design." / "GoHighLevel isn't connected right now, so I can't schedule it." Stop at the last step that can run.
- A request to post right now, skipping the gates — "Every post goes through copy, design and schedule approval."
- A request to schedule into a slot that's passed or under 1 hour away — "That slot has passed; I'd post it <new time> instead." (GoHighLevel needs lead time to stage the post)

## Failure modes

- **Started directly with no slot** — run content-post's Steps 1-2 first; if there's still no slot, say so and offer to plan content.
- **Business file or playbook missing** — draft from `strategy.md` and her voice only; say which file was missing.
- **Canva transaction expired before commit** — open a new transaction, re-apply only the approved edits, re-show the previews, commit on yes. Never claim it saved.
- **Canva 409 / `polled_too_early`** — wait and retry once; then report and stop.
- **Export download blocked (403)** — stop. "Your computer can't reach export-download.canva.com yet. It needs to be added to the allowed sites in Claude's settings." Nothing is scheduled.
- **Upload to GoHighLevel fails (401/403)** — stop. "The GoHighLevel key in your content folder's settings file is missing or doesn't allow uploads." Never ask for the key in chat.
- **`create-post` 4xx** — report the message once; fix the one named field if it is clear (e.g. empty `userId` → `ghl.md`); otherwise stop. Never retry blindly — a duplicate post is worse than a late one.
- **Text overflow that can't be fixed from here** — leave it, list it as a hand fix at the design gate.
- **Connection token expired** (`ghl.md` expiry date passed, or GoHighLevel says so) — stop at schedule: "Reconnect <platform> in GoHighLevel's Social Planner."
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes, commit no open Canva transaction, schedule nothing. Report what was already done (post folder, design ID, uploads, GoHighLevel post ID if any) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her at three gates, so it does not run unattended. With nobody watching (scheduled or non-interactive): read the files, write one receipt line naming the slot and the recommended idea (`draft, not approved`), and execute nothing else — no design copy, no upload, no post.

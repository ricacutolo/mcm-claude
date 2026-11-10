---
name: content-newsletter
description: "Writes one email newsletter issue with her, from her own material or a suggestion, to scheduled in MCM: the idea, the draft with subject lines and preview text, and the schedule to her list, with her yes at each step. Usually started from a newsletter slot in the plan; also when she says \"/content-newsletter\", \"write the newsletter\", \"next newsletter\", \"I have something for the newsletter\", \"send an email to my list\"."
---

# content-newsletter — one newsletter issue, her words to scheduled

She leads with her voice and her ideas; this skill shapes them into one email and schedules it. It never sends on its own.

It does one thing: **take one newsletter issue from her material (or a suggestion) to scheduled.** It is usually started by content-post with a newsletter slot from the plan. Started directly by name, it first runs content-post's Steps 1-2 (find the slot, the missed-slot rule) and then continues here. Social posts belong to content-static and content-video.

Speak to her in plain, warm US English. Say "the newsletter", "the email", "your list", "the calendar"; never file names, "skill", "API", "campaign ID" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`.

1. The slot content-post passed: issue number, date and time (and the original slot if it was missed), topic, newsletter format, idea.
2. `departments/content/brief.md` — its Next step and Current state.
3. `departments/content/strategy.md` — who we write for, which layers are on, topics, the newsletter line in Cadence (on, how often, day and time, which list), the CTA, the wedge, which issues are offer issues.
4. `../content-strategy/platforms/newsletter.md` — the newsletter's formats, writing rules, scheduling and results. Only if the newsletter is on in `strategy.md`. Substack on too: `../content-strategy/platforms/substack.md` (the issue also goes out there as an article).
5. `departments/content/plan.md`, `calendar.md` and `ideas.md` — the slot, what's scheduled, the idea backlog.
6. `departments/content/ghl.md` — location and user IDs, and its Newsletter section: from name, from email, reply-to, the list (tag or segment).
7. The issue's own `departments/content/newsletters/issue-NN-<slug>.md`, if it exists — to resume.
8. `about-me/about-me.md` — only her time zone.
9. Only when suggesting or drafting (Steps 2-3):
   - the business file of the area in play (`about-me/business.md`, or `business-<area>.md` per /system's **Areas**). It evolves; always read the current one.
   - `../content-strategy/playbook.md` — rules, awareness levels, hooks, CTA by layer, the newsletter section, the 4-point check.
   - `../content-strategy/library.md` — the newsletter formats catalog.
   - `departments/content/swipe.md` — lines that worked for her, if it exists.
   - the posts published since the last issue (`calendar.md`, their `post.md`) — material for a suggestion.
   - `about-me/writing.md` — her voice.

Never read or print `departments/content/.env`.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is scheduled or sent without an explicit yes at the schedule gate. A yes to the draft is not a yes to send."

> "Two gates, in order: draft (with subject lines and preview text), schedule. Each waits for an explicit yes (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a yes."

> "Her material comes first. Step 2 always asks for what she has, and offers a suggestion in the same message. Claude never invents a story, a client, a result or a stance she hasn't given."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "One idea and one ask per email. Plain text, no images."

> "A client story or case study goes out only when she confirms the client agreed."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

## Workflow

### Step 1 — The issue and where it stands
- Use the slot content-post passed. If `newsletters/issue-NN-<slug>.md` exists, read its Step/Status table and resume at the first step not done.
- New issue: create `departments/content/newsletters/issue-NN-<slug>.md` in the shape below (the slug once the idea is set).
- Newsletter leads the theme (`strategy.md`): this issue sets the topic for the cycle's posts and is due by its write-by date in `plan.md` (2 days before it's sent). Say so in one line when it's close.
- The newsletter is off in `strategy.md`: "The newsletter isn't switched on in your content strategy yet. Want to switch it on first?" Stop.
- `ghl.md` has no Newsletter section, or no list: "Your newsletter isn't set up in MCM yet: <what's missing>. Want to finish that first?" Hand to content-install on yes. Stop.

**Issue shape:**

```markdown
# Issue N: <short title, once the idea is set>

Slot: <day date time> · <topic> · <format> · offer issue: yes/no

| Step | Status |
|---|---|
| Idea | |
| Draft | |
| Schedule | |
| Results | |

## Her material
<what she gave, as she gave it>

## Email
Subject options: 1. … 2. … 3. …
Preview text:
<body>

## Run notes
- <calls made without asking, her edits at each gate>
```

### Step 2 — Her material, with a suggestion
- One message, both at once: "Anything you want to write about this time — a few lines, a voice note, a client story, a question someone asked you? Or here's what I'd suggest: <one suggestion in one line, and why>."
- The suggestion comes from the slot's topic and format, the posts since the last issue (their best idea, gone deeper), `ideas.md`, and real questions she's mentioned. One suggestion, not a menu.
- Her material wins. Keep it in the issue file as she gave it. If it fits a different format than the slot's, say which and use it.
- She takes the suggestion: ask one question that gets her own angle on it ("What's one time you saw this happen?"). A newsletter without anything of hers in it is a blog post.

### Step 3 — Draft (gate 1)
- Write it in the slot's format (the library's newsletter formats), from her material, in her voice: the newsletter section of the playbook and `platforms/newsletter.md`. Plain text, 200-400 words, short paragraphs, one CTA for the layer that's on (or the offer, on an offer issue).
- Then the subject: 2-3 options, short and specific, written last, no emoji, plus one preview text line that adds to the subject.
- **Newsletter leads the theme:** under the email, propose the cycle's post angles, one per post slot in this cycle (from `plan.md`), each matched to its slot's post type and format, by the playbook's "From newsletter to posts" section: its points → a carousel, its story → a reel, its question → a text post, its moment → a photo post. One line each: the post, the angle, why it stands alone.
- Run the playbook's 4-point check (hook, what they get, plain, CTA) and fix what fails before showing.
- Show the subject options, the preview text and the email as it will read.
- **Gate:** "Does the newsletter work? Pick a subject and say **yes** (the post angles come with it), or tell me what to change."
- Record the approved email, subject and preview text in the issue file.

### Step 4 — Schedule (gate 2)
- Date and time from the slot, in her time zone; the list, from name, from email and reply-to from `ghl.md`.
- If the slot has passed or is under 1 hour away: content-post's missed-slot rule decides the new time.
- **Gate:** "Ready to schedule? <day date time> to <list>, from <name>. Say **yes** and I'll schedule it." Substack on: "…to <list>, from <name>, and on your Substack at the same time." Her yes covers both.
- On yes:
  1. MCM `create-email-campaign`: `name` "Newsletter <N>: <short title>", `editorType: text`, `editorContent` = the approved email, `timeZone` = hers, `userId` from `ghl.md`. Idempotency key: `<location ID>-newsletter-NN-<slug>-create`.
  2. MCM `schedule-campaign`: `scheduleType: scheduled`, `scheduleConfig.sendAt` in her time zone, `emailMeta` = subject, from name, from email, reply-to, preview text; `recipients` = the list from `ghl.md` (tag or segment). Idempotency key: `<location ID>-newsletter-NN-<slug>-schedule`.
  3. Verify it shows as scheduled; report the campaign status.
  4. Substack on: hand the approved email, the chosen subject, the preview text and the send time to content-substack (article). If it can't schedule it, the email still goes; say so in one line.

### Step 5 — Close
- Issue file: Draft and Schedule rows, campaign ID, send time.
- `calendar.md`: the issue's row (date, `Newsletter <N>: <topic>`, format `newsletter`, idea, `Scheduled <time>`).
- `plan.md`: set this slot's Status to `scheduled` — the Status cell only.
- `ideas.md`: mark the idea `used: newsletter N` if it came from there; add new ideas she mentioned as `unused`.
- Led cycle: each approved angle goes into `ideas.md` as `unused`, source `newsletter N`, tagged `for post M`.
- Department brief: set Next step to the next `planned` slot of any kind, as content-static does; update Current state with its date and one line, and `updated:`. Mention it in one short line.
- Receipt and milestone (below). Hand back to content-post's Step 4.

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-newsletter | idea / draft-approved / scheduled / stopped-at-<gate> | newsletter N · <topic> · <format> · campaign <ID> · missed: yes/no`

## Milestone

Runs that reached a new stage: hand /context one line for `context/content.md`:
`Newsletter N <draft approved / scheduled for <slot>>: <topic>, <format>. Still open: <next step, or none>.`

## What this skill never does

- Sends or schedules without an explicit yes at the schedule gate. Never uses `scheduleType: immediate`.
- Writes a newsletter without asking for her material first.
- Invents a story, a client, a quote, numbers or results.
- Adds images or a designed template; it's a plain-text email.
- Changes the list, the sending domain or anything else in MCM beyond the one campaign.
- Reads, prints, copies or asks for `.env` or the MCM key.
- Edits `strategy.md`, `ghl.md`, the shipped library, playbook or platform files, `about-me/`, or anything in `context/` (milestones go through /context).
- Changes `plan.md` beyond the Status cell of the slot it scheduled; touches the brief beyond Next step, Current state and `updated:`.
- Runs more than one issue per run.

## When to refuse

- No `strategy.md`, or the newsletter is off — "The newsletter isn't switched on in your content strategy yet. Want to switch it on first?"
- No sending address or list in MCM — "Your newsletter isn't set up in MCM yet. Want to finish that first?"
- A request to send right now, skipping the gates — "Every newsletter goes through draft and schedule approval."
- A client story without her confirming the client agreed — "Did <client> agree to be in the newsletter? I'll keep them anonymous until you say so."
- MCM not connected — "MCM isn't connected right now, so I can't schedule it." Stop after the draft.

## Failure modes

- **Started directly with no slot** — run content-post's Steps 1-2 first; with still no newsletter slot, write it for the next newsletter date in her cadence and say so.
- **She has nothing and doesn't want the suggestion** — keep the slot as it is; offer to move it to the next date. Never send a filler issue.
- **`create-email-campaign` or `schedule-campaign` 4xx** — report the message once; fix the one named field if it's clear (e.g. from email not verified → tell her the sending address needs verifying in MCM); otherwise stop. Never retry blindly: a duplicate send is worse than a late one.
- **The campaign was created but scheduling failed** — leave the draft campaign in MCM, record its ID in the issue file, and say so; the next run picks it up at Step 4.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes, schedule nothing. Report what was already done (issue file, campaign ID if any) and wait.

## Headless behavior

This skill needs her at two gates, so it does not run unattended. With nobody watching: read the files, write one receipt line naming the slot and the suggestion (`draft, not approved`), and execute nothing else.

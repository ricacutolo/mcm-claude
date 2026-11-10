---
name: content-post
description: "Finds her next post in the content plan and gets it made: carousels and other image posts go to the design steps, reels to the video steps, on her yes. Also saves post ideas and checks that scheduled posts went live. When she says \"/content-post\", \"next post\", \"what should I post next\", \"make the next post\", \"let's do post 5\", \"continue post 5\", \"time for a post\", \"did the post go live\", \"save this as a post idea\", \"post idea:\", or when the Content department's next step is a post."
---

# content-post — what's next, and who makes it

The front door of the content machine. It finds the next post in the plan (or the one she names), checks what could get in the way (a connection about to expire, a slot that already passed), and hands the post to the right maker: **content-static** for carousels and other image posts, **content-video** for reels. It makes nothing itself and never posts on its own.

Three entry points:
- **Next post** — Steps 1-4: find it, move it if the slot was missed, hand it over, then keep the queue one post ahead.
- **Idea capture** — "save this as a post idea": one row in her ideas list, then back to whatever was happening (Step C).
- **Publish check** — "did the post go live?": confirm in MCM and record the links (Step P). It also runs at the start of every next-post run.

Speak to her in plain, warm US English. Say "the plan", "the calendar", "your ideas list", "the department brief"; never file names, "skill", "MCP", "API" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Content department, `departments/content/`. The shared reference files ship with the plugin next to this skill's folder (`../content-strategy/library.md`, `../content-strategy/playbook.md`); the makers read them, this skill doesn't need them.

1. `departments/content/plan.md` — the next planned slot: post number, date and time, topic, post type, format, template, idea.
2. `departments/content/brief.md` — its Next step and Current state.
3. `departments/content/strategy.md` — cadence, slot time, platforms; topics (for idea capture).
4. `departments/content/calendar.md` — what's scheduled and published, and which days already hold a post.
5. `departments/content/ghl.md` — account IDs and each connection's token expiry date (not secret).
6. The post's own `departments/content/posts/<folder>/post.md`, if it exists — where it stands.
7. `about-me/about-me.md` — only her time zone.
8. Idea capture only: `departments/content/ideas.md`.
9. Publish check only: `departments/content/performance-log.md`.

Never read or print `departments/content/.env`. The scripts read it; this skill never does.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "This skill makes nothing. Copy, design, video and scheduling belong to content-static and content-video, and a post is handed to them only on her yes."

> "A missed slot moves; it is never skipped silently or doubled up. Never two posts on the same day."

> "One post per run. The next post starts as its own run, on her yes."

> "Nothing is scheduled or published from here. The publish check only reads MCM and records what went live."

> "The department's Next step and Current state are kept current without asking. Nothing else in the brief is touched; anything else goes to `_system/pending.md`."

> "An idea capture is approved by the request itself. It appends one row and nothing else."

## Workflow — next post

### Step 0 — Anything that should have gone live?
If `calendar.md` has a row marked `Scheduled` whose time has passed, run Step P for it first and give the result in one line. Then carry on.

### Step 1 — Find the post and where it stands
- Take the first `planned` slot in `plan.md`. If she names a post ("post 5"), use that one.
- No `plan.md`, or no planned slot: fall back to the department's Next step, then the calendar, and say so in one line. Offer to plan the next 4 weeks (content-plan); run it only on yes.
- If `posts/<folder>/post.md` exists, read its Step/Status table. Say in one line: "Post N, <topic> × <post type>, picking up at <step>." The maker resumes there.
- Read the token expiry dates in `ghl.md`. If any is 14 days away or less, say so first, in one line: "Your <platform> connection expires <date>. Reconnect it in MCM's Social Planner before then." Then carry on. Already expired: say so; the maker will stop at the schedule step until it's reconnected.

### Step 2 — Missed slot
Her time zone comes from `about-me/about-me.md`. If it isn't there, ask once ("Which time zone do you post in?"), use the answer, and add it to `_system/pending.md` as an item for `about-me/about-me.md`.

- A slot is **missed** when its time has passed or is less than 1 hour away.
- **The new time:** the same day if it can go out at least 1 hour from now and by 6 PM in her time zone, and nothing else is posted that day; otherwise the next cadence date with no post on it (check the calendar and the plan's scheduled slots).
- Say it in one line: "Post N's slot was <day time>; I'd post it <new time>." The maker confirms the new time at its schedule gate.
- Newsletter slots are their own channel: they never count toward one post a day, and a missed newsletter moves to the next free newsletter date.
- If that date already holds the next planned post, the later posts shift one slot: "That moves the rest of the plan back one slot. Want me to shift it?" On yes, run content-plan's "Refresh: shift after a missed slot". Never put two posts on the same day.

### Step 3 — Hand it to the maker
Route by the slot's format (formats as named in `../content-strategy/library.md`):

| Slot format | Maker |
|---|---|
| Carousel, illustrated carousel, text post — and any other still-image format with a template (screenshot post) | content-static |
| Photo post, photo carousel | content-static (her own photos, no template) |
| Talking-head reel, or any other reel or video format | content-video (beta; it says which video formats it can make) |
| Newsletter | content-newsletter (only when the newsletter is on in `strategy.md`) |
| Stories, or a format nothing makes yet | none — say so in one line and offer to swap the slot's format with content-plan's refresh |

Ask: "Post N is a <format>: <topic> × <post type>, <day time>. Want to start it now?" For a reel add one line: "Video is new in the system, so I'll first check I can make it on your setup."

On **yes**, run the maker and pass it the slot: post number, date and time (the new time if the slot was missed, with the original slot), topic, post type, format, template, idea, and the post folder if one exists. Anything other than a clear yes: stop here and keep the slot as it is.

### Step 4 — After the maker finishes
The maker hands back here when the post is scheduled (even when she started the maker directly by name).
- **Stay one post ahead:** if the next `planned` slot isn't scheduled yet: "Want to make post N+1 now, so there's always one in the queue?" Start it only on yes, as its own run (back to Step 1). One approved post waiting in MCM means a busy week doesn't leave a slot empty.
- **The publish check:** there are no reminders on a timer. Tell her once: "Once it's out, ask me \"did it go live?\" and I'll send you the links. I'll also check the next time we make a post."
- If the maker stopped at a gate instead, add nothing; it already said where it stopped.
- Receipt (below).

## Step P — Publish check

For each calendar row marked `Scheduled` whose time has passed, or the post she names:
1. MCM `get-posts` (body: `type: all`, `accounts` as a comma-separated string from `ghl.md`, `skip`/`limit` as strings, dates bracketing the slot). Find each platform's child post and its `previewLink`. The parent record may show `platform: google` until publish; ignore it.
2. **Found:** set the calendar row to `Published <date time>` with the links; record the links and the publish time in the post's `post.md` Results row; add the post's row to `performance-log.md` with the first numbers MCM has (likes, comments, shares), marked `early`. Create `performance-log.md` if missing:
   ```
   # Performance log: <business>

   ## Posts
   | # | Date | Topic × post type | Format | Hook | Platform | Likes | Comments | Shares | Reach | Pulled | Notes |
   |---|---|---|---|---|---|---|---|---|---|---|---|

   ## Account totals

   ## What we learned
   ```
3. **Not found yet:** within an hour of the slot, say it may still be going out and to ask again later. More than an hour past: "Post N hasn't shown up as published in MCM yet. It's worth a look in the Social Planner." Never mark it Published on a guess.
4. Tell her in one line per post: "Post N is live: <links>."
5. Department brief: Current state with today's date and one line. Hand /context a one-line milestone for `context/content.md`: `Post N published <date> (<topic> × <post type>)`.

## Step C — Idea capture

Triggered by "save this as a post idea", "post idea: …", "add this to my post ideas", from inside any other work.
- The explicit request is the approval for this one append.
- Append one row to `departments/content/ideas.md` (create it with `# Post ideas` and the columns `# · date · topic · idea · source · status` if missing): next #, today's date, topic (best match from `strategy.md`; `?` if none fits), the idea in her words, source (where it came up), `unused`.
- Confirm in one line: "Saved as post idea #N (<topic>)." If the topic was a guess, say so. Then return to whatever was happening — no other step runs.
- Receipt line. No milestone for a capture.

## Receipt

One line per run in `_system/log.md` (re-read the file before writing):

`YYYY-MM-DD | content-post | routed / declined / captured / publish-check / no-slot | post N · <format> → content-static or content-video · missed: yes/no · <published links or idea #N>`

## What this skill never does

- Drafts copy, designs, makes video, uploads or schedules. Those belong to the makers.
- Hands a post to a maker without her yes.
- Sets a post to published in MCM, or marks it Published in the calendar without finding it live.
- Reads, prints, copies or asks for `.env` or the MCM key.
- Edits `strategy.md`, `plan.md`, `templates.md`, `brand-style.md`, `ghl.md`, the shipped library or playbook, `about-me/`, or anything in `context/` (milestones go through /context).
- Touches anything in the department brief beyond Next step, Current state and `updated:`.
- Skips a missed slot, puts two posts on the same day, or shifts the plan without her yes.
- Deletes posts, files or ideas. A dropped idea is marked `dropped`, not removed.
- Runs more than one post per run.
- Creates reminders or tasks on a timer.

## When to refuse

- No `strategy.md` — "There's no content strategy yet, so there's nothing to post from. Want to set it up now?" (offers content-strategy on yes)
- A request to post right now and skip the steps — "Every post goes through copy, design and schedule approval. Want to start it now?"
- A request to put two posts on one day — "One post a day keeps the account steady. I'd put it on <next free date>."
- A request to schedule into a slot that's passed or under an hour away — "That slot has passed; I'd post it <new time> instead." (MCM needs lead time)

## Failure modes

- **No plan or no planned slot** — fall back to the department's Next step, then the calendar; say so; offer to plan the next 4 weeks.
- **Department brief missing** — skip the brief update; say so.
- **MCM not connected** — the publish check can't run: "MCM isn't connected right now, so I can't check what went live." The routing still works.
- **Calendar and plan disagree** (a planned slot already holds a scheduled post) — the calendar wins; say so and take the next free slot.
- **Time zone unknown and she doesn't answer** — stop before the missed-slot step; nothing is moved on a guess.
- Prefer doing less: when unsure, stop and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, start no maker. Report what was already done (publish check rows, idea row, receipt) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her yes to hand a post over, so it doesn't run unattended. With nobody watching (scheduled or non-interactive): read the files, write one receipt line naming the next slot and its maker, and do nothing else — no hand-off, no publish check writes, no idea rows.

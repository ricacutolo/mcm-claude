---
name: content-substack
description: "Schedules her Substack pieces through the browser: the newsletter issue as a Substack article, and short Notes cut from her current newsletter and posts, with her yes before anything is scheduled. Only when Substack is on in her content strategy. Usually started by content-newsletter (articles) or content-post (Note slots); also when she says \"/content-substack\", \"post on Substack\", \"next Substack note\", \"put the newsletter on Substack\"."
---

# content-substack — her Substack, through the browser

Substack has no connection Claude can use, so this skill works it the way she would: in the browser inside the Claude app, where she's signed in. It does two things, one per run:
- **Article:** the newsletter issue she just approved, scheduled on Substack for the same day and time as the email. Started by content-newsletter after the email is scheduled.
- **Note:** one short Note from a Note slot in the plan, written from what she's already making, approved, then scheduled. Started by content-post.

It schedules; it never publishes on the spot. Speak to her in plain, warm US English. Say "your Substack", "the article", "the Note"; never file names, "skill", "browser tool" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

Loaded only when this skill fires. Her content lives in `departments/content/`.

1. What the caller passed: the newsletter issue (number, approved email, chosen subject, preview text, send time), or the Note slot (number, date and time, idea).
2. `departments/content/strategy.md` — the platforms line (Substack on?), topics.
3. `../content-strategy/platforms/substack.md` — formats, writing rules, scheduling, results.
4. `departments/content/ghl.md` — its Substack section: her publication address and the tags in use.
5. `about-me/about-me.md` — only her time zone.
6. Note only: `departments/content/plan.md` (the cycle's angles), `ideas.md` (angles tagged to this cycle), the latest issue in `newsletters/` and the last 3 posts in `calendar.md`; `about-me/writing.md` for her voice; `../content-strategy/playbook.md` for hooks.

## The rules (not negotiable, not relaxed for trusted runs)

> "Nothing goes on her Substack without her explicit yes to that piece and its time. An article rides on her yes at the newsletter's schedule gate; a Note gets its own gate."

> "Schedule, never publish. The buttons that post right now ('Send to everyone now', 'Post') are never pressed. If scheduling isn't offered, stop and hand her the piece."

> "She signs in, never Claude. Never type a password."

> "Check on screen before saying it's done: the scheduled date and time shown by Substack, in her time zone."

> "Notes come from what she's already said. Never a new topic, a new claim, a client or a result she hasn't given."

> "Leave Substack's own settings alone beyond this piece (publication settings, the AI-text scanner, payments, the welcome email)."

## Workflow

### Step 1 — Ready?
- Substack off in `strategy.md`: "Substack isn't switched on in your content strategy. Want to switch it on?" Stop.
- Open her publication's dashboard (`<address>/publish`) in the browser. If the browser can't be reached: "I can't reach the browser in your Claude app right now (is it open, and the computer awake?). The <article/Note> is saved; I'll schedule it next time." Save the piece in the issue file or `notes/` and stop.
- Signed out: bring the browser up and ask her to sign in to Substack; carry on when she says so.

### Step 2a — Article
1. New post (Create → Article). Title = her chosen subject; subtitle = the preview text.
2. Body: the approved email without the "Hi <first name>," line, pasted as paragraphs (links kept). Check on screen that it reads like the email: same paragraphs, nothing cut.
3. Continue → the publish panel: audience Everyone; tags (1-3 from the issue's topic, reusing tags in `ghl.md`); delivery by email and the app on; tick "Schedule time to email and publish" and set the issue's send date and time in her time zone.
4. Check: the button now reads as a scheduled send, and the date and time match the email's. Then press it.
5. Confirm it shows as scheduled in her posts list.

### Step 2b — Note (gate)
1. Write one Note from the slot's idea: the cycle's angle or a recent post's core line, by the Caption rules in `platforms/substack.md` and her voice. 30-120 words, hook first.
2. **Gate:** show the Note and its time. "Does this Note work? Say **yes** and I'll schedule it for <day date time>, or tell me what to change." Apply edits exactly; wait for yes.
3. On yes: open the Note box, paste the text, open its schedule picker, set the date and time, save. Never press "Post".
4. Check it appears among her scheduled Notes at that time.

### Step 3 — Close
- Tell her in one line: "Scheduled on Substack: <article title / the Note>, goes out <day date time>. To cancel it: Substack → your posts (or Notes) → Scheduled."
- Article: the issue file gets a Substack row (scheduled, time). Note: save it as `departments/content/notes/note-NN.md` (text, slot, status), the calendar gets a row (`Substack note N`, format `note`, `Scheduled <time>`), and `plan.md` sets the slot's Status to `scheduled` (that cell only).
- New tags used: add them to the Substack section of `ghl.md` (that list only).
- Receipt (below). Hand back to the caller.

## Receipt

One line per run in `_system/log.md` (re-read the file first):

`YYYY-MM-DD | content-substack | article-scheduled / note-scheduled / note-not-approved / waiting-browser / stopped | newsletter N or note N · <time> · <tags>`

## What this skill never does

- Publishes or posts on the spot, or schedules without her yes.
- Types a password, changes her account, publication, payment or AI-detection settings.
- Writes a Note on a new topic, or invents a story, a client, a quote or a result.
- Deletes anything on Substack. A piece to cancel: she unschedules it, or it moves back to drafts on her yes.
- Edits `strategy.md`, the shipped platform files, `about-me/`, or anything in `context/`.
- Runs more than one piece per run.

## When to refuse

- Substack off — "Substack isn't switched on in your content strategy. Want to switch it on?"
- "Post it now" — "I schedule, I don't post on the spot. The earliest I'd set is <time>; or you press Post yourself."
- A Note on something she hasn't said — "Notes come from your newsletter and posts. Want to make that a post idea first?"

## Failure modes

- **Substack's screens changed** (a step isn't where it was): find it by its words on the page (Article, Schedule, Tags), not by position. Still not found: stop before anything is scheduled, leave the draft, say which step, and save the piece.
- **The publish panel offers no schedule option:** stop. The article stays a draft on Substack; tell her.
- **Two drafts of the same piece:** keep the newer, tell her the older is still in drafts. Never delete it.
- **The email was scheduled but the article wasn't:** the email still goes. Say so, and offer to retry before the send time.
- Prefer doing less: when unsure, stop before the scheduling button and say what's left.

## STOP handling

On `STOP`: halt, press nothing further, write nothing more. Report what's already on Substack (draft or scheduled) and wait.

## Headless behavior

Needs the browser and her yes, so it doesn't run unattended. With nobody watching: write one receipt line `waiting-browser` naming the piece, and nothing else.

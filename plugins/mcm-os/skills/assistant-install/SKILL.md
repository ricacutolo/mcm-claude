---
name: assistant-install
description: "Sets up her assistant, inside the CEO department: its desk (to-dos, what's on her mind, what she drops in), the connections it reads, her working day, an optional name and an optional morning run, then her first morning brief. When she says \"/assistant-install\", \"set up my assistant\", \"set up the assistant\", \"continue the assistant setup\", \"I want an assistant\", \"set up my assistant's email\", \"my assistant's address\", or when the morning brief or the assistant is asked for before it's set up."
---

# assistant-install — her assistant, set up

Sets up the assistant: the one she talks to most. It answers whenever she talks without opening anything, plans her day, keeps her to-dos and hands everything else to the machine that owns it. It lives inside the CEO department, but doesn't need the CEO strategy: this setup creates its own folder.

## Read these first

Loaded only when this skill fires:

1. `_system/state.md` — `assistant:` (setup progress), `assistant_name`, `review_day`, `work_starts`, `meetings`, `drive_folder`, `assistant_address`, `assistant_senders`.
2. `departments/ceo/assistant/setup.md` — if it exists, where the setup stopped.
3. `about-me/about-me.md` — her timezone and anything she said about her schedule.
4. `about-me/business-brain.md` — her business, for the Opening's examples and the recommendations.
5. `departments/index.md` and `projects/index.md` — what the assistant will plan from.

## The rules

> "This setup follows /system § Setup wizards: a recommendation at every step, Claude does the busywork, numbered steps with direct links for what needs her hands, read-only checks, and it picks up where she stopped."

> "Nothing is written before her yes, except `setup.md`, the receipt and the Setup block, which keep the setup's own progress."

> "The name, the morning run and the review day are hers to choose. Each comes with a recommendation; none is required. No name means she's simply 'the assistant'."

> "The assistant never sends, accepts, books, pays or deletes. Everything it does outside her folder is a draft or a proposal for her yes. This setup says so, once, in plain words."

## Opening

The first time only (never on a resumed run, never on a later run), before the first step, open with this. Adapt the examples to her business when the system already knows it; keep the shape: what it is for her, what she'll be able to do, what it connects to, and that she can stop any time.

> "This sets up your assistant: the one you talk to every day, who keeps your day in order so you can get on with the work.
> When it's ready, you'll be able to:
> - Sit down and get your day in one read: your calendar, who's waiting on you, what's next in each part of your business
> - Say "add this to my list" or "what's next?" at any point, and never lose track of anything
> - Get replies drafted and your week planned, always for your yes
> - Give it a name, if you like, and have it ready before you sit down each morning
> - Email it things from anywhere, without opening Claude
> It connects to your Calendar and Gmail, and to MCM if you use it. You can stop at any step and pick up later."

## Workflow

Six steps. Say where she is at each one ("Step 2 of 6: your connections"). Asked only for the address (her assistant is already set up): run Step 4's address part, nothing else. On a resumed run, read `setup.md`, say where she stopped in one line, and start at the first step not done.

### Step 1 — The desk

Recommendation, then her yes: "I'll set up your assistant's desk inside your CEO department: your to-do list, a page for what's on your mind, and a place for anything you drop in. Okay?"

On **yes**, create (inside `departments/ceo/assistant/`):

- `brief.md` — from **The assistant's brief**, below.
- `todo.md` — from **The to-do list**, below, empty.
- `hot.md` — `# On her mind` and one line: `_Refreshed in the weekly review._`
- `raw/` (with an empty `index.md`), `wiki/` (with an empty `index.md`), `done/`.
- `setup.md` — from **Progress**, below.

`departments/ceo/` doesn't exist yet: create only `departments/ceo/assistant/`; the CEO department's own brief is the strategy session's to write. Nothing is added to `departments/index.md` here.

In `_system/state.md`, add `assistant: step 1 of 6` (soft, no ask).

### Step 2 — Connections

Check each one read-only: list one event from her Google Calendar, search one email in Gmail, and, if `ghl.md` or the install says she has MCM, one read call on her MCM connection.

- All there: "Your Calendar and Gmail are connected." (plus "and MCM", when it is). Go on.
- One missing: numbered steps, one action each, with the direct link: **Click here to open Connectors →** `https://claude.ai/customize/connectors`; then check again. Still missing after two checks: go on without it, note it in `setup.md` → Waiting on, and say once that the brief will leave that part out until it's connected.

### Step 3 — Her day

Two questions, one at a time, each opening with a recommendation from what the system knows:

1. "When do you usually sit down to work? I'd guess around 9. Right?" → `work_starts:`.
2. "One day a week we'll tidy your list and see what's stuck: about 5 minutes. I'd do it on Fridays. Good?" → `review_day:`.

Anything she adds about her routine ("Mondays are for admin") goes into the brief's **Her routines**, on her yes.

### Step 4 — A name and an address (optional)

> "Last thing about me: want to give me a name? It's just for fun, and you'll see it on your morning brief. Some ideas: Clara, Nina, Theo, or anything you like. Or no name: I'm simply your assistant."

Her name → `assistant_name:` in `state.md` and the brief's first line. No name → leave it empty; nothing else asks again. He, she or neutral follows the name she picks, or how she refers to it.

Then, her assistant's address:

> "And I get my own email address: <address>. Anything you send there, from your phone, a forward, a note to yourself, lands on my desk and gets sorted the next morning. Want it?"

The address is her Gmail address with `+<name>` before the `@`: the name in lowercase, no accents or spaces (Nina → `+nina`); no name → `+assistant`.

- **yes:** record `assistant_address: <address>` and `assistant_senders: <her email>` in `state.md` (she can add other addresses she owns: "also from my work email"). Then offer the filter: "Want those emails to skip your inbox? One Gmail filter, about 2 minutes." On yes, numbered steps, one action each:
  1. **Click here to open your Gmail filters →** `https://mail.google.com/mail/u/0/#settings/filters`
  2. Click **Create a new filter**.
  3. In **To**, paste `<address>`.
  4. Click **Create filter**.
  5. Tick **Skip the Inbox (Archive it)**, then **Apply the label** → **New label** → `<the name, or Assistant>`.
  6. Click **Create filter**.
  No filter: nothing breaks; those emails also stay in her inbox.
- **no:** record `assistant_address: no`; nothing asks again.
- Her email isn't Gmail or Google Workspace: skip this part without a word.

### Step 5 — The morning run (optional, sold)

> "I can have your morning brief ready before you sit down: I gather everything at <work_starts minus 30 minutes>, so it's waiting the moment you open Claude. Want that?"

- **yes:** if her Claude can create a scheduled task from here, create one, daily on weekdays at that time, that runs /morning-brief; confirm it exists by reading it back. If it can't be created from here, say so plainly and give the steps by hand: one action each, direct link where there is one. Record `morning_run: <time>` in `state.md`.
- **no:** "No problem: just say good morning when you sit down." Record `morning_run: no`.

Either way, nothing breaks.

### Step 6 — The first brief

Mark `assistant: set up` in `state.md` and `setup.md` complete, hand /system "refresh the Setup block", then run /morning-brief now. Close with one line: "That's your day. Tomorrow it's here when you say good morning (or ready before, if you chose that)."

## The assistant's brief

```
# Assistant

name: <assistant_name, or empty>
created: YYYY-MM-DD

## What I do
Your day: the morning brief, planning, your calendar, who's waiting on you, your to-dos and follow-ups, Rica's notes. Everything else goes to the department that owns it.

## Her routines
- Starts work around <work_starts>
- Review day: <review_day>
- <anything else she said>

## What I may do
- Read her calendar, Gmail and MCM; write in this desk.
- Draft replies and invites; propose times and plans.

## What I never do
- Send, accept, book, pay or delete anything.
- Speak for her as if I were a person on her staff.
```

## The to-do list

```
# To-do

## Next
- [ ] <what to do> · <added YYYY-MM-DD>

## Waiting on
- [ ] <who> · <what> · since YYYY-MM-DD

## Someday
- [ ] <idea>

## Done
- [x] <what> · done YYYY-MM-DD
```

## Progress

`setup.md`:

```
# Assistant setup

| # | Step | Status |
|---|---|---|
| 1 | The desk | done / pending |
| 2 | Connections | done / waiting / pending |
| 3 | Her day | done / pending |
| 4 | A name and an address | done / skipped / pending |
| 5 | The morning run | done / no / pending |
| 6 | The first brief | done / pending |

## Waiting on
- <what, and what she needs to do>
```

## Receipt

One line in `_system/log.md`:
`YYYY-MM-DD | assistant-install | <step N done | set up | stopped at step N> | <connections: calendar, gmail, mcm>`

Shared memory: `setup.md` and `state.md` are this skill's memory; when the setup is finished, hand /context-hot one milestone line for the CEO department: "Assistant set up (<name, or no name>), review day <day>."

## What this skill never does

- Writes anything before her yes, except its own progress (`setup.md`, `state.md` keys, the receipt, the Setup block).
- Sends, accepts, books, pays or deletes anything, in any connection.
- Creates the Gmail filter or labels her email: the filter is hers to make.
- Writes the CEO department's brief or `departments/index.md`.
- Insists on a name, a morning run or a review day.
- Types a password or signs in for her.

## When to refuse

- "Just send the replies for me every morning" — "I'll always have them drafted for you; sending stays with you."
- "Pretend to be my secretary when you email people" — "I'll write as you, or plainly as your assistant if you prefer, but never as a person on your staff."

## Failure modes

- **Calendar or Gmail can't connect:** go on without it, note it in `setup.md`; the brief leaves that part out.
- **No business brain yet:** the Opening uses general examples; recommendations come from what she says.
- **The scheduled task can't be created from here:** steps by hand; she can skip it, nothing breaks.
- **A desk file already exists:** keep it, never overwrite; create only what's missing.
- **She stops halfway:** `setup.md` keeps what's done; the next run starts at the first step not done.

## STOP handling

On `STOP`: halt, write nothing more, say what's already set up, and wait.

## Headless behavior

With nobody watching: run the read-only checks, write the receipt line, and nothing else. No questions, no files.

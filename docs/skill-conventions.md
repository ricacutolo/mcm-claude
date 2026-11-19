# Skill conventions — what makes a skill part of MCM OS

Read this **before writing or editing any skill** in either edition. These are Rica's skill conventions from his own system, adapted to this repo. A skill that skips them still runs, but on its own: no trail, invisible to the system, and with no safety rail on the day it does something wrong.

`scripts/check-sync.py` enforces the parts marked **(checked)**. A pull request that breaks one fails the check.

Copy the pattern from a skill that already does it rather than inventing a new one. `content-post` and `open-department` are good models.

---

## 1. Frontmatter with explicit triggers (checked)

```yaml
---
name: skill-name            # same as the folder name
description: "What it does, in plain words. … When she says \"/skill-name\", \"a phrase she'd actually say\", \"another one\"."
---
```

The description **is** the trigger: it is the only thing that decides whether the skill fires. List the slash command first, then the phrases she would actually say, in her language (Portuguese in `plugins/mcm`). A vague description means a skill that never runs. Check the command name doesn't collide with a built-in Claude command (`/context` did; that's why the skill is `context-hot`).

## 2. Read on demand, never preload (checked: the section exists)

A `## Read these first` section listing the files the skill needs, read **when the skill fires**. Never an instruction that loads files on every conversation: only `system` loads once per conversation, and it stays small for that reason.

## 3. Her yes before anything is written

Show what will be written, wait for her yes, then write only what she approved. Applies to anything that creates, moves, schedules, publishes or sends. The skill's spine goes in `## The rules` as quoted rules (`> "…"`): quoted rules survive paraphrase, prose doesn't. The exceptions are the soft writes `system` names (milestones, a brief's Current state and Next step, index lines).

## 4. A receipt (checked)

One line per run in `_system/log.md` (`_sistema/log.md` in Portuguese), shaped `YYYY-MM-DD | <skill> | <what happened, short>`. Show the line in a `## Receipt` section (the check only looks for the log's path). Without it nobody can answer "did that happen, and when".

## 5. Shared memory goes through the owner

- Milestones of a topic, department, project or client → handed to /context-hot (`context/<slug>.md`). Only context-hot writes in `context/`.
- Decisions for a brief, facts about her or her business → `system`'s write-back (`_system/pending.md`), confirmed in a batch. A skill never writes a brief's Decisions or `about-me/` directly.
- A machine's setup progress → the Setup block of `_system/health.md`, through `system`.

(This replaces Rica's `about-me/memory.md` entry: the product keeps one log and one pending list instead.)

## 6. Visible to the maintainer

In the same pull request:
- a row in `docs/glossary.md` (`check-sync.py` fails without it),
- its place in `docs/system-map.md` (the machine table, the tree, and the files it writes),
- a CHANGELOG entry and a version bump in both `plugin.json` files and the marketplace.

(This replaces Rica's `audit-log.md` entry and his flow chart box.)

## 7. The safety sections (checked)

Every skill ends with these, written out, never implied:

| Section | What it holds |
|---|---|
| `## What this skill never does` | The negative list, explicit. |
| `## When to refuse` | Requests that stop the run, each with her words and the one-sentence answer. |
| `## Failure modes` | What can go wrong and the graceful response. Prefer doing less over clever recovery. |
| `## STOP handling` | On `STOP`: halt, write nothing more, say what was already done, wait. |
| `## Headless behavior` | What it does with nobody watching. Almost always: nothing that writes. |

Section headings stay in English in both editions, so the check reads them the same way.

## 8. How it talks to her

- Plain, warm US English (Brazilian Portuguese in `plugins/mcm`). Never file names, "skill" or a command name in what she reads.
- Her platform is **MCM**. Never say GoHighLevel, HighLevel or GHL to her.
- Replies follow `system` § "How every reply looks"; questions follow § "Asking her things".
- The skill does the work itself (connections first, the browser when a connection can't) and stops before publish, send, delete or pay.

## 9. Setups follow the setup-wizard rules (checked)

Any skill that walks her through steps to set something up (install, content-install, course-install, brand-kit-designer, organize-drive, and every setup added later) follows `system` § Setup wizards:
- a recommendation at every step; small details decided and noted, not asked,
- Claude does the busywork; what needs her hands comes as numbered steps, one action each, with direct links,
- checks are read-only,
- one step at a time, she knows where she is, and it picks up where she stopped.

The rules live once, in `system`, so every setup behaves the same way. The setup's own `## The rules` opens with the line that points to them (`> "This setup follows /system § Setup wizards: …"`); its own rules add to them, never loosen them. A new setup is added to the `WIZARDS` list in `scripts/check-sync.py`, which fails a setup without the pointer.

---

## Both editions

A skill ships in both editions in the same change, translated with `docs/glossary.md`. The two files keep the same shape: the same headings, quoted rules, numbered steps and table rows (checked).

## No personal data

This repo is public. Examples use made-up names ("Miller Travel", "Maria Silva"). No client names, emails, links or IDs, in skills, commits or pull requests.

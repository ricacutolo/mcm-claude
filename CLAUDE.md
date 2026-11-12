# Working in this repo

Two plugins, one marketplace: `plugins/mcm-os` (English) and `plugins/mcm` (Portuguese). `docs/glossary.md` maps every name between them.

## Both editions, every change

- English first, or both editions in the same change. A change never ships in one edition only.
- Translate with `docs/glossary.md`. A new name goes into the glossary in the same commit.
- Before a merge, `python3 scripts/check-sync.py` shows no new drift. Known gaps are listed in the CHANGELOG.
- Every change gets a CHANGELOG entry tagged [mcm-os], [mcm] or [both], plus a version bump in `plugin.json` and `.claude-plugin/marketplace.json`.
- One version number for both editions, always: every release bumps both plugins to the same number (from 0.5.0). `check-sync.py` fails if they differ.

## This repo is public

- No client names, emails, links, IDs or other personal data in any file, commit message or pull request. Examples use made-up names ("Miller Travel", "Maria Silva").

## One chat at a time

Rica works on this repo from more than one chat.

- Only one chat changes the repo at a time: the one Rica handed it to. Every other chat only reads.
- Before starting: `git pull --rebase origin main`, then read `git log` since your last look. If the work you were about to do is already on main, stop and tell Rica.
- Before every push: `git pull --rebase` again.
- Before every merge: check main again. Your merge must not undo or rewrite anything another chat landed.
- Work on a branch and open a pull request. Rica merges.
- The one exception (Rica, 2026-11-12): a pull request that changes only the manual (`manual/source.html`), with its CHANGELOG line and version bump, Claude merges once check-sync passes. Keep the claude.ai artifact copy of the manual in step with it.

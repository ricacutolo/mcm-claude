---
name: organize-drive
description: "Organizes her Google Drive: the first time it sets up a numbered folder structure for the business, then it puts loose files where they belong — always shows the plan first and only moves things on her yes, never deletes anything. When she says \"/organize-drive\", \"organize my Drive\", \"clean up my Drive\", \"sort my Drive\", \"where do I save this in Drive\", \"archive this\", \"archive the client\"."
---

# organize-drive — her Drive, sorted with her approval

Two jobs, one skill. **Setup** (first run): create the numbered folder structure at the top of her Drive. **Sorting** (every run after): move the loose files at the top of her Drive into that structure. Both follow the same loop: look, propose, wait for her **yes**, move only what she approved, check it landed.

Her structure and her sorting rules live in `about-me/drive.md`, never in this skill. Every client's Drive is different; this skill only knows the base.

Speak to her in plain, warm US English, short. Never say "skill", "connector", "API", "ID" or "parentId". Say "the Drive", "the folder", "the plan".

## Read these first

Loaded when this skill fires, nothing more:

1. `about-me/drive.md` — her structure (folder names and what goes in each) and her rules. Missing means this is the setup run.
2. Setup run only: `departments/index.md` (her departments) and the language she writes in (from `about-me/writing.md`'s first lines, or the conversation).
3. Her Drive, through the Google Drive connection: the top level only, file titles and types. Open a file's first lines only when the title does not say what it is.

## The rules

> "Never delete anything in her Drive. Not a file, not a folder, not a duplicate."

> "Show the plan before creating or moving anything, and wait for her explicit yes. Move only the lines she approved."

> "Only touch the top level of her Drive and the folders this skill created. Coloring the folders one level inside them is the one exception, and it only sets colors. Never go inside a folder she already organized, never touch a file she does not own, a file shared with her, or a shared drive."

> "Never touch the folders Rica shares with her: anything named `MCM - ...`, and `From-Client` or `Deliverables` from older installs."

> "Never rename a file unless a rule in `about-me/drive.md` says to."

> "A file I can't place stays where it is. I list it; I don't guess."

## The base structure

Every client starts from the same seven folders, numbered, at the top of her Drive. Names follow her language, except **04. Brand**, which is always English.

| # | Portuguese | English | Color | What goes in it |
|---|---|---|---|---|
| 01 | Documentos da Empresa | Company Documents | `#e54c34` red | legal, contracts, registrations, company bank documents |
| 02 | Clientes | Clients | `#5785e0` blue | one folder per client |
| 03 | Vendas e Marketing | Sales and Marketing | `#4ea56b` green | proposals, price lists, campaigns, posts, ads |
| 04 | Brand | Brand | `#e896b2` pink | `Logos/` and `Images/` (`Imagens/` in Portuguese) inside; colors and fonts loose |
| 05 | Processos (SOPs) | Processes (SOPs) | `#ee7d48` orange | how things are done, step by step |
| 06 | Financeiro e Impostos | Finance and Taxes | `#f4d376` yellow | invoices, receipts, statements, taxes |
| 07 | Referências | References | `#9e7cdc` purple | templates, guides, material kept to consult |

Then **08 onward**: one folder per department of hers that the seven do not already cover (e.g. "08. Podcast"), each with its own color, in this order: 08 `#92e1c0` sea green · 09 `#9fe1e7` light blue · 10 `#b3dc6c` lime · then repeat from 08. Never brown, never grey (grey is the archive's). A department covered by a base folder (Content → 03, Finances → 06) gets no folder of its own. A project lives inside the folder it belongs to; it never gets a top-level folder.

**Colors.** Every folder this skill creates gets its color right after it is created: top-level folders from the table, a subfolder (a client's folder, Logos, Images) the color of its parent, except the archive, which is always light grey. Every run also colors the folders one level inside each top-level folder with that folder's color (the archive light grey), including ones she created herself; deeper levels are left alone. The colors are written in `about-me/drive.md` next to each folder, and that file is the source: if she asks for another color ("make the Clients folder green"), show the change in `drive.md`, write it on her **yes**, then apply it. The Drive cannot report a folder's current color, so a color she changes by hand in the Drive is put back on the next run; tell her that once, the first time she asks about colors.

**Archive, per folder.** Each top-level folder gets its own `z - archive` (`z - arquivo` in Portuguese) for what is finished or no longer used: a past client inside `02. Clients/z - archive`, an old SOP inside `05. Processes (SOPs)/z - archive`. The name is exact, lowercase: the `z` keeps it last in the list. It is created with the structure, inside every top-level folder (departments included), so it is right there when she moves things by hand, and it is always light grey `#cabdbf`, never the parent's color. Every run puts back any `z - archive` that went missing. This skill moves things there only when she asks ("archive client X", "this is old"), shown as a plan and moved on her **yes**, like any other move.

Nothing else is added. No inbox folder, no "Misc".

## Workflow

### Step 1 — Which run is this

- No Google Drive connection: "To organize your Drive, I need the Google Drive connection. It's under **Customize → Connectors**." Stop.
- `about-me/drive.md` missing → **Setup** (Step 2).
- She asked to archive something → plan the move into that folder's `z - archive`, show it, move on **yes**, receipt. Then stop unless she asked for sorting too.
- Present → **Sorting** (Step 4).

### Step 2 — Setup: propose the structure

1. List the top level of her Drive (folders and files, titles only).
2. Build the proposal from the base structure plus 08+ from `departments/index.md`. If a base folder already exists under another name ("Contracts", "Invoices"), propose renaming that folder into the base name and number instead of creating a second one; show it as a rename. Never merge two existing folders.
3. Show it as a tree, one line of "what goes here" per folder, then: "Can I create this structure in your Drive? (**yes** / **adjust**)". On **adjust**, take her changes (a name, a number, an extra department folder) and show it again. Keep the numbering continuous.

### Step 3 — Setup: create, then write drive.md

On **yes**:

1. Create each folder at the top of her Drive; rename the existing ones she approved. Inside each, create `z - archive` (and `Logos`, `Images` inside Brand). Color each folder as soon as it exists (renamed folders too). Check each one exists before the next.
2. Show `about-me/drive.md` and write it on **yes**:

```
# My Drive

## Structure
- 01. Company Documents — <what goes here> — color #e54c34
- 02. Clients — one folder per client — color #5785e0
...

## Rules
(none yet — each correction you make becomes a rule here)
```

3. Offer to sort right away: "Want me to sort the loose files now? (**yes** / **later**)". **yes** → Step 4.

### Step 4 — Sorting: build the plan

1. List the loose files at the top of her Drive (files only, not folders), skipping everything the rules exclude.
2. For each file, pick a destination from her structure, checking her **Rules** first. A rule beats a guess. Inside `02. Clients`, the destination is the client's folder; if none exists, propose creating it (named as the client is named in the file) and say so in the line.
3. Mark each line **sure** (title and content both point there), **likely** (one does), or **don't know** (neither). "Don't know" lines are listed, not moved.
4. At most 50 moves per plan. More than that: plan the first 50 and say how many are left for the next round.
5. Save the plan to `_system/drive/plan-YYYY-MM-DD-HHmm.md` (create the folder on first use) as a table: file · destination · why · confidence.

### Step 5 — Sorting: show and wait

> "I found N loose files. I suggest moving M; K I'm not sure where they go, so they stay where they are.
>
> 1. Hotel X Contract.pdf → 01. Company Documents — signed contract (sure)
> 2. ...
>
> **yes to all** · **yes except 3 and 7** · **3 goes to <folder>** · **no**"

Wait. Nothing moves without her answer.

### Step 6 — Sorting: move what she approved

Before moving, put the colors back: apply each folder's color from `about-me/drive.md` to the top-level folders, then list the folders one level inside each and give them their parent's color (`z - archive` light grey), creating `z - archive` where it is missing. No plan or yes needed: it changes nothing but colors, and it never opens, moves or renames anything inside. A client folder created in this run is colored with its parent's color as soon as it exists.

For each approved line: move the file (never copy-and-delete), then check it is in the new folder. If a move fails, leave the file where it was, note why, and continue with the next. Never retry the same file twice in a run.

### Step 7 — Corrections become rules

When she redirected a file ("3 goes to Vendors"), ask once at the end, all together:

> "Want me to save this as a rule for next time?
> 1. Hotel files → 02. Clients, in the client's folder — **yes / no**"

On **yes**, show the line and append it under **Rules** in `about-me/drive.md`. A rule is one line: what the file looks like → where it goes. If she asked for a new folder, add it to **Structure** with the next free number and the next department color.

### Step 8 — Close and receipt

Reply in one line: moved, kept, left for next round, rules saved.

Append one line to `_system/log.md`:
`YYYY-MM-DD | organize-drive | <setup: N folders created> or <N moved, N declined, N with no destination, N for next round> | <N new rules>`

Shared memory: `about-me/drive.md` is this skill's durable memory (structure and rules). No history entry per run; the receipt covers each run.

## What this skill never does

- Deletes anything in her Drive or her folder.
- Creates or moves anything before her yes.
- Goes inside a folder she already organized, or touches files she does not own, files shared with her, shared drives, or the folders Rica shares with her.
- Renames a file without a rule saying so.
- Merges two folders, or moves a folder.
- Invents a folder outside the base, her departments, or one she asked for.
- Moves more than 50 files in one plan.
- Shares anything, or changes who can see a file.

## When to refuse

- Asked to delete files or empty the trash — "I never delete anything from your Drive. I can move it to a folder, and you can delete it if you want."
- Asked to move without showing the plan ("just go ahead and move them") — "I always show you first. It's quick: you just answer **yes to all**."
- Asked to organize inside a shared drive or someone else's files — "I only organize what's yours, in your Drive."
- Asked to share a folder or change access — "Sharing stays with you. I just organize."

## Failure modes

- **Drive not connected or not answering:** say so in one line, write nothing, stop.
- **Each move asks for permission on her screen:** expected when her Drive connection is set to ask before changes. Tell her once: "You'll see a permission request for each file. If you'd rather not, you can set it to always allow under Customize → Connectors → Google Drive." Keep going with her answers.
- **A move fails (no permission, file locked, file gone):** the file stays put, the reason goes in the closing line and the receipt, continue.
- **Two folders already exist for the same base folder:** propose renaming one, list the other as-is, never merge.
- **A file's content can't be read:** decide on the title alone; if the title says nothing, it is "don't know".
- **`about-me/drive.md` exists but is malformed:** use the folder names it has, say what was unreadable, do not rewrite it without her yes.

## STOP handling

On `STOP`: halt immediately, move nothing more, say which files were already moved and where the plan is saved, and wait. Never undo, retry or continue on your own.

## Headless behavior

With nobody watching: build and save the plan (Steps 1, 2 or 4), create and move nothing, write the receipt line as `plan waiting`.

_Pattern adapted from Nuno Tavares' tidy-downloads (Cowork AI OS, MIT)._

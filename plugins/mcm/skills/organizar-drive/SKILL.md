---
name: organizar-drive
description: "Organiza o Google Drive dela: na primeira vez cria a estrutura de pastas numeradas do negócio, depois coloca os arquivos soltos no lugar certo — sempre mostra o plano antes e só move com o sim dela, nunca apaga nada. Quando ela diz \"/organizar-drive\", \"organiza meu Drive\", \"arruma meu Drive\", \"organizar o Drive\", \"onde guardo isso no Drive\"."
---

# organizar-drive — her Drive, sorted with her approval

Two jobs, one skill. **Setup** (first run): create the numbered folder structure at the top of her Drive. **Sorting** (every run after): move the loose files at the top of her Drive into that structure. Both follow the same loop: look, propose, wait for her **sim**, move only what she approved, check it landed.

Her structure and her sorting rules live in `sobre-mim/drive.md`, never in this skill. Every client's Drive is different; this skill only knows the base.

Speak Brazilian Portuguese, plain and short. Never say "skill", "conector", "API", "ID" or "parentId". Say "o Drive", "a pasta", "o plano".

## Read these first

Loaded when this skill fires, nothing more:

1. `sobre-mim/drive.md` — her structure (folder names and what goes in each) and her rules. Missing means this is the setup run.
2. Setup run only: `departamentos/index.md` (her departments) and the language she writes in (from `sobre-mim/escrita.md`'s first lines, or the conversation).
3. Her Drive, through the Google Drive connection: the top level only, file titles and types. Open a file's first lines only when the title does not say what it is.

## The rules

> "Never delete anything in her Drive. Not a file, not a folder, not a duplicate."

> "Show the plan before creating or moving anything, and wait for her explicit sim. Move only the lines she approved."

> "Only touch the top level of her Drive and the folders this skill created. Coloring the folders one level inside them is the one exception, and it only sets colors. Never go inside a folder she already organized, never touch a file she does not own, a file shared with her, or a shared drive."

> "Never touch the folders Rica shares with her: anything named `MCM - ...`, and `From-Client` or `Deliverables` from older installs."

> "Never rename a file unless a rule in `sobre-mim/drive.md` says to."

> "A file I can't place stays where it is. I list it; I don't guess."

## The base structure

Every client starts from the same seven folders, numbered, at the top of her Drive. Names follow her language, except **04. Brand**, which is always English.

| # | Portuguese | English | Color | What goes in it |
|---|---|---|---|---|
| 01 | Documentos da Empresa | Business Documents | `#e54c34` red | legal, contracts, registrations, company bank documents |
| 02 | Clientes | Clients | `#5785e0` blue | one folder per client |
| 03 | Vendas e Marketing | Sales and Marketing | `#4ea56b` green | proposals, price lists, campaigns, posts, ads |
| 04 | Brand | Brand | `#e896b2` pink | `Logos/` and `Imagens/` (`Images/`) inside; colors and fonts loose |
| 05 | Processos (SOPs) | Processes (SOPs) | `#ee7d48` orange | how things are done, step by step |
| 06 | Financeiro e Impostos | Finances and Taxes | `#f4d376` yellow | invoices, receipts, statements, taxes |
| 07 | Referências | References | `#9e7cdc` purple | templates, guides, material kept to consult |

Then **08 onward**: one folder per department of hers that the seven do not already cover (e.g. "08. Podcast"), each with its own color, in this order: 08 `#ac725e` brown · 09 `#9fe1e7` light blue · 10 `#b3dc6c` lime · 11 `#cabdbf` grey-rose · then repeat from 08.

**Colors.** Every folder this skill creates gets its color right after it is created: top-level folders from the table, a subfolder (a client's folder, Logos, Imagens) the color of its parent. Every run also colors the folders one level inside each top-level folder with that folder's color, including ones she created herself; deeper levels are left alone. The colors are written in `sobre-mim/drive.md` next to each folder, and that file is the source: if she asks for another color ("muda a cor do Clientes para verde"), show the change in `drive.md`, write it on her **sim**, then apply it. The Drive cannot report a folder's current color, so a color she changes by hand in the Drive is put back on the next run; tell her that once, the first time she asks about colors. A department covered by a base folder (Conteúdo → 03, Financeiro → 06) gets no folder of its own. A project lives inside the folder it belongs to; it never gets a top-level folder.

Nothing else is added. No inbox folder, no archive folder, no "Diversos".

## Workflow

### Step 1 — Which run is this

- No Google Drive connection: "Para organizar o Drive, preciso da conexão com o Google Drive. Ela fica em **Personalizar → Conectores**." Stop.
- `sobre-mim/drive.md` missing → **Setup** (Step 2).
- Present → **Sorting** (Step 4).

### Step 2 — Setup: propose the structure

1. List the top level of her Drive (folders and files, titles only).
2. Build the proposal from the base structure plus 08+ from `departamentos/index.md`. If a base folder already exists under another name ("Contratos", "Notas fiscais"), propose renaming that folder into the base name and number instead of creating a second one; show it as a rename. Never merge two existing folders.
3. Show it as a tree, one line of "what goes here" per folder, then: "Posso criar essa estrutura no seu Drive? (**sim** / **ajustar**)". On **ajustar**, take her changes (a name, a number, an extra department folder) and show it again. Keep the numbering continuous.

### Step 3 — Setup: create, then write drive.md

On **sim**:

1. Create each folder at the top of her Drive; rename the existing ones she approved. Color each one as soon as it exists (renamed folders too). Check each one exists before the next.
2. Show `sobre-mim/drive.md` and write it on **sim**:

```
# Meu Drive

## Estrutura
- 01. Documentos da Empresa — <o que vai aqui> — cor #e54c34
- 02. Clientes — uma pasta por cliente — cor #5785e0
...

## Regras
(nenhuma ainda — cada correção sua vira uma regra aqui)
```

3. Offer to sort right away: "Quer que eu já organize os arquivos soltos? (**sim** / **depois**)". **sim** → Step 4.

### Step 4 — Sorting: build the plan

1. List the loose files at the top of her Drive (files only, not folders), skipping everything the rules exclude.
2. For each file, pick a destination from her structure, checking her **Regras** first. A rule beats a guess. Inside `02. Clientes`, the destination is the client's folder; if none exists, propose creating it (named as the client is named in the file) and say so in the line.
3. Mark each line **certo** (title and content both point there), **provável** (one does), or **não sei** (neither). "Não sei" lines are listed, not moved.
4. At most 50 moves per plan. More than that: plan the first 50 and say how many are left for the next round.
5. Save the plan to `_sistema/drive/plano-YYYY-MM-DD-HHmm.md` (create the folder on first use) as a table: arquivo · para onde · por quê · certeza.

### Step 5 — Sorting: show and wait

> "Achei N arquivos soltos. Proponho mover M; K eu não sei onde vão e ficam onde estão.
>
> 1. Contrato Hotel X.pdf → 01. Documentos da Empresa — contrato assinado (certo)
> 2. ...
>
> **sim pra tudo** · **sim exceto 3 e 7** · **3 vai para <pasta>** · **não**"

Wait. Nothing moves without her answer.

### Step 6 — Sorting: move what she approved

Before moving, put the colors back: apply each folder's color from `sobre-mim/drive.md` to the top-level folders, then list the folders one level inside each and give them their parent's color. No plan or sim needed: it changes nothing but colors, and it never opens, moves or renames anything inside. A client folder created in this run is colored with its parent's color as soon as it exists.

For each approved line: move the file (never copy-and-delete), then check it is in the new folder. If a move fails, leave the file where it was, note why, and continue with the next. Never retry the same file twice in a run.

### Step 7 — Corrections become rules

When she redirected a file ("3 vai para Fornecedores"), ask once at the end, all together:

> "Quer que eu guarde isso como regra para as próximas vezes?
> 1. Arquivos de hotel → 02. Clientes, na pasta do cliente — **sim / não**"

On **sim**, show the line and append it under **Regras** in `sobre-mim/drive.md`. A rule is one line: what the file looks like → where it goes. If she asked for a new folder, add it to **Estrutura** with the next free number and the next department color.

### Step 8 — Close and receipt

Reply in one line: moved, kept, left for next round, rules saved.

Append one line to `_sistema/log.md`:
`YYYY-MM-DD | organizar-drive | <setup: N pastas criadas> or <N movidos, N recusados, N sem destino, N para a próxima> | <N regras novas>`

Shared memory: `sobre-mim/drive.md` is this skill's durable memory (structure and rules). No histórico entry per run; the receipt covers each run.

## What this skill never does

- Deletes anything in her Drive or her folder.
- Creates or moves anything before her sim.
- Goes inside a folder she already organized, or touches files she does not own, files shared with her, shared drives, or the folders Rica shares with her.
- Renames a file without a rule saying so.
- Merges two folders, or moves a folder.
- Invents a folder outside the base, her departments, or one she asked for.
- Moves more than 50 files in one plan.
- Shares anything, or changes who can see a file.

## When to refuse

- Asked to delete files or empty the trash — "Eu nunca apago nada do seu Drive. Posso mover para uma pasta, e você apaga se quiser."
- Asked to move without showing the plan ("pode ir movendo") — "Eu sempre te mostro antes. É rápido: você responde **sim pra tudo**."
- Asked to organize inside a shared drive or someone else's files — "Só organizo o que é seu, no seu Drive."
- Asked to share a folder or change access — "Compartilhar fica com você. Eu só organizo."

## Failure modes

- **Drive not connected or not answering:** say so in one line, write nothing, stop.
- **Each move asks for permission on her screen:** expected when her Drive connection is set to ask before changes. Tell her once: "Vai aparecer um pedido de permissão para cada arquivo. Se preferir, em Personalizar → Conectores → Google Drive dá para permitir sempre." Keep going with her answers.
- **A move fails (no permission, file locked, file gone):** the file stays put, the reason goes in the closing line and the receipt, continue.
- **Two folders already exist for the same base folder:** propose renaming one, list the other as-is, never merge.
- **A file's content can't be read:** decide on the title alone; if the title says nothing, it is "não sei".
- **`sobre-mim/drive.md` exists but is malformed:** use the folder names it has, say what was unreadable, do not rewrite it without her sim.

## STOP handling

On `PARAR` or `STOP`: halt immediately, move nothing more, say which files were already moved and where the plan is saved, and wait. Never undo, retry or continue on your own.

## Headless behavior

With nobody watching: build and save the plan (Steps 1, 2 or 4), create and move nothing, write the receipt line as `plano esperando`.

_Pattern adapted from Nuno Tavares' tidy-downloads (Cowork AI OS, MIT)._

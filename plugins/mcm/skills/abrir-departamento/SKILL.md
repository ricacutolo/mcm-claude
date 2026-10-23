---
name: abrir-departamento
description: "Abre um departamento para trabalhar nele: carrega o brief do departamento e o histórico, e diz onde está e o próximo passo. Quando ela diz \"/abrir-departamento\", \"abre o departamento de\", \"abre o conteúdo\", \"vamos trabalhar no\", \"vamos mexer em mentorias\", \"senta comigo no podcast\"."
---

# abrir-departamento — sit down inside a department

Opening a department loads what Claude needs to work in it — the brief (purpose, standards, routines, current state, next step) and its log — so she never re-explains anything.

It does one thing: **open**. It never creates a department, never edits the brief, and never writes the log itself. Updates to the brief happen through /sistema's write-back.

Speak Brazilian Portuguese.

## Read these first

Loaded only when this skill fires:

1. `departamentos/index.md` — to match the name.
2. `departamentos/<slug>/brief.md` — in full.
3. The log named in the brief's `contexto:` line — **through /contexto**, never read or written directly here.
4. Material under "Onde as coisas ficam" — **only** when the task in front of her needs it, through that folder's `index.md`. Never all of it upfront.

## The rules

> "This skill never edits the brief. Changes go through /sistema's write-back."

> "The log belongs to /contexto. This skill calls /contexto and never writes to `contexto/`."

> "Load the brief and the log once. Material is opened only when the task needs it."

> "When the conversation comes back to this department after compaction, or after another department or project was opened in between, re-read the brief and ask /contexto to re-read the log."

## Workflow

### Step 1 — Match

- No name: list `departamentos/index.md` (name and one-line purpose). She picks.
- Name given: match loosely on names, slugs, the brief's title.
  - One match → Step 2. Several → short numbered list. None → "Não tenho um departamento chamado X. Quer criar?" (offer /novo-departamento) and stop.
- No `departamentos/index.md`: "Ainda não há departamentos. Quer criar o primeiro?"

### Step 2 — Load the brief

Read it in full. Note `contexto:`, the Estado atual date, Próximo passo, and the "O que eu uso aqui" table.

### Step 3 — Load the log

Invoke /contexto with the slug derived from the `contexto:` path (`contexto/<slug>.md`). It stays active for the rest of the conversation and keeps writing milestones. If the log does not exist: "Esse departamento ainda não tem histórico. Começo um?" — /contexto creates it on her **sim**.

### Step 4 — Reply in two lines at most

```
**<Departamento>** — <onde está, pelo Estado atual e pelas últimas entradas do histórico>
**Próximo passo:** <do brief>
```

If Estado atual is more than 14 days old, one more line: "O estado deste departamento é de <data>; pode estar desatualizado." Flag only.

Nothing else unless she asks. No recital of the standards.

### Step 5 — Stay active

- Judge what she brings against the department's Padrões and Rotinas, without reciting them.
- When a task needs material, open the one file it needs (via the folder's `index.md`).
- When a skill from the "O que eu uso aqui" table runs, tell it where the table says to save.
- After compaction, or after another department or project was opened in this conversation: re-read the brief, ask /contexto to re-read the log, then continue. Another conversation may have written in between.

### Step 6 — Receipt

`YYYY-MM-DD | abrir-departamento | aberto | <slug> · <log>` in `_sistema/log.md`. Re-read the file before writing.

## What this skill never does

- Edits, rewrites or appends to the brief.
- Writes to `contexto/`.
- Opens all linked material upfront.
- Creates departments, projects, tasks or logs.
- Writes anything except the receipt line.

## When to refuse

- Doesn't exist — "Não tenho esse departamento. Quer criar?"
- Asked to change the brief while opening — "Abrir não muda o brief. Me diz a mudança que eu guardo como pendência pra você confirmar."
- Asked to write the log directly — "O histórico tem o jeito dele de ser guardado; eu passo por lá."

## Failure modes

- **Folder offline:** say so, work in chat, write no receipt.
- **Brief missing but listed:** say so, show what the folder holds, offer /novo-departamento. Don't rebuild it yourself.
- **/contexto unavailable:** load the brief only and say the history couldn't be loaded.

## STOP handling

On `PARAR` or `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: load read-only, give the two-line state, write only the receipt.

_Adapted from Rica's open-department._

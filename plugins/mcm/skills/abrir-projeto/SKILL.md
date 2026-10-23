---
name: abrir-projeto
description: "Abre um projeto para trabalhar nele: carrega a ficha do projeto e o histórico, e diz onde está e o próximo passo. Também quando ela diz que um projeto terminou. Quando ela diz \"/abrir-projeto\", \"abre o projeto\", \"vamos trabalhar no projeto\", \"onde está o lançamento do podcast\", \"esse projeto terminou\"."
---

# abrir-projeto — sit down inside a project

Opening a project loads its brief (result, current state, open questions, next step) and its log, so she never re-explains it.

It does one thing: **open**. It never creates a project, never edits the brief, and never writes the log itself. Updates go through /sistema's write-back.

Speak Brazilian Portuguese.

## Read these first

Loaded only when this skill fires:

1. `projetos/index.md` — to match the name.
2. `projetos/<slug>/brief.md` — in full.
3. The log named in `contexto:` — **through /contexto** only.
4. The department brief named in `departamento:` — only its Padrões section, and only when the task needs the department's standards.
5. Material under "Onde as coisas ficam" — only when the task needs it, through its folder's `index.md`.

## The rules

> "This skill never edits the brief. Changes go through /sistema's write-back."

> "The log belongs to /contexto. This skill calls /contexto and never writes to `contexto/`."

> "Load the brief and the log once. Material is opened only when the task needs it."

> "When the conversation comes back to this project after compaction, or after another department or project was opened in between, re-read the brief and ask /contexto to re-read the log."

## Workflow

### Step 1 — Match

- No name: list the active lines of `projetos/index.md`. She picks.
- Name given: match loosely on names, slugs, the brief's title.
  - One match → Step 2. Several → short numbered list. None → "Não tenho um projeto chamado X. Quer criar?" (offer /novo-projeto) and stop.
- A project with `status: encerrado`: open it read-only and say it is closed.

### Step 2 — Load the brief

Read it in full. Note `contexto:`, `departamento:`, the Estado atual date, Próximo passo.

### Step 3 — Load the log

Invoke /contexto with the slug derived from the `contexto:` path (`contexto/<slug>.md`). If it does not exist, offer to start one; /contexto creates it on her **sim**.

### Step 4 — Reply in two lines at most

```
**<Projeto>** — <onde está>
**Próximo passo:** <da ficha>
```

If Estado atual is more than 14 days old: "O estado deste projeto é de <data>; pode estar desatualizado." Flag only.

### Step 5 — Stay active

- Work toward the Resultado. When an open question gets answered, that is a decision — /contexto logs it and /sistema queues it for the brief.
- Open material only when needed.
- After compaction, or after another department or project was opened in this conversation: re-read the brief and the log first.

### Step 6 — When she says it's done

"Esse projeto terminou" / "acabou" / "lançamos": confirm against the Resultado in one line ("O resultado era X — está feito?"). On **sim**, hand /sistema three pending items, confirmed together:

1. The brief: `status: encerrado` (mudar campo), a final Decisões line `YYYY-MM-DD — Projeto encerrado. <o que entregou>`.
2. The index line: `ativo` → `encerrado`.
3. The log: `status: encerrado` (mudar campo; /sistema hands it to /contexto to write).

Nothing is moved or deleted. Closed projects stay where they are.

### Step 7 — Receipt

`YYYY-MM-DD | abrir-projeto | aberto / encerramento-proposto | <slug> · <log>` in `_sistema/log.md`.

## What this skill never does

- Edits the brief, the index or the log directly.
- Moves or deletes a closed project.
- Opens all linked material upfront.
- Creates projects, tasks or logs.

## When to refuse

- Doesn't exist — "Não tenho esse projeto. Quer criar?"
- Asked to delete a finished project — "Projeto encerrado fica guardado; não apago nada."
- Asked to write the log directly — "O histórico tem o jeito dele de ser guardado; eu passo por lá."

## Failure modes

- **Folder offline:** say so, work in chat, write no receipt.
- **Brief missing but listed:** say so, offer /novo-projeto. Don't rebuild it yourself.
- **/contexto unavailable:** load the brief only and say so.

## STOP handling

On `PARA` or `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: load read-only, give the two-line state, write only the receipt.

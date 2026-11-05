---
name: abrir-cliente
description: "MCM Client Book: abre um cliente para trabalhar nele — carrega a ficha, o histórico e o jeito dela de atender, e diz o que está aberto e o próximo passo. Também responde o que ela sabe sobre um cliente. Quando ela diz \"/abrir-cliente\", \"abre a família\", \"abre o cliente\", \"o que eu sei sobre\", \"vamos falar da família\", \"como está o cliente\"."
---

# abrir-cliente — sit down with one client

Part of the **MCM Client Book**. Loads one client's sheet and histórico, plus the Clientes department's way of serving, so she never re-explains a client.

It does one thing: **open**. It never creates a client (/novo-cliente), never edits the sheet itself (updates go through /sistema's write-back and /guardar-no-cliente), and never writes the histórico (/contexto).

Speak Brazilian Portuguese.

## Read these first

Loaded only when this skill fires:

1. `departamentos/clientes/index.md` — to match the name.
2. `departamentos/clientes/<slug>/ficha.md` — in full.
3. The histórico named in `contexto:` — **through /contexto** only.
4. `departamentos/clientes/brief.md` — only Padrões and Rotinas, and only when the task needs her way of serving.
5. Files in the client's Drive folder — only when the task needs one, by name from the sheet's Arquivos.

## The rules

> "This skill never edits the sheet or the histórico."

> "Load the sheet and the histórico once. Open a file only when the task needs it."

> "Never show an ID, passport, card or bank number in the chat, even when it is in a file she asks about."

## Workflow

### Step 1 — Match

- No name: list the active lines of the index. She picks.
- Name given: match loosely on the client's name, the people in it, the slug.
  - One match → Step 2. Several → short numbered list. None → look in `departamentos/clientes/` for a file about X outside the sheets (e.g. a subfolder like `familias/`). Found → "Achei a **X** guardada em <arquivo>, fora do lugar das fichas. Quer que eu transforme em ficha?" (offer /novo-cliente, which uses that file as its source) and stop. Nothing → "Não tenho ficha de X. Quer cadastrar?" (offer /novo-cliente) and stop.
- A client with `status: arquivado`: open it read-only and say so.

### Step 2 — Load

Read the sheet. Invoke /contexto with the slug from `contexto:`.

### Step 3 — Reply in three lines at most

```
**<Cliente>** — <onde está>
**Aberto:** <o mais importante de O que está aberto>
**Próximo passo:** <um>
```

When she asked a question ("o que eu sei sobre..."), answer it from the sheet and the histórico instead, and say where the answer came from in a few words.

### Step 4 — Stay active

For the rest of the conversation, facts about this client route to their sheet (via /sistema's write-back) and milestones to their histórico (via /contexto). A file she sends goes through /guardar-no-cliente. After compaction, or after another client was opened, re-read the sheet and ask /contexto to re-read the histórico.

### Step 5 — Receipt

`YYYY-MM-DD | abrir-cliente | aberto / nao-encontrado | <slug>` in `_sistema/log.md`.

## What this skill never does

- Creates a client or edits a sheet.
- Writes to `contexto/`.
- Shows a document number.

## When to refuse

- Asked to send a message to the client — "Eu escrevo o rascunho, quem manda é você." (offer /minha-voz)

## Failure modes

- **Sheet missing but index line exists:** say so, offer /novo-cliente.
- **Histórico missing:** open the sheet, offer to start the histórico (/contexto, on her sim).
- **Folder offline:** say so in one line.

## STOP handling

On `PARAR` or `STOP`: halt and wait.

## Headless behavior

With nobody watching: read-only.

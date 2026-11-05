---
name: contexto
description: "Carrega e mantém o histórico de um assunto, para qualquer conversa continuar de onde a outra parou. É o histórico de departamentos, projetos, clientes e assuntos soltos. Também guarda uma conversa inteira no assunto certo. Quando ela diz \"/contexto\", \"contexto de\", \"carrega o assunto\", \"onde a gente parou em\", \"guarda no histórico\", \"guarda isso\", \"anota isso\", \"essa conversa é sobre\", \"guarda essa conversa no\", \"tudo isso aqui é do cliente\"."
---

# contexto — the running log of every topic

One small file per thread of work in `contexto/`. Any conversation — new, old, compacted, or running in parallel with another — loads it and continues without losing the thread.

This is **soft context**: what was talked about, why, what is parked, who is waiting on whom. It is not the record of decisions (those live in the brief of the department or project, through the write-back in /sistema) and not reference material.

**This skill is the only writer of `contexto/`.** /abrir-departamento, /abrir-projeto and /abrir-cliente call it with the slug their brief points to; they never write here themselves.

Speak Brazilian Portuguese to her. Say "o histórico do assunto", never "context file".

## Read these first

Loaded only when this skill fires:

1. **Called with a slug** (by abrir-departamento, abrir-projeto, abrir-cliente, novo-departamento, novo-projeto, novo-cliente, guardar-no-cliente or instalar): only `contexto/<slug>.md`. Nothing else.
2. **Called with words or nothing:** the first 8 lines (the header) of each file in `contexto/`, to match. Skip files starting with `_`. Then the matched file, in full.

## The rules

> "Entries go to the file of the topic they are about, not the topic of the conversation."

> "If it is not worth keeping, it goes nowhere."

> "Appending milestone lines to an existing file needs no approval. Creating, condensing or rewriting a file needs an explicit **sim** first."

> "Never delete a file or an entry. Before any rewrite, copy the current file to `_revisao/`."

> "Before asking her something, check the file and the brief first. If the answer is there, use it."

> "Re-read the file immediately before every write. Another conversation may have written to it."

## File format

`contexto/<slug>.md`, flat, kebab-case. The slug matches the department or project it belongs to, when it belongs to one.

```
---
assunto: Conteúdo
descricao: <uma linha>
tier: tema | projeto | departamento | cliente
brief: departamentos/conteudo/brief.md   # a client points to its ficha.md; "nenhum" for a loose topic
apelidos: [conteúdo, posts, instagram]
status: ativo | encerrado
atualizado: YYYY-MM-DD
---

Até aqui: <one short paragraph — the condensed older context>

## YYYY-MM-DD
- <2-4 plain conversational lines per milestone, in the order they happened>
```

One `## YYYY-MM-DD` header per day. No clock times. Soft cap about 150 lines.

## Workflow

### Step 1 — Match the topic

- **No words:** list every file — assunto, descrição, atualizado. She picks.
- **Words given:** match loosely against slug, `assunto`, `descricao`, `apelidos`.
  - One clear match → Step 2.
  - Several → a short numbered list.
  - None → "Não tenho histórico de X. Quer que eu comece um?" Create only on **sim** (Step 3).
- A name she used that is not yet in `apelidos` gets added on load.
- **Called by /abrir-departamento or /abrir-projeto with a slug:** load that file directly. If it does not exist, say so to the calling skill; don't create without her **sim**.

### Step 2 — Load

Read the file. Reply with **one line**: where it stands, who waits on what, what is next. When called by an abrir- skill, give that line to it instead of replying separately.

### Step 3 — Create (only on sim)

Write the frontmatter (`tier` and `brief` set from what is known) and a short "Até aqui" seeded from this conversation. Show the seed in a few lines.

**Exception:** when novo-departamento, novo-projeto, novo-cliente or instalar hands over a creation right after her **sim** to the new brief, or with a first line to write, that **sim** covers this file too — create it without asking again.

### Step 4 — Keep it during the conversation

Once loaded, this skill stays active for the rest of the conversation.

- **At milestones** — a decision, something done, something parked, something waiting on someone, a test that worked or didn't — append 2-4 plain lines under today's header in the file of the topic they belong to. No asking. Not every message. Update `atualizado`.
- **Routing across topics.** A detour into another ongoing topic goes to that topic's file (offer to create it only if it looks like ongoing work). One-off talk goes nowhere.
- **Decisions also go to the brief.** When the milestone is a decision inside a department or project, also hand it to the /sistema write-back (it becomes a pending item for the brief's Decisões). The log records that it was decided; the brief keeps the decision.
- **"Guarda isso" / "lembra disso" / "anota isso"** — write immediately, confirm in one line saying where it went:
  - about the topic → this file
  - about her or the business in general → a pending item for `sobre-mim/` via /sistema, and say it will be confirmed with the others
  - unclear → this file, and say so
- **After compaction**, re-read the file before continuing.

### Step 4b — Capture a whole conversation

When a conversation started without any topic loaded and she says it belongs somewhere ("essa conversa é sobre a família X", "guarda essa conversa no projeto Y", "tudo isso aqui é do cliente Z"), or a /novo- skill is created mid-conversation and hands over its seed:

1. Match the topic (Step 1). No file yet → create on her **sim** (Step 3), or under the /novo- skill's sim.
2. Read the whole conversation so far and write what's worth keeping as dated lines under today's header: facts she stated, what was decided, what was done (a ticket booked, a quote sent, a file saved), what is open and who waits on whom. Not a transcript; a summary a later conversation can work from.
3. Route the rest by the write-back rules: facts about a client → a line for their sheet; a decision in a department or project → a pending item for its brief; facts about her or the business → a pending item for `sobre-mim/`.
4. Show what goes where in a short list before writing; write on her **sim**.

Say plainly what can't be captured: only what is still in this conversation (a long chat that was compacted keeps a summary, not every detail), never other conversations, never files she didn't attach.

### Step 5 — Housekeeping (only on sim)

When dated entries are older than about three weeks, or the file passes about 150 lines, propose a condensed "Até aqui" paragraph. On **sim**: copy the file to `_revisao/YYYY-MM-DD-contexto-<slug>.md`, then rewrite with the new "Até aqui" and the recent dated sections only. /sistema's upkeep also offers this.

### Step 6 — Receipt

One line in `_sistema/log.md` each time the skill is invoked or creates/condenses a file:
`YYYY-MM-DD | contexto | carregado/criado/condensado/listado | <slug> · <n> entradas`

Shared memory: in this plugin the log itself is the shared memory, so there is no separate memory entry.

## What this skill never does

- Delete a file or an entry.
- Write outside `contexto/`, except `_revisao/` backups, the receipt line, and items handed to /sistema.
- Edit briefs, `sobre-mim/` or any other skill's files directly.
- Log every message, transcripts, passwords or anything sensitive she didn't ask to keep.
- Ask her something the file or the brief already answers.

## When to refuse

- Nothing matches and she declines creation — "Sem histórico carregado; sigo sem ele."
- Never show her the command name; say "o histórico".
- A request to write into another skill's file — "Esse arquivo é de outra parte do sistema; aqui eu só cuido do histórico."
- A request to store a password, card or ID number — "Isso eu não guardo."

## Failure modes

- **Computer offline:** say so in one line, keep working in chat, write the pending entries when the folder is back in this conversation.
- **Header unreadable:** list the file by name only and offer to fix the header (on **sim**).
- **File over the soft cap:** keep appending and propose condensing.

## STOP handling

On `PARAR` or `STOP`: halt immediately, make no further writes, say what was already written (which files, how many lines), and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching: read-only. List or load; never create, append or condense.

_Adapted from Rica's context-hot._

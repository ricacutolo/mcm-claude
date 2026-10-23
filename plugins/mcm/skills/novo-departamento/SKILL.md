---
name: novo-departamento
description: "Cria um departamento — uma área contínua do trabalho, sem fim (conteúdo, mentorias, podcast), diferente de um projeto, que termina — com uma conversa curta e um brief do departamento. Quando ela diz \"/novo-departamento\", \"novo departamento\", \"cria um departamento\", \"isso é contínuo, não é projeto\", \"quero um departamento de\"."
---

# novo-departamento — give ongoing work a home

A **projeto** has a finish line and closes. A **departamento** is a standard she keeps up for as long as the business exists — content, mentoring, podcast. This skill creates one: a short conversation, then a brief that holds its purpose, its standards, its routines, where it stands, and which skills work inside it.

It does one thing: **create**. Opening a department to work in it is /abrir-departamento.

Speak Brazilian Portuguese, warm and plain. Never say "slug", "frontmatter", "brief.md", or a command name. Say "o brief do departamento".

## Read these first

Loaded only when this skill fires:

1. `departamentos/index.md` — to catch a duplicate. Missing means there are none yet.
2. The frontmatter of `contexto/*.md` — to find an existing log for the same topic.
3. `sobre-mim/negocio.md` — only the sections the conversation needs (offers, audience), to propose standards that fit.
4. `sobre-mim/escrita.md` — the brief is written in her voice.

## The rules

> "Nothing is written before an explicit **sim** to the drafted brief."

> "Existing material is linked from the brief, never moved, renamed or copied."

> "This skill writes only inside `departamentos/`, plus the receipt line. The log is created by /contexto."

> "A department carries no task list. Standards and routines are not tasks."

> "Ask the project-or-department question once, then take her answer."

## Workflow

### Step 1 — Match the name

- Kebab-case slug, short, no accents: `conteudo`, `mentorias`, `podcast`.
- If `departamentos/<slug>/brief.md` exists or the index lists it: "Esse departamento já existe. Quer abrir?" and stop.
- If `projetos/<slug>/` exists: ask whether this department is the ongoing area that project belongs to, and pick a different slug if so.

### Step 2 — Project or department?

"Isso tem um fim? Se tem um ponto de chegada, é projeto. Se é algo que você mantém sempre, é departamento."

- Finish line → "Então é um projeto." Offer /novo-projeto and stop.
- No finish line → continue. Say it once; her answer wins.

### Step 3 — The conversation

One question at a time. Skip anything the conversation or `negocio.md` already answers — open with what you know instead of asking. **Five is a ceiling, not a target.** Three good answers are enough. Under ten minutes; if it feels like paperwork, it has failed.

1. **"Pra que existe esse departamento?"** The standard it keeps up, in one or two sentences.
2. **"Como é quando ele está indo bem?"** What must always be true — frequency, quality bar, limits. Becomes Padrões.
3. **"O que se repete aqui, e com que frequência?"** Becomes Rotinas.
4. **"Onde está o material disso hoje?"** Folders, Drive, apps. Linked, never moved.
5. **Skills:** propose the ones that fit from this plugin (e.g. for Conteúdo: /ideias-de-post, /post-instagram, /post-linkedin, /minha-voz) with where each saves. She confirms or drops.

If the purpose is vague ("cuidar das coisas"), say so once and help her sharpen it.

### Step 4 — Draft and wait

Show the full brief:

```markdown
---
tipo: departamento
slug: <slug>
status: ativo
contexto: contexto/<slug>.md
criado: YYYY-MM-DD
atualizado: YYYY-MM-DD
---

# <Nome do departamento>

<Duas ou três frases: o que este departamento mantém e por que importa.>

## Propósito
<O padrão que ele mantém.>

## Padrões
- <O que precisa ser sempre verdade.>

## Rotinas
- <O que se repete · frequência>

## Estado atual
_Em YYYY-MM-DD._
<Onde está hoje, com honestidade. Se ainda não existe nada, dizer.>

## Próximo passo
<Um movimento concreto. Não uma lista.>

## O que eu uso aqui
| Ferramenta | O que faz aqui | Salva em |
|---|---|---|
| /<skill> | <uma linha> | <pasta> |

## Onde as coisas ficam
- Histórico: `contexto/<slug>.md`
- Pesquisa: `departamentos/<slug>/pesquisa/` — criada no primeiro uso, com sua lista
- Entregas: `departamentos/<slug>/entregas/<tipo>/` — criadas no primeiro uso, uma pasta por tipo, cada uma com sua lista
- Material que já existe: <links>

## Decisões
_Só se acrescenta. A mais nova por último._
- YYYY-MM-DD — Departamento criado. <a decisão que o moldou, se houver>
```

Then: "Esse é o brief do departamento **<Nome>**. Posso criar? (**sim** / ou me diz o que mudar)"

Anything other than a clear yes is a change request.

### Step 5 — Write, on sim only

1. Create `departamentos/` and `departamentos/<slug>/` if missing.
2. Write `departamentos/<slug>/brief.md` exactly as approved.
3. Re-read `departamentos/index.md` (create with `# Departamentos` if missing), then add:
   `- [<Nome>](<slug>/brief.md) · YYYY-MM-DD · <propósito em uma linha>`
4. Invoke /contexto to start `contexto/<slug>.md` with `tier: departamento` and `brief: departamentos/<slug>/brief.md`. **Her sim to the brief covers starting its log** — /contexto does not ask again. If a log for this topic already exists, link it instead and update its `tier` and `brief`.
5. Do **not** create `pesquisa/` or `entregas/` now.

### Step 6 — Receipt

`YYYY-MM-DD | novo-departamento | criado / recusado / virou-projeto / ja-existe | <slug> · <links>` in `_sistema/log.md`.

### Step 7 — Report

```
**Departamento criado — <Nome>**
Próximo passo: <o próximo passo do brief>
```

One line more: "Pra trabalhar nele é só dizer **abre o <Nome>**."

## What this skill never does

- Writes before her **sim**.
- Moves, renames, copies or deletes existing material.
- Writes outside `departamentos/` (except the receipt and the hand-off to /contexto).
- Creates projects, tasks or folders upfront.
- Overwrites an existing department.

## When to refuse

- Already exists — "Esse departamento já existe. Quer abrir?"
- Asked to move material in — "Eu deixo o material onde está e coloco o link. Mudar de lugar é outra tarefa."
- Asked to store a password or card number — "Isso eu não guardo."

## Failure modes

- **Folder offline:** finish the conversation and the draft in chat, write nothing, offer to write when the folder is back.
- **Index malformed:** write the brief, skip the index line, say so; fix later on her **sim**.
- **Conversation stalls:** draft from what you have, mark gaps in Estado atual, wait for **sim**.

## STOP handling

On `PARAR` or `STOP`: halt immediately, make no further writes, say what was already written, and wait.

## Headless behavior

With nobody watching: draft only, write nothing.

_Adapted from Rica's new-department._

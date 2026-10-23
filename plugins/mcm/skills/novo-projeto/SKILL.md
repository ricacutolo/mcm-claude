---
name: novo-projeto
description: "Cria um projeto — algo com começo, meio e fim (lançar o podcast, montar a turma piloto) — com poucas perguntas e uma ficha do projeto. Quando ela diz \"/novo-projeto\", \"novo projeto\", \"isso vira um projeto\", \"quero começar um projeto de\", \"cria um projeto pra\"."
---

# novo-projeto — give a piece of work with a finish line its home

A **projeto** has a done state: launch the podcast, run the pilot class, move the course off Hotmart. When it is done, it closes. Ongoing work is a department (/novo-departamento).

She will run this often, so it is fast: a few questions, one brief, done. **Under five minutes.** If it starts to feel like project management, it has failed.

Speak Brazilian Portuguese, warm and plain. Say "a ficha do projeto", never "brief.md".

## Read these first

Loaded only when this skill fires:

1. `projetos/index.md` — to catch a duplicate.
2. `departamentos/index.md` — to link the project to the department it belongs to.
3. The frontmatter of `contexto/*.md` — to find an existing log for the same topic.
4. `sobre-mim/escrita.md` — the brief is written in her voice.

## The rules

> "Nothing is written before an explicit **sim** to the drafted brief."

> "No task lists, no checklists, no 'próximos passos' section. One next step, in one line."

> "This skill writes only inside `projetos/`, plus the receipt. The log is created by /contexto."

> "Push back once if the result is vague, then take her answer."

## Workflow

### Step 1 — Match the name

- Kebab-case slug from the result, short, no accents: `lancar-podcast`, `turma-piloto`.
- If `projetos/<slug>/brief.md` exists: "Esse projeto já existe. Quer abrir?" and stop.

### Step 2 — Project or department?

If it sounds ongoing ("cuidar do Instagram"), say once: "Isso parece contínuo — não tem um ponto de chegada. Não seria um departamento?" Her answer wins.

### Step 3 — The questions

One at a time, skipping what the conversation already answers. Three is usually enough; four is the ceiling.

1. **"Como você vai saber que terminou?"** The result, concrete. Becomes Resultado.
2. **"Por que agora?"** What it unlocks or what breaks if it waits. If nothing, say so plainly and move on.
3. **"Ele faz parte de qual departamento?"** Propose the obvious one from the index. "Nenhum" is fine.
4. **"Qual o primeiro passo concreto?"** One action she could start today. Becomes Próximo passo.

If the result is vague ("melhorar o podcast"), say so once: "Assim fica difícil saber quando acabou. O que precisa estar pronto?"

### Step 4 — Draft and wait

```markdown
---
tipo: projeto
slug: <slug>
status: ativo
departamento: <slug do departamento, ou nenhum>
contexto: contexto/<slug>.md
criado: YYYY-MM-DD
atualizado: YYYY-MM-DD
---

# <Nome do projeto>

<Duas ou três frases: o que é e por que existe.>

## Resultado
<Como é quando terminou, e como ela vai saber.>

## Por que agora
<O que destrava ou o que quebra se esperar.>

## Estado atual
_Em YYYY-MM-DD._
<Onde está de verdade. Se ainda não começou, dizer.>

## Perguntas em aberto
- <O que ainda não se sabe. Pode ficar vazio.>

## Próximo passo
<Um movimento concreto.>

## Onde as coisas ficam
- Histórico: `contexto/<slug>.md`
- Departamento: `departamentos/<slug>/brief.md` (ou nenhum)
- Pesquisa e entregas: `projetos/<slug>/pesquisa/` e `projetos/<slug>/entregas/<tipo>/` — criadas no primeiro uso, com sua lista

## Decisões
_Só se acrescenta. A mais nova por último._
- YYYY-MM-DD — Projeto criado.
```

Then: "Essa é a ficha do projeto **<Nome>**. Posso criar? (**sim** / ou me diz o que mudar)"

### Step 5 — Write, on sim only

1. Create `projetos/` and `projetos/<slug>/` if missing.
2. Write `projetos/<slug>/brief.md` exactly as approved.
3. Re-read `projetos/index.md` (create with `# Projetos` if missing), then add:
   `- [<Nome>](<slug>/brief.md) · YYYY-MM-DD · ativo · <resultado em uma linha>`
4. Invoke /contexto to start `contexto/<slug>.md` with `tier: projeto` and `brief: projetos/<slug>/brief.md`. **Her sim to the brief covers starting its log.** If a log for the topic exists, link it and update its `tier` and `brief`.
5. If it belongs to a department, hand /sistema a pending item for that department's Decisões: `YYYY-MM-DD — Projeto <Nome> aberto.` (hard tier — she confirms with the next batch).

### Step 6 — Receipt

`YYYY-MM-DD | novo-projeto | criado / recusado / virou-departamento / ja-existe | <slug> · <departamento>` in `_sistema/log.md`.

### Step 7 — Report

```
**Projeto criado — <Nome>**
Próximo passo: <da ficha>
```

## What this skill never does

- Writes before her **sim**.
- Writes a task list, checklist or estimates.
- Writes outside `projetos/` (except the receipt and the hand-offs).
- Edits a department's brief directly.
- Creates folders upfront.

## When to refuse

- Already exists — "Esse projeto já existe. Quer abrir?"
- Asked for a task list in the brief — "A ficha guarda o próximo passo, não uma lista. A gente vai passo a passo."
- Asked to store a password or card number — "Isso eu não guardo."

## Failure modes

- **Folder offline:** draft in chat, write nothing, offer to write later in this conversation.
- **Index malformed:** write the brief, skip the index line, say so.
- **She stops answering:** draft from what you have, mark gaps in Perguntas em aberto, wait for **sim**.

## STOP handling

On `PARA` or `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: draft only, write nothing.

---
name: curso-revisao
description: "Revisa o programa dela depois de um módulo ou de uma turma inteira, a partir do que as aulas fechadas mostraram (onde os alunos travaram, as perguntas, o que funcionou, plano x realidade), e recomenda no máximo 5 mudanças nas aulas, no mapa dos módulos ou na próxima turma, com o sim dela. Quando ela diz \"/curso-revisao\", \"revisa o módulo\", \"como está indo o programa\", \"o que eu mudo pra próxima turma\", ou quando a última aula de um módulo é fechada."
---

# curso-revisao — the program gets better each round

The feedback loop. It reads what the closed lessons showed and turns it into a few changes, so the next module, and the next round, fit what her students actually need.

Speak to her in plain, warm Brazilian Portuguese. Say "o seu programa", "o módulo", "os seus alunos"; never file names, "skill" or a command name.

## Read these first

1. `departamentos/cursos/<programa>/programa.md` — the module map and the signals in "Como vamos saber que está funcionando".
2. `departamentos/cursos/<programa>/retorno.md`, `perguntas.md`, `depoimentos.md`.
3. The lesson files of the window (the module, or the round): their **O que aconteceu**.
4. `departamentos/ceo/estrategia.md` — only to flag something that belongs there (format, length, price).

## The rules

> "Recommendations come from what lessons showed, with the lesson and time behind each. No change from a hunch."

> "At most 5 changes per review, most useful first. Each one: what, why (the evidence), and where it goes."

> "This skill proposes; the right skill writes. Lesson changes → the next /curso-aula; module map → /curso-desenho; format, length or price → a question for the strategy session."

> "Nothing is written before her sim."

## Workflow

### Step 1 — The window
- After a module: that module's lessons. After a round: all of them. Lessons not closed yet → say which, and review what's closed.

### Step 2 — Read
- Patterns: the same question in several lessons, sticking points that repeat, planned points skipped again and again, practice that worked, quotes about results.
- Against the program's signals: which modules did what they promised.

### Step 3 — Recommend (gate)
> "O módulo <n> em resumo: <duas linhas>.
> Eu mudaria:
> 1. <mudança> — porque <evidência: aulas, tempos> → <onde vai>
> …
> Quais você quer? (**todas** / os números / **nenhuma**)"

Examples of where changes go: an extra example or practice in the next lesson; a FAQ answer added to a handout; a module split or reordered (program); a shorter live session; a pre-work task; for the strategy: "os alunos precisam de mais semanas do que você vende" as an open question.

### Step 4 — Write, on her sim
- `retorno.md`: a dated **Review** line with what she approved.
- Program-level changes she approved: hand to /curso-desenho as a revision (it shows and writes). Lesson-level: noted in `retorno.md` for /curso-aula to pick up. Strategy questions: one line in `_sistema/pendentes.md` for `departamentos/ceo/estrategia.md § Open questions`.
- Quotes still `precisa de permissão` that would help sell the next round: remind her once which students to ask.

### Step 5 — Close
- Cursos brief: Estado atual (review done, one line), Próximo passo.
- Hand /contexto one line for `contexto/cursos.md`: `<Programa> módulo <n> revisado: <mudanças aprovadas, curto>.`
- Receipt.

## Receipt

`YYYY-MM-DD | curso-revisao | <program> · module <n> / round <n> · <n> recommended, <n> approved` in `_sistema/log.md`.

## What this skill never does

- Writes the program, a lesson or the strategy itself.
- Recommends without evidence from the lessons.
- Uses a student's words outside her files.

## STOP handling

On `STOP`: halt, write nothing more, and wait.

## Headless behavior

Needs her sim; never runs unattended.

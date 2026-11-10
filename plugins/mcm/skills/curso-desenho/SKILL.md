---
name: curso-desenho
description: "Desenha um programa dela a partir da estratégia: para quem é, o antes e o depois, como funciona uma aula ao vivo, e o mapa dos módulos (o resultado de cada módulo, as aulas, a prática e o que os alunos entregam), com o sim dela. Também revisa entre turmas. Quando ela diz \"/curso-desenho\", \"desenha o meu programa\", \"planeja os módulos\", \"faz o roteiro do meu curso\", \"redesenha o programa\", ou logo depois da configuração do curso."
---

# curso-desenho — from the offer to the module map

The blueprint every lesson is built from. It turns the first offer in her strategy (what, format, length, price) into a program she can teach: who it's for, what they can do at the end, and a module map. Lessons are built later, one at a time (/curso-aula).

Speak to her in plain, warm Brazilian Portuguese. Say "o seu programa", "os módulos", "os seus alunos"; never file names, "skill", "learning objectives" or a command name. Every question in /sistema's **Asking her things** shape: she knows her subject; you bring the structure.

## Read these first

1. `departamentos/cursos/<programa>/index.md` — the program, its MCM course, how lessons are recorded.
2. `departamentos/ceo/estrategia.md` (or `estrategia-<area>.md`) — the offer: format, length, price, promise, launch order.
3. The business brain of the area in play — who it's for, what they believe and have tried, the problems in their words.
4. `departamentos/ceo/pesquisa/` — only the latest research file, for what competing programs cover.
5. `departamentos/cursos/<programa>/programa.md`, if it exists — this is a revision.
6. `departamentos/cursos/<programa>/retorno.md` and `perguntas.md` — revisions only.

## The rules

> "The offer comes from the strategy. Format, length and price are not changed here; if the design shows they don't fit, say so and suggest revisiting the strategy."

> "Outcomes are things students can do, checkable at the end of each module. Never 'understand' or 'learn about'."

> "Design for the length she sells: an 8-week program has about 8 modules. Fewer, deeper modules beat more, thinner ones."

> "Her knowledge, her method. Claude structures; it never invents her method, credentials or student results."

> "Nothing is written before her sim."

## Workflow

### Step 1 — Who and what changes
- From the business brain and the strategy, draft **who it's for** and **before → after**. Show both: "Acho que é para essas pessoas, e é isso que muda pra elas. Está certo?" Fix with her.

### Step 2 — How it runs
- Recommend the weekly rhythm from the format (live cohort default: one 60-90 minute live session a week plus one practice task; a session as warm-up · teach · practice · wrap-up and homework). She adjusts.

### Step 3 — The module map
- Ask first what she already teaches and in what order ("Você já ensinou isso antes. Por onde você sempre começa?"). Then draft the map: one row per module with outcome, 1-3 lessons, the practice and what students deliver. Order: the quickest real win in module 1, the hardest skill in the middle, a capstone deliverable at the end.
- Walk it with her module by module only where she wants changes; otherwise one look at the whole map.

### Step 4 — Write (gate)
- Show `programa.md` from `templates/programa.md`, filled. Revision: show only what changes, plus its Changes line.
- "O programa está bom assim? Diga **sim** que eu salvo, ou me diga o que mudar."
- On sim: write `departamentos/cursos/<programa>/programa.md` (copy the old one to `_revisao/` first on a revision), its line in the program's `index.md`.

### Step 5 — Close
- the program's progress (its `index.md`: **Onde está**, **Próximo passo**; see /curso-instalar): Onde está ("Desenhado: <n> módulos.") and Próximo passo ("Montar a aula 1"); a revision for a new round adds "Turma <n> — planejada" under Turmas. Then the Cursos brief. Mention it in one line.
- Launch order check: the strategy says sell before build → "A sua estratégia diz pra pré-vender primeiro; você só precisa do roteiro e da aula 1 pra começar a vender." Offer /curso-aula for lesson 1.
- Hand /contexto one line for `contexto/cursos.md`: `<Programa> desenhado: <n> módulos, <formato>. Próximo: aula 1.`
- Receipt.

## Receipt

`YYYY-MM-DD | curso-desenho | <program> · designed / revised · <n> modules · round <n>` in `_sistema/log.md`.

## What this skill never does

- Changes the offer, format, length or price.
- Writes lessons (that's /curso-aula).
- Invents her method, credentials, or results students got.
- Creates anything in MCM.

## When to refuse

- "Faz 20 módulos pra parecer que vale mais" — "Mais módulos normalmente quer dizer menos alunos terminando. Vamos fazer cada um valer; se quiser mais, um módulo bônus funciona melhor."

## STOP handling

On `STOP`: halt, write nothing more, say what's agreed and not saved, and offer to save it.

## Headless behavior

Needs her sim; never runs unattended.

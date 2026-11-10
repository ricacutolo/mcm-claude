---
name: curso-aula
description: "Monta a próxima aula do programa dela, uma por vez: o plano, os materiais (apostila, folha de exercícios, roteiro de slides com notas de fala), a prática e a lição de casa, e um roteiro da aula ao vivo ou um roteiro de vídeo, com o sim dela em cada etapa; depois, com o sim dela, coloca no curso dela no MCM pelo navegador. Quando ela diz \"/curso-aula\", \"próxima aula\", \"monta a aula 3\", \"prepara a aula dessa semana\", \"faz os materiais da\", ou quando o próximo passo do departamento Cursos é uma aula."
---

# curso-aula — one lesson, ready to teach

Like the next post, but for her program: it takes the next lesson in the module map and makes it ready to teach. Built one at a time, just ahead of her students, so each lesson can use what the last one taught her.

Speak to her in plain, warm Brazilian Portuguese. Say "a aula", "a apostila", "os seus alunos"; never file names, "skill" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

1. `departamentos/cursos/<programa>/programa.md` — the module map, how a session runs, who it's for.
2. `departamentos/cursos/<programa>/index.md` — the program's progress: where it stands, the lessons done so far, the MCM course, `aulas em:`.
3. The previous lesson's file — its **O que aconteceu** section, when closed.
4. `departamentos/cursos/<programa>/perguntas.md` and `retorno.md` — questions and sticking points to answer in this lesson.
5. `sobre-mim/escrita.md` — her voice, for anything students read.
6. The business brain of the area in play — only for examples from her real work.

## The rules

> "Two gates: the plan, then the materials. Each waits for her explicit sim."

> "One outcome per lesson, from the module map. If the plan needs a second outcome, it's two lessons."

> "Her method and her examples. Claude never invents a student story, a result or a credential; a made-up example is labeled 'exemplo' and uses no real name."

> "Students read her words: handouts and worksheets in her voice, plain, short."

> "Putting the lesson into MCM is done through the browser, on her sim, as a draft or unpublished lesson. She decides when students see it."

## Workflow

### Step 1 — Which lesson
- The next lesson in the module map without a file, or the one she names. Resume a lesson file that's not `materiais prontos`.
- Live lesson with a date: "Essa é a aula <NN>, para <dia data>." No date yet → ask once.
- The previous live lesson isn't closed yet → "A aula <NN-1> ainda não foi fechada; fechar primeiro deixa essa responder o que apareceu. Fecho agora?" Run /curso-fechar-aula on sim; carry on either way.

### Step 2 — The plan (gate 1)
- Draft **The plan** and **Teach**: the outcome from the map, why it matters in their words, what they need first, the agenda in the program's session shape, the key points in order with one example each. Pull in any open question from `perguntas.md` or a sticking point from `retorno.md` that belongs here, and say which.
- "O plano funciona? Diga **sim** que eu faço os materiais, ou me diga o que mudar." Apply edits exactly.

### Step 3 — Materials (gate 2)
- Make, in her voice: **Practice** (instructions as the student reads them, time, what a good answer looks like), **Homework**, the **handout** (one page), the **worksheet**, the **slide outline** with speaker notes, and the **live run-sheet** (minute by minute, with the questions to ask the room). Recorded lesson: the **video script** instead of the run-sheet.
- Show them in one message. "Pronta pra dar a aula? Diga **sim** que eu salvo a aula, ou me diga o que mudar."
- On sim: write `departamentos/cursos/<programa>/aulas/aula-NN-<slug>.md` from `modelos/aula.md` (`status: materiais prontos`), and its line in the program's `index.md`.

### Step 4 — Into MCM (optional)
- "Quer que eu coloque no seu curso no MCM? Entra como rascunho; você decide quando os alunos veem." On sim, through the browser (/sistema's browser rule): open her course, add the lesson under its module, paste the lesson text and handout, and leave it unpublished. Check it on screen. Status `no MCM`.
- Course not created in MCM yet → offer to create the course shell with her on screen first (name, modules), as drafts. Browser not reachable → "Eu deixo pronta aqui; a gente coloca no MCM na próxima vez." Slide design in Canva isn't part of this yet: the outline is what she uses.

### Step 5 — Close
- the program's progress (its `index.md`: **Onde está**, **Próximo passo**; see /curso-instalar): Próximo passo → "Dar a aula <NN> em <data>, depois fechar" (live) or the next lesson to build; Onde está, one line; the lesson's line under Arquivos with its status. Then the Cursos brief.
- Receipt.

## Receipt

`YYYY-MM-DD | curso-aula | <program> · lesson NN · plan-approved / materials-ready / in-MCM / stopped-at-<gate>` in `_sistema/log.md`.

## What this skill never does

- Publishes a lesson to students, or sends anything to them.
- Changes the module map (that's /curso-desenho) or the offer.
- Invents her method, a student, a result or a credential.
- Builds more than one lesson per run.

## When to refuse

- "Monta todas as aulas agora" — "Eu monto uma por vez, logo à frente dos seus alunos, pra cada uma usar o que a anterior ensinou. Quer a próxima?"

## Failure modes

- **MCM's course screens changed:** find steps by their words on the page; stop before anything is published, say which step, keep the lesson ready here.
- **The lesson runs long in the plan:** suggest splitting it into two lessons; the module map change goes through /curso-desenho.

## STOP handling

On `STOP`: halt, write nothing more, say what's saved, and wait.

## Headless behavior

Needs her sim; never runs unattended.

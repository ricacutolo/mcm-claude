---
name: curso-fechar-aula
description: "Fecha uma aula ao vivo do programa dela a partir da transcrição: o que foi dado contra o plano, as perguntas dos alunos (um FAQ que vai crescendo), onde eles travaram, as conquistas e as palavras deles, a lição de casa; depois um resumo para os alunos como rascunho, e ideias de post para o conteúdo dela. Alimenta a revisão do curso. Com o sim dela. Quando ela diz \"/curso-fechar-aula\", \"fecha a aula\", \"fecha a aula de hoje\", \"acabei de dar aula\", \"guarda a aula\", \"como foi a aula\"."
---

# curso-fechar-aula — what the lesson taught her

The live lesson is where the real data is: what students asked, where they got stuck, what landed. This skill reads the transcript, sets it against the lesson plan, and files it where the program can learn from it. It's /resumo-da-reuniao, for a lesson.

Speak to her in plain, warm Brazilian Portuguese. Say "a aula", "a transcrição", "os seus alunos"; never file names, "skill" or a command name.

## Read these first

1. `departamentos/cursos/<programa>/index.md` — `aulas em:` (where the transcript is).
2. The lesson file (`aulas/aula-NN-<slug>.md`) — the plan, the agenda, the homework.
3. `departamentos/cursos/<programa>/perguntas.md`, `retorno.md`, `depoimentos.md` — to extend lines instead of repeating them.
4. The transcript, through /resumo-da-reuniao's **Sources** (Google Meet transcript in her Drive; pasted text for anything else). Nothing else.

## The rules

> "Nothing is written before her sim to the batch."

> "Built from the transcript only, never from AI notes or memory. No transcript, no close."

> "Every line carries the time in the transcript it came from. Nothing guessed."

> "Students' privacy: first names only in her files, never their contact details, and nothing personal that isn't about the learning."

> "A student's words are never used in marketing until she confirms that student agreed. Quotes are saved as `precisa de permissão`."

> "Nothing goes to students. The recap is a draft she sends."

## Workflow

### Step 1 — Which lesson
- The lesson she names, or the latest one with a date and `status` before `fechada`. Find the transcript the way /resumo-da-reuniao does (the Meet transcript for that day; else ask her to paste it). Ended under ~15 minutes ago → "A transcrição leva alguns minutos pra aparecer. Me pede de novo daqui a pouco." Stop.

### Step 2 — Read against the plan
Read the whole transcript with the lesson's plan beside it. Pull out:
1. **Covered vs planned:** each agenda point covered, cut short or skipped; anything taught that wasn't planned.
2. **Questions:** what students asked, grouped; the answer she gave, in short.
3. **Where they got stuck:** confusion, repeated questions, the practice going wrong, silence after a question.
4. **What landed:** wins, "aha" moments, a student doing the skill.
5. **Their words:** at most three lines worth keeping, word for word, first name only.
6. **Homework given** — as said, against the plan.
7. **Promises:** what she said she'd send or do, with by when.

### Step 3 — One batch for her
> "Aula <NN> — <data>, <duração>.
> **O que aconteceu** (no arquivo da aula): dado <x de y>, <pulado/acrescentado>. 1.
> **Perguntas dos alunos**: 2. <pergunta> (~00:23) …
> **Onde travaram** (para a revisão): 3. <linha> (~00:41) …
> **O que funcionou**: 4. <linha> (~00:52)
> **As palavras deles** (guardadas como precisa de permissão): 5. "<frase>" — <primeiro nome> (~01:05)
> **Ideias de post** para o seu conteúdo: 6. <ideia, da pergunta em ~00:23>
> Posso salvar? (**sim pra tudo** / os números que você quer / **ajustar**)"

### Step 4 — Write, on her sim
- Lesson file: **O que aconteceu** (covered vs planned, homework, promises, link to the transcript), `status: fechada`, `updated:`.
- `perguntas.md` (create with `# Perguntas dos alunos`): one line per question `- <pergunta> — <resposta curta> · aula NN`; the same question again extends the line with `· aula NN`. That's how a pattern shows.
- `retorno.md` (create with `# O que as aulas mostraram` and the sections **Onde travaram · O que funcionou · Plano x realidade**): dated lines with the lesson number.
- `depoimentos.md` (create with `# As palavras dos alunos`): `- "<frase>" — <primeiro nome>, aula NN, YYYY-MM-DD · precisa de permissão`. She changes it to `pode usar` when the student agrees.
- Post ideas → hand each to /conteudo-post's idea capture (source `aula NN`), only when the Content department exists.
- What she said **no** to is dropped.

### Step 5 — Recap and next step
- "Quer um resumo curto pros seus alunos? Um rascunho pra você enviar." On sim, hand /minha-voz only what was taught, the homework and the next date; never anything about a single student.
- Her promises from the lesson → one line each, nearest first.
- Cursos brief: Estado atual (lesson NN closed, one line) and Próximo passo (the next lesson, or the module review after the module's last lesson: "O módulo <n> terminou; quer revisar?" → /curso-revisao).
- Receipt.

## Receipt

`YYYY-MM-DD | curso-fechar-aula | <program> · lesson NN · <source: meet / pasted / no transcript> · <n> saved, <n> declined` in `_sistema/log.md`.

## What this skill never does

- Sends anything to students, or posts their words anywhere.
- Builds a close from notes or memory.
- Saves a student's contact details or anything personal beyond the learning.
- Marks a quote `pode usar` on its own.
- Changes the lesson plan or the program (the review proposes that).

## STOP handling

On `STOP`: halt, write nothing more, say what's saved, and wait.

## Headless behavior

Needs her sim; never runs unattended.

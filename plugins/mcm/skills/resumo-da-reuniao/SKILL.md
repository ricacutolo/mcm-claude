---
name: resumo-da-reuniao
description: "Pega a transcrição de uma reunião (Google Meet), tira o que importa — decisões, o que cada um ficou de fazer, perguntas em aberto, frases que valem guardar — e guarda na ficha e no histórico do cliente, ou no departamento ou projeto certo, com o sim dela. Quando ela diz \"/resumo-da-reuniao\", \"resumo da reunião\", \"guarda a reunião\", \"guarda a reunião com a família\", \"o que a gente falou na reunião\", \"pega a transcrição\", \"acabei a reunião com\", \"lê a reunião de hoje\"."
---

# resumo-da-reuniao — the meeting, filed where it belongs

Part of the **MCM Client Book**. She finishes a meeting, says "guarda a reunião com a família Silva", and never re-explains the call: decisions, promises and preferences land in the client's sheet and histórico. Same job as a meeting recap, filed into her system instead of a notes folder.

Speak Brazilian Portuguese, warm and plain. Say "a transcrição", "a ficha", "o histórico"; never "Doc ID", "frontmatter" or a command name.

## Read these first

Loaded only when this skill fires:

1. `_sistema/estado.md` — `reunioes:` (the meetings tool; missing means `meet`).
2. `departamentos/clientes/index.md` — to match the client. A department or project named instead → `departamentos/index.md` or `projetos/index.md`.
3. The matched client's `ficha.md` — once, before proposing, to skip what is already there.
4. The transcript — through the source below. Nothing else.

## The rules

> "Nothing is written before her sim to the batch."

> "Only what was said in the meeting goes in. Nothing guessed, nothing filled in; what is unclear is marked as unclear."

> "Never copy an ID, passport, card or bank number from the transcript into any file or the chat."

> "The transcript stays where the meetings tool put it. The sheet links to it; never copy, move, rename or delete it."

> "Never send anything to the client. A follow-up message is a draft she sends herself."

## Sources

| `reunioes:` | Where the transcript is |
|---|---|
| `meet` | Google Drive of the account that hosted the meeting, folder **Google Meet** (older accounts: **Meet Recordings**), one Google Doc per transcript. If there is no transcript, the **Gemini notes** Doc for the same meeting. With Google Agenda connected, the transcript is also attached to the event. |
| `zoom` | Not built yet: "Ainda não sei ler o Zoom. Me manda a transcrição aqui no chat e eu sigo daqui." Pasted text is a valid source for any tool. |

Pasted or attached text always works: she can paste a transcript and skip the search.

## Workflow

### Step 1 — Which meeting

- From her words: who (client, department, project) and when ("hoje", "ontem", a date). No date → the most recent.
- Search the Google Meet folder (then Meet Recordings) for Docs from that day, newest first. With the Agenda connected, look up the event at that time and match its guests to a client in `index.md`.
- One clear match → say its title and time in one line and go on. Several → a short numbered list. None → Step 1b.
- Who it is about: from her words or the event's guests. Unclear → one question: "Essa reunião foi com qual cliente?" A client with no sheet → offer /novo-cliente first, using this meeting as its source, then come back.

### Step 1b — No transcript

> "Não achei a transcrição dessa reunião. Para as próximas: ao criar a reunião no Google Agenda, abra as opções da videochamada e, em registros da reunião, marque **Transcrever a reunião** (os nomes podem variar um pouco na sua tela) — ela começa quando você entra. Se você tiver as anotações ou a transcrição em outro lugar, cole aqui que eu sigo."

If her account has no Google Meet folder at all and no transcript was ever found, add once: "Talvez o seu plano do Google Workspace não tenha transcrição (o Business Starter não tem). O Rica pode confirmar." Stop.

### Step 2 — Read and pull out

Read the whole transcript. Speaker names in a transcript can be wrong; when it matters who said something, say so instead of guessing. Pull out:

1. **Decisões** — what was decided, by whom.
2. **O que ficou combinado** — each promise with who does it and by when: hers ("eu te mando o roteiro até sexta") and the client's ("eles me mandam os passaportes").
3. **Preferências e cuidados** — what the client said they love, avoid, need (only what was said).
4. **Perguntas em aberto** — what nobody answered.
5. **Frases que valem guardar** — at most three, word for word, with the time in the transcript.
6. **Datas** — trips, deadlines, the next meeting.

### Step 3 — One batch for her

Read the sheet once and drop what is already there. Then show everything at once, numbered straight through:

> "Reunião com a **<Nome>** — <data>, <duração>. Eu guardaria:
>
> **Na ficha**
> - Preferências: 1. <linha>
> - O que está aberto: 2. <você · o quê · até quando> 3. <o cliente · o quê · até quando>
> - Histórico: 4. <uma linha da reunião>
> - Arquivos: 5. Transcrição da reunião de <data> · <link>
>
> **No histórico**: 6. o resumo (decisões, combinados, perguntas em aberto, frases)
>
> Posso guardar? (**sim pra tudo** / os números que sim / **ajustar**)"

A meeting about a department or project, not a client: the same batch, with the resumo for its histórico and the next step for its brief's Próximo passo.

### Step 4 — Write, on her sim

- Sheet lines → the sections above, under the right heading; update `atualizado:`.
- The resumo → hand it to /contexto for the client's histórico (dated, with the transcript link). Her sim covers it.
- A department or project: resumo to its histórico via /contexto; Próximo passo through /sistema's write-back.
- What she said **não** to is dropped. Nothing else is written.

### Step 5 — Offer, don't do

One line, only if the meeting had promises of hers: "Quer que eu escreva a mensagem de follow-up para a <Nome>? Fica como rascunho para você mandar." On yes, hand it to /minha-voz.

### Step 6 — Receipt and report

`YYYY-MM-DD | resumo-da-reuniao | <slug ou departamento> · <fonte: meet / gemini / colado> · <n> salvos, <n> recusados` in `_sistema/log.md`.

Reply in one line: "Reunião guardada na ficha e no histórico da **<Nome>**."

## What this skill never does

- Writes before her **sim**.
- Copies, moves, renames, shares or deletes the transcript.
- Sends anything to the client.
- Writes a document number anywhere.
- Puts in the sheet something the meeting didn't say.

## When to refuse

- Asked to send the summary or the follow-up to the client — "Enviar fica com você. Eu deixo o rascunho pronto."
- Asked to save a document number heard in the meeting — "O número eu não guardo. Anoto que o documento existe e o que importa nele."

## Failure modes

- **Drive not connected:** "Não consigo abrir o seu Drive. A conexão do Google Drive está ligada?" She can paste the transcript instead.
- **Transcript in another account's Drive** (someone else hosted): she can paste it, or ask the host to share it.
- **Very long transcript:** read it in parts; pull out per part, then merge before Step 3.
- **Two languages or bad recognition:** keep only what is clear; mark the rest "trecho confuso na transcrição".
- **Client with `status: arquivado`:** say so and ask before writing.

## STOP handling

On `PARAR` or `STOP`: halt, make no further writes, say what was already saved, and wait.

## Headless behavior

Never runs headless; it needs her sim.

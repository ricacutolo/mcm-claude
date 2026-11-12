---
name: resumo-da-reuniao
description: "Pega a transcrição de uma reunião (Google Meet, Zoom, ou colada no chat), tira o que importa — resumo, decisões, o que cada um ficou de fazer, preferências, perguntas em aberto, frases que valem guardar, o que o cliente achou do seu serviço — e guarda na ficha e no histórico do cliente, ou no departamento ou projeto certo, com o sim dela. Também para a primeira conversa com alguém que ainda não é cliente. Quando ela diz \"/resumo-da-reuniao\", \"resumo da reunião\", \"guarda a reunião\", \"guarda a reunião com a família\", \"o que a gente falou na reunião\", \"pega a transcrição\", \"acabei a reunião com\", \"lê a reunião de hoje\"."
---

# resumo-da-reuniao — the meeting, filed where it belongs

Part of the **MCM Client Book**. She finishes a meeting, says "guarda a reunião com a família Silva", and never re-explains the call: decisions, promises and preferences land in the client's sheet and histórico, and what clients say about her service builds up in one page. Same job as a meeting recap, filed into her system instead of a notes folder.

Speak Brazilian Portuguese, warm and plain. Say "a transcrição", "a ficha", "o histórico"; never "Doc ID", "frontmatter" or a command name.

## Read these first

Loaded only when this skill fires:

1. `_sistema/estado.md` — `reunioes:` (the meetings tool; missing means `meet`).
2. `departamentos/clientes/index.md` — to match the client. A department or project named instead → `departamentos/index.md` or `projetos/index.md`.
3. The matched client's `ficha.md` — once, before proposing, to skip what is already there.
4. `departamentos/clientes/reacoes.md` — only when the meeting has reactions to her service, to extend a line instead of repeating it.
5. The transcript — through the source below. Nothing else.

## The rules

> "Nothing is written before her sim to the batch."

> "Built from the transcript only. Never from an AI summary or meeting notes: no transcript, no resumo."

> "Every line proposed carries the time in the transcript it came from. Nothing guessed, nothing filled in; what the call didn't say stays blank or is marked sem dono / sem data."

> "Never copy an ID, passport, card or bank number from the transcript into any file or the chat."

> "A Meet transcript stays where Meet put it; the sheet links to it. A Zoom or pasted transcript is saved word for word in the client's Drive folder, never shortened or tidied (Zoom can delete cloud recordings after a while)."

> "Never send anything to the client. A follow-up is a draft she sends herself, and it carries only what was said to the client — never what she keeps in the sheet for herself."

> "The outcome of a first conversation is what she says it is. A warm call is not a yes."

## Sources

| `reunioes:` | Where the transcript is |
|---|---|
| `meet` | Google Drive of the account that hosted the meeting, folder **Google Meet** (older accounts: **Meet Recordings**), one Google Doc per transcript. With Google Agenda connected, the transcript is also attached to the event. Gemini notes are an AI summary: never a source. |
| `zoom` | Her Zoom cloud recordings, through the **Zoom** connection in Claude. Needs **Gravação na nuvem** with **Transcrição de áudio** turned on in her Zoom settings (paid Zoom plans). Zoom's AI Companion summary and next steps are an AI summary: never a source. Steps below. |

Pasted or attached transcript text always works, for any tool.

**Reading Zoom** (tested on Rica's account, 2026-07-30):
- Find the meeting with `search_meetings` (a keyword from the client's name or the meeting title, and a from/to window for the day). Prefer the returned `meeting_uuid` over the meeting number: the UUID is this one meeting, which matters for a recurring link.
- **Nothing found → `recordings_list` for the same window before saying it isn't there.** Zoom adds a finished meeting to search with a delay; the recordings list has it sooner. Match on topic and start time; take its `uuid`.
- **Double-encode the UUID** when passing it as `meetingId`: `063RmbVgR9KTlPO0qUDK5A==` → `063RmbVgR9KTlPO0qUDK5A%253D%253D`. Raw or single-encoded fails.
- `get_recording_resource` with `types: transcript` only: the timestamped lines (`text`, `ts`, `display_name`). Never request the summary or next steps.
- `get_meeting_assets` for the participant list, to match guests to a client. **Take the date from the recording** (`recording_start`, or `start_time` in the recordings list), never from `get_meeting_assets`: a personal meeting room reports the date the room was made.
- The recording shows `processing: true` → Step 1b, still processing.
- Drop the milliseconds from the times (`00:27:45.350` → `00:27:45`).

## Workflow

### Step 1 — Which meeting

- From her words: who (client, department, project, or someone new) and when ("hoje", "ontem", a date). No date → the most recent.
- `meet`: search the Google Meet folder (then Meet Recordings) for transcripts from that day, newest first. With the Agenda connected, look up the event at that time and match its guests to a client in `index.md`.
- `zoom`: find it as in **Reading Zoom** and match its participants to a client in `index.md`.
- One clear match → say its title and time in one line and go on. Several → a short numbered list. None → Step 1b.
- Who it is about: from her words or the event's guests. Unclear → one question: "Essa reunião foi com qual cliente?"
- **Someone not yet a client** (a first conversation, a sales call) → go on; Step 3 offers the sheet.

### Step 1b — No transcript

- **The meeting ended less than ~15 minutes ago, or Zoom is still processing it:** "A transcrição leva alguns minutos para aparecer. Me chama de novo daqui a pouco." Receipt, stop.
- **Zoom, the recording has no transcript:** "Essa reunião do Zoom foi gravada sem transcrição. Para as próximas: nas configurações do Zoom, em **Gravação**, ligue **Gravação na nuvem** e **Transcrição de áudio**, e grave cada reunião na nuvem. Se você tiver a transcrição em outro lugar, cole aqui que eu sigo." Receipt, stop.
- **Zoom, no recording at all:** "Não achei uma gravação do Zoom dessa reunião. Para eu ler, grave na nuvem com a **Transcrição de áudio** ligada. Se você tiver a transcrição, cole aqui." Receipt, stop.
- **Meet, otherwise:** "Não achei a transcrição dessa reunião. Para as próximas: ao criar a reunião no Google Agenda, abra as opções da videochamada e, em registros da reunião, marque **Transcrever a reunião** (os nomes podem variar um pouco na sua tela) — ela começa quando você entra. Se você tiver a transcrição em outro lugar, cole aqui que eu sigo."
- No Google Meet folder at all and no transcript ever found → add once: "Talvez o seu plano do Google Workspace não tenha transcrição (o Business Starter não tem). O Rica pode confirmar."
- Write the receipt (`sem transcrição`) and stop. Never build from memory or notes.

### Step 2 — Read and pull out

Read the whole transcript. Speaker names can be wrong; when it matters who said something, say so instead of guessing. Each item keeps its time (`~00:14`).

1. **Resumo** — one short paragraph.
2. **Decisões** — what was decided, by whom.
3. **O que ficou combinado** — each promise with who and by when: hers ("eu te mando o roteiro até sexta") and the client's ("eles me mandam os passaportes"). Missing → `sem dono` / `sem data`.
4. **Preferências e cuidados** — what the client said they love, avoid, need.
5. **Perguntas em aberto** — what nobody answered.
6. **Frases que valem guardar** — at most three, word for word.
7. **Datas** — trips, deadlines, the next meeting.
8. **O que acharam do seu serviço** — only when her offer, prices, way of working or results came up: what they asked, worried about, loved, already do on their own, or asked for. One line each, from transcript lines only. Not their trip or personal facts — those go to the sheet. None → skip.

### Step 3 — One batch for her

Read the sheet once and drop what is already there. Then show everything at once, numbered straight through:

> "Reunião com a **<Nome>** — <data>, <duração>.
> <resumo>
>
> **Na ficha**
> - Preferências: 1. <linha> (~00:14)
> - O que está aberto: 2. <você · o quê · até quando> (~00:31) 3. <o cliente · o quê · sem data> (~00:40)
> - Histórico: 4. <uma linha da reunião>
> - Arquivos: 5. Transcrição da reunião de <data> · <link>
>
> **No histórico**: 6. o resumo (decisões, combinados, perguntas em aberto, frases)
>
> **O que os clientes acham do seu serviço**: 7. <linha> (~00:52)
>
> Posso guardar? (**sim pra tudo** / os números que sim / **ajustar**)"

- **Zoom or pasted transcript:** add a line "8. A transcrição completa na pasta da <Nome> no Drive".
- **Someone not yet a client:** ask first, one question: "Como ficou — **fechou**, **vai pensar** ou **não**?" Record her word. Fechou or vai pensar → offer /novo-cliente with this meeting as its source, then show the batch for the new sheet. Não → only the reactions line and a dated note in `departamentos/clientes/index.md` under `## Conversas que não viraram cliente` (name, date, why, in their words when given).
- **A department or project meeting:** the resumo for its histórico and the next step for its brief's Próximo passo; no sheet, no reactions unless clients' views on her service came up.

### Step 4 — Write, on her sim

- Sheet lines → their sections, under the right heading; update `atualizado:`.
- The resumo → hand it to /contexto for the client's histórico (dated, with the transcript link). Her sim covers it.
- Zoom or pasted transcript → saved word for word as `Transcrição - <Nome> - YYYY-MM-DD.md` (Zoom: `[HH:MM:SS] <Pessoa>: <texto>` per line) in the client's Drive folder, the same way /guardar-no-cliente saves a file; the Arquivos line points to it.
- Reactions → `departamentos/clientes/reacoes.md` (create it with the header below if missing), under the section that fits: **O que encantou · Dúvidas e receios · O que já fazem sozinhos · Pediram**. Line: `- **<rótulo curto>.** "<frase>" <contexto em poucas palavras>. — <cliente>, <data>`. The same reaction from another client extends the existing line with `· <cliente>, <data>` — that is how a pattern shows. Never rewrite or remove a line.
- A department or project: resumo to its histórico via /contexto; Próximo passo through /sistema's write-back.
- What she said **não** to is dropped.

`reacoes.md` header, when created:

```markdown
# O que os clientes acham do meu serviço

_Cada linha vem de uma reunião, nas palavras do cliente. Quando outro cliente diz o mesmo, a linha cresce._

## O que encantou
## Dúvidas e receios
## O que já fazem sozinhos
## Pediram
```

### Step 5 — Próximo passo and follow-up

End with one line: the single most urgent thing — her promise with the nearest date first; else what the client owes and she needs to chase; else the first step of a decision. "**Próximo passo:** mandar o roteiro para a Silva até sexta — você prometeu aos 31 minutos."

Then, only if she promised something: "Quer que eu escreva a mensagem de follow-up para a <Nome>? Fica como rascunho para você mandar." On yes, hand /minha-voz only what was said in the meeting.

### Step 6 — Receipt and report

Always, even when the run stopped early:

`YYYY-MM-DD | resumo-da-reuniao | <slug ou departamento> · <fonte: meet / zoom / colado / sem transcrição> · <n> salvos, <n> recusados · reações <n>` in `_sistema/log.md`.

Reply in one line: "Reunião guardada na ficha e no histórico da **<Nome>**." plus the próximo passo.

## What this skill never does

- Writes before her **sim**.
- Builds a resumo from an AI summary, notes or memory.
- Copies, moves, renames, shares or deletes a Meet transcript.
- Shortens or tidies a transcript it saves.
- Sends anything to the client, or puts her private notes in a follow-up.
- Writes a document number anywhere.
- Decides the outcome of a first conversation for her.

## When to refuse

- Asked to send the summary or the follow-up to the client — "Enviar fica com você. Eu deixo o rascunho pronto."
- Asked to make the resumo from the Gemini or Zoom AI notes, or from memory — "Sem a transcrição eu posso errar o que foi dito. Cola a transcrição aqui que eu faço."
- Asked to save a document number heard in the meeting — "O número eu não guardo. Anoto que o documento existe e o que importa nele."

## Failure modes

- **Drive not connected:** "Não consigo abrir o seu Drive. A conexão do Google Drive está ligada?" She can paste the transcript instead.
- **Zoom not connected** (`reunioes: zoom`, no Zoom tools): "Não consigo abrir o seu Zoom. Conecte ele nas configurações do Claude, em **Conectores**, e me chama de novo. Ou cola a transcrição aqui." Use the browser only if she asks.
- **Someone else hosted the Zoom meeting:** the recording is in their account; she can paste the transcript, or ask the host for it.
- **Transcript in another account's Drive** (someone else hosted): she can paste it, or ask the host to share it.
- **Very long transcript:** read it in parts; pull out per part, then merge before Step 3.
- **Two languages or bad recognition:** keep only what is clear; mark the rest "trecho confuso na transcrição".
- **Client with `status: arquivado`:** say so and ask before writing.
- **No Drive folder for the client** (`drive: a criar`) and a Zoom or pasted transcript: keep it in `departamentos/clientes/<slug>/` locally and say it moves to the Drive once the folder exists.

## STOP handling

On `PARAR` or `STOP`: halt, make no further writes, say what was already saved, and wait.

## Headless behavior

Never runs headless; it needs her sim.

---
name: conteudo-newsletter
description: "Escreve uma edição da newsletter com ela, a partir do material dela ou de uma sugestão, até o agendamento no MCM: a ideia, o rascunho com opções de assunto e texto de pré-visualização, e o agendamento para a lista dela, com o sim dela em cada etapa. Normalmente começa por um horário de newsletter no plano; também quando ela diz \"/conteudo-newsletter\", \"escreve a newsletter\", \"próxima newsletter\", \"tenho uma coisa pra newsletter\", \"manda um e-mail pra minha lista\"."
---

# conteudo-newsletter — one newsletter issue, her words to scheduled

She leads with her voice and her ideas; this skill shapes them into one email and schedules it. It never sends on its own.

It does one thing: **take one newsletter issue from her material (or a suggestion) to scheduled.** It is usually started by conteudo-post with a newsletter slot from the plan. Started directly by name, it first runs conteudo-post's Steps 1-2 (find the slot, the missed-slot rule) and shows its "This post" table (Step 3; Kind of post: the newsletter format; Ends with: the offer if it's an offer issue, else her reply invitation), then continues here. Social posts belong to conteudo-estatico and conteudo-video.

Speak to her in plain, warm Brazilian Portuguese. Say "a newsletter", "o e-mail", "a sua lista", "o calendário"; never file names, "skill", "API", "campaign ID" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`.

1. The slot conteudo-post passed: issue number, date and time (and the original slot if it was missed), topic, newsletter format, idea.
2. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.
3. `departamentos/conteudo/estrategia.md` — who we write for, which layers are on, topics, the newsletter line in Cadence (on, how often, day and time, which list), the ask, the wedge, which issues are offer issues.
4. `../conteudo-estrategia/platforms/newsletter.md` — the newsletter's formats, writing rules, scheduling and results. Only if the newsletter is on in `estrategia.md`. Substack on too: `../conteudo-estrategia/platforms/substack.md` (the issue also goes out there as an article).
5. `departamentos/conteudo/plano.md`, `calendario.md` and `ideias.md` — the slot, what's scheduled, the idea backlog.
6. `departamentos/conteudo/ghl.md` — location and user IDs, and its Newsletter section: from name, from email, reply-to, the list (tag or segment).
7. The issue's own `departamentos/conteudo/newsletters/edicao-NN-<slug>.md`, if it exists — to resume. When the newsletter is the podcast: the episode's `departamentos/conteudo/podcast/episodio-NN-<slug>/episodio.md` (its approved kit and transcript are her material).
8. `sobre-mim/sobre-mim.md` — only her time zone.
9. Only when suggesting or drafting (Steps 2-3):
   - the business file of the area in play (`sobre-mim/cerebro-do-negocio.md`, or `cerebro-do-negocio-<area>.md` per /sistema's **Areas**). It evolves; always read the current one.
   - `../conteudo-estrategia/playbook.md` — rules, awareness levels, hooks, how posts end (§ 7), the newsletter section, the 4-point check.
   - `../conteudo-estrategia/library.md` — the newsletter formats catalog.
   - `departamentos/conteudo/swipe.md` — lines that worked for her, if it exists.
   - the posts published since the last issue (`calendario.md`, their `post.md`) — material for a suggestion.
   - `sobre-mim/escrita.md` — her voice.

Never read or print `departamentos/conteudo/.env`.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is scheduled or sent without an explicit sim at the schedule gate. A yes to the draft is not a sim to send."

> "Two gates, in order: draft (with subject lines and preview text), schedule. Each waits for an explicit sim (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a sim."

> "Her material comes first. Step 2 always asks for what she has, and offers a suggestion in the same message. Claude never invents a story, a client, a result or a stance she hasn't given."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "One idea and one ask per email. Plain text, no images."

> "A client story or case study goes out only when she confirms the client agreed."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 1 — The issue and where it stands
- Use the slot conteudo-post passed. If `newsletters/edicao-NN-<slug>.md` exists, read its Etapa/Status table and resume at the first step not done.
- New issue: create `departamentos/conteudo/newsletters/edicao-NN-<slug>.md` in the shape below (the slug once the idea is set).
- The newsletter is the anchor (`estrategia.md`; an older strategy saying the newsletter leads the theme counts): this issue sets the topic for the cycle's posts and is due by its write-by date in `plano.md` (2 days before it's sent). Say so in one line when it's close.
- The newsletter is the podcast: this issue comes from episode N (the slot's idea, `do episódio N`). Its kit isn't approved yet → offer the episode first ("Essa edição vem do episódio N. Quer fazer o episódio primeiro?"); she says no → the issue goes ahead as a normal one on the planned topic.
- The newsletter is off in `estrategia.md`: "A newsletter ainda não está ligada na sua estratégia de conteúdo. Quer ligar primeiro?" Stop.
- `ghl.md` has no Newsletter section, or no list: "A sua newsletter ainda não está configurada no MCM: <what's missing>. Quer terminar isso primeiro?" Hand to conteudo-instalar on sim. Stop.

**Issue shape:**

```markdown
# Edição N: <short title, once the idea is set>

Horário: <day date time> · <topic> · <format> · edição de oferta: sim/não

| Etapa | Status |
|---|---|
| Ideia | |
| Rascunho | |
| Agendamento | |
| Resultados | |

## O material dela
<what she gave, as she gave it>

## E-mail
Opções de assunto: 1. … 2. … 3. …
Pré-visualização:
<body>

## Notas da execução
- <calls made without asking, her edits at each gate>
```

### Step 2 — Her material, with a suggestion
- One message, both at once: "Tem alguma coisa que você quer escrever dessa vez — umas linhas, um áudio, a história de um cliente, uma pergunta que alguém te fez? Ou eu sugiro: <one suggestion in one line, and why>."
- The suggestion comes from the slot's topic and format, the posts since the last issue (their best idea, gone deeper), `ideias.md`, and real questions she's mentioned. One suggestion, not a menu.
- Her material wins. Keep it in the issue file as she gave it. If it fits a different format than the slot's, say which and use it.
- She takes the suggestion: ask one question that gets her own angle on it ("Me conta uma vez em que você viu isso acontecer?"). A newsletter without anything of hers in it is a blog post.
- **The newsletter is the podcast:** skip the question. Her material is the episode: its transcript and approved kit. Say in one line: "Vou escrever essa a partir do episódio N." The letter is the episode's idea in her words (playbook § 12), with the link to listen once, near the end.

### Step 3 — Draft (gate 1)
- Write it in the slot's format (the library's newsletter formats), from her material, in her voice: the newsletter section of the playbook and `platforms/newsletter.md`. Plain text, 200-400 words, short paragraphs, one CTA for the layer that's on (or the offer, on an offer issue).
- Then the subject: 2-3 options, short and specific, written last, no emoji, plus one preview text line that adds to the subject.
- **The newsletter is the anchor:** under the email, propose the cycle's post angles, one per post slot in this cycle (from `plano.md`), each matched to its slot's post type and format, by the playbook's "From the anchor to everything" section (§ 12): its points → a carousel, its story → a reel, its question → a text post, its moment → a photo post. One line each: the post, the angle, why it stands alone.
- Run the playbook's 4-point check (hook, what they get, plain, ending: the one ask of the email, or the offer on an offer issue) and fix what fails before showing.
- Show the subject options, the preview text and the email as it will read.
- **Gate:** "A newsletter está boa? Escolhe um assunto e diz **sim** (os ângulos dos posts vêm junto), ou me diz o que mudar."
- Record the approved email, subject and preview text in the issue file.

### Step 4 — Schedule (gate 2)
- Date and time from the slot, in her time zone; the list, from name, from email and reply-to from `ghl.md`.
- If the slot has passed or is under 1 hour away: conteudo-post's missed-slot rule decides the new time.
- First issue (no issue has a campaign ID yet): run conteudo-instalar step 14's newsletter check again before the gate. A failed check stops here: say what's missing, keep the approved draft.
- **Gate:** "Pronto pra agendar? <day date time> para <list>, de <name>. Diga **sim** que eu agendo." Substack on: "…para <list>, de <name>, e no seu Substack no mesmo horário." Her sim covers both.
- On sim:
  1. MCM `create-email-campaign`: `name` "Newsletter <N>: <short title>", `editorType: text`, `editorContent` = the approved email, `timeZone` = hers, `userId` from `ghl.md`. Idempotency key: `<location ID>-newsletter-NN-<slug>-create`.
  2. MCM `schedule-campaign`: `scheduleType: scheduled`, `scheduleConfig.sendAt` in her time zone, `emailMeta` = subject, from name, from email, reply-to, preview text; `recipients` = the list from `ghl.md` (tag or segment). Idempotency key: `<location ID>-newsletter-NN-<slug>-schedule`.
  3. Verify it shows as scheduled; report the campaign status.
  4. Substack on: hand the approved email, the chosen subject, the preview text and the send time to conteudo-substack (article). If it can't schedule it, the email still goes; say so in one line.

### Step 5 — Close
- Issue file: Draft and Schedule rows, campaign ID, send time.
- `calendario.md`: the issue's row (date, `Newsletter <N>: <topic>`, format `newsletter`, idea, `Agendado <time>`).
- `plano.md`: set this slot's Status to `agendado` — the Status cell only.
- `ideias.md`: mark the idea `usada: newsletter N` if it came from there; add new ideas she mentioned as `não usada`.
- Led cycle: each approved angle goes into `ideias.md` as `não usada`, source `newsletter N`, tagged `para o post M`.
- **The podcast is the newsletter:** offer the episode next, in one line: "Quer preparar o episódio N agora? Você vai falar essa carta."
- Department brief: set Próximo passo to the next `planejado` slot of any kind, as conteudo-estatico does; update Estado atual with its date and one line, and `atualizado:`. Mention it in one short line.
- Receipt and milestone (below). Hand back to conteudo-post's Step 4.

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-newsletter | idea / draft-approved / scheduled / stopped-at-<gate> | newsletter N · <topic> · <format> · campaign <ID> · missed: yes/no`

## Milestone

Runs that reached a new stage: hand /contexto one line for `contexto/conteudo.md`:
`Newsletter N <rascunho aprovado / agendada para <slot>>: <topic>, <format>. Em aberto: <next step, ou nada>.`

## What this skill never does

- Sends or schedules without an explicit sim at the schedule gate. Never uses `scheduleType: immediate`.
- Writes a newsletter without asking for her material first.
- Invents a story, a client, a quote, numbers or results.
- Adds images or a designed template; it's a plain-text email.
- Changes the list, the sending domain or anything else in MCM beyond the one campaign.
- Reads, prints, copies or asks for `.env` or the MCM key.
- Edits `estrategia.md`, `ghl.md`, the shipped library, playbook or platform files, `sobre-mim/`, or anything in `contexto/` (milestones go through /contexto).
- Changes `plano.md` beyond the Status cell of the slot it scheduled; touches the brief beyond Próximo passo, Estado atual and `atualizado:`.
- Runs more than one issue per run.

## When to refuse

- No `estrategia.md`, or the newsletter is off — "A newsletter ainda não está ligada na sua estratégia de conteúdo. Quer ligar primeiro?"
- No sending address or list in MCM — "A sua newsletter ainda não está configurada no MCM. Quer terminar isso primeiro?"
- A request to send right now, skipping the gates — "Toda newsletter passa pela aprovação do rascunho e do agendamento."
- A client story without her confirming the client agreed — "<client> concordou em aparecer na newsletter? Eu deixo anônimo até você confirmar."
- MCM not connected — "O MCM não está conectado agora, então não consigo agendar." Stop after the draft.

## Failure modes

- **Started directly with no slot** — run conteudo-post's Steps 1-2 first; with still no newsletter slot, write it for the next newsletter date in her cadence and say so.
- **She has nothing and doesn't want the suggestion** — keep the slot as it is; offer to move it to the next date. Never send a filler issue.
- **`create-email-campaign` or `schedule-campaign` 4xx** — report the message once; fix the one named field if it's clear (e.g. from email not verified → tell her the sending address needs verifying in MCM); otherwise stop. Never retry blindly: a duplicate send is worse than a late one.
- **The campaign was created but scheduling failed** — leave the draft campaign in MCM, record its ID in the issue file, and say so; the next run picks it up at Step 4.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes, schedule nothing. Report what was already done (issue file, campaign ID if any) and wait.

## Headless behavior

This skill needs her at two gates, so it does not run unattended. With nobody watching: read the files, write one receipt line naming the slot and the suggestion (`draft, not approved`), and execute nothing else.

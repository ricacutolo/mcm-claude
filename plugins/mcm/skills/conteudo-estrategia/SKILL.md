---
name: conteudo-estrategia
description: "Monta ou revisa a estratégia de conteúdo dela — para quem ela posta, para que o conteúdo serve agora, temas, tipos de post, formatos, quando ela posta e a única chamada para ação — partindo do que já se sabe do negócio, e depois oferece planejar as próximas 4 semanas. Quando ela diz \"/conteudo-estrategia\", \"monta a minha estratégia de conteúdo\", \"revisa a estratégia\", \"atualiza a estratégia de conteúdo\", \"quero mudar sobre o que eu posto\", depois que a revisão mensal de conteúdo recomenda, ou durante a configuração do conteúdo."
---

# conteudo-estrategia — set up or revise

Decides how her content works: who it's for, what it's for right now, and what it picks from (topics, post types, formats). It starts from what's already known about her business, so she answers as few questions as possible.

It does one thing: **set or revise her content strategy.** It never plans slots (that's conteudo-plano), makes posts (conteudo-post) or edits her business file.

Speak to her in plain, warm Brazilian Portuguese. Say "a sua estratégia de conteúdo", "o arquivo do seu negócio", "o plano"; never file names, "skill", "layer" without explaining it, or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. Two reference files ship with the plugin in this skill's own folder, and other skills read them from here: `library.md` (the strategy library: post types, formats, entries by type of business) and `playbook.md` (the copy playbook). Both are read-only. Both are written in English, with English examples; her posts are written in Brazilian Portuguese, so carry the move, never the English words.

1. the business file of the area in play (`sobre-mim/negocio.md`, or `negocio-<area>.md` per /sistema's **Areas**) — what she sells, who she sells to, what those people believe, objections, pains, why customers pick her, how she sells, booking, goals, what's off-limits. Always the current file, never a remembered copy.
2. `library.md` — the post types and formats catalogs, and entries for her type of business. Then `departamentos/conteudo/notas-da-biblioteca.md`, if it exists — her own entries and catalog additions; they win for her business.
3. `playbook.md` — CTA by layer, awareness levels.
4. `departamentos/conteudo/estrategia.md` — if it exists (revise mode), including its "Diferenças deliberadas do arquivo do negócio".
5. Revise mode only: `departamentos/conteudo/desempenho.md` ("O que aprendemos") and the last `conteudo-revisao` line in `_sistema/log.md`.
6. `sobre-mim/escrita.md` — for the voice of the strategy's own wording.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is written to the strategy before an explicit sim to the full draft shown. Silence or an edit request is not a sim."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

> "Her business file is read, never edited. Where the strategy differs from it, say so as a suggestion; she decides, and a change to the business file waits in `_sistema/pendentes.md` for her sim."

> "A difference she has marked as deliberate is never flagged again."

> "Only post types and formats from the library catalogs or her library notes. A new one goes into her library notes first, through the monthly content review."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 1 — Mode
- No `estrategia.md` → **setup** (round 1).
- `estrategia.md` exists → **revise** (next round). Say what triggered it: her request, or a conteudo-revisao recommendation (quote it).

### Step 2 — Draft from what's known
From her business file and the library, draft every section:
- **Who we post for** — from who she sells to.
- **Topics** — 4-8, from her customers' pains, objections and what they believe about the problem, in her customers' words.
- **Wedge** — from why customers pick her.
- **CTA** — from her booking flow, matched to the layer that's on (playbook).
- **Idea rules** — from how she sells and what's off-limits, plus the playbook's rules.
- **Library entries for her type of business** — anything marked working; unproven ones only as options.
In revise mode, start from the current strategy and change only what the trigger calls for.

### Step 3 — Ask only what the business file doesn't answer
At most 6 questions, one message, each with a recommended answer:
1. Para que o conteúdo serve agora — quais camadas estão ligadas: credibilidade (quem te pesquisa confia no que vê), audiência (mais gente te encontra), contatos (os posts trazem pedidos de orçamento)?
2. Aparecer na câmera: sim, não ou às vezes?
3. Quais fotos existem (o seu trabalho, a equipe, o espaço), e pode usar fotos de clientes?
4. Quanto tempo por semana para conteúdo?
5. Frequência, dias, horário e plataformas.
6. Algum formato para usar mais, ou tipos de post para desligar?
Skip any question the business file, the current strategy or the conversation already answers. If her time zone isn't in `sobre-mim/sobre-mim.md`, ask it with question 5.

### Step 4 — Business file check
List where the draft differs from her business file (audience, offer, CTA, tone). For each: one line, and a choice — "atualizar o arquivo do negócio" (a suggested line) or "manter como diferença deliberada". Skip differences already listed under "Diferenças deliberadas do arquivo do negócio".

### Step 5 — Gate
Show the full strategy draft, the business file check, and in revise mode what changed from the last round.

> "A estratégia está boa? Diga **sim**, ou me diz o que mudar."

Apply edits exactly, re-show, wait for sim. Differences she keeps go under "Diferenças deliberadas do arquivo do negócio". Business file updates she picks go to `_sistema/pendentes.md` (below).

### Step 6 — Write
On sim:
1. Revise mode: copy the current `estrategia.md` to `departamentos/conteudo/rodadas-anteriores/estrategia-rodada-<N>.md` (create the folder if missing) before writing.
2. Write `departamentos/conteudo/estrategia.md`, headed "# Estratégia: <business>, rodada <N>" and "Status: CONFIRMADA rodada <N> (<her name>, <date>)", with sections: Para quem postamos · Diferenças deliberadas do arquivo do negócio · Para que serve o conteúdo agora (camadas) · O CTA único · Diferencial · Como os posts são escolhidos: tema × tipo de post × formato (Temas, Tipos de post ligados, Formatos ligados) · Regras de ideia · Frequência (dias, horário, fuso, plataformas) · Modelos · Voz.
3. Each business file update she picked: one line in `_sistema/pendentes.md` (re-read it first), in the system's format: `- [ ] YYYY-MM-DD · add · sobre-mim/negocio.md § <section> · <the exact proposed line> · (de: estratégia de conteúdo rodada <N>)`. The time zone, if she gave one and it isn't in `sobre-mim/sobre-mim.md`: the same, for that file.
4. Department brief: update Estado atual (date, one line on the round) and `atualizado:`. If there's no current plan, or the change affects planned slots, set Próximo passo to "Planejar as próximas 4 semanas. Diga \"planeja o conteúdo\"." Touch nothing else; mention it in one short line.
5. Receipt and milestone (below).

### Step 7 — Hand off
> "Quer que eu planeje as próximas 4 semanas agora?"

Run conteudo-plano only on sim.

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-estrategia | setup / revised / draft-not-approved | round <N> · trigger: <request / conteudo-revisao / content setup> · business file suggestions: <N pending, or none>`

## Milestone

Each approved run: hand /contexto one line for `contexto/conteudo.md`:
`Estratégia de conteúdo rodada <N> aprovada: camadas <list>, <count> temas, formatos <list>. Em aberto: <planejar as próximas 4 semanas / sugestões pro arquivo do negócio pendentes / nada>.`

## What this skill never does

- Writes `estrategia.md` without an explicit sim.
- Edits `sobre-mim/negocio.md` or any `sobre-mim/` file. Changes there only wait in `_sistema/pendentes.md`.
- Re-flags a difference marked as deliberate.
- Edits `library.md`, `playbook.md`, `notas-da-biblioteca.md`, `swipe.md`, `plano.md`, `calendario.md`, `ideias.md` or anything in `contexto/` (milestones go through /contexto).
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Invents post types or formats outside the catalogs, or claims something "works" without the library or her notes marking it working.
- Deletes an old strategy round — it goes to `rodadas-anteriores/`.
- Runs conteudo-plano without a sim.

## When to refuse

- No business file and no answers to work from — "Ainda não tem de onde montar a estratégia. Vamos preencher o arquivo do seu negócio primeiro, ou você pode responder algumas perguntas." (the strategy starts from what's known)
- A request to make up results or proof — "A estratégia só usa o que é real; resultados entram quando a gente tiver." (real things only)
- A request to switch on a post type or format that isn't in the catalogs — "Vamos colocar nas suas notas da biblioteca primeiro (a revisão mensal faz isso), e aí ligar." (one owner per concern)

## Failure modes

- **Business file thin or out of date** — draft what it supports, ask the gaps in Step 3, and add "atualizar o arquivo do negócio" as a suggestion.
- **Library missing a catalog** — use what exists, flag the gap, never invent entries.
- **She stops mid-questions** — keep the answers in the conversation; write nothing to `estrategia.md`; receipt `draft-not-approved`.
- **Department brief missing** — write `estrategia.md` only; say so.
- **`_sistema/pendentes.md` can't be read** — keep the suggestions in the conversation and say they weren't saved.
- Prefer doing less: when unsure, stop at the gate and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already written (past-rounds copy, `estrategia.md`, pending items, brief lines, receipt) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): read the files and draft the strategy and the business file check, then write only one receipt line marked `draft-not-approved`. Never write `estrategia.md`, `rodadas-anteriores/`, pending items or the department brief without her sim.

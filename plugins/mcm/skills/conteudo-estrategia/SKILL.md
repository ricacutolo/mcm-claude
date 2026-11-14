---
name: conteudo-estrategia
description: "Monta ou revisa a estratégia de conteúdo dela — para quem ela posta, para que o conteúdo serve agora, temas, tipos de post, formatos, quando ela posta e a única chamada para ação — partindo do que já se sabe do negócio, e depois oferece planejar as próximas 4 semanas. Quando ela diz \"/conteudo-estrategia\", \"monta a minha estratégia de conteúdo\", \"revisa a estratégia\", \"atualiza a estratégia de conteúdo\", \"quero mudar sobre o que eu posto\", depois que a revisão mensal de conteúdo recomenda, ou durante a configuração do conteúdo."
---

# conteudo-estrategia — set up or revise

Decides how her content works: who it's for, what it's for right now, and what it picks from (topics, post types, formats). It starts from what's already known about her business, so she answers as few questions as possible.

It does one thing: **set or revise her content strategy.** It never plans slots (that's conteudo-plano), makes posts (conteudo-post) or edits her business file.

Speak to her in plain, warm Brazilian Portuguese. Say "a sua estratégia de conteúdo", "o arquivo do seu negócio", "o plano"; never file names, "skill", "layer" without explaining it, or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. Two reference files ship with the plugin in this skill's own folder, and other skills read them from here: `library.md` (the strategy library: post types, formats, entries by type of business) and `playbook.md` (the copy playbook). Both are read-only. A third set ships in `platforms/`: one read-only file per platform (`platforms/README.md` explains them). The platforms line in her strategy is the switch: every content skill reads only the files for the platforms on it. Both are written in English, with English examples; her posts are written in Brazilian Portuguese, so carry the move, never the English words.

1. the business file of the area in play (`sobre-mim/cerebro-do-negocio.md`, or `cerebro-do-negocio-<area>.md` per /sistema's **Areas**) — what she sells, who she sells to, what those people believe, objections, pains, why customers pick her, how she sells, booking, goals, what's off-limits. Always the current file, never a remembered copy.
2. `library.md` — the post types and formats catalogs, and entries for her type of business. Then `departamentos/conteudo/notas-da-biblioteca.md`, if it exists — her own entries and catalog additions; they win for her business.
3. `playbook.md` — CTA by layer, awareness levels. Then `platforms/README.md` and the file for each platform she has or might use (each file's "When to recommend it").
4. `departamentos/conteudo/estrategia.md` — if it exists (revise mode), including its "Diferenças deliberadas" and its `Segue:` line.
4b. the CEO strategy (`departamentos/ceo/estrategia.md`, or `estrategia-<area>.md` for the area in play) — if it exists: its **Direções → Conteúdo**, Minha primeira oferta, Como vende and Próximos 90 dias. The CEO decides what content is for; this skill decides how. Never written here.
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
From the CEO's direction for content (when there is one), her business file and the library, draft every section. With a direction, "What content is for right now" (the layers) and the CTA come from it; without one, from the business file as below. In revise mode, a CEO strategy newer than the `Segue:` date is a trigger on its own: say what changed in the direction, in one line.
- **Who we post for** — from who she sells to.
- **Topics** — 4-8, from her customers' pains, objections and what they believe about the problem, in her customers' words.
- **Wedge** — from why customers pick her.
- **Como os posts terminam** — the business ask, from her booking flow and matched to the layer that's on (playbook § 7), plus the ask rhythm: about 1 post in 3 carries the ask; the rest end lightly (save it, a question to answer in the comments) or with nothing at all. The plan marks which slots carry the ask.
- **Idea rules** — from how she sells and what's off-limits, plus the playbook's rules.
- **Library entries for her type of business** — anything marked working; unproven ones only as options.
In revise mode, start from the current strategy and change only what the trigger calls for.

### Step 3 — Ask only what the business file doesn't answer
At most 6 questions, one message, each with a recommended answer:
1. (Skipped when the CEO's direction says it.) Para que o conteúdo serve agora — quais camadas estão ligadas: credibilidade (quem te pesquisa confia no que vê), audiência (mais gente te encontra), contatos (os posts trazem pedidos de orçamento)?
2. Aparecer na câmera: sim, não ou às vezes? (Skipped when the content setup already asked about reels: its answer in `configuracao.md` decides whether reels are on.)
3. Quais fotos existem (o seu trabalho, a equipe, o espaço), e pode usar fotos de clientes? (As fotos vão numa pasta do Google Drive, Fotos de conteúdo, sempre que ela tiver; os posts escolhem de lá.)
4. Quanto tempo por semana para conteúdo?
5. Frequência, dias, horário e plataformas. Recommend platforms from each platform file's "When to recommend it": Instagram always, Facebook when she has a Page, LinkedIn when she sells to professionals, the newsletter (`platforms/newsletter.md`) when she sells something people decide on over time and has a list, Substack (`platforms/substack.md`) only with the newsletter on, when her expertise is what she sells or she already has a Substack (light: each issue goes there too, plus 2-3 Notes a week from what she's already making). If the content setup already noted her platforms, start from those. Newsletter on: how often (every two weeks for a new list, weekly once she's keeping up), day and time (Tuesday morning by default), and how often an issue is an offer (one in four or five), and whether the newsletter leads the theme (recommend yes: each issue sets the topic for the posts until the next one).
6. Algum formato para usar mais, ou tipos de post para desligar?
Skip any question the business file, the current strategy or the conversation already answers. If her time zone isn't in `sobre-mim/sobre-mim.md`, ask it with question 5.

### Step 4 — Business file and direction check
List where the draft differs from her business file (audience, offer, CTA, tone). For each: one line, and a choice — "atualizar o arquivo do negócio" (a suggested line) or "manter como diferença deliberada". Skip differences already listed under "Diferenças deliberadas do arquivo do negócio".
Then, with a CEO direction: where the draft goes against it (she wants it so), one line each with her reason, kept under "Diferenças deliberadas da direção do CEO". Never silently; never an edit to the CEO strategy.

### Step 5 — Gate
Show the draft so she sees the thinking behind it, not a preset. In this order:

1. **Para que serve o seu conteúdo:** the three options (confiança, audiência, contatos) and the pick, in a short paragraph with the reason tied to her business (or the CEO's direction).
2. **Tipos de post:** a short paragraph first ("Minha escolha: liguei estes porque …"), then every post type in the library catalog (and her library notes), each with a few-word gloss and its mark: **[Ligado]** or **[Desligado]**.
3. **Formatos:** the same: the paragraph, then every format in the catalog, **[Ligado]** or **[Desligado]**. The reason names what drives it (face, photos, time).
4. **Onde:** the same, every platform file: **[Ligado]** or **[Desligado]**.
5. **Como os seus posts terminam:** the paragraph, then the list, each line with its rhythm: **[Ligado]** O pedido ("<her ask, in her words>") · mais ou menos 1 post em 3 / **[Ligado]** Salvar para depois · mais ou menos 1 em 3 / **[Ligado]** Uma pergunta para responder nos comentários · mais ou menos 1 em 4 / **[Ligado]** Sem pedido, só valor · o resto / **[Desligado]** Compartilhar com quem precisa / **[Desligado]** Seguir para ver mais / **[Desligado]** Comentar uma palavra para receber algo (vem com contatos). The rhythm is her strategy's own; these are the defaults for credibility.
6. **Quando:** a short paragraph with the pick and why.
7. "Quer ligar ou desligar alguma coisa? É só me dizer."
8. **Mudando depois:** "muda o plano", "revisa a minha estratégia", and "transforma isso em post" for an idea in the middle of the plan.

Then the business file check, and in revise mode what changed from the last round.

> "Responde com **1** ou **2**: 1. Está boa 2. Quero mudar algo. Ou me conta o que você está pensando." (one option per line, as in /sistema's reply rules)

Apply edits exactly, re-show, wait for sim. Differences she keeps go under "Diferenças deliberadas do arquivo do negócio" (or "Diferenças deliberadas da direção do CEO"). Business file updates she picks go to `_sistema/pendentes.md` (below).

### Step 6 — Write
On sim:
1. Revise mode: copy the current `estrategia.md` to `departamentos/conteudo/rodadas-anteriores/estrategia-rodada-<N>.md` (create the folder if missing) before writing.
2. Write `departamentos/conteudo/estrategia.md`, headed "# Estratégia: <business>, rodada <N>" and "Status: CONFIRMADA rodada <N> (<her name>, <date>)" and "Segue: estratégia do CEO de <its `atualizado:` date>" (or "Segue: sem estratégia do CEO ainda (arquivo do negócio)"), with sections: Para quem postamos · Diferenças deliberadas do arquivo do negócio · Diferenças deliberadas da direção do CEO (only when there is one) · Para que serve o conteúdo agora (camadas) · Como os posts terminam (the ask, in her words, and the rhythm: each ending, on or off, and how often) · Diferencial · Como os posts são escolhidos: tema × tipo de post × formato (Temas, Tipos de post ligados, Formatos ligados) · Regras de ideia · Frequência (dias, horário, fuso, plataformas: the switch the other content skills read; reels on or off; a separate LinkedIn time only if it differs; the newsletter line when it's on: how often, day and time, offer issues, newsletter leads the theme: sim/não; the Substack line when it's on: Notes a week, 2 or 3) · Modelos · Voz.
3. Each business file update she picked: one line in `_sistema/pendentes.md` (re-read it first), in the system's format: `- [ ] YYYY-MM-DD · add · sobre-mim/cerebro-do-negocio.md § <section> · <the exact proposed line> · (de: estratégia de conteúdo rodada <N>)`. The time zone, if she gave one and it isn't in `sobre-mim/sobre-mim.md`: the same, for that file.
4. Department brief: update Estado atual (date, one line on the round) and `atualizado:`. If there's no current plan, or the change affects planned slots, set Próximo passo to "Planejar as próximas 4 semanas. Diga \"planeja o conteúdo\"." Touch nothing else; mention it in one short line.
5. Receipt and milestone (below).

### Step 7 — Hand off
> "Quer que eu planeje as próximas 4 semanas agora?"

Run conteudo-plano only on sim.

No CEO strategy, and none offered yet (no `Sessão do CEO oferecida` line in `estrategia.md`): offer it once, after the plan question: "O seu conteúdo fica mais certeiro depois que a estratégia do seu negócio estiver definida. Quer fazer essa sessão?" Run /estrategia-do-negocio only on sim. Either way, add `Sessão do CEO oferecida: YYYY-MM-DD` under the strategy's header so it isn't offered again.

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-estrategia | setup / revised / draft-not-approved | round <N> · trigger: <request / conteudo-revisao / content setup> · business file suggestions: <N pending, or none>`

## Milestone

Each approved run: hand /contexto one line for `contexto/conteudo.md`:
`Estratégia de conteúdo rodada <N> aprovada: camadas <list>, <count> temas, formatos <list>. Em aberto: <planejar as próximas 4 semanas / sugestões pro arquivo do negócio pendentes / nada>.`

## What this skill never does

- Writes `estrategia.md` without an explicit sim.
- Edits `sobre-mim/cerebro-do-negocio.md` or any `sobre-mim/` file. Changes there only wait in `_sistema/pendentes.md`.
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

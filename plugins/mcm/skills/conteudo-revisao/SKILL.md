---
name: conteudo-revisao
description: "A revisão mensal de conteúdo dela: puxa os resultados de cada post no MCM, lê por tema, tipo de post e formato, e recomenda no máximo 5 mudanças para o sim dela — o que aprendemos, frases que valem guardar, mudanças na estratégia ou no plano, sugestões pro arquivo do negócio. Quando ela diz \"/conteudo-revisao\", \"revisão mensal do conteúdo\", \"como foram os meus posts\", \"revisa o conteúdo\", \"o que está funcionando\", na rotina mensal do departamento Conteúdo, ou antes de planejar as próximas 4 semanas."
---

# conteudo-revisao — what the results say, once a month

Turns a month of posts into decisions. It pulls the numbers, reads them honestly, and recommends a few changes. The other skills make the changes; this one only recommends and records what we learned.

It does one thing: **review one window of results and turn them into approved learnings and hand-offs.** It never edits the strategy, the plan, her business file or a post.

Speak to her in plain, warm Brazilian Portuguese. Say "os seus posts", "os resultados", "o que aprendemos", "a sua estratégia de conteúdo"; never file names, "skill", "API" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. The shared reference files ship with the plugin next to this skill's folder: `../conteudo-estrategia/library.md` (the strategy library) and `../conteudo-estrategia/playbook.md` (the copy playbook). Both are read-only; what's learned for her business goes into her own files.

1. `departamentos/conteudo/desempenho.md` — results so far and what we learned.
2. `_sistema/log.md` — the last `conteudo-revisao` line (where the window starts).
3. `departamentos/conteudo/calendario.md` — what was published and when.
4. `departamentos/conteudo/posts/*/post.md` — per post: topic, post type, format, template, hook pattern, MCM post ID.
5. `departamentos/conteudo/estrategia.md` — layers on, topics, post types, formats, cadence, platforms. Then `../conteudo-estrategia/platforms/<platform>.md` for each platform on: its Results section says what counts most there.
6. `departamentos/conteudo/plano.md` — what's coming, so recommendations can say which slots they'd change.
7. `departamentos/conteudo/ghl.md` — location, account and profile IDs.
8. `../conteudo-estrategia/library.md` — entries and statuses (unproven, working, dropped); then `departamentos/conteudo/notas-da-biblioteca.md` and `departamentos/conteudo/swipe.md`, if they exist.
9. `sobre-mim/negocio.md` — for business file suggestions only. Never edited here.
10. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Numbers are copied from MCM as they are. Nothing is estimated, rounded up or invented; a number MCM doesn't give is written as n/a."

> "Nothing is called working or not working until that kind has at least 3 posts and the account reaches more than about 100 people per post. Below that, say 'ainda não dá pra julgar' and what would make it judgeable."

> "At most 5 recommendations per review, each with what, why (the numbers) and where it goes."

> "Learnings, library notes and swipe lines are written only after an explicit sim to each item. Silence or an edit request is not a sim."

> "This skill recommends; other skills change. It never edits the strategy, the plan, her business file or a post, and never the shipped library or playbook. Hand-offs run only on a sim."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 1 — Window
- From the date of the last `conteudo-revisao` line in `_sistema/log.md` to today. First run: everything published.
- Say in one line: "Olhando de <first date> a <last date>: <N> posts publicados."

### Step 2 — Pull the numbers (no gate: facts)
- MCM `get-posts` for the window (body: `type: all`, `accounts` as a comma-separated string, `skip`/`limit` as strings): for each published post, each platform's likes, comments and shares.
- MCM `get-statistics` with the profile IDs (not the account IDs): impressions, reach and new followers per day for the window.
- Newsletter on: MCM `get-campaign-stats` for each issue sent in the window: clicks, replies, unsubscribes (opens recorded, not trusted). Weigh them by `../conteudo-estrategia/platforms/newsletter.md`'s Results section.
- In `desempenho.md`: fill or refresh each post's row (numbers 7+ days after posting count as settled; mark fresher ones `inicial`), with the day's reach as the post's reach, and note the pull date. Add one line under "Totais da conta" for the window. If the file is missing, create it in conteudo-post's format (Posts · Totais da conta · O que aprendemos).

### Step 3 — Read
- Group by topic, post type, format, hook pattern, dark/light and platform (weigh each platform by its file's Results section); and the account trend (reach, followers) across the window.
- Apply the small-numbers rule to every group. Say plainly where the numbers are too small to mean anything.
- Note anything unusual worth a look (a post that got comments, a day reach jumped).

### Step 4 — Recommend (gate)
At most 5 items, ranked. Each: what · why (the numbers) · where it goes · our recommendation (do it, or not yet):
- **Library note** — a new or changed entry for her business, with status unproven / working / dropped and the evidence → `departamentos/conteudo/notas-da-biblioteca.md`. A new post type or format for her catalogs only as its own item.
- **Swipe line** — a line or post that worked, with why and the evidence → `departamentos/conteudo/swipe.md`.
- **Strategy change** — hand-off to conteudo-estrategia (revise).
- **Plan change** — hand-off to conteudo-plano (refresh), naming the slots it would change.
- **Layer** — switch audience or leads on when the numbers support it (a strategy change).
- **Business file** — a suggested update to `sobre-mim/negocio.md`, which waits in `_sistema/pendentes.md` for her sim.

> "Quais desses você quer? Diga **sim** pros que você quer (ou **sim pra todos**), ou me diz o que mudar."

Apply edits exactly, re-show, wait for sim.

### Step 5 — Write
On sim, for the approved items only:
1. `desempenho.md`: under "O que aprendemos", one dated line per approved learning.
2. `notas-da-biblioteca.md`: approved entries under her type of business, with date, status and evidence. Create the file if missing:
   ```
   # Notas da biblioteca: <business>

   O que ela acrescentou à biblioteca de estratégia. Valem mais que a biblioteca para o negócio dela.

   ## Adições ao catálogo
   | Data | Tipo de post ou formato | O que é | Combina com | Status |
   |---|---|---|---|---|

   ## Entradas
   | Data | O quê | Status | Evidência | Notas |
   |---|---|---|---|---|
   ```
3. `swipe.md`: approved swipe lines. Create the file if missing with `# Swipe file: <business>` and the columns `Data · Frase ou post · Por que funcionou · Evidência`.
4. Business file items: one line each in `_sistema/pendentes.md` (re-read it first), in the system's format: `- [ ] YYYY-MM-DD · add · sobre-mim/negocio.md § <section> · <the exact proposed line> · (de: revisão de conteúdo de <first date> a <last date>)`.
5. Offer each approved hand-off ("Quer que eu atualize a sua estratégia de conteúdo agora?" / "Quer que eu atualize o plano agora?"); run it only on sim.
6. Department brief: Estado atual with today's date and one line on the review, and `atualizado:`. If a strategy or plan hand-off was approved and not run, set Próximo passo to it ("Atualizar a estratégia de conteúdo: <change>. Diga \"revisa a estratégia\"."). Mention it in one short line.
7. Receipt and milestone (below).

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-revisao | reviewed / numbers-only / draft-not-approved | <first date> to <last date> · <N> posts · approved: <items or none> · hand-offs: <run / offered / none>`

## Milestone

Each review: hand /contexto one line for `contexto/conteudo.md`:
`Revisão de conteúdo de <first date> a <last date>: <one-line read>. Aprovado: <changes>. Em aberto: <hand-offs not run, ou nada>.`

## What this skill never does

- Invents, estimates or rounds a number; fills a gap MCM doesn't cover with a guess.
- Calls something working or not working below the small-numbers rule.
- Writes learnings, library notes or swipe lines without an explicit sim.
- Edits `estrategia.md`, `plano.md`, `calendario.md`, `ideias.md`, `posts/`, `sobre-mim/` (business suggestions only wait in `_sistema/pendentes.md`), the shipped library or playbook, or anything in `contexto/` (milestones go through /contexto).
- Changes a library note to working without her own numbers behind it.
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Runs a hand-off without a sim.
- Deletes rows or entries. A dropped entry is marked dropped, not removed.
- Makes more than 5 recommendations.

## When to refuse

- A request to make the numbers look better, or to call something working early — "Os números são o que são; eu te digo o que faria eles valerem a análise." (numbers as they are, small-numbers rule)
- A request to change the strategy or plan directly from here — "Isso acontece na estratégia ou no plano. Quer que eu leve pra lá?" (one owner per concern)
- MCM not connected — "O MCM não está conectado agora, então não consigo puxar os números." Review only what's already in the log, and say so.
- No published posts in the window — "Nada foi publicado desde a última revisão, então ainda não tem o que ler."

## Failure modes

- **`get-statistics` rejects the IDs** — use the profile IDs from `ghl.md` (not the account IDs); if it still fails, review the per-post numbers only and say the account line is missing.
- **A post's child posts aren't found** — mark that row "não encontrado no MCM", don't guess; continue with the rest.
- **A post folder has no post type or format** (older posts) — use the calendar row; if that's missing too, group it as "unknown".
- **Library notes missing a section for her type of business** — propose the section as an item; don't create it without a sim.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, recommend "not yet" and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already written (numbers pulled, learnings, library notes, swipe lines, pending items) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): read the files and the numbers and draft the read and the recommendations, then write only one receipt line marked `draft-not-approved`. Never write `desempenho.md`, library notes, swipe lines, pending items or the brief, and never start a hand-off.

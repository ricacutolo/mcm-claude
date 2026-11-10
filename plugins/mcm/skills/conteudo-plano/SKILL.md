---
name: conteudo-plano
description: "Planeja as próximas 4 semanas de posts dela — um tema, um tipo de post e um formato por horário — e avisa qual modelo de design precisa ser criado antes. Quando ela diz \"/conteudo-plano\", \"planeja o conteúdo\", \"planeja as próximas 4 semanas\", \"o que a gente vai postar esse mês\", \"atualiza o plano\", \"coloca formatos no plano\", \"empurra o plano\", \"que fotos eu tiro\", ou quando o próximo passo do departamento Conteúdo diz que o plano está acabando."
---

# conteudo-plano — the next 4 weeks

Decides what gets posted when: one topic, one post type and one format per slot, for the next 4 weeks, so the account rotates instead of repeating itself and the department always knows what's next.

It does one thing: **fill the next 4 weeks of slots.** It never drafts copy, designs or schedules — that's conteudo-post and its makers.

Speak to her in plain, warm Brazilian Portuguese. Say "o plano", "o calendário", "um modelo"; never file names, "skill" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. The shared reference files ship with the plugin next to this skill's folder: `../conteudo-estrategia/library.md` (the strategy library).

1. `departamentos/conteudo/estrategia.md` — topics, which post types and formats are on (and any format to lean on), which layers are on, cadence and slot time, idea rules.
2. `../conteudo-estrategia/library.md` — the post types catalog and the formats catalog (which post types each format fits). Then `departamentos/conteudo/notas-da-biblioteca.md`, if it exists — her own additions to the catalogs.
3. `departamentos/conteudo/calendario.md` — what's already scheduled or published, and the last topics and post types used.
4. `departamentos/conteudo/plano.md` — the current plan, if any (to roll it forward).
5. `departamentos/conteudo/ideias.md` — unused ideas.
6. `departamentos/conteudo/modelos.md` — which templates exist (a template is format × post type).
7. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.
8. `sobre-mim/sobre-mim.md` — only her time zone.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is written to the plan before an explicit sim to the 4 weeks shown. Silence or an edit request is not a sim."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

> "Only topics in the strategy, and only post types and formats that are on. Never invent a topic or switch a type or format on."

> "A suggested angle is marked 'sugestão'. Never present it as her idea or as decided."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 1 — Find the slots
- Cadence and slot time from `estrategia.md` (e.g. Tue and Thu, 12h30), in her time zone (from `sobre-mim/sobre-mim.md`, else ask once).
- Start after the last post that is scheduled in `calendario.md` or planned in `plano.md`, whichever is later. Never re-plan a slot that's already scheduled.
- Fill 4 weeks of slots from there. Number them as post numbers, continuing from the calendar.

### Step 2 — Fill the matrix
For each slot, pick one topic, one post type and one format:
- No topic twice in a row.
- No post type repeated within 2 weeks.
- Only post types marked on in `estrategia.md`.
- Format: only formats marked on in `estrategia.md` that fit the post type (formats catalog, "Fits post types"). Where `estrategia.md` names a format to lean on, pick it wherever it fits. No format more than 2 slots in a row unless only one fits.
- Template: the template for that format × post type in `modelos.md`, or "to build: <format> × <post type>". Reels need no Canva template: write "reel". Photo posts and photo carousels need none either: write "foto". A newsletter needs none: write "newsletter". For a photo slot's idea, suggest from unused photos in `departamentos/conteudo/fotos.md` when it exists.
- Spread the topics: every topic appears before any topic appears a third time.
- **Newsletter slots,** only when the newsletter is on in `estrategia.md`: on its own cadence, day and time (they don't take a post slot and don't count toward one post a day). Each gets a topic, format `newsletter` and a newsletter format from the library's newsletter catalog (no format twice in a row; the default one-idea letter fills the gaps), and every fourth or fifth is marked an offer issue as the strategy says. The idea is a suggestion only: the issue starts from her material.
- **Newsletter-led cycles,** when the strategy says the newsletter leads the theme: a cycle is one newsletter slot plus the post slots until the next one. The newsletter slot gets the cycle's topic, and every post slot in that cycle gets the same topic, with post types and formats still rotating inside the cycle; their idea cell says `da newsletter N`. The topic rules apply between cycles instead of between posts: no cycle topic twice in a row, every topic before any a third time. The newsletter row also gets its write-by date, 2 days before it's sent.
- First 2 weeks: prefer format × post type pairs that already have a template, so new templates have lead time.
- Match unused ideas from `ideias.md` to slots first (by topic, then type). Where none fits, write one suggested angle, marked "sugestão", following the idea rules in `estrategia.md` (what the reader gets, never technical).
- Use the last 4 posts in `calendario.md` for the "in a row" and "within 2 weeks" checks across the plan boundary.

### Refresh (keep the slots, change one thing)
When asked to refresh the current plan for one thing (e.g. "add formats to the plan", or conteudo-post asking to swap one slot's format), keep its slots, topics, post types and ideas exactly as approved, change only what was asked, and show the result at the gate. The approved version moves under Planos anteriores when the refresh is written.

### Refresh: shift after a missed slot
When conteudo-post moved a missed post onto the next slot (or she asks to shift the plan): every `planejado` slot from that point moves one slot later in the cadence, keeping its topic, post type, format, template and idea. The plan keeps its 4 weeks: the last slot moves past the horizon and goes to the top of the next plan. Recompute the template build-by dates (3 days before the first slot that uses each). Re-check "no topic twice in a row" and "no post type within 2 weeks" across the shifted slots and say if one now breaks. Show it at the gate as a refresh.

### Step 3 — Modelos a criar
- List every format × post type in the plan whose template is "to build", with a build-by date 3 days before its first slot.
- **Fotos para tirar:** for each photo slot with no fitting unused photo in `departamentos/conteudo/fotos.md`, one line: what to photograph, where or how (phone, light, angle, in plain words), and for which post. 5-10 lines at most; real things she can shoot this week. When she only asks "que fotos eu tiro", run just this from the current plan and write it.

### Step 4 — Gate
Show the plan as a table: post # · date · topic · post type · format · template · idea (or sugestão). Then the templates to build and the photos to take.

> "O plano está bom? Diga **sim**, ou me diz o que mudar."

Apply edits exactly, re-show, wait for sim.

### Step 5 — Write
On sim:
1. `plano.md`: create it if missing (header: "# Plano de conteúdo: <business>" and one line on how it works). Move the previous current plan, if any, under `## Planos anteriores` with its dates. Write the approved plan under `## Plano atual (<first date> a <last date>)`, columns: # · data · horário · tema · tipo de post · formato · modelo · ideia · status (`planejado`). Keep any slot's status other than `planejado` as it is. Then `### Modelos a criar` and `### Fotos para tirar`.
2. Department brief: set Próximo passo to the next unscheduled slot ("Post N, <day date>, <time>: <topic> × <post type>, <format>. Diga \"próximo post\"."), or "Criar o modelo <format> × <post type> até <date>. Diga \"cria o próximo modelo\"." if one is due first. In a newsletter-led cycle whose issue isn't written yet, the newsletter comes first: "Escrever a newsletter N até <write-by date>. Diga \"escreve a newsletter\"." Update Estado atual with its date and one line on the plan, and `atualizado:`. Touch nothing else; mention it in one short line.
3. Receipt and milestone (below).

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-plano | planned / refreshed / shifted / draft-not-approved | <first date> to <last date> · posts <first #>-<last #> · templates to build: <list or none>`

## Milestone

Each approved run: hand /contexto one line for `contexto/conteudo.md`:
`Plano de conteúdo de <first date> a <last date> aprovado: <N> posts. Próximo: <the brief's new Próximo passo>. Modelos a criar: <list, ou nenhum>.`

## What this skill never does

- Writes `plano.md` without an explicit sim.
- Re-plans or moves a slot that's already scheduled in MCM or the calendar. A shift after a missed slot moves only `planejado` slots.
- Edits `estrategia.md`, `calendario.md`, `ideias.md`, `modelos.md`, `notas-da-biblioteca.md`, the shipped library, or anything in `contexto/`. It only reads them.
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Invents topics, switches post types or formats on, or presents a suggested angle as decided.
- Drafts copy, designs, builds templates or schedules posts.
- Deletes a past plan — it moves under Planos anteriores.

## When to refuse

- No `estrategia.md`, or one without topics or post types — "Ainda não tem estratégia de conteúdo com temas, então não tem de onde planejar. Quer montar primeiro?" (the plan fills a strategy, it doesn't make one)
- No cadence or slot time in `estrategia.md` — "A estratégia ainda não diz quando você posta. Vamos definir isso primeiro." (no slots to fill; offers conteudo-estrategia on sim)
- A request to plan more than 4 weeks — "O plano é de 4 em 4 semanas; a gente planeja as próximas quando estiver acabando."

## Failure modes

- **Fewer topics or post types than the rotation rules need** (e.g. 2 topics) — relax "spread the topics" first, then "within 2 weeks"; never relax "no topic twice in a row" unless only 1 topic exists. Say which rule was relaxed.
- **Calendar and plan disagree** (a planned slot already scheduled with something else) — the calendar wins; re-number and say so.
- **Catalog missing a post type that the strategy lists** — plan it with template "to build" and flag it.
- **No format that's on fits a post type** — say so and leave the slot's format blank for her to pick at the gate; never switch a format on.
- **Department brief missing** — write `plano.md` only, skip the brief, say so.
- Prefer doing less: when unsure, stop at the gate and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already written (`plano.md`, brief lines, receipt) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): read the files and build the draft plan, then write only one receipt line marked `draft-not-approved`. Never write `plano.md` or the department brief without her sim.

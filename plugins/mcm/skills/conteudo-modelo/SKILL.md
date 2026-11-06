---
name: conteudo-modelo
description: "Cria um modelo de design no Canva para os posts dela — um formato para um tipo de post, como um carrossel ilustrado para posts de Vazamento — primeiro o layout, depois o design no Canva com diagramas nativos, depois o guia de preenchimento, com o sim dela em cada etapa. Quando ela diz \"/conteudo-modelo\", \"cria o próximo modelo\", \"cria o modelo ilustrado\", \"faz um modelo pro post 5\", quando o plano tem um modelo com prazo, ou quando um post para porque o modelo ainda não existe."
---

# conteudo-modelo — one Canva template, format × post type

Builds the templates conteudo-estatico fills. A template is one format × one post type (e.g. illustrated carousel × Leak). It is built once, the first time the plan schedules that pair, and copied for every post after.

It does one thing: **build one Canva template and its fill guide.** It never makes posts, writes copy for a real post, or changes the plan beyond its template cells.

Speak to her in plain, warm Brazilian Portuguese. Say "o modelo", "o layout", "o plano"; never file names, "skill", "API", "token" or a command name. To her, placeholders are "os espaços onde entram as palavras de cada post".

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. The shared reference files ship with the plugin next to this skill's folder: `../conteudo-estrategia/library.md` (the strategy library), `../conteudo-estrategia/playbook.md` (the copy playbook) and `../conteudo-instalar/guides.md` (Guia B: hand fixes in Canva).

1. `departamentos/conteudo/plano.md` — "Modelos a criar": what's due, by when, and which slots use it.
2. `departamentos/conteudo/modelos.md` — the templates that exist, their Canva IDs and fill guides.
3. `departamentos/conteudo/estilo-da-marca.md` — color roles, font roles, logo; `sobre-mim/marca.md` when it exists, for the logo files.
4. `departamentos/conteudo/estrategia.md` — which formats and post types are on.
5. `../conteudo-estrategia/library.md` — the format and post type definitions; then `departamentos/conteudo/notas-da-biblioteca.md`, if it exists.
6. `../conteudo-estrategia/playbook.md` — structure per post type (slide count, what each slide holds).
7. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.
8. Canva: the existing TEMPLATE designs, read only, to pick the one to copy.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Two gates, in order: layout, then design. Nothing is built in Canva before the layout gets a sim; nothing is committed, titled TEMPLATE or written to modelos.md or plano.md before the design gets a sim. Silence or an edit request is not a sim."

> "Never edit an existing TEMPLATE design. Always build on a copy."

> "Diagrams are native Canva shapes, lines and text in brand colors — no AI-generated images, no stock illustrations."

> "Every placeholder is a unique token in square brackets ([HOOK], [POINT 1 TITLE]), so conteudo-estatico can fill it with find-and-replace."

> "Only formats and post types that are on in the strategy and defined in the library or her library notes."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 1 — Pick the template
- The first line in the plan's "Modelos a criar" not marked built, or the template she names.
- Say in one line: "Criando o modelo <format> para posts de <post type>, prazo <date>, para os posts <N, M>."
- If an existing template can serve with no new layout (same format, same structure), say so and recommend reusing it instead of building.

### Step 2 — Layout (gate 1)
- From the playbook's structure for the post type and the library's format definition, draft the template slide by slide, as one table: slide · what it holds · tokens · which regions are in the accent color · diagram (if any) · light or dark.
- Diagrams are a fixed skeleton per post type, built from rounded boxes, simple icons (SVG paths) and arrows, with label tokens ([STEP 1], [BREAK]). Name the skeleton in one line (e.g. Leak: lead → step → step, a break marked between two steps).
- Recommend which existing template to copy and why (fonts and logo carry over; fonts can't be set from here).
- Note what will need a hand fix (e.g. a new text box Canva adds without the brand font).

> "O layout está bom? Diga **sim**, ou me diz o que mudar."

Apply edits exactly, re-show, wait for sim.

### Step 3 — Build in Canva
- `copy-design` the chosen template; title the copy "DRAFT - <Format> - <Post type>".
- Open an editing transaction and read every page.
- Restructure to the approved layout: add, reorder or delete pages; reposition, resize, recolor or delete elements; set page backgrounds from the brand-style color roles.
- Text: reuse existing styled text elements wherever possible (move, resize, `find_and_replace_text` with the tokens). Use `add_text` only where no styled element can serve, and list each one as a hand fix.
- Accent regions: keep the template's two-region pattern (a light or dark region + an accent region) so conteudo-estatico can move where the accent starts. Never recolor part of a one-color text box with `format_text`.
- Diagrams: `insert_shape` for boxes and icons (paths use only M/L/H/V/C/S/A/Z), lines with arrow markers connected to the boxes, label tokens inside. Brand colors only. Group each diagram.
- Check every slide's thumbnail: overflow, collisions, text off the canvas, arrows not meeting their boxes, a box that jumped after a resize. Fix by resizing or repositioning.

### Step 4 — Design (gate 2)
- Send the previews, and list the hand fixes only she can do in Canva (fonts on new text, logo placement, anything that can't be styled from here), with Guia B's clicks.

> "O design está bom? Diga **sim** que eu salvo, ou me diz o que mudar."

- On sim: commit the transaction **immediately** (open transactions expire), then retitle to "TEMPLATE - <Format> - <Post type>".
- If she then makes the hand fixes in Canva, re-read the design before Step 5 so the fill guide matches.

### Step 5 — Write
On the design sim:
1. `modelos.md`: add one row (template, Canva ID, format, slides, use for) and a fill guide under it: the token map by slide, where the accent starts in each two-region text, how to fill the diagram labels, light or dark, hand fixes still open.
2. `plano.md`: in the current plan, set the Modelo cell of each slot this template serves; in "Modelos a criar", mark the line built with the date and Canva ID. Touch no other cell.
3. Department brief: if the next post needed this template, set Próximo passo to that post ("Post N, <day date>, <time>: <topic> × <post type>. Diga \"próximo post\"."); otherwise leave Próximo passo as it is. Update Estado atual with today's date and one line, and `atualizado:`. Mention it in one short line.
4. Receipt and milestone (below).

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-modelo | layout-approved / built / stopped-at-<gate> / draft-not-approved | <format> × <post type> · Canva <design ID> · serves posts <N, M> · hand fixes: <list or none>`

## Milestone

Each template built: hand /contexto one line for `contexto/conteudo.md`:
`Modelo criado: <format> × <post type> (Canva <design ID>), atende os posts <N, M>. Em aberto: <ajustes à mão, ou nada>.`

## What this skill never does

- Builds in Canva before the layout gets a sim, or commits, titles TEMPLATE, or writes files before the design gets a sim.
- Edits an existing TEMPLATE design.
- Uses AI-generated images or stock illustrations for diagrams.
- Writes copy for a real post, drafts captions, or schedules anything — that's conteudo-estatico.
- Edits `estrategia.md`, `estilo-da-marca.md`, `calendario.md`, `ideias.md`, `posts/`, `sobre-mim/`, the shipped library, playbook or guides, or anything in `contexto/` (milestones go through /contexto).
- Changes `plano.md` beyond the Modelo cells of the slots it serves and its line in "Modelos a criar".
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Deletes Canva designs or files. A draft without a sim stays titled DRAFT for her to keep or delete.
- Builds more than one template per run.

## When to refuse

- A format or post type that's off in the strategy, or missing from the library — "Esse não está ligado na sua estratégia de conteúdo. Quer ligar primeiro?" (only what's on; offers conteudo-estrategia on sim)
- A request to edit an existing TEMPLATE in place — "Eu crio numa cópia; o original fica como está." (never edit a template)
- A request to skip the layout step — "Uma olhada no layout primeiro; é fácil mudar antes de criar qualquer coisa."
- A request for AI-drawn or stock illustrations — "Os diagramas são feitos com formas do Canva, pra continuarem editáveis e cada post poder preencher."
- Canva not connected — "O Canva não está conectado agora, então não consigo criar o modelo." Stop after the layout gate.

## Failure modes

- **No closer template to copy** — copy the nearest one anyway for fonts and logo; more of the build becomes hand fixes; say so at the layout gate.
- **A Canva operation is rejected** (e.g. a shape path it won't take) — simplify the shape once; if it still fails, leave it as a hand fix.
- **Canva transaction expired before commit** — open a new transaction, re-apply only the approved edits, re-show the previews, commit on sim. Never claim it saved.
- **Canva 409 / `polled_too_early`** — wait and retry once; then report and stop.
- **`plano.md` missing or has no "Modelos a criar"** — build the named template; skip the plan writes; say so.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, commit no open Canva transaction. Report what was already done (draft design ID, files written) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): pick the template and draft the layout table, then write only one receipt line marked `draft-not-approved`. Never touch Canva, `modelos.md`, `plano.md` or the brief.

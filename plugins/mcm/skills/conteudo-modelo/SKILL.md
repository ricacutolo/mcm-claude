---
name: conteudo-modelo
description: "Cria o design de onde saem os posts dela: um modelo no Canva — um formato para um tipo de post, como um carrossel ilustrado para posts de Vazamento — primeiro o layout, depois o design no Canva com diagramas nativos, depois o guia de preenchimento; ou, sem o Canva, o visual dela: as cores, as fontes e os padrões de slide com que o Claude desenha os posts dela, a partir de posts que ela gosta. O sim dela em cada etapa. Também guarda as referências dela, os posts e designs que ela gosta, numa lista contínua. Quando ela diz \"/conteudo-modelo\", \"cria o próximo modelo\", \"faz outro modelo\", \"vamos criar uns modelos\", \"cria o modelo ilustrado\", \"faz um modelo pro post 5\", \"configura o meu visual\", \"atualiza o meu visual\", \"salva como referência\", \"guarda nas minhas referências\", \"referência:\", quando o plano tem um modelo com prazo, ou quando um post para porque o modelo ainda não existe."
---

# conteudo-modelo — one Canva template, format × post type

Builds the templates conteudo-estatico fills. A template is one format × one post type (e.g. illustrated carousel × Leak). It is built once, the first time the plan schedules that pair, and copied for every post after.

It does one thing: **build the design source her posts are filled from**: one Canva template and its fill guide, or, when she designs without Canva, her look (`visual.md`, below). It also keeps the list both are built from: her references (`referencias.md`, below). It never makes posts, writes copy for a real post, or changes the plan beyond its template cells.

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
9. `departamentos/conteudo/visual.md`, if it exists (her look, below).
10. `departamentos/conteudo/referencias.md`, if it exists (her references, below): the rows for a look or a template.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Two gates, in order: layout, then design. Nothing is built in Canva before the layout gets a sim; nothing is committed, titled TEMPLATE or written to modelos.md or plano.md before the design gets a sim. Silence or an edit request is not a sim."

> "Never edit an existing TEMPLATE design. Always build on a copy."

> "Diagrams are native Canva shapes, lines and text in brand colors — no AI-generated images, no stock illustrations."

> "Every placeholder is a unique token in square brackets ([HOOK], [POINT 1 TITLE]), so conteudo-estatico can fill it with find-and-replace."

> "Only formats and post types that are on in the strategy and defined in the library or her library notes."

> "Her look is hers: built from her own posts, her brand and posts she likes, read for feel. Never copied from another brand or creator."

> "A reference capture is approved by the request itself. It appends one row to referencias.md and nothing else."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 1 — Pick the template
- **A reference** ("salva como referência", "referência: …", a post or screenshot she sends to keep): go to **Reference capture** below; no other step runs.
- **Her look** ("configura o meu visual", "atualiza o meu visual", the content setup without Canva, or no Canva connected): go to **Her look** below instead of Steps 2-5.
- The first line in the plan's "Modelos a criar" not marked built, or the template she names.
- Say in one line: "Criando o modelo <format> para posts de <post type>, prazo <date>, para os posts <N, M>."
- If an existing template can serve with no new layout (same format, same structure), say so and recommend reusing it instead of building.

### Step 2 — Layout (gate 1)
- From the playbook's structure for the post type and the library's format definition, draft the template slide by slide, as one table: slide · what it holds · tokens · which regions are in the accent color · diagram (if any) · light or dark.
- Diagrams are a fixed skeleton per post type, built from rounded boxes, simple icons (SVG paths) and arrows, with label tokens ([STEP 1], [BREAK]). Name the skeleton in one line (e.g. Leak: lead → step → step, a break marked between two steps).
- Her references marked for templates (or for this format), read for feel: say in one line what the layout takes from them.
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

### Her look (without Canva)
For a client who designs without Canva: Claude makes her slides itself from `visual.md` (conteudo-estatico's Step 4), and she changes them by telling Claude in the chat. Two gates, the same as a template: the look's table first, then sample slides.
1. **Read:** 3-5 posts or slides she likes (her own first; screenshots or links), her references marked for her look, `sobre-mim/marca.md` and `estilo-da-marca.md`, her site if she has one. Posts she sends now are saved as references first (Reference capture), so the next update has them. Nothing to show and no idea yet how she wants her posts to look: ask for 3-5 posts she likes from anyone, any field ("Me manda alguns posts que você gosta, de qualquer pessoa; eu pego a sensação, não o design"). Still nothing: build from her brand alone, and say she can update it any time ("atualiza o meu visual").
2. **Draft the look (gate 1):** one table, in `visual.md`'s shape (below): size, colors with their roles, fonts (free Google Fonts, the closest match to what she uses), what every slide carries (margins, kicker, footer, page marks, logo), and the patterns (one line each). "Esse é o seu visual? Diga **sim**, ou me diz o que mudar."
3. **Sample slides (gate 2):** render one slide of each pattern at its size with placeholder text in her language, the same way conteudo-estatico renders posts, and send them. "Isso tem a sua cara? Diga **sim** e eu salvo o seu visual, ou me diz o que mudar."
4. **Write, on sim:** `visual.md`; in `modelos.md`, one row per image format on, template `visual`, with each slide's pattern in its fill guide; the brief as in Step 5. Updating an existing look: show what changes, side by side, and keep the old one as `visual-<data>.md`.

**`visual.md`:**

```markdown
# O visual dela

Como o Claude desenha os posts dela quando desenha ele mesmo. Feito em AAAA-MM-DD a partir de: <posts dela / posts que ela gosta / a marca dela>. A marca em si continua em sobre-mim/marca.md.

Tamanho: 1080×1350 (4:5) | 1080×1440 (3:4)

## Cores
| Papel | Hex | Usado em |
|---|---|---|
| Fundo | | a maioria dos slides |
| Título | | títulos |
| Destaque | | palavras-chave, números, chamada pequena, seta |
| Texto | | texto corrido |
| Suave | | texto secundário, rodapé |

## Fontes (Google Fonts)
- Título: <fonte, peso>
- Texto: <fonte, peso>
- Citação: <fonte, estilo>

## Todo slide
- <margens, chamada pequena, rodapé, marcas de página, seta, logo: onde, ou nenhum>

## Padrões
| Padrão | O que leva |
|---|---|
| Capa | |
| Texto | |
| Lista | |
| Citação | |
| Foto | |
| Fechamento | |

## Nunca
- <o que não combina com o visual dela>
```

### Reference capture
Her references are one running list of posts and designs she likes, for her look, her templates and her photos. She sends them any time, from inside any work.
- Triggered by "salva como referência", "guarda nas minhas referências", "referência: …", or a post, screenshot or link she sends to keep for later.
- Keep the file: a screenshot or image goes to `04. Brand/Referências` in her Drive (`departamentos/conteudo/referencias/` in her folder when her Drive isn't organized), named `AAAA-MM-DD-<nome-curto>`. A link is kept as the link.
- Append one row to `departamentos/conteudo/referencias.md` (create it with the shape below if missing): next #, today's date, the file or link, what she likes in her words (ask in one line if she didn't say: "O que você gosta nele?"), what Claude reads in it for feel (layout, density, color, type, tone; one line, never "copy this"), and what it's for (visual, modelos, fotos, or qualquer).
- Confirm in one line: "Salvo como referência #N (<para>)." Then return to whatever was happening. When her look exists and the reference changes something in it, add: "Diga \"atualiza o meu visual\" quando quiser incluir." Nothing else is changed.
- Receipt line. No milestone for a capture.

**`referencias.md`:**

```markdown
# As referências dela

Posts e designs que ela gosta, para o visual, os modelos e as fotos dela. Lidos pela sensação, nunca copiados. Os arquivos ficam em 04. Brand/Referências.

| # | Data | Arquivo ou link | O que ela gosta (nas palavras dela) | A sensação | Para |
|---|---|---|---|---|---|
```

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-modelo | layout-approved / built / look-saved / reference-saved / stopped-at-<gate> / draft-not-approved | <format> × <post type> · Canva <design ID>, or look, or reference #N · serves posts <N, M> · hand fixes: <list or none>`

## Milestone

Each template built: hand /assunto one line for `contexto/conteudo.md`:
`Modelo criado: <format> × <post type> (Canva <design ID>), atende os posts <N, M>. Em aberto: <ajustes à mão, ou nada>.`

## What this skill never does

- Builds in Canva before the layout gets a sim, or commits, titles TEMPLATE, or writes files before the design gets a sim.
- Edits an existing TEMPLATE design.
- Uses AI-generated images or stock illustrations for diagrams.
- Writes copy for a real post, drafts captions, or schedules anything — that's conteudo-estatico.
- Edits `estrategia.md`, `estilo-da-marca.md`, `calendario.md`, `ideias.md`, `posts/`, `sobre-mim/`, the shipped library, playbook or guides, or anything in `contexto/` (milestones go through /assunto).
- Changes `plano.md` beyond the Modelo cells of the slots it serves and its line in "Modelos a criar".
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Deletes Canva designs or files. A draft without a sim stays titled DRAFT for her to keep or delete.
- Builds more than one template per run, or a look and a template in the same run.
- Copies another brand's or creator's design into her look.
- Changes her look or a template because of a reference; a capture only appends its row.

## When to refuse

- A format or post type that's off in the strategy, or missing from the library — "Esse não está ligado na sua estratégia de conteúdo. Quer ligar primeiro?" (only what's on; offers conteudo-estrategia on sim)
- A request to edit an existing TEMPLATE in place — "Eu crio numa cópia; o original fica como está." (never edit a template)
- A request to skip the layout step — "Uma olhada no layout primeiro; é fácil mudar antes de criar qualquer coisa."
- A request for AI-drawn or stock illustrations — "Os diagramas são feitos com formas do Canva, pra continuarem editáveis e cada post poder preencher."
- Canva not connected — "O Canva não está conectado agora, então não consigo criar o modelo. Posso desenhar os seus posts eu mesmo a partir do seu visual, ou a gente conecta o Canva antes." (her look, or the content setup's Canva step)
- A request to copy another brand's or creator's look — "Eu levo o que você gosta nele, a sensação, pro seu próprio visual; não copio." (her look is hers)

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

With nobody watching (scheduled or non-interactive): pick the template and draft the layout table, then write only one receipt line marked `draft-not-approved`. Never touch Canva, `modelos.md`, `plano.md`, `referencias.md` or the brief.

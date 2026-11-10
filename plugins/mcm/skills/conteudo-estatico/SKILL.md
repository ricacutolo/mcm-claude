---
name: conteudo-estatico
description: "Faz um post de imagem — carrossel, carrossel ilustrado, post de texto, post de foto ou carrossel de fotos — da ideia ao agendamento: a ideia, o texto, o design no Canva (ou as fotos dela, preparadas) e o agendamento no MCM, com o sim dela em cada etapa. Normalmente começa pelo próximo post do plano; também quando ela diz \"/conteudo-estatico\", \"faz esse carrossel\", \"faz o carrossel do post 5\", \"cria o próximo carrossel\", \"vamos fazer um post de texto\", \"posta essa foto\", \"faz um post com essas fotos\"."
---

# conteudo-estatico — one image post, idea to scheduled

She leads with her voice and her ideas; this skill drafts, designs and schedules around them. It never posts on its own.

It does one thing: **take one image post from idea to scheduled.** It is usually started by conteudo-post with a slot from the plan. Started directly by name, it first runs conteudo-post's Steps 1-2 (find the slot, the connection warning, the missed-slot rule) and then continues here. Reels belong to conteudo-video.

Speak to her in plain, warm Brazilian Portuguese. Say "o texto", "o design", "o calendário", "o brief do departamento"; never file names, "skill", "API" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. The shared reference files ship with the plugin next to this skill's folder: `../conteudo-estrategia/playbook.md` (the copy playbook) and `../conteudo-estrategia/library.md` (the strategy library).

1. The slot conteudo-post passed: post number, date and time (and the original slot if it was missed), topic, post type, format, template, idea.
2. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.
3. `departamentos/conteudo/estrategia.md` — who we post for, which layers are on, topics, post types, idea rules, cadence and platforms, CTA, wedge.
4. `departamentos/conteudo/plano.md` — the slot's row and the next `planejado` slot.
5. `departamentos/conteudo/calendario.md` — what's scheduled and published.
6. `departamentos/conteudo/ideias.md` — the idea backlog.
7. `departamentos/conteudo/modelos.md` and `estilo-da-marca.md` — which template, which color and font roles. `sobre-mim/marca.md` when it exists, for her logo files.
8. `departamentos/conteudo/ghl.md` — location, user and account IDs (not secret).
9. The post's own `departamentos/conteudo/posts/<folder>/post.md`, if it exists — to resume.
10. `sobre-mim/sobre-mim.md` — only her time zone.
    Photo formats also: `departamentos/conteudo/fotos.md` (her photo library index, below) and her Google Drive folder **Fotos de conteúdo**; for a generated image, `../conteudo-estrategia/image-prompts.md` and `departamentos/conteudo/estilo-de-foto.md` (below).
11. Only when recommending ideas or drafting copy (Steps 2-3):
    - the business file of the area in play (`sobre-mim/negocio.md`, or `negocio-<area>.md` per /sistema's **Areas**) — the offer, who it's for, the wedge, current positioning. It evolves; always read the current one, never a remembered copy.
    - `../conteudo-estrategia/playbook.md` — rules, awareness levels, hooks, frameworks, structure per post type, caption formula, CTA by layer, the 4-point check.
    - `departamentos/conteudo/swipe.md` — lines that worked for her, if it exists.
    - `../conteudo-estrategia/platforms/<platform>.md` for each platform on in `estrategia.md` — its formats and caption rules. Only those.
    - `sobre-mim/escrita.md` — her voice.

Never read or print `departamentos/conteudo/.env`. The script reads it; this skill never does.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Nothing is scheduled or published without an explicit sim at the schedule gate. A yes to the copy or the design is not a sim to schedule."

> "Three gates, in order: copy, design (photos, for a photo post), schedule. Each waits for an explicit sim (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a sim."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "Her point of view leads. Claude may recommend an idea and angles; it never invents a stance she hasn't taken and never presents a recommendation as decided."

> "Never edit a TEMPLATE design. Always work on a copy."

> "A generated image never stands in for her work, her customers, her results or her. It shows the reader's world, an object or an idea, and the post's notes say it was generated."

> "A missed slot moves; it is never skipped silently or doubled up. Never two posts on the same day."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 1 — The post and where it stands
- Use the slot conteudo-post passed. If the slot's format is a reel or video: "O post N é um reel; ele é feito nas etapas de vídeo. Quer que eu comece?" and hand back to conteudo-post on sim.
- If `posts/<folder>/post.md` exists, read its Etapa/Status table and resume at the first step not done.
- New post: create `departamentos/conteudo/posts/post-NN-<slug>/post.md` in the shape below, with the slot's topic, post type, format and template — the slug once the idea is picked.
- Photo post and photo carousel need no template (the plan says "foto"); `## Slides` in `post.md` lists the photos in order instead.
- If the slot's template is "to build": stop. "O post N precisa do modelo de <post type>, que ainda não foi criado. Quer criar primeiro, ou trocar o tipo de post desse horário?" Building it is conteudo-modelo, run on sim. Never improvise a template.

**`post.md` shape:**

```markdown
# Post N: <short title, once the idea is picked>

Horário: <day date time> · <topic> × <post type> · <format> · modelo: <name>

| Etapa | Status |
|---|---|
| Ideia | |
| Texto | |
| Design | |
| Agendamento | |
| Resultados | |

## A direção dela
- <what she said she wants this post to say or avoid>

## Slides ([colchetes] = palavras em destaque)
1. ...

## Legenda

## Notas da execução
- <calls made without asking, her edits at each gate, size changes, hand fixes>

## Slides finais (links permanentes)
```

### Step 2 — Idea
- **Her material and a suggestion, in one message.** The slot gives the topic and post type. Ask what she has for it and recommend at the same time: "Tem alguma coisa sobre <topic> pra esse post — uma ideia, uma história, algo que um cliente perguntou? Se não, eu faria assim: <the slot's idea from `ideias.md`, or the plan's suggestion>. Ou: <angle 2> · <angle 3>." Her material wins: shape it into the slot's post type. A suggestion she takes still gets one question for her own angle ("Me conta uma vez em que você viu isso acontecer?").
- Ideas follow the idea rules in `estrategia.md` and the rules in the playbook: what the reader gets, never technical, real things only. Read `negocio.md` for the offer, the audience and the wedge.
- Photo formats: the idea starts from a photo she has. Sync the photo library first (below), then recommend the photo (photo post) or 2-10 in order (photo carousel) that fit the slot's topic × post type, unused ones first, with one line each on why; she picks, or brings others. People in a photo: customers only if the strategy says customer photos are OK and the library says they agreed.
- She picks. If she changes the topic or post type, say the plan will show it changed and note it in `post.md`. Record topic, post type, idea and who chose it in `post.md`.

### Step 3 — Copy (gate 1)
- Read the playbook and her voice. Choose the awareness level for the post type, pick a hook pattern, use the structure for the post type and the caption formula, and the CTA for the layer that's on. That's the main caption. For each platform on whose file gives it its own caption (LinkedIn), write that caption too, from the same idea, by its file's rules.
- Photo formats: no slide text. The copy is the caption(s), the hook in the first line, and for a photo carousel the order of the photos.
- For the 5-slide tips list: slide 1 hook (accent color on the words that sting) + "Arrasta pro lado →"; slides 2-4 one point each (number, short title, 2-4 lines, the turn in the accent color); slide 5 reframe line, promise in the accent color, the CTA.
- Run the playbook's 4-point check (hook, what they get, plain, CTA) and fix what fails before showing.
- Show slides and every caption (labeled by platform), accent words in [brackets], and one line naming the hook pattern used.
- **Gate:** "O texto está bom? Diga **sim**, ou me diz o que mudar." Apply edits exactly; re-show; wait for sim. Record the approved copy, captions (one per platform that has its own, labeled) and hook pattern in `post.md`.

### Step 4 — Design (gate 2)
- **Photo formats skip the Canva steps in this section.** Get the picked photos from her library (download from Drive), or from this chat if she just dropped them. **No photo that fits?** Offer two ways, recommending one: take it (the plan's Fotos para tirar says what; she adds it to the library and we pick up here), or generate it. Generated: follow `../conteudo-estrategia/image-prompts.md` and her `estilo-de-foto.md`, with a calibration round first if her style isn't settled; make 2 options per photo, she picks. Canva hands back an image stored in her Canva, not a file: copy her `TEMPLATE - Photo - full frame`, put the picked image in its one image element, export JPG 1080x1440, and download it into `photos/`. Note "gerada" in the run notes. A generated image never goes into her photo library, and never for a post about her work, her clients or her results. Check each: sharp, at least 1080 px wide, not a screenshot; say plainly which one fails and ask for another, never upscale. Crop to 1080x1440 (3:4) keeping the subject, convert to JPEG, remove location data, and save them in `posts/<folder>/photos/` as `01.jpg`, `02.jpg`…; never change her originals. Use whatever image tool her computer has (Python Pillow, `sips` on a Mac, or ffmpeg). Send the previews in order. **Gate:** "As fotos estão boas? Diga **sim**, ou me diz o que mudar." Then go to Step 5.
- Use the slot's template from `modelos.md`. Where a post type has a dark and a light version, alternate against the last published post.
- `copy-design` the template; title the copy `Post N - <hook>`. Record the new design ID in `post.md`.
- Open an editing transaction, read every page, and fill with `find_and_replace_text` on each placeholder region — it keeps each region's color and weight. To move where the accent color starts, empty a region and put the words in the next one; never recolor with `format_text` (it recolors the whole element). Font size changes with `format_text` are fine. `add_text` comes in unstyled — don't use it. Fonts can't be set from here.
- Check every slide's thumbnail: overflow, a heading wrapping into the big number, a word alone on the last line, text off the canvas, a text box that jumped after a resize. Fix by shrinking the font, resizing or repositioning the box. Keep body sizes the same across the point slides.
- Send the previews. List anything only a hand edit can do (the accent color on part of a one-color text box, fonts, logo) — `../conteudo-instalar/guides.md` Guia B has the clicks.
- **Gate:** "O design está bom? Diga **sim** que eu salvo, ou me diz o que mudar." On sim, commit the transaction **immediately** — open transactions expire.
- If she then edits by hand in Canva, that is fine: Step 5 re-reads the design before export.

### Step 5 — Schedule (gate 3)
- The date and time conteudo-post passed (the slot, or the new time for a missed slot), at least 1 hour out. Platforms and accounts from `estrategia.md` + `ghl.md`, and each platform's Scheduling section from its file. Times are in her time zone (from `sobre-mim/sobre-mim.md`, else ask once).
- If the time has slipped to under 1 hour away while we worked, it's now a missed slot: recompute with conteudo-post's missed-slot rule (`../conteudo-post/SKILL.md`, Step 2) and say the new time in one line. Never schedule two posts on the same day.
- If a connection in `ghl.md` has expired: stop here. "A conexão do <platform> venceu. Reconecte no Social Planner do MCM e me avisa quando terminar."
- **Gate:** show date and time (her time zone), platforms, captions, slide or photo count. "Pronto pra agendar? Diga **sim** que eu agendo." Wait for an explicit sim.
- On sim:
  1. Re-read the design so hand edits are in; export PNG 1080x1440, all pages. Photo formats: skip this and step 2; instead, from `departamentos/conteudo/`, run `bash scripts/media-to-ghl.sh posts/<folder>/photos/<NN>.jpg post-NN-<slug>-<NN>` for each photo in order (copy `scripts/media-to-ghl.sh` from `../conteudo-instalar/scripts/` first if missing); it prints one permanent MCM URL per photo.
  2. Run on her computer, from `departamentos/conteudo/`: `bash scripts/canva-to-ghl.sh posts/<folder> <export url 1> ... <export url N>`. It saves local copies to `posts/<folder>/slides/` and prints one permanent MCM URL per slide. Canva export links expire within hours — never schedule with them. If `scripts/canva-to-ghl.sh` is missing, copy it from `../conteudo-instalar/scripts/` first.
  3. MCM `create-post`: `accountIds` from `ghl.md`, `userId` from `ghl.md`, `type: post`, `status: scheduled`, `scheduleDate` in UTC, `instagramPostDetails: {type: post}`, `facebookPostDetails: {type: post}` when Facebook is in, `summary` = approved caption, `media` = the permanent URLs as `image/png` (photos: `image/jpeg`), in slide order. Idempotency key: `<location ID>-post-NN-<slug>-schedule`. This post carries the platforms that share the main caption. Each platform with its own caption gets its own `create-post`, as its file's Scheduling section says (same media, its caption, its own idempotency key).
  4. Verify with `get-posts` (body: `type: all` or `type: scheduled`, `accounts` as a comma-separated string, `skip`/`limit` as strings, dates bracketing the slot). The parent record may show `platform: google` until publish, and the list may show only the first image — ignore both; per-platform child posts are created at publish time.

### Step 6 — Close
- `post.md`: Design and Agendamento rows, design ID, permanent URLs, MCM post IDs (one per `create-post`), slot.
- Photo formats: `fotos.md`, the photos' `usada em`. Generated images: none in the library; `estilo-de-foto.md` only if she approved a style change.
- `calendario.md`: the post's row (date, `<topic> × <post type>`, format, idea, `Agendado <time>`); add the row if missing (create the file with `# Calendário de conteúdo` and the columns `# · data · post · formato · ideia · status` if needed). For a missed slot, the actual date and time, plus "(movido de <slot>, perdido)".
- `plano.md`: set this slot's Status to `agendado` — the Status cell only; the plan's other cells belong to conteudo-plano. For a missed slot: `agendado (movido para <day time>)`.
- `ideias.md`: mark the idea `usada: post N` if it came from there; add any new ideas she mentioned during the run as `não usada`.
- Department brief: set Próximo passo to the next `planejado` slot ("Post N+1, <day date>, <time>: <topic> × <post type>. Diga \"próximo post\"."). If fewer than 2 weeks of planned slots remain, the Próximo passo is "Planejar as próximas 4 semanas. Diga \"planeja o conteúdo\"." instead. Update Estado atual with its date and one line, and `atualizado:`. No approval needed; mention it in one short line.
- Receipt and milestone (below).
- Hand back to conteudo-post's Step 4 (stay one post ahead, and how she'll hear it went live) — also when she started this skill directly.

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-estatico | idea / copy-approved / design-approved / scheduled / stopped-at-<gate> | post N · <topic> × <post type> · design <ID> · GHL post <ID> · missed: yes/no`

## Milestone

Runs that reached a new stage: hand /contexto one line for `contexto/conteudo.md`:
`Post N <texto aprovado / design aprovado / agendado para <slot>>: <topic> × <post type>, <format>. Em aberto: <ajustes à mão, ou nada>.`

## Photo library

Her photos accumulate in one place, whenever she has them, with no post in mind: a Google Drive folder **Fotos de conteúdo** (the Drive app uploads straight from her phone). Claude keeps an index of it in `departamentos/conteudo/fotos.md`:

`# Biblioteca de fotos: <business>` and the columns `# · arquivo · onde · o que tem · pessoas · adicionada · usada em`. `onde` is the Drive file (or `chat` → saved to Drive); `pessoas` is nenhuma / ela / equipe / cliente (concordou: sim / não perguntado).

- **Sync** at a photo slot's idea step, or when she says she added photos: list the Drive folder, add each new file to the index with a short plain description of what's in it (look at it), and ask once, in one message, about any new photo with people she hasn't described ("Alguém nessas fotos é cliente? A pessoa concordou em aparecer?"). No folder yet: offer to create **Fotos de conteúdo** in her Drive and tell her to drop photos there from her phone.
- **Dropped in chat:** a photo she sends here for a post is also uploaded to the Drive folder and indexed, so it isn't lost.
- **Used:** after scheduling, write the post number in `usada em`. A used photo can be posted again only when she asks.
- Never delete or move her photos; the index is the only thing Claude writes.

## Photo style

Her look for generated images, calibrated with her over a few rounds (method in `../conteudo-estrategia/image-prompts.md`), kept in `departamentos/conteudo/estilo-de-foto.md`:

```markdown
# Estilo de foto: <business>

Status: calibrando (rodada N) | definido YYYY-MM-DD

## O visual
<one paragraph in plain words: what her generated images feel like>

## Prompt base
- Câmera: <e.g. phone photo, eye level, 35mm, shallow depth of field>
- Luz: <e.g. soft natural window light>
- Cor: <her palette as color words, from estilo-da-marca.md>
- Clima: <one or two words>
- Composição: vertical 3:4, <placement>

## Assuntos que funcionam
- <subject> — <why it fits her audience>

## Nunca
- <what she rejected, as a rule>

## Ferramenta
Canva generate-image, PORTRAIT_3_4

## Rodadas
| Data | O que testamos | O que ela disse | O que mudou |
|---|---|---|---|
```

Every change to this file is shown to her and written on her sim: it's her look.

## What this skill never does

- Schedules or publishes without an explicit sim at the schedule gate. Never sets `status: published` directly.
- Reads, prints, copies or asks for `.env` or the MCM key.
- Edits a TEMPLATE design, `estrategia.md`, `estilo-da-marca.md`, `modelos.md`, `ghl.md`, the shipped library or playbook, `sobre-mim/`, or anything in `contexto/` (milestones go through /contexto).
- Changes `plano.md` beyond the Status cell of the slot it scheduled.
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Improvises a template for a post type that has none.
- Makes a reel or any video post. Those go to conteudo-video.
- Invents her point of view, numbers or results, or presents a recommended idea as decided.
- Schedules with Canva export links (they expire).
- Deletes posts, designs, files or ideas. A dropped idea is marked `descartada`, not removed.
- Runs more than one post per run.
- Schedules two posts on the same day, or lets a missed slot pass without moving it.

## When to refuse

- No `estrategia.md` — "Ainda não tem estratégia de conteúdo. Quer montar primeiro?" (the post comes from a strategy; it doesn't make one)
- The slot's template is "to build" or missing — "O post N precisa do modelo de <post type>. Quer criar primeiro, ou trocar o tipo de post?" (never edit or improvise a template)
- Canva or MCM not connected — "O Canva não está conectado agora, então não consigo fazer o design." / "O MCM não está conectado agora, então não consigo agendar." Stop at the last step that can run.
- A request to post right now, skipping the gates — "Todo post passa pela aprovação do texto, do design e do agendamento."
- A request to schedule into a slot that's passed or under 1 hour away — "Esse horário já passou; eu postaria <new time>." (MCM needs lead time to stage the post)

## Failure modes

- **Started directly with no slot** — run conteudo-post's Steps 1-2 first; if there's still no slot, say so and offer to plan content.
- **Business file or playbook missing** — draft from `estrategia.md` and her voice only; say which file was missing.
- **Canva transaction expired before commit** — open a new transaction, re-apply only the approved edits, re-show the previews, commit on sim. Never claim it saved.
- **Canva 409 / `polled_too_early`** — wait and retry once; then report and stop.
- **Export download blocked (403)** — stop. "O seu computador ainda não acessa export-download.canva.com. Ele precisa entrar nos sites permitidos nas configurações do Claude." Nothing is scheduled.
- **Upload to MCM fails (401/403)** — stop. "A chave do MCM no arquivo de configurações da sua pasta de conteúdo está faltando ou não permite uploads." Never ask for the key in chat.
- **`create-post` 4xx** — report the message once; fix the one named field if it is clear (e.g. empty `userId` → `ghl.md`); otherwise stop. Never retry blindly — a duplicate post is worse than a late one.
- **Text overflow that can't be fixed from here** — leave it, list it as a hand fix at the design gate.
- **Connection token expired** (`ghl.md` expiry date passed, or MCM says so) — stop at schedule: "Reconecte o <platform> no Social Planner do MCM."
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes, commit no open Canva transaction, schedule nothing. Report what was already done (post folder, design ID, uploads, MCM post ID if any) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her at three gates, so it does not run unattended. With nobody watching (scheduled or non-interactive): read the files, write one receipt line naming the slot and the recommended idea (`draft, not approved`), and execute nothing else — no design copy, no upload, no post.

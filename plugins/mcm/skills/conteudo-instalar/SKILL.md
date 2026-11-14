---
name: conteudo-instalar
description: "Conduz a configuração da máquina de conteúdo em 20 etapas — o departamento Conteúdo, o Canva, a marca e os modelos dela, o MCM, o caminho de upload e a estratégia — com uma recomendação em cada etapa, fazendo o trabalho braçal por ela, retomando de onde ela parou. Quando ela diz \"/conteudo-instalar\", \"configura a máquina de conteúdo\", \"configura o meu conteúdo\", \"continua a configuração do conteúdo\", \"onde a gente está na configuração do conteúdo\", ou quando o próximo passo do departamento Conteúdo diz que a configuração está aberta."
---

# conteudo-instalar — ready for the first post

Gets her content machine ready: the Conteúdo department, Canva, her brand on the design templates, MCM, the upload path and the strategy. It walks the steps in order, opens every step with the answer we'd pick and why, decides small details for her and notes them, and picks up where it left off.

It does one thing: **get her content machine ready for its first post.** It never writes the strategy, plans posts or makes posts — it hands off to the skills that do.

Speak to her in plain, warm Brazilian Portuguese, in her voice rules from `sobre-mim/escrita.md`: plain words, nothing technical. Say "o Canva conectado ao Claude", "o seu MCM conectado ao Claude", "o arquivo de configurações da sua pasta de conteúdo"; never "connector", "MCP", "API", "token", file names, "skill" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. This skill ships two things in its own folder: `guides.md` (Guias 0 and B for Canva, C, D and E for MCM) and `scripts/` (the upload and transcription scripts copied into her content folder).

1. `departamentos/conteudo/configuracao.md` — progress and the resume point. If missing, this is a new setup.
2. `departamentos/conteudo/brief.md` — whether the department exists; its Próximo passo and Estado atual.
3. `departamentos/conteudo/estilo-da-marca.md`, `modelos.md`, `ghl.md` — if they exist, to know what's already filled.
4. `sobre-mim/marca.md` — her colors, fonts and logo files, if her brand kit exists.
5. `sobre-mim/cerebro-do-negocio.md` and `sobre-mim/escrita.md` — only to check they exist and are filled in. Never edited here.
6. `guides.md` — when a step points to one of its guides.

Never read or print `departamentos/conteudo/.env`. Step 19 checks only whether a key is set.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Every step opens with a recommendation: the answer we'd pick and why. She confirms or changes it. Small details get decided and noted, not asked."

> "Claude does the busywork. She only does what needs her hands (signing in, approving, pasting a key), and every one of those comes as numbered steps, one action each, with a direct link wherever one exists (**Clique aqui para abrir <a página> →**). If Claude can check something, it checks instead of asking her to report."

> "estilo-da-marca.md, modelos.md and ghl.md are Claude's reference notes: written without asking and mentioned in one line. What she decides in them (which templates, her newsletter details) is confirmed with her first."

> "Checks are read-only. A check never creates, edits, sends or connects anything."

> "Template rebrands are saved only after an explicit sim to the previews. Only her own fresh copies are edited, never a shared original, and never a template of her own beyond the placeholders she approved."

> "The MCM key goes into .env by her own hand. Never ask for it in chat, never read it, never print it."

> "The Conteúdo department brief is written only after her sim to it. Hand-offs (instalar, brand-kit-designer, conteudo-estrategia) run only on a sim."

> "configuracao.md, the receipt and the department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

## The steps

| # | Stage | Step | Done when | How |
|---|---|---|---|---|
| 1 | Home | Conteúdo department exists | `departamentos/conteudo/brief.md` exists | If missing → create it from **The Conteúdo department** below: one question (its area), the brief shown, written on sim. No interview: the content machine already knows what this department is |
| 2 | Home | Setup tracker | `configuracao.md` exists | Create it (format below) |
| 3 | Business | Business file filled in | `sobre-mim/cerebro-do-negocio.md` exists with offer, audience and pains | Missing → offer to redo instalar's business step (step 3; a completed install still runs "refazer etapa 3"), and run it on her sim. Thin → ask what's missing (at most 3 questions) and add the lines to `_sistema/pendentes.md` as items for `sobre-mim/cerebro-do-negocio.md`; done when they're written |
| 4 | Business | Voice captured | `sobre-mim/escrita.md` exists with real samples | Missing → offer to redo instalar's writing step (step 4; a completed install still runs "refazer etapa 4"), and run it on her sim. No samples → ask her for 2-3 things she wrote and add them to `_sistema/pendentes.md` as an item for `sobre-mim/escrita.md` |
| 5 | Canva | Canva account | she confirms | Guia 0. Recommend Free to start; skip Pro trials. Her plan never matters to the setup |
| 6 | Canva | Canva connected to Claude | `list-brand-kits` answers | She connects Canva in Claude's **Personalizar → Conectores** (Customize → Connectors) (**Clique aqui para abrir os Conectores →** `https://claude.ai/customize/connectors`); then check. If the check fails right after she connects, she starts a new conversation so the connection loads, and says "continua a configuração do conteúdo" |
| 7 | Brand | Her logo and colors | `sobre-mim/marca.md` exists, or she chose "later" | Ask first: "**Você já tem um logo e as cores da sua marca?**" **Sim** → "Coloca os arquivos do seu logo, e qualquer coisa que mostre as suas cores (um guia de estilo, um design antigo), na pasta **04. Brand** do seu Drive, ou anexa aqui. O seu site também serve: é só mandar o link." Then /brand-kit-designer in its **from her own brand** mode, run on her sim. **Não** → offer to make them now (/brand-kit-designer, about 15 minutes) or later. Later → the templates keep MCM's colors until she has hers; note it under "Decidido por ela". No Canva Brand Kit step: her colors go into the templates themselves (step 9) |
| 8 | Brand | Logo on her templates | her logo is placed on every template that has a logo spot | Claude places it, after steps 9, 17-19 are done: her light and color logo files (from `sobre-mim/marca.md`) go into her Canva (from her computer with `create-upload-url` once `www.canva.com` is an allowed site, or `media-to-ghl.sh` for a permanent link and `upload-asset-from-url`), then `update_fill` on each template's logo spot. Neither works → fallback: she drags her logo into one design Claude links her to (**Clique aqui para abrir →**), from her Canva Uploads; Claude reads its media ID from that design and places it everywhere. No logo yet (brand later) → step waits, nothing to do now |
| 9 | Templates | Her templates | every template she'll use is in her Canva, titled TEMPLATE, design ID known | Ask first: "**Você já tem modelos de post no Canva?** Comprados, feitos por você ou feitos pra você." **Sim** → she sends the links (or the names, and Claude finds them): see "Her own templates" below. Then: "Quer os cinco modelos do MCM também? **Sim, nas minhas cores** / **Sim, do jeito que estão** / **Não, os meus bastam**". **Não** → MCM's five, in her colors. MCM's five: "Carousel - Tips list (3 points)" (dark), "Carousel - Tips list (3 points) - Light", "Illustrated carousel - Leak", "Photo - full frame" (one page, one full-bleed image: generated images go through it to come out as a full-size file) and "Photo - headline" (one page: a full-bleed photo, a soft dark fade at the bottom and a headline on it). Rica shares them to her Canva email as "Can edit" (by hand: Canva can't share from here). Claude copies each one into her Canva itself (`copy-design`) and rebrands the copy (below); she does nothing but say yes. A shared design that doesn't show for her: ask Rica to share it to the email her Canva uses, and mark the step waiting. Then, optional: "**Tem algum post ou perfil com um visual que você adora?** Anexa prints ou manda os links." (see "Design references" below). Last, once all her templates are in: "Quer as fontes da sua marca nos seus modelos? Uns 2 minutos por modelo." Optional; Guia B with a link to each template |
| 10 | Templates | Brand style | `estilo-da-marca.md` written | Claude writes it from `sobre-mim/marca.md` (or MCM's colors when her brand is "later"), the templates and her references, without asking; one line: "Anotei como as suas cores e os seus modelos são usados." |
| 11 | Templates | Template index | `modelos.md` has every template set up here | Claude writes the rows and fill guides in conteudo-modelo's shape: one row per template (template, Canva ID, format, post type, slides, use for) with its fill guide under it, hers and MCM's side by side; no approval, one line as in step 10 |
| 12 | MCM | Her MCM connected to Claude | the MCM connection lists her business (sub-account) | Guia C: she connects MCM from the plugin's **Conectores** (Connectors) tab, signs in, picks her business and approves the permissions, social posts read and write included; she starts a new conversation so the connection loads; then check. The plugin's connector doesn't show or fails → Guia C's fallback (custom connector). Record her location ID and her MCM app address (the `uiUrl` from `fetch-media-content`, its domain) in `ghl.md`: the links in steps 13 and 19 are built from them |
| 13 | MCM | Platforms and social accounts | `get-account` lists every platform she'll post on | Recommend her platforms first, from each `../conteudo-estrategia/platforms/` file's "When to recommend it" (Instagram; Facebook when she has a Page; LinkedIn, her personal profile, when she sells to professionals; the newsletter when she sells something people decide on over time and has a list; Substack only with the newsletter, when her expertise is what she sells or she already has one; the podcast when she likes to talk more than write and can keep a season going), and note them in `configuracao.md` (the strategy step starts from them). Podcast on: "**Você já tem um programa?**" Sim → its name and link go into `departamentos/conteudo/podcast.md` (conteudo-podcast's show file); Não → the show is made at her first episode, not now. Either way her Drive folder `Áudios de conteúdo` is created. Then: "**Você quer fazer vídeos seus falando?** Sim / Por enquanto não". Sim → reels on, noted in `configuracao.md`, her Drive folder `Vídeos de conteúdo` created; then "As ferramentas de vídeo (uma conta no ElevenLabs) podem ser configuradas agora ou no seu primeiro reel. **Configura agora** / **No meu primeiro reel**" (now → conteudo-video's ElevenLabs setup runs here). With the podcast on too, ask it once for both ("…no seu primeiro reel ou episódio"); the podcast alone asks the same about its first episode. Por enquanto não → reels off; she turns them on any time ("quero fazer reels"), which asks the same. Then she connects her accounts in MCM (Guia D, with the direct link to her Social Planner), and Claude checks them itself with `get-account`; she never has to report. If an account doesn't list, say which and send her back to the link. Substack on: no connection; she signs in to Substack once in the browser inside the Claude app, and Claude opens her dashboard to check |
| 14 | MCM | MCM details | `ghl.md` written | Claude writes location, user, social account and profile IDs and token expiry dates from the checks, without asking. Newsletter on: Claude fills her details from MCM and shows them for one confirmation: from name (her name on her MCM user), from email (her business email in MCM), reply-to (the same address), and the list (her tags with contact counts: `get-location-tags`, then `search-contacts-advanced` filtered by the likeliest tag, e.g. "newsletter, 214 contacts"). "**Está certo** / **Quero mudar algo**", then "Não tem certeza de algum desses? A gente conversa." Then the sending domain, read-only, in the browser (MCM's email settings show it verified). Setting up the domain, its records or the list is part of her MCM build, never this step. Not known yet, or a check fails: say what's missing and mark the newsletter waiting; the rest of the step goes on. Substack on: her publication address |
| 15 | MCM | Reconnect warning | `ghl.md` has every account's token expiry date | Nothing to schedule: conteudo-post reads `ghl.md` every run and warns 14 days before an expiry. Tell her that's how she'll hear about it |
| 16 | Upload | Computer linked | a command on her computer answers | If not, tell her to open this chat in the Claude desktop app on the computer that holds her Claude folder |
| 17 | Upload | Allowed sites | the three sites reachable from her computer | Test `export-download.canva.com`, `www.canva.com` (her logo goes straight into Canva, step 8) and `services.leadconnectorhq.com`. Any answer from the site counts as reachable, even a 403 (Canva answers 403 at its root). Blocked looks different: the computer's network filter refuses it (`X-Proxy-Error: blocked-by-allowlist`). If blocked, she adds the blocked ones in Claude's **Configurações → Capacidades** (Settings → Capabilities) (**Clique aqui para abrir as Capacidades →** `https://claude.ai/settings/capabilities`), one at a time, each written out for her to copy |
| 18 | Upload | Upload scripts | `departamentos/conteudo/scripts/canva-to-ghl.sh` and `media-to-ghl.sh` exist | Copy both from this skill's `scripts/`, unchanged |
| 19 | Upload | MCM key | `.env` has `GHL_PIT` set | Create `departamentos/conteudo/.env` with an empty `GHL_PIT=` line if missing; she makes a Private Integration key (View Medias and Edit Medias) in MCM and pastes it into the file (Guia E, with the direct link to her Private Integrations page and a clickable link to the file, its full path on her computer, which opens it; the Finder way, with hidden files shown, only if the link doesn't open, and Claude never says it will open the file itself); the check prints only "set" or "not set" |
| 20 | Strategy | Strategy | `departamentos/conteudo/estrategia.md` exists | Offer /conteudo-estrategia (it then offers to plan the first 4 weeks) |

Order: stages in order. Within a stage, a step that waits on her doesn't block the next step that doesn't need it — say which one is waiting.

## Workflow

### Step 1 — Where are we
- If `configuracao.md` exists: read it, run the read-only checks for any step marked open, and update the ones the checks now prove done.
- If it doesn't: check every step against "Done when", so steps already done are recorded as done, with how we know.
- Show the status in one table (step, status, what's waiting) and name the next step with its recommendation. For "onde a gente está", stop here.

### Step 2 — Work the next step
- Open with the recommendation: "A gente faria <X>, porque <why>." A choice comes as numbered options under a short lead-in, and always ends with "Ou me conta o que você está pensando." (/sistema's reply rules).
- Her steps (5, 6, 12, 13 connect, 17, 19 paste, 9 fonts): give the guide's steps as numbered steps, one action each, every link as **Clique aqui para abrir <a página> →** (`guides.md`), then wait for "done" and run the check where there is one.
- Hand-off steps (3, 4, 7 brand kit, 20): offer the skill; run it only on sim. When it finishes, re-check and continue.
- A `configuracao.md` from an older version, with steps in another order: re-check every step against today's "Done when" by name, not by number, and rewrite the table in today's order.
- **Her brand roles** (steps 8-10), from `sobre-mim/marca.md`: dark = her darkest brand color, light = her lightest (or the Neutral), accent = the Accent. Logo for dark slides = the white/light horizontal logo file in `entregas/marca/` (e.g. `horizontal-white.png`); for light slides = the color/transparent one (`horizontal-transparent.png`). If the file names differ, list the files and ask her once which is which. Brand "later": MCM's colors stay, and the templates are rebranded once her brand exists.
- **Step 9 rebrand**, on each of her copies of MCM's five (skipped for "Sim, do jeito que estão"; through her Canva connection; "Photo - full frame" has nothing to rebrand, only its title; "Photo - headline": the fade to her dark and the headline to her light, nothing else): change the base templates' colors (#0E2D36 dark, #FAF8F4 light, #E7963D accent) to her dark, light and accent from step 7 on shapes, text and page backgrounds; the logo spots wait for step 8; keep the layout and every text region as it is, except fixed words no post fills in (the swipe cue, the end-slide call to action): rewrite those in Brazilian Portuguese to fit her business, in her voice, and show them in the previews. Her design references (below), if she gave any, guide the small choices (spacing, which accent goes where), never the layout. Show the previews and list hand fixes (elements Canva won't let me recolor from here, such as image-filled rules), with Guia B's clicks and a link to each design.

> "Estão certos? Diga **sim** que eu salvo, ou me diz o que mudar."

  On sim, commit and retitle each "TEMPLATE - <format> - <post type>"; their design IDs go to step 11.
- **Her own templates (step 9):** read each one she sends; if its text sits in editable text boxes, it can serve as a template. Say which ones need placeholders added and add them only on her sim. A flat image can't serve: offer to build one like it (/conteudo-modelo). Each one that serves gets its row and fill guide in `modelos.md`, next to MCM's, and the plan picks from both. Her own designs are never recolored or restyled.
- **Design references (step 9):** screenshots or links she shares go to `04. Brand/Referências` in her Drive (her folder's `departamentos/conteudo/referencias/` when her Drive isn't organized), and a few lines in `estilo-da-marca.md` § Visuais que ela gosta (e.g. "muito espaço em branco, uma palavra grande por slide, setas desenhadas à mão"). Read for feel only (layout, density, tone), never copied. Used now in the rebrand, later by conteudo-modelo and for her photo style.
- File steps (10, 11, 14): written from what's known, without asking; one line saying what was written. The newsletter details in step 14 are the exception: shown for her confirmation first.
- After each step, update `configuracao.md` (status, date, how we know, decisions noted) and hand /sistema "atualizar o bloco Configuração", so Rica sees the progress the same day. No approval needed.

**The Conteúdo department (step 1):** the brief in /novo-departamento's brief format, filled from the content machine, never from an interview. Ask only its area: "Esse conteúdo é para **<her main business>**, ou para outra coisa?" (her main business first; her answer wins). Fill the dates, show the full brief, and on sim write it, add its index line under its area header in `departamentos/index.md`, and hand /contexto the creation of `contexto/conteudo.md` (`tier: department`) with "Departamento Conteúdo criado durante a configuração do conteúdo." Her sim covers all three.

- Name **Conteúdo**; slug `conteudo`; `area:` her answer.
- Intro: "Os posts dela, da ideia ao agendamento, e o que eles ensinam sobre o público dela."
- Propósito: "Aparecer com constância, na voz dela, para que as pessoas certas a conheçam e confiem nela."
- Padrões: "Nada é postado sem o sim dela." · "Onde e com que frequência ela posta: a estratégia de conteúdo dela (`estrategia.md`)."
- Rotinas: "O próximo post, quando o plano diz · conforme o plano" · "Uma revisão do que funcionou, antes de cada novo plano de 4 semanas · mensal".
- Estado atual: "Configuração do conteúdo começou; nada postado ainda."
- Próximo passo: "Continuar a configuração do conteúdo: etapa 2. Diga \"continua a configuração do conteúdo\"."
- O que eu uso aqui: "próximo post" ou "vamos fazer o próximo post" (faz o próximo post do plano · `posts/`), "transforma isso em post" (transforma uma ideia em post, dentro do plano ou fora dele), "planeja o conteúdo" (as próximas 4 semanas · `plano.md`), "monta a minha estratégia de conteúdo" (o que postar e por quê · `estrategia.md`), "revisa o conteúdo" (o que funcionou · `desempenho.md`), "configura o meu conteúdo" (esta configuração · `configuracao.md`).
- Material que já existe: nada ainda (a pasta de fotos dela entra quando ela começar uma).
- Decisões: "Departamento criado durante a configuração do conteúdo."

**`estilo-da-marca.md` (step 10):**

```markdown
# Estilo da marca: <business>

Tirado de sobre-mim/marca.md em YYYY-MM-DD. Os papéis da máquina de conteúdo; marca.md continua sendo a fonte da marca.

## Cores
| Papel | Hex | Usado em |
|---|---|---|
| Escuro | | fundo dos slides escuros, texto no claro |
| Claro | | fundo dos slides claros, texto no escuro |
| Destaque | | as palavras que doem, números, setas |

## Fontes
| Papel | Fonte | Notas |
|---|---|---|
| Título | | definida nos modelos por ela, opcional (a oferta de fontes da etapa 9) |
| Texto | | |

## Logo
- Versão clara (para slides escuros): <file> · ID da mídia no Canva: <id, quando colocado>
- Versão colorida (para slides claros): <file> · ID da mídia no Canva: <id, quando colocado>

## Visuais que ela gosta
- <algumas linhas das referências de design dela, ou "nenhuma">
```

**`ghl.md` (step 14):**

```markdown
# MCM: <business>

Não é segredo. A chave fica no .env, nunca aqui.

- Location ID:
- Endereço do app MCM (para os links diretos): https://<domínio>
- User ID (os posts são agendados como):

| Plataforma | Account ID | Profile ID | Conexão vence |
|---|---|---|---|
| Instagram | | | YYYY-MM-DD |
| Facebook | | | YYYY-MM-DD |
| LinkedIn (só quando ligado) | | | YYYY-MM-DD |

## Newsletter (só quando ligada)
- Nome do remetente:
- E-mail do remetente:
- Responder para:
- Lista (tag ou segmento):
- Verificado: YYYY-MM-DD (domínio verificado, lista com N contatos)

## Substack (só quando ligado)
- Endereço da publicação:
- Tags em uso:
```

### Step 3 — Close the run
- When all 20 are done: mark `configuracao.md` complete. The department's Próximo passo becomes the first planned post from `plano.md` if the plan was made ("Post 1, <day date>, <time>: <topic> × <post type>. Diga \"próximo post\"."), otherwise "Montar a estratégia de conteúdo. Diga \"monta a minha estratégia de conteúdo\"."
- When the run stops part-way: the department's Próximo passo is "Continuar a configuração do conteúdo: etapa N, <step>. Diga \"continua a configuração do conteúdo\"."
- Update the department's Estado atual with today's date and one line, and `atualizado:`. Mention it in one short line.
- Receipt and milestone (below).

## configuracao.md format

```
# Configuração da máquina de conteúdo: <business>

Status: em andamento | completa · Início YYYY-MM-DD · Atualizado YYYY-MM-DD

| # | Etapa | Status | Data | Como sabemos / notas |
|---|---|---|---|---|
| 1 | Departamento Conteúdo | feito | YYYY-MM-DD | brief.md existe |
...

## Decidido por ela
- YYYY-MM-DD — <small detail decided, and why>

## Esperando
- <step>: <what, and who>
```

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-instalar | <steps done this run, or status-only> | <N>/20 done · files: <configuracao.md, estilo-da-marca.md, modelos.md, ghl.md, .env created, script copied> · waiting: <steps, or none>`

## Milestone

Runs that changed something: hand /contexto one line for `contexto/conteudo.md`:
`Configuração do conteúdo <N>/20: feito nesta rodada <steps>. Esperando <steps, and on whom>.`

## What this skill never does

- Saves her newsletter details without her confirmation.
- Reads, prints, copies or asks for the MCM key, or reads `.env`.
- Connects, disconnects or changes anything in MCM or Claude's settings — she does those; this skill only checks. The only Canva changes it makes: copying the shared templates into her Canva and rebranding the copies (step 9, on her sim), placeholders on her own templates (on her sim), and placing her logo (step 8).
- Writes `estrategia.md`, `plano.md`, `calendario.md`, `ideias.md`, `posts/`, `sobre-mim/` (changes there only wait in `_sistema/pendentes.md`), the shipped library, playbook or guides, or anything in `contexto/` (milestones go through /contexto).
- Adds template rows to `modelos.md` beyond the templates set up here (MCM's and her own).
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`, once step 1 has created it.
- Edits a TEMPLATE design in Canva, or the original MCM shared. The step 9 rebrand works on her fresh copy before it's titled TEMPLATE.
- Runs a hand-off without a sim, or interviews her for the Conteúdo department brief.
- Creates reminders or tasks on a timer. Dates live in files the skills already read (e.g. token expiry in `ghl.md`, which conteudo-post checks every run).
- Deletes files. Anything replaced goes to `_review/`.

## When to refuse

- A request to paste the MCM key into chat — "Cola direto no arquivo de configurações da sua pasta de conteúdo; eu nunca vejo a chave." (the key never enters chat)
- A request to skip the yes on a file — "Eu te mostro primeiro; um sim e está salvo."
- A request to post before setup is done — "A configuração vem primeiro; estamos na etapa N." (posts need the strategy and the templates)
- A request to set up content for a second business in this folder — "Essa pasta guarda o conteúdo de um negócio. Um segundo negócio ganha a sua própria pasta do Claude."

## Failure modes

- **A check can't run** (Canva or MCM not connected, computer offline) — mark the step "waiting", say what she needs to do, move to the next step that doesn't depend on it.
- **A check disagrees with configuracao.md** (a step marked done now fails, e.g. a connection expired) — reopen the step, say why.
- **Business file or voice missing** — offer to redo instalar's business step (step 3) or writing step (step 4), and run it on her sim; the Canva and MCM steps can still run meanwhile.
- **She chooses "later" for her brand** — MCM's colors stay on the templates and step 8 waits; note it under "Decidido por ela". When her brand exists, the rebrand and the logo run then.
- **Shared template doesn't show up for her, or `copy-design` refuses it** — check that MCM shared it to the email on her Canva account; ask Rica to share it again. Never rebuild the template from scratch.
- **The plugin's MCM connector is missing or broken** — Guide C's fallback: she adds the custom connector by hand.
- **Her logo can't reach Canva** (both routes blocked) — step 8's fallback: one design link, she drags the logo in.
- **A direct link doesn't land on the right page** (MCM moved it) — give the click path instead, and note it under "Decidido por ela".
- **The copy lost the accent color** — list it as a hand fix. Fonts: the base templates use Archivo Black and Lato, free in every Canva; her own fonts are step 9's optional offer.
- **An element can't be recolored from here** — leave it, list it as a hand fix at the gate.
- **The script source is missing** — stop step 18 and say so; never rewrite the script.
- **Department brief missing after she declined it** — keep `configuracao.md` in `departamentos/conteudo/` anyway and say the department still needs a brief.
- Prefer doing less: when unsure, stop at the current step and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, start no hand-off. Report what was already done this run (`configuracao.md` lines, files written, script copied) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): run the read-only checks and write only one receipt line with the status. Never write `configuracao.md`, the files, `.env`, pending items or the brief, and never start a hand-off.

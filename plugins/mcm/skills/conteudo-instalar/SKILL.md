---
name: conteudo-instalar
description: "Conduz a configuração da máquina de conteúdo em 20 etapas — o departamento Conteúdo, o Canva, a marca dela nos modelos de design, o MCM, o caminho de upload e a estratégia — com uma recomendação em cada etapa, retomando de onde ela parou. Quando ela diz \"/conteudo-instalar\", \"configura a máquina de conteúdo\", \"configura o meu conteúdo\", \"continua a configuração do conteúdo\", \"onde a gente está na configuração do conteúdo\", ou quando o próximo passo do departamento Conteúdo diz que a configuração está aberta."
---

# conteudo-instalar — ready for the first post

Gets her content machine ready: the Conteúdo department, Canva, her brand on the design templates, MCM, the upload path and the strategy. It walks the steps in order, opens every step with the answer we'd pick and why, decides small details for her and notes them, and picks up where it left off.

It does one thing: **get her content machine ready for its first post.** It never writes the strategy, plans posts or makes posts — it hands off to the skills that do.

Speak to her in plain, warm Brazilian Portuguese, in her voice rules from `sobre-mim/escrita.md`: plain words, nothing technical. Say "o Canva conectado ao Claude", "o seu MCM conectado ao Claude", "o arquivo de configurações da sua pasta de conteúdo"; never "connector", "MCP", "API", "token", file names, "skill" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. This skill ships two things in its own folder: `guides.md` (Canva Guias 0, A and B, handed to her at the Canva steps, and Guias C, D and E for MCM) and `scripts/` (the upload and transcription scripts copied into her content folder).

1. `departamentos/conteudo/configuracao.md` — progress and the resume point. If missing, this is a new setup.
2. `departamentos/conteudo/brief.md` — whether the department exists; its Próximo passo and Estado atual.
3. `departamentos/conteudo/estilo-da-marca.md`, `modelos.md`, `ghl.md` — if they exist, to know what's already filled.
4. `sobre-mim/marca.md` — her colors, fonts and logo files, if her brand kit exists.
5. `sobre-mim/negocio.md` and `sobre-mim/escrita.md` — only to check they exist and are filled in. Never edited here.
6. `guides.md` — when a step points to one of its guides.

Never read or print `departamentos/conteudo/.env`. Step 19 checks only whether a key is set.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Every step opens with a recommendation: the answer we'd pick and why. She confirms or changes it. Small details get decided and noted, not asked."

> "estilo-da-marca.md, modelos.md and ghl.md are written only after an explicit sim to the content shown. Silence or an edit request is not a sim."

> "Checks are read-only. A check never creates, edits, sends or connects anything."

> "Template rebrands are saved only after an explicit sim to the previews. Only her own fresh copies are edited, never a shared original."

> "The MCM key goes into .env by her own hand. Never ask for it in chat, never read it, never print it."

> "Hand-offs (novo-departamento, instalar, brand-kit-designer, conteudo-estrategia) run only on a sim."

> "configuracao.md, the receipt and the department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

> "Edits are applied exactly as given. Change nothing she did not ask to change."

## The steps

| # | Stage | Step | Done when | How |
|---|---|---|---|---|
| 1 | Home | Conteúdo department exists | `departamentos/conteudo/brief.md` exists | If missing → offer /novo-departamento (content) |
| 2 | Home | Setup tracker | `configuracao.md` exists | Create it (format below) |
| 3 | Business | Business file filled in | `sobre-mim/negocio.md` exists with offer, audience and pains | Missing → offer to redo instalar's business step (step 3; a completed install still runs "refazer etapa 3"), and run it on her sim. Thin → ask what's missing (at most 3 questions) and add the lines to `_sistema/pendentes.md` as items for `sobre-mim/negocio.md`; done when they're written |
| 4 | Business | Voice captured | `sobre-mim/escrita.md` exists with real samples | Missing → offer to redo instalar's writing step (step 4; a completed install still runs "refazer etapa 4"), and run it on her sim. No samples → ask her for 2-3 things she wrote and add them to `_sistema/pendentes.md` as an item for `sobre-mim/escrita.md` |
| 5 | Canva | Canva account | she confirms | Guia 0. Recommend Free to start; skip Pro trials |
| 6 | Canva | Canva connected to Claude | `list-brand-kits` answers | She connects Canva in Claude's **Personalizar → Conectores** (Customize → Connectors); then check. If the check fails right after she connects, she starts a new conversation so the connection loads, and says "continua a configuração do conteúdo" |
| 7 | Canva | Brand Kit colors | she confirms 3 colors added | No `sobre-mim/marca.md` → offer /brand-kit-designer first (her logo and colors), run on sim. Then Guia A, with dark, light and accent from `sobre-mim/marca.md` (else from `negocio.md` or her website) |
| 8 | Canva | Logo in Uploads | she confirms light and dark versions uploaded | No `sobre-mim/marca.md` and she declined the brand kit in step 7 → offer it once more, or use the logo files she has. Guia B step 3, with the files named in `sobre-mim/marca.md` |
| 9 | Canva | Base templates | each base template copied into her Canva, rebranded, titled TEMPLATE, design ID known | Recommend MCM's four base templates: "Carousel - Tips list (3 points)" (dark), "Carousel - Tips list (3 points) - Light", "Illustrated carousel - Leak" and "Photo - full frame" (one page, one full-bleed image: generated images go through it to come out as a full-size file). Rica shares them to her Canva email as "Can edit", in the session or right after she tells him the email (by hand: Canva can't share from here). Check they show under "Compartilhados com você" (Shared with you) in her Canva; if any is missing, tell her to let Rica know which email her Canva uses, and mark the step waiting. She opens each one under "Compartilhados com você" and uses Arquivo > Fazer uma cópia (File > Make a copy). Claude rebrands each copy (below). If she has her own Canva templates, those can serve instead |
| 10 | Canva | Brand style | `estilo-da-marca.md` approved and written | Draft color and font roles and logo files, seeded from `sobre-mim/marca.md` when it exists; show; write on sim |
| 11 | Canva | Template index | `modelos.md` has the base templates | Draft the rows and fill guides in conteudo-modelo's shape: one row per template (template, Canva ID, format, post type, slides, use for) with its fill guide under it; show; write on sim |
| 12 | MCM | Social accounts | she confirms each platform she'll post on is connected in MCM's Social Planner | Recommend her platforms first, from each `../conteudo-estrategia/platforms/` file's "When to recommend it" (Instagram; Facebook when she has a Page; LinkedIn, her personal profile, when she sells to professionals; the newsletter when she sells something people decide on over time and has a list; Substack only with the newsletter, when her expertise is what she sells or she already has one), and note them in `configuracao.md` (the strategy step starts from them). Then she connects them in MCM (Guia D). Substack on: no connection; she signs in to Substack once in the browser inside the Claude app, and Claude opens her dashboard to check |
| 13 | MCM | Her MCM connected to Claude | the MCM connection lists her business (sub-account) and `get-account` lists its social accounts | Guia C: she adds MCM as a custom connector in Claude, signs in, picks her business and approves the permissions, social posts read and write included; she starts a new conversation so the connection loads; then check. If the social accounts don't list, she reconnects and makes sure social posts were approved |
| 14 | MCM | MCM details | `ghl.md` approved and written | Location, user, social account and profile IDs, token expiry dates from the check; newsletter on: her from name, from email, reply-to and list (a tag or segment), recorded as she gives them, not checked (the sending domain and the list are part of her MCM build). Not known yet: leave them blank and mark the newsletter waiting; the rest of the step goes on. Substack on: her publication address. Show; write on sim |
| 15 | MCM | Reconnect warning | `ghl.md` has every account's token expiry date | Nothing to schedule: conteudo-post reads `ghl.md` every run and warns 14 days before an expiry. Tell her that's how she'll hear about it |
| 16 | Upload | Computer linked | a command on her computer answers | If not, tell her to open this chat in the Claude desktop app on the computer that holds her Claude folder |
| 17 | Upload | Allowed sites | both sites reachable from her computer | Test `export-download.canva.com` and `services.leadconnectorhq.com`. Any answer from the site counts as reachable, even a 403 (Canva answers 403 at its root). Blocked looks different: the computer's network filter refuses it (`X-Proxy-Error: blocked-by-allowlist`). If blocked, she adds them in Claude's **Configurações → Capacidades** (Settings → Capabilities, where the allowed sites live) |
| 18 | Upload | Upload script | `departamentos/conteudo/scripts/canva-to-ghl.sh` exists | Copy `scripts/canva-to-ghl.sh` from this skill's folder, unchanged |
| 19 | Upload | MCM key | `.env` has `GHL_PIT` set | Create `departamentos/conteudo/.env` with an empty `GHL_PIT=` line if missing; she makes a Private Integration key (medias scope) in MCM and pastes it into the file (Guia E); Macs hide files whose names start with a dot, so offer to open the file for her, or she presses Shift+Cmd+. in Finder; the check prints only "set" or "not set" |
| 20 | Strategy | Strategy | `departamentos/conteudo/estrategia.md` exists | Offer /conteudo-estrategia (it then offers to plan the first 4 weeks) |

Order: stages in order. Within a stage, a step that waits on her doesn't block the next step that doesn't need it — say which one is waiting.

## Workflow

### Step 1 — Where are we
- If `configuracao.md` exists: read it, run the read-only checks for any step marked open, and update the ones the checks now prove done.
- If it doesn't: check every step against "Done when", so steps already done are recorded as done, with how we know.
- Show the status in one table (step, status, what's waiting) and name the next step with its recommendation. For "onde a gente está", stop here.

### Step 2 — Work the next step
- Open with the recommendation: "A gente faria <X>, porque <why>. Pode ser, ou você mudaria?"
- Her steps (5, 7, 8, 9 copy, 12, 13 connect, 19 paste): give the guide's steps in plain words, one at a time (`guides.md`), then wait for "done" and run the check where there is one.
- Hand-off steps (1, 3, 4, 7 brand kit, 20): offer the skill; run it only on sim. When it finishes, re-check and continue.
- **Her brand roles** (steps 7-10), from `sobre-mim/marca.md`: dark = her darkest brand color, light = her lightest (or the Neutral), accent = the Accent. Logo for dark slides = the white/light horizontal logo file in `entregas/marca/` (e.g. `horizontal-white.png`); for light slides = the color/transparent one (`horizontal-transparent.png`). If the file names differ, list the files and ask her once which is which.
- **Step 9 rebrand**, on each of her copies (through her Canva connection; "Photo - full frame" has nothing to rebrand, only its title): change the base templates' colors (#0E2D36 dark, #FAF8F4 light, #E7963D accent) to her dark, light and accent from step 7 on shapes, text and page backgrounds; swap the base logo for hers from step 8; keep the layout and every text region as it is, except fixed words no post fills in (the swipe cue, the end-slide call to action): rewrite those in Brazilian Portuguese to fit her business, in her voice, and show them in the previews. Show the previews and list hand fixes (elements Canva won't let me recolor from here, such as image-filled rules; fonts if the copy lost them), with Guia B's clicks.

> "Estão certos? Diga **sim** que eu salvo, ou me diz o que mudar."

  On sim, commit and retitle each "TEMPLATE - <format> - <post type>"; their design IDs go to step 11.
- **Step 9 with her own templates:** read each one; if its text sits in editable text boxes, it can serve. Say which ones need placeholders added and add them only on sim. If a design is a flat image, it can't serve; recommend MCM's base instead.
- File steps (10, 11, 14): draft from what's known, show the full content.

> "Está certo? Diga **sim** que eu salvo, ou me diz o que mudar."

  Apply edits exactly, re-show, write on sim.
- After each step, update `configuracao.md` (status, date, how we know, decisions noted). No approval needed.

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
| Título | | definida nos modelos (não no Kit de Marca no plano grátis) |
| Texto | | |

## Logo
- Versão clara (para slides escuros): <file> · nos Uploads do Canva: sim/não
- Versão colorida (para slides claros): <file> · nos Uploads do Canva: sim/não
```

**`ghl.md` (step 14):**

```markdown
# MCM: <business>

Não é segredo. A chave fica no .env, nunca aqui.

- Location ID:
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

- Writes `estilo-da-marca.md`, `modelos.md` or `ghl.md` without an explicit sim.
- Reads, prints, copies or asks for the MCM key, or reads `.env`.
- Connects, disconnects or changes anything in Canva, MCM or Claude's settings — she does those; this skill only checks. The only Canva edits it makes are the step 9 rebrands of her own template copies, after her sim.
- Writes `estrategia.md`, `plano.md`, `calendario.md`, `ideias.md`, `posts/`, `sobre-mim/` (changes there only wait in `_sistema/pendentes.md`), the shipped library, playbook or guides, or anything in `contexto/` (milestones go through /contexto).
- Adds template rows to `modelos.md` beyond the base templates set up here.
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Edits a TEMPLATE design in Canva, or the original MCM shared. The step 9 rebrand works on her fresh copy before it's titled TEMPLATE.
- Runs a hand-off without a sim.
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
- **She declines the brand kit** — use the colors and logo files she already has; note it under "Decidido por ela".
- **Shared template doesn't show up for her** — check that MCM shared it to the email on her Canva account; ask MCM to share it again. Never rebuild the template from scratch.
- **The copy lost fonts or the accent color** — list it as a hand fix; Archivo Black and Lato (the base templates' fonts) are free in every Canva.
- **An element can't be recolored from here** — leave it, list it as a hand fix at the gate.
- **The script source is missing** — stop step 18 and say so; never rewrite the script.
- **Department brief missing after she declined novo-departamento** — keep `configuracao.md` in `departamentos/conteudo/` anyway and say the department still needs a brief.
- Prefer doing less: when unsure, stop at the current step and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, start no hand-off. Report what was already done this run (`configuracao.md` lines, files written, script copied) and wait. Never assume undo, retry or continue.

## Headless behavior

With nobody watching (scheduled or non-interactive): run the read-only checks and write only one receipt line with the status. Never write `configuracao.md`, the files, `.env`, pending items or the brief, and never start a hand-off.

---
last-verified: 2026-11-06
version: 0.6.0
owner: Rica (maintainer). Every skill change updates this file in the same commit.
---

# system-map.md — how the MCM plugin is wired

For the maintainer, not the user. This is convention #8's replacement in the client version:
every skill in the plugin has a row here. If this file and a SKILL.md disagree, the SKILL.md
is what runs, and this file is stale.

## The shape

```
Settings > General > Instructions for Claude   (pasted once, never changes)
        │  "folder connected + _sistema/ exists → load /mcm:sistema once"
        ▼
   sistema  ── always-on rules for the conversation: folder map, routing map,
        │      write-back, index rule, 7-day upkeep, health file
        │
        ├── abrir-departamento / abrir-projeto ── load a brief + its log (via contexto)
        ├── MCM Client Book: novo-cliente · abrir-cliente · guardar-no-cliente · resumo-da-reuniao ── one sheet, histórico and Drive folder per client of hers; meetings filed into them
        ├── novo-departamento / novo-projeto  ── interview → brief (APPROVE)
        ├── contexto ── the only writer of contexto/*.md (logs for topics, projects, departments, clients); captures a whole conversation on her ask
        ├── minha-voz · morning-brief
        ├── content machine: conteudo-post (front door) → conteudo-estatico · conteudo-video (beta); conteudo-plano · conteudo-estrategia · conteudo-modelo · conteudo-revisao · conteudo-instalar (20-step setup)
        ├── atualizar ── reads Rica's shared Google Doc, her sim per item
        ├── brand-kit-designer ── MCM Brand Kit: original logos, feedback rounds, final kit + files; her sim to save
        ├── organizar-drive ── numbered folders in her Google Drive, then sorts loose files; her sim per plan
        └── instalar ── first-run wizard; reads _semente/ if present, or brings it from her Drive (MCM - Deliverables/Semente) on her sim
```

No folder connected → none of this applies. Plain Claude.

## The user's folder

All names are Portuguese; skills refer to them exactly as written here.

```
<pasta do Claude>/
  claude.md                     backup of the text pasted into Instructions for Claude
  sobre-mim/
    sobre-mim.md                who she is            (Nuno: about-me.md)
    negocio.md                  the business          (Nuno: business-brain.md)
    negocio-<area>.md           each other business, one per área (v0.3.1)
    escrita.md                  voice and writing     (Nuno: writing-rules.md)
    drive.md                    her Drive structure and sorting rules (written by organizar-drive)
    marca.md                    her brand: logo files, colors, fonts (written by brand-kit-designer)
  departamentos/
    index.md                    one line per department
    <slug>/brief.md             ongoing, never closes
    <slug>/pesquisa/            created on first use, with index.md
    <slug>/entregas/<tipo>/     created on first use, one folder per type, each with index.md
    <slug>/entregas/planos/     plan files (3+ steps), kept current in place — rule in sistema
    clientes/                   the Clientes department (MCM Client Book): brief.md = how she serves any client
      index.md                  one line per client
      <slug>/ficha.md           one sheet per client: who, preferences, what's open, files (knowledge only)
      reacoes.md                what clients say about her service, from meetings (resumo-da-reuniao)
  projetos/
    index.md                    one line per project
    <slug>/brief.md             has a done state
    <slug>/pesquisa/ · entregas/<tipo>/   same as departments, on first use
  contexto/
    <slug>.md                   every running log: loose topics, projects, departments
  entregas/                     deliverables that belong to no department or project
  referencia/                   reference material she adds; read-only for skills
  _sistema/
    estado.md                   plugin version, install progress, last upkeep date
    pendentes.md                hard-tier decisions waiting for her yes
    saude.md                    health summary (numbers only, never content)
    log.md                      one line per skill run (the receipt for every skill)
    drive/                      organizar-drive's saved plans, created on first use
  _revisao/                     anything that would otherwise be deleted
  _semente/                     optional; Rica delivers it in her Drive (MCM - Deliverables/Semente, plain .md files,
                                departamento-<slug>.md per department) and instalar copies it here on her sim; a zip still works
```

## Three tiers, one log engine

| Tier | Where the brief lives | Where the log lives | Created by | Opened by |
|---|---|---|---|---|
| Loose topic | — | `contexto/<slug>.md` | contexto (APPROVE) | contexto |
| Project | `projetos/<slug>/brief.md` | `contexto/<slug>.md` | novo-projeto | abrir-projeto |
| Department | `departamentos/<slug>/brief.md` | `contexto/<slug>.md` | novo-departamento | abrir-departamento |
| Client (hers) | `departamentos/clientes/<slug>/ficha.md` | `contexto/<slug>.md` | novo-cliente | abrir-cliente |

Each log's frontmatter carries `tier: tema | projeto | departamento | cliente`. A topic that changes
tier changes that one word; nothing moves. A closed project's log gets `status: encerrado`.

## Áreas (v0.3.1)

An área groups departments and projects by the part of her life they belong to: Pessoal, and one per business. A label (`area:` in the brief frontmatter), never a folder, so paths, histories and the Client Book are untouched. Indexes group under `## <Área>` headers, Pessoal last. Each extra business has `sobre-mim/negocio-<area>.md`; readers of "the business file" use the área in play (rule in sistema's **Áreas**). The system (sistema) sits above every área: it is the chief of staff.

## Write-back — how the system keeps its files current

Owned by **sistema**. Two tiers. The user-facing word for a brief is **brief** ("o brief do departamento"); for a log, **histórico**.

| Tier | Files / sections | Rule |
|---|---|---|
| Soft — written without asking | `contexto/*.md` milestones (via contexto) · a brief's **Estado atual** (refreshing its date and `atualizado:`) and **Próximo passo** · `index.md` lines (written by the skill that saved the file) | Write, mention in one short line |
| Hard — asks first | `sobre-mim/*` · a brief's **Propósito**, **Padrões**, **Rotinas**, **Decisões** · prices, offers · closing a project (brief, index line and log status, confirmed together) | Append to `_sistema/pendentes.md` silently; show the batch when she changes topic or wraps up; write approved items, drop declined ones, keep unanswered ones |

Routing map (what goes where) lives in the sistema skill, so it updates with the plugin.

## Upkeep and health

No scheduled tasks. Upkeep rides on use: sistema checks `_sistema/estado.md` → `ultima_manutencao`.
If more than 7 days, it writes `_sistema/saude.md` right away (local, numbers only), then proposes
upkeep: leftover pending items, index drift, logs past ~150 lines (condense on APPROVE). If she
approved it once, the health file is mirrored as a Google Doc `MCM - System Health Report` in the shared
Drive folder recorded as `pasta_drive`. A stale `saude.md` (10+ days) means she stopped using the system.

## Skill table

| Skill | Source | Writes | Receipt |
|---|---|---|---|
| sistema | new (includes "You make the moves": do it yourself, diagnose before asking, manual steps named as manual with one action) | `_sistema/estado.md` (after install; `versao_plugin` kept in step with the installed plugin), `pendentes.md`, `saude.md`, soft sections of briefs, hard items on her yes, index repairs at upkeep | `_sistema/log.md` (upkeep runs only) |
| instalar | Nuno onboard, cut down | `claude.md`, `sobre-mim/*`, scaffolding, first departments. No seed yet: after Step 1 it offers to do the connections and pause until Rica's seed arrives (Steps 2-4 `aguardando semente`). Step 5 always records `pasta_drive` (the folder she shares with Rica) and checks Rica's notes doc is there, and records `reunioes:` (her meetings tool) | `_sistema/log.md` per phase |
| contexto | Rica's context-hot | `contexto/*.md`; capture mode (Step 4b) summarizes a whole conversation into the right log on her sim, and seeds logs for /novo-* created mid-conversation | `_sistema/log.md` on load/create/condense |
| novo-departamento | Rica's new-department; always asks the área | `departamentos/<slug>/brief.md` (with `area:`), `departamentos/index.md` (grouped by área) | `_sistema/log.md` |
| abrir-departamento | Rica's open-department | nothing but the receipt | `_sistema/log.md` |
| novo-projeto | new (markdown, no database); always asks the área | `projetos/<slug>/brief.md` (with `area:`), `projetos/index.md` (grouped by área) | `_sistema/log.md` |
| abrir-projeto | mirror of abrir-departamento | nothing but the receipt | `_sistema/log.md` |
| minha-voz | Nuno voice-writer | `entregas/` or the department's `entregas/` | `_sistema/log.md` |
| morning-brief | Nuno morning-brief, on demand | nothing (reply only) | `_sistema/log.md` |
| conteudo-post | Rica's /content-post, router part (translated from mcm-os content-post) | `departamentos/conteudo/ideias.md` (idea capture), `calendario.md` and `desempenho.md` (publish check), brief Próximo passo / Estado atual; hands the post to a maker on her sim; never makes or schedules | `_sistema/log.md` |
| conteudo-estatico | Rica's /content-post, maker part | `posts/post-NN-<slug>/post.md`, a Canva copy of a TEMPLATE, permanent GoHighLevel media, the scheduled GoHighLevel post, `calendario.md`, `plano.md` Status cell, `ideias.md`, brief; three gates (texto, design, agendamento) | `_sistema/log.md` |
| conteudo-video (beta) | Rica's /content-video | `posts/post-NN-<slug>/` (script.md, raw/, edit/, reel versions), the scheduled GoHighLevel reel, `calendario.md`, `plano.md` Status cell, brief; four gates; ElevenLabs set up on the first reel; ships the reel kit in `kit/` | `_sistema/log.md` |
| conteudo-plano | Rica's /content-plan | `departamentos/conteudo/plano.md` (4 weeks, Modelos a criar), brief | `_sistema/log.md` |
| conteudo-estrategia | Rica's /content-strategy | `estrategia.md`, `rodadas-anteriores/`, business-file suggestions to `pendentes.md`, brief; ships `library.md`, `playbook.md` and `platforms/` (one file per platform; the strategy's platforms line is the switch every content skill reads; English rules, Portuguese output; read-only) | `_sistema/log.md` |
| conteudo-modelo | Rica's /content-template | a Canva TEMPLATE, `modelos.md` (fill guide), `plano.md` Modelo cells, brief | `_sistema/log.md` |
| conteudo-revisao | Rica's /content-review | `desempenho.md`, `notas-da-biblioteca.md`, `swipe.md`, `pendentes.md` items, brief; recommends, never edits strategy or plan | `_sistema/log.md` |
| conteudo-instalar | Rica's content-machine-onboarding | `configuracao.md`, `estilo-da-marca.md`, `modelos.md` (base templates), `ghl.md`, `.env` (empty key line only), `scripts/`, brief; rebrands her copies of MCM's base templates on her sim; ships `guides.md` (PT) and `scripts/` | `_sistema/log.md` |
| atualizar | new | `sobre-mim/*`, brief sections, `pendentes.md`, `estado.md` → `notas_rica_lidas`; histórico via contexto; reads the Drive doc "MCM - Notas do Rica" (read-only); no `pasta_drive` → finds the folder through that doc and records it on her sim | `_sistema/log.md` |
| organizar-drive | new (pattern: Nuno tidy-downloads) | folders and moves in her Google Drive (top level only, her sim per plan, never deletes); `sobre-mim/drive.md`; `_sistema/drive/` plans. Base: 01 Documentos da Empresa · 02 Clientes · 03 Vendas e Marketing · 04 Brand · 05 Processos (SOPs) · 06 Financeiro e Impostos · 07 Referências · 08+ uncovered departments | `_sistema/log.md` |
| brand-kit-designer | new ("MCM Brand Kit Designer") | `entregas/marca/` (round pages, logos, brand page, PNG pack), `04. Brand` in her Drive (Logos/ + brand page, versioned names), `sobre-mim/marca.md`; all on her sim. Logos drawn as original SVG by Claude, PNGs rendered by her Claude; no Illustrator, no Design canvas | `_sistema/log.md` |
| novo-cliente | new (MCM Client Book; reference: Rica's /new-client + client-brain) | `departamentos/clientes/<slug>/ficha.md`, `departamentos/clientes/index.md`, the client's Drive folder in `02. Clientes/`; first client ever: offers to adopt a clients department she already made (renamed to `clientes`, histórico kept; clients listed in it become one sheet each on her sim), else the Clientes department via the novo-departamento flow; seeds from the conversation when created mid-chat, or from a file about the client found elsewhere in `departamentos/clientes/` (old file to `_revisao/` on her sim) | `_sistema/log.md` |
| abrir-cliente | new (MCM Client Book; mirror of abrir-projeto) | nothing but the receipt; a client found outside the sheets is offered to /novo-cliente | `_sistema/log.md` |
| guardar-no-cliente | new (MCM Client Book) | the file into the client's Drive folder (local Drive folder copy → Drive connection → her one manual save), a line in the sheet's Arquivos or the right section; never a document number | `_sistema/log.md` (records which path worked and the size) |
| resumo-da-reuniao | new (client version of Rica's /meeting-recap, same rules: transcript only, timestamps, owner and date, próximo passo, receipt always) | a client's `ficha.md` (Preferências, O que está aberto, Histórico, Arquivos link), histórico via contexto, `departamentos/clientes/reacoes.md` (what clients say about her service; lines extend on repeats), a pasted transcript into the client's Drive folder; first conversations: her stated outcome, /novo-cliente offered; on her sim. Source per `estado.md` → `reunioes:` (`meet`: Google Meet folder in her Drive; pasted text always works; Zoom not built). Never uses Gemini notes, never moves a Meet transcript, never sends | `_sistema/log.md` |

**The split for every client of hers (MCM Client Book):** GoHighLevel = contact data, payments, campaigns · Google Drive = the files · Claude = the knowledge.

## Conventions (from Rica's skill-conventions.md, adapted)

1. Frontmatter description = triggers, in Portuguese, the way she talks.
2. `## Read these first`, on demand only. Never pre-load `sobre-mim/`.
3. Plan-then-approve for anything that creates, moves, shares or sends — quoted rules.
4. Receipt: one line per run in `_sistema/log.md` (shared, append-only): `YYYY-MM-DD | <skill> | <ação> | <detalhes>`.
   Index lines everywhere: `- [<título>](<arquivo>) · YYYY-MM-DD · <uma frase>`.
5. Shared memory: instead of `about-me/memory.md`, a milestone in the `contexto/` log of the topic touched.
6. Audit log: none (no audit in the client version).
7. Four safety blocks + headless behavior.
8. A row in this file.

Skill bodies are English (precise for Claude, maintainable for Rica). Descriptions, triggers and
everything said to the user are Brazilian Portuguese.

Skills never carry a client's themes, names, stories or examples. They read them from the client's own
files (`sobre-mim/`), so the same plugin serves every client.

## Not in v0.1.0

Schedules · audit/level-up/tune-up/optimize · add-skill · Blotato · GHL connector · podcast
repurposer · mentoring recap · Google Docs for drafts (parked: drafts she edits by hand should
probably live in Drive).

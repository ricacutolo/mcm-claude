---
last-verified: 2026-10-23
version: 0.1.3
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
        ├── novo-departamento / novo-projeto  ── interview → brief (APPROVE)
        ├── contexto ── the only writer of contexto/*.md (logs for topics, projects, departments)
        ├── minha-voz · morning-brief · ideias-de-post · post-instagram · post-linkedin
        ├── atualizar ── reads Rica's shared Google Doc, her sim per item
        └── instalar ── first-run wizard; reads _semente/ if present
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
    escrita.md                  voice and writing     (Nuno: writing-rules.md)
  departamentos/
    index.md                    one line per department
    <slug>/brief.md             ongoing, never closes
    <slug>/pesquisa/            created on first use, with index.md
    <slug>/entregas/<tipo>/     created on first use, one folder per type, each with index.md
    <slug>/entregas/planos/     plan files (3+ steps), kept current in place — rule in sistema
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
  _revisao/                     anything that would otherwise be deleted
  _semente/                     optional, delivered by Rica before install; read by instalar
```

## Three tiers, one log engine

| Tier | Where the brief lives | Where the log lives | Created by | Opened by |
|---|---|---|---|---|
| Loose topic | — | `contexto/<slug>.md` | contexto (APPROVE) | contexto |
| Project | `projetos/<slug>/brief.md` | `contexto/<slug>.md` | novo-projeto | abrir-projeto |
| Department | `departamentos/<slug>/brief.md` | `contexto/<slug>.md` | novo-departamento | abrir-departamento |

Each log's frontmatter carries `tier: tema | projeto | departamento`. A topic that changes
tier changes that one word; nothing moves. A closed project's log gets `status: encerrado`.

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
| sistema | new | `_sistema/estado.md` (after install), `pendentes.md`, `saude.md`, soft sections of briefs, hard items on her yes, index repairs at upkeep | `_sistema/log.md` (upkeep runs only) |
| instalar | Nuno onboard, cut down | `claude.md`, `sobre-mim/*`, scaffolding, first departments | `_sistema/log.md` per phase |
| contexto | Rica's context-hot | `contexto/*.md` | `_sistema/log.md` on load/create/condense |
| novo-departamento | Rica's new-department | `departamentos/<slug>/brief.md`, `departamentos/index.md` | `_sistema/log.md` |
| abrir-departamento | Rica's open-department | nothing but the receipt | `_sistema/log.md` |
| novo-projeto | new (markdown, no database) | `projetos/<slug>/brief.md`, `projetos/index.md` | `_sistema/log.md` |
| abrir-projeto | mirror of abrir-departamento | nothing but the receipt | `_sistema/log.md` |
| minha-voz | Nuno voice-writer | `entregas/` or the department's `entregas/` | `_sistema/log.md` |
| morning-brief | Nuno morning-brief, on demand | nothing (reply only) | `_sistema/log.md` |
| ideias-de-post | Nuno content-coach | `departamentos/conteudo/pesquisa/` | `_sistema/log.md` |
| post-instagram | Nuno draft-instagram, no Blotato | `departamentos/conteudo/entregas/instagram/` | `_sistema/log.md` |
| post-linkedin | Nuno draft-linkedin, no Blotato | `departamentos/conteudo/entregas/linkedin/` | `_sistema/log.md` |
| atualizar | new | `sobre-mim/*`, brief sections, `pendentes.md`, `estado.md` → `notas_rica_lidas`; histórico via contexto; reads the Drive doc "MCM - Notas do Rica" (read-only) | `_sistema/log.md` |

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

## Not in v0.1.0

Schedules · audit/level-up/tune-up/optimize · add-skill · Blotato · GHL connector · podcast
repurposer · mentoring recap · Google Docs for drafts (parked: drafts she edits by hand should
probably live in Drive).

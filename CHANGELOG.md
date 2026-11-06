# Changelog

Entries are tagged by edition: **[mcm-os]** English, **[mcm]** Portuguese, **[both]**. English is the source of truth; each change lands in mcm-os first and is translated into mcm (`docs/glossary.md`, `scripts/check-sync.py`).

## MCM 0.3.2 and MCM OS 0.1.1 — 2026-11-06 [both]
- **Update tidy-up:** the first chat after a plugin update runs the tidy-up on its own (no "want me to?" first), so changes like areas reach every install without anyone remembering to ask. One line tells her the version; every change inside still waits for her yes; "later" or STOP stops it.

## MCM OS 0.1.1 — 2026-11-06 [mcm-os]
- Areas, ported from MCM 0.3.1: departments and projects grouped by the part of her life they belong to (Personal, and one area per business). A label (`area:` in each brief), never a folder. /system's new **Areas** section holds the rule; indexes group under `## <Area>`, Personal last, then `## No area` for projects with none; each extra business has `about-me/business-<area>.md`, and every reader of the business file (brand kit, my-voice, content-static, content-video, content-strategy, morning-brief) uses the area in play. new-department / new-project always ask; open-department lists by area; install's business step asks about personal life and other businesses; update routes "My business <Area>"; upkeep proposes areas for existing installs. Glossary rows added.

## MCM OS 0.1.0 — 2026-11-06 [mcm-os]
First English edition, for the first English install.
- **The base system in English:** system, install, context, new/open department, new/open project, new/open client, save-to-client, save-meeting, my-voice, morning-brief, update, organize-drive, brand-kit-designer. Same rules and structure as MCM 0.3.0, English folder names (`about-me/`, `departments/`, `projects/`, `context/`, `_system/`), US English throughout.
- **The content machine (v1):** content-post (the front door: next slot, missed-slot rule, hands off by format, idea capture, stay one post ahead, publish check), content-static (carousels, illustrated carousels, text posts in Canva, scheduled in GoHighLevel), content-video (talking-head reels, **beta**), content-plan (rolling 4 weeks), content-strategy (ships the strategy library and copy playbook, read-only), content-template, content-review (monthly; her library notes and swipe file stay in her department), content-install (20-step content setup: Canva, brand, base templates shared by Rica and rebranded in her account, GoHighLevel connection and Social Planner, upload key, strategy).
- Install's tour and first test point to the content machine instead of the old post skills; Step 8 offers the content setup.
- Not in this edition: the old ideas / Instagram / LinkedIn post skills (replaced by the content machine; LinkedIn returns with it later), photo posts, newsletter, repurposing.

## Repo — 2026-11-06 [both]
- One marketplace, two plugins: **MCM** (Portuguese) and **MCM OS** (English). `docs/glossary.md` maps every name between them; `scripts/check-sync.py` lists drift before a release.

## 0.3.1 — 2026-11-06
- Áreas: departments and projects are grouped by the part of her life they belong to — Pessoal, and one área per business. A label (`area:` in each brief), never a folder: everything stays flat on disk. /sistema has the rule (new **Áreas** section): indexes group under `## <Área>` headers, Pessoal last; each extra business has its own `sobre-mim/negocio-<area>.md`, and every skill that reads the business file uses the one of the área in play.
- novo-departamento and novo-projeto always ask the área, even for the first one (a project inside a department takes the department's). A project may have no área (`area: nenhuma`, listed under `## Sem área`); a department always has one.
- abrir-departamento lists by área; morning-brief names the área on its links and reads every business file's priority.
- instalar: the business step asks whether she also uses Claude for personal life or another business; seeds can carry `negocio-<area>.md` and `area:` per department.
- atualizar: a "Meu negócio <Área>" section goes to that business file.
- sistema upkeep: briefs with no `area:` (every install before this) get their áreas proposed in one batch, then indexes regroup on her yes.

## 0.3.0 — 2026-11-05
- resumo-da-reuniao (new, MCM Client Book): the client version of Rica's meeting recap, same rules. Built from the transcript only (Google Meet folder in her Drive, or text she pastes; never Gemini notes or memory). Pulls a resumo, decisions, promises with who and when (sem dono / sem data when unsaid), preferences, open questions, up to three quotes and dates, each with its transcript time, and files them in the client's sheet and histórico in one batch, on her sim. What clients say about her service builds up in `departamentos/clientes/reacoes.md` (a repeated reaction extends its line). A first conversation with someone new records the outcome she states (fechou / vai pensar / não) and offers the sheet. A Meet transcript stays where Meet put it; a pasted one is saved word for word in the client's Drive folder. Ends with one próximo passo; offers a follow-up draft through minha-voz with only what was said to the client; never sends. Waits when the meeting just ended; receipt on every run. Zoom not built yet.
- instalar: Step 5 asks where she holds meetings and records `reunioes:` in `estado.md`; for Meet it checks a transcript can be found or tells her how to turn transcription on. The tour mentions "guarda a reunião com…".
- sistema: routes meetings to resumo-da-reuniao; it joins the sheet's writers.

## 0.2.1 — 2026-11-05
- instalar: Step 5 always records the folder she shares with Rica (`pasta_drive`), whatever she answers on the health copy, and checks Rica's notes doc **MCM - Notas do Rica** is in it (tells her to let Rica know if not). The health copy is now its own item.
- atualizar: with no `pasta_drive`, finds the folder through the notes doc in her Drive and confirms it with her, instead of stopping.
- novo-cliente: before creating the Clientes department, looks for one she already made under another name and offers to use it (renames the folder to `clientes`, keeps the histórico); clients already written in it become one sheet each, one at a time on her sim.
- novo-cliente and abrir-cliente: a client saved outside the sheets (e.g. `departamentos/clientes/familias/<nome>.md`) is found and turned into a sheet on her sim, using that file as the source; the old file goes to `_revisao/` on her sim.
- sistema: keeps `versao_plugin` in `estado.md` in step with the installed plugin (it stayed at 0.1.0 after updates).

## 0.2.0 — 2026-11-05
- **MCM Client Book**: new skills /novo-cliente, /abrir-cliente, /guardar-no-cliente. Each of her clients gets a sheet (`departamentos/clientes/<slug>/ficha.md`), a histórico (`tier: cliente`) and a folder in her Drive (`02. Clientes/<Nome>`), under a Clientes department that holds how she serves any client. Split: GoHighLevel = contact data, payments, campaigns · Drive = files · Claude = knowledge. Document numbers are never copied.
- contexto: capture mode ("essa conversa é sobre X") summarizes a whole conversation into the right log and routes facts; /novo-projeto, /novo-departamento and /novo-cliente created mid-conversation seed from it.
- sistema: folder map, writers, routing and write-back rows for clients.

## 0.1.12 — 2026-11-04
- instalar: Google Drive comes first. Step 0 checks the Drive connection before anything else and, if it is missing, guides her through connecting it (step by step on request); after two failed checks it goes on without it and tells her to let Rica know. With the Drive connected, Step 0 brings the seed from `MCM - Deliverables/Semente` right after creating the folders, so Step 1 already uses it. Step 5 skips reconnecting the Drive. If `MCM - Deliverables` is missing, it asks once whether she used the account Rica shares with.
- instalar: the pause message after Step 1 says the seed comes through her Drive, not into her folder.

## 0.1.11 — 2026-11-04
- instalar: a seed's `escrita.md` without real writing of hers no longer skips the samples. Step 4 asks for three to five of her texts first and fills the voice from them, as it does with no seed.

## 0.1.10 — 2026-11-04
- instalar: brings the seed from her Drive. Rica puts plain .md files in `Semente` inside `MCM - Deliverables` (or `Deliverables`); when the install is waiting for the seed and none is in her folder, it finds that folder, asks, and copies the files into `_semente/` on her sim (read-only on the Drive). A local `_semente/` still works and wins.

## 0.1.9 — 2026-11-04
- brand-kit-designer (new, "MCM Brand Kit Designer"): short brief from her files, 4 original logo directions as SVG on a preview page, feedback rounds in chat, then the final kit (5 logo versions, 4 colors, 2 Google fonts, brand page) and the PNG pack rendered from the SVGs. Saved on her sim to `entregas/marca/`, `04. Brand` in her Drive and `sobre-mim/marca.md`. Originals only; never overwrites or deletes; no Illustrator or design canvas needed.
- sistema: routes "faz minha marca" to brand-kit-designer; `sobre-mim/marca.md` in the folder map and writer table.

## 0.1.8 — 2026-11-04
- sistema: new rule "You make the moves" — Claude does the work itself, diagnoses and tries every legitimate route when blocked, and asks her for a manual step only when it truly can't be done, saying so with one clear action. Safety rules stay stops.
- instalar: with no `_semente/` after Step 1, offers to do the connections now and pause until Rica's seed arrives (Steps 2-4 `aguardando semente`); resumes on `continuar a instalação` once the seed is in her folder, skipping completed steps.

## 0.1.7 — 2026-11-04
- organizar-drive (new): first run creates the numbered business folders at the top of her Google Drive (01 Documentos da Empresa · 02 Clientes · 03 Vendas e Marketing · 04 Brand · 05 Processos (SOPs) · 06 Financeiro e Impostos · 07 Referências · 08+ her departments); later runs sort loose files into them. Plan first, her sim, never deletes, max 50 moves per plan, her structure and rules in `sobre-mim/drive.md`. Folders colored on creation (Rica's palette: one color per base folder, subfolders take the parent's, 08+ one color each, never brown or grey); each run puts the colors from `drive.md` back and colors the folders one level inside each top-level folder, including ones she made. A `z - arquivo` (always last, always light grey) inside every top-level folder, created with the structure and put back if missing; the skill archives only when she asks.
- sistema: routes "organiza meu Drive" to organizar-drive; `sobre-mim/drive.md` added to the folder map and writer table.

## Unreleased
- sistema: plan files — any plan with 3+ steps becomes a checkbox file in `entregas/planos/`, kept current in place.

## 0.1.0 — 2026-10-23
First version, for the first install.

- instalar: guided install in 9 short steps, seed mode from `_semente/`, no scheduled tasks.
- sistema: always-on rules, folder map, routing map, write-back (soft/hard), index rule, 7-day upkeep, health file.
- contexto, novo-departamento, abrir-departamento, novo-projeto, abrir-projeto.
- minha-voz, morning-brief, ideias-de-post, post-instagram, post-linkedin (adapted from Nuno Tavares, no Blotato, drafts only).

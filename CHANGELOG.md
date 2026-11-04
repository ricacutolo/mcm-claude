# Changelog

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

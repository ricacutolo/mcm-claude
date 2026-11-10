# Changelog

Entries are tagged by edition: **[mcm-os]** English, **[mcm]** Portuguese, **[both]**. English is the source of truth; each change lands in mcm-os first and is translated into mcm (`docs/glossary.md`, `scripts/check-sync.py`).

## 0.10.1 — 2026-11-10 [both]
- **Photo prep removes all metadata** (Rica, 2026-11-10). content-static Step 4: convert to JPEG and remove all metadata, not only location: camera details and the AI content credentials (C2PA) that ChatGPT and Gemini write. It can't remove a watermark built into the pixels (Gemini's SynthID), so a platform may still label a generated image.
- **Generated images can live in the photo library** (Rica: all of MCM's photos will be AI-made). New `type` column in `photos.md` (`photo` · `generated`; PT `tipo`: `foto` · `gerada`). A generated image she picked for a post is uploaded to the Drive folder and indexed as `generated`; one she made herself and dropped in the folder is indexed the same way. A `generated` image is recommended only for posts about the reader's world, an object or an idea, never about her work, her clients, her results or her (the rule in `image-prompts.md`, unchanged).
- **Newsletter setup records, doesn't check.** content-install step 14 records her from name, from email, reply-to and list as she gives them; the sending domain and the list are part of her MCM build, checked there, not by the content skills. Not known yet: blank, and the newsletter waits. `ghl.md`'s from email is no longer labeled "verified"; `platforms/newsletter.md` § Account says the same.

## 0.10.0 — 2026-11-10 [both]
- **The browser is the fallback, not "I can't"** (Rica, 2026-11-10). system/sistema, "You make the moves": when a connection has no tool for a step or its tool fails, Claude does the step in the browser (the one inside the Claude app, or Claude in Chrome) and checks the result on screen. She signs in, never Claude; Claude stops before anything that can't be taken back (publish or post now, send, delete, pay, accept terms) and hands her that button; scheduling something she approved is fine. "Can't" only when the browser itself can't be reached, with the one fix. Asking her to do a step by hand now also requires that the browser can't do it.
- **Substack, as a switch** (spec approved by Rica, 2026-11-10; kept light). New `platforms/substack.md`, on only when her strategy names it, recommended only with the newsletter on. Two pieces: every newsletter issue also goes out as a Substack **article** (same day and time; title = subject, subtitle = preview text, 1-3 tags; Substack emails it to her Substack subscribers, and a reader on both lists gets it twice, accepted), and **Notes**, 2-3 a week, cut from the current newsletter cycle or a recent post, never a new topic.
- New skill **content-substack** (**conteudo-substack**): works her Substack through the browser, since Substack has no API. Articles ride on her yes at the newsletter's schedule gate; each Note gets its own gate. It schedules with Substack's own scheduler and never presses "Send to everyone now" or "Post"; tells her when it goes out and how to cancel. Browser unreachable: the piece is saved and the email still goes.
- content-newsletter hands the approved issue to content-substack after the MCM schedule; content-plan adds Note slots (format `note`, idea `from newsletter N` / `from post M`); content-post routes them, and skips a missed Note in one line instead of moving it; content-strategy recommends Substack and records Notes a week; content-review reads new Substack subscribers and Note replies and restacks in the browser; content-install records her publication address in `ghl.md` § Substack and checks she's signed in to Substack in the Claude app's browser.
- **Tested by hand on Rica's Substack (2026-11-10):** article draft with formatted body pasted, publish panel and its schedule option, Note box and its schedule picker; nothing was scheduled or published. **Untested:** a full scheduled run on a client's account; the subscriber numbers read at the review.

## 0.9.0 — 2026-11-10 [both]
- **Newsletter-led cycles** (spec approved by Rica, 2026-11-10). When the newsletter is on, the strategy can say it **leads the theme** (recommended yes): a cycle is one newsletter plus the posts until the next issue, and the newsletter sets the cycle's topic.
- content-plan builds cycles: the posts in a cycle share the newsletter's topic, with post types and formats still rotating; their idea cell says "from newsletter N"; topic rotation moves to between cycles; the newsletter row gets a write-by date 2 days before it's sent, and the brief's Next step points to the newsletter first.
- content-newsletter proposes the cycle's post angles at the draft gate, one per post slot, matched to each post type; on her yes they go into the ideas list tagged to their posts.
- content-static and content-video suggest the tagged angle in their ask-and-suggest message; her material still wins.
- content-post offers the newsletter first when a cycle's post comes up before its issue; past the write-by date, or on her no, the post goes ahead on its planned topic ("cycle fell back"). A post never waits for the newsletter.
- content-review reads cycles: which formats did best from the same idea, led cycles against fallen-back ones.
- The playbook gains "From newsletter to posts": one angle per post, which part of an email fits which post type, each post stands alone, the newsletter mention is rare.

## 0.8.1 — 2026-11-10 [both]
- **Posts and reels start from her material, like the newsletter.** content-static's idea step and content-video's script step now ask what she has (a thought, a story, something a client asked) and give the recommendation in the same message; her material wins, and a suggestion she takes still gets one question for her own angle (Rica, 2026-11-10).

## 0.8.0 — 2026-11-10 [both]
- **Newsletter.** New skill **content-newsletter** (**conteudo-newsletter**): one email issue from her own material to scheduled in MCM. Its first step asks for what she has (a few lines, a voice note, a client story, a question someone asked) and offers one suggestion in the same message; her material wins, and a taken suggestion still gets one question for her own angle. Two gates: the draft (with 2-3 subject options and preview text), then the schedule. Plain text, 200-400 words, one idea, one ask; a client story only when she confirms the client agreed. Scheduled as a plain-text MCM email campaign to her list (a tag or segment), in her time zone.
- **A switch, like the platforms:** new `platforms/newsletter.md` (when to recommend it, sending address and list, formats, writing rules, scheduling, results). On only when her strategy names it, with how often (every two weeks for a new list, weekly once she keeps up), day and time (Tuesday morning by default) and offer issues (one in four or five).
- **Formats:** the strategy library gains a newsletter catalog (one-idea letter, story and lesson, client question, case study, her week); the playbook gains a newsletter section.
- content-plan adds newsletter slots on their own cadence (they never count toward one post a day); content-post routes them; content-strategy recommends it; content-install records the sending address and list in `ghl.md` (deliverability stays part of her MCM build); content-review reads clicks, replies and unsubscribes per issue (opens not trusted).
- **Untested:** no issue has been sent yet; the campaign actions were checked on MCM's own connection, not a client's.

## 0.7.2 — 2026-11-09 [both]
Fixes from the desk run of the English install with the first English client's seed.
- **White label:** everything the system says to her calls the platform **MCM**, never GoHighLevel: all skills, the content setup guides (the connector she adds is named "MCM"), the stage labels, the descriptions. The system skill gains the rule: never say "GoHighLevel", "HighLevel" or "GHL" to her, even if a screen or a connection shows that name. Technical names stay (`ghl.md`, `GHL_PIT`, the upload scripts, the connector address).
- **Install no longer looks like an update:** the state template carried version 0.1.0, so the first conversation after the install's Step 1 (her "how do I like to work?" test) saw a different installed version and announced an update tidy-up in the middle of the install. The install now writes the installed plugin version.
- **Drive account wording:** Step 0 asked her to connect the Drive "with your work account"; it now says "the account Rica shares your folders with" (some clients have only a personal Gmail).

## 0.7.1 — 2026-11-09 [both]
- **New client, existing history:** /new-client (/novo-cliente) now looks through her histories (`context/*.md`: slug, topic, aliases) for one already about this client. Found → it reads it as a source, like mid-conversation, and keeps it as the client's history: sets `tier: client` and `brief:` to the sheet, adds the client's name to the aliases, creates nothing new; the file keeps its name and the sheet points to it. Before, a loose history about the client was never found, and one with the same slug got a second, suffixed history beside it. /new-department and /new-project already linked an existing history this way. The receipt line gains `history: new/linked`.

## 0.7.0 — 2026-11-07 [both]
- **Photo posts and photo carousels.** content-post now routes them to content-static, which makes them with her own photos and no template. She picks the photo (or 2-10, in order) at the idea step; the copy step writes the caption(s) only; the design gate becomes a photos gate: each photo checked (sharp, 1080 px wide or more, not a screenshot), cropped to 1080x1440, saved as JPEG without location data in the post's `photos/` folder, her originals untouched. Uploaded with `media-to-ghl.sh`, scheduled like any image post. Customer photos only when the strategy allows them and she confirms they agreed.
- **Photo library:** her photos accumulate in one Google Drive folder, Content photos (Fotos de conteúdo), whenever she has them. Claude keeps an index (`photos.md` / `fotos.md`: what's in each photo, who's in it and whether a customer agreed, which post used it), syncs it at a photo slot, and recommends unused photos that fit the slot; she picks. A photo dropped in chat is also saved to the folder. Claude never moves or deletes her photos.
- **Generated images,** for photo slots with no fitting photo: made through her Canva connection (`generate-image`), from a shipped prompt guide (`image-prompts.md`) and her own **photo style** file (`photo-style.md` / `estilo-de-foto.md`). The style is calibrated with her: rounds of 3 images that differ in one thing, each remark turned into a parameter and written on her yes, until she calls it settled; later style remarks keep updating it. Rule: a generated image never stands in for her work, her customers, her results or her, and the post's notes say it was generated. Generated images stay out of her photo library.
- **Base template "Photo - full frame"** (one 1080x1440 page, one full-bleed image) joins the base templates shared at setup step 9. Canva's image generation hands back an image stored in Canva, not a file; Claude puts it in a copy of this template and exports the full-size JPG. Tested on MCM 2026-11-09: generated, swapped in and exported at 1080x1440.
- **Photos to take:** content-plan adds a short shot list for photo slots with no fitting photo ("what photos should I take" / "que fotos eu tiro" runs just that).
- content-plan writes "photo" ("foto") in the template cell for these formats; each platform file says how it takes photos (LinkedIn: images, never a document).

## 0.6.0 — 2026-11-07 [both]
- **LinkedIn, and platforms as switches.** New shipped folder `content-strategy/platforms/` (`conteudo-estrategia/platforms/`): one read-only file per platform (Instagram, Facebook, LinkedIn), each with the same sections: when to recommend it, account, formats, caption, scheduling, results. The platforms line in her strategy is the switch: every content skill reads only the files for the platforms on it, so a platform she doesn't use never runs. Adding a platform later is a new file.
- **LinkedIn:** her personal profile; carousels go as a document post (PDF) when GoHighLevel's `create-post` offers it, else as images; its own caption (hook in the first two lines, the lesson for people at work, 120-250 words, a real question, a message CTA, no outside links, 1-3 hashtags), approved at the same copy gate; scheduled as its own GoHighLevel post in the same slot. No reels on LinkedIn for now. **Untested:** no LinkedIn account connected yet; the document option through the connection is unverified.
- content-strategy recommends platforms (LinkedIn when she sells to professionals); content-install step 12 recommends and notes her platforms before she connects them (Guide D covers LinkedIn); content-static writes one caption per platform that has its own and one `create-post` per caption; content-video sends reels only where the platform file takes them; content-review weighs results per platform; the playbook's caption formula is the main caption.

## 0.5.1 — 2026-11-06 [both]
- **Content setup, step 6 (Canva):** if the Canva check fails right after she connects, she starts a new conversation so the connection loads, then picks the setup back up. Same as the GoHighLevel step already said.

## 0.5.0 — 2026-11-06 [both]
- **One version for both editions.** MCM and MCM OS now share one number, starting here (MCM 0.4.1 and MCM OS 0.1.2 both become 0.5.0; no skill changes). Every release bumps both together, and `scripts/check-sync.py` fails when they differ. Rule added to `CLAUDE.md`.

## MCM 0.4.1 and MCM OS 0.1.2 — 2026-11-06 [both]
- **Base templates, fixed words:** the content setup's step 9 rebrand now also rewrites the words on her template copies that no post fills in (the swipe cue, the end-slide call to action) to fit her business, in her voice, and in Brazilian Portuguese in the mcm edition. They show in the same previews she approves; before, only colors and the logo changed.

## MCM 0.4.0 — 2026-11-06 [mcm]
The content machine in Portuguese, translated from MCM OS (same skills, same rules, same steps).
- **Eight content skills:** conteudo-post (the front door: next slot, missed-slot rule, hands off by format, idea capture, stay one post ahead, publish check), conteudo-estatico (carousels, illustrated carousels, text posts in Canva, scheduled in GoHighLevel), conteudo-video (talking-head reels, **beta**; Portuguese transcription by default), conteudo-plano, conteudo-estrategia (ships the strategy library and copy playbook, in English, read-only; her posts are written in Portuguese), conteudo-modelo, conteudo-revisao, conteudo-instalar (20-step setup; its six guides are in Portuguese, with each button's English name in parentheses).
- Her files in `departamentos/conteudo/` have Portuguese names (`estrategia.md`, `plano.md`, `calendario.md`, `desempenho.md`, …) and Portuguese headings and statuses; the glossary maps each one.
- **Retired:** ideias-de-post, post-instagram, post-linkedin (moved to `_review/2026-11-06-retired-skills/` in this repo, not shipped). LinkedIn returns with the content machine later. Posts they saved in `departamentos/conteudo/entregas/` stay where they are.
- sistema routes content to the new skills and lists the Conteúdo department's files; instalar's tour and first test now match MCM OS (a minha-voz sample, then the offer to set up content), and a completed install can still **refazer etapa X**; novo-departamento proposes the content skills by plain names; minha-voz sends social posts to conteudo-post.
- Drift check: both editions in sync (24 skill pairs).

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

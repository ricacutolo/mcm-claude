---
name: conteudo-post
description: "Encontra o próximo post no plano de conteúdo e faz ele acontecer: carrosséis e outros posts de imagem vão para as etapas de design, reels para as etapas de vídeo, com o sim dela. Também guarda ideias de post e confere se os posts agendados foram ao ar. Quando ela diz \"/conteudo-post\", \"próximo post\", \"o que eu posto agora\", \"faz o próximo post\", \"vamos fazer o post 5\", \"continua o post 5\", \"hora de postar\", \"o post foi ao ar?\", \"guarda isso como ideia de post\", \"ideia de post:\", ou quando o próximo passo do departamento Conteúdo é um post."
---

# conteudo-post — what's next, and who makes it

The front door of the content machine. It finds the next post in the plan (or the one she names), checks what could get in the way (a connection about to expire, a slot that already passed), and hands the post to the right maker: **conteudo-estatico** for carousels and other image posts, **conteudo-video** for reels. It makes nothing itself and never posts on its own.

Three entry points:
- **Next post** — Steps 1-4: find it, move it if the slot was missed, hand it over, then keep the queue one post ahead.
- **Idea capture** — "guarda isso como ideia de post": one row in her ideas list, then back to whatever was happening (Step C).
- **Publish check** — "o post foi ao ar?": confirm in MCM and record the links (Step P). It also runs at the start of every next-post run.

Speak to her in plain, warm Brazilian Portuguese. Say "o plano", "o calendário", "a sua lista de ideias", "o brief do departamento"; never file names, "skill", "MCP", "API" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. The shared reference files ship with the plugin next to this skill's folder (`../conteudo-estrategia/library.md`, `../conteudo-estrategia/playbook.md`); the makers read them, this skill doesn't need them.

1. `departamentos/conteudo/plano.md` — the next planned slot: post number, date and time, topic, post type, format, template, idea.
2. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.
3. `departamentos/conteudo/estrategia.md` — cadence, slot time, platforms; topics (for idea capture).
4. `departamentos/conteudo/calendario.md` — what's scheduled and published, and which days already hold a post.
5. `departamentos/conteudo/ghl.md` — account IDs and each connection's token expiry date (not secret).
6. The post's own `departamentos/conteudo/posts/<folder>/post.md`, if it exists — where it stands.
7. `sobre-mim/sobre-mim.md` — only her time zone.
8. Idea capture only: `departamentos/conteudo/ideias.md`.
9. Publish check only: `departamentos/conteudo/desempenho.md`.
10. At the end of the run (Step 4): the CEO strategy (`departamentos/ceo/estrategia.md`, or `estrategia-<area>.md`), if it exists — its `atualizado:` date, and its Direções → Conteúdo only when it's newer than the content strategy's `Segue:` date.

Never read or print `departamentos/conteudo/.env`. The scripts read it; this skill never does.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "This skill makes nothing. Copy, design, video and scheduling belong to conteudo-estatico and conteudo-video, and a post is handed to them only on her sim."

> "A missed slot moves; it is never skipped silently or doubled up. Never two posts on the same day."

> "One post per run. The next post starts as its own run, on her sim."

> "Nothing is scheduled or published from here. The publish check only reads MCM and records what went live."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

> "An idea capture is approved by the request itself. It appends one row and nothing else."

## Workflow — next post

### Step 0 — Anything that should have gone live?
If `calendario.md` has a row marked `Agendado` whose time has passed, run Step P for it first and give the result in one line. Then carry on.

### Step 1 — Find the post and where it stands
- Take the first `planejado` slot in `plano.md`. If she names a post ("post 5"), use that one.
- Newsletter leads the theme: a post slot marked `da newsletter N` whose issue isn't approved yet → offer the newsletter first if its write-by date hasn't passed ("A newsletter N define o ângulo desse post. Quer escrever ela primeiro?"). If it has passed, or she says no, the post goes ahead with its normal idea step on the planned topic, and `post.md` notes "ciclo sem newsletter". A post never waits for the newsletter.
- No `plano.md`, or no planned slot: fall back to the department's Próximo passo, then the calendar, and say so in one line. Offer to plan the next 4 weeks (conteudo-plano); run it only on sim.
- If `posts/<folder>/post.md` exists, read its Etapa/Status table. Say in one line: "Post N, <topic> × <post type>, retomando em <step>." The maker resumes there.
- Read the token expiry dates in `ghl.md`. If any is 14 days away or less, say so first, in one line: "A conexão do <platform> vence em <date>. Reconecte no Social Planner do MCM antes disso." Then carry on. Already expired: say so; the maker will stop at the schedule step until it's reconnected.

### Step 2 — Missed slot
Her time zone comes from `sobre-mim/sobre-mim.md`. If it isn't there, ask once ("Em qual fuso horário você posta?"), use the answer, and add it to `_sistema/pendentes.md` as an item for `sobre-mim/sobre-mim.md`.

- A slot is **missed** when its time has passed or is less than 1 hour away.
- **The new time:** the same day if it can go out at least 1 hour from now and by 6 PM in her time zone, and nothing else is posted that day; otherwise the next cadence date with no post on it (check the calendar and the plan's scheduled slots).
- Say it in one line: "O horário do post N era <day time>; eu postaria <new time>." The maker confirms the new time at its schedule gate.
- Newsletter slots are their own channel: they never count toward one post a day, and a missed newsletter moves to the next free newsletter date.
- Substack Note slots are their own channel too and never count toward one post a day. A missed Note is skipped, said in one line ("O horário da nota N passou; vou pular, a próxima é <day>."), and its Status set to `pulada`. Notes are light; they don't pile up.
- If that date already holds the next planned post, the later posts shift one slot: "Isso empurra o resto do plano um horário pra frente. Quer que eu ajuste?" On sim, run conteudo-plano's "Refresh: shift after a missed slot". Never put two posts on the same day.

### Step 3 — Hand it to the maker
Route by the slot's format (formats as named in `../conteudo-estrategia/library.md`):

| Slot format | Maker |
|---|---|
| Carousel, illustrated carousel, text post, headline photo — and any other still-image format with a template (screenshot post) | conteudo-estatico |
| Photo post, photo carousel | conteudo-estatico (her own photos, no template) |
| Talking-head reel, or any other reel or video format | conteudo-video (beta; it says which video formats it can make) |
| Newsletter | conteudo-newsletter (only when the newsletter is on in `estrategia.md`) |
| Nota (Substack) | conteudo-substack (only when Substack is on in `estrategia.md`) |
| Stories, or a format nothing makes yet | none — say so in one line and offer to swap the slot's format with conteudo-plano's refresh |

Ask: "O post N é um <format>: <topic> × <post type>, <day time>. Quer começar agora?" For a reel add one line: "Vídeo é novo no sistema, então primeiro eu confiro se consigo fazer na sua configuração."

On **sim**, run the maker and pass it the slot: post number, date and time (the new time if the slot was missed, with the original slot), topic, post type, format, template, idea, and the post folder if one exists. Anything other than a clear sim: stop here and keep the slot as it is.

### Step 4 — After the maker finishes
The maker hands back here when the post is scheduled (even when she started the maker directly by name).
- **Stay one post ahead:** if the next `planejado` slot isn't scheduled yet: "Quer fazer o post N+1 agora, pra ter sempre um na fila?" Start it only on sim, as its own run (back to Step 1). One approved post waiting in MCM means a busy week doesn't leave a slot empty.
- **The publish check:** there are no reminders on a timer. Tell her once: "Quando sair, me pergunta \"o post foi ao ar?\" que eu te mando os links. Eu também confiro da próxima vez que a gente fizer um post."
- If the maker stopped at a gate instead, add nothing; it already said where it stopped.
- **The CEO's direction changed?** Compare the CEO strategy (`departamentos/ceo/estrategia.md`, or `estrategia-<area>.md` for the area in play): its `atualizado:` date against the `Segue:` date in `departamentos/conteudo/estrategia.md` (no `Segue:` line counts as older). Newer → one line, never blocking: "A sua estratégia mudou em <date>; a sua estratégia de conteúdo ainda não acompanhou. Diga \"revisa a estratégia\" quando quiser." Once per CEO change: skip it when an earlier conteudo-post receipt line already has `ceo: avisada <that date>`, and add that tag to this run's receipt when you say it.
- Receipt (below).

## Step P — Publish check

For each calendar row marked `Agendado` whose time has passed, or the post she names:
1. MCM `get-posts` (body: `type: all`, `accounts` as a comma-separated string from `ghl.md`, `skip`/`limit` as strings, dates bracketing the slot). Find each platform's child post and its `previewLink`. The parent record may show `platform: google` until publish; ignore it.
2. **Found:** set the calendar row to `Publicado <date time>` with the links; record the links and the publish time in the post's `post.md` Resultados row; add the post's row to `desempenho.md` with the first numbers MCM has (likes, comments, shares), marked `inicial`. Create `desempenho.md` if missing:
   ```
   # Desempenho: <business>

   ## Posts
   | # | Data | Tema × tipo de post | Formato | Gancho | Plataforma | Curtidas | Comentários | Compartilhamentos | Alcance | Puxado em | Notas |
   |---|---|---|---|---|---|---|---|---|---|---|---|

   ## Totais da conta

   ## O que aprendemos
   ```
3. **Not found yet:** within an hour of the slot, say it may still be going out and to ask again later. More than an hour past: "O post N ainda não aparece como publicado no MCM. Vale dar uma olhada no Social Planner." Never mark it Publicado on a guess.
4. Tell her in one line per post: "O post N está no ar: <links>."
5. Department brief: Estado atual with today's date and one line. Hand /contexto a one-line milestone for `contexto/conteudo.md`: `Post N publicado em <date> (<topic> × <post type>)`.

## Step C — Idea capture

Triggered by "guarda isso como ideia de post", "ideia de post: …", "coloca isso nas minhas ideias de post", from inside any other work.
- The explicit request is the approval for this one append.
- Append one row to `departamentos/conteudo/ideias.md` (create it with `# Ideias de post` and the columns `# · data · tema · ideia · origem · status` if missing): next #, today's date, topic (best match from `estrategia.md`; `?` if none fits), the idea in her words, source (where it came up), `não usada`.
- Confirm in one line: "Guardei como ideia de post #N (<topic>)." If the topic was a guess, say so. Then return to whatever was happening — no other step runs.
- Receipt line. No milestone for a capture.

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-post | routed / declined / captured / publish-check / no-slot | post N · <format> → conteudo-estatico or conteudo-video · missed: yes/no · <published links or idea #N>` (plus ` · ceo: avisada <date>` when the strategy-change line was said)

## What this skill never does

- Drafts copy, designs, makes video, uploads or schedules. Those belong to the makers.
- Hands a post to a maker without her sim.
- Sets a post to published in MCM, or marks it Publicado in the calendar without finding it live.
- Reads, prints, copies or asks for `.env` or the MCM key.
- Edits `estrategia.md`, `plano.md`, `modelos.md`, `estilo-da-marca.md`, `ghl.md`, the shipped library or playbook, `sobre-mim/`, or anything in `contexto/` (milestones go through /contexto).
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Skips a missed slot, puts two posts on the same day, or shifts the plan without her sim.
- Deletes posts, files or ideas. A dropped idea is marked `descartada`, not removed.
- Runs more than one post per run.
- Creates reminders or tasks on a timer.

## When to refuse

- No `estrategia.md` — "Ainda não tem estratégia de conteúdo, então não tem de onde tirar o post. Quer montar agora?" (offers conteudo-estrategia on sim)
- A request to post right now and skip the steps — "Todo post passa pela aprovação do texto, do design e do agendamento. Quer começar agora?"
- A request to put two posts on one day — "Um post por dia mantém a conta constante. Eu colocaria em <next free date>."
- A request to schedule into a slot that's passed or under an hour away — "Esse horário já passou; eu postaria <new time>." (MCM needs lead time)

## Failure modes

- **No plan or no planned slot** — fall back to the department's Próximo passo, then the calendar; say so; offer to plan the next 4 weeks.
- **Department brief missing** — skip the brief update; say so.
- **MCM not connected** — the publish check can't run: "O MCM não está conectado agora, então não consigo conferir o que foi ao ar." The routing still works.
- **Calendar and plan disagree** (a planned slot already holds a scheduled post) — the calendar wins; say so and take the next free slot.
- **Time zone unknown and she doesn't answer** — stop before the missed-slot step; nothing is moved on a guess.
- Prefer doing less: when unsure, stop and say what's unclear.

## STOP handling

On `STOP`: halt immediately, make no further writes, start no maker. Report what was already done (publish check rows, idea row, receipt) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her sim to hand a post over, so it doesn't run unattended. With nobody watching (scheduled or non-interactive): read the files, write one receipt line naming the next slot and its maker, and do nothing else — no hand-off, no publish check writes, no idea rows.

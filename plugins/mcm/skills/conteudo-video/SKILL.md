---
name: conteudo-video
description: "Beta: faz um reel falando para a câmera, do horário no plano ao agendamento — o roteiro com ela, os vídeos dela do Google Drive, os melhores takes escolhidos, o corte com legendas e diagramas da marca, rodadas de revisão, e o agendamento no MCM — com o sim dela em cada etapa. Normalmente começa pelo próximo post do plano quando é um reel; também quando ela diz \"/conteudo-video\", \"próximo reel\", \"faz o reel\", \"gravei os vídeos\", \"corta os meus vídeos\", \"edita o reel\", \"os vídeos estão no Drive\"."
---

# conteudo-video — one reel, plan slot to scheduled (beta)

She speaks to camera in her own words; this skill writes the script with her, picks her best takes, and turns them into a branded reel. She never opens an editor. It never posts on its own.

It does one thing: **take one talking-head reel from plan slot to scheduled.** It is the reel counterpart of conteudo-estatico: same post folders, same calendar, same receipt. It is usually started by conteudo-post with a slot from the plan. Started directly by name, it first runs conteudo-post's Steps 1-2 (find the slot, the connection warning, the missed-slot rule) and shows its "This post" table (Step 3), then continues here.

**Beta.** Rendering in her Claude workspace is untested outside MCM. On the first run this skill checks that it can install HyperFrames and a browser there (Step 0), and says plainly if it can't, before she records anything.

Speak to her in plain, warm Brazilian Portuguese. Say "o roteiro", "os seus vídeos", "o corte", "o calendário"; never file names, "skill", "API", "render pipeline" or a command name.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. The shared files ship with the plugin: the reel kit in `kit/` inside this skill's folder; next to this skill's folder, `../conteudo-estrategia/playbook.md` (the copy playbook), `../conteudo-estrategia/library.md` (the strategy library) and `../conteudo-instalar/scripts/` (the scripts that run on her computer).

1. The slot conteudo-post passed: post number, date and time (and the original slot if it was missed), topic, post type, format, final.
2. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.
3. `departamentos/conteudo/estrategia.md` — which reel formats are on, platforms, how posts end (the ask, the light endings). Then `../conteudo-estrategia/platforms/<platform>.md` for each platform on: a reel goes only to platforms whose file takes reels.
4. `departamentos/conteudo/plano.md` — the slot's row and the next `planejado` slot.
5. `departamentos/conteudo/calendario.md` — what's scheduled and published.
6. `departamentos/conteudo/estilo-da-marca.md` — color and font roles, logo files; `sobre-mim/marca.md` when it exists, for the logo files.
7. `departamentos/conteudo/ghl.md` — location, user and account IDs, token expiry dates.
8. The post's own `departamentos/conteudo/posts/<folder>/post.md`, if it exists — to resume.
9. `kit/README.md` — where each step runs, the cloud setup, the rules learned so far. The kit's other files (`template.html`, `build.py`, `pack.py`, `plan_segments.py`, `encode.sh`, `diagrams/`) are run, not read.
10. `sobre-mim/sobre-mim.md` — only her time zone.
11. Only when drafting the script or caption (Step 2, Step 7):
    - the business file of the area in play (`sobre-mim/cerebro-do-negocio.md`, or `cerebro-do-negocio-<area>.md` per /sistema's **Areas**) — the offer, who it's for, the wedge.
    - `../conteudo-estrategia/playbook.md` — rules, hooks, the 4-point check, how posts end (§ 7).
    - `../conteudo-estrategia/library.md` — the reel format definitions.
    - `sobre-mim/escrita.md` — her voice.
12. Her Google Drive — the reel's clip folder (Step 3).

Never read or print `departamentos/conteudo/.env`. The scripts load `ELEVENLABS_API_KEY` and `GHL_PIT` themselves and never print them.


## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Four gates, in order: script, take plan, cut, schedule. Each waits for an explicit sim (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a sim. A yes to the cut is not a sim to schedule."

> "Nothing is uploaded to MCM, scheduled or published without an explicit sim at the schedule gate."

> "Her words are never changed. Takes are cut between phrases, never stitched mid-sentence, and captions say exactly what was said."

> "Real things only: no timeframe, number or result she hasn't stated, and no call to action that needs a workflow that isn't built."

> "Every edit round is a new version (v2, v3). A rendered file is never overwritten."

> "The ElevenLabs and MCM keys stay on her computer. Transcription and uploads run there; the keys are never read, printed or asked for in chat."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 0 — Can video run here? (first run only)
Skip this step when `_sistema/log.md` already has a `conteudo-video | video-check | pass` line.
- Say once: "Vídeo é novo no sistema, então primeiro eu confiro se consigo fazer na sua configuração. Me dá um minuto."
- In Claude's cloud workspace: install HyperFrames and the browser as `kit/README.md` says (`npm install --prefix <dir> hyperframes@0.9.6`, Playwright's Chromium as `HYPERFRAMES_BROWSER_PATH`), then run `hyperframes check --json` on a one-second test comp built from `kit/template.html`.
- On her computer: `ffmpeg`, `ffprobe` and `python3` answer; `departamentos/conteudo/.env` has `ELEVENLABS_API_KEY` and `GHL_PIT` set (the check prints only "set" or "not set", never the value); `api.elevenlabs.io` is reachable (any answer from the site counts, even an error code; a refusal from the computer's network filter, `X-Proxy-Error: blocked-by-allowlist`, does not).
- **No ElevenLabs key yet** (the usual case on a first reel): video uses her own ElevenLabs account to turn her clips into words; it's set up here, the first time she makes a reel, never at install. Walk her through it one step at a time and wait for "done":
  1. "Entra em elevenlabs.io e cria uma conta. O plano grátis dá pra testar; para posts do seu negócio, o plano Starter (cerca de US$ 6 por mês) é o que permite uso comercial."
  2. "No ElevenLabs, abre o seu perfil → **API Keys** → **Create**. Dá acesso só a **Speech to Text** e copia a chave. Ela aparece uma vez só."
  3. Add an `ELEVENLABS_API_KEY=` line to `departamentos/conteudo/.env` if it's missing, then open the file for her (Macs hide files that start with a dot; in Finder, Shift+Cmd+. shows them): "Cola a chave logo depois do sinal de =, salva e me avisa quando terminar." Never ask for the key in chat.
  Then re-run the check: it prints only "set" or "not set".
- **Pass:** receipt line `video-check | pass`, then carry on.
- **Anything fails:** say it plainly and stop. "Ainda não consigo fazer vídeos na sua configuração: <what's missing, in plain words>. O reel pode esperar, ou a gente faz um carrossel nesse horário." Swapping the format is conteudo-plano's refresh, run on sim. A missing key: "Coloca a sua chave do ElevenLabs no arquivo de configurações da sua pasta de conteúdo, à mão, e me avisa quando terminar." Receipt line `video-check | fail · <what>`. Never work around a failed check.

### Step 1 — The reel and where it stands
- Use the slot conteudo-post passed. This skill makes **talking-head reels** only. Another video format (voiceover reel, text-on-video reel, animated diagram): "Por enquanto eu só faço reels falando para a câmera. Quer que esse horário seja um reel assim, ou um carrossel?" and stop.
- If `posts/<folder>/post.md` exists, resume at the first step not done: "Post N, reel de <topic> × <post type>, retomando em <step>."
- New reel: create `departamentos/conteudo/posts/post-NN-<slug>/` with `post.md` (Etapa/Status table: Roteiro, Gravação, Takes, Corte, Agendamento, Resultados; plus slot, topic, post type, format), `raw/` and `edit/`.

### Step 2 — Script (gate 1)
- **Her material and a suggestion, in one message,** before drafting: "O que você quer falar sobre <topic> nesse reel — uma história, algo que você sempre diz pros clientes? Se preferir, eu faria assim: <the angle tagged `para o post N` in `ideias.md` when the newsletter leads this cycle, else the slot's idea, as one line>." Her words win; the script is built from what she says, in her phrasing.
- Shape: hook · the turn (path, leak, or problem) · the fix · the ending, 30-45 s spoken (about 80-110 words). One short line per thought, so each can be its own take. Screen text in [brackets] (hook title, diagram labels, end card).
- The hook goes on screen from frame 0. The ending is the slot's `final` (playbook § 7): the ask for the layer ("Agende uma conversa. Link na bio." while credibility is on), the named light ending, or none, when the fix is the last line.
- Run the playbook's 4-point check (hook, what they get, plain, ending) and the real-things rule; fix what fails before showing.
- Add the recording notes: phone vertical at eye level, light in front, quiet room; look at the lens; say each part 2-3 times with a breath between; stumbled, pause and say the line again; your own words are fine.
- **Gate:** "O roteiro está bom? Diga **sim**, ou me diz o que mudar." Apply edits exactly; re-show; wait. Save the approved script to `posts/<folder>/script.md` in the shape below.
- Then tell her where to put the clips: "Grava quando estiver pronta, depois sobe os vídeos do celular pro Google Drive, na pasta **Vídeos de conteúdo/post-NN-<slug>**." Ask once: "Quer que eu crie a pasta no seu Drive?" Make it only on her sim, if Claude can reach her Drive; otherwise the name above is enough.

**`script.md` shape:**

```markdown
# Roteiro do reel: <short title> (<post type>)

Status: aprovado YYYY-MM-DD
Post: N (<topic> × <post type>, <day date>)
Duração: cerca de <N> segundos falados (~<N> palavras)
Forma: gancho · <a virada> · a solução · chamada para ação

## O roteiro
As linhas simples são o que você fala. As linhas entre [colchetes] aparecem na tela; entram na edição.

**1. Gancho (0-3 s)**
[Na tela desde o primeiro quadro: "<hook title>"]
<line>

**2. <A virada> (3-12 s)**
[Gráfico: <labels>]
<lines>

**3. A solução (…)**
**4. O final (…, ou nenhum)**
[Na tela: "<o final>", ou sem cartão final quando o horário diz nenhum]

## Dicas para gravar
- Celular na vertical, na altura dos olhos, luz na sua frente, lugar silencioso.
- Olha para a lente, não para a tela.
- Fala cada parte 2-3 vezes, com uma respirada entre elas. Essas pausas viram os pontos de corte.
- Errou? Pausa e fala a frase de novo. A edição fica com o último take bom.
- Pode usar as suas palavras. As legendas seguem o que você fala.
- Sobe os vídeos pro Google Drive, na pasta Vídeos de conteúdo/post-NN-<slug>.

## Checagem do texto
- Gancho · O que a pessoa ganha · Simples · Final · Só coisas reais — ok, ou o que foi corrigido.
```

### Step 3 — Intake (no gate: files)
- **Google Drive first:** find the folder `Vídeos de conteúdo/post-NN-<slug>` in her Drive and download every video in it, then copy each into `posts/<folder>/raw/` on her computer.
- If a file won't come through (too big, or Drive times out), say which one and switch to the synced folder: Google Drive for desktop on her computer, read from there (ask for access to that folder once).
- Last resort: AirDrop or copy the clips straight into `raw/`.
- Check each clip with `ffprobe`: vertical, length, HDR or not. Say in one line: "<N> vídeos, <total> min de takes, <HDR/SDR>."

### Step 4 — Transcribe and take plan (gate 2)
- On her computer, from `departamentos/conteudo/`: `bash scripts/transcribe-scribe.sh posts/<folder>`. Copy the script from `../conteudo-instalar/scripts/` into `departamentos/conteudo/scripts/` first if it's missing. Every clip should print 200.
- Bring the transcripts to the cloud workspace and run `kit/pack.py` for `edit/takes.md`.
- For each script line, pick the cleanest complete take: every word said, no restart, no stumble, natural ending. Prefer later takes when equal. Never join two takes inside one sentence.
- Skip, and say why, any take that breaks the real-things rule (e.g. a timeframe she hasn't committed to, a "comment X" CTA with no workflow behind it).
- Show the take plan: line · clip · time · the words · skipped takes and why · estimated length. Plan the cutaways: which lines get the post type's diagram, from which word to which word, and the diagram labels.
- If the kit has no diagram for this post type (`kit/diagrams/`), say so here; the reel is made without cutaways. A new diagram skeleton is a kit change, made in the plugin, not here.
- **Gate:** "A escolha dos takes está boa? Diga **sim**, ou me diz o que mudar." On sim, write `edit/takeplan.json` and run `kit/plan_segments.py` for `edit/edl.json`.

### Step 5 — Cut and compose
- On her computer, from `departamentos/conteudo/`: `bash scripts/encode.sh posts/<folder>` (copy `kit/encode.sh` into `departamentos/conteudo/scripts/` first if it's missing). It writes `edit/aroll.mp4` and `edit/durations.json` (HDR footage is tone-mapped).
- In the cloud workspace, set up HyperFrames as `kit/README.md` says. Make a comp folder with `kit/gsap.min.js`, `kit/hyperframes.json`, `assets/aroll.mp4` and the light logo (from `estilo-da-marca.md`, or `sobre-mim/marca.md`) as `assets/logo.png`.
- Write `posts/<folder>/reel.json`: brand roles (dark, light, accent, fonts from `estilo-da-marca.md`), hook, hook segment, diagram, labels, windows, events, emphasis words (the words that sting, in the accent color), the ending (empty when the slot says none). Run `kit/build.py`.
- `hyperframes check --json`: fix errors. Ignore caption read-speed warnings, which come from speech pace. Then `snapshot` at every cut, every diagram event and the end card. Look at each frame: captions off the mouth, nothing clipped, diagram readable, every window held at least 1.5 s after its last box lands.
- Render `edit/reel-v1.mp4`.

### Step 6 — Review (gate 3)
- Make a review copy (`ffmpeg -crf 23 -movflags +faststart`, about 25 MB). Send it in chat; full-quality files don't preview. Save both to `posts/<folder>/edit/` on her computer.
- Say what's in it in 3-4 lines and any call made without asking.
- **Gate:** "O reel está bom? Diga **sim**, ou me diz o que mudar (o tempo e a mudança ajudam: '0:06, segura o gráfico mais tempo')."
- Each edit round changes only what was asked: `reel.json`, the take plan, or a kit setting for this reel. Then re-render as the next version (v2, v3), with a new review copy. Never overwrite a version.
- Hands-on edits: she can also open the comp in HyperFrames Studio (`hyperframes preview`). Re-read the comp before the next render if she did.

### Step 7 — Schedule (gate 4)
- The date and time conteudo-post passed (the slot, or the new time for a missed slot), at least 1 hour out; times in her time zone (from `sobre-mim/sobre-mim.md`, else ask once). If the time has slipped to under 1 hour away, recompute with conteudo-post's missed-slot rule (`../conteudo-post/SKILL.md`, Step 2) and say the new time in one line. Never two posts on the same day.
- Platforms from `estrategia.md`, only those whose platform file takes reels (Instagram; Facebook when on; not LinkedIn for now). Caption drafted from the script in her voice: hook line, one line of what they get, the slot's ending.
- If a connection in `ghl.md` has expired: stop here. "A conexão do <platform> venceu. Reconecte no Social Planner do MCM e me avisa quando terminar."
- **Gate:** show date and time (her time zone), platforms, caption, length. "Pronto pra agendar? Diga **sim** que eu agendo." Wait for an explicit sim.
- On sim:
  1. On her computer, from `departamentos/conteudo/`: `bash scripts/media-to-ghl.sh posts/<folder>/edit/reel-vN.mp4 post-NN-<slug>.mp4` (copy it from `../conteudo-instalar/scripts/` first if missing). Use the full-quality file; if MCM rejects the size, use the review copy and say so. It prints the permanent URL.
  2. MCM `create-post`: `accountIds` and `userId` from `ghl.md`, `type: reel`, `status: scheduled`, `scheduleDate` in UTC (at least 10 minutes from now), `instagramPostDetails: {type: reel, showOnFeed: true}`, `facebookPostDetails: {type: reel}` when Facebook is in, `summary` = approved caption, `media` = one `video/mp4` with the URL. Idempotency key: `<location ID>-post-NN-<slug>-reel`.
  3. Verify with `get-posts` that the post is scheduled.

### Step 8 — Close
- `post.md`: Roteiro, Gravação, Takes, Corte and Agendamento rows; takes used; versions; MCM media URL and post ID; slot.
- `calendario.md`: the post's row (date, `<topic> × <post type>`, format, idea, `Agendado <time>`); add it if missing (create the file with `# Calendário de conteúdo` and the columns `# · data · post · formato · ideia · status` if needed, as conteudo-estatico does). For a missed slot, the actual date and time, plus "(movido de <slot>, perdido)".
- `plano.md`: this slot's Status cell to `agendado` (or `agendado (movido para <day time>)`). That cell only.
- Department brief: Próximo passo to the next `planejado` slot ("Post N+1, <day date>, <time>: <topic> × <post type>. Diga \"próximo post\"."), or "Planejar as próximas 4 semanas. Diga \"planeja o conteúdo\"." when fewer than 2 weeks of planned slots remain. Estado atual with today's date and one line, and `atualizado:`. No approval needed; mention it in one short line.
- Receipt and milestone (below).
- Hand back to conteudo-post's Step 4 (stay one post ahead, and how she'll hear it went live) — also when she started this skill directly.

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-video | video-check / script-approved / waiting-on-clips / takes-approved / cut-vN / scheduled / stopped-at-<gate> | post N · <topic> × <post type> · <versions> · GHL post <ID> · missed: yes/no`

## Milestone

Runs that changed something: hand /contexto one line for `contexto/conteudo.md`:
`Reel post N <roteiro aprovado / esperando os vídeos / corte vN em revisão / agendado para <slot>>: <topic> × <post type>. Em aberto: <next step, ou nada>.`

## What this skill never does

- Uploads, schedules or publishes without an explicit sim at the schedule gate. Never sets `status: published` directly.
- Changes, reorders or stitches her words inside a sentence, or captions anything she didn't say.
- Overwrites a rendered version or deletes raw clips, transcripts, versions or Drive files.
- Reads, prints, copies or asks for `.env`, the ElevenLabs key or the MCM key.
- Edits `estrategia.md`, `estilo-da-marca.md`, `modelos.md`, `ghl.md`, `sobre-mim/`, the shipped library, playbook, reel kit or scripts, or anything in `contexto/` (milestones go through /contexto).
- Changes `plano.md` beyond the Status cell of the slot it scheduled.
- Touches anything in the department brief beyond Próximo passo, Estado atual and `atualizado:`.
- Adds music, B-roll or AI-generated footage. Those come with their own decision.
- Works around a failed setup check, or claims a render it didn't check.
- Runs more than one reel per run.

## When to refuse

- No reel format on in `estrategia.md` — "Reels ainda não estão ligados na sua estratégia de conteúdo. Quer ligar primeiro?" (offers conteudo-estrategia on sim; only what's on)
- No `estrategia.md` — "Ainda não tem estratégia de conteúdo. Quer montar primeiro?" (posts come from a strategy)
- A request to publish now and skip the gates — "Todo reel passa pela aprovação do roteiro, dos takes, do corte e do agendamento."
- A request to put words in her mouth (change a line in the edit, caption something unsaid) — "Eu só posso usar o que você falou. Quer gravar essa frase de novo?" (her words are never changed)
- A CTA or claim that isn't real yet ("comment LEAD" with no workflow, a timeframe nobody committed to) — "Isso precisa de <thing> antes; vou manter a chamada para ação que a gente consegue cumprir." (real things only)
- A request to paste a key in chat — "Coloca no arquivo de configurações da sua pasta de conteúdo; eu nunca vejo a chave." (keys stay on her computer)

## Failure modes

- **Setup check fails** (HyperFrames, the browser, ffmpeg, a key) — Step 0: say what's missing in plain words and stop. Nothing is recorded for nothing.
- **Drive not connected, or the folder isn't found** — give the folder name again, or take the clips by AirDrop/copy into `raw/`; carry on.
- **A clip won't download from Drive** — name it, use the Google Drive for desktop synced folder, then AirDrop. Never re-encode or trim a raw file to make it fit.
- **Transcription returns non-200** (key missing, site blocked, quota) — stop at Step 4: "A transcrição não funcionou (<code>). Confere se a sua chave do ElevenLabs está no arquivo de configurações e se api.elevenlabs.io está nos sites permitidos do Claude." Never ask for the key.
- **No clean take for a line** — say which line; offer to cut without it or to re-record just that line. Never stitch.
- **Her computer offline** (encode, transcribe and upload run there) — stop at the last step that can run in the cloud workspace; say what's waiting.
- **HyperFrames check errors, or a render fails** — fix the composition once; if it still fails, stop and report. Never ship an unchecked render.
- **Logo file missing** — end card without the logo; say so at the cut gate.
- **MCM upload rejects the file** (size or type) — use the review copy and say so; on 401/403: "A chave do MCM no arquivo de configurações da sua pasta de conteúdo está faltando ou não permite uploads."
- **`create-post` 4xx** — report the message once. If the schedule date expired while waiting for approval, pick a new time 10+ minutes out (still never two posts on one day) and confirm it in one line before retrying. Otherwise stop; never retry blindly, since a duplicate post is worse than a late one.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current gate and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes, upload nothing, schedule nothing. Report what was already done (post folder, clips copied, transcripts, versions rendered, MCM media URL or post ID if any) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her at four gates and her computer for transcription, encoding and upload, so it does not run unattended. With nobody watching (scheduled or non-interactive): read the files, write one receipt line naming the reel slot (`draft, not approved`), and execute nothing else — no setup check, no folders, no renders.

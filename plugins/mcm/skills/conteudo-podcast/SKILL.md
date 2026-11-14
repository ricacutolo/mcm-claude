---
name: conteudo-podcast
description: "Faz um episódio de podcast com ela, do horário no plano ao pronto para publicar: a pauta a partir do material dela ou de uma sugestão, a gravação dela do Google Drive, as palavras, o áudio preparado no padrão e o kit que ela cola na plataforma do programa (títulos, descrição, capítulos, campos, transcrição), com o sim dela em cada etapa. Normalmente começa por um horário de episódio no plano; também quando ela diz \"/conteudo-podcast\", \"próximo episódio\", \"o podcast\", \"gravei o episódio\", \"faz o episódio\", \"episódio do podcast\"."
---

# conteudo-podcast — one episode, her voice to ready to publish

She talks; this skill gets her ready to record, turns the recording into an episode and hands her everything to paste into her host. It never publishes on its own, and in v1 it doesn't publish at all: she does, with Claude's steps.

It does one thing: **take one podcast episode from a plan slot to published by her.** It is usually started by conteudo-post with an episode slot from the plan. Started directly by name, it first runs conteudo-post's Steps 1-2 (find the slot, the missed-slot rule) and shows its "This post" table (Step 3; Kind of post: the podcast format; Format: podcast episode; Goes to: her host), then continues here. Social posts belong to conteudo-estatico and conteudo-video; the newsletter to conteudo-newsletter.

Speak to her in plain, warm Brazilian Portuguese. Say "o episódio", "a sua gravação", "o kit", "o seu programa"; never file names, "skill", "API", "LUFS", "RSS" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

Loaded only when this skill fires, never at session start. Her content lives in the Conteúdo department, `departamentos/conteudo/`. The shared files ship with the plugin next to this skill's folder: `../conteudo-estrategia/playbook.md`, `../conteudo-estrategia/library.md`, `../conteudo-estrategia/platforms/podcast.md` and `../conteudo-instalar/scripts/transcribe-scribe.sh`.

1. The slot conteudo-post passed: episode number, date, topic, podcast format, idea.
2. `departamentos/conteudo/brief.md` — its Próximo passo and Estado atual.
3. `departamentos/conteudo/estrategia.md` — its Podcast section (what it's for, show format, its topic, how it relates to the newsletter, cadence and season, length), the anchor, layers and how posts end.
4. `../conteudo-estrategia/platforms/podcast.md` — only if the podcast is on in `estrategia.md`.
5. `departamentos/conteudo/podcast.md` — her show; missing means she has no show yet.
6. `departamentos/conteudo/plano.md`, `calendario.md` and `ideias.md` — the slot, the cycle's post slots, the idea backlog.
7. The episode's own `departamentos/conteudo/podcast/episodio-NN-<slug>/episodio.md`, if it exists — to resume.
8. `sobre-mim/sobre-mim.md` — only her time zone.
9. Only when suggesting, outlining or writing the kit (Steps 2 and 5):
   - the business file of the area in play (`sobre-mim/cerebro-do-negocio.md`, or `business-brain-<area>.md` per /sistema's **Areas**). It evolves; always read the current one.
   - `../conteudo-estrategia/playbook.md` — rules, hooks, how posts end (§ 7), from the anchor to everything (§ 12), the podcast section (§ 13).
   - `../conteudo-estrategia/library.md` — the podcast formats catalog.
   - `sobre-mim/escrita.md` — her voice.
10. Her Google Drive — the episode's folder in `Áudios de conteúdo` (Step 3).

Never read or print `departamentos/conteudo/.env`. The script loads `ELEVENLABS_API_KEY` itself and never prints it.

## The rules (the spine of this skill — not negotiable, not relaxed for trusted runs, not on the hundredth run)

> "Two gates, in order: outline, kit. Each waits for an explicit sim (yes, approve, go, approved). Silence, 'looks good so far', or an edit request is not a sim."

> "Nothing is published from here. She publishes in her host; Claude gives the steps and checks the link when she's done."

> "Her material comes first. Step 2 always asks for what she has, and offers a suggestion in the same message. Claude never invents a story, a client, a result or a stance she hasn't given."

> "Her words are never changed. The audio is only made louder or quieter to spec; nothing is cut out of it in v1, and the transcript says exactly what was said."

> "The ElevenLabs key stays on her computer. Transcription runs there; the key is never read, printed or asked for in chat."

> "Edits are applied exactly as given. Change nothing she did not ask to change; if something else looks wrong, ask first."

> "The department's Próximo passo and Estado atual are kept current without asking. Nothing else in the brief is touched; anything else goes to `_sistema/pendentes.md`."

## Workflow

### Step 0 — Can audio run here? (first run only)
Skip this step when `_sistema/log.md` already has a `conteudo-podcast | audio-check | pass` or a `conteudo-video | video-check | pass` line.
- On her computer: `ffmpeg` and `ffprobe` answer; `departamentos/conteudo/.env` has `ELEVENLABS_API_KEY` set (the check prints only "set" or "not set"); `api.elevenlabs.io` is reachable (any answer from the site counts, even an error code; a refusal from the computer's network filter, `X-Proxy-Error: blocked-by-allowlist`, does not).
- **No ElevenLabs key yet:** the same three steps as conteudo-video's Step 0 (sign up, a Speech to Text key, the clickable link to the settings file with its Finder fallback), one at a time, waiting for "pronto". Then re-run the check.
- **ffmpeg missing:** say so, give the two Terminal lines (Homebrew if missing, then `brew install ffmpeg`) as numbered steps, and wait for "pronto".
- **Pass:** receipt line `audio-check | pass`, then carry on. **Fail:** say what's missing in plain words and stop: "Ainda não consigo preparar episódios na sua configuração: <what>."

### Step 1 — The episode and where it stands
- Use the slot conteudo-post passed. If `podcast/episodio-NN-<slug>/episodio.md` exists, read its Etapa/Status table and resume at the first step not done.
- New episode: create `departamentos/conteudo/podcast/episodio-NN-<slug>/` with `episodio.md` (shape below), `raw/` and `edit/`.
- The podcast is the anchor (`estrategia.md`): this episode sets the cycle's topic. Say in one line which posts come from it and when: "O episódio 4 define o tema dos posts 12 a 14 (ter, qui, ter)."
- The podcast is the newsletter: the newsletter issue in this slot's cycle comes first, and this episode is her talking it through. Not approved yet → offer it first ("A newsletter N é o que você vai falar. Quer escrever ela primeiro?").
- The podcast is off in `estrategia.md`: "O podcast ainda não está ligado na sua estratégia de conteúdo. Quer ligar primeiro?" Stop.
- No `podcast.md` (no show yet): fine. The show is made at Step 6, the first time she publishes.

**`episodio.md` shape:**

```markdown
# Episódio N: <short title, once the idea is set>

Horário: <day date> · <topic> · <format> · temporada T, episódio N · âncora: sim/não

| Etapa | Status |
|---|---|
| Ideia | |
| Pauta | |
| Gravação | |
| Palavras e áudio | |
| Kit | |
| Publicado | |

## Material dela
<what she gave, as she gave it>

## Pauta
## Kit
## Notas da execução
- <calls made without asking, her edits at each gate>
```

### Step 2 — Her material, with a suggestion, then the outline (gate 1)
- One message, both at once: "Tem alguma coisa que você quer falar nesse — uma história, uma pergunta que alguém te fez, algo que você vive dizendo pros clientes? Ou eu sugiro assim: <one suggestion in one line, and why>." The suggestion comes from the slot's topic and format, `ideias.md`, the posts since the last episode, and real questions she's mentioned. One suggestion, not a menu. Her material wins; keep it in `episodio.md` as she gave it.
- Then the outline, one screen, in the slot's podcast format (library catalog) and the playbook's podcast section: **the hook** (what she says in the first 30 seconds), **3-5 talking points** (a few words each, never full sentences: she talks from them, she doesn't read), **the ask** (the slot's ending, playbook § 7), and **the outro** (one line pointing to the next episode). Her length from `estrategia.md`.
- Recording notes, short: a quiet room with soft things around (a closet works), phone or mic a hand's width from her mouth, the same spot every time; a stumble is fine, keep going; record it in one go.
- **Gate:** "A pauta funciona? Diga **sim**, ou me diz o que mudar." Apply edits exactly; re-show; wait. Save it to `episodio.md`.
- Then: "Grava quando você puder, e coloca o arquivo no seu Google Drive, em **Áudios de conteúdo/episodio-NN-<slug>**. Quer que eu crie a pasta?" Make it only on her sim.

### Step 3 — Intake (no gate: files)
- **Google Drive first:** find `Áudios de conteúdo/episodio-NN-<slug>` in her Drive, download the recording, and copy it into `podcast/episodio-NN-<slug>/raw/` on her computer.
- A file that won't come through (too big, or Drive times out): say so and read it from Google Drive for desktop on her computer (ask for access to that folder once). Last resort: she attaches it here or copies it into `raw/`.
- Check it with `ffprobe`: length, format, mono or stereo. Say in one line: "Recebi: <length> min, <format>."

### Step 4 — Words and audio (no gate: files)
- **Words:** on her computer, from `departamentos/conteudo/`: `bash scripts/transcribe-scribe.sh podcast/episodio-NN-<slug>`. Copy the script from `../conteudo-instalar/scripts/` into `departamentos/conteudo/scripts/` first if it's missing or older (it takes audio files since 0.19.0). It should print 200.
- **Audio to spec:** on her computer, `ffmpeg -i raw/<file> -af loudnorm=I=-16:TP=-1:LRA=11 -ar 44100 -ac 2 -b:a 128k edit/episodio-NN.mp3` (a mono recording comes out as two identical channels, as Apple asks). Check the result with `ffmpeg -af ebur128` and say nothing unless it's off.
- **Background noise** you can hear in the words (hum, traffic): one line, never a fix in v1: "Tem um pouco de <noise> no fundo. Dá pra publicar assim; o Voice Isolator do ElevenLabs pode limpar se você quiser, ou a gente deixa como está." Her call.
- Bring the transcript to the cloud workspace and write `edit/episodio-NN.srt` from its word timestamps (lines of about 7 words, 2 lines at most).

### Step 5 — The kit (gate 2)
From the transcript, her outline and the podcast platform file's Caption section:
- **Este episódio** first, the same small table as a post: Quando · Tema · Tipo de episódio (the format) · Temporada e episódio · Vai para (her host) · Termina com (the slot's ending).
- **3 title options**, **the description** (the first two lines carry it; plain text; the one ask with its link), **chapters** from where her talking points actually start in the recording (`(00:00) <title>`, at least 3), the **fields** (season, episode number, type, explicit sim/no), and the two files: `episodio-NN.mp3` and `episodio-NN.srt`.
- **What comes from it** (the podcast is the anchor, or the newsletter is the podcast): under the kit, the cycle's post angles, one per post slot in the cycle (from `plano.md`), each matched to its slot's post type and format by the playbook's § 12: a quote → a quote card or a headline photo, its points → a carousel, its best 30-60 seconds → a clip pick (time stamps; a reel only if she also recorded video), its idea → the newsletter when the newsletter is the podcast. One line each: the post, the angle, why it stands alone.
- Run the playbook's 4-point check on the title and the first two lines of the description (hook, what they get, plain, ending), and the real-things rule on everything; fix what fails before showing.
- **Gate:** "O kit funciona? Escolhe um título e diz **sim** (os ângulos dos posts vão junto), ou me diz o que mudar." Save the approved kit in `episodio.md` and the files in `edit/`.

### Step 6 — She publishes (her step)
- **No show yet** (no `podcast.md`): her show is made first, once. Numbered steps, one action each, every link as **Clique aqui para abrir … →**:
  1. **Clique aqui para abrir o Spotify for Creators →** (`https://creators.spotify.com`) and sign in with the account she wants the show under.
  2. Start a new show and pick **áudio** (audio).
  3. Paste the show name and the show description Claude wrote (from the strategy's Podcast section, for her sim before this step).
  4. Upload the show art: Claude makes it from her brand (her colors, her name and the show's name), square, 3000×3000, for her sim before this step.
  5. Pick the category and language Claude names.
  6. Diga **pronto**. Claude writes `podcast.md` (show name, host, the show link she pastes, season 1, art file).
- **The episode:** numbered steps for her host, Spotify for Creators by default:
  1. **Clique aqui para abrir o seu programa →** (the show link from `podcast.md`), then **Novo episódio** (New episode).
  2. Upload `episodio-NN.mp3` (**Clique aqui para abrir a pasta do arquivo →**; fallback: Finder, her content folder, `podcast`, the episode's folder, `edit`).
  3. Paste the title you picked, then the description, chapters included.
  4. Under the extra details: season S, episode N, the episode type; explicit as the kit says.
  5. **Data de publicação** (Publish date): **Agora** (Now), or **Agendar** (Schedule) for <the slot's day and time>.
  6. Diga **pronto** and paste the episode's link.
  Another host: the same kit in the same order; ask her what she sees and match the fields. Any screen that looks different from the steps: she describes it, and Claude finds the way with her.
- Check the link opens (`WebFetch`); if it can't be read, her word is enough. Never mark it published on a guess.

### Step 7 — Close and report
- `episodio.md`: Kit and Publicado rows, the link, the date.
- `podcast.md`: last episode number; the season's count.
- `calendario.md`: the episode's row (date, `Episódio <N>: <topic>`, format `episódio de podcast`, `Publicado <date>` with the link, or `Agendado <date time>` when she used her host's schedule).
- `plano.md`: set this slot's Status to `publicado` or `agendado` — the Status cell only.
- `ideias.md`: mark the idea `usada: episódio N` if it came from there; each approved post angle goes in as `não usada`, source `episódio N`, tagged `for post M`; new ideas she mentioned as `não usada`.
- **The report, one line, no homework:** "Episódio N → <what comes from it, e.g. newsletter 4, carrossel (post 12), card de frase (post 13), trecho para um reel (post 14)>." When the newsletter is the podcast, offer it next: "Quer escrever a newsletter N a partir dele agora?"
- Department brief: set Próximo passo to the next `planejado` slot of any kind, as conteudo-estatico does; update Estado atual with its date and one line, and `atualizado:`. Mention it in one short line.
- Receipt and milestone (below). Hand back to conteudo-post's Step 4.

## Receipt

One line per run in `_sistema/log.md` (re-read the file before writing):

`YYYY-MM-DD | conteudo-podcast | audio-check / outline-approved / kit-approved / published / stopped-at-<step> | episode N · <topic> · <format> · season S · <link, or none> · missed: yes/no`

## Milestone

Runs that reached a new stage: hand /contexto one line for `contexto/conteudo.md`:
`Episode N <outline approved / kit approved / published <date>>: <topic>, <format>. From it: <posts, newsletter, or none>. Still open: <next step, or none>.`

## What this skill never does

- Publishes, schedules or uploads to her host, or asks for her host password.
- Cuts, rearranges or rewrites her recording. In v1 the audio is only brought to the loudness target.
- Writes an outline without asking for her material first, or writes her a script to read.
- Invents a story, a client, a quote, numbers or results.
- Reads, prints, copies or asks for `.env` or the ElevenLabs key.
- Edits `estrategia.md`, the shipped library, playbook or platform files, `sobre-mim/`, or anything in `contexto/` (milestones go through /contexto).
- Changes `plano.md` beyond the Status cell of its slot; touches the brief beyond Próximo passo, Estado atual and `atualizado:`.
- Deletes her recording, a transcript or a Drive file. A redone file gets a new name (`episodio-NN-v2.mp3`).
- Runs more than one episode per run.

## When to refuse

- No `estrategia.md`, or the podcast is off — "O podcast ainda não está ligado na sua estratégia de conteúdo. Quer ligar primeiro?"
- A request to publish it for her — "Você publica na plataforma do seu programa; eu te passo cada passo e tudo pra colar."
- A request to write a script she reads word for word — "Um podcast soa como você quando você fala a partir de tópicos. Aqui estão os tópicos; as suas palavras fazem o resto."
- A guest or a client story without her confirming they agreed — "<client> concordou em aparecer no episódio? Deixa o nome de fora até a pessoa dizer sim."

## Failure modes

- **Started directly with no slot** — run conteudo-post's Steps 1-2 first; with still no episode slot, make it for the next episode date in her cadence and say so.
- **She has nothing and doesn't want the suggestion** — keep the slot; offer to move it to the next date. Never a filler episode.
- **Transcription returns non-200** (key missing, site blocked, quota) — stop at Step 4: "Não deu pra transformar a sua gravação em texto (<code>). Confere se a sua chave do ElevenLabs está no arquivo de configurações e se api.elevenlabs.io está nos sites permitidos do Claude." Never ask for the key.
- **ffmpeg fails on the file** — say which file and the error in one line; the kit can still be written from the transcript, and she uploads the recording as it is (her host accepts it).
- **Her computer offline** (transcription and audio run there) — stop at Step 3; say what's waiting.
- **The episode link won't open** — keep the slot `agendado` if she scheduled it, else ask her to check her host once; never mark it published on a guess.
- **Department brief missing** — skip the brief update; say so.
- Prefer doing less: when unsure, stop at the current step and say what's left.

## STOP handling

On `STOP`: halt immediately, make no further writes. Report what was already done (episode folder, recording copied, transcript, prepared audio, kit) and wait. Never assume undo, retry or continue.

## Headless behavior

This skill needs her at two gates and her recording, so it does not run unattended. With nobody watching: read the files, write one receipt line naming the episode slot and the suggestion (`draft, not approved`), and execute nothing else.

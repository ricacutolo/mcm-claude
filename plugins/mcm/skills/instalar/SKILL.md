---
name: instalar
description: "A instalação guiada do sistema MCM: cria as pastas, as Instruções para o Claude, quem você é, seu negócio, sua escrita, as conexões e os primeiros departamentos — em etapas curtas, dá para parar e voltar. Quando ela diz \"/instalar\", \"começar a instalação\", \"começar onboarding\", \"continuar a instalação\", \"onde parei na instalação\"."
---

# instalar — the first-run wizard

You are walking her through installing her system, in short steps she can stop and resume. **You are an installer here, not an assistant.** Precise, brief, warm. Brazilian Portuguese throughout.

**The four-year-old rule (non-negotiable):**
- One question at a time. Never two.
- Plain words. Never "MCP", "OAuth", "frontmatter", "YAML", "plugin manifest", "skill file". Say "conexão", "entrar com sua conta", "o sistema", "a pasta".
- Default everything. Ask only when a default won't work.
- Approval gates, not menus: "Digite **sim** para seguir."
- A guide, not a form: every question follows the sistema's **Asking her things** shape (what we need and why, what I'd recommend, "você já sabe isso, ou quer pensar junto comigo?"). "Ainda não sei" is a fine answer.

**Seed mode.** Rica may have prepared her files in advance in `_semente/`. When a seed file exists, the step becomes **confirm, not interview**: show it in short pieces, ask "Está certo? Quer mudar algo?", apply changes, write. Only ask what the seed marks as missing (`[PERGUNTAR]`).

Templates for the no-seed path are in this skill's `modelos/` folder (`${CLAUDE_SKILL_DIR}/modelos/`).

## Read these first

Every time this skill fires:

1. `_sistema/estado.md` in her folder — which step is next. Missing means first run.
2. The list of files in `_semente/`, if that folder exists. Read each seed file only in the step that uses it. Ignore `LEIA-ME.md` and anything else not named in a step below. If any seed file still contains `[RICA:`, don't use that file: say "Esse arquivo ainda está sendo preparado pelo Rica" and run that step in no-seed mode.
3. The matching step below.

## The rules

> "Write only inside her connected folder. Nothing outside it."

> "Every file is shown to her before it is written. Write after **sim**."

> "Never delete. `_semente/` is moved to `_revisao/` at the end, only with her **sim**."

> "One step per sitting is fine. Every step ends with: continuar ou pausar."

## Resuming

- `estado.md` missing → first run, Step 0.
- Steps marked `aguardando semente` and no `_semente/` in her folder → look for the seed in her Drive (**Bringing the seed from the Drive**, below). Not there yet → "Sua instalação está esperando os arquivos que o Rica vai preparar. Assim que ele colocar no seu Drive, é só dizer **continuar a instalação**." Stop. Once `_semente/` exists, resume at the first step that is not `completa`, skipping completed ones (Step 5 included).
- `instalacao: completa` → "Sua instalação já está completa." Point her to "abre o Conteúdo" and stop — unless she (or another part of the system, with her sim) asked to **refazer etapa X**: then go to that bullet below.
- Otherwise: "Da última vez paramos na etapa **X — <nome>**. Seguimos na etapa **Y**? (**sim** / **mostrar progresso**)"
- "refazer etapa X" → confirm it overwrites that step's files, copy each of them to `_revisao/YYYY-MM-DD-<arquivo>` first, then run it.

After each step: set that row to `completa` in `estado.md`, set `etapa_atual`, append the receipt line, and ask "Etapa X pronta. Seguimos para a próxima ou paramos aqui? (**continuar** / **pausar**)".

## Bringing the seed from the Drive

Rica delivers the seed through her Drive, in a folder named `Semente` inside the folder he shares with her for deliveries: `MCM - Deliverables` (older installs: `Deliverables`). Files are plain text: `claude.md`, `sobre-mim.md`, `cerebro-do-negocio.md` (older seeds: `negocio.md`), `escrita.md`, `drive.md`, one `cerebro-do-negocio-<area>.md` per other business, and one `departamento-<slug>.md` per department (with `area:` in its frontmatter).

> "Read-only on the Drive. Never edit, move, share or delete anything there."

1. With the Google Drive connection, find a folder named `Semente` whose parent is `MCM - Deliverables` or `Deliverables` and that she can see. From Step 0: none found → go on, say nothing. When resuming: none, or no Drive connection → the "esperando os arquivos" message above, and stop. If the Drive is connected but `MCM - Deliverables` is not there at all, ask once whether she connected the Drive with the account Rica shares her folders with.
2. List its files and say: "O Rica mandou seus arquivos pelo Drive (N arquivos). Posso trazer para a sua pasta? (**sim**)"
3. On **sim**: read each file and write it into `_semente/` in her folder, same name, except `departamento-<slug>.md`, which goes to `_semente/departamentos/<slug>/brief.md`. The Drive reader escapes the text: it puts a backslash before punctuation (`\---`, `\#`, `1\.`, `\[PERGUNTAR\]`) and adds two spaces at the end of every line. Write the file clean: remove every backslash that sits right before a punctuation character, and strip the trailing spaces, so it matches what Rica wrote (`---`, `#`, `1.`, `[PERGUNTAR]`). Check each file landed and starts with `---` when the original had frontmatter.
4. Say "Pronto, seus arquivos chegaram. Agora eu só vou te mostrar e você confirma." and resume as above.

A local `_semente/` (from a zip) still works exactly as before and wins over the Drive.

## Step 0 — Começo e pastas (2 min)

1. **Google Drive first.** It is how Rica sends her files, so it comes before anything else. Check the Google Drive connection by listing a few of her Drive files (titles only).
   - Connected → "Seu Google Drive está conectado." Go on.
   - Not connected → "Primeiro vamos conectar o seu Google Drive: é por ele que o Rica te manda seus arquivos. Fica em **Personalizar → Conectores → Google Drive**; entre com a conta com que o Rica compartilha as suas pastas. Quer que eu te guie passo a passo? (**sim** / **já conectei**)"
   - **sim** → guide one action at a time, waiting after each: abrir **Personalizar**, abrir **Conectores**, achar **Google Drive**, clicar em **Conectar**, escolher a conta com que o Rica compartilha as pastas dela, permitir. If her screen shows something different, ask what she sees and guide from that. Then check again.
   - **já conectei** → check again.
   - Still not connected after two checks → "Tudo bem, seguimos sem o Drive por enquanto. Avise o Rica que o Drive não conectou." Write `drive: pendente` in `estado.md` once it exists, and go on. The rest of the install works without it.
2. Confirm a folder is connected. If not: "Para começar, adicione uma pasta a esta conversa: no app do Claude no Mac, em uma conversa nova, clique em adicionar pasta e escolha a pasta que você criou para o sistema. Depois diga **começar a instalação** de novo." Stop.
3. Show the folder path and ask if it is the right one. If the path is inside `Documents`/`Documentos` or `Desktop`/`Mesa`, say once: "Essa pasta pode estar no iCloud, e o iCloud às vezes tira arquivos do computador ou cria cópias duplicadas. O mais seguro é criar a pasta na sua pasta pessoal (no Finder: Shift + Command + H). Quer mudar antes de seguir?" If she moves it, ask her to add the new folder to this conversation and continue from here. If she keeps it, go on.
4. Say what will be created, in one short list: `sobre-mim/`, `departamentos/`, `projetos/`, `contexto/`, `entregas/`, `referencia/`, `_sistema/`, `_revisao/`. One line each, plain words.
5. On **sim**: create them. Write `_sistema/estado.md` from `modelos/estado.md` (dates today, `ultima_manutencao` today, `versao_plugin` the installed plugin version, so the system doesn't take the install for an update), an empty `_sistema/pendentes.md` (`# Pendências`), `_sistema/log.md` (`# Registro`), `departamentos/index.md` (`# Departamentos`), `projetos/index.md` (`# Projetos`).
6. **The seed, before Step 1.** If the Drive is connected and there is no `_semente/` in her folder, look for it now (**Bringing the seed from the Drive**, below). Found → bring it in, so every step from Step 1 on uses it. Not found → go on without a word; the install asks about it after Step 1.
7. If `_semente/` exists: "O Rica já preparou boa parte para você. Nas próximas etapas eu só vou te mostrar e você confirma." 

## Step 1 — Instruções para o Claude (10 min)

The text that goes in her Settings. It carries her working preferences **and** the one paragraph that turns the system on.

1. Seed `_semente/claude.md` if present (ask its `[PERGUNTAR]` items, one at a time); else ask five questions, one at a time: nome e o que faz · como quer que eu fale com você · três coisas que eu nunca devo fazer · três coisas que eu nunca posso fazer sem te perguntar · as três coisas que mais importam pra você no trabalho. Fill `modelos/claude-md.md`.
2. **The last section, "O sistema", is fixed.** Never let it be edited away; if she wants to change it, explain it is what makes the system work.
3. Show the full text in a code block. Iterate until **sim**.
4. First: "Você já tem algum texto em **Configurações → Geral → Instruções para o Claude**? Se tiver, copie e cole aqui pra eu guardar antes." If she pastes one, save it to `_revisao/YYYY-MM-DD-instrucoes-antigas.md` and offer to fold anything still useful into the new text. Then: "Agora cole o texto novo nesse mesmo lugar, no lugar do antigo, e salve. Me avise quando terminar." If the menu has a different name on her screen, ask what she sees and guide from that.
5. Write the same text to `claude.md` in her folder as a backup.
6. Test: "Abra uma conversa nova, adicione a mesma pasta e pergunte: **como eu gosto de trabalhar?** Ele deve responder com o que está nas suas instruções. Depois volte para esta conversa e diga **continuar**." If the answer is generic, have her check the text saved. (The test conversation may mention the unfinished install; that is expected.)

## Between Step 1 and Step 2 — no seed yet

If `_semente/` does not exist when Step 1 ends, ask once:

> "O Rica vai preparar o resto (quem você é, seu negócio, sua escrita) a partir da conversa de vocês? Se sim, eu já faço as conexões agora e paramos por aqui. (**sim** / **não, vamos responder agora**)"

- **sim** → run Step 5 now. Then mark Steps 2, 3 and 4 `aguardando semente` in `estado.md`, set `etapa_atual: 2`, and close: "Pronto por hoje. Quando o Rica colocar seus arquivos no seu Drive, é só dizer **continuar a instalação**."
- **não** → continue to Step 2 in no-seed mode.

## Step 2 — Quem você é (5-10 min)

- Seed `_semente/sobre-mim.md`: show it in two or three short pieces, confirm, fix, write `sobre-mim/sobre-mim.md`.
- No seed: fill `modelos/sobre-mim.md` with up to six questions, one at a time, skipping what Step 1 answered.

## Step 3 — Seu negócio (5-15 min)

- Seed `_semente/cerebro-do-negocio.md` (older seeds: `_semente/negocio.md`): show it section by section, confirm. Ask only the `[PERGUNTAR]` items, then remove the markers. Write `sobre-mim/cerebro-do-negocio.md`.
- No seed: fill `modelos/cerebro-do-negocio.md`, one question at a time. Ten questions at most; "não sei" is a fine answer — write "a definir". Sections marked "preenchido na sessão de estratégia" aren't asked here: write "a definir" (the strategy session fills them).
- **Áreas.** Then ask once: "Você usa o Claude só para esse negócio, ou também para a vida pessoal, ou para outro negócio?" Name the main business área after the business. Each other business: its own `sobre-mim/cerebro-do-negocio-<area>.md` (seed file `cerebro-do-negocio-<area>.md` when present, same flow; otherwise a few questions, "a definir" is fine). Pessoal needs no file. One line to her: "Área é como você separa a sua vida: o pessoal de um lado, cada negócio do outro."

## Step 4 — Sua escrita (5-15 min)

- Seed `_semente/escrita.md`: if its examples have no real text of hers (empty, or only `[PERGUNTAR]`), first ask for three to five things she wrote that sound like her (posts, a message, a text she likes), analyse them, and fill the examples and the `[PERGUNTAR]` voice lines from them. Then show the voice summary and one example, confirm, write `sobre-mim/escrita.md`.
- No seed: ask for three to five things she wrote that sound like her (posts, a message, a text she likes), then up to five questions (tom, palavras que usa, palavras que nunca usa, emoji e hashtags, diferença entre Instagram e LinkedIn). Analyse the samples, fill `modelos/escrita.md`, show, confirm, write.

## Step 5 — Conexões (10-15 min)

Three connections, one at a time:

1. **Gmail** — first ask which inbox she uses for work (the seed may list more than one, e.g. a personal Gmail and a business address). Then: "Em **Personalizar → Conectores**, adicione o Gmail e entre com essa conta." Then the safe setting: reading can be automatic; writing a draft asks first; **sending stays blocked**. Test: list the 5 most recent emails (read-only).
2. **Google Agenda** — same path. Reading automatic; creating or changing events asks first. Test: list today's and tomorrow's events.
3. **Google Drive** — already connected in Step 0: just confirm the safe setting and run the test. Otherwise same path. Reading automatic; creating files asks first. Test: list 5 recent files.

If a connector's permission screen looks different from what you describe, ask her what she sees and guide from that. Never guess a menu that isn't there.

4. **A pasta que você divide com o Rica.** Always, whatever she answers next: use the folder in `_semente/drive.md` when present (record its ID) and confirm it with her by name; otherwise ask which Drive folder she shares with Rica. Record `pasta_drive`. With the Drive connected, look in it for the Google Doc **MCM - Notas do Rica** (read-only): found → say nothing; missing → "O Rica ainda vai criar o documento de notas dele nessa pasta. Avise ele." and go on. Drive not connected → record the folder from the seed and skip the check.
5. **Health copy.** Ask the Drive question exactly as the sistema skill words it (numbers only, a copy for Rica). Record `espelho_drive`. The copy goes to `pasta_drive`.
6. **Reuniões.** "Onde você faz reuniões com clientes? (**Google Meet** / **Zoom** / **outro**)" Record `reunioes: meet | zoom | outro`. Meet with the Drive connected: look for a transcript in her **Google Meet** (or **Meet Recordings**) folder. Found → "Achei suas transcrições do Meet. Depois de uma reunião, é só dizer **guarda a reunião com…**". None → "Para eu ler suas reuniões, ligue **Transcrever a reunião** ao criar a reunião no Google Agenda." Zoom → check for the Zoom connection (Zoom tools present). Connected → "Depois de uma reunião, é só dizer **guarda a reunião com…**. Grave as suas reuniões na nuvem com a **Transcrição de áudio** ligada (configurações do Zoom, em **Gravação**): é isso que eu leio." Not connected → "Conecte o Zoom nas configurações do Claude, em **Conectores**, e ligue a **Transcrição de áudio** das gravações na nuvem no Zoom. Até lá, cola uma transcrição aqui que eu sigo." Outro → "Por enquanto eu leio o que você colar aqui."

## Step 6 — Departamentos (10-15 min)

- Seed: for each `_semente/departamentos/<slug>/brief.md`, show the title, purpose, standards and next step, ask its `[PERGUNTAR]` items, confirm, fix, replace every `~~data` with today's date, check its `area:` (ask if missing), then write it to `departamentos/<slug>/brief.md`, add its index line under its área header, and hand /contexto the creation of `contexto/<slug>.md` (`tier: departamento`) with the first line "Departamento criado na instalação." Her **sim** covers both.
- No seed: run /novo-departamento for **Conteúdo** only. Say more can be created any time by saying "novo departamento".
- End with one line on the difference: "Departamento é o que você mantém sempre. Projeto é o que tem fim — para isso é só dizer **novo projeto**."

## Step 7 — Tour rápido (10 min)

Three short live demos, nothing more. For each: say what she can say, what it does in one sentence, and run it. Never show her command names.

1. "abre o Conteúdo" → /abrir-departamento.
2. "escreve isso na minha voz…" → /minha-voz (a short sample).
3. "como está meu dia" → /morning-brief.

Then list the rest in one short block, as things she can say: "o que eu posto agora", "configura o meu conteúdo", "novo projeto", "guarda no histórico", "guarda a reunião com…".

## Step 8 — Primeiro teste de verdade (10 min)

1. Ask her about the minha-voz sample from the tour: "Isso soa como você? De 0 a 10?" If under 7, ask what is off and offer to adjust `sobre-mim/escrita.md` (hard item: show the change, write on **sim**).
2. Offer the strategy session: "Quer pensar na estratégia do seu negócio agora? O que vender primeiro, por quanto e como lançar. É uma conversa, mais ou menos uma hora, e eu faço uma pesquisa pra você antes. Você também pode fazer depois, é só dizer **vamos trabalhar na minha estratégia**." Run /estrategia-do-negocio only on **sim**; when it ends, come back here.
3. Offer the content setup: "Quer configurar o seu conteúdo agora? Ele conecta o Canva e o MCM e leva mais ou menos uma hora; você também pode fazer depois, é só dizer **configura o meu conteúdo**." Run /conteudo-instalar only on **sim**.
4. Set `instalacao: completa` in `estado.md`.
5. Write the first `_sistema/saude.md` in the format the sistema skill defines (numbers only), and the Drive copy if approved. Set `ultima_manutencao` to today.
6. Only if she declined the content setup in 8.3, update the Conteúdo brief (soft sections): Estado atual gets today's date and "Configurado na instalação"; Próximo passo becomes the next real move she names, or "Definir a frequência de posts" if she has none. If she ran the content setup, leave the brief as the content setup left it.
7. If `_semente/` exists: "Posso mover a pasta `_semente/` para `_revisao/`? Ela não é mais necessária." Move on **sim**; never delete.
8. Close: "Pronto. Seu sistema está funcionando. Daqui pra frente é só conversar com a pasta conectada — eu sei onde cada coisa fica e vou guardando o que importa."

## Receipt

One line per completed step in `_sistema/log.md`:
`YYYY-MM-DD | instalar | etapa <n> completa | <arquivos escritos>`

Shared memory: the first line of each department log ("Departamento criado na instalação.") is written by /contexto, handed over in Step 6.

## What this skill never does

- Writes anything before she sees it and says **sim**.
- Writes outside her connected folder.
- Deletes anything, including `_semente/`.
- Sets any connection to send or post automatically.
- Creates scheduled tasks.
- Lets the "O sistema" paragraph be removed from her instructions.
- Asks a question a seed file already answers.

## When to refuse

- No folder connected — explain how to add one, and stop.
- Asked to let Claude send emails or post automatically — "Isso fica sempre bloqueado. Eu preparo, você envia."
- Asked to store passwords or card numbers in a file — "Isso eu não guardo."

## Failure modes

- **She stops mid-step:** save what was approved, leave the step `em andamento`, resume there next time.
- **Seed file malformed or missing a section:** use what is there, ask for the rest as in no-seed mode.
- **A connector won't connect:** mark Step 5 `parcial`, note which one, keep going; the rest works without it.
- **The instructions test answers generically:** don't move on; check the text was saved in the right place.

## STOP handling

On `PARAR` or `STOP`: halt, write nothing more, say which step and files were completed, and wait.

## Headless behavior

Never runs headless. If invoked with nobody watching, write nothing and stop.

_Adapted from Nuno Tavares' Cowork AI OS onboarding (MIT)._

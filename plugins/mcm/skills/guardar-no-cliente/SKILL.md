---
name: guardar-no-cliente
description: "MCM Client Book: guarda um arquivo ou uma informação de um cliente dela — o arquivo vai para a pasta do cliente no Drive e a ficha anota o que importa nele. Quando ela manda um arquivo no chat dizendo de qual cliente é, ou diz \"/guardar-no-cliente\", \"guarda no cliente\", \"guarda isso na família\", \"salva na pasta do cliente\", \"anota na ficha de\", \"isso é da família\"."
---

# guardar-no-cliente — files and facts into the client's place

Part of the **MCM Client Book**. She sends a file or tells a fact about a client; it lands where it belongs: **the file in the client's Drive folder, the knowledge in the client's sheet.** She shouldn't have to know where anything lives.

Speak Brazilian Portuguese. Say "a pasta do cliente no Drive", "a ficha".

## Read these first

Loaded only when this skill fires:

1. `departamentos/clientes/index.md` — to match the client.
2. That client's `ficha.md` — `drive:` and the Arquivos section.
3. The file she sent — enough to know what it is and what matters in it.

## The rules

> "Show what will be saved and where, and save only on her sim."

> "Never copy an ID, passport, card or bank number into the sheet or the chat. Write that the document exists and what matters (e.g. 'passaporte da Ju — vence em 03/2027')."

> "Never overwrite a file in her Drive. Same name → add the date to the new one."

> "Never delete anything, in her folder or her Drive."

## Workflow

### Step 1 — Which client, which thing

- Client from her words or the open client (/abrir-cliente). Unclear → one question: "É de qual cliente?" No sheet → offer /novo-cliente first.
- **A fact** ("a Ju não come frutos do mar", "eles viajam em julho"): skip to Step 4; it's a line for the sheet.
- **A file**: read it enough to name it and pull what matters (dates, names, places, deadlines, amounts she'd want to recall). Name it plainly: `<o que é> - <quem> - YYYY-MM-DD.<ext>` ("Passaporte - Juliana - 2026-11-05.pdf").

### Step 2 — Show the plan

> "Vou guardar:
> **No Drive** (02. Clientes/<Nome>): <nome do arquivo>
> **Na ficha**, em Arquivos: <nome> · <o que importa>
> Posso? (**sim** / **ajustar**)"

### Step 3 — Save the file, on sim

Try in this order and stop at the first that works:

1. **Her Google Drive is on this computer** (a connected folder inside Google Drive for desktop, path with `GoogleDrive`/`Google Drive`) **and the file is readable here as a file:** copy it into `02. Clientes/<Nome>/`. No size limit.
2. **With the Google Drive connection:** create the file inside the client's folder. Works for text and small files; a large PDF or photo may not go through.
3. **Neither worked:** say it plainly, with one action: "Esse arquivo é grande demais pra eu subir daqui. Salva ele no seu Drive, na pasta **02. Clientes/<Nome>** — a pasta já existe — e me avisa. Eu leio de lá e anoto na ficha." When she says it's there, find it, read it, go on.

Check the file is in the folder before writing the sheet line. Note which path worked, and the file size, in the receipt.

### Step 4 — The sheet

Re-read the sheet, then:
- a file → one line under **Arquivos**: `- <nome> · <onde no Drive> · <o que importa> · YYYY-MM-DD`
- a fact she stated → one line in the right section (Quem é, Preferências, O que está aberto, Notas). Facts she states are written and mentioned in one line; anything inferred goes to /sistema as a pending item instead.

Update `atualizado:`. If something changed what's open or happened (a ticket issued, a quote sent), hand a milestone line to /contexto for the client's histórico.

### Step 5 — Receipt and report

`YYYY-MM-DD | guardar-no-cliente | arquivo / fato / recusado | <slug> · <caminho: pasta-local / conexao / manual> · <tamanho>` in `_sistema/log.md`.

Reply in one line: "Guardado na pasta da **<Nome>** e anotado na ficha."

## What this skill never does

- Saves before her **sim**.
- Writes a document number anywhere.
- Overwrites, deletes or moves her other files.
- Saves outside the client's Drive folder and sheet (plus the histórico hand-off and the receipt).
- Shares a file or changes who can see it.

## When to refuse

- Asked to save the number itself ("anota o número do passaporte") — "O número eu não guardo. O documento fica no Drive e eu anoto o vencimento e o que mais importar."
- Asked to share the file with the client — "Compartilhar fica com você. Eu guardo e organizo."

## Failure modes

- **No Drive folder for the client** (`drive: a criar`): offer to create it now (her Drive must be organized; else offer /organizar-drive); the fact or note still goes in the sheet.
- **Drive not connected:** save the knowledge in the sheet, say the file still needs a home, and keep the file name ready.
- **File unreadable:** save it, write "conteúdo não lido" on its line, ask what matters in it.

## STOP handling

On `PARAR` or `STOP`: halt, make no further writes, say what was saved, and wait.

## Headless behavior

Never runs headless; it needs her sim.

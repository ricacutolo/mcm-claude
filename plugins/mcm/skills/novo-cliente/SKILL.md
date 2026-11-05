---
name: novo-cliente
description: "MCM Client Book: cadastra um cliente dela — uma família, uma pessoa ou uma empresa — com uma ficha, um histórico e uma pasta no Drive. Se a conversa já era sobre esse cliente, aproveita tudo o que foi dito. Quando ela diz \"/novo-cliente\", \"novo cliente\", \"cadastra a família\", \"cadastra o cliente\", \"cria a ficha de\", \"esse é um cliente novo\", \"guarda esse cliente\"."
---

# novo-cliente — a home for each of her clients

Part of the **MCM Client Book**. Each of her clients gets one sheet (`ficha.md`), one histórico and one folder in her Drive, so Claude can answer "o que eu sei sobre a família Almeida?" without her re-explaining.

Where things live, for every client:
- **GoHighLevel** — contact data (names, e-mails, phones, birthdays), payments, campaigns. The sheet links there; it never copies it.
- **Google Drive** — the files themselves, in `02. Clientes/<Nome>/`.
- **Her Claude folder** — the knowledge: who they are, preferences, history, what's open, which files exist and what matters in them.

Speak Brazilian Portuguese, warm and plain. Say "a ficha do cliente", "o histórico", "a pasta do cliente no Drive"; never "ficha.md" or "slug".

## Read these first

Loaded only when this skill fires:

1. `departamentos/clientes/index.md` — to catch a duplicate. Missing means this is the first client.
2. `departamentos/clientes/brief.md` — only its Padrões (what she asks every new client). Missing means there is no Clientes department yet.
3. `sobre-mim/drive.md` — where `02. Clientes` is. Missing means her Drive is not organized yet.
4. This conversation — when it was already about this client, it is the main source.

## The rules

> "Nothing is written before her explicit sim to the drafted sheet."

> "Never copy ID, passport, card or bank numbers into any file. The sheet says the document exists and what matters in it, never the number."

> "Contact data lives in GoHighLevel. The sheet keeps a link, not a copy."

> "Only what she said goes in the sheet. Nothing inferred, nothing invented; a blank stays a blank."

## Workflow

### Step 0 — The Clientes department (first client only)

No `departamentos/clientes/brief.md`:

1. **One she already made.** Read `departamentos/index.md`. A department whose name or purpose is about her clients (cliente, clientes, contatos, CRM, carteira) → "Você já tem o departamento **<Nome>**. Posso usar ele como o seu departamento de Clientes? Eu mudo o nome da pasta para `clientes`, para o sistema sempre achar. (**sim** / **não, é outra coisa**)" On **sim**: move `departamentos/<slug>/` to `departamentos/clientes/` (move, never delete), fix its line in `departamentos/index.md`, and ask /contexto to update its histórico's `brief:` to `departamentos/clientes/brief.md` (the histórico keeps its name). Several candidates → short numbered list; she picks or says none.
2. **Clients already written inside it.** If that brief or its histórico lists clients with details (names plus who they are, trips, preferences): "Vi N clientes guardados no departamento: <nomes>. Quer que eu crie uma ficha para cada um? Um de cada vez, você confirma cada ficha." On **sim**, for each one run Steps 1-4 with what is written about them as the source (like mid-conversation). Never remove the original text on your own; when all are done, offer: "Posso mover a lista antiga para `_revisao/`? As fichas já têm tudo." Move on **sim**.
3. **None.** "Antes do primeiro cliente, vou criar o departamento **Clientes** — é onde fica o seu jeito de atender qualquer cliente (o que você pergunta sempre, seus passos). Pode ser?" On **sim**, run the /novo-departamento flow for `clientes`, then come back here.

### Step 1 — Match the name

Kebab-case slug, short, no accents (`familia-almeida`, `joao-silva`). Never `pesquisa`, `entregas` or `index` (those are department folders). If `departamentos/clientes/<slug>/ficha.md` exists: "Esse cliente já tem ficha. Quer abrir?" and stop. Also check `contexto/<slug>.md` doesn't already belong to another topic; if it does, add a suffix (`familia-almeida-cliente`).

### Step 2 — Gather

**Mid-conversation:** if this conversation already talked about this client, take everything she said about them — people, preferences, what was done (tickets, quotes, bookings), what was decided, what's open — and ask only what's missing.

**Otherwise**, one at a time, at most three:
1. "Quem faz parte? (nomes e quem é quem)"
2. "Como chegou até você, e desde quando?"
3. The first question from the department's Padrões, if it has one.

### Step 3 — Draft and wait

```markdown
---
tipo: cliente
slug: <slug>
status: ativo
contexto: contexto/<slug>.md
drive: 02. Clientes/<Nome>
ghl: <link do contato no GHL, ou "a ligar">
criado: YYYY-MM-DD
atualizado: YYYY-MM-DD
---

# <Nome do cliente>

## Quem é
- <Nome> — <papel> (ex.: "Felipe — pai")
- Como chegou: <...> · Desde: <...>

## Contato
No GoHighLevel: <link, ou "a ligar">

## Preferências
- <o que ama, o que não gosta, estilo, restrições — só o que ela disse>

## Histórico
<Resumo curto. O detalhe fica no histórico.>

## O que está aberto
- <o que ela deve fazer · o que o cliente deve · próxima conversa>

## Arquivos
_Os arquivos ficam no Drive, em 02. Clientes/<Nome>. Aqui fica o que importa em cada um._

## Notas
```

Show the draft, then: "Essa é a ficha da **<Nome>**. Posso criar? Também crio a pasta **02. Clientes/<Nome>** no seu Drive. (**sim** / ou me diz o que mudar)"

### Step 4 — Write, on sim only

1. Create `departamentos/clientes/<slug>/` and write `ficha.md` exactly as approved.
2. Re-read `departamentos/clientes/index.md` (create with `# Clientes` if missing), then add:
   `- [<Nome>](<slug>/ficha.md) · YYYY-MM-DD · ativo · <uma frase>`
3. Invoke /contexto to create `contexto/<slug>.md` with `tier: cliente` and `brief: departamentos/clientes/<slug>/ficha.md`. **Her sim covers it.** Mid-conversation: hand /contexto the capture of this conversation as the seed (its capture mode), not a one-line summary.
4. Drive: with `sobre-mim/drive.md`, create `<Nome>` inside `02. Clientes` (colored like its parent, per /organizar-drive's rule) and check it exists. Without `drive.md`: say "A pasta no Drive fica para quando o seu Drive estiver organizado — quer organizar agora?" (offers /organizar-drive) and set `drive: a criar`.

### Step 5 — Receipt

`YYYY-MM-DD | novo-cliente | criado / recusado / ja-existe | <slug> · drive: sim/não · da-conversa: sim/não` in `_sistema/log.md`.

### Step 6 — Report

```
**Cliente cadastrado — <Nome>**
Ficha, histórico e pasta no Drive prontos. Pode me mandar arquivos dele aqui no chat.
```

## What this skill never does

- Writes before her **sim**.
- Copies contact data from GHL, or any ID, passport, card or bank number.
- Invents a fact or fills a blank with a guess.
- Writes outside `departamentos/clientes/`, except the hand-off to /contexto, the Drive folder and the receipt.
- Contacts the client.

## When to refuse

- Already exists — "Esse cliente já tem ficha. Quer abrir?"
- Asked to store an ID, passport or card number — "O número eu não guardo. O documento fica no Drive e eu anoto o que importa nele."

## Failure modes

- **Folder offline:** draft in chat, write nothing, offer to write later in this conversation.
- **Drive not connected or not answering:** write the sheet and the histórico, set `drive: a criar`, say the Drive folder waits.
- **Long conversation, summarized:** say once that the early part of the chat is only a summary, and ask her to confirm anything important from it.

## STOP handling

On `PARAR` or `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: draft only, write nothing.

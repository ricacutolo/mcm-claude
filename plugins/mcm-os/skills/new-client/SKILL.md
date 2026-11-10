---
name: new-client
description: "MCM Client Book: adds one of her clients — a family, a person or a company — with a sheet, a history and a folder in her Drive. If the conversation was already about this client, it uses everything that was said. When she says \"/new-client\", \"new client\", \"add the … family\", \"add a client\", \"make a sheet for\", \"this is a new client\", \"save this client\"."
---

# new-client — a home for each of her clients

Part of the **MCM Client Book**. Each of her clients gets one sheet (`sheet.md`), one history and one folder in her Drive, so Claude can answer "what do I know about the Johnson family?" without her re-explaining.

Where things live, for every client:
- **MCM** — contact data (names, emails, phones, birthdays), payments, campaigns. The sheet links there; it never copies it.
- **Google Drive** — the files themselves, in `02. Clients/<Name>/`.
- **Her Claude folder** — the knowledge: who they are, preferences, history, what's open, which files exist and what matters in them.

Speak to her in plain, warm US English. Say "the client's sheet", "the history", "the client's folder in Drive"; never "sheet.md" or "slug".

## Read these first

Loaded only when this skill fires:

1. `departments/clients/index.md` — to catch a duplicate. Missing means this is the first client.
2. `departments/clients/brief.md` — only its Standards (what she asks every new client). Missing means there is no Clients department yet.
3. `about-me/drive.md` — where `02. Clients` is. Missing means her Drive is not organized yet.
4. This conversation — when it was already about this client, it is the main source.
5. The frontmatter of `context/*.md` — to find a history she already has about this client.

## The rules

> "Nothing is written before her explicit yes to the drafted sheet."

> "Never copy ID, passport, card or bank numbers into any file. The sheet says the document exists and what matters in it, never the number."

> "Contact data lives in MCM. The sheet keeps a link, not a copy."

> "Only what she said goes in the sheet. Nothing inferred, nothing invented; a blank stays a blank."

## Workflow

### Step 0 — The Clients department (first client only)

No `departments/clients/brief.md`:

1. **One she already made.** Read `departments/index.md`. A department whose name or purpose is about her clients (client, clients, contacts, CRM, roster) → "You already have the **<Name>** department. Can I use it as your Clients department? I'll rename the folder to `clients` so the system can always find it. (**yes** / **no, that's something else**)" On **yes**: move `departments/<slug>/` to `departments/clients/` (move, never delete), fix its line in `departments/index.md`, and ask /context to update its history's `brief:` to `departments/clients/brief.md` (the history keeps its name). Several candidates → short numbered list; she picks or says none.
2. **Clients already written inside it.** If that brief, its history or another file in its folder lists clients with details (names plus who they are, trips, preferences): "I see N clients saved in the department: <names>. Want me to make a sheet for each one? One at a time, and you confirm each sheet." On **yes**, for each one run Steps 1-4 with what is written about them as the source (like mid-conversation). Never remove the original text on your own; when all are done, offer: "Can I move the old list to `_review/`? The sheets have everything now." Move on **yes**.
3. **None.** "Before your first client, I'll set up the **Clients** department — that's where your way of serving any client lives (what you always ask, your steps). Sound good?" On **yes**, run the /new-department flow for `clients`, then come back here.

### Step 1 — Match the name

Kebab-case slug, short, no accents (`johnson-family`, `john-smith`). Never `research`, `deliverables` or `index` (those are department folders). If `departments/clients/<slug>/sheet.md` exists: "This client already has a sheet. Want to open it?" and stop. **A history already about them?** Match the name against the slug, `topic` and `aliases` of every `context/*.md`. One that is about this client → read it in full and use it as a source, like mid-conversation, and keep it as their history: "You already have a history about **<Name>**. I'll use it, and it becomes their history." Several → short numbered list; she picks one or says none. A `context/<slug>.md` about something else → add a suffix to the new slug (`johnson-family-client`).

**Already written somewhere else?** Look in `departments/clients/` for any other file about this client — anything that is not a `<slug>/sheet.md`, `brief.md` or `index.md` (e.g. a subfolder like `families/`). Found → read it in full and use it as the source, like mid-conversation: "I found what you'd already saved about **<Name>** in <file>. I'll use it as the starting point." After Step 4, offer: "Can I move the old file to `_review/`? The sheet has everything now." Move on **yes** (and its folder, when nothing else is left in it); never delete.

### Step 2 — Gather

**Mid-conversation:** if this conversation already talked about this client, take everything she said about them — people, preferences, what was done (tickets, quotes, bookings), what was decided, what's open — and ask only what's missing.

**Otherwise**, one at a time, at most three:
1. "Who's included? (names and who's who)"
2. "How did they find you, and since when?"
3. The first question from the department's Standards, if it has one.

### Step 3 — Draft and wait

```markdown
---
type: client
slug: <slug>
status: active
context: context/<slug>.md
drive: 02. Clients/<Name>
ghl: <contact link in MCM, or "to link">
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Client name>

## Who they are
- <Name> — <role> (e.g. "Mike — dad")
- How they found you: <...> · Since: <...>

## Contact
In MCM: <link, or "to link">

## Preferences
- <what they love, what they don't, style, restrictions — only what she said>

## History
<Short summary. The detail lives in the history.>

## What's open
- <what she needs to do · what the client owes · next conversation>

## Files
_The files live in Drive, in 02. Clients/<Name>. What matters in each one goes here._

## Notes
```

Show the draft, then: "Here's the sheet for **<Name>**. Can I create it? I'll also create the folder **02. Clients/<Name>** in your Drive. (**yes** / or tell me what to change)"

### Step 4 — Write, on yes only

1. Create `departments/clients/<slug>/` and write `sheet.md` exactly as approved.
2. Re-read `departments/clients/index.md` (create with `# Clients` if missing), then add:
   `- [<Name>](<slug>/sheet.md) · YYYY-MM-DD · active · <one sentence>`
3. Invoke /context to create `context/<slug>.md` with `tier: client` and `brief: departments/clients/<slug>/sheet.md`. **Her yes covers it.** If Step 1 found her history about this client, link it instead: /context sets its `tier` to `client` and its `brief` to the sheet, adds the client's name to `aliases`, and creates nothing; the file keeps its name and the sheet's `context:` points to it. Mid-conversation: hand /context the capture of this conversation as the seed (its capture mode), not a one-line summary.
4. Drive: with `about-me/drive.md`, create `<Name>` inside `02. Clients` (colored like its parent, per /organize-drive's rule) and check it exists. Without `drive.md`: say "The Drive folder will wait until your Drive is organized — want to organize it now?" (offers /organize-drive) and set `drive: to create`.

### Step 5 — Receipt

`YYYY-MM-DD | new-client | created / declined / already-exists | <slug> · drive: yes/no · from-chat: yes/no · history: new/linked` in `_system/log.md`.

### Step 6 — Report

```
**Client added — <Name>**
Sheet, history and Drive folder are ready. You can send me their files right here in the chat.
```

## What this skill never does

- Writes before her **yes**.
- Copies contact data from MCM, or any ID, passport, card or bank number.
- Invents a fact or fills a blank with a guess.
- Writes outside `departments/clients/`, except the hand-off to /context, the Drive folder and the receipt.
- Contacts the client.

## When to refuse

- Already exists — "This client already has a sheet. Want to open it?"
- Asked to store an ID, passport or card number — "I don't keep the number. The document lives in Drive, and I note what matters in it."

## Failure modes

- **Folder offline:** draft in chat, write nothing, offer to write later in this conversation.
- **Drive not connected or not answering:** write the sheet and the history, set `drive: to create`, say the Drive folder waits.
- **Long conversation, summarized:** say once that the early part of the chat is only a summary, and ask her to confirm anything important from it.

## STOP handling

On `STOP`: halt, make no further writes, say what was written, and wait.

## Headless behavior

With nobody watching: draft only, write nothing.

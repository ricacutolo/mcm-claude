---
name: save-to-client
description: "MCM Client Book: saves a file or a piece of information about one of her clients — the file goes to the client's folder in Drive and the sheet notes what matters in it. When she sends a file in the chat and says which client it's for, or says \"/save-to-client\", \"save to the client\", \"save this to the … family\", \"put this in the client's folder\", \"note it on …'s sheet\", \"this is for the … family\"."
---

# save-to-client — files and facts into the client's place

Part of the **MCM Client Book**. She sends a file or tells a fact about a client; it lands where it belongs: **the file in the client's Drive folder, the knowledge in the client's sheet.** She shouldn't have to know where anything lives.

Speak to her in plain, warm US English. Say "the client's folder in Drive", "the sheet".

## Read these first

Loaded only when this skill fires:

1. `departments/clients/index.md` — to match the client.
2. That client's `sheet.md` — `drive:` and the Files section.
3. The file she sent — enough to know what it is and what matters in it.

## The rules

> "Show what will be saved and where, and save only on her yes."

> "Never copy an ID, passport, card or bank number into the sheet or the chat. Write that the document exists and what matters (e.g. 'Sarah's passport — expires 03/2027')."

> "Never overwrite a file in her Drive. Same name → add the date to the new one."

> "Never delete anything, in her folder or her Drive."

## Workflow

### Step 1 — Which client, which thing

- Client from her words or the open client (/open-client). Unclear → one question: "Which client is this for?" No sheet → offer /new-client first.
- **A fact** ("Sarah doesn't eat seafood", "they travel in July"): skip to Step 4; it's a line for the sheet.
- **A file**: read it enough to name it and pull what matters (dates, names, places, deadlines, amounts she'd want to recall). Name it plainly: `<what it is> - <who> - YYYY-MM-DD.<ext>` ("Passport - Sarah - 2026-11-05.pdf").

### Step 2 — Show the plan

> "Here's what I'll save:
> **In Drive** (02. Clients/<Name>): <file name>
> **On the sheet**, under Files: <name> · <what matters>
> OK? (**yes** / **adjust**)"

### Step 3 — Save the file, on yes

Try in this order and stop at the first that works:

1. **Her Google Drive is on this computer** (a connected folder inside Google Drive for desktop, path with `GoogleDrive`/`Google Drive`) **and the file is readable here as a file:** copy it into `02. Clients/<Name>/`. No size limit.
2. **With the Google Drive connection:** create the file inside the client's folder. Works for text and small files; a large PDF or photo may not go through.
3. **Neither worked:** say it plainly, with one action: "This file is too big for me to upload from here. Please save it to your Drive, in the folder **02. Clients/<Name>** — the folder's already there — and let me know. I'll read it from there and note it on the sheet." When she says it's there, find it, read it, go on.

Check the file is in the folder before writing the sheet line. Note which path worked, and the file size, in the receipt.

### Step 4 — The sheet

Re-read the sheet, then:
- a file → one line under **Files**: `- <name> · <where in Drive> · <what matters> · YYYY-MM-DD`
- a fact she stated → one line in the right section (Who they are, Preferences, What's open, Notes). Facts she states are written and mentioned in one line; anything inferred goes to /system as a pending item instead.

Update `updated:`. If something changed what's open or happened (a ticket issued, a quote sent), hand a milestone line to /context for the client's history.

### Step 5 — Receipt and report

`YYYY-MM-DD | save-to-client | file / fact / declined | <slug> · <path: local-folder / connection / manual> · <size>` in `_system/log.md`.

Reply in one line: "Saved in **<Name>**'s folder and noted on the sheet."

## What this skill never does

- Saves before her **yes**.
- Writes a document number anywhere.
- Overwrites, deletes or moves her other files.
- Saves outside the client's Drive folder and sheet (plus the history hand-off and the receipt).
- Shares a file or changes who can see it.

## When to refuse

- Asked to save the number itself ("write down the passport number") — "I don't keep the number. The document lives in Drive, and I note the expiration date and anything else that matters."
- Asked to share the file with the client — "Sharing is up to you. I save it and keep it organized."

## Failure modes

- **No Drive folder for the client** (`drive: to create`): offer to create it now (her Drive must be organized; else offer /organize-drive); the fact or note still goes in the sheet.
- **Drive not connected:** save the knowledge in the sheet, say the file still needs a home, and keep the file name ready.
- **File unreadable:** save it, write "content not read" on its line, ask what matters in it.

## STOP handling

On `STOP`: halt, make no further writes, say what was saved, and wait.

## Headless behavior

Never runs headless; it needs her yes.

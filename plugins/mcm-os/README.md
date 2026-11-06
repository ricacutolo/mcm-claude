# MCM OS for Claude

MyClientMachine's work system inside Claude: Claude gets to know who you are, how your business works and how you write, organizes your work into departments (the ongoing stuff) and projects (the stuff that has an end), and keeps the history of every topic so any conversation picks up right where the last one left off.

## How to install (one time only)

1. Use the Claude desktop app on your computer, on a paid plan.
2. Create a folder for the system in your home folder (in Finder: **Shift + Command + H**, then **Shift + Command + N**), for example `Claude`. Avoid Documents and Desktop if they're synced to iCloud.
3. In Claude, open **Settings → Plugins → Add marketplace → Add from a repository** and paste: `ricacutolo/mcm-claude`
4. Enable the **MCM OS** plugin and turn on **Sync automatically**, so you get updates on your own.
5. If Rica prepared your files, they arrive in your Drive (folder **MCM - Deliverables**) and the install brings them into your folder with your yes. If he sent you a `_seed` folder some other way, put it inside the system folder.
6. Open a new conversation, add the folder you created and say: **start the install**.

The install goes in short steps. You can stop at any time and come back by saying **continue the install**.

## In everyday use

Chat with the folder connected. A few ways to start:

- **open Content** — goes into the department and tells you where you left off and the next step
- **what should I post next** · **set up my content**
- **write this in my voice…** — emails, messages, posts
- **how's my day looking** — calendar and important emails
- **new project** · **new department**
- **new client** · **open the … family** · **what do I know about…** — a sheet for each of your clients, with their history and a folder in Drive
- **save to the client…** — send a file in the chat and it goes to the client's folder in Drive, and the sheet notes what matters
- **save the meeting with…** — reads the meeting transcript in Google Meet and saves decisions, agreements and preferences to the client's sheet, and what clients think of your service on a single page, with your yes
- **this conversation is about…** — saves the whole conversation to the right topic, project or client
- **save this** — saves something to the topic's history
- **make my brand** — designs your logo from scratch with you and delivers the full kit: logo versions, colors, fonts and ready-to-use files
- **organize my Drive** — creates your business folders in Google Drive and puts loose files where they belong, always with your yes
- **update** — pulls in the latest notes Rica left in the shared document and shows them to you to approve

Without the folder connected, Claude works as usual, without the system.

## Safety

The system never sends, publishes or deletes anything on its own. Everything becomes a draft for you to approve, and anything that would be deleted goes to `_review/`.

## Credits

Created by Ricardo Cutolo (MyClientMachine). Parts adapted from Cowork AI OS and cowork-social by Nuno Tavares, under the MIT license.

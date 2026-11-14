# Guides for the content setup

The few things she does by hand, handed to her at the content setup steps listed below. Written so someone who has never used Canva or MCM can follow along. Claude gives them as numbered steps, one action each, with every link written as **Click here to open <the page> →** and filled in for her (her MCM app address and business from `ghl.md`, her files from `about-me/brand.md`). Never "Claude will open it for you": Claude can't open apps on her computer.

- **Guide 0** — first time in Canva (setup step 5)
- **Guide B** — brand fonts on a template, a hand fix, or dragging her logo into one design (setup steps 8 and 9, and any hand fix after a template or post design)
- **Guide C** — connect MCM to Claude (setup step 12)
- **Guide D** — connect your social accounts (Instagram, Facebook, LinkedIn when on) in MCM's Social Planner (setup step 13)
- **Guide E** — make your MCM key and put it in the settings file (setup step 19)

---

## Guide 0: First time in Canva

1. **Click here to open Canva →** (`https://www.canva.com/signup`) and sign up with the email you want your designs under. The free plan is enough to start.
2. Canva asks "What will you be using Canva for?" Pick **Work and business**.
3. If the next screens offer a team setup or a free Pro trial, skip them. A trial starts billing when it ends unless you cancel. The screens after this vary; skip anything that asks for payment details.

## Guide B: Fonts, hand fixes and your logo on a template

**Your brand fonts on a template** (optional, about 2 minutes per template):

1. **Click here to open the template →** (Claude gives one link per template).
2. Click a heading, hold Shift and click the other headings on that slide.
3. Click the font name on the top toolbar, search for your heading font (Claude tells you which) and click it.
4. Do the same for the body text, with your body font.
5. Repeat for each slide. If a font doesn't come up in the search, stop and tell Claude.

**A hand fix** (something Claude can't change from here, like the color of a line that's an image): Claude names the element and the slide, with the link to the design. Click it, change what Claude says, and you're done; Canva saves on its own.

**Your logo, when Claude can't bring it in itself** (setup step 8's fallback):

1. **Click here to open the logo design →**
2. In the narrow menu on the far left of the editor, click **Uploads** (if it isn't there, check **Apps** or **More**), then **Upload files**, and choose your logo file. Claude tells you which one.
3. Click your uploaded logo so it drops onto the page. Upload and drop your second version too (light for dark slides, color for light ones), if Claude asks for it.
4. Tell Claude it's in. Claude takes it from there and places it on every template.

Sources (Canva help): [brand fonts](https://www.canva.com/help/brand-fonts/), [uploading](https://www.canva.com/help/upload-media/). Canva moves buttons now and then; if a click isn't where the guide says, describe what you see and Claude finds it with you.

## Guide C: Connect MCM to Claude (about 3 minutes)

This lets Claude schedule your posts in MCM's Social Planner and read how they did. You approve everything on the sign-in screen that opens.

1. **Click here to open your plugins →** (`https://claude.ai/customize/plugins`) and open the MCM plugin.
2. Open its **Connectors** tab and click **Connect** next to MCM.
3. Sign in to MCM with your usual login.
4. Pick your business when it asks which account to give access to.
5. Approve the permissions. Make sure **social posts** are included, both reading and writing: that's what lets Claude schedule your posts.
6. Start a new conversation in Claude (the connection loads with a new conversation) and say **continue content setup**.

**If MCM isn't on the plugin's Connectors tab, or it won't connect** (fallback):

1. **Click here to open Connectors →** (`https://claude.ai/customize/connectors`) and choose **Add custom connector**.
2. Name it **MCM** and paste this address: `https://services.leadconnectorhq.com/mcp/anthropic/v2`. Save it.
3. Then steps 3 to 6 above.

## Guide D: Connect your social accounts in MCM (about 5 minutes)

This lets MCM's Social Planner put your approved posts on Instagram, Facebook and, if we turned it on, LinkedIn.

1. **Click here to open your Social Planner →** (Claude's link: `<MCM app address>/v2/location/<location ID>/marketing/social-planner`; if it doesn't land there: in MCM, **Marketing**, then **Social Planner**).
2. Connect **Instagram**, signing in with the account that runs your business.
3. Connect **Facebook** too if you post there, with the account that runs your business Page.
4. If we turned LinkedIn on, connect **LinkedIn** with your own personal profile, not a company page: profiles get far more reach there.
5. Approve what each one asks for, and say **done**. Claude checks your accounts itself.

## Guide E: Make your MCM key (about 5 minutes)

This key lets your computer send your finished designs to MCM. Treat it like a password: it goes only into the settings file in your content folder, never into the chat.

1. **Click here to open Private Integrations →** (Claude's link: `<MCM app address>/v2/location/<location ID>/settings/private-integrations`; if it doesn't land there: in MCM, **Settings**, then **Private Integrations**).
2. Click **Create new integration**, name it **Claude uploads**, and click **Next**.
3. In the permission list, search **medias** and tick **View Medias** and **Edit Medias**.
4. Click **Create**.
5. Your key shows **only once**: click **Copy** right away. If you lose it, just make a new one.
6. **Click here to open your settings file →** (Claude's link to the file in your content folder). Paste the key right after `GHL_PIT=`, with no spaces, and save.
7. Say **saved**. Claude only checks that a key is there, never what it says.

If your screen looks different, describe what you see and Claude finds it with you.

---
name: post-instagram
description: Rascunha uma legenda de Instagram na voz dela — gancho forte na primeira linha, texto, chamada e hashtags — mais a ideia do visual em palavras. Use quando ela disser "faz um post pro Instagram sobre", "legenda pro Insta", "post pro Instagram", "escreve um carrossel sobre", "roteiro de reels sobre", "transforma isso em post pro Insta". Só rascunho; nunca publica.
---

# post-instagram — an Instagram caption in her voice

Draft one Instagram post (caption, CTA, hashtags) plus the visual idea described in words. Drafts
only; she posts. Speak to her in Brazilian Portuguese.

## Read these first

Loaded only when this skill fires:

1. `sobre-mim/escrita.md` — her voice, and its **Por plataforma** section (Instagram).
2. `sobre-mim/negocio.md` — audience, pains, method, offers, real proof.
3. `${CLAUDE_PLUGIN_ROOT}/skills/ideias-de-post/hooks.md` — hook patterns and the first-words test.
4. `${CLAUDE_PLUGIN_ROOT}/skills/minha-voz/kill-list.md`.
5. `departamentos/conteudo/entregas/instagram/index.md` — if it exists, to avoid repeating a recent hook or topic.

## Instagram defaults (her `escrita.md` overrides any of these)

| Field | Default |
|---|---|
| Length | ~150-350 words; the hook lands in the first ~125 characters, before "mais" |
| Opening | a direct question or a short punchy line |
| Shape | hook → name the pattern → one reference in plain words → her own life → reframe or 2-3 steps → question back + CTA |
| Line breaks | short paragraphs, a blank line between them; reticências (…) for pauses |
| Emoji | rare, one or two at most |
| Hashtags | 4-8 in Portuguese at the end, mixing lowercase and CamelCase |
| CTA | her own ("Me conta nos comentários!", "Salva e compartilha com quem precisa", "Me chama no direct", "O link está na bio") — soft, after the value |
| Formats | caption (default); carrossel = numbered slide texts; reels = spoken script with short sentences and a turn |

An image is **not** required. Every draft ends with a **Visual** line: the photo, slide or scene idea in one or two sentences.

## The rules

> "Drafts only. This skill never posts, schedules or publishes."

> "Never invent a story, a testimonial, a quote or a number. Missing proof is a marked placeholder: [DEPOIMENTO REAL AQUI]."

> "Nothing is saved until she approves the draft."

## Workflow

### Step 1 — Understand the topic

From her message (or a handed-off idea from `ideias-de-post`): topic, format (legenda / carrossel / reels),
and any real story or fact to use. If the topic is missing, ask one question: "Sobre o que você quer falar?"

### Step 2 — Three hooks, she picks

Pick the three best patterns from `hooks.md`, write one hook per pattern, run the first-words test
and the kill-list scan on each, then show:

> "Três aberturas:
> 1. <gancho>
> 2. <gancho>
> 3. <gancho>
> Qual vai? Ou quer outras?"

Never show her the pattern names; they are for choosing, not for her.

### Step 3 — Write the full draft

Write it in her voice with the chosen hook, following the defaults and her `escrita.md`. Then a light
self-check before showing (this replaces a separate grader):

- Does the hook land in the first ~125 characters and pass the first-words test?
- Does it sound like her samples (register, *a gente*, feminine forms, her references)?
- One idea only? One clear CTA?
- 4-8 hashtags? Zero em dashes? Clean against the kill list?

Fix whatever fails, then show the draft plus the **Visual** line, and ask:

> "Tá bom assim, ou quer mudar algo?"

### Step 4 — Save (only after approval)

Save to `departamentos/conteudo/entregas/instagram/YYYY-MM-DD-<slug>.md` (create the folder and its
`index.md` with a `# Instagram` header on first use). If the Conteúdo department does not exist, save to
`entregas/` and say so.

File frontmatter:

```yaml
---
data: YYYY-MM-DD
rede: instagram
formato: legenda | carrossel | reels
gancho: <padrão>
status: rascunho
---
```

Body = the caption ready to copy, hashtags at the end, then `Visual: <idea>`.

Append to the folder's `index.md`: `- [<tema>](YYYY-MM-DD-<slug>.md) · YYYY-MM-DD · <tema em uma linha> (rascunho)`.

### Step 5 — Receipt

Append one line to `_sistema/log.md`:
`YYYY-MM-DD | post-instagram | rascunho salvo | <path>`

Shared memory: this skill does not write `contexto/`; if the Conteúdo log is open, `contexto` records the milestone.

Close with one line: "Quando quiser, é só copiar e postar. Quer uma versão pro LinkedIn também?"

## What this skill never does

- Post, schedule, publish or connect to a posting tool.
- Invent stories, testimonials, results, numbers or client names.
- Save before approval, or overwrite an existing draft (add `-2` to the slug instead).
- Use em dashes or more than 8 hashtags.

## When to refuse

- "Posta pra mim" — "Eu deixo pronto; postar é sempre com você."
- A fabricated testimonial or result — "Não posso inventar. Deixo o espaço marcado pra um depoimento real."

## Failure modes

- `escrita.md` missing: draft with a warm neutral tone, apply the kill list, flag once.
- Folder not connected: draft in chat only; nothing saved.
- Index unreadable: save the draft, skip the index line, and say so.

## STOP handling

On `STOP`: halt, make no further writes, say what was saved (path), and wait.

## Headless behavior

With nobody watching: draft into the run output with the strongest hook, save nothing.

---
Adapted from Nuno Tavares' Cowork AI OS / cowork-social (MIT).

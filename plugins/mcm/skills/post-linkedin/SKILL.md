---
name: post-linkedin
description: Rascunha um post de LinkedIn na voz dela, com o ângulo corporativo e de liderança — gancho forte, texto, pergunta no final. Use quando ela disser "post pro LinkedIn", "faz um post pro LinkedIn sobre", "escreve pro LinkedIn", "transforma isso em post pro LinkedIn", "versão LinkedIn desse post". Só rascunho; nunca publica.
---

# post-linkedin — a LinkedIn post in her voice

Draft one LinkedIn post: longer than Instagram, with the corporate and leadership angle, built to
start a conversation in the comments. Drafts only; she posts. Speak to her in Brazilian Portuguese.

## Read these first

Loaded only when this skill fires:

1. `sobre-mim/escrita.md` — her voice, and its **Por plataforma** section (LinkedIn).
2. `sobre-mim/negocio.md` — audience, pains, method, offers, real proof, her corporate background.
3. `${CLAUDE_PLUGIN_ROOT}/skills/ideias-de-post/hooks.md` — hook patterns and the first-words test.
4. `${CLAUDE_PLUGIN_ROOT}/skills/minha-voz/kill-list.md`.
5. `departamentos/conteudo/entregas/linkedin/index.md` — if it exists, to avoid repeating a recent hook or topic.
6. An existing Instagram draft, only when she asks for "a versão LinkedIn desse post".

## LinkedIn defaults (her `escrita.md` overrides any of these)

| Field | Default |
|---|---|
| Length | ~1,200-1,900 characters; hook within the first ~140 characters, before "ver mais" |
| Angle | the corporate and leadership side: teams, decisions, microgerenciamento, the exhausted executive ("No ambiente corporativo, a gente raramente fala sobre isso") |
| Shape | hook → the situation → the pattern named → one reference → her experience as an executive → what to do differently → question back |
| Line breaks | short paragraphs, generous white space |
| Emoji | none or one |
| Hashtags | 0-3 at the end |
| CTA | a real question that invites a comment; link to the offer only if she asks |
| Image | optional; add a **Visual** line only if one would help |

## The rules

> "Drafts only. This skill never posts, schedules or publishes."

> "Never invent a story, a testimonial, a quote or a number. Missing proof is a marked placeholder: [DEPOIMENTO REAL AQUI]."

> "Nothing is saved until she approves the draft."

## Workflow

### Step 1 — Understand the topic

From her message, a handed-off idea, or an Instagram draft to adapt. If adapting, keep the idea and
rewrite for LinkedIn (longer, corporate angle, fewer hashtags) rather than copying. If the topic is
missing, ask one question: "Sobre o que você quer falar?"

### Step 2 — Three hooks, she picks

Pick the three best patterns from `hooks.md` (bastidores, conceito com credencial and reframe fit
LinkedIn best), one hook each, first-words test and kill-list scan on each, then:

> "Três aberturas:
> 1. <gancho>
> 2. <gancho>
> 3. <gancho>
> Qual vai? Ou quer outras?"

Never show her the pattern names; they are for choosing, not for her.

### Step 3 — Write the full draft

Write it with the chosen hook, following the defaults and her `escrita.md`. Light self-check before
showing (this replaces a separate grader):

- Hook within the first ~140 characters, passes the first-words test?
- Sounds like her LinkedIn samples, with the leadership angle?
- One idea, ending in a real question?
- 0-3 hashtags? Zero em dashes? Clean against the kill list?

Fix what fails, show the draft, and ask:

> "Tá bom assim, ou quer mudar algo?"

### Step 4 — Save (only after approval)

Save to `departamentos/conteudo/entregas/linkedin/YYYY-MM-DD-<slug>.md` (create the folder and its
`index.md` with a `# LinkedIn` header on first use). If the Conteúdo department does not exist, save to
`entregas/` and say so.

File frontmatter:

```yaml
---
data: YYYY-MM-DD
rede: linkedin
gancho: <padrão>
origem: <ideia / post do Instagram de YYYY-MM-DD / tema dela>
status: rascunho
---
```

Body = the post ready to copy, line breaks preserved.

Append to the folder's `index.md`: `- [<tema>](YYYY-MM-DD-<slug>.md) · YYYY-MM-DD · <tema em uma linha> (rascunho)`.

### Step 5 — Receipt

Append one line to `_sistema/log.md`:
`YYYY-MM-DD | post-linkedin | rascunho salvo | <path>`

Shared memory: this skill does not write `contexto/`; if the Conteúdo log is open, `contexto` records the milestone.

## What this skill never does

- Post, schedule, publish or connect to a posting tool.
- Invent stories, testimonials, results, numbers or client names.
- Save before approval, or overwrite an existing draft (add `-2` to the slug instead).
- Use em dashes or more than 3 hashtags.

## When to refuse

- "Posta pra mim" — "Eu deixo pronto; postar é sempre com você."
- A fabricated case or result — "Não posso inventar. Deixo o espaço marcado pra um caso real."

## Failure modes

- `escrita.md` missing: draft in a warm, professional neutral tone, apply the kill list, flag once.
- Folder not connected: draft in chat only; nothing saved.
- Index unreadable: save the draft, skip the index line, and say so.

## STOP handling

On `STOP`: halt, make no further writes, say what was saved (path), and wait.

## Headless behavior

With nobody watching: draft into the run output with the strongest hook, save nothing.

---
Adapted from Nuno Tavares' Cowork AI OS / cowork-social (MIT).

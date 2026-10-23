---
name: ideias-de-post
description: Cinco ideias de post específicas, ligadas ao negócio e à voz dela, cada uma com gancho e a melhor rede. Use quando ela disser "me dá ideias de post", "não sei o que postar", "sobre o que eu posto essa semana", "ideias pro Instagram", "ideias pro LinkedIn", "tô sem ideia de conteúdo", "o que eu poderia falar".
---

# ideias-de-post — the front door for "não sei o que postar"

Five specific post ideas tied to her business, each with a hook, the best platform, and the skill to
run next. In Brazilian Portuguese. Ideas only; drafting happens in `post-instagram` / `post-linkedin`.

## Read these first

Loaded only when this skill fires:

1. `sobre-mim/negocio.md` — who she serves, their pains in their words, her method and offers, her real proof.
2. `sobre-mim/escrita.md` — her themes, references and the stories she tells (personal disclosures, corporate years).
3. `departamentos/conteudo/entregas/instagram/index.md` and `.../linkedin/index.md` — if they exist, the last 30 days, so no topic or hook repeats.
4. `departamentos/conteudo/pesquisa/index.md` — if it exists, ideas she saved before; one of the five may come from there.
5. `${CLAUDE_SKILL_DIR}/hooks.md` — the hook patterns.
6. `${CLAUDE_PLUGIN_ROOT}/skills/minha-voz/kill-list.md`.

If `negocio.md` is missing, say once: "Pra ideias boas eu preciso do arquivo do seu negócio. Quer rodar a instalação primeiro?" and stop unless she gives a topic.

## The rules

> "Specific, not generic. An idea any coach could post is rejected and replaced."

> "Never invent a client story, a testimonial or a number. Story ideas use only material already in her files, or ask her for the real story."

> "Ideas are saved only when she asks, and only after she approves."

## Workflow

### Step 1 — Generate five ideas, mixing angles

At least one of each where her files support it:

1. **Reframe of her core message** — produtividade com propósito vs. "fazer mais".
2. **A pattern named** — a sabotador, autossabotagem, piloto automático; the reader recognizes herself.
3. **Concept explained** — one reference (neurociência, Inteligência Positiva, an author) in plain language.
4. **Her own experience** — a real moment from her files (burnout, marathon, perfectionism, corporate life), reframed as the reader's lesson.
5. **Corporate / leadership angle** — for LinkedIn: teams, decisions, the executive who is exhausted.

If her files hold a mentee result she has already made public, one idea can be a proof story; otherwise
replace it with a second pattern or concept idea. Never leave fewer than five.

### Step 2 — Format each idea

```
**Ideia N — <título em uma linha>**
- Gancho: <uma frase de abertura real, não um resumo do tema>
- Por que funciona: <uma frase — que dor ou desejo toca>
- Melhor rede: <Instagram ou LinkedIn>
- Próximo passo: post-instagram / post-linkedin
```

Run the first-words test from `hooks.md` and the kill-list scan on every hook before showing.

### Step 3 — Present and ask

> "Qual dessas fala mais com você? Me diz o número, ou peço mais cinco."

If she picks a weaker one, write it anyway but say why in one line ("Essa tende a render menos que a 2, porque…").

### Step 4 — Hand off or save

- She picks a number → run `post-instagram` or `post-linkedin` with that idea; don't make her retype it.
- She says "salva essas" → show what will be saved, wait for her yes, then write
  `departamentos/conteudo/pesquisa/YYYY-MM-DD-ideias.md` (create `pesquisa/` and its `index.md` on first use)
  and append to `pesquisa/index.md`: `- [Ideias de post](YYYY-MM-DD-ideias.md) · YYYY-MM-DD · 5 ideias: <temas curtos>`.
  If the Conteúdo department does not exist, save to `entregas/` and say so.

### Step 5 — Receipt

Append one line to `_sistema/log.md`:
`YYYY-MM-DD | ideias-de-post | <ideias geradas / ideias salvas / entregue para post-X> | <path or ->`

Shared memory: this skill does not write `contexto/`; if the Conteúdo log is open, `contexto` records the milestone.

## What this skill never does

- Draft the full post (that is `post-instagram` / `post-linkedin`).
- Post, schedule or publish anything.
- Invent stories, testimonials, results or numbers.
- Save without her approval.

## When to refuse

- A request to post an idea directly — "Eu deixo pronto pra você; publicar é sempre com você."
- A request to make up a client case — "Não posso inventar um caso. Me conta um real, ou fico com outra ideia."

## Failure modes

- No content indexes yet: skip the repeat check and say nothing about it.
- Folder not connected: ideas in chat only; nothing saved.
- Thin `negocio.md`: generate from what is there and flag the one missing piece that would help most.

## STOP handling

On `STOP`: halt, make no further writes, say what was saved (if anything), and wait.

## Headless behavior

With nobody watching: generate the five ideas into the run output, save nothing.

---
Adapted from Nuno Tavares' Cowork AI OS / cowork-social (MIT).

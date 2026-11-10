---
name: estrategia-do-negocio
description: "A sessão de estratégia do negócio, no departamento CEO: primeiro uma pesquisa do mercado dela, depois uma conversa que decide o que ela vende primeiro, o formato, a duração e o preço, como vende, a ordem do lançamento e os próximos 90 dias. Grava a estratégia dela e, quando algo está decidido, o cérebro do negócio, com o sim dela. Oferecida no fim da instalação; também quando ela diz \"/estrategia-do-negocio\", \"vamos trabalhar na minha estratégia\", \"o que eu vendo primeiro\", \"quanto eu cobro\", \"planeja o meu lançamento\", \"pra onde o meu negócio está indo\", ou quando o plano dela muda."
---

# estrategia-do-negocio — the strategy session

Her business strategy is decided here, at the top of the system, in the **CEO** department. The departments (content, courses, marketing) carry it out; they don't decide it. In her words: "Você fica com a parte criativa; o CEO mantém o negócio no rumo."

It does one thing: **one strategy session, from research to a written strategy.** The first run sets the strategy; later runs revise it. Speak to her in plain, warm Brazilian Portuguese. Say "a sua estratégia", "a sua primeira oferta", "o cérebro do seu negócio"; never file names, "skill", "framework" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her.

## Read these first

Loaded only when this skill fires.

1. The business brain of the area in play (`sobre-mim/cerebro-do-negocio.md`, or `cerebro-do-negocio-<area>.md` per /sistema's **Áreas**) — what's already settled.
2. `departamentos/ceo/estrategia.md` (or `estrategia-<area>.md`) — if it exists, this is a revision: start from its Perguntas em aberto and Próximos 90 dias.
3. `departamentos/ceo/pesquisa/index.md` — research already done (Rica may have run it before a call).
4. `sobre-mim/sobre-mim.md` — her time, her situation, what she wants her role to be.
5. `${CLAUDE_SKILL_DIR}/playbook.md` — the frameworks. Read the section in play, not all of it.
6. Only when proposing what the departments should adjust: the briefs in `departamentos/index.md`.

## The rules (not negotiable, not relaxed for trusted runs)

> "Research before opinions. No price, format or competitor claim without the research step behind it, or her own numbers."

> "A guide, not a form. Every topic in /sistema's **Asking her things** shape: what we need and why, what I'd recommend, 'você já sabe isso, ou quer pensar junto comigo?'. Not knowing is the point of this session."

> "She decides. Recommend clearly, with the reason, then let her choose. Her choice is written as hers, even when it differs from the recommendation (note the recommendation under Perguntas em aberto only if she wants it kept)."

> "Nothing is written without her sim: the strategy at the end, the business brain changes in the same batch."

> "Only what's settled goes to the business brain. Still being decided → the strategy's Perguntas em aberto."

> "Never invent her numbers (audience, revenue, students, results). Unknown → ask, or 'a definir'."

## Workflow

### Step 1 — Where we start
- **First run, no CEO department yet:** say what it is in two lines ("O CEO é onde mora a estratégia do seu negócio: o que você vende primeiro, como, e o que vem depois. Os seus outros departamentos seguem ele.") and, on sim, create `departamentos/ceo/brief.md` in /novo-departamento's brief format: name **CEO**, área = her main business, Propósito "Manter a estratégia do negócio clara e atual, pra todo departamento trabalhar rumo ao mesmo próximo passo.", Rotinas "Revisar a estratégia depois da primeira turma de cada oferta, e a cada 90 dias.", O que eu uso aqui: "vamos trabalhar na minha estratégia". Add its index line under its área header, and hand /contexto the creation of `contexto/ceo.md` with "Departamento CEO criado." Her sim covers all three.
- **Revision:** "Da última vez decidimos <primeira oferta, preço>, e a pergunta em aberto era <…>. O que mudou?" Work only on what changed.
- Another business area in play: its own `estrategia-<area>.md`, same shape.
- Set expectations once: "Isso é uma conversa. Mais ou menos uma hora, e você pode parar quando quiser; eu guardo onde paramos."

### Step 2 — Research (she watches)
- Existing research in `departamentos/ceo/pesquisa/` from the last 60 days: summarize it in five lines and ask if anything's missing. Otherwise:
- "Primeiro eu vou olhar o seu mercado, pra gente decidir com fatos, não com chutes. Leva alguns minutos. Quer acompanhar?" Then search the web for:
  1. 4-6 real offers close to hers: who, what, format, length, price, the promise they lead with, link.
  2. Where her buyers gather and what they say they struggle with (forums, groups, reviews), in their words.
  3. Price anchors: the low, the middle, the premium.
- Save it as `departamentos/ceo/pesquisa/YYYY-MM-DD-<slug>.md` (sources linked, each claim next to its source), with its index line. Show the five-line summary: "Olha o que eu encontrei."
- Searching isn't available: say so in one line, ask her what she knows about her market, and mark prices "to be checked".

### Step 3 — The conversation
Go through what isn't settled yet, in this order, skipping what the business brain or the strategy already answers. One topic at a time, each in the guide shape, recommending from the playbook and the research:

1. **Where she is:** time per week, money and runway, the audience she already has, what she's tried.
2. **The first offer:** what, format, length, price (playbook 1-3). Recommend one, with the reason.
3. **The promise in one line.**
4. **How it sells:** the path to a sale, the money model, a guarantee (playbook 6).
5. **Launch order:** sell before build (playbook 4-5), with dates.
6. **Próximos 90 dias:** one number, the #1 priority, what stays out (playbook 7).
7. **Brain check:** for each brain section still "to be decided" (the promise, what buyers believe and have tried, how she sells, the money model), keep it if it fits her business, or mark it "não se aplica" if it doesn't.

She can stop at any topic: save what's agreed (Step 4) and put the rest in Perguntas em aberto.

### Step 4 — Write (gate)
- Show the strategy from `modelos/estrategia.md`, filled: decided items in her words, open ones under Perguntas em aberto, the research linked. A revision shows only what changes, plus its line for Mudanças (`YYYY-MM-DD — <what changed and why>`).
- In the same message, the business brain changes: only what's settled (the first offer and price under What I sell, the promise, how she sells, the money model, the 90-day goal, anti-goals), one line each.
- "Isso resume bem? Diga **sim** que eu salvo a sua estratégia e essas atualizações no cérebro do seu negócio, ou me diga o que mudar."
- On sim: copy the business brain to `_revisao/YYYY-MM-DD-cerebro-do-negocio.md` first, then write both. Strategy `updated:` set to today.

### Step 5 — Close
- CEO brief: Estado atual (today's date, one line: the first offer and the 90-day goal), Próximo passo (the first launch step), `updated:`.
- Departments that should follow it, one line each, as offers, never done here: "A sua estratégia de conteúdo ainda fala de <oferta antiga>; quer atualizar?" (conteúdo → /conteudo-estrategia). Nothing else changes.
- The first offer is a program (a course, cohort, group, workshop): "Quer começar a montar? A máquina de cursos desenha o programa e monta uma aula por vez." Run /curso-instalar on sim.
- Hand /contexto one line for `contexto/ceo.md`: `Estratégia <definida / revisada>: <primeira oferta, preço, formato>; 90 dias: <meta>. Em aberto: <a principal pergunta em aberto, ou nada>.`
- Receipt (below).

## Receipt

One line per run in `_sistema/log.md` (re-read the file first):

`YYYY-MM-DD | estrategia-do-negocio | set / revised / paused / stopped | <area> · first offer: <offer, price> · 90 days: <goal> · research: <file or none>`

## What this skill never does

- Decides for her, or writes a recommendation as her decision.
- States a competitor, price or market fact without the research behind it.
- Changes another department's files (content strategy, plan, briefs other than the CEO's). It only offers.
- Writes the business brain without her sim, or writes what's still open into it.
- Creates offers, pages, courses or products in MCM. That's other machines' work.
- Edits `sobre-mim/sobre-mim.md`, `escrita.md`, or anything in `contexto/`.

## When to refuse

- "Só me diz o que fazer" — recommend clearly anyway, one line why, and still let her choose: "Eu faria isso, e por quê. A decisão é sua."
- A guaranteed-income promise for her offer — "Eu não posso prometer resultado pros seus clientes por você. Vamos escrever uma promessa que você consegue cumprir."
- Legal or tax structure questions — "Essa é pra um contador ou advogado; eu anoto em Perguntas em aberto."

## Failure modes

- **She has no idea where to start:** begin with what people already ask her for help with; the first offer usually lives there.
- **Two businesses mixed in one answer:** ask which area this is for, and keep separate strategies.
- **The research finds nothing close:** say so plainly; widen one step (nearby niche, other country) and mark prices as rough.
- **The session runs long:** pause at a topic boundary, save what's agreed, resume from Perguntas em aberto.

## STOP handling

On `STOP`: halt, write nothing more. Say what's agreed so far and that it's not saved, and offer to save it.

## Headless behavior

It's a conversation, so it doesn't run unattended. With nobody watching: write one receipt line `paused` and nothing else.

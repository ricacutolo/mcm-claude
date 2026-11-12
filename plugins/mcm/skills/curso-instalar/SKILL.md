---
name: curso-instalar
description: "Prepara a máquina de cursos para um programa dela: o departamento Cursos, a conferência de que a estratégia já decidiu a primeira oferta (formato, duração, preço), aulas ao vivo gravadas com transcrição, e onde o curso vai ficar no MCM. Curta, retomável, e depois passa para o desenho do programa. Quando ela diz \"/curso-instalar\", \"configura o meu curso\", \"configura a máquina de cursos\", \"quero montar o meu programa\", \"vamos criar o meu curso\", ou quando a sessão de estratégia termina com um curso como primeira oferta."
---

# curso-instalar — getting the course machine ready

The course machine builds **what she sells** (a program, a course, a cohort), not the marketing for it. The strategy (what offer, format, length, price) is decided in the CEO department; this machine carries it out, one module at a time, just ahead of her students.

It does one thing: **get one program ready to be designed.** About 15 minutes. Speak to her in plain, warm Brazilian Portuguese. Say "o seu programa", "as suas aulas", "os seus alunos"; never file names, "skill" or a command name. Her platform is **MCM**: never say "GoHighLevel", "HighLevel" or "GHL" to her. Every question in /sistema's **Asking her things** shape.

## Read these first

1. `departamentos/ceo/estrategia.md` (or `estrategia-<area>.md` for the area in play) — the first offer.
2. The business brain of the area in play — who it's for, the promise.
3. `departamentos/cursos/index.md` — programs already set up (a second program reuses the department).
4. `_sistema/estado.md` — `reunioes:`.

## The rules

> "The strategy decides the offer; this machine never does. No first offer in the strategy → offer the strategy session first."

> "Nothing is written before her sim."

> "Live lessons are recorded with a transcript, or the feedback loop has nothing to learn from."

## Workflow

### Step 1 — The offer
- The strategy names a first offer that is a program (course, cohort, group, workshop, coaching program): show it in one line ("A sua primeira oferta: <o quê>, <formato>, <duração>, <preço>.") and confirm it's the one to build.
- No strategy, or no first offer in it: "Antes de montar, a sua estratégia precisa decidir o que você vende primeiro, em que formato e por quanto. É uma conversa de mais ou menos uma hora. Quer fazer agora?" Run /estrategia-do-negocio on sim; come back here when it ends. Otherwise stop.
- The first offer isn't something taught (a service, a product): "A sua primeira oferta não é um programa, então a máquina de cursos espera até ter um." Stop.

### Step 2 — The department and the program
- No Cursos department yet: on sim, create `departamentos/cursos/brief.md` in /novo-departamento's brief format: name **Cursos**, área = the strategy's área, Propósito "Montar e melhorar os programas que ela vende, um módulo por vez, a partir do que os alunos realmente precisam.", Rotinas "Fechar cada aula ao vivo no mesmo dia; revisar depois de cada módulo e de cada turma.", O que eu uso aqui: "desenha o meu programa", "próxima aula", "fecha a aula", "revisa o módulo". Index line under its area header; hand /contexto the creation of `contexto/cursos.md` ("Departamento Cursos criado.").
- The program: a slug from its name, `departamentos/cursos/<programa>/` with its `index.md`, and a line in `departamentos/cursos/index.md`.
- **The program's `index.md` is its progress file**, kept current by every course skill without asking (soft), the way content skills keep the Conteúdo brief current:

```markdown
# <Nome do programa>
aulas em: <meet | zoom | outro (colar)> · curso no MCM: <nome | ainda não criado>

## Onde está
_Em YYYY-MM-DD._
<turma N: aula X de Y feita, próxima data ao vivo, o que está em aberto>

## Próximo passo
<um movimento concreto para este programa>

## Turmas
- Turma 1 — <planejada | começou YYYY-MM-DD | terminou YYYY-MM-DD> · <n> alunos

## Arquivos
- [Programa](programa.md) · YYYY-MM-DD · <uma linha>
- [Aula 01: <título>](aulas/aula-01-<slug>.md) · <status>
```

- **The Cursos brief** keeps one Estado atual and Próximo passo for the whole department: the program that's most urgent (the nearest live date, else the most recent work), pointing to its progress file. With one program, it mirrors that program.

### Step 3 — Recording live lessons
- `reunioes: meet` → "As suas aulas ao vivo vão ser no Google Meet. Ligue **Transcrever a reunião** ao criar cada aula no Google Agenda; é isso que me deixa fechar cada aula pra você."
- `reunioes: zoom` → "As suas aulas ao vivo vão ser no Zoom. Grave cada uma na nuvem com a **Transcrição de áudio** ligada (configurações do Zoom, em **Gravação**); é isso que me deixa fechar cada aula pra você."
- Outro → "Para aulas ao vivo eu recomendo o Google Meet ou o Zoom com transcrição ligada: essas eu leio sozinho. Com outra ferramenta, você teria que colar a transcrição depois de cada aula. Quer mudar para as aulas?" Record her answer on the program's `aulas em:` line.

### Step 4 — Where it lives in MCM
- "O seu curso vai ficar no MCM, onde os seus alunos entram. Ele já está criado lá?" Record it on the program's `curso no MCM:` line. Not created → "Sem problema; quando as primeiras aulas estiverem prontas, eu monto lá com você."

### Step 5 — Close
- the program's progress (its `index.md`: **Onde está**, **Próximo passo**; see /curso-instalar): Onde está ("Configurado: <formato>, <duração>.") and Próximo passo ("Desenhar o programa"); Turmas "Turma 1 — planejada". Then the Cursos brief, as above.
- Offer the design: "Quer desenhar o programa agora? A gente vai da sua oferta até o mapa completo dos módulos." Run /curso-desenho on sim.
- Receipt.

## Receipt

`YYYY-MM-DD | curso-instalar | <program> · offer: <format, length, price> · lessons on: <tool> · MCM: <name or not created>` in `_sistema/log.md`.

## What this skill never does

- Decides or changes the offer, format, length or price.
- Creates anything in MCM.
- Writes outside the Cursos department, except /contexto's log and the receipt.

## STOP handling

On `STOP`: halt, write nothing more, say what was set up, and wait.

## Headless behavior

Needs her sim; never runs unattended.

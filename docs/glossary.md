# Glossary: mcm (Portuguese) ↔ mcm-os (English)

The two plugins are the same system in two languages. English (`mcm-os`) is the source of truth; every change lands there first and is translated into `mcm` in the same release. This table is the contract: a name in one column always maps to the same name in the other. `scripts/check-sync.py` uses it.

## Skills
| mcm (PT) | mcm-os (EN) |
|---|---|
| sistema | system |
| instalar | install |
| contexto | context |
| novo-departamento | new-department |
| abrir-departamento | open-department |
| novo-projeto | new-project |
| abrir-projeto | open-project |
| novo-cliente | new-client |
| abrir-cliente | open-client |
| guardar-no-cliente | save-to-client |
| resumo-da-reuniao | save-meeting |
| minha-voz | my-voice |
| morning-brief | morning-brief |
| atualizar | update |
| organizar-drive | organize-drive |
| brand-kit-designer | brand-kit-designer |
| conteudo-post | content-post |
| conteudo-estatico | content-static |
| conteudo-video | content-video |
| conteudo-plano | content-plan |
| conteudo-estrategia | content-strategy |
| conteudo-modelo | content-template |
| conteudo-revisao | content-review |
| conteudo-instalar | content-install |
| conteudo-newsletter | content-newsletter |
| conteudo-substack | content-substack |
| estrategia-do-negocio | business-strategy |
| curso-instalar | course-install |
| curso-desenho | course-design |
| curso-aula | course-lesson |
| curso-fechar-aula | course-close-lesson |
| curso-revisao | course-review |
| ideias-de-post, post-instagram, post-linkedin | retired in content machine v1 (MCM 0.4.0), no English edition |

## Folders and files in her folder
| mcm (PT) | mcm-os (EN) |
|---|---|
| `claude.md` | `claude.md` |
| `sobre-mim/` | `about-me/` |
| `sobre-mim/sobre-mim.md` | `about-me/about-me.md` |
| `sobre-mim/cerebro-do-negocio.md` (before 0.11.0: `negocio.md`) | `about-me/business-brain.md` (before 0.11.0: `business.md`) |
| `sobre-mim/cerebro-do-negocio-<area>.md` | `about-me/business-brain-<area>.md` |
| `sobre-mim/escrita.md` | `about-me/writing.md` |
| `sobre-mim/drive.md` | `about-me/drive.md` |
| `sobre-mim/marca.md` | `about-me/brand.md` |
| `departamentos/` | `departments/` |
| `departamentos/clientes/` | `departments/clients/` |
| `<client>/ficha.md` | `<client>/sheet.md` |
| `departamentos/clientes/reacoes.md` | `departments/clients/reactions.md` |
| `departamentos/ceo/` · `estrategia.md` · `estrategia-<area>.md` · `pesquisa/` | `departments/ceo/` · `strategy.md` · `strategy-<area>.md` · `research/` |
| shipped `estrategia-do-negocio/playbook.md` · `modelos/estrategia.md` | `business-strategy/playbook.md` · `templates/strategy.md` |
| `departamentos/cursos/` · `<programa>/programa.md` · `aulas/aula-NN-<slug>.md` · `perguntas.md` · `retorno.md` · `depoimentos.md` | `departments/courses/` · `<program>/program.md` · `lessons/lesson-NN-<slug>.md` · `faq.md` · `feedback.md` · `quotes.md` |
| program `index.md` fields `aulas em:` · `curso no MCM:` | `lessons on:` · `MCM course:` |
| program `index.md` (its progress file) sections `Onde está` · `Próximo passo` · `Turmas` (`Turma N — planejada / começou / terminou`) · `Arquivos` | `Where it stands` · `Next step` · `Rounds` (`Round N — planned / started / finished`) · `Files` |
| lesson status `planejada · materiais prontos · no MCM · dada · fechada` · quotes `precisa de permissão` / `pode usar` | `planned · materials ready · in MCM · taught · closed` · `needs permission` / `ok to use` |
| shipped `modelos/programa.md` · `modelos/aula.md` | `templates/program.md` · `templates/lesson.md` |
| `departamentos/conteudo/` | `departments/content/` |
| `departamentos/conteudo/configuracao.md` | `departments/content/setup.md` |
| `…/conteudo/estrategia.md` · `plano.md` · `calendario.md` · `ideias.md` | `…/content/strategy.md` · `plan.md` · `calendar.md` · `ideas.md` |
| `…/conteudo/modelos.md` · `estilo-da-marca.md` · `ghl.md` | `…/content/templates.md` · `brand-style.md` · `ghl.md` |
| `…/conteudo/fotos.md` (photo library index) · Drive: `Fotos de conteúdo` | `…/content/photos.md` · Drive: `Content photos` |
| photo library `tipo` column: `foto` · `gerada` | `type` column: `photo` · `generated` |
| `…/conteudo/estilo-de-foto.md` (her look for generated images) · plan section `Fotos para tirar` | `…/content/photo-style.md` · plan section `Photos to take` |
| shipped `conteudo-estrategia/image-prompts.md` | `content-strategy/image-prompts.md` |
| `…/conteudo/newsletters/edicao-NN-<slug>.md` · `ghl.md` § Newsletter | `…/content/newsletters/issue-NN-<slug>.md` · `ghl.md` § Newsletter |
| `…/conteudo/notas/nota-NN.md` · `ghl.md` § Substack (Endereço da publicação, Tags em uso) | `…/content/notes/note-NN.md` · `ghl.md` § Substack (Publication address, Tags in use) |
| `…/conteudo/desempenho.md` · `notas-da-biblioteca.md` · `swipe.md` | `…/content/performance-log.md` · `library-notes.md` · `swipe.md` |
| `…/conteudo/posts/` · `scripts/` · `.env` · `rodadas-anteriores/estrategia-rodada-<N>.md` | `…/content/posts/` · `scripts/` · `.env` · `past-rounds/strategy-round-<N>.md` |
| `contexto/conteudo.md` | `context/content.md` |
| Drive: `Vídeos de conteúdo/post-NN-<slug>` | Drive: `Content videos/post-NN-<slug>` |
| `projetos/` | `projects/` |
| `contexto/` | `context/` |
| `pesquisa/` | `research/` |
| `entregas/` | `deliverables/` |
| `entregas/planos/` | `deliverables/plans/` |
| `entregas/marca/` | `deliverables/brand/` |
| `referencia/` | `reference/` |
| `_sistema/` | `_system/` |
| `_sistema/estado.md` | `_system/state.md` |
| `_sistema/pendentes.md` | `_system/pending.md` |
| `_sistema/saude.md` | `_system/health.md` |
| `_sistema/log.md` | `_system/log.md` |
| `_sistema/drive/` | `_system/drive/` |
| `_revisao/` | `_review/` |
| `_semente/` | `_seed/` |
| `_semente/departamentos/<slug>/brief.md` | `_seed/departments/<slug>/brief.md` |
| `index.md` | `index.md` |
| `brief.md` | `brief.md` |
| skill folder `modelos/` | skill folder `templates/` |
| `conteudo-estrategia/platforms/<platform>.md` (shipped, one per platform; names stay English) | `content-strategy/platforms/<platform>.md` |
| plan column `final`: `pedido` · `leve: <qual>` (salvar, pergunta, compartilhar, seguir) · `nenhum` | `ends`: `ask` · `light: <which>` (save, question, share, follow) · `none` |
| strategy section Como os posts terminam | How posts end |
| `estilo-da-marca.md` § Visuais que ela gosta · Drive `04. Brand/Referências` · `departamentos/conteudo/referencias/` | `brand-style.md` § Looks she likes · Drive `04. Brand/References` · `departments/content/references/` |
| `sobre-mim/marca.md` line `Origem: criada aqui \| o logo dela (<file>)` | `about-me/brand.md` line `Source: designed here \| her own logo (<file>)` |
| `ghl.md` line `Endereço do app MCM (para os links diretos):` | `MCM app address (for direct links):` |

## State fields (`estado.md` → `state.md`)
| PT | EN |
|---|---|
| versao_plugin | plugin_version |
| instalacao: completa / incompleta | install: complete / incomplete |
| etapa_atual | current_step |
| iniciada | started |
| ultima_manutencao | last_upkeep |
| espelho_drive | drive_mirror |
| pasta_drive | drive_folder |
| reunioes: meet / zoom / outro | meetings: meet / zoom / other |
| notas_rica_lidas | rica_notes_read |
| aguardando semente | waiting for seed |
| pendente / feito | pending / done |

## Brief and log words
| PT | EN |
|---|---|
| Propósito | Purpose |
| Padrões | Standards |
| Rotinas | Routines |
| Decisões | Decisions |
| Estado atual | Current state |
| Próximo passo | Next step |
| atualizado: | updated: |
| histórico (the user's word for a log) | history |
| tier: tema / projeto / departamento / cliente | tier: topic / project / department / client |
| status: encerrado | status: closed |
| arquivado | archived |
| Ficha sections: Preferências, O que está aberto, Histórico, Arquivos | Preferences, What's open, History, Files |
| fechou / vai pensar / não | closed / thinking / no |
| plan idea cell in a newsletter-led cycle: `da newsletter N` · idea tag `para o post N` · post note `ciclo sem newsletter` | `from newsletter N` · `for post N` · `cycle fell back` |
| Substack Note: format `nota` · calendar `Nota do Substack N` · plan idea cell `do post M` · status `pulada` | `note` · `Substack note N` · `from post M` · `skipped` |
| plan Modelo cell for formats with no template: `reel` · `foto` | Template cell: `reel` · `photo` |
| format Headline photo, said to her as `foto com título` (template `TEMPLATE - Photo - headline`, token `[HEADLINE]`, names kept) | format `Headline photo` |
| plan and calendar status: `planejado` · `agendado` · `Agendado <time>` · `Publicado <date time>` | `planned` · `scheduled` · `Scheduled <time>` · `Published <date time>` |
| idea status: `não usada` · `usada: post N` · `descartada` | `unused` · `used: post N` · `dropped` |
| file sections: Modelos a criar · Planos anteriores · O que aprendemos · Totais da conta · Diferenças deliberadas do arquivo do negócio · Decidido por ela | Templates to build · Past plans · What we learned · Account totals · Deliberate differences from the business file · Decided for her |
| CEO strategy section Direções → Conteúdo: Para que serve o conteúdo agora · Aponta para · Público a crescer · Fica de fora | Directions → Content: What content is for now · Points to · Audience to grow · Stays out |
| content strategy lines `Segue: estratégia do CEO de <date>` · `Segue: sem estratégia do CEO ainda (arquivo do negócio)` · `Sessão do CEO oferecida:` · section Diferenças deliberadas da direção do CEO | `Follows: CEO strategy of <date>` · `Follows: no CEO strategy yet (business file)` · `CEO session offered:` · Deliberate differences from the CEO's direction |
| `departamentos/ceo/relatorios.md` (sections Abertos · Resolvidos; shipped `estrategia-do-negocio/modelos/relatorios.md`) | `departments/ceo/reports.md` (Open · Settled; `business-strategy/templates/reports.md`) |
| receipt tag `ceo: avisada <date>` | `ceo: told <date>` |
| post.md steps: Ideia · Texto · Design · Agendamento · Resultados (reel: Roteiro · Gravação · Takes · Corte) | Idea · Copy · Design · Schedule · Results (reel: Script · Recording · Takes · Cut) |
| area: (frontmatter) | area: |
| Áreas (sistema section) | Areas (system section) |
| Pessoal | Personal |
| area: nenhuma · ## Sem área | area: none · ## No area |
| Meu negócio <Área> (notes section) | My business <Area> |
| sem dono / sem data | no owner / no date |

## Her Drive
| PT | EN |
|---|---|
| MCM - Deliverables / Semente | MCM - Deliverables / Seed |
| MCM - Notas do Rica | MCM - Rica's Notes |
| MCM - System Health Report | MCM - System Health Report |
| 01. Documentos da Empresa | 01. Company Documents |
| 02. Clientes | 02. Clients |
| 03. Vendas e Marketing | 03. Sales and Marketing |
| 04. Brand | 04. Brand |
| 05. Processos (SOPs) | 05. Processes (SOPs) |
| 06. Financeiro e Impostos | 06. Finance and Taxes |
| 07. Referências | 07. References |
| z - arquivo | z - archive |

## Words said to her
| PT | EN |
|---|---|
| sim (her approval word) | yes |
| ajustar | adjust |
| o sistema · o brief do departamento · a lista · o histórico | the system · the department brief · the list · the history |
| começar a instalação / continuar a instalação | start the install / continue the install |
| abre o Conteúdo | open Content |
| Configurações → Plugins → Adicionar marketplace | Settings → Plugins → Add marketplace |
| Instruções para o Claude | Instructions for Claude |
| Responde com **1** ou **2**: · Ou me conta o que você está pensando. | Reply with **1** or **2**: · Or tell me what you're thinking. |
| **Clique aqui para abrir <a página> →** | **Click here to open <the page> →** |
| vamos fazer o próximo post · transforma isso em post | let's make the next post · make this a post |
| eu já tenho um logo · usa o meu logo · coloca a minha marca | I have a logo · use my logo · add my brand |
| quero fazer reels | I want to make reels |
| [Ligado] · [Desligado] (strategy draft marks) | [On] · [Off] |
| post table: Este post · Quando · Tema · Tipo de post · Formato · Vai para · Termina com | This post · When · Topic · Kind of post · Format · Goes to · Ends with |

Tone in English: warm, plain, US English, no jargon. The English edition speaks to US small-business owners; the Portuguese one to Brazilian ones. Never translate word for word when a phrase reads stiff; keep the meaning and the rule.

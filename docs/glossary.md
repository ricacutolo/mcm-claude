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
| ideias-de-post, post-instagram, post-linkedin | retired in content machine v1 (MCM 0.4.0), no English edition |

## Folders and files in her folder
| mcm (PT) | mcm-os (EN) |
|---|---|
| `claude.md` | `claude.md` |
| `sobre-mim/` | `about-me/` |
| `sobre-mim/sobre-mim.md` | `about-me/about-me.md` |
| `sobre-mim/negocio.md` | `about-me/business.md` |
| `sobre-mim/negocio-<area>.md` | `about-me/business-<area>.md` |
| `sobre-mim/escrita.md` | `about-me/writing.md` |
| `sobre-mim/drive.md` | `about-me/drive.md` |
| `sobre-mim/marca.md` | `about-me/brand.md` |
| `departamentos/` | `departments/` |
| `departamentos/clientes/` | `departments/clients/` |
| `<client>/ficha.md` | `<client>/sheet.md` |
| `departamentos/clientes/reacoes.md` | `departments/clients/reactions.md` |
| `departamentos/conteudo/` | `departments/content/` |
| `departamentos/conteudo/configuracao.md` | `departments/content/setup.md` |
| `…/conteudo/estrategia.md` · `plano.md` · `calendario.md` · `ideias.md` | `…/content/strategy.md` · `plan.md` · `calendar.md` · `ideas.md` |
| `…/conteudo/modelos.md` · `estilo-da-marca.md` · `ghl.md` | `…/content/templates.md` · `brand-style.md` · `ghl.md` |
| `…/conteudo/fotos.md` (photo library index) · Drive: `Fotos de conteúdo` | `…/content/photos.md` · Drive: `Content photos` |
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
| plan and calendar status: `planejado` · `agendado` · `Agendado <time>` · `Publicado <date time>` | `planned` · `scheduled` · `Scheduled <time>` · `Published <date time>` |
| idea status: `não usada` · `usada: post N` · `descartada` | `unused` · `used: post N` · `dropped` |
| file sections: Modelos a criar · Planos anteriores · O que aprendemos · Totais da conta · Diferenças deliberadas do arquivo do negócio · Decidido por ela | Templates to build · Past plans · What we learned · Account totals · Deliberate differences from the business file · Decided for her |
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

Tone in English: warm, plain, US English, no jargon. The English edition speaks to US small-business owners; the Portuguese one to Brazilian ones. Never translate word for word when a phrase reads stiff; keep the meaning and the rule.

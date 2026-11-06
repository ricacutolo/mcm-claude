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
| ideias-de-post, post-instagram, post-linkedin | retired in content machine v1, no English edition |

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

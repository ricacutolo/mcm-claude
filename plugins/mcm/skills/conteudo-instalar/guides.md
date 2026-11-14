# Guias da configuração do conteúdo

O pouco que ela faz com as próprias mãos, entregue nas etapas da configuração do conteúdo listadas abaixo. Escritos para quem nunca usou o Canva nem o MCM. Claude passa como passos numerados, uma ação em cada, com todo link escrito como **Clique aqui para abrir <a página> →** e já preenchido para ela (o endereço do app MCM e o negócio dela, de `ghl.md`; os arquivos dela, de `sobre-mim/marca.md`). Nunca "o Claude abre para você": o Claude não abre aplicativos no computador dela.

Os nomes dos botões aparecem primeiro em português e, entre parênteses, em inglês, porque o Canva, o Claude e o MCM podem estar em qualquer um dos dois idiomas na tela dela.

- **Guia 0** — primeira vez no Canva (etapa 5)
- **Guia B** — fontes da marca num modelo, um ajuste à mão, ou arrastar o logo para um design (etapas 8 e 9, e qualquer ajuste à mão depois de um modelo ou do design de um post)
- **Guia C** — conectar o MCM ao Claude (etapa 12)
- **Guia D** — conectar as suas redes (Instagram, Facebook, LinkedIn quando ligado) no Social Planner do MCM (etapa 13)
- **Guia E** — criar a sua chave do MCM e colocar no arquivo de configurações (etapa 19)

---

## Guia 0: Primeira vez no Canva

1. **Clique aqui para abrir o Canva →** (`https://www.canva.com/signup`) e cria a conta com o e-mail em que você quer os seus designs. O plano grátis basta para começar.
2. O Canva pergunta para que você vai usar. Escolhe **Trabalho e negócios** (Work and business).
3. Se as próximas telas oferecerem configurar uma equipe ou um teste grátis do Pro, pula. O teste começa a cobrar quando acaba, a não ser que você cancele. As telas seguintes mudam; pula qualquer uma que peça dados de pagamento.

## Guia B: Fontes, ajustes à mão e o seu logo num modelo

**As fontes da sua marca num modelo** (opcional, uns 2 minutos por modelo):

1. **Clique aqui para abrir o modelo →** (o Claude passa um link por modelo).
2. Clica num título, segura Shift e clica nos outros títulos do slide.
3. Clica no nome da fonte na barra de cima, procura a sua fonte de título (o Claude diz qual) e clica nela.
4. Faz o mesmo com o texto, com a sua fonte de texto.
5. Repete em cada slide. Se uma fonte não aparecer na busca, para e avisa o Claude.

**Um ajuste à mão** (algo que o Claude não consegue mudar daqui, como a cor de uma linha que é imagem): o Claude diz qual elemento e em qual slide, com o link do design. Clica nele, muda o que o Claude disse, e pronto; o Canva salva sozinho.

**O seu logo, quando o Claude não consegue trazer sozinho** (o plano B da etapa 8):

1. **Clique aqui para abrir o design do logo →**
2. No menu estreito à esquerda do editor, clica em **Uploads** (se não estiver lá, olha em **Apps** ou **Mais** (More)), depois em **Enviar arquivos** (Upload files), e escolhe o arquivo do seu logo. O Claude diz qual.
3. Clica no logo enviado para ele entrar na página. Envia e coloca a segunda versão também (clara para slides escuros, colorida para os claros), se o Claude pedir.
4. Avisa o Claude que está lá. Ele cuida do resto e coloca o logo em todos os modelos.

Fontes (ajuda do Canva, em inglês): [fontes da marca](https://www.canva.com/help/brand-fonts/), [enviar arquivos](https://www.canva.com/help/upload-media/). O Canva muda os botões de lugar de vez em quando; se um clique não estiver onde o guia diz, descreve o que você vê e o Claude acha com você.

## Guia C: Conecte o MCM ao Claude (uns 3 minutos)

Isso deixa o Claude agendar os seus posts no Social Planner do MCM e ver como eles foram. Você aprova tudo na tela de login que abrir.

1. **Clique aqui para abrir os seus plugins →** (`https://claude.ai/customize/plugins`) e abre o plugin MCM.
2. Abre a aba **Conectores** (Connectors) e clica em **Conectar** (Connect) ao lado do MCM.
3. Entra no MCM com o seu login de sempre.
4. Escolhe o seu negócio quando ele perguntar a qual conta dar acesso.
5. Aprova as permissões. Confere que **posts de redes sociais** (social posts) estão incluídos, para ler e escrever: é isso que deixa o Claude agendar os seus posts.
6. Começa uma conversa nova no Claude (a conexão carrega numa conversa nova) e diz **continua a configuração do conteúdo**.

**Se o MCM não estiver na aba Conectores do plugin, ou não conectar** (plano B):

1. **Clique aqui para abrir os Conectores →** (`https://claude.ai/customize/connectors`) e escolhe **Adicionar conector personalizado** (Add custom connector).
2. Dá o nome **MCM** e cola este endereço: `https://services.leadconnectorhq.com/mcp/anthropic/v2`. Salva.
3. Depois, os passos 3 a 6 de cima.

## Guia D: Conecte as suas redes no MCM (uns 5 minutos)

Isso deixa o Social Planner do MCM colocar os seus posts aprovados no Instagram, no Facebook e, se a gente ligou, no LinkedIn.

1. **Clique aqui para abrir o seu Social Planner →** (o link do Claude: `<endereço do app MCM>/v2/location/<ID do local>/marketing/social-planner`; se não cair lá: no MCM, **Marketing**, depois **Social Planner**).
2. Conecta o **Instagram**, entrando com a conta do seu negócio.
3. Conecta o **Facebook** também, se você posta lá, com a conta que administra a Página do seu negócio.
4. Se a gente ligou o LinkedIn, conecta o **LinkedIn** com o seu perfil pessoal, não uma página de empresa: perfis alcançam muito mais gente lá.
5. Aprova o que cada um pedir, e diz **pronto**. O Claude confere as suas contas sozinho.

## Guia E: Crie a sua chave do MCM (uns 5 minutos)

Essa chave deixa o seu computador mandar os seus designs prontos para o MCM. Trata como uma senha: ela vai só no arquivo de configurações da sua pasta de conteúdo, nunca no chat.

1. **Clique aqui para abrir as Integrações privadas →** (o link do Claude: `<endereço do app MCM>/v2/location/<ID do local>/settings/private-integrations`; se não cair lá: no MCM, **Configurações** (Settings), depois **Integrações privadas** (Private Integrations)).
2. Clica em **Criar nova integração** (Create new integration), dá o nome **Claude uploads** e clica em **Próximo** (Next).
3. Na lista de permissões, procura **medias** e marca **View Medias** e **Edit Medias**.
4. Clica em **Criar** (Create).
5. A sua chave aparece **uma vez só**: clica em **Copiar** (Copy) na hora. Se perder, é só criar outra.
6. **Clique aqui para abrir o seu arquivo de configurações →** (o link do Claude para o arquivo na sua pasta de conteúdo). Cola a chave logo depois de `GHL_PIT=`, sem espaços, e salva.
7. Diz **salvei**. O Claude só confere que tem uma chave lá, nunca o que ela diz.

Se a sua tela estiver diferente, descreve o que você vê e o Claude acha com você.

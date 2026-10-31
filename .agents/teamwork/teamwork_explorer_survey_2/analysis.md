# Auditoria Linguística e Mapeamento de Padrões de AI Slop

**Projeto:** Seminário Red Team 1 — Recon & OSINT  
**Escopo:** Auditoria textual completa de todos os 54 slides (12 arquivos HTML em `slides/`)  
**Metodologia e Referência:** Skill `/no-ai-slop` (`/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md` e `eval.md`)  
**Data da Auditoria:** 31 de Outubro de 2026  
**Auditor:** Explorer 2 (Auditor Linguístico e Mapeador de Padrões)

---

## 1. Diagnóstico Textual Global: Voz Original vs. "Verniz de IA"

### 1.1. A Voz Original e o Propósito do Seminário
O projeto é um seminário acadêmico/técnico de segurança ofensiva, estruturado para 45 minutos de apresentação oral por 5 graduandos/pesquisadores (Geovana, Emilio, Daniel, João Pedro Gonçalves e João Pedro Almeida).
O conteúdo subjacente (documentado no roteiro e no repositório) possui grande valor técnico e didático:
- Fundamentos de redes explicados visualmente (IP, portas, pacotes TCP, handshake);
- Prática com ferramentas de linha de comando e análise de tráfego (Nmap, Wireshark, Shodan, Censys, Subfinder);
- Discussão de inteligência em fontes abertas (OSINT, Certificate Transparency, metadados EXIF);
- Estudos de caso históricos de grande repercussão (vazamento de credenciais do Smart Sampa, spear-phishing da RSA SecurID, mapa de calor militar do Strava);
- Demonstrações de geolocalização e correlação em grafo (GEOSINT, nós de OSINT);
- Dicas operacionais de segurança defensiva e privacidade (OpSec, 2FA, gerenciamento de senhas).

### 1.2. A Camada de "Verniz de IA" (AI Slop)
Ao ser redigida e polida via modelos de linguagem, a apresentação foi recoberta por uma camada homogênea de clichês estilísticos de IA. O texto perdeu o tom espontâneo e didático de estudantes apresentando um projeto técnico e assumiu uma postura híbrida de "palestra motivacional TEDx", "trailer cinematográfico dramático" e "manual corporativo hiper-defensivo".

Os vícios mais graves diagnosticados globalmente são:

1. **A Máquina de Contrastes Binários ("Não é X, é Y")**: A apresentação sofre de uma obsessão mecânica por definições negativas seguidas de revelações antitéticas. O padrão aparece mais de 25 vezes ao longo dos slides. Em vez de explicar o que um conceito faz, o slide prefere afirmar pomposamente o que ele *não é* para em seguida lançar um aforismo.
2. **Ritmo Robótico e Colon Reveals em Série**: Nos blocos conceituais (Ciclo de OSINT e Técnicas Passivas), a estrutura textual foi clonada com rigidez matemática: `[Verbo/Substantivo]: [Frase de efeito]`. Todos os slides seguem rigorosamente a mesma métrica frasal.
3. **Fragmentação Telegráfica Dramática ("X. Y.")**: Títulos e subtítulos abusam de frases curtas sem verbo ou emparelhamento de números e substantivos para simular profundidade e impacto ("Três hipóteses. Uma coordenada.", "Vinte minutos de coleta. Um grafo.", "58 mil câmeras. 11 meses de senhas expostas.").
4. **Aforismos Filosóficos Inflados (Fake-profound kickers)**: Criação de máximas de sabedoria pretensamente profundas ("Todo ataque começa com uma pergunta", "O exploit é a confiança", "OSINT é uma peça. O tabuleiro é maior.", "O dado mais perigoso é aquele que parece inofensivo", "OpSec é higiene, não evento").
5. **Hiper-Hedged Legalism (Engessamento Defensivo Burocrático)**: No bloco de ferramentas, cada slide foi blindado com disclaimers defensivos idênticos repetidos 6 vezes ("Cenário fictício", "DADOS FICTÍCIOS", "registros não confirmam a situação atual"), gerando rigidez e tédio.
6. **Poluição por Travessões (47 Em Dashes)**: O travessão (`—`) foi usado como muleta rítmica compulsiva para quebrar orações e criar pausas de suspense artificial.
7. **Direção Cênica nas Notas do Orador**: Nas notas para o apresentador, a IA chegou a prescrever literalmente: `"Pausa dramática: deixar a frase no telão por alguns segundos"` (slide 44), evidenciando a artificialidade da construção.

---

## 2. Catálogo Sistemático de Padrões Violados (Conforme Skill `/no-ai-slop`)

| Categoria do Padrão | Descrição segundo a Skill | Ocorrências Identificadas nos Slides | Gravidade |
| :--- | :--- | :---: | :---: |
| **Binary contrasts** | *"This is not X. It's Y." / "X, não Y"*. Afirme Y diretamente sem a muleta da negação prévia. | 28 ocorrências explícitas | **Crítica** |
| **Colon reveals** | Sintagma nominal + dois pontos + revelação dramática em caixa baixa. | 18 ocorrências em títulos/subtítulos | **Alta** |
| **Dramatic fragmentation** | Frases cortadas artificialmente para dar impacto (*"X. And Y. And Z."*). | 16 ocorrências em títulos e chamadas | **Alta** |
| **Fake-profound kickers** | Aforismos e frases de efeito de "mic-drop" que fecham a ideia com metáfora fútil. | 14 ocorrências | **Alta** |
| **Robotic rhythm** | Repetição de formas sintáticas e layouts idênticos em slides consecutivos. | 2 blocos inteiros (Ciclo OSINT e Ferramentas) | **Crítica** |
| **Banned words & adverbs** | Palavras banidas expressas como *acionável* e advérbios/jargões vazios. | *acionável* (2x), *ecossistema* (5x), *fricção* (1x) | **Média** |
| **Em dashes excessivos (—)** | Uso desmedido do travessão como muleta de ritmo e contraste em textos curtos. | 47 ocorrências catalogadas | **Alta** |
| **Faux-insight & Throat-clearing** | Preparação retórica do tipo *"O que ninguém te conta"*, *"Três coisas que você precisa saber"*. | 6 ocorrências | **Média** |
| **Formatting / Defensive Slop** | Repetição mecânica de avisos burocráticos ("Cenário fictício", "dados fictícios"). | Presente em 6 slides consecutivos | **Alta** |

---

## 3. Auditoria Detalhada Slide a Slide (54 Slides / 12 Arquivos)

### Bloco 00: Abertura e Agenda (`slides/00-abertura.html`)

#### Slide 01 · Capa (Linhas 4–58)
- **Trecho Citado:** `"Tudo o que o alvo revela antes de ser atacado."` (Linha 10)  
  - **Padrão:** *Dramatic fragmentation / Aphoristic tagline*.
  - **Crítica:** Tagline pretensiosa e melodramática típica de IA para apresentações de cibersegurança.
  - **Recomendação:** Substituir por um subtítulo direto e informativo: *"Identificação de superfície de ataque e coleta em fontes abertas"*.
- **Trecho Citado (Notas):** `"Provocar: “antes de qualquer ataque, alguém passou semanas só olhando”."` (Linha 53)  
  - **Padrão:** *Theatrical metadiscourse*.
  - **Recomendação:** Tornar a nota natural para o apresentador: explicar que a maior parte do tempo em um teste de invasão é gasta em reconhecimento.

#### Slide 02 · Agenda (Linhas 63–123)
- **Trecho Citado:** `"Seis blocos.<br />Uma pergunta: <em class="red">o que o alvo já contou?</em>"` (Linha 70)  
  - **Padrão:** *Dramatic fragmentation* + *Colon reveal*. Fórmula clássica de IA: `[Número + Substantivo]. [Número + Substantivo]: [pergunta de impacto]`.
  - **Recomendação:** *"Roteiro da apresentação: como o reconhecimento mapeia a superfície de ataque"*.
- **Trecho Citado:** `"Redes, portas, Nmap e Wireshark — quando o alvo responde."` (Linha 90)  
  - **Padrão:** *Em dash as rhythmic crutch*.
  - **Recomendação:** Retirar o travessão decorativo: *"Reconhecimento ativo: varredura de portas e análise de tráfego com Nmap e Wireshark"*.
- **Trecho Citado:** `"O rastro que você deixa — e como reduzir."` (Linha 110)  
  - **Padrão:** *Em dash as rhythmic crutch*.
  - **Recomendação:** *"Práticas de OpSec para redução da exposição digital"*.

---

### Bloco 01: Conceito e Contexto (`slides/01-conceito-contexto.html`)

#### Slide 03 · Divisor 01 (Linhas 4–23)
- **Trecho Citado:** `<h2 class="statement">Todo ataque começa com uma pergunta.</h2><p class="lede">Reconhecer é descobrir a resposta antes de tocar no alvo.</p>` (Linhas 9–10)  
  - **Padrão:** *Fake-profound kickers / Aphorism setup*.
  - **Crítica:** Pseudo-filosofia barata. "Todo ataque começa com uma pergunta" soa artificial e vazio.
  - **Recomendação:** Ir direto ao ponto técnico: *"Conceito e contexto: o papel do reconhecimento na segurança ofensiva"*.

#### Slide 04 · Era das Mídias Sociais (Linhas 28–80)
- **Trecho Citado:** `<h2 class="h-lg">O celular acordou<br />antes de você.</h2>` (Linha 32)  
  - **Padrão:** *Faux-insight setup / Personificação forçada*.
  - **Recomendação:** Substituir por um título temático real: *"Exposição contínua: o volume de tempo conectado no Brasil"*.
- **Trecho Citado:** `"A média do brasileiro passa quase 9 horas por dia diante de uma tela — e quase 3 horas desse tempo dentro de redes sociais."` (Linha 38)  
  - **Padrão:** *Em dash excessivo*.
  - **Recomendação:** Trocar por vírgula simples ou conjunção natural: *"...diante de telas, sendo cerca de 3 horas dedicadas a redes sociais."*
- **Trecho Citado:** `"Métricas de pesquisas diferentes: use como ordem de grandeza, não como cronômetro."` (Linha 57)  
  - **Padrão:** *Colon reveal* + *Binary contrast* ("não como cronômetro").
  - **Recomendação:** *"Estimativas baseadas em relatórios setoriais para ilustrar a ordem de grandeza da exposição."*

#### Slide 05 · Evolução das Redes (Linhas 85–155)
- **Trecho Citado:** `<h2 class="h-lg">Quatro décadas<br />até o feed.</h2>` (Linha 89)  
  - **Padrão:** *Dramatic fragmentation*.
  - **Recomendação:** *"A evolução das plataformas e o crescimento do compartilhamento público"*.
- **Trecho Citado:** `"Cada plataforma removeu uma fricção: encontrar, publicar, transmitir, mostrar."` (Linha 90)  
  - **Padrão:** *Colon reveal* + *Jargão corporativo* ("fricção").
  - **Recomendação:** Explicar claramente: *"A simplificação das interfaces facilitou a publicação imediata de dados pessoais e profissionais."*

#### Slide 06 · Superexposição (Linhas 160–253)
- **Trecho Citado:** `<h2 class="h-lg">A internet não esquece.<br />Você posta de novo amanhã.</h2>` (Linha 164)  
  - **Padrão:** *Dramatic fragmentation* + *Cynical aphorism*.
  - **Recomendação:** *"Superexposição digital e acúmulo de dados históricos"*.
- **Trecho Citado:** `"Nos tornamos dependentes de estímulo e superexpomos a própria vida."` (Linhas 169–170)  
  - **Padrão:** *Importance puffery / Pregação moralizante*.
  - **Crítica:** Tom paternalista e moralista desnecessário em um seminário técnico.
  - **Recomendação:** Focar no aspecto de cibersegurança: *"O compartilhamento rotineiro em redes expõe cargos, tecnologias corporativas e rotinas operacionais."*
- **Trecho Citado:** `"A pergunta não é só o que você publica — é com quem você está realmente se conectando."` (Linha 181)  
  - **Padrão:** *Binary contrast* + *Em dash* + *Interpretive metadiscourse*.
  - **Recomendação:** Cortar o floreio: mostrar os dados técnicos do post exemplo (metadados EXIF, localização e contexto de trabalho).

#### Slide 07 · Caso Twitter (Linhas 258–324)
- **Trecho Citado:** `<h2 class="h-lg">O post que virou<br /><em class="red">coordenada.</em></h2>` (Linha 262)  
  - **Padrão:** *Dramatic fragmentation*.
  - **Recomendação:** *"Estudo de caso: correlação de local e horário a partir de publicação em tempo real"*.
- **Trecho Citado:** `"Não foi invasão. Foi <em>leitura de contexto</em> em tempo real."` (Linha 310)  
  - **Padrão:** *Binary contrast* ("Não foi X. Foi Y").
  - **Recomendação:** Afirmar Y diretamente: *"A identificação do alvo ocorreu exclusivamente por cruzamento de informações públicas postadas voluntariamente."*

#### Slide 08 · Caso Smart Sampa (Linhas 329–391)
- **Trecho Citado:** `<h2 class="h-lg">58 mil câmeras.<br />11 meses de senhas expostas.</h2>` (Linha 333)  
  - **Padrão:** *Dramatic fragmentation* ("Number + Noun. Number + Noun").
  - **Recomendação:** *"Caso Smart Sampa: exposição prolongada de credenciais de acesso"*.
- **Trecho Citado:** `"...ficaram expostas por 11 meses — não por um exploit sofisticado, mas por uma falha de cuidado."` (Linhas 340–341)  
  - **Padrão:** *Em dash* + *Binary contrast* ("não por X, mas por Y").
  - **Recomendação:** *"As credenciais de acesso ficaram expostas publicamente por falha de configuração administrativa."*
- **Trecho Citado:** `"Exposição não é o mesmo que invasão — mas é o convite."` (Linha 363)  
  - **Padrão:** *Binary contrast* + *Em dash* + *Fake-profound kicker*.
  - **Recomendação:** Eliminar a frase de efeito; citar apenas a fonte jornalística e o impacto técnico da vulnerabilidade.

#### Slide 09 · Definição (Linhas 396–447)
- **Trecho Citado:** `<h2 class="def-quote">Recon não é invadir.<br /><em>É entender.</em></h2>` (Linha 405)  
  - **Padrão:** *Binary contrast clássico* ("Não é X. É Y.").
  - **Recomendação:** *"Reconhecimento: mapeamento e inteligência prévia sobre o alvo"*.
- **Trecho Citado:** `"É a primeira fase de um ataque — não a invasão."` (Linha 407)  
  - **Padrão:** *Binary contrast* + *Em dash*.
  - **Recomendação:** *"Representa a fase inicial do ciclo ofensivo, focada em mapear serviços, tecnologias e possíveis vulnerabilidades."*
- **Trecho Citado (Notas):** `"Frase de transição: “entender sem tocar é o passivo; tocar para entender é o ativo”."` (Linha 443)  
  - **Padrão:** *Forced chiasmus / Robotic symmetry*.
  - **Recomendação:** Orientar o apresentador de forma natural: explicar que o próximo bloco abordará quando enviamos pacotes diretamente ao alvo.

---

### Bloco 02: Reconhecimento Ativo (`slides/02-recon-ativo.html`)

#### Slide 10 · Divisor 02 (Linhas 4–23)
- **Trecho Citado:** `<h2 class="statement">Quando o alvo<br /><em>começa a responder.</em></h2><p class="lede">Aqui saem pacotes de verdade. E com eles, rastros.</p>` (Linhas 9–10)  
  - **Padrão:** *Dramatic fragmentation*.
  - **Recomendação:** *"Reconhecimento ativo: interação direta com os serviços de rede do alvo"*.

#### Slide 11 · Redes Simplificado (Linhas 28–125)
- **Trecho Citado:** `<h2 class="h-md">Três coisas que você precisa saber sobre redes</h2>` (Linha 32)  
  - **Padrão:** *Throat-clearing opener* ("Três coisas que você precisa saber").
  - **Recomendação:** *"Fundamentos de rede: endereços IP, portas lógicas e pacotes"*.

#### Slide 12 · Nmap Simulação (Linhas 130–222)
- **Trecho Citado:** `<h2 class="h-md">Nmap: o mapa que o alvo entrega sem querer</h2>` (Linha 134)  
  - **Padrão:** *Colon reveal* + *Personificação forçada*.
  - **Recomendação:** *"Varredura de portas com Nmap: identificação de serviços e versões"*.
- **Trecho Citado:** `"A aplicação não registra o handshake — mas o firewall vê."` (Linha 202)  
  - **Padrão:** *Em dash* + *Binary contrast*.
  - **Recomendação:** *"O SYN scan envia apenas o primeiro pacote do handshake; a aplicação não completa a sessão, mas firewalls e IDS registram a tentativa."*
- **Trecho Citado:** `"O scan não explora nada. Ele só pergunta — e o alvo responde."` (Linha 209)  
  - **Padrão:** *Dramatic fragmentation* + *Binary contrast* + *Em dash*.
  - **Recomendação:** *"A varredura identifica portas abertas e versões ativas sem executar exploração de vulnerabilidades."*

#### Slide 13 · Wireshark Simulação (Linhas 227–319)
- **Trecho Citado:** `<h2 class="h-md">Wireshark: o que realmente passa no fio</h2>` (Linha 231)  
  - **Padrão:** *Colon reveal* + *Metáfora informal desnecessária*.
  - **Recomendação:** *"Inspeção de tráfego com Wireshark: análise detalhada de pacotes e protocolos"*.
- **Trecho Citado:** `"Sem filtro, 1.284 pacotes viram ruído. Com filtro, sete contam uma história."` (Linha 305)  
  - **Padrão:** *Robotic symmetrical antithesis* ("Sem X, ruído. Com X, história").
  - **Recomendação:** *"O uso de filtros de exibição (ex: tcp.port == 80) permite isolar fluxos específicos em meio a milhares de pacotes capturados."*

#### Slide 14 · Wireshark Handshake e Stream (Linhas 324–414)
- **Trecho Citado:** `<h2 class="h-md">Três pacotes para abrir uma conexão.<br />Um clique para ler tudo.</h2>` (Linha 328)  
  - **Padrão:** *Symmetrical dramatic fragmentation*.
  - **Recomendação:** *"Estabelecimento de sessão TCP e reconstrução de fluxo HTTP (Follow Stream)"*.
- **Trecho Citado:** `"O handshake só confirma que o serviço está ouvindo. Não diz o que ele responde."` (Linha 368)  
  - **Padrão:** *Binary contrast*.
  - **Recomendação:** *"O handshake valida a porta aberta; a transmissão de dados subsequente revela banners e cabeçalhos de autenticação."*
- **Trecho Citado:** `"Em HTTPS o conteúdo seria cifrado — os metadados, não."` (Linha 400)  
  - **Padrão:** *Em dash* + *Binary contrast*.
  - **Recomendação:** *"Conexões HTTPS criptografam a carga útil, embora dados de transporte e certificados continuem observáveis."*

#### Slide 15 · Phishing (Linhas 419–505)
- **Trecho Citado:** `<h2 class="h-md">O exploit é a confiança</h2>` (Linha 423)  
  - **Padrão:** *Fake-profound aphorism*.
  - **Recomendação:** *"Engenharia social e phishing: exploração do fator humano"*.
- **Trecho Citado:** `"Planilha com macros não é formulário de RH. É execução de código."` (Linha 480)  
  - **Padrão:** *Binary contrast* ("Não é X. É Y.").
  - **Recomendação:** *"Planilhas habilitadas para macros (.xlsm/.xlsx) podem conter código malicioso voltado ao comprometimento do endpoint."*
- **Trecho Citado (Notas):** `"Explicar que o phishing não quebra a rede: convence alguém a abrir a porta."` (Linha 500)  
  - **Padrão:** *Colon reveal* + *Binary contrast*.
  - **Recomendação:** Explicar diretamente que o vetor inicial explora a interação do usuário para obter acesso à rede interna.

---

### Bloco 03a: Reconhecimento Passivo — Introdução (`slides/03a-passivo-introducao.html`)

#### Slide 16 · Divisor 03 (Linhas 4–23)
- **Trecho Citado:** `<h2 class="statement">Coletar<br /><em>sem tocar.</em></h2>` (Linha 9)  
  - **Padrão:** *Epigrammatic dramatic fragment*.
  - **Recomendação:** *"Reconhecimento passivo: coleta de inteligência sem interação direta com o alvo"*.

#### Slide 17 · Conceito de Reconhecimento Passivo (Linhas 28–55)
- **Trecho Citado:** `<h2 class="h-md">Mapear a pegada sem consultar o alvo.</h2>` (Linha 32)  
  - **Padrão:** *Buzzword corporativo* ("pegada digital").
  - **Recomendação:** *"Mapeamento da superfície externa através de repositórios públicos e registros de terceiros"*.

#### Slide 18 · O que é OSINT (Linhas 60–110)
- **Trecho Citado:** `<h2 class="h-lg">Informação pública<br />não é informação <em class="red">inofensiva.</em></h2>` (Linha 64)  
  - **Padrão:** *Binary contrast* ("X não é Y").
  - **Recomendação:** *"Inteligência de Fontes Abertas (OSINT): potencial e riscos da informação pública"*.
- **Trecho Citado:** `"...com método, propósito e registro. Não é “achar coisas no Google”: é transformar fragmentos em inteligência acionável."` (Linhas 71–72)  
  - **Padrão:** *Banned Word* (`acionável`) + *Binary contrast* ("Não é X: é Y") + *Colon reveal*.
  - **Recomendação:** *"OSINT consiste em coletar, validar e cruzar informações publicamente acessíveis para apoiar tomadas de decisão técnicas."*
- **Trecho Citado:** `"No reconhecimento passivo, você consulta fontes externas — índices, arquivos e históricos — sem contatar diretamente..."` (Linha 75)  
  - **Padrão:** *Double Em Dash*.
  - **Recomendação:** Usar vírgulas ou parênteses: *"No reconhecimento passivo, a consulta a fontes externas (índices, bases WHOIS e históricos) evita contato com os sistemas do alvo."*
- **Trecho Citado:** `"REGRA DE OURO / 0 / pacotes enviados ao alvo durante toda a coleta."` (Linhas 86–88)  
  - **Padrão:** *Dramatic gimmick / Importance puffery*.
  - **Recomendação:** Explicar o princípio de discrição sem dramatização de "regra de ouro".

---

### Bloco 03b: Ciclo de OSINT (`slides/03b-ciclo-osint.html`)

#### Slide 19 · Visão Geral do Ciclo (Linhas 4–29)
- **Trecho Citado:** `"<h2 class="h-md">De uma pergunta à próxima.</h2><p class="lede">Dados brutos só viram inteligência quando respondem a uma necessidade.</p>"` (Linhas 8–9)  
  - **Padrão:** *Faux-profound aphorism*.
  - **Recomendação:** *"As seis etapas do ciclo de inteligência aplicado a fontes abertas"*.

#### Slides 20 a 25 · As Fases do Ciclo (Linhas 34–195)
*Nota de Auditoria: Este bloco inteiro sofre do padrão **Robotic rhythm** e **Colon reveals**, onde todos os títulos usam rigidamente a fórmula `[Infinitivo]: [Frase de efeito]`.*

- **Slide 20 (Linha 38):** `<h2 class="h-md">Planejar: faça a pergunta certa.</h2>`  
  - **Padrão:** *Colon reveal* + *Aphoristic command*.  
  - **Ajuste:** *"Fase 1 — Planejamento: definição de escopo, objetivos e requisitos de inteligência"*.
- **Slide 21 (Linha 64):** `<h2 class="h-md">Coletar: reúna evidências, não certezas.</h2>`  
  - **Padrão:** *Colon reveal* + *Binary contrast* ("evidências, não certezas").  
  - **Ajuste:** *"Fase 2 — Coleta: levantamento sistemático e preservação de fontes"*.
- **Slide 22 (Linha 94):** `<h2 class="h-md">Processar: separe sinal de ruído.</h2>`  
  - **Padrão:** *Colon reveal* + *Clichê corporativo* ("sinal de ruído").  
  - **Ajuste:** *"Fase 3 — Processamento: normalização, desduplicação e estruturação dos dados"*.
- **Slide 23 (Linha 121):** `<h2 class="h-md">Analisar: conecte sem presumir.</h2>`  
  - **Padrão:** *Colon reveal* + *Aphoristic command*.  
  - **Ajuste:** *"Fase 4 — Análise: correlação de evidências e validação de hipóteses"*.
- **Slide 24 (Linha 149):** `<h2 class="h-md">Disseminar: entregue algo acionável.</h2>`  
  - **Padrão:** *Banned Word* (`acionável`) + *Colon reveal*.  
  - **Ajuste:** *"Fase 5 — Disseminação: estruturação do relatório técnico para a equipe responsável"*.
- **Slide 25 (Linha 176):** `<h2 class="h-md">Feedback: a resposta abre outra pergunta.</h2>`  
  - **Padrão:** *Colon reveal* + *Circular aphorism*.  
  - **Ajuste:** *"Fase 6 — Avaliação e Feedback: revisão de lacunas e ajuste de direcionamento"*.

---

### Bloco 03c: Técnicas e Ferramentas OSINT (`slides/03c-tecnicas-ferramentas.html`)

#### Slide 26 · Técnicas Passivas (Linhas 4–30)
- **Trecho Citado:** `<h2 class="h-md">Quatro portas de entrada — nenhuma delas é o alvo</h2>` (Linha 8)  
  - **Padrão:** *Em dash* + *Binary contrast*.
  - **Recomendação:** *"Categorias fundamentais de fontes externas para reconhecimento passivo"*.
- **Trecho Citado:** `"Fontes diferentes respondem a perguntas diferentes — e cada uma tem limites."` (Linha 12)  
  - **Padrão:** *Em dash as rhythmic crutch*.
  - **Recomendação:** *"Cada grupo de fontes oferece ângulos específicos sobre a infraestrutura e a organização."*

#### Slides 27 a 30 · Detalhamento de Técnicas (Linhas 35–141)
*Nota de Auditoria: Repetição mecânica de **Colon reveals** em quatro slides consecutivos.*

- **Slide 27 (Linha 39):** `<h2 class="h-md">Busca e indexação: refine a pergunta.</h2>`  
  - **Padrão:** *Colon reveal*.  
  - **Ajuste:** *"Técnicas de busca avançada: operadores de filtragem e dorks em mecanismos de busca"*.
- **Slide 28 (Linha 67):** `<h2 class="h-md">DNS e certificados: nomes deixam rastros.</h2>`  
  - **Padrão:** *Colon reveal* + *Aphorism*.  
  - **Ajuste:** *"Consulta de Certificate Transparency (CT) e resolução histórica de DNS"*.
- **Slide 29 (Linha 94):** `<h2 class="h-md">Registros e infraestrutura: conecte as fontes.</h2>`  
  - **Padrão:** *Colon reveal*.  
  - **Trecho Linha 97:** `"Cada registro acrescenta contexto — não uma prova automática de propriedade."` (*Binary contrast*).  
  - **Ajuste:** *"Mapeamento de infraestrutura: bases WHOIS, blocos de IP e Sistemas Autônomos (ASN)"*.
- **Slide 30 (Linha 123):** `<h2 class="h-md">Pessoas e vazamentos: contexto com cuidado.</h2>`  
  - **Padrão:** *Colon reveal* + *Rima/Aliteração informal*.  
  - **Trecho Linha 126:** `"Perfis públicos, vagas e repositórios oferecem contexto, não certezas."` (*Binary contrast*).  
  - **Ajuste:** *"Análise de fontes humanas e exposição em repositórios: limites éticos e legais"*.

#### Slide 31 · O Kit de Coleta (Linhas 146–199)
- **Trecho Citado:** `<h2 class="h-md">O kit de coleta — e o que cada fonte responde</h2>` (Linha 150)  
  - **Padrão:** *Em dash as rhythmic crutch*.
  - **Recomendação:** *"Mapeamento de ferramentas especializadas por escopo de investigação"*.
- **Trecho Citado (Notas):** `"Automação multiplica resultados — e multiplica erros se não houver validação."` (Linha 193)  
  - **Padrão:** *Em dash* + *Symmetrical antithesis*.
  - **Recomendação:** *"Destacar a necessidade de validar manualmente os achados automatizados para evitar falsos positivos."*

---

### Bloco 03c1: Detalhes de Ferramentas (`slides/03c1-ferramentas-detalhes.html`)

#### Slides 32 a 37 · Detalhamento Ferramenta a Ferramenta (Linhas 1–237)
*Nota de Auditoria: Este arquivo apresenta o caso mais evidente de **Robotic Rhythm** e **Defensive Boilerplate Slop** do repositório. Todos os 6 slides (Shodan/Censys, WHOIS, SecurityTrails/VirusTotal, crt.sh, Subfinder/Amass, ExifTool/FOCA) repetem a mesma estrutura tabular hiper-engessada.*

- **Padrões Identificados em Série:**
  1. **Template Clônico Rigoroso:** Cada slide possui as exatas etiquetas: `O que responde` -> `Cenário fictício` -> `Limite` -> `SIMULAÇÃO DE INTERFACE / DADOS FICTÍCIOS` -> `PISTA`.
  2. **Repetição Paranoica de Disclaimers:**
     - Linha 15: `"Cada índice tem cobertura e datas próprias; os registros não confirmam a situação atual."`
     - Linha 54: `"Dados pessoais podem estar protegidos, omitidos ou desatualizados."`
     - Linha 93: `"As fontes têm datas e cobertura diferentes; associações antigas não comprovam propriedade ou risco atuais."`
     - Linha 132: `"Um nome no certificado não prova que o serviço está ativo; a cobertura não é absoluta."`
     - Linha 171: `"Revise modos e fontes: verificações ativas podem gerar tráfego direto ao alvo."`
     - Linha 213: `"Dados podem estar ausentes ou incorretos; a obtenção dos arquivos pode contatar o alvo."`
- **Diagnóstico e Recomendação:**  
  A repetição de disclaimers defensivos em 6 slides consecutivos cria uma leitura extremamente travada e burocrática. O plano de reescrita deve transformar esses disclaimers repetitivos em explicações técnicas objetivas sobre o funcionamento de cada ferramenta, unificando advertências de escopo sem engessar os slides.

---

### Bloco 03d: Reconhecimento Físico e Ecossistema (`slides/03d-fisico-ecossistema.html`)

#### Slide 38 · Dumpster Diving (Linhas 4–59)
- **Trecho Citado:** `<h2 class="h-md">Dumpster diving: quando o descarte vira pista</h2>` (Linha 8)  
  - **Padrão:** *Colon reveal*.
  - **Recomendação:** *"Descarte documental e de mídias: riscos na segurança física"*.
- **Trecho Citado:** `"O lixo de uma organização conta a história que o site institucional não conta."` (Linhas 31–32)  
  - **Padrão:** *Aphoristic contrast*.
  - **Recomendação:** *"Documentos impressos, notas fiscais e anotações internas descartadas sem trituração adequada revelam dados organizacionais confidenciais."*
- **Trecho Citado:** `"...está escrito no escopo — não no improviso."` (Linha 42)  
  - **Padrão:** *Em dash* + *Binary contrast*.
  - **Recomendação:** *"...está formalizado nas regras de engajamento do teste de segurança."*

#### Slide 39 · Shoulder Surfing (Linhas 64–90)
- **Trecho Citado:** `<h2 class="h-md">Shoulder surfing: informação à vista.</h2>` (Linha 68)  
  - **Padrão:** *Colon reveal*.
  - **Recomendação:** *"Shoulder surfing: observação visual direta de telas e credenciais"*.

#### Slide 40 · Ecossistema INT (Linhas 95–158)
- **Trecho Citado:** `<h2 class="h-md">OSINT é uma peça. O tabuleiro é maior.</h2>` (Linha 99)  
  - **Padrão:** *Metáfora clichê de xadrez* + *Dramatic fragmentation* + *Fake-profound kicker*.
  - **Recomendação:** *"O ecossistema de inteligência: as diferentes disciplinas de coleta (INTS)"*.
- **Trecho Citado:** `"OSINT alimenta o ecossistema. Ela não substitui as outras disciplinas."` (Linha 143)  
  - **Padrão:** *Binary contrast* ("não substitui").
  - **Recomendação:** *"A inteligência de fontes abertas complementa disciplinas como SIGINT, HUMINT e GEOINT em operações coordenadas."*

---

### Bloco 04: Estudos de Caso (`slides/04-estudos-caso.html`)

#### Slide 41 · Divisor 04 (Linhas 4–24)
- **Trecho Citado:** `<h2 class="statement">Quando o reconhecimento<br /><em>vira manchete.</em></h2><p class="lede">Dois casos reais. Nenhum deles começou com um exploit zero-day.</p>` (Linhas 9–10)  
  - **Padrão:** *Dramatic fragmentation* + *Negative listing*.
  - **Recomendação:** *"Estudos de caso reais: análise do reconhecimento nos incidentes RSA e Strava"*.

#### Slide 42 · Caso RSA (Linhas 29–94)
- **Trecho Citado:** `"O vetor não foi técnico: foi humano."` (Linha 62)  
  - **Padrão:** *Binary contrast* ("não foi X: foi Y") + *Colon reveal*.
  - **Recomendação:** *"O vetor inicial de comprometimento foi um e-mail de spear-phishing direcionado a colaboradores específicos."*
- **Trecho Citado:** `"<b style="color: var(--red)">Lição:</b> o reconhecimento não precisa descobrir uma falha. Basta descobrir quem abre anexos."` (Linhas 80–81)  
  - **Padrão:** *Colon reveal* + *Faux-insight aphorism*.
  - **Recomendação:** Explicar o mecanismo de ataque: *"A coleta direcionada de e-mails corporativos permitiu o envio de mensagens contextuais que contornaram a desconfiança inicial dos usuários."*

#### Slide 43 · Caso Strava (Linhas 99–183)
- **Trecho Citado:** `<h2 class="h-lg" style="font-size: 1.9em">O mapa que desenhou<br /><em class="red">bases secretas.</em></h2>` (Linha 104)  
  - **Padrão:** *Dramatic metaphor title*.
  - **Recomendação:** *"Caso Strava (2018): exposição de instalações por agregação de dados geográficos"*.
- **Trecho Citado:** `"01 Ninguém invadiu nada. O dado era público e autorizado. Só não deveria revelar tanto."` (Linha 113)  
  - **Padrão:** *Dramatic punchy fragmentation*.
  - **Recomendação:** *"O mapa de calor foi gerado a partir de dados voluntários de usuários, demonstrando como informações agregadas podem criar inteligência sensível."*
- **Trecho Citado:** `"03 Correlação vence senha. Heatmap + satélite + geografia = localização provável."` (Linha 121)  
  - **Padrão:** *Fake-strong slogan* ("Correlação vence senha").
  - **Recomendação:** *"O cruzamento de rotas circulares isoladas com fotografias de satélite permitiu identificar perímetros de segurança."*

#### Slide 44 · Lição dos Casos (Linhas 188–222)
- **Trecho Citado:** `<h2 class="lesson-quote">O dado mais perigoso é aquele que parece <em>inofensivo.</em></h2>` (Linha 192)  
  - **Padrão:** *Fake-profound kicker / Aphorism*.
  - **Recomendação:** *"Princípio da agregação: o risco decorrente da correlação de dados públicos"*.
- **Trecho Citado:** `"Reconhecimento é <strong>correlação</strong>, não coleta. O valor não está na fonte isolada — está no que ela revela quando cruza com a próxima."` (Linhas 210–212)  
  - **Padrão:** *Stacked binary contrasts* ("é X, não Y" + "não está em X — está em Y") + *Em dash*.
  - **Recomendação:** *"O valor prático do reconhecimento reside em cruzar fragmentos independentes de informação para reconstruir a infraestrutura e os fluxos do alvo."*
- **Trecho Citado (Notas):** `"Pausa dramática: deixar a frase no telão por alguns segundos."` (Linha 217)  
  - **Padrão:** *Theatrical slop direction*.
  - **Recomendação:** Cortar a instrução teatral; orientar a recapitular o elo entre os casos e a demonstração prática.

---

### Bloco 05: Demonstração GEOSINT e OSINT (`slides/05-geosint-osint.html`)

#### Slide 45 · Divisor 05 (Linhas 4–24)
- **Trecho Citado:** `<h2 class="statement">Do dado público<br /><em>ao alvo provável.</em></h2>` (Linha 9)  
  - **Padrão:** *Symmetrical phrasing*.
  - **Recomendação:** *"Demonstrações práticas: aplicação de técnicas de GEOSINT e correlação em grafo"*.

#### Slide 46 · GEOSINT 1 (Linhas 29–150)
- **Trecho Citado:** `"Montanhas baixas, solo seco, vegetação rasteira — não é litoral."` (Linha 119)  
  - **Padrão:** *Em dash* + *Binary contrast*.
  - **Recomendação:** *"Características biogeográficas indicativas de região pré-cordilheirana árida."*
- **Trecho Citado:** `<span class="chip amber">confiança, não certeza</span>` (Linha 137)  
  - **Padrão:** *Binary contrast*.
  - **Recomendação:** `<span class="chip amber">estimativa probabilística: 78%</span>`

#### Slide 47 · GEOSINT 2 (Linhas 155–232)
- **Trecho Citado:** `<h2 class="h-md">Três hipóteses. Uma coordenada.</h2>` (Linha 159)  
  - **Padrão:** *Dramatic fragmentation* ("Três X. Um Y").
  - **Recomendação:** *"Processo de eliminação e validação de coordenadas geográficas"*.
- **Trecho Citado:** `<h3 class="h-sm" style="margin-bottom: 8px">Eliminar, não adivinhar.</h3>` (Linha 198)  
  - **Padrão:** *Binary contrast*.
  - **Recomendação:** *"Metodologia de descarte sucessivo baseada em evidências"*.
- **Trecho Citado:** `"Cada pista precisa derrubar uma hipótese. O que sobra não é certeza: é o próximo teste."` (Linha 200)  
  - **Padrão:** *Binary contrast* + *Colon reveal*.
  - **Recomendação:** *"Cada indicador analisado (azimut solar, relevo e malha viária) reduz o leque de áreas compatíveis."*

#### Slide 48 · OSINT Demo — Grafo (Linhas 237–311)
- **Trecho Citado:** `<h2 class="h-md">Vinte minutos de coleta. Um grafo.</h2>` (Linha 241)  
  - **Padrão:** *Dramatic fragmentation*.
  - **Recomendação:** *"Construção de grafo relacional: encadeamento de fontes abertas"*.
- **Trecho Citado:** `"Não testamos a senha vazada. Não acessamos a VPN. Não enviamos nada ao alvo. Sem autorização, o grafo para aqui."` (Linha 293)  
  - **Padrão:** *Dramatic fragmentation* + *Repetitive negative listing*.
  - **Recomendação:** *"Limites éticos: a análise encerra-se no mapeamento relacional; testes de autenticação e conexões ativas dependem de autorização formal prévia."*
- **Trecho Citado:** `"O próximo passo é um relatório com evidências, não um login."` (Linha 297)  
  - **Padrão:** *Binary contrast*.
  - **Recomendação:** *"O resultado da investigação compõe o relatório de inteligência para encaminhamento às equipes de defesa."*

---

### Bloco 06: OpSec e Fechamento (`slides/06-opsec-fechamento.html`)

#### Slide 49 · Divisor 06 (Linhas 4–23)
- **Trecho Citado:** `"<h2 class="statement">O rastro que você<br /><em>deixa sem perceber.</em></h2><p class="lede">Se o reconhecimento coleta, a OpSec reduz o que existe para coletar.</p>"` (Linhas 9–10)  
  - **Padrão:** *Chiasmus / Robotic symmetry*.
  - **Recomendação:** *"Segurança Operacional (OpSec): minimização de rastros e gestão de superfície de exposição"*.

#### Slide 50 · OpSec Conceito (Linhas 28–80)
- **Trecho Citado:** `<h2 class="h-lg" style="font-size: 1.8em">OpSec é sobre<br /><em class="red">não virar dado.</em></h2>` (Linha 49)  
  - **Padrão:** *Aphoristic slogan*.
  - **Recomendação:** *"Princípios de OpSec: proteção de rotinas, dados e comunicações"*.
- **Trecho Citado:** `"Não é paranoia: é priorização por impacto."` (Linha 61)  
  - **Padrão:** *Binary contrast* ("Não é X: é Y") + *Colon reveal*.
  - **Recomendação:** *"A OpSec avalia a probabilidade e o impacto de cada exposição para estabelecer salvaguardas proporcionais."*

#### Slide 51 · OpSec no Dia a Dia (Linhas 85–140)
- **Trecho Citado:** `<p class="opsec-quote">O elo mais barato de atacar continua sendo <em>o hábito.</em></p>` (Linha 121)  
  - **Padrão:** *Aphoristic kicker*.
  - **Recomendação:** Integrar com o texto didático sobre hábitos de higiene digital.
- **Trecho Citado:** `"O difícil não é saber — é manter. OpSec é higiene, não evento."` (Linhas 123–124)  
  - **Padrão:** *Em dash* + *Double binary contrast* ("não é X — é Y" + "é X, não Y").
  - **Recomendação:** *"Medidas de segurança operacional requerem aplicação contínua e revisões periódicas de configuração."*

#### Slide 52 · Takeaways / Fechamento (Linhas 145–183)
- **Trecho Citado:** `<h3>Recon é processo, não ferramenta.</h3>` (Linha 156)  
  - **Padrão:** *Binary contrast*.
  - **Recomendação:** *"O valor do reconhecimento está no método analítico e na formulação de hipóteses técnicas."*
- **Trecho Citado:** `"“Recon é a única fase do ataque que a defesa também pode praticar — e deveria.”"` (Linha 172)  
  - **Padrão:** *Fake-profound kicker / Mic-drop ending*.
  - **Recomendação:** *"A autoavaliação contínua da superfície externa permite que equipes de segurança identifiquem exposições antes de atores maliciosos."*

---

### Bloco 07: Referências e Perguntas (`slides/07-referencias-perguntas.html`)

#### Slide 53 · Referências (Linhas 4–47)
- Bloco limpo, com citações bibliográficas reais (MITRE ATT&CK, OWASP, Michael Bazzell, G1, The Guardian). Travessões aqui funcionam como separadores de títulos bibliográficos convencionais.

#### Slide 54 · Q&A (Linhas 52–78)
- **Trecho Citado:** `<p class="qa-sub">O microfone é de vocês. A parte mais interessante do recon é o que a gente não pensou em perguntar.</p>` (Linha 57)  
  - **Padrão:** *Faux-insight setup / Aphorism*.
  - **Recomendação:** Simplificar para uma recepção acadêmica aberta e acolhedora: *"Estamos à disposição para dúvidas, comentários e discussão técnica."*

---

## 4. Tabela de Severidade e Frequência por Slide

| Bloco | Arquivo | Slides | Gravidade | Padrões Predominantes |
| :---: | :--- | :---: | :---: | :--- |
| **00** | `00-abertura.html` | 01–02 | Baixa/Média | Dramatic fragmentation, Colon reveal, Em dashes em listas |
| **01** | `01-conceito-contexto.html` | 03–09 | **Crítica** | Binary contrasts ("Recon não é invadir. É entender."), Pregação moralizante, Aforismos vazios, Travessões |
| **02** | `02-recon-ativo.html` | 10–15 | **Alta** | Antíteses simétricas ("Sem filtro... Com filtro..."), Binary contrasts, Colon reveals, Fake-strong verbs |
| **03a**| `03a-passivo-introducao.html`| 16–18 | **Alta** | Palavra banida (*acionável*), Binary contrasts ("Não é achar no Google: é..."), Double em dash |
| **03b**| `03b-ciclo-osint.html` | 19–25 | **Crítica** | Robotic rhythm (6x Verbo: Aforismo), Colon reveals em todos os slides, Palavra banida (*acionável*) |
| **03c**| `03c-tecnicas-ferramentas.html` | 26–31 | **Alta** | Colon reveals (4 slides seguidos), Binary contrasts ("contexto, não certezas"), Travessões |
| **03c1**| `03c1-ferramentas-detalhes.html`| 32–37 | **Crítica** | Robotic rhythm extremo (6x template clônico), Disclaimers burocráticos defensivos repetidos |
| **03d**| `03d-fisico-ecossistema.html` | 38–40 | **Média/Alta** | Metáfora de xadrez ("tabuleiro é maior"), Colon reveals, Aforismos de encerramento |
| **04** | `04-estudos-caso.html` | 41–44 | **Crítica** | Tom dramatizado de documentário, Stacked binary contrasts, Fake-profound kickers, "Pausa dramática" nas notas |
| **05** | `05-geosint-osint.html` | 45–48 | **Alta** | Dramatic fragmentation ("Três X. Um Y", "Vinte X. Um Y"), Binary contrasts negativos redundantes |
| **06** | `06-opsec-fechamento.html` | 49–52 | **Crítica** | Acúmulo de contrastes binários triplos ("não é X — é Y", "higiene, não evento"), Mic-drop ending |
| **07** | `07-referencias-perguntas.html` | 53–54 | Baixa | Faux-insight kicker em Q&A |

---

## 5. Diretrizes e Recomendações Estruturais para o Plano de Implementação

1. **Desmontar as Antíteses Binárias:** Em vez de definir conceitos por negação contrastante (*"Não é X. É Y."*), definir diretamente por seus atributos positivos, funcionamento e causa-efeito.
2. **Romper o Ritmo Robótico dos Ciclos e Ferramentas:**
   - No Ciclo de OSINT (slides 20–25), substituir o padrão mecânico `[Infinitivo]: [Frase de efeito]` por títulos substantivados descritivos da atividade técnica.
   - No bloco de Ferramentas (slides 32–37), quebrar o template engessado de 5 caixas idênticas e trazer exemplos de dados reais da ferramenta em vez de repetir 6 vezes disclaimers idênticos de "Cenário fictício".
3. **Substituir Aforismos por Informação Técnica:** Eliminar frases de efeito como *"O exploit é a confiança"* ou *"O tabuleiro é maior"* e explicar o vetor técnico subjacente (ex: uso de engenharia social para contornar defesas perimetrais; complementaridade de fontes de sinais, imagens e tráfego).
4. **Higienizar Travessões Desnecessários:** Reduzir os 47 travessões para no máximo 3 ou 4 ocorrências genuinamente úteis em toda a apresentação, priorizando vírgulas, dois pontos informativos ou pontos finais.
5. **Humanizar as Notas do Orador:** Remover direções de palco artificiais (*"Pausa dramática"*, *"Provocar a turma"*) e fornecer tópicos de fala objetivos, fluidos e técnicos para cada apresentador.

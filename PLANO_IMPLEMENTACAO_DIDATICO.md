# Plano Mestre de Implementação Didática e Reformulação Textual
## Seminário Red Team 1 — Reconhecimento e OSINT (`IntroReconSeminário`)

**Data de Emissão:** 31 de Outubro de 2026  
**Responsável Técnico:** Worker 2 (Especialista em Comunicação Técnica e Elaboração do Plano de Implementação Didático)  
**Documento Relacionado:** `AUDITORIA_AI_SLOP.md` (Auditoria Oficial de Padrões Linguísticos)  
**Referencial Normativo:** Skill `/no-ai-slop` (`/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md`), Teoria da Carga Cognitiva (Sweller) e Princípios de Multimídia Didática (Mayer).  
**Diretriz de Integridade:** Não intervenção em arquivos-fonte (`slides/` mantido 100% inalterado); 100% de preservação factual dos dados técnicos, ferramentas, parâmetros, comandos e estudos de caso.

---

# 1. Sumário Executivo e Diretrizes Pedagógicas Globais

## 1.1. Contexto e Justificativa da Reformulação
A apresentação acadêmica *Red Team 1 — Recon & OSINT* possui excelência visual e rigor metodológico: conta com simulações completas de terminal (Nmap 7.95), interface gráfica de dissecação de pacotes (Wireshark com reconstrução TCP Stream e Basic Auth), fluxo investigativo em fontes abertas, diagramas de rede em SVG e três estudos de caso de grande impacto histórico (Smart Sampa 2026, RSA SecurID 2011 e Strava Heatmap 2018).

No entanto, o diagnóstico emitido pelo relatório `AUDITORIA_AI_SLOP.md` comprovou que o texto original foi gerado e polido com forte dependência de modelos de linguagem sintéticos, resultando em:
1. **Proliferação de fórmulas antitéticas mecânicas (*Binary contrasts*):** Ocorrência de mais de 28 instâncias de "Não é X, é Y", gerando uma cadência pedante e negativa que adia a entrega de explicações funcionais diretas.
2. **Ritmo robótico e gabaritos clônicos (*Robotic rhythm*):** Sequências de 6 slides no Ciclo de OSINT e 6 slides em Detalhes de Ferramentas com sintaxe, formatação e disclaimers idênticos.
3. **Hiper-hedging burocrático (*Defensive boilerplate slop*):** Repetição sistemática de ressalvas legais e protocolares ("Cenário fictício", "DADOS FICTÍCIOS", "registros não confirmam a situação atual") em quase todos os componentes visuais, engessando a narrativa.
4. **Artifícios dramáticos e direção cênica artificial:** Títulos fragmentados sem verbo ("Três hipóteses. Uma coordenada."), aforismos pretensiosos ("O exploit é a confiança") e rubricas teatrais nas notas do orador ("Pausa dramática").
5. **Conflitos de dados e anacronismos:** Ocorrência de métricas conflitantes no slide 04 (9h de tela/dia versus 116h/semana) e anacronismo no slide 42 (anexo nomeado `2021_Recruitment_Plan.xlsx` em um caso ocorrido em março de 2011).

Este documento estabelece o **Plano Mestre de Implementação Didática** para a futura etapa de aplicação (M3), fornecendo propostas concretas de reescrita, modelos mentais e notas faladas para cada um dos 54 slides da apresentação, garantindo máxima fluidez didática para a banca examinadora e 100% de preservação técnica.

---

## 1.2. Princípios de "Dessengessamento" e Redação Humana
Baseando-se nas diretrizes da skill `/no-ai-slop`, a reestruturação textual seguirá seis princípios fundamentais:

1. **Transformação de Antíteses Negativas em Declarações Afirmativas e Causais:**
   - *Padrão a eliminar:* "Recon não é invadir. É entender." / "Não foi invasão. Foi leitura de contexto." / "Reconhecimento é correlação, não coleta."
   - *Diretriz dessengessada:* Afirmar diretamente o mecanismo de causa e efeito. Dizer com exatidão o que o analista faz e qual o resultado técnico: "O reconhecimento mapeia a superfície de ataque externa sem explorar vulnerabilidades." / "A localização física foi determinada pelo cruzamento de postagens públicas em tempo real."
2. **Eliminação de Jargões Vazios e Vocábulos Banidos:**
   - Erradicação completa de termos como `acionável` (banned word), `ecossistema`, `fricção`, `robusto`, `alavancar`, `mergulhar` e expressões de enchimento como `vale notar`, `é importante destacar` e `no final do dia`.
3. **Erradicação de Revelações por Dois Pontos (*Colon reveals*) e Fragmentação Dramática:**
   - Títulos compostos por `[Substantivo]: [Frase de efeito]` e fragmentações telegráficas como `[Número]. [Número]` serão convertidos em orações completas com sujeito, verbo e predicado claro, funcionando como manchetes informativas.
4. **Substituição de Disclaimers Repetitivos por Enquadramento Metodológico Inicial:**
   - Os avisos de conformidade e uso educacional serão concentrados na introdução dos blocos, liberando os slides de ferramentas do excesso de etiquetas burocráticas repetitivas.
5. **Foco no Verbo Ativo ("Make verbs do the work"):**
   - Substituição de nominalizações pesadas ("proceder à execução da varredura", "realização da verificação autorizada") por verbos diretos ("o analista varre as 65.535 portas", "a equipe valida o certificado").
6. **Eliminação da Muleta de Travessões (Em Dashes):**
   - Redução dos 38 travessões decorativos para pontuação gramatical limpa (vírgulas, pontos e conjunções).

---

## 1.3. Resolução da Sobrecarga Cognitiva do Bloco de Daniel (Slides 16 a 40)
O Bloco 03 representa 25 slides consecutivos apresentados pelo mesmo orador (Daniel), perfazendo quase metade de todo o seminário. Na estrutura original, o bloco gerava severa fadiga cognitiva devido à repetição de templates idênticos nos sub-blocos 03b (Ciclo OSINT) e 03c1 (Ferramentas).

**Estratégia de Alívio e Dinamização:**
1. **Ritmo de Apresentação Diferenciado (Aceleração Cinematográfica no Ciclo):**
   - Os slides 19 a 25 serão tratados não como aulas teóricas isoladas de 1 minuto, mas como um percurso fluido de 20 a 25 segundos por tela. Daniel conduzirá a plateia mostrando o dado sendo refinado passo a passo, variando a entonação em cada fase (da dúvida inicial ao relatório final).
2. **Quebra dos Gabaritos Clônicos em Detalhes de Ferramentas (Slides 32 a 37):**
   - Cada slide de ferramenta terá um foco pedagógico único:
     - Slide 32 (Shodan/Censys): Busca em portas expostas na nuvem.
     - Slide 33 (WHOIS): A infraestrutura administrativa e limites de privacidade (GDPR/LGPD).
     - Slide 34 (SecurityTrails/VirusTotal): A linha do tempo (DNS histórico).
     - Slide 35 (crt.sh): O cartório imutável dos certificados SSL.
     - Slide 36 (Subfinder/Amass): A automação de inventário passivo.
     - Slide 37 (ExifTool/FOCA): Os metadados embutidos em arquivos baixados.
3. **Quebra de Ritmo com o Bloco Físico (Slides 38 a 40):**
   - A transição do terminal digital para o lixo corporativo (Dumpster Diving) e a observação de telas no aeroporto (Shoulder Surfing) servirá como alívio cômico e sensorial para revitalizar a atenção da plateia antes dos estudos de caso.

---

## 1.4. O Fio Narrativo Unificado: O Caso Marina Sousa & Acme Pagamentos
Para conferir coesão dramática ao seminário e amarrar os 5 apresentadores em uma única equipe integrada, o caso fictício da analista Marina Sousa e da empresa Acme Pagamentos será expandido como um fio condutor que costura todo o deck:

1. **Slide 06 (Geovana - Contexto):** Marina Sousa (@marina.souza) posta uma selfie comemorando o fim de plantão no novo datacenter da *Acme Pagamentos*, expondo o crachá no pescoço e a localização geográfica da instalação.
2. **Slide 15 (Emilio - Recon Ativo):** Um e-mail de spear-phishing forjado em nome do RH da Acme Pagamentos (`rh@beneficios-acme.com`) é enviado para colaboradores da empresa explorando o contexto do plano de saúde corporativo.
3. **Slides 21, 28 e 35 (Daniel - Recon Passivo):** A consulta a logs de Certificate Transparency revela a criação recente do subdomínio `datacenter-sp.acme.com`, confirmando tecnicamente o que Marina havia antecipado em seu post social.
4. **Slide 48 (João Pedro Almeida - Demonstração Prática):** O grafo de correlação OSINT conecta todos os nós do seminário: `@marina.souza` $\rightarrow$ `marina@acme.com` $\rightarrow$ 2 vazamentos de senhas corporativas $\rightarrow$ `acme.com` $\rightarrow$ VPN de borda exposta $\rightarrow$ cargo de aprovação no financeiro.

Essa amarração narrativa transforma slides isolados em uma investigação contínua e palpável, demonstrando na prática como fragmentos públicos aparentemente inofensivos constroem uma superfície de ataque crítica.

---

## 1.5. Resolução de Conflitos Fatuais e Anacronismos
O plano corrige formalmente duas falhas históricas e estatísticas presentes no deck:

1. **Harmonização do Slide 04 (Tempo de Tela):**
   - *Problema original:* O slide exibia simultaneamente 9h diárias de tela e 116h semanais conectado ($116 \div 7 \approx 16,5\text{ h/dia}$), gerando inconsistência lógica aparente e obrigando a notas defensivas de rodapé.
   - *Solução do plano:* Cortar a métrica de 116h semanais. Consolidar o dado em uma métrica unificada e consistente: **9 horas diárias diante de telas**, sendo **3 horas dedicadas a redes sociais** (aproximadamente um terço de todo o período em vigília).
2. **Correção do Anacronismo do Slide 42 (Caso RSA SecurID):**
   - *Problema original:* No slide que descreve o ataque ocorrido em março de 2011 contra a RSA SecurID, o anexo simulado foi grafado como `2021_Recruitment_Plan.xlsx`, introduzindo um erro anacrônico de uma década.
   - *Solução do plano:* Alinhar o anexo para `2011_Recruitment_Plan.xls` (formato original compatível com o exploit de Adobe Flash encapsulado em planilha Excel amplamente documentado no ataque histórico de 2011).

---

## 1.6. Diferenciação Funcional da Tríade de Certificate Transparency
A redundância crítica diagnosticada em torno do conceito de *Certificate Transparency (CT)* é resolvida com papéis pedagógicos estritos e complementares em cada uma das suas três aparições:

| Slide | Bloco / Sub-bloco | Função Didática Exclusiva | Modelo Mental / Metáfora | Foco do Orador (Daniel) |
| :---: | :--- | :--- | :--- | :--- |
| **Slide 21** | 03b: Ciclo OSINT (Fase 2: Coleta) | **Coleta de Evidência Bruta** | "A impressão digital digitalizada" | Demonstrar como um log bruto de CT registra a emissão de certificados sem qualificar se o host está ativo ou seguro. |
| **Slide 28** | 03c: Técnicas (DNS e Certificados) | **Mecânica Sistêmica Global** | "O Diário Oficial do Cartório Web" | Explicar a arquitetura RFC 6962: para navegadores confiarem em conexões HTTPS, as Autoridades Certificadoras são obrigadas a registrar publicamente todas as emissões em servidores imutáveis append-only. |
| **Slide 35** | 03c1: Ferramentas (`crt.sh`) | **Operação Prática com Wildcards** | "O Catálogo de Busca Instantânea" | Demonstrar a sintaxe de consulta no motor web `crt.sh` utilizando o operador curinga `%.example.com` para enumerar subdomínios e hosts de homologação esquecidos. |

---

## 1.7. Catálogo de Modelos Mentais e Metáforas Funcionais

| Conceito Técnico | Metáfora Funcional | Explicação Intuitiva para o Público |
| :--- | :--- | :--- |
| **Reconhecimento Passivo vs. Ativo** | *A Vitrine da Loja vs. A Maçaneta da Porta* | Passivo é caminhar pela calçada pública anotando os preços, modelos e horários expostos na vitrine (sem tocar na loja). Ativo é atravessar a porta ou forçar a maçaneta dos fundos para ver se a trava cede (gerando ruído e alarmes). |
| **Nmap SYN Scan (`-sS`)** | *Bater e Correr na Campainha* | O atacante aperta a campainha (SYN). O morador se levanta e destranca a fechadura (SYN/ACK). Mas antes que a porta se abra, o atacante foge (RST). O morador não chega a receber uma visita, mas o atacante já confirmou que tem gente na casa. |
| **Wireshark Follow Stream & Base64** | *Envelope de Papel Celofane Transparente* | Basic Authentication não é cofre de segurança; é apenas empacotamento para viagem. A string codificada em Base64 é como uma carta dentro de um envelope transparente: qualquer intermediário no caminho lê o remetente, a senha e a mensagem sem esforço. |
| **Certificate Transparency (CT)** | *O Diário Oficial dos Cartórios* | Nenhuma empresa pode emitir um certificado HTTPS válido em segredo. Pela regra global dos navegadores, todo certificado novo precisa ser publicado em um livro de atas público. Se a equipe de TI subir um subdomínio de teste (`homolog-api.banco.com`), o Diário Oficial publica na mesma hora. |
| **Dados Agregados (Caso Strava)** | *A Trilha de Formigas no Jardim* | Uma formiga correndo na grama é invisível. Dez mil formigas marchando repetidamente pelo mesmo percurso abrem uma vala na terra visível até por satélite. Soldados correndo individualmente em volta de uma base secreta desenharam o perímetro militar com precisão métrica. |
| **Google Dorking** | *A Lente Polarizada do Pescador* | O Google já pescou e indexou a internet inteira. Usar dorks (`site:`, `filetype:xls`, `inurl:admin`) é como colocar óculos polarizados: remove o reflexo da água barrenta e mostra os peixes grandes — planilhas de senhas e arquivos de configuração — que estavam no fundo. |
| **Segurança Operacional (OpSec)** | *Higiene Básica Cotidiana* | OpSec não é construir um bunker subterrâneo ou desconectar os cabos de rede; é lavar as mãos antes de comer. Trata-se de manter hábitos consistentes (senhas exclusivas, 2FA, limpeza de metadados) para que a rotina não entregue chaves de bandeja. |

---

# 2. Plano Detalhado Slide a Slide (Slides 01 a 54)

```
================================================================================
ARQUIVO 01 / 12: slides/00-abertura.html
Bloco Temático: Capa e Agenda Global
Apresentadores: Todos
Slides: 01 e 02
================================================================================
```

### Slide 01 · Capa da Apresentação
- **Cabeçalho:** Slide 01 | Arquivo: `slides/00-abertura.html` | Apresentadores: Todos | Título Original: `Recon & OSINT`
- **Objetivo Didático Central:** Abrir o seminário estabelecendo com clareza o escopo de segurança ofensiva: o reconhecimento é a fase preliminar em que o atacante analisa a superfície pública antes de qualquer toque direto.
- **Diagnóstico de AI Slop & Engessamento:** Subtítulo original melodramático e fragmentado (*"Tudo o que o alvo revela antes de ser atacado."*); rubrica teatral nas notas (*"Provocar: antes de qualquer ataque, alguém passou semanas só olhando"*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Reconhecimento e OSINT` | Subtítulo: `Mapeamento de superfície de ataque e inteligência em fontes abertas`.
  - *Proposta de Corpo de Texto e Tópicos:* Manter a interface de radar sweep e a caixa de redação tarjada com os termos-chave em destaque: `Superfície de ataque`, `Inteligência em fontes abertas`, `Segurança ofensiva e defensiva`. Demonstrações práticas e estudos ao longo do deck integrando varreduras com Nmap e captura com Wireshark.
  - *Modelo Mental / Metáfora Funcional:* A planta baixa do edifício: antes de qualquer obra ou arrombamento, o arquiteto ou invasor estuda as plantas disponíveis na prefeitura.
  - *Roteiro e Tom do Apresentador:* Fala natural, segura e acadêmica: "Bom dia a todos, professor e colegas. Hoje apresentaremos os fundamentos, as técnicas práticas e os casos reais de reconhecimento em segurança da informação. Em um teste de intrusão profissional, a maior parte do esforço concentra-se na análise do que a organização já expôs na internet antes da execução de comandos diretos de exploração."
- **Fatos Técnicos Preservados:**
  - [x] Título Red Team 1 — Recon & OSINT
  - [x] Mês e ano: Outubro de 2026
  - [x] Nomes dos cinco integrantes da equipe (Geovana, Emilio, Daniel, João Pedro Gonçalves, João Pedro Almeida)
  - [x] Termos tarjados na abertura visual

---

### Slide 02 · Agenda da Apresentação
- **Cabeçalho:** Slide 02 | Arquivo: `slides/00-abertura.html` | Apresentadores: Todos | Título Original: `Seis blocos. Uma pergunta: o que o alvo já contou?`
- **Objetivo Didático Central:** Apresentar a estrutura da apresentação em seis blocos lógicos, guiando a audiência da exposição inicial de dados até os controles defensivos de higiene operacional.
- **Diagnóstico de AI Slop & Engessamento:** Título com fórmula de IA `[Número]. [Número]: [Pergunta]`; travessões decorativos como muleta em quase todos os itens da lista; metáfora clichê ("duas faces do reconhecimento").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Roteiro do Seminário` | Subtítulo: `Como o reconhecimento estrutura a análise de segurança ofensiva`.
  - *Proposta de Corpo de Texto e Tópicos:*
    1. `Conceito e contexto:` da pegada digital individual ao mapeamento formal de superfície.
    2. `Reconhecimento ativo:` interação direta com portas e serviços via Nmap e Wireshark.
    3. `Reconhecimento passivo e OSINT:` coleta em bases públicas sem envio de pacotes ao alvo.
    4. `Estudos de caso reais:` incidentes históricos da RSA SecurID e do Strava Heatmap.
    5. `Demonstrações práticas:` geolocalização por sombras e construção de grafo relacional.
    6. `Segurança operacional (OpSec):` métodos práticos para redução da exposição digital.
  - *Modelo Mental / Metáfora Funcional:* O mapa de viagem da investigação: partir da observação de longe, aproximar-se da rede, examinar casos concretos e voltar com as medidas de proteção.
  - *Roteiro e Tom do Apresentador:* "Para guiar nosso seminário de 45 minutos, dividimos a apresentação em seis blocos bem delimitados. Vamos partir da superexposição em redes sociais, entrar na parte de redes com varredura ativa de portas e tráfego, passar pelo ciclo completo de OSINT e ferramentas passivas, analisar dois casos históricos de grande impacto, mostrar duas demonstrações práticas e encerrar com práticas defensivas de OpSec."
- **Fatos Técnicos Preservados:**
  - [x] Os seis blocos temáticos sequenciais
  - [x] Atribuição dos blocos aos 5 apresentadores
  - [x] Menção explícita a Nmap, Wireshark, OSINT, RSA, Strava e OpSec

---

```
===============================================================================
ARQUIVO 02 / 12: slides/01-conceito-contexto.html
Bloco Temático: Bloco 01 — Conceito & Contexto
Apresentadora: Geovana
Slides: 03 a 09
===============================================================================
```

### Slide 03 · Divisor do Bloco 01
- **Cabeçalho:** Slide 03 | Arquivo: `slides/01-conceito-contexto.html` | Apresentadora: Geovana | Título Original: `Todo ataque começa com uma pergunta.`
- **Objetivo Didático Central:** Demarcar a transição para o Bloco 01, contextualizando que a segurança da informação começa pela análise metodológica de dados antes de qualquer interação técnica ofensiva.
- **Diagnóstico de AI Slop & Engessamento:** Frase de efeito de abertura (*Fake-profound kicker*); contraste antitético nas notas do orador ("sair da ideia de hacker invadindo para a de analista investigando").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fundamentos e Contexto` | Subtítulo: `A investigação prévia como base da segurança ofensiva`.
  - *Proposta de Corpo de Texto e Tópicos:* `Bloco 01 · Geovana`. Declaração central: "O reconhecimento identifica onde estão as vulnerabilidades antes do primeiro contato com a infraestrutura."
  - *Modelo Mental / Metáfora Funcional:* O trabalho pericial: o perito não chuta portas; ele examina os registros, os vestígios e a vizinhança.
  - *Roteiro e Tom do Apresentador:* "Assumo a palavra para abrir o nosso primeiro bloco. Quando pensamos em testes de segurança, a imagem comum é a de alguém tentando quebrar senhas em um terminal. Mas na prática de segurança ofensiva, a primeira pergunta que o analista faz é: o que essa organização já expôs na internet sem perceber?"
- **Fatos Técnicos Preservados:**
  - [x] Numeração do Bloco: 01
  - [x] Apresentadora responsável: Geovana
  - [x] Conceito fundamental de reconhecimento preliminar

---

### Slide 04 · Era das Mídias Sociais
- **Cabeçalho:** Slide 04 | Arquivo: `slides/01-conceito-contexto.html` | Apresentadora: Geovana | Título Original: `O celular acordou antes de você.`
- **Objetivo Didático Central:** Demonstrar o volume massivo de tempo que a população brasileira passa conectada gerando dados telemétricos contínuos.
- **Diagnóstico de AI Slop & Engessamento:** Título publicitário ("O celular acordou antes de você"); métricas conflitantes lado a lado (9h/dia versus 116h/semana); caveat burocrático na nota de rodapé ("Métricas de pesquisas diferentes: use como ordem de grandeza, não como cronômetro").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Volume de Exposição Digital` | Subtítulo: `A geração contínua de dados em redes públicas no Brasil`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Destaque principal: **9 horas e 13 minutos** diárias de tela em média no Brasil.
    - Destaque secundário: **3 horas e 37 minutos** dedicadas a redes sociais.
    - Análise técnica: Aproximadamente um terço de todo o período diário em vigília gerando telemetria, check-ins, interações e metadados públicos.
    - *(Corte definitivo da métrica conflitante de 116h/semana e eliminação da nota defensiva de rodapé).*
  - *Modelo Mental / Metáfora Funcional:* O rádio transmissor ligado no bolso: passamos o dia transmitindo coordenadas, contatos e rotinas sem nos darmos conta.
  - *Roteiro e Tom do Apresentador:* "Para entender por que o reconhecimento é tão eficaz hoje, precisamos olhar para os dados de conectividade. O brasileiro passa em média mais de 9 horas diárias diante de telas, sendo mais de 3 horas e meia em redes sociais. Em termos práticos, um terço do dia de um colaborador é passado gerando registros públicos de hábitos, conexões e rotinas corporativas."
- **Fatos Técnicos Preservados:**
  - [x] Métrica: 9 horas diárias de tempo de tela
  - [x] Métrica: ~3 horas diárias em redes sociais
  - [x] Contextualização da telemetria digital no Brasil

---

### Slide 05 · Evolução das Redes
- **Cabeçalho:** Slide 05 | Arquivo: `slides/01-conceito-contexto.html` | Apresentadora: Geovana | Título Original: `Quatro décadas até o feed.`
- **Objetivo Didático Central:** Apresentar a linha do tempo das plataformas sob a perspectiva da expansão contínua da superfície de ataque e da redução das barreiras de publicação.
- **Diagnóstico de AI Slop & Engessamento:** Título telegráfico ("Quatro décadas até o feed"); emprego de palavra banida/jargão corporativo (`fricção` na linha 90); anacronismo conceitual histórico (Usenet datada em 1974 em vez da fundação operacional de 1979/1980).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Evolução da Superfície de Exposição` | Subtítulo: `Como a facilidade de compartilhamento ampliou o rastro público`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - `1979 (Usenet):` Primeiros grupos de discussão e vazamentos de e-mails em texto puro.
    - `2003 (LinkedIn):` Organogramas corporativos abertos: cargos, fornecedores e pilhas de tecnologia.
    - `2004 (Facebook/Orkut):` Mapeamento de redes de amizade e respostas para perguntas de segurança.
    - `2006 (Twitter/X):` Publicações curtas com telemetria em tempo real e relatos operacionais imediatos.
    - `2010 (Instagram):` Fotos de alta resolução com crachás, salas de servidores e metadados EXIF.
  - *Modelo Mental / Metáfora Funcional:* Da carta fechada ao megafone: passamos de mensagens técnicas restritas a murais públicos onde qualquer um pode ler o contexto operacional de uma empresa.
  - *Roteiro e Tom do Apresentador:* "Essa superexposição não surgiu do nada; ela foi construída nas últimas quatro décadas. Em 1979, na Usenet, tínhamos mensagens de texto restritas entre administradores. A partir dos anos 2000, o LinkedIn abriu os organogramas das empresas, o Twitter passou a registrar eventos em tempo real e o Instagram popularizou fotos de crachás e escritórios. Cada nova rede facilitou a publicação e aumentou o rastro deixado."
- **Fatos Técnicos Preservados:**
  - [x] Marcos temporais da evolução das redes
  - [x] Plataformas citadas: Usenet, LinkedIn, Facebook, Twitter, Instagram
  - [x] Relação causal entre evolução da mídia e segurança ofensiva

---

### Slide 06 · Superexposição e Rastro
- **Cabeçalho:** Slide 06 | Arquivo: `slides/01-conceito-contexto.html` | Apresentadora: Geovana | Título Original: `A internet não esquece. Você posta de novo amanhã.`
- **Objetivo Didático Central:** Introduzir a personagem Marina Sousa e o caso da Acme Pagamentos, demonstrando como hábitos rotineiros de publicação expõem infraestruturas críticas.
- **Diagnóstico de AI Slop & Engessamento:** Título com aforismo cínico; tom moralista e pregação comportamental ("Nos tornamos dependentes de estímulo e superexpomos a própria vida"); antítese vazia na linha 181.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Vazamento de Contexto Operacional` | Subtítulo: `Como publicações de rotina entregam vetores corporativos`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Exame do post de Marina Sousa (@marina.souza): foto com crachá da Acme Pagamentos no novo datacenter de São Paulo.
    - Informações extraídas sem invasão:
      1. Entidade e cargo: Analista financeira na Acme Pagamentos.
      2. Localização física: Endereço do novo datacenter.
      3. Dependência tecnológica: Visibilidade de monitores e modelo de credencial de acesso.
    - *(Eliminação do tom de sermão moral; foco estrito na análise analítica da imagem).*
  - *Modelo Mental / Metáfora Funcional:* O crachá na mesa do restaurante: o funcionário sai para almoçar com o crachá à mostra e qualquer pessoa descobre a empresa, o setor e o nível de acesso.
  - *Roteiro e Tom do Apresentador:* "Vejam este caso ilustrativo que acompanhará nosso seminário. Aqui temos uma postagem no Instagram da analista Marina Sousa comemorando a entrega do novo datacenter da Acme Pagamentos. Para os amigos dela, é apenas uma celebração de plantão. Para um analista de segurança, essa foto entrega o nome da empresa, o cargo dela, a localização exata do datacenter e até o formato do crachá corporativo. O adversário não precisou quebrar nenhum firewall para obter esses dados."
- **Fatos Técnicos Preservados:**
  - [x] Personagem: Marina Sousa (@marina.souza)
  - [x] Organização fictícia: Acme Pagamentos
  - [x] Elementos da imagem: Crachá, tela ao fundo, novo datacenter
  - [x] Marco inicial do fio narrativo unificado

---

### Slide 07 · Caso Twitter / Cinema
- **Cabeçalho:** Slide 07 | Arquivo: `slides/01-conceito-contexto.html` | Apresentadora: Geovana | Título Original: `O post que virou coordenada.`
- **Objetivo Didático Central:** Apresentar estudo de caso real de rastreamento físico com latência zero baseado no cruzamento de postagens em tempo real.
- **Diagnóstico de AI Slop & Engessamento:** Título fragmentado; contraste binário rígido na linha 310 (*"Não foi invasão. Foi leitura de contexto em tempo real."*); uso de travessão rítmico.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Rastreamento Físico em Tempo Real` | Subtítulo: `Determinação de coordenadas geográficas a partir de mensagens abertas`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - O caso do desentendimento em rede social que culminou em confronto físico em um cinema.
    - Mecânica investigativa da correlação:
      1. *Sinal:* Tweet anunciando sessão de cinema às 21h em shopping específico.
      2. *Cruzamento:* Consulta à grade pública de filmes e horários do complexo.
      3. *Resultado:* Localização física exata da pessoa com janela de 120 minutos de previsibilidade.
  - *Modelo Mental / Metáfora Funcional:* O rastro de migalhas com horário marcado: o alvo anuncia onde estará pelos próximos 120 minutos e perde qualquer privacidade física.
  - *Roteiro e Tom do Apresentador:* "Vejam este caso concreto que repercutiu amplamente. Dois usuários se desentenderam em uma discussão pública no Twitter. Um deles postou que estava na fila do cinema para a sessão das 21h. O interlocutor consultou a programação do shopping, foi até a sala de exibição e abordou o desafeto presencialmente. A localização física foi obtida sem interceptar sinal de GPS ou invadir conta; bastou correlacionar o post público com a grade de horários do cinema."
- **Fatos Técnicos Preservados:**
  - [x] Plataforma: Twitter/X
  - [x] Caso real do cinema e correlação de horário/local
  - [x] Dedução analítica: horário de sessão e presença física

---

### Slide 08 · Caso Smart Sampa
- **Cabeçalho:** Slide 08 | Arquivo: `slides/01-conceito-contexto.html` | Apresentadora: Geovana | Título Original: `58 mil câmeras. 11 meses de senhas expostas.`
- **Objetivo Didático Central:** Analisar o incidente real do sistema Smart Sampa em São Paulo (outubro de 2026), demonstrando os riscos da exposição prolongada de credenciais de infraestrutura pública.
- **Diagnóstico de AI Slop & Engessamento:** Título fragmentado em números (`58 mil câmeras. 11 meses de senhas expostas`); antítese fraca e vaga ("não por um exploit sofisticado, mas por uma falha de cuidado"); aforismo dramático de encerramento ("é o convite").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Caso Smart Sampa (São Paulo, 2026)` | Subtítulo: `Exposição contínua de credenciais de videomonitoramento municipal`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Dados do caso real: reportagem de 21/10/2026 sobre o sistema de monitoramento de São Paulo.
    - Métricas: Acesso potencial a 58.000 câmeras de vigilância urbana.
    - Mecânica do incidente: Credenciais administrativas permaneceram indexadas e acessíveis por 11 meses consecutivos devido a repositórios desprotegidos e ausência de rotação periódica de chaves.
    - Consequência técnica: O acesso não exigiu exploração de vulnerabilidade de dia zero (zero-day); bastou coletar credenciais expostas publicamente.
  - *Modelo Mental / Metáfora Funcional:* A chave mestra esquecida no quadro de avisos: não foi necessário arrombar a fechadura da prefeitura; a chave estava pendurada em local visível a qualquer transeunte.
  - *Roteiro e Tom do Apresentador:* "Um caso recente e muito expressivo ocorreu na cidade de São Paulo em outubro de 2026 com o projeto Smart Sampa. Credenciais de acesso ao sistema de 58 mil câmeras de videomonitoramento ficaram expostas na internet por 11 meses. Não houve exploração de vulnerabilidade avançada no software de vídeo; as senhas estavam simplesmente disponíveis em repositórios abertos. O reconhecimento defensivo teria detectado essa exposição nos primeiros dias."
- **Fatos Técnicos Preservados:**
  - [x] Nome do caso: Smart Sampa
  - [x] Local e ano: São Paulo, Outubro de 2026
  - [x] Métrica: 58 mil câmeras
  - [x] Duração da exposição: 11 meses
  - [x] Fonte de referência: Matéria de 21/10/2026

---

### Slide 09 · Definição Formal de Reconhecimento
- **Cabeçalho:** Slide 09 | Arquivo: `slides/01-conceito-contexto.html` | Apresentadora: Geovana | Título Original: `Recon não é invadir. É entender.`
- **Objetivo Didático Central:** Formalizar a definição de reconhecimento ofensivo ancorando-se na matriz MITRE ATT&CK (TA0043) e delimitar a fronteira entre recon ativo e passivo.
- **Diagnóstico de AI Slop & Engessamento:** Título estruturado na antítese mecânica central ("Recon não é invadir. É entender."); repetição de contrastes negativos ("não a invasão"); quiasmo forçado nas notas ("entender sem tocar é o passivo; tocar para entender é o ativo").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Definição de Reconhecimento` | Subtítulo: `Mapeamento sistemático da superfície de ataque e tática MITRE ATT&CK TA0043`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - `Conceito:` Conjunto de metodologias e técnicas destinadas a descobrir, catalogar e correlacionar informações sobre a infraestrutura, serviços e pessoas ligadas ao alvo.
    - `Classificação operacional:`
      1. *Reconhecimento Passivo:* Coleta realizada exclusivamente em fontes externas de terceiros, gerando zero pacotes direcionados ao alvo.
      2. *Reconhecimento Ativo:* Interação direta com a infraestrutura do alvo por meio de varreduras de rede e consultas de protocolo com ferramentas como o Nmap.
    - `Referencial:` Tática preparatória inicial MITRE ATT&CK TA0043.
  - *Modelo Mental / Metáfora Funcional:* O diagnóstico antes do tratamento: nenhum médico opera sem antes solicitar exames laboratoriais e imagens; o reconhecimento é o diagnóstico completo da rede.
  - *Roteiro e Tom do Apresentador:* "Com esses exemplos, consolidamos a definição formal. Na matriz internacional MITRE ATT&CK, o reconhecimento é catalogado sob o código TA0043 como a tática preparatória de qualquer operação de segurança. Ele se divide em duas modalidades: o passivo, onde consultamos bases externas sem tocar no alvo, e o ativo, onde enviamos pacotes para descobrir portas e versões com ferramentas como o Nmap. Passo agora a palavra ao Emilio, que demonstrará a mecânica técnica do reconhecimento ativo."
- **Fatos Técnicos Preservados:**
  - [x] Código MITRE ATT&CK: TA0043 (Reconnaissance)
  - [x] Divisão conceitual: Ativo vs. Passivo
  - [x] Ferramenta central de reconhecimento ativo antecipada: Nmap
  - [x] Delimitação de escopo sem exploração de falhas
  - [x] Gancho de transição para o apresentador Emilio

---
```
================================================================================
ARQUIVO 03 / 12: slides/02-recon-ativo.html
Bloco Temático: Bloco 02 — Reconhecimento Ativo
Apresentador: Emilio
Slides: 10 a 15
================================================================================
```

### Slide 10 · Divisor do Bloco 02
- **Cabeçalho:** Slide 10 | Arquivo: `slides/02-recon-ativo.html` | Apresentador: Emilio | Título Original: `Quando o alvo começa a responder.`
- **Objetivo Didático Central:** Introduzir o Bloco 02 caracterizando a natureza do reconhecimento ativo: o envio direto de pacotes IP pela rede e a consequente geração de telemetria e registros nos sistemas de segurança do alvo.
- **Diagnóstico de AI Slop & Engessamento:** Título melodramático simulando suspense de seriado ("Quando o alvo começa a responder / Aqui saem pacotes de verdade. E com eles, rastros.").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Reconhecimento Ativo` | Subtítulo: `Interação direta via pacotes IP, varredura de portas e análise de tráfego`.
  - *Proposta de Corpo de Texto e Tópicos:* `Bloco 02 · Emilio`. Declaração de princípio: "No reconhecimento ativo, o analista emite sondagens diretas contra a rede do alvo para identificar portas abertas, versões de serviços e fluxos de dados."
  - *Modelo Mental / Metáfora Funcional:* Tocar na maçaneta: a transição entre observar a vitrine de longe e aproximar-se da porta para testar a fechadura.
  - *Roteiro e Tom do Apresentador:* "Obrigado, Geovana. Entramos agora no Bloco 02 para falar de Reconhecimento Ativo. A diferença central em relação ao bloco anterior é física: aqui nós geramos pacotes TCP/IP reais endereçados à máquina do alvo. Vamos entender como ferramentas consagradas como Nmap e Wireshark operam, e por que essa interação gera rastros inevitáveis em firewalls e sistemas de detecção de intrusão."
- **Fatos Técnicos Preservados:**
  - [x] Numeração do Bloco: 02
  - [x] Apresentador responsável: Emilio
  - [x] Caracterização técnica da transmissão direta de pacotes

---

### Slide 11 · Redes Simplificadas
- **Cabeçalho:** Slide 11 | Arquivo: `slides/02-recon-ativo.html` | Apresentador: Emilio | Título Original: `Três coisas que você precisa saber sobre redes`
- **Objetivo Didático Central:** Nivelar o conhecimento técnico da audiência sobre os três elementos estruturais da comunicação TCP/IP: Endereço IP (host), Porta Lógica (processo escutando) e Pacote (unidade de dados com cabeçalhos).
- **Diagnóstico de AI Slop & Engessamento:** Abertura típica de caça-cliques de internet (*Throat-clearing opener* "Três coisas que você precisa saber sobre redes").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fundamentos de Rede para Reconhecimento` | Subtítulo: `Endereçamento IP, portas de serviço e encapsulamento de pacotes`.
  - *Proposta de Corpo de Texto e Tópicos:*
    1. `Endereço IP (O Host):` O identificador numérico que localiza uma interface de rede específica na internet ou rede local (comunicação entre o cliente `10.10.14.5` e o alvo `10.10.14.23`).
    2. `Porta Lógica (O Processo):` Um ponto de terminação de 16 bits (0 a 65.535). Uma porta aberta significa que um daemon ou software está ativamente escutando requisições do sistema operacional.
    3. `Pacote IP/TCP (A Mensagem):` Carga útil estruturada contendo cabeçalhos com IPs de origem/destino, portas, números de sequência e flags de controle (SYN, ACK, FIN, RST), base para análise com Nmap e Wireshark.
  - *Modelo Mental / Metáfora Funcional:* A analogia clássica do correio: o IP é o endereço do edifício; a porta lógica é o número do apartamento; o pacote é o envelope com remetente, destinatário e lacre de segurança.
  - *Roteiro e Tom do Apresentador:* "Para quem nunca configurou um scanner de portas, pensemos nestes três pilares: o IP localiza a máquina na rede — no nosso laboratório, o atacante em `10.10.14.5` e o servidor em `10.10.14.23`. A porta lógica indica qual programa está aguardando conexões: porta 80 é servidor web, 22 é terminal SSH remoto, 3306 é banco de dados MySQL. E o pacote é o envelope que transporta as mensagens entre cliente e servidor com flags de controle bem definidas, inspecionadas no Nmap e Wireshark."
- **Fatos Técnicos Preservados:**
  - [x] Conceito de Endereço IP e relação cliente (`10.10.14.5`) vs alvo (`10.10.14.23`)
  - [x] Faixa de portas: 0 a 65.535 (16 bits)
  - [x] Estrutura e flags de pacotes TCP inspecionados via Nmap e Wireshark
  - [x] Diagrama SVG de topologia (notebook, roteador gateway, servidor, pacote SYN)

---

### Slide 12 · Nmap Simulação
- **Cabeçalho:** Slide 12 | Arquivo: `slides/02-recon-ativo.html` | Apresentador: Emilio | Título Original: `Nmap: o mapa que o alvo entrega sem querer`
- **Objetivo Didático Central:** Demonstrar a execução real de uma varredura de portas completa (`-p-`) com detecção de versão (`-sV`) e técnica SYN scan (`-sS`), interpretando os resultados da superfície de ataque exposta.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e personificação do alvo ("Nmap: o mapa que o alvo entrega sem querer"); antíteses mecânicas repetidas ("não explora nada. Ele só pergunta"); travessões excessivos usados como marcadores de parâmetros.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Varredura de Portas com Nmap` | Subtítulo: `Enumeração de portas e detecção de versões de serviço via SYN Scan`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Comando executado: `nmap -sS -sV -p- 10.10.14.23 -oA recon_alvo`
    - Decomposição das flags:
      - `-sS`: SYN Scan (conexão semiaberta, stealth scan).
      - `-sV`: Sondagem de versão dos serviços em execução.
      - `-p-`: Varredura em todas as 65.535 portas TCP.
      - `-oA`: Exportação simultânea nos três formatos (texto puro `.nmap`, XML `.xml` e grepable `.gnmap`).
    - Análise dos serviços descobertos em 41,72 segundos:
      - `22/tcp open ssh`: OpenSSH 8.9p1 (Ubuntu).
      - `80/tcp open http`: nginx 1.24.0.
      - `443/tcp open ssl/http`: nginx 1.24.0.
      - `3306/tcp open mysql`: MySQL 8.0.35 (atenção: banco de dados exposto diretamente).
      - `8080/tcp open http-proxy`: Jetty 9.4.53 (painel interno ou aplicação legado).
      - `3389/tcp filtered`: RDP (bloqueado por firewall).
  - *Modelo Mental / Metáfora Funcional:* *Bater e correr na campainha:* O Nmap envia o pacote SYN. Se a porta estiver aberta, o servidor devolve SYN/ACK. Em vez de enviar o ACK para abrir a sessão, o scanner devolve RST (reset) e encerra a conversa. O servidor não chega a estabelecer a conexão nem registrar log de aplicação, mas o atacante já descobriu o serviço.
  - *Roteiro e Tom do Apresentador:* "Temos aqui a saída real de um scan em laboratório autorizado. Notem os parâmetros: o `-sS` é o SYN scan; enviamos o primeiro pacote do handshake e, ao receber o SYN/ACK, cancelamos com RST. Em 41 segundos, testamos todas as 65 mil portas. O que chama nossa atenção imediatamente? A porta 3306 do MySQL está aberta para a rede externa, sem isolamento de banco de dados, e a porta 8080 roda uma aplicação Jetty. Ambas são alvos prioritários de investigação."
- **Fatos Técnicos Preservados:**
  - [x] Comando: `nmap -sS -sV -p- 10.10.14.23 -oA recon_alvo`
  - [x] Versão Nmap: 7.95
  - [x] IP do alvo: `10.10.14.23` (rede de laboratório `10.10.14.0/24`)
  - [x] Portas e versões exatas: 22 (OpenSSH 8.9p1), 80/443 (nginx 1.24.0), 3306 (MySQL 8.0.35), 8080 (Jetty 9.4.53)
  - [x] Porta filtrada: 3389 (RDP)
  - [x] Tempo total de execução: 41,72 segundos
  - [x] Arquivos gerados: `recon_alvo.nmap` (18K) e `recon_alvo.xml` (42K)

---

### Slide 13 · Wireshark Simulação
- **Cabeçalho:** Slide 13 | Arquivo: `slides/02-recon-ativo.html` | Apresentador: Emilio | Título Original: `Wireshark: o que realmente passa no fio`
- **Objetivo Didático Central:** Apresentar a interface e a utilidade do Wireshark para inspeção profunda de pacotes (DPI), demonstrando a aplicação de filtros de exibição para isolar sessões HTTP entre milhares de pacotes capturados.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal, advérbio vazio e gíria de telecomunicações ("o que realmente passa no fio"); antítese poética artificial na linha 305 ("Sem filtro, 1.284 pacotes viram ruído. Com filtro, sete contam uma história.").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Inspeção de Tráfego com Wireshark` | Subtítulo: `Filtragem de pacotes e análise da pilha de protocolos na interface de rede`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Captura na interface `eth0`: Total de **1.284 pacotes** capturados.
    - Sintaxe do filtro de exibição: `ip.addr == 10.10.14.23 && tcp.port == 80`
    - Resultado da filtragem: **7 pacotes** isolados (0,5% do total capturado).
    - Camadas do pacote 1 inspecionado na árvore de dissecação:
      - *Frame 1:* 74 bytes capturados na interface.
      - *Ethernet II:* MAC Origem (`00:1a:2b:3c:4d:5e`) e MAC Destino (`00:0c:29:aa:bb:cc`).
      - *IPv4:* Origem `10.10.14.23` $\rightarrow$ Destino `10.10.14.5`.
      - *TCP:* Porta origem 49812 $\rightarrow$ Porta destino 80, Flag `0x002 (SYN)`, Window: 64240, MSS=1460.
    - Visualização hexadecimal e ASCII correspondente no painel inferior.
  - *Modelo Mental / Metáfora Funcional:* A escuta telefônica da rede: o Wireshark não transmite nada; ele atua em modo promíscuo gravando cada bit que atravessa a placa de rede e permitindo examinar o conteúdo envelope por envelope.
  - *Roteiro e Tom do Apresentador:* "Vimos as portas abertas no Nmap. Agora abrimos o Wireshark para inspecionar os pacotes trafegados na interface eth0. Em poucos segundos, capturamos mais de 1.200 pacotes. Para não nos perdermos em dados dispersos, aplicamos o filtro `ip.addr == 10.10.14.23 && tcp.port == 80`. Imediatamente a tela isola apenas 7 pacotes: vemos o handshake TCP, a requisição HTTP GET para `/admin/` e a resposta do servidor com o status `401 Unauthorized`. Abaixo, a árvore de protocolos disseca cada byte do cabeçalho."
- **Fatos Técnicos Preservados:**
  - [x] Filtro Wireshark: `ip.addr == 10.10.14.23 && tcp.port == 80`
  - [x] Interface: `eth0`
  - [x] Total de pacotes: 1.284 | Exibidos no filtro: 7 (0,5%)
  - [x] Detalhes de camada: Frame (74 bytes), Ethernet II MACs, IPv4 (`10.10.14.23` para `10.10.14.5`), TCP portas 49812 e 80, Flag `0x002 (SYN)`
  - [x] Sequência de pacotes: SYN, SYN/ACK, ACK, GET /admin/, ACK, 401 Unauthorized, GET com credenciais

---

### Slide 14 · Wireshark Handshake e Stream
- **Cabeçalho:** Slide 14 | Arquivo: `slides/02-recon-ativo.html` | Apresentador: Emilio | Título Original: `Três pacotes para abrir uma conexão. Um clique para ler tudo.`
- **Objetivo Didático Central:** Explicar a mecânica temporal do TCP Three-Way Handshake em microssegundos e demonstrar como o recurso *Follow TCP Stream* do Wireshark remonta a conversa HTTP, revelando credenciais em texto puro codificadas em Base64.
- **Diagnóstico de AI Slop & Engessamento:** Título com fragmentação simétrica sensacionalista ("Três pacotes... Um clique..."); contrastes binários repetidos na nota do diagrama e no rodapé ("não diz o que responde", "os metadados, não").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Handshake TCP e Reconstrução de Sessão` | Subtítulo: `Validação de conexão em 0,2 ms e decodificação de credenciais HTTP Basic Auth`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Diagrama sequencial do Three-Way Handshake TCP:
      - `t=0.000000s`: Cliente (49812) envia `SYN (Seq=0)` ao Servidor (80).
      - `t=0.000187s`: Servidor responde `SYN, ACK (Seq=0, Ack=1)`.
      - `t=0.000203s`: Cliente confirma com `ACK (Seq=1, Ack=1)`. Conexão estabelecida em 0,203 ms.
      - `t=0.000310s`: Envio de dados HTTP `GET /admin/`.
    - Painel *Follow TCP Stream (Stream 0 · 412 bytes)*:
      - Requisição: `GET /admin/ HTTP/1.1` | Host: `10.10.14.5:8080`
      - Desafio do servidor: `HTTP/1.1 401 Unauthorized` | `WWW-Authenticate: Basic realm="Jetty Admin"`
      - Nova requisição autenticada: `Authorization: Basic YWRtaW46YWRtaW4=`
      - Decodificação: A string Base64 `YWRtaW46YWRtaW4=` equivale diretamente a `admin:admin`.
  - *Modelo Mental / Metáfora Funcional:* *O envelope de celofane:* HTTP Basic Authentication opera como um envelope transparente de celofane: apenas codifica caracteres em base64 para transporte, permitindo que qualquer analisador na rede recupere a senha em texto claro.
  - *Roteiro e Tom do Apresentador:* "Observem o diagrama à esquerda: o aperto de mão TCP acontece em apenas 0,2 milissegundos. Assim que a conexão abre, o cliente solicita a página `/admin/`. O servidor Jetty devolve erro 401 informando que exige autenticação básica. O navegador então reenvia a requisição incluindo o cabeçalho `Authorization: Basic YWRtaW46YWRtaW4=`. Clicamos com o botão direito no Wireshark e selecionamos 'Follow TCP Stream'. Como a conexão não usava HTTPS, a string em Base64 é imediatamente revertida para o usuário `admin` e senha `admin`."
- **Fatos Técnicos Preservados:**
  - [x] Tempos e sequência do Three-Way Handshake: 0.000000 (SYN), 0.000187 (SYN/ACK), 0.000203 (ACK), 0.000310 (GET)
  - [x] Portas: Cliente 49812 e Servidor 80 / 8080
  - [x] Janela Follow TCP Stream: Stream 0, tamanho total de 412 bytes
  - [x] Realm do servidor: `Jetty Admin`
  - [x] Cabeçalho HTTP: `Authorization: Basic YWRtaW46YWRtaW4=`
  - [x] Par de credenciais decodificado: `admin:admin`

---

### Slide 15 · Phishing e Engenharia Social
- **Cabeçalho:** Slide 15 | Arquivo: `slides/02-recon-ativo.html` | Apresentador: Emilio | Título Original: `O exploit é a confiança`
- **Objetivo Didático Central:** Integrar a engenharia social e o spear-phishing à cadeia de reconhecimento, demonstrando como dados públicos corporativos tornam mensagens fraudulentas altamente verossímeis.
- **Diagnóstico de AI Slop & Engessamento:** Título com aforismo pretensioso (*Fake-profound aphorism* "O exploit é a confiança"); contraste binário forçado na linha 480 ("Planilha com macros não é formulário de RH. É execução de código.").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Engenharia Social e Spear-Phishing` | Subtítulo: `A exploração do fator humano embasada em dados prévios de reconhecimento`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Simulação de e-mail malicioso direcionado aos colaboradores da Acme Pagamentos:
      - Remetente forjado: `RH · Benefícios <rh@beneficios-acme.com>` (domínio similar / typosquatting).
      - Destinatário corporativo: `voce@acme.com.br`.
      - Assunto urgente: `Atualização obrigatória do plano de saúde — até hoje`.
      - Anexo perigoso: `Formulario_Plano_2026.xlsx` (arquivo contendo macros VBA maliciosas).
    - Análise dos quatro gatilhos psicológicos alimentados por recon:
      1. *Urgência artificial:* Prazo até 18h do mesmo dia sob pena de suspensão do benefício.
      2. *Autoridade legítima:* Simulação do departamento interno de Recursos Humanos.
      3. *Contexto verossímil:* Padrão de e-mails corporativos da organização obtido previamente.
      4. *Vetor de execução:* Planilha com solicitação para habilitar macros de automação.
  - *Modelo Mental / Metáfora Funcional:* O uniforme falso do entregador: o atacante não arromba a porta giratória blindada do banco; ele veste o crachá e o colete da transportadora e o próprio funcionário abre a porta.
  - *Roteiro e Tom do Apresentador:* "Vimos a varredura e a interceptação de pacotes na rede. Mas há outro vetor de reconhecimento ativo: a engenharia social. Vejam este e-mail forjado para os funcionários da Acme Pagamentos. Por que um ataque desse tipo funciona? Porque o invasor fez reconhecimento prévio: descobriu que a empresa usa o domínio `acme.com.br`, identificou o setor de RH e registrou um domínio similar para forjar a comunicação. Ao abrir o anexo e habilitar macros, o usuário executa código malicioso dentro do computador da empresa."
- **Fatos Técnicos Preservados:**
  - [x] Organização fictícia do fio condutor: Acme Pagamentos
  - [x] Remetente simulado: `rh@beneficios-acme.com`
  - [x] Destinatário corporativo: `voce@acme.com.br`
  - [x] Anexo: `Formulario_Plano_2026.xlsx`
  - [x] Quatro vetores de engenharia social (urgência, autoridade, credibilidade de domínio e execução por macros)
  - [x] Conexão com a personagem Marina Sousa

---

```
================================================================================
ARQUIVO 04 / 12: slides/03a-passivo-introducao.html
Bloco Temático: Bloco 03 (Parte 1) — Reconhecimento Passivo & Introdução
Apresentador: Daniel
Slides: 16 a 18
================================================================================
```

### Slide 16 · Divisor do Bloco 03
- **Cabeçalho:** Slide 16 | Arquivo: `slides/03a-passivo-introducao.html` | Apresentador: Daniel | Título Original: `Coletar sem tocar.`
- **Objetivo Didático Central:** Marcar a abertura do Bloco 03 (o maior bloco do seminário), definindo a tese central do reconhecimento passivo: obter inteligência profunda sobre a organização sem gerar nenhum tráfego em sua direção.
- **Diagnóstico de AI Slop & Engessamento:** Título fragmentado com efeito poético ("Coletar sem tocar.").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Reconhecimento Passivo e OSINT` | Subtítulo: `Coleta de inteligência em fontes externas sem interação com a infraestrutura do alvo`.
  - *Proposta de Corpo de Texto e Tópicos:* `Bloco 03 · Daniel`. Princípio operacional: "No reconhecimento passivo, todas as requisições são direcionadas a servidores públicos e índices de terceiros, preservando a invisibilidade em relação aos firewalls do alvo."
  - *Modelo Mental / Metáfora Funcional:* A consulta aos livros de cartório: investigar o patrimônio de alguém lendo registros públicos no cartório de imóveis, sem que a pessoa receba qualquer aviso.
  - *Roteiro e Tom do Apresentador:* "Obrigado, Emilio. Assumo a apresentação para conduzir o Bloco 03, dedicado ao Reconhecimento Passivo e à Inteligência em Fontes Abertas (OSINT). Se o Emilio acabou de mostrar como enviar pacotes e interagir com portas de rede, aqui a nossa regra fundamental é a oposta: não emitiremos um único pacote contra o alvo. Veremos como mapear servidores, certificados, tecnologias e pessoas consultando exclusivamente bases que já existem na internet."
- **Fatos Técnicos Preservados:**
  - [x] Numeração do Bloco: 03
  - [x] Apresentador responsável: Daniel
  - [x] Princípio fundamental de zero pacotes ao alvo

---

### Slide 17 · Conceito de Reconhecimento Passivo
- **Cabeçalho:** Slide 17 | Arquivo: `slides/03a-passivo-introducao.html` | Apresentador: Daniel | Título Original: `Mapear a pegada sem consultar o alvo.`
- **Objetivo Didático Central:** Explicar a topologia de isolamento do reconhecimento passivo, demonstrando como o analista consulta provedores intermediários (índices, DNS e repositórios) enquanto a infraestrutura do alvo permanece intocada.
- **Diagnóstico de AI Slop & Engessamento:** Emprego de palavra informal/jargão vago (`pegada` em vez de superfície de ataque externa); tautologia no rodapé ("OSINT, fontes abertas e o ecossistema").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Topologia de Coleta Passiva` | Subtítulo: `Mapeamento da superfície externa através de intermediários e repositórios públicos`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Esquema de comunicação triangular:
      - *Analista $\rightarrow$ Servidores Públicos de Terceiros:* Consultas a motores de busca, bases WHOIS, logs de Certificate Transparency e scanners de varredura global.
      - *Alvo:* Permanece em repouso completo, sem registrar logs de conexão nem alertas em seus sistemas perimetrais.
    - Tipos de dados obtidos de forma passiva:
      1. Blocos de endereçamento IP e Sistemas Autônomos (ASN).
      2. Nomes de subdomínios e histórico de certificados SSL/TLS.
      3. Pilhas de tecnologia e vagas de emprego corporativas.
      4. Credenciais vazadas em incidentes anteriores.
  - *Modelo Mental / Metáfora Funcional:* A consulta aos jornais arquivados na biblioteca pública: você lê tudo sobre a empresa sem precisar ligar para a recepção dela.
  - *Roteiro e Tom do Apresentador:* "Vejam este esquema: quando fazemos recon passivo, todo o nosso tráfego de rede vai para terceiros — para o Google, para o Shodan, para os servidores de Certificate Transparency. O firewall do alvo não acende nenhuma luz vermelha porque nenhum byte foi enviado para o IP da empresa. Estamos lendo o que o ecossistema da internet já registrou sobre ela."
- **Fatos Técnicos Preservados:**
  - [x] Topologia do reconhecimento passivo
  - [x] Relação Analista $\leftrightarrow$ Fontes Externas $\leftrightarrow$ Alvo
  - [x] Princípio de ausência de alertas em SIEM e firewalls locais

---

### Slide 18 · O que é OSINT
- **Cabeçalho:** Slide 18 | Arquivo: `slides/03a-passivo-introducao.html` | Apresentador: Daniel | Título Original: `Informação pública não é informação inofensiva.`
- **Objetivo Didático Central:** Definir com precisão metodológica o conceito de OSINT (Open Source Intelligence), estabelecendo que inteligência exige método, validação temporal e correlação, e não apenas busca desordenada na web.
- **Diagnóstico de AI Slop & Engessamento:** Título com antítese clássica ("não é inofensiva"); violação flagrante de palavra banida pela skill (`acionável` / *actionable* na linha 72); travessões duplos; card com rotulagem autoelogiosa ("REGRA DE OURO").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Inteligência em Fontes Abertas (OSINT)` | Subtítulo: `Metodologia de coleta, validação e correlação de dados públicos`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - `Definição de OSINT:` Disciplina de inteligência que envolve a coleta, o processamento e a análise sistemática de dados de acesso público para responder a objetivos investigativos específicos.
    - `Diferenciação conceitual:`
      - Dado isolado: um número de IP ou nome de subdomínio encontrado em um registro.
      - Inteligência contextualizada: a correlação que comprova que aquele subdomínio hospeda uma aplicação interna de pagamentos sem autenticação multifator.
    - `Ecossistema de fontes externas e ferramentas abertas:`
      - Mecanismos de busca e repositórios: Google, Bing, Brave, LinkedIn, GitHub e imprensa.
      - Infraestrutura e cartórios de certificados: Shodan, Censys, WHOIS e crt.sh.
      - Arquivos históricos e bases de incidentes: **Wayback Machine** (arquivo histórico de páginas web) e **Have I Been Pwned / HIBP** (consulta a credenciais e contas expostas em vazamentos históricos).
    - `Métrica operacional permanente:` **0 pacotes** enviados aos servidores do alvo durante toda a rotina de levantamento.
    - *(Eliminação do termo banido `acionável`; substituição por "para embasar decisões técnicas e operacionais").*
  - *Modelo Mental / Metáfora Funcional:* As peças de um quebra-cabeça: uma peça avulsa encontrada no chão parece insignificante; encaixada com outras vinte peças, revela o desenho completo da fechadura.
  - *Roteiro e Tom do Apresentador:* "Definimos aqui o conceito formal de OSINT: Open Source Intelligence. Muitas pessoas confundem OSINT com simplesmente digitar termos no Google. Mas inteligência é processo: envolve selecionar fontes confiáveis, filtrar ruído, verificar carimbos de data e cruzar dados para fundamentar decisões de segurança — consultando desde Shodan e Censys até o arquivo do Wayback Machine e bases de vazamentos como Have I Been Pwned / HIBP. E a nossa métrica contínua continua sendo zero pacotes enviados para a rede da organização."
- **Fatos Técnicos Preservados:**
  - [x] Definição formal de OSINT (Open Source Intelligence)
  - [x] Três pilares metodológicos: método, propósito e registro temporal
  - [x] Catálogo de fontes externas e ferramentas mapeadas: Shodan, Censys, WHOIS, crt.sh, Wayback Machine (arquivo histórico web) e Have I Been Pwned / HIBP (consulta a credenciais vazadas)
  - [x] Métrica: 0 pacotes enviados ao alvo
  - [x] Eliminação da palavra proibida "acionável"

---

```
================================================================================
ARQUIVO 05 / 12: slides/03b-ciclo-osint.html
Bloco Temático: Bloco 03 (Parte 2) — O Ciclo de OSINT em 6 Fases
Apresentador: Daniel
Slides: 19 a 25
================================================================================
```

### Slide 19 · Visão Geral do Ciclo de OSINT
- **Cabeçalho:** Slide 19 | Arquivo: `slides/03b-ciclo-osint.html` | Apresentador: Daniel | Título Original: `De uma pergunta à próxima.`
- **Objetivo Didático Central:** Apresentar a estrutura cíclica da inteligência em 6 fases interdependentes (Planejar, Coletar, Processar, Analisar, Disseminar, Feedback) via diagrama orbital SVG.
- **Diagnóstico de AI Slop & Engessamento:** Título fragmentado e lede de autoajuda ("De uma pergunta à próxima. Dados brutos só viram inteligência quando respondem a uma necessidade.").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `O Ciclo de Inteligência em Fontes Abertas` | Subtítulo: `As seis etapas sistemáticas para transformação de dados brutos em decisões de segurança`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Diagrama orbital com as 6 fases conectadas em loop contínuo:
      1. `Planejar:` Definição de escopo, perguntas investigativas e limites legais.
      2. `Coletar:` Extração em bases públicas com preservação de carimbos de data.
      3. `Processar:` Normalização de formatos, remoção de duplicatas e indexação.
      4. `Analisar:` Cruzamento de fontes independentes e validação de hipóteses.
      5. `Disseminar:` Elaboração de relatórios estruturados para tomada de decisão.
      6. `Feedback:` Revisão das lacunas encontradas e reorientação do escopo.
  - *Modelo Mental / Metáfora Funcional:* A engrenagem da investigação científica: uma pergunta gera experimentos, os dados são filtrados, o resultado é publicado e a conclusão gera novas perguntas.
  - *Roteiro e Tom do Apresentador:* "A investigação de OSINT não é aleatória; ela segue um ciclo de inteligência formalizado em seis fases bem definidas. Vamos percorrer essas seis etapas de forma dinâmica utilizando um exemplo didático em `example.com`: começamos formulando a pergunta técnica correta e acompanhamos o refinamento do dado até a entrega do relatório de segurança."
- **Fatos Técnicos Preservados:**
  - [x] As 6 fases do ciclo: Planejar, Coletar, Processar, Analisar, Disseminar, Feedback
  - [x] Diagrama orbital SVG em anel contínuo
  - [x] Domínio de teste educacional: `example.com` (RFC 2606)

---

### Slide 20 · Ciclo 01: Planejar
- **Cabeçalho:** Slide 20 | Arquivo: `slides/03b-ciclo-osint.html` | Apresentador: Daniel | Título Original: `Planejar: faça a pergunta certa.`
- **Objetivo Didático Central:** Explicar a Fase 1 do ciclo (Planejamento), ressaltando que sem delimitação prévia de escopo e objetivos a coleta se perde em volumes infinitos de dados irrelevantes.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e ordem aforística (*Robotic rhythm* clonado em 6 slides); etiquetas repetitivas de disclaimer burocrático ("CASO FICTÍCIO · PERGUNTA INICIAL").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fase 1 — Planejamento` | Subtítulo: `Formulação de requisitos, delimitação de escopo e definição de limites éticos`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Pergunta investigativa central do exemplo: *"Quais serviços e subdomínios associados ao domínio institucional example.com estão expostos na internet?"*
    - Critérios estabelecidos no planejamento:
      1. Delimitação estrita do domínio principal e suas zonas registradas.
      2. Definição do prazo temporal para análise (dados coletados nos últimos 12 meses).
      3. Proibição expressa de qualquer pacote ou varredura ativa direcionada aos servidores.
  - *Modelo Mental / Metáfora Funcional:* A bússola na selva: entrar na internet sem escopo é como entrar em uma floresta sem bússola; você anda muito e não chega a lugar nenhum.
  - *Roteiro e Tom do Apresentador:* "Começamos pela Fase 1: Planejamento. Aqui definimos a pergunta que queremos responder. No nosso estudo, a pergunta é: quais serviços vinculados ao domínio example.com estão acessíveis na internet? Definir o escopo evita perder horas analisando servidores que não pertencem à empresa ou coletando dados sem relevância operacional."
- **Fatos Técnicos Preservados:**
  - [x] Fase 1: Planejamento
  - [x] Domínio de teste: `example.com`
  - [x] Requisitos de escopo e conformidade ética

---

### Slide 21 · Ciclo 02: Coletar (Tríade CT — Parte 1: Evidência Bruta)
- **Cabeçalho:** Slide 21 | Arquivo: `slides/03b-ciclo-osint.html` | Apresentador: Daniel | Título Original: `Coletar: reúna evidências, não certezas.`
- **Objetivo Didático Central:** Demonstrar a Fase 2 (Coleta) focando na preservação da procedência do dado bruto e introduzindo a primeira faceta de Certificate Transparency: o registro histórico imutável como evidência sem atestado de status atual.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e contraste binário ("evidências, não certezas"); etiqueta redundante de dados fictícios.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fase 2 — Coleta` | Subtítulo: `Levantamento sistemático em bases públicas e preservação de procedência`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Dado bruto coletado na simulação:
      - Fonte 1 (Registro de certificados CT): Certificado SSL/TLS contendo o subdomínio `portal.example.com` emitido em 14 de março de 2024 pela autoridade `Let's Encrypt Authority X3`.
      - Fonte 2 (Índice externo de serviços): Associação prévia do nome a um serviço web ativo no endereço reservado de documentação RFC 5737 `192.0.2.10` na porta HTTPS `443`.
    - Princípio da evidência bruta: O log de certificados comprova categoricamente que um certificado foi emitido para aquele nome naquela data e associado ao IP `192.0.2.10:443`, mas **não atesta** se o host físico continua ligado hoje.
  - *Modelo Mental / Metáfora Funcional:* A certidão de nascimento no cartório: o documento prova que a pessoa nasceu naquele dia, mas você precisa de outras fontes para saber onde ela mora hoje.
  - *Roteiro e Tom do Apresentador:* "Passamos para a Fase 2: Coleta. Aqui buscamos as evidências brutas em repositórios externos. Localizamos um registro de Certificate Transparency indicando que foi emitido um certificado para `portal.example.com` associado ao IP de teste `192.0.2.10` na porta 443. Guardamos o carimbo de data e a fonte emissora. O registro comprova a existência do subdomínio no histórico da empresa, mas ainda não sabemos se o servidor responde."
- **Fatos Técnicos Preservados:**
  - [x] Fase 2: Coleta
  - [x] Subdomínio alvo: `portal.example.com`
  - [x] Endereço de documentação associado: `192.0.2.10` na porta HTTPS `443`
  - [x] Primeira aparição funcional de CT: registro bruto como evidência
  - [x] Preservação de timestamp e procedência

---

### Slide 22 · Ciclo 03: Processar
- **Cabeçalho:** Slide 22 | Arquivo: `slides/03b-ciclo-osint.html` | Apresentador: Daniel | Título Original: `Processar: separe sinal de ruído.`
- **Objetivo Didático Central:** Explicar a Fase 3 (Processamento), detalhando as técnicas de higienização de dados: desduplicação, conversão de formatos (JSON/CSV) e descarte de dados fora do escopo.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e clichê corporativo de IA ("separe sinal de ruído").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fase 3 — Processamento` | Subtítulo: `Normalização de registros, remoção de duplicatas e catalogação temporal`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Operações técnicas de processamento:
      1. *Parsing:* Extração de campos estruturados a partir de respostas brutas em JSON e HTML.
      2. *Deduplicação:* Eliminação de 40 certificados emitidos para o mesmo domínio ao longo de renovações automáticas sucessivas.
      3. *Filtragem de escopo:* Descarte de subdomínios de CDNs e provedores de terceiros que não pertencem ao bloco IP sob análise.
    - Saída processada: Tabela limpa associando subdomínio, data mais recente e hashes de validação.
  - *Modelo Mental / Metáfora Funcional:* A esteira de triagem de minério: o analista lava a terra e separa as pedras britadas antes de tentar lapidar o diamante.
  - *Roteiro e Tom do Apresentador:* "Na Fase 3, processamos o material bruto. Uma consulta em bases de certificados pode retornar 50 entradas para o mesmo host devido às renovações trimestrais do Let's Encrypt. O processamento remove duplicatas, padroniza as datas e descarta nomes que pertenciam a fornecedores descontinuados, entregando uma base limpa para a etapa analítica."
- **Fatos Técnicos Preservados:**
  - [x] Fase 3: Processamento
  - [x] Operações de deduplicação e normalização
  - [x] Separação de registros históricos e ativos

---

### Slide 23 · Ciclo 04: Analisar
- **Cabeçalho:** Slide 23 | Arquivo: `slides/03b-ciclo-osint.html` | Apresentador: Daniel | Título Original: `Analisar: conecte sem presumir.`
- **Objetivo Didático Central:** Apresentar a Fase 4 (Análise), demonstrando como a correlação entre fontes independentes valida hipóteses técnicas sem gerar falsos positivos.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e aforismo imperativo (*"Analisar: conecte sem presumir"*); nominalização pesada ("realização da verificação autorizada").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fase 4 — Análise` | Subtítulo: `Cruzamento de fontes independentes e validação de hipóteses técnicas`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Cruzamento de evidências na simulação:
      - Fonte 1 (Certificate Transparency): Registro de `portal.example.com`.
      - Fonte 2 (DNS Passivo / SecurityTrails): O subdomínio apontava historicamente para o bloco `192.0.2.0/24`.
      - Fonte 3 (Shodan/Censys): O IP `192.0.2.10` mantém a porta 443 aberta com banner Nginx e certificado coincidente.
    - Hipótese técnica validada: O portal de acesso existe, está ativo e possui serviços associados sem que precisássemos emitir varredura própria contra o IP.
  - *Modelo Mental / Metáfora Funcional:* A triangulação de antenas: um sinal isolado dá apenas uma direção vaga; o cruzamento de três antenas independentes aponta o ponto exato no mapa.
  - *Roteiro e Tom do Apresentador:* "Chegamos à Fase 4: Análise. Aqui cruzamos os dados limpos. O certificado apontou o subdomínio `portal.example.com`. Consultamos o DNS histórico e descobrimos o IP `192.0.2.10`. Consultamos os índices do Shodan e confirmamos que esse IP responde na porta 443 com o mesmo certificado. Sem tocar no servidor, três fontes independentes confirmaram a existência e a localização do serviço."
- **Fatos Técnicos Preservados:**
  - [x] Fase 4: Análise
  - [x] Endereçamento RFC 5737: `192.0.2.10` (TEST-NET-1) e bloco `192.0.2.0/24`
  - [x] Cruzamento de CT + DNS Passivo + Portas indexadas

---

### Slide 24 · Ciclo 05: Disseminar
- **Cabeçalho:** Slide 24 | Arquivo: `slides/03b-ciclo-osint.html` | Apresentador: Daniel | Título Original: `Disseminar: entregue algo acionável.`
- **Objetivo Didático Central:** Explicar a Fase 5 (Disseminação), detalhando a formatação do relatório técnico e executivo direcionado às equipes de infraestrutura e tomada de decisão.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e violação direta da palavra proibida (`acionável` / *actionable*); estilo telegráfico burocrático.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fase 5 — Disseminação` | Subtítulo: `Estruturação do relatório técnico para apoio a decisões de segurança`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Elementos essenciais do relatório de reconhecimento:
      1. *Sumário Executivo:* Visão clara para a diretoria sobre o nível de exposição externa.
      2. *Matriz de Ativos Identificados:* Lista consolidada de domínios, subdomínios, endereços IP e portas abertas.
      3. *Severidade e Risco:* Classificação de prioridades (ex: painel de homologação exposto com autenticação padrão).
      4. *Recomendações Práticas:* Ações corretivas sugeridas (fechamento de portas no firewall, revogação de certificados órfãos, habilitação de 2FA).
    - *(Erradicação do termo banido `acionável`; foco na aplicabilidade do relatório).*
  - *Modelo Mental / Metáfora Funcional:* O laudo do engenheiro civil: não adianta entregar 500 fotos de tijolos; o laudo precisa apontar claramente onde está a trinca na viga e qual o risco de desabamento.
  - *Roteiro e Tom do Apresentador:* "A Fase 5 é a Disseminação. Dados sem um relatório compreensível não têm utilidade. O decisor não quer uma lista desordenada de milhares de certificados; ele precisa de um relatório técnico estruturado que responda: quais ativos estão expostos, qual o risco real para o negócio e o que a equipe de infraestrutura deve fechar primeiro."
- **Fatos Técnicos Preservados:**
  - [x] Fase 5: Disseminação
  - [x] Estrutura do relatório técnico e executivo
  - [x] Eliminação da palavra banida "acionável"

---

### Slide 25 · Ciclo 06: Feedback
- **Cabeçalho:** Slide 25 | Arquivo: `slides/03b-ciclo-osint.html` | Apresentador: Daniel | Título Original: `Feedback: a resposta abre outra pergunta.`
- **Objetivo Didático Central:** Apresentar a Fase 6 (Feedback e Avaliação), demonstrando como cada descoberta técnica gera novos vetores investigativos e retroalimenta o ciclo contínuo de inteligência.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e aforismo circular ("a resposta abre outra pergunta").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Fase 6 — Avaliação e Feedback` | Subtítulo: `Identificação de novas lacunas e reorientação do escopo investigativo`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Retroalimentação do ciclo com os achados do exemplo:
      - O subdomínio `portal.example.com` revelou uma aplicação web de autenticação.
      - Nova pergunta investigativa: *"Quem são os funcionários autorizados a acessar esse portal e quais credenciais corporativas foram expostas em vazamentos históricos?"*
      - O ciclo retorna imediatamente à Fase 1 (Planejar) com foco em pessoas e vazamentos (SOCMINT / credenciais expostas).
  - *Modelo Mental / Metáfora Funcional:* O zoom da câmera: ao focar em um prédio específico, descobrimos uma porta aberta que exige uma nova aproximação com lentes de maior resolução.
  - *Roteiro e Tom do Apresentador:* "Fechamos com a Fase 6: Feedback. A investigação de segurança é dinâmica. Assim que identificamos o `portal.example.com`, surge a próxima pergunta: quem acessa esse portal e qual tecnologia de login ele utiliza? O ciclo se retroalimenta, ajustamos o escopo e iniciamos uma nova rodada de coleta mais direcionada."
- **Fatos Técnicos Preservados:**
  - [x] Fase 6: Avaliação e Feedback
  - [x] Retroalimentação para a Fase 1
  - [x] Conexão com o subdomínio `portal.example.com`
  - [x] Fechamento da maratona do Ciclo OSINT em 6 fases

---
```
================================================================================
ARQUIVO 06 / 12: slides/03c-tecnicas-ferramentas.html
Bloco Temático: Bloco 03 (Parte 3) — Técnicas Passivas & Visão Geral de Ferramentas
Apresentador: Daniel
Slides: 26 a 31
================================================================================
```

### Slide 26 · Visão Geral das Quatro Portas de Entrada
- **Cabeçalho:** Slide 26 | Arquivo: `slides/03c-tecnicas-ferramentas.html` | Apresentador: Daniel | Título Original: `Quatro portas de entrada — nenhuma delas é o alvo`
- **Objetivo Didático Central:** Apresentar a taxonomia das quatro fontes externas essenciais do reconhecimento passivo, orientando o analista sobre qual tipo de dado buscar em cada repositório.
- **Diagnóstico de AI Slop & Engessamento:** Título com travessão rítmico e contraste binário ("nenhuma delas é o alvo"); tautologia mecânica na linha 12 ("Fontes diferentes respondem a perguntas diferentes").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Categorias de Fontes para Reconhecimento Passivo` | Subtítulo: `As quatro vertentes de inteligência em repositórios externos`.
  - *Proposta de Corpo de Texto e Tópicos:*
    1. `Busca e Indexação Web:` Motores de busca gerais e operadores avançados (Dorks) para localização de arquivos expostos.
    2. `DNS e Certificados Digitais:` Resolução de nomes históricos e registros públicos de emissão TLS (Certificate Transparency).
    3. `Registros e Infraestrutura:` Bases cadastrais de domínio (WHOIS), alocação de blocos IP e Sistemas Autônomos (ASN).
    4. `Pessoas e Credenciais Expostas:` Mapeamento de colaboradores, pilhas tecnológicas descritas em vagas e vazamentos corporativos.
  - *Modelo Mental / Metáfora Funcional:* As quatro gavetas do arquivo público: cada gaveta guarda um tipo de documento legal da organização (endereço predial, alvarás, contratos e quadro de sócios).
  - *Roteiro e Tom do Apresentador:* "Para estruturar a coleta passiva sem nos perdermos em centenas de ferramentas isoladas, organizamos as fontes externas em quatro categorias fundamentais: busca web, DNS e certificados, registros de infraestrutura de rede e informações sobre pessoas e credenciais. Veremos agora a lógica técnica de cada uma dessas quatro portas."
- **Fatos Técnicos Preservados:**
  - [x] As 4 categorias de fontes passivas
  - [x] Relação complementar entre fontes
  - [x] Preservação da taxonomia estrutural de OSINT

---

### Slide 27 · Busca e Indexação (Google Dorks)
- **Cabeçalho:** Slide 27 | Arquivo: `slides/03c-tecnicas-ferramentas.html` | Apresentador: Daniel | Título Original: `Busca e indexação: refine a pergunta.`
- **Objetivo Didático Central:** Explicar a técnica de Google Dorking (operadores booleanos e avançados de busca) para localizar arquivos sensíveis, consoles administrativos e diretórios indexados inadvertidamente.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal (*"Busca e indexação: refine a pergunta"*); estilo de comando aforístico.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Busca Avançada e Indexação Web` | Subtítulo: `Filtragem de arquivos sensíveis e painéis de administração via Google Dorks`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Operadores essenciais de busca (Google Hacking Database / GHDB):
      - `site:example.com`: Restringe a busca exclusivamente aos domínios e subdomínios do alvo.
      - `filetype:pdf OR filetype:xls OR filetype:env`: Localiza arquivos de documentos e configurações.
      - `inurl:admin OR inurl:login`: Filtra caminhos de URL associados a painéis de acesso.
      - `intitle:"index of /"`: Descobre listagens abertas de diretórios em servidores web mal configurados.
    - Mecânica técnica: O analista não faz varredura no servidor; consulta a cópia em cache que o robô do Google já rastreou e armazenou em seus datacenters.
  - *Modelo Mental / Metáfora Funcional:* *A lente polarizada do pescador:* A internet é um rio turbulento; usar dorks é colocar óculos polarizados que removem o reflexo da superfície e permitem ver exatamente os arquivos afundados no leito do rio.
  - *Roteiro e Tom do Apresentador:* "A primeira categoria é busca e indexação. Os motores de busca varrem a web continuamente. Com operadores avançados, filtramos esse índice gigantesco: podemos buscar apenas arquivos `.env` ou planilhas dentro de `example.com`, ou localizar páginas com 'index of' no título, que revelam diretórios inteiros sem proteção. Tudo isso consultando os servidores do Google, sem tocar no alvo."
- **Fatos Técnicos Preservados:**
  - [x] Operadores avançados de busca: `site:`, `filetype:`, `inurl:`, `intitle:`
  - [x] Conceito de GHDB (Google Hacking Database)
  - [x] Consulta sobre réplicas em cache de motores de busca

---

### Slide 28 · DNS e Certificados (Tríade CT — Parte 2: Mecânica Sistêmica Global)
- **Cabeçalho:** Slide 28 | Arquivo: `slides/03c-tecnicas-ferramentas.html` | Apresentador: Daniel | Título Original: `DNS e certificados: nomes deixam rastros.`
- **Objetivo Didático Central:** Apresentar a mecânica estrutural e obrigatória dos registros de Certificate Transparency (RFC 6962) e a resolução histórica de DNS como fontes primárias de enumeração de infraestrutura.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e aforismo simplista (*"DNS e certificados: nomes deixam rastros"*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Mapeamento de Nomes: DNS e Certificate Transparency` | Subtítulo: `A obrigatoriedade global de logs públicos para emissão de certificados TLS`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Arquitetura de Certificate Transparency (RFC 6962):
      - Para evitar fraudes e emissões indevidas de certificados SSL/TLS, os navegadores modernos exigem que qualquer Autoridade Certificadora (CA) registre todas as emissões em logs públicos e append-only.
      - Quando a equipe de engenharia do alvo emite um certificado para um novo ambiente (`vpn-homolog.example.com`), o registro é publicado imediatamente em um livro-razão público global auditável por criptografia (Merkle Trees).
    - DNS Passivo:
      - Sensores globais armazenam resoluções antigas de registros A, AAAA, MX e TXT, permitindo mapear migrações de servidores e endereços IP históricos que não constam mais no DNS autoritativo atual.
  - *Modelo Mental / Metáfora Funcional:* *O Diário Oficial do Cartório Web:* Nenhuma empresa pode emitir uma escritura de HTTPS em segredo. Pela lei técnica da web, toda nova emissão precisa sair no Diário Oficial. Se a empresa criar um subdomínio de teste, o mundo inteiro fica sabendo no mesmo instante.
  - *Roteiro e Tom do Apresentador:* "A segunda categoria reúne DNS e certificados digitais. Aqui temos uma das fontes mais valiosas de OSINT: o Certificate Transparency. Pelo padrão RFC 6962, nenhuma Autoridade Certificadora pode emitir um certificado TLS válido sem publicá-lo em logs públicos globais imutáveis. Quando a equipe de infraestrutura cria um subdomínio para testes internos, como `vpn-dev.empresa.com`, esse nome é indexado publicamente. O atacante descobre novos serviços minutos após a emissão do certificado."
- **Fatos Técnicos Preservados:**
  - [x] Segunda aparição funcional de CT: Mecânica sistêmica e arquitetura global
  - [x] Referencial RFC 6962 (Certificate Transparency)
  - [x] Conceito de DNS Passivo (registros A, CNAME, TXT históricos)
  - [x] Merkle Trees e logs append-only

---

### Slide 29 · Registros e Infraestrutura (WHOIS e ASN)
- **Cabeçalho:** Slide 29 | Arquivo: `slides/03c-tecnicas-ferramentas.html` | Apresentador: Daniel | Título Original: `Registros e infraestrutura: conecte as fontes.`
- **Objetivo Didático Central:** Explicar a consulta a registros de infraestrutura de rede, detalhando a função das bases WHOIS e a identificação de Sistemas Autônomos (ASN) para delimitar o perímetro de rede do alvo.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal; contraste binário na linha 97 ("não uma prova automática de propriedade").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Registros de Infraestrutura: WHOIS e Sistemas Autônomos` | Subtítulo: `Mapeamento de blocos IP autoritativos e operadoras através de bases regionais`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Consulta WHOIS e Encadeamento de Infraestrutura:
      - Registro de titularidade de domínios mantido pelos Registros Regionais de Internet (RIRs como Registro.br, ARIN, LACNIC e RIPE) para `example.com`.
      - Identificação dos servidores de nome autoritativos (Nameservers / NS) e blocos de contato administrativo/técnico.
      - Cruzamento com DNS histórico: associação observada anteriormente ao endereço reservado RFC 5737 `192.0.2.10`.
    - Autonomous System Number (ASN):
      - O identificador único de roteamento BGP de uma grande organização ou provedor de nuvem (ex: AS15169 para Google, AS16509 para Amazon AWS).
      - Permite descobrir todos os blocos de endereços IP (prefixos CIDR) oficialmente alocados para a instituição investigada.
  - *Modelo Mental / Metáfora Funcional:* O CEP e a escritura do imóvel: o WHOIS informa quem registrou o loteamento; o ASN é o código postal que revela todos os quarteirões de IPs que pertencem àquela organização.
  - *Roteiro e Tom do Apresentador:* "Na terceira categoria, analisamos registros de infraestrutura. A consulta WHOIS revela quais são os servidores de nome DNS autoritativos da organização. Cruzando com o DNS histórico que apontava para o IP de teste `192.0.2.10`, chegamos ao ASN — Autonomous System Number — que é fundamental para grandes empresas: ele indica quais blocos inteiros de IPs pertencem ao provedor ou ao alvo, permitindo delimitar com precisão o perímetro de rede."
- **Fatos Técnicos Preservados:**
  - [x] Bases cadastrais WHOIS e RIRs (Registro.br, ARIN, LACNIC, RIPE)
  - [x] Associação histórica de DNS ao IP reservado RFC 5737 `192.0.2.10`
  - [x] Conceito de ASN (Autonomous System Number) e roteamento BGP
  - [x] Prefixos de rede CIDR e servidores NS

---

### Slide 30 · Pessoas e Vazamentos
- **Cabeçalho:** Slide 30 | Arquivo: `slides/03c-tecnicas-ferramentas.html` | Apresentador: Daniel | Título Original: `Pessoas e vazamentos: contexto com cuidado.`
- **Objetivo Didático Central:** Discutir a coleta em fontes humanas (SOCMINT) e repositórios de vazamento, abordando a análise de vagas corporativas para descoberta de tecnologias e os limites éticos e legais (LGPD/GDPR).
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal; antítese frouxa na linha 126 ("oferecem contexto, não certezas").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Análise de Fontes Humanas e Credenciais Expostas` | Subtítulo: `Levantamento de tecnologias por vagas corporativas e parâmetros éticos da investigação`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Engenharia reversa via anúncios de emprego:
      - Uma vaga corporativa para "Engenheiro DevOps" listando requisitos como `Kubernetes 1.28`, `AWS EKS`, `PostgreSQL 14` e `Fortinet VPN` entrega o inventário tecnológico da infraestrutura sem necessidade de varredura ativa.
    - Bases de vazamentos e credenciais expostas:
      - Serviços de verificação de violações (como HaveIBeenPwned) indicam se e-mails corporativos foram comprometidos em incidentes anteriores de terceiros.
    - Limites éticos e jurídicos estritos:
      - A investigação de segurança limita-se a identificar se credenciais foram expostas para solicitar a rotação preventiva de senhas; testar as senhas encontradas contra servidores em produção constitui invasão não autorizada.
  - *Modelo Mental / Metáfora Funcional:* O manual de instrução na vitrine de empregos: ao pedir um mecânico especialista em determinada marca de cofre, a empresa revela publicamente qual é o cofre instalado no escritório.
  - *Roteiro e Tom do Apresentador:* "Nossa quarta porta de entrada foca no fator humano. Vagas de emprego no LinkedIn são minas de ouro para o reconhecimento: quando uma empresa pede experiência em versões específicas de bancos de dados ou modelos de firewalls, ela está publicando seu inventário tecnológico. Além disso, bases de vazamentos históricos indicam se credenciais corporativas vazaram no passado, exigindo que a equipe de defesa force a troca de senhas antes que invasores as utilizem."
- **Fatos Técnicos Preservados:**
  - [x] Engenharia reversa de pilhas de tecnologia via vagas de trabalho
  - [x] Consulta a bases de violação de dados (data breaches)
  - [x] Limites éticos e legais (proibição de testes ativos de senhas sem escopo)

---

### Slide 31 · O Kit de Coleta (Tabela Geral de Ferramentas)
- **Cabeçalho:** Slide 31 | Arquivo: `slides/03c-tecnicas-ferramentas.html` | Apresentador: Daniel | Título Original: `O kit de coleta — e o que cada fonte responde`
- **Objetivo Didático Central:** Sintetizar em matriz comparativa as 18 ferramentas e plataformas especializadas de reconhecimento passivo, mapeando cada uma ao seu escopo técnico específico.
- **Diagnóstico de AI Slop & Engessamento:** Título com travessão decorativo (*"O kit de coleta — e o que cada fonte responde"*); antítese simétrica nas notas do orador ("multiplica resultados e multiplica erros").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Matriz de Ferramentas Especializadas em OSINT` | Subtítulo: `Mapeamento de plataformas por categoria técnica e escopo investigativo`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Organização da matriz em 6 escopos de aplicação:
      1. *Serviços e portas indexadas:* Shodan, Censys.
      2. *Registros cadastrais de domínios:* WHOIS, RDAP.
      3. *DNS passivo e reputação histórica:* SecurityTrails, VirusTotal.
      4. *Certificados digitais e subdomínios:* crt.sh, Certificate Search.
      5. *Enumeração automatizada de nomes:* Subfinder, OWASP Amass.
      6. *Extração de metadados em arquivos:* ExifTool, FOCA.
    - Orientação didática: O analista profissional não executa ferramentas às cegas; ele seleciona a ferramenta adequada para cada etapa do ciclo investigativo.
  - *Modelo Mental / Metáfora Funcional:* A caixa de ferramentas do mecânico: você não usa a chave de fenda para soltar a roda do carro; cada ferramenta tem um encaixe exato na peça certa.
  - *Roteiro e Tom do Apresentador:* "Consolidamos aqui o nosso kit de ferramentas em uma matriz técnica. Notem que cada plataforma tem um propósito muito específico: não usamos Shodan para descobrir subdomínios, nem crt.sh para ver tráfego de rede. O analista experiente escolhe a ferramenta certa para cada etapa do ciclo de OSINT. Vamos agora detalhar seis dessas ferramentas essenciais em telas simuladas."
- **Fatos Técnicos Preservados:**
  - [x] Lista das ferramentas de OSINT: Shodan, Censys, WHOIS, SecurityTrails, VirusTotal, crt.sh, Subfinder, OWASP Amass, ExifTool, FOCA
  - [x] Matriz de correspondência entre escopo e utilitário
  - [x] Transição para o bloco de detalhamento prático

---

```
================================================================================
ARQUIVO 07 / 12: slides/03c1-ferramentas-detalhes.html
Bloco Temático: Bloco 03 (Parte 4) — Telas e Fluxos de Ferramentas OSINT
Apresentador: Daniel
Slides: 32 a 37
================================================================================
```

### Slide 32 · Shodan e Censys
- **Cabeçalho:** Slide 32 | Arquivo: `slides/03c1-ferramentas-detalhes.html` | Apresentador: Daniel | Título Original: `Shodan / Censys`
- **Objetivo Didático Central:** Explicar a mecânica de motores de busca de dispositivos conectados (Shodan e Censys), demonstrando a identificação de portas abertas e banners de serviço em endereços IP de documentação.
- **Diagnóstico de AI Slop & Engessamento:** Layout clonado com repetição excessiva de disclaimers burocráticos (*"Cenário fictício"*, *"DADOS FICTÍCIOS"*, *"os registros não confirmam a situação atual"*); ritmo mecânico.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Motores de Busca de Dispositivos Conectados` | Subtítulo: `Consulta a portas e banners de serviço indexados no Shodan e Censys`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Consulta comparativa no endereço de documentação RFC 5737: `192.0.2.10`
    - Resultados extraídos do índice:
      - *Shodan:* Porta 443 aberta executando serviço HTTPS com banner ativo.
      - *Censys:* Associação do certificado digital expedido para `example.com`.
      - *Data da coleta:* Histórico de observação realizado por varreduras globais dos próprios motores.
    - Mecânica técnica: A equipe investigadora realiza uma consulta passiva via API web sem enviar nenhum pacote ao IP investigado; o Shodan é quem realizou a varredura prévia na internet.
  - *Modelo Mental / Metáfora Funcional:* A lista telefônica de portas abertas: os motores de busca percorrem o planeta batendo em todas as portas e publicam o catálogo; você apenas folheia as páginas do catálogo.
  - *Roteiro e Tom do Apresentador:* "Abrimos nosso detalhamento com Shodan e Censys. Essas plataformas são scanners globais contínuos da internet. Quando consultamos o IP `192.0.2.10`, o Shodan nos informa que a porta 443 HTTPS está aberta e o Censys confirma o certificado associado. O nosso computador não disparou nenhum pacote contra o alvo; consultamos o banco de dados mantido pelas plataformas."
- **Fatos Técnicos Preservados:**
  - [x] Ferramentas: Shodan e Censys
  - [x] Endereço IP reservado para documentação RFC 5737: `192.0.2.10`
  - [x] Serviço e porta: HTTPS porta 443
  - [x] Certificado associado a `example.com`

---

### Slide 33 · WHOIS
- **Cabeçalho:** Slide 33 | Arquivo: `slides/03c1-ferramentas-detalhes.html` | Apresentador: Daniel | Título Original: `WHOIS`
- **Objetivo Didático Central:** Demonstrar a extração de dados de registro de domínio através do protocolo WHOIS e discutir o impacto das regulamentações modernas de privacidade (GDPR e LGPD) sobre a visibilidade dos contatos.
- **Diagnóstico de AI Slop & Engessamento:** Caixa burocrática idêntica com disclaimers repetidos; passividade textual na descrição do limite.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Consulta Cadastral de Domínios: WHOIS` | Subtítulo: `Identificação de servidores autoritativos e impacto das leis de privacidade de dados`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Consulta ao domínio institucional: `example.com`
    - Registros obtidos no retorno:
      - *Registrador:* Entidade credenciada pela ICANN responsável pela custódia do domínio.
      - *Servidores de Nome (NS):* `ns1.example.com` (indica onde a zona DNS autoritativa é hospedada).
      - *Contatos administrativos e técnicos:* Exibição de campos mascarados (*Privacy Protect / Dados Protegidos*).
    - Análise técnica: Desde a implementação da GDPR na Europa e da LGPD no Brasil, dados de contato pessoal são ofuscados por padrão, mas a infraestrutura de servidores NS permanece visível para análise de perímetro.
  - *Modelo Mental / Metáfora Funcional:* A certidão de matrícula com dados tarjados: você vê quem é o cartório e onde fica o imóvel, mas o nome do morador vem resguardado por sigilo.
  - *Roteiro e Tom do Apresentador:* "Aqui vemos uma consulta WHOIS para `example.com`. Notem que obtemos o registrador oficial e os servidores de nomes `ns1.example.com`. No entanto, os campos de e-mail e telefone aparecem como 'dados protegidos'. Desde a entrada em vigor da GDPR e da LGPD, os registradores mascaram dados pessoais para evitar abusos, mas a infraestrutura de resolução DNS continua pública."
- **Fatos Técnicos Preservados:**
  - [x] Ferramenta / Protocolo: WHOIS
  - [x] Domínio consultado: `example.com`
  - [x] Servidor de nomes: `ns1.example.com`
  - [x] Contexto legal: GDPR e LGPD sobre dados de contato

---

### Slide 34 · SecurityTrails e VirusTotal
- **Cabeçalho:** Slide 34 | Arquivo: `slides/03c1-ferramentas-detalhes.html` | Apresentador: Daniel | Título Original: `SecurityTrails / VirusTotal`
- **Objetivo Didático Central:** Explicar a importância da investigação de DNS histórico e correlação de ameaças, permitindo rastrear endereços IP que o domínio utilizou no passado e que podem manter portas esquecidas abertas.
- **Diagnóstico de AI Slop & Engessamento:** Disclaimer burocrático repetido na caixa de limite; texto frouxo sobre associações históricas.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Resolução Histórica de DNS e Relações de Infraestrutura` | Subtítulo: `Rastreamento de migrações e servidores legados com SecurityTrails e VirusTotal`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Dados históricos do domínio: `example.com`
    - Retorno das plataformas:
      - *SecurityTrails (DNS Passivo):* Registro apontando que em 2023 o domínio resolvia para o IP `198.51.100.20` (bloco RFC 5737 TEST-NET-2).
      - *VirusTotal:* Relação mapeada com o IP atual `192.0.2.10` e histórico de subdomínios associados.
    - Utilidade ofensiva e defensiva: Muitas empresas migram seus sites principais para a nuvem moderna mas esquecem os servidores antigos ligados no IP anterior (`198.51.100.20`), deixando aplicações vulneráveis ativas sem monitoramento.
  - *Modelo Mental / Metáfora Funcional:* O histórico de endereços de um inquilino: saber onde a pessoa morava antes revela se ela deixou correspondências ou caixas antigas esquecidas no imóvel anterior.
  - *Roteiro e Tom do Apresentador:* "SecurityTrails e VirusTotal oferecem a máquina do tempo da internet: o DNS histórico. Vemos que `example.com` hoje aponta para `192.0.2.10`, mas em 2023 apontava para `198.51.100.20`. Por que isso importa? Porque frequentemente as empresas esquecem o servidor antigo ligado na máquina antiga. Se o analista testar o IP histórico, pode encontrar uma versão antiga da aplicação sem atualizações de segurança."
- **Fatos Técnicos Preservados:**
  - [x] Ferramentas: SecurityTrails e VirusTotal
  - [x] Domínio alvo: `example.com`
  - [x] Endereços IP RFC 5737: `198.51.100.20` (histórico de 2023) e `192.0.2.10` (relação atual)
  - [x] Conceito de DNS passivo e servidores esquecidos (shadow IT)

---

### Slide 35 · crt.sh (Tríade CT — Parte 3: Operação Prática com Wildcards)
- **Cabeçalho:** Slide 35 | Arquivo: `slides/03c1-ferramentas-detalhes.html` | Apresentador: Daniel | Título Original: `crt.sh`
- **Objetivo Didático Central:** Demonstrar a operação prática do buscador web `crt.sh`, ensinando a sintaxe de consulta com operador curinga (`%`) para descoberta automatizada de subdomínios e Subject Alternative Names (SAN).
- **Diagnóstico de AI Slop & Engessamento:** Disclaimer burocrático idêntico; texto com negative listing na caixa de limite ("não prova que está ativo; a cobertura não é absoluta").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Enumeração Prática de Certificados via crt.sh` | Subtítulo: `Descoberta de subdomínios e ambientes de teste com operadores curinga (wildcards)`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Sintaxe da consulta web no motor crt.sh: `%.example.com`
    - Resultados extraídos do log de Certificate Transparency:
      - *Nome Comum (CN):* `example.com`
      - *Subject Alternative Name (SAN):* `teste.example.com`
      - *Fonte pública:* Registro auditável da autoridade certificadora emissora.
    - Aplicação prática do operador `%`: O símbolo de porcentagem atua como curinga SQL, retornando todos os subdomínios registrados de qualquer profundidade (ex: `api.teste.example.com`, `vpn-homolog.example.com`).
  - *Modelo Mental / Metáfora Funcional:* *O Catálogo de Busca Instantânea:* O crt.sh é o motor de pesquisa que indexa o Diário Oficial do SSL; ao digitar `%.empresa.com`, você lista todos os subdomínios que já receberam um certificado HTTPS na história da empresa.
  - *Roteiro e Tom do Apresentador:* "Fechamos a tríade de Certificate Transparency com a ferramenta prática: o `crt.sh`. O site consulta diretamente os logs públicos de CT. Usamos o operador curinga `%.example.com`. A busca nos retorna instantaneamente o subdomínio `teste.example.com` registrado no campo SAN (Subject Alternative Name). Em três segundos, identificamos um ambiente de teste criado pela equipe de TI sem precisar fazer força bruta de nomes no DNS."
- **Fatos Técnicos Preservados:**
  - [x] Terceira aparição funcional de CT: Ferramenta prática `crt.sh`
  - [x] Sintaxe de consulta: `%.example.com` com operador curinga SQL `%`
  - [x] Subdomínio descoberto no campo SAN: `teste.example.com`
  - [x] Domínio raiz: `example.com`

---

### Slide 36 · Subfinder e OWASP Amass
- **Cabeçalho:** Slide 36 | Arquivo: `slides/03c1-ferramentas-detalhes.html` | Apresentador: Daniel | Título Original: `Subfinder / Amass`
- **Objetivo Didático Central:** Explicar o funcionamento de ferramentas de agregação e enumeração de subdomínios em larga escala, alertando sobre a necessidade de configurar modos estritamente passivos para evitar geração de tráfego direto.
- **Diagnóstico de AI Slop & Engessamento:** Alerta defensivo burocrático na caixa de limite; descrição genérica de relacionamentos.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Automação de Enumeração de Subdomínios` | Subtítulo: `Agregação em larga escala com Subfinder e mapeamento de relações com OWASP Amass`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Diferenciação funcional das duas ferramentas de linha de comando:
      - *Subfinder (ProjectDiscovery):* Projetado para velocidade extrema; consulta passivamente mais de 30 fontes públicas (APIs do VirusTotal, Censys, Shodan, crt.sh) e retorna listas desduplicadas de subdomínios (ex: `www.example.com`).
      - *OWASP Amass:* Ferramenta analítica mais densa; além de consultar fontes passivas, constrói grafos de relacionamento entre ASN, blocos CIDR, subdomínios (ex: `teste.example.com`) e IPs.
    - Cuidados operacionais de modo passivo: É obrigatório utilizar a flag `-passive` (Subfinder) e `enum -passive` (Amass) para garantir que módulos de resolução DNS ativa não enviem pacotes aos servidores autoritativos do alvo.
  - *Modelo Mental / Metáfora Funcional:* A rede de arrasto de pescador: em vez de pescar de anzol em cada fonte uma a uma, o Subfinder joga uma rede gigante sobre trinta índices simultaneamente e recolhe tudo de uma só vez.
  - *Roteiro e Tom do Apresentador:* "Quando precisamos automatizar a enumeração em larga escala, utilizamos Subfinder e OWASP Amass. O Subfinder consulta dezenas de APIs públicas em paralelo e retorna uma lista limpa de nomes como `www.example.com`. O Amass vai além: ele cruza esses nomes com os blocos de IP e ASNs da organização. Notem que usamos ambas as ferramentas com as opções de modo passivo ativadas para não emitir consultas ativas aos servidores do alvo."
- **Fatos Técnicos Preservados:**
  - [x] Ferramentas: Subfinder e OWASP Amass
  - [x] Subdomínios agregados no exemplo: `www.example.com` e `teste.example.com`
  - [x] Parâmetros de modo passivo (`-passive`)
  - [x] Construção de grafos de relações via Amass

---

### Slide 37 · ExifTool e FOCA
- **Cabeçalho:** Slide 37 | Arquivo: `slides/03c1-ferramentas-detalhes.html` | Apresentador: Daniel | Título Original: `ExifTool / FOCA`
- **Objetivo Didático Central:** Demonstrar a extração forense de metadados ocultos em documentos públicos (PDFs, planilhas e fotos), identificando softwares utilizados, nomes de usuários e caminhos de rede internos.
- **Diagnóstico de AI Slop & Engessamento:** Disclaimer burocrático na caixa de cautela; passividade textual ("Quais metadados podem aparecer em arquivos já obtidos?").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Extração Forense de Metadados em Arquivos` | Subtítulo: `Identificação de autores, versões de software e caminhos internos com ExifTool e FOCA`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Análise do documento baixado de repositório público: `relatorio.pdf`
    - Metadados técnicos revelados na simulação:
      - *ExifTool:* Campo `Author: Equipe Exemplo`, Data de criação e Sistema Operacional.
      - *FOCA (Fingerprinting Organizations with Collected Archives):* Campo `Software: Editor de PDF v2.4`, caminho de rede local (`\\servidor-interno\arquivos\`) e impressora utilizada.
    - Impacto para a segurança ofensiva: Metadados expõem a versão exata do software de criação do documento (potencialmente vulnerável) e o padrão de nomes de usuário corporativos que alimenta campanhas de spear-phishing.
  - *Modelo Mental / Metáfora Funcional:* A poeira nas solas dos sapatos: o documento parece apenas um relatório em PDF limpo, mas carrega nas suas propriedades a poeira de onde foi gerado (o nome do autor, a impressora e a máquina local).
  - *Roteiro e Tom do Apresentador:* "Fechamos os detalhes de ferramentas com a extração de metadados. Quando uma empresa publica um relatório em PDF ou uma planilha no site, esses arquivos frequentemente contêm metadados invisíveis a olho nu. Executando o ExifTool e a FOCA no arquivo `relatorio.pdf`, descobrimos o nome de usuário do autor, o software usado para salvar o PDF e caminhos de pastas internas da rede. Esses dados alimentam a engenharia social que o Emilio demonstrou anteriormente."
- **Fatos Técnicos Preservados:**
  - [x] Ferramentas: ExifTool e FOCA
  - [x] Arquivo inspecionado: `relatorio.pdf`
  - [x] Metadados extraídos: Autor (Equipe Exemplo), Software (Editor de PDF), caminhos locais
  - [x] Conexão causal com engenharia social

---

```
================================================================================
ARQUIVO 08 / 12: slides/03d-fisico-ecossistema.html
Bloco Temático: Bloco 03 (Parte 5) — Reconhecimento Físico & Disciplinas INT
Apresentador: Daniel
Slides: 38 a 40
================================================================================
```

### Slide 38 · Dumpster Diving
- **Cabeçalho:** Slide 38 | Arquivo: `slides/03d-fisico-ecossistema.html` | Apresentador: Daniel | Título Original: `Dumpster diving: quando o descarte vira pista`
- **Objetivo Didático Central:** Apresentar a técnica de coleta em descarte físico (Dumpster Diving), destacando os riscos do descarte inadequado de impressos corporativos e as exigências estritas das regras de engajamento (RoE).
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal; contraste aforístico na linha 31 ("O lixo de uma organização conta a história que o site institucional não conta"); antítese com travessão ("no escopo — não no improviso").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Reconhecimento Físico: Descarte de Materiais e Mídias` | Subtítulo: `Vetores de exposição predial e limites legais das Regras de Engajamento (RoE)`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Mecânica do Dumpster Diving:
      - Coleta sistemática de papéis, notas fiscais, manuais internos e mídias óticas descartadas em lixeiras externas de escritórios sem trituração adequada.
    - Vetores revelados no lixo corporativo:
      1. Organogramas e ramais telefônicos de funcionários.
      2. Senhas provisórias anotadas em post-its.
      3. Notas fiscais revelando fornecedores de tecnologia e prestadores de serviço terceirizados.
    - Princípio legal: Em testes de invasão autorizados, a coleta em lixo deve constar expressamente nas Regras de Engajamento (Rules of Engagement / RoE); a coleta em propriedade privada sem permissão expressa constitui ilícito civil e penal.
  - *Modelo Mental / Metáfora Funcional:* A trituradora de papel como firewall físico: jogar documentos inteiros na lixeira da calçada é equivalente a desativar o firewall do servidor e deixar o tráfego aberto.
  - *Roteiro e Tom do Apresentador:* "Fazemos agora uma quebra importante: a segurança não acontece apenas no teclado. O Dumpster Diving é o reconhecimento físico através do lixo corporativo. Documentos impressos jogados fora sem trituração revelam notas fiscais de fornecedores, nomes de gerentes e até senhas anotadas em papéis. Mas atenção ao rigor ético: em um teste de invasão profissional, qualquer coleta física precisa estar explicitamente autorizada nas Regras de Engajamento assinadas pela diretoria."
- **Fatos Técnicos Preservados:**
  - [x] Técnica: Dumpster Diving (reconhecimento físico de descarte)
  - [x] Conceito de Regras de Engajamento (Rules of Engagement / RoE)
  - [x] Tipos de materiais descartados (documentos, mídias, notas fiscais)

---

### Slide 39 · Shoulder Surfing
- **Cabeçalho:** Slide 39 | Arquivo: `slides/03d-fisico-ecossistema.html` | Apresentador: Daniel | Título Original: `Shoulder surfing: informação à vista.`
- **Objetivo Didático Central:** Discutir a observação visual direta de telas e rotinas de digitação (Shoulder Surfing) em locais públicos e ambientes corporativos, apresentando as contramedidas técnicas de mitigação.
- **Diagnóstico de AI Slop & Engessamento:** Título com colon reveal e trocadilho rimado ("Shoulder surfing: informação à vista.").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Reconhecimento Visual Direto (Shoulder Surfing)` | Subtítulo: `Observação física de telas, credenciais e contramedidas de privacidade`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Dinâmica da observação visual:
      - Acompanhamento da digitação de senhas, códigos de autenticação (2FA) e telas de sistemas corporativos por cima dos ombros do usuário em aeroportos, cafés, transportes e saguões de empresas.
    - Fatores de amplificação modernos:
      - Câmeras de smartphones de altíssima resolução e lentes teleobjetivas capazes de gravar telas a vários metros de distância.
    - Contramedidas físicas diretas:
      1. Aplicação de películas micropolarizadas de privacidade em telas de notebooks.
      2. Gestão de telas voltadas para paredes em áreas de circulação.
      3. Ocultação de caracteres em interfaces de autenticação.
  - *Modelo Mental / Metáfora Funcional:* A mão cobrindo o teclado do caixa eletrônico: um reflexo simples de proteção física que impede o transeunte atrás da faixa amarela de ler os dígitos da sua senha.
  - *Roteiro e Tom do Apresentador:* "Complementando o reconhecimento físico, temos o Shoulder Surfing: a simples observação da tela ou do teclado por quem está ao redor. Em transportes públicos ou aeroportos, pessoas abrem planilhas financeiras ou digitam senhas corporativas com a tela totalmente exposta. Hoje, com câmeras de celular de alta definição, um observador a metros de distância grava a digitação da senha. A contramedida técnica é simples: películas polarizadas de privacidade e atenção constante ao ambiente."
- **Fatos Técnicos Preservados:**
  - [x] Técnica: Shoulder Surfing (observação visual física)
  - [x] Locais de risco: cafés, aeroportos, áreas de trânsito público
  - [x] Contramedidas: Películas de privacidade e ocultação de digitação

---

### Slide 40 · O Ecossistema de Inteligência (9 Disciplinas INT)
- **Cabeçalho:** Slide 40 | Arquivo: `slides/03d-fisico-ecossistema.html` | Apresentador: Daniel | Título Original: `OSINT é uma peça. O tabuleiro é maior.`
- **Objetivo Didático Central:** Apresentar a taxonomia militar das 9 disciplinas de inteligência (INTs), destacando como a OSINT se integra a campos complementares como HUMINT, GEOINT e SOCMINT.
- **Diagnóstico de AI Slop & Engessamento:** Metáfora clichê de xadrez corporativo no título ("OSINT é uma peça. O tabuleiro é maior."); presença de palavra banida (`ecossistema` na linha 143); sobrecarga cognitiva na apresentação de 9 siglas simultâneas.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Disciplinas Complementares de Inteligência (INTs)` | Subtítulo: `A correlação entre OSINT e as especialidades de inteligência estratégica`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Quadro das 9 disciplinas formalizadas de coleta de inteligência:
      - `OSINT (Open Source Intelligence):` Fontes abertas e dados públicos acessíveis.
      - `HUMINT (Human Intelligence):` Fontes humanas, informantes e engenharia social.
      - `GEOINT (Geospatial Intelligence):` Imagens de satélite, dados de terreno e geolocalização.
      - `SOCMINT (Social Media Intelligence):` Perfis, conexões e tendências em redes sociais.
      - `CYBINT/DNINT (Cyber Intelligence):` Análise de malware, infraestrutura de comando e tráfego de rede.
      - `SIGINT (Signals Intelligence):` Interceptação de comunicações de rádio e sinais eletromagnéticos.
      - `ELINT (Electronic Intelligence):` Telemetria e emissões de radares e sensores eletrônicos.
      - `IMINT (Imagery Intelligence):` Sensores fotográficos aéreos e espaciais.
      - `TECHINT (Technical Intelligence):` Avaliação de equipamentos bélicos e capacidades técnicas do adversário.
      - `FININT (Financial Intelligence):` Rastreamento de transações bancárias, empresas de fachada e fluxos de capitais.
    - Orientação de apresentação: Não ler as nove siglas exaustivamente; enfatizar as quatro que conectam os blocos do seminário (OSINT, HUMINT, GEOINT e SOCMINT).
  - *Modelo Mental / Metáfora Funcional:* Os sentidos humanos: o olho (GEOINT), o ouvido (SIGINT), a conversa com vizinhos (HUMINT) e a leitura dos jornais (OSINT). O cérebro precisa de todos os sentidos combinados para entender a realidade.
  - *Roteiro e Tom do Apresentador:* "Para fechar o Bloco 03, enquadramos a OSINT no panorama maior das disciplinas formais de inteligência conhecidas pelas siglas INT. A OSINT é uma disciplina fundamental porque seu custo de coleta é baixo e sua legalidade é ampla. Mas ela se cruza com outras: conecta-se à HUMINT através do phishing e da engenharia social que o Emilio mostrou, à SOCMINT através do post da Marina no Bloco 1, e à GEOINT, que é a inteligência geográfica que o João Pedro Almeida demonstrará logo mais. Passo agora a palavra ao João Pedro Gonçalves para apresentar os grandes estudos de caso históricos."
- **Fatos Técnicos Preservados:**
  - [x] As 9 disciplinas INT completas: HUMINT, GEOINT, FININT, ELINT, IMINT, TECHINT, CYBINT, SOCMINT, SIGINT
  - [x] Definições e campos de atuação de cada especialidade
  - [x] Eliminação da palavra banida "ecossistema"
  - [x] Conexão e transição formal para o Bloco 04 (João Pedro Gonçalves)

---
```
================================================================================
ARQUIVO 09 / 12: slides/04-estudos-caso.html
Bloco Temático: Bloco 04 — Estudos de Caso Históricos (RSA & Strava)
Apresentador: João Pedro Gonçalves
Slides: 41 a 44
================================================================================
```

### Slide 41 · Divisor do Bloco 04
- **Cabeçalho:** Slide 41 | Arquivo: `slides/04-estudos-caso.html` | Apresentador: João Pedro Gonçalves | Título Original: `Quando o reconhecimento vira manchete.`
- **Objetivo Didático Central:** Abrir o Bloco 04 de estudos de caso reais de repercussão global, demonstrando que os maiores incidentes de cibersegurança da história moderna não começaram com exploração direta de zero-days, mas com reconhecimento metodológico e correlação de dados públicos.
- **Diagnóstico de AI Slop & Engessamento:** Título melodramático e fragmentado com negative listing (*"Quando o reconhecimento vira manchete / Dois casos reais. Nenhum deles começou com um exploit zero-day."*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Estudos de Caso Reais em Reconhecimento` | Subtítulo: `A mecânica técnica por trás dos incidentes RSA SecurID e Strava Heatmap`.
  - *Proposta de Corpo de Texto e Tópicos:* `Bloco 04 · João Pedro Gonçalves`. Introdução temática: "Apresentamos dois marcos históricos da segurança da informação que comprovam como o levantamento prévio de informações sobre pessoas e rotinas viabiliza o comprometimento de organizações tidas como inexpugnáveis."
  - *Modelo Mental / Metáfora Funcional:* A autópsia do incidente: examinar a caixa-preta de dois acidentes aéreos célebres para entender a sequência exata de pequenas falhas humanas e técnicas que derrubaram o avião.
  - *Roteiro e Tom do Apresentador:* "Obrigado, Daniel. Entramos no Bloco 04 para examinar como a teoria e as ferramentas que vimos até aqui operaram em dois dos casos mais emblemáticos da história da segurança mundial. Vamos analisar a invasão histórica da RSA SecurID em 2011 e o vazamento de instalações militares secretas pelo mapa de calor do Strava em 2018. Em ambos os casos, a falha crítica ocorreu na fase de reconhecimento."
- **Fatos Técnicos Preservados:**
  - [x] Numeração do Bloco: 04
  - [x] Apresentador responsável: João Pedro Gonçalves
  - [x] Casos abordados: RSA SecurID (2011) e Strava (2018)

---

### Slide 42 · Caso RSA SecurID (2011)
- **Cabeçalho:** Slide 42 | Arquivo: `slides/04-estudos-caso.html` | Apresentador: João Pedro Gonçalves | Título Original: `O e-mail que abriu a RSA`
- **Objetivo Didático Central:** Detalhar a anatomia do ataque contra a RSA Security em março de 2011, explicando como o spear-phishing direcionado a colaboradores de RH permitiu a execução de um exploit de Adobe Flash encapsulado em Excel, culminando no comprometimento de sementes criptográficas de tokens SecurID em escala global.
- **Diagnóstico de AI Slop & Engessamento:** Título de romance policial ("O e-mail que abriu a RSA"); contraste binário forçado na linha 62 (*"O vetor não foi técnico: foi humano"*); aforismo de efeito na lição (*"basta descobrir quem abre anexos"*); **Anacronismo factual grave na linha 75** (anexo nomeado `2021_Recruitment_Plan.xlsx` em um caso ocorrido em março de 2011).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Caso RSA SecurID (Março de 2011)` | Subtítulo: `Spear-phishing corporativo e comprometimento de sementes criptográficas de autenticação`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Cronologia técnica do incidente:
      1. *Março de 2011:* Reconhecimento prévio identifica funcionários de recrutamento e recursos humanos da RSA Security.
      2. *Vetor de entrada:* Envio de dois e-mails de spear-phishing contendo o anexo `2011_Recruitment_Plan.xls` (correção do anacronismo original).
      3. *Exploração:* Abertura por um colaborador; execução de código via vulnerabilidade não corrigida no Adobe Flash Player embutido na planilha Excel (CVE-2011-0609).
      4. *Movimento lateral:* Estabelecimento de backdoor Poison Ivy, elevação de privilégios e exfiltração de dados sensíveis sobre os algoritmos e sementes (seeds) dos tokens de duplo fator RSA SecurID.
      5. *Consequência global:* A RSA investiu dezenas de milhões de dólares para substituir cerca de 40 milhões de tokens de clientes corporativos em todo o mundo.
    - Análise de Reconhecimento: Os invasores não dispararam varreduras ruidosas contra os firewalls da RSA; mapearam previamente no LinkedIn os funcionários juniores do RH que recebiam currículos diariamente por dever de ofício.
  - *Modelo Mental / Metáfora Funcional:* A carta endereçada ao carteiro: o atacante não tentou enganar os engenheiros de criptografia do núcleo da empresa; ele enviou uma proposta de currículo para a equipe de recrutamento, cuja função diária é justamente abrir anexos de desconhecidos.
  - *Roteiro e Tom do Apresentador:* "Vejam a gravidade deste caso ocorrido em março de 2011. A RSA Security era a referência mundial em autenticação forte com seus tokens SecurID. Os atacantes queriam as sementes criptográficas desses tokens. Como entraram? Não foi explorando o firewall principal. Fizeram reconhecimento de RH e enviaram um e-mail com o anexo `2011_Recruitment_Plan.xls` para quatro colaboradores de recrutamento. Um funcionário abriu a planilha, um exploit de Flash executou código em segundo plano e os invasores ganharam acesso lateral à rede interna, forçando a substituição de 40 milhões de tokens no mercado."
- **Fatos Técnicos Preservados:**
  - [x] Nome do caso: RSA SecurID
  - [x] Data histórica exata: Março de 2011
  - [x] Correção do anacronismo: Anexo corrigido para `2011_Recruitment_Plan.xls` (ou `.xlsx` alinhado ao ano de 2011)
  - [x] Vulnerabilidade subjacente: Exploit de Flash embutido em planilha Excel
  - [x] Impacto: Movimento lateral e comprometimento de tokens SecurID
  - [x] Fonte referenciada: Zoho Workplace / relatórios públicos de segurança do incidente

---

### Slide 43 · Caso Strava Global Heatmap (2018)
- **Cabeçalho:** Slide 43 | Arquivo: `slides/04-estudos-caso.html` | Apresentador: João Pedro Gonçalves | Título Original: `O mapa que desenhou bases secretas.`
- **Objetivo Didático Central:** Analisar o incidente do mapa de calor global do Strava (2018), demonstrando o conceito pedagógico nobre de inteligência emergente por agregação de dados públicos e autorizados.
- **Diagnóstico de AI Slop & Engessamento:** Título melodramático; fragmentação em estilo slogan publicitário na linha 113 (*"01 Ninguém invadiu nada. O dado era público e autorizado. Só não deveria revelar tanto."*); falsa equação de efeito na linha 121 (*"Correlação vence senha. Heatmap + satélite + geografia = localização provável."*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Caso Strava Global Heatmap (2017–2018)` | Subtítulo: `Descoberta de instalações militares sigilosas por agregação de telemetria esportiva`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Fatos técnicos do incidente:
      - Em novembro de 2017, o aplicativo esportivo Strava publicou uma versão atualizada do seu mapa de calor global (Global Heatmap), consolidando mais de **3 trilhões de pontos de GPS** e **13 bilhões de quilômetros** de atividades físicas de usuários em todo o mundo.
      - Em janeiro de 2018, o analista australiano Nathan Ruser identificou que, em regiões desérticas e zonas de conflito no Afeganistão (como as coordenadas `34.5°N 69.2°E`), Síria e Somália (onde o uso de smartphones pela população local era quase nulo), surgiam traçados luminosos nítidos de pistas de corrida em formato retangular e circular.
    - Mecânica investigativa de correlação:
      1. *Sinal primário:* Traçados concêntricos de exercícios ao ar livre no deserto.
      2. *Cruzamento:* Sobreposição com imagens ópticas de satélite (Google Earth / Sentinel).
      3. *Resultado:* Mapeamento exato das guaritas, perímetros fortificados, pistas de pouso e rotas de patrulha de bases militares avançadas (como a base militar no Afeganistão em `34.5°N 69.2°E`) e postos operacionais sigilosos.
    - Ausência de ataque cibernético: Nenhum soldado violou ordens de sigilo voluntariamente e os servidores do Strava não sofreram invasão; a vulnerabilidade decorreu exclusivamente da agregação de dados públicos de telemetria com configurações padrão de privacidade desprotegidas.
  - *Modelo Mental / Metáfora Funcional:* *A trilha de formigas no jardim:* Uma formiga correndo individualmente pelo quintal é invisível ao olho humano. Dez mil formigas marchando repetidamente pelo mesmo percurso abrem uma vala nítida na grama perceptível até por satélite.
  - *Roteiro e Tom do Apresentador:* "O caso Strava de 2018 ilustra o que chamamos em inteligência de vulnerabilidade por agregação de dados. O Strava publicou um mapa de calor agregando 3 trilhões de pontos de GPS de atletas. Um estudante de 20 anos, Nathan Ruser, olhou para o mapa em zonas de guerra como Afeganistão e Síria. Enquanto as cidades tinham manchas difusas, no meio do deserto surgiam desenhos perfeitamente geométricos de pistas de corrida — como na base do Afeganistão em 34.5°N 69.2°E. Eram soldados ocidentais correndo ao redor de suas bases secretas com relógios inteligentes. A sobreposição com fotos de satélite revelou a localização exata das instalações militares sem que ninguém tivesse invadido o sistema."
- **Fatos Técnicos Preservados:**
  - [x] Nome do caso: Strava Global Heatmap
  - [x] Período: Novembro de 2017 (lançamento) a Janeiro de 2018 (revelação)
  - [x] Analista responsável: Nathan Ruser
  - [x] Locais citados: Afeganistão, Síria, Somália e bases de patrulha
  - [x] Coordenadas geográficas exatas da base no Afeganistão: 34.5°N 69.2°E
  - [x] Métricas do mapa: 3 trilhões de pontos GPS, 13 bilhões de km
  - [x] Princípio técnico de inteligência emergente por agregação

---

### Slide 44 · Lições Compartilhadas dos Casos
- **Cabeçalho:** Slide 44 | Arquivo: `slides/04-estudos-caso.html` | Apresentador: João Pedro Gonçalves | Título Original: `O dado mais perigoso é aquele que parece inofensivo.`
- **Objetivo Didático Central:** Sintetizar os aprendizados técnicos compartilhados entre os casos RSA e Strava, fixando o princípio fundamental de que o valor do reconhecimento reside na correlação analítica entre fontes distintas e preparando o terreno para as demonstrações práticas.
- **Diagnóstico de AI Slop & Engessamento:** Frase de efeito de encerramento em estilo mic-drop (*"O dado mais perigoso é aquele que parece inofensivo"*); duplo contraste binário empilhado na linha 210 (*"Reconhecimento é correlação, não coleta. O valor não está na fonte isolada — está no que ela revela..."*); **direção teatral artificial na linha 217** (*"Pausa dramática: deixar a frase no telão por alguns segundos"*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Síntese dos Estudos de Caso` | Subtítulo: `A correlação de dados como gerador de inteligência ofensiva`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Quadro comparativo dos fatores determinantes:
      - *No caso RSA (2011):* O dado isolado era a lista pública de nomes de funcionários de RH no LinkedIn. A correlação com o formato de e-mail corporativo viabilizou o spear-phishing que bypassou as defesas perimetrais.
      - *No caso Strava (2018):* O dado isolado era a rota individual de corrida de um usuário com smartwatch. A correlação com mapas de satélite mapeou o perímetro físico de bases militares sigilosas.
    - Princípio metodológico: A inteligência de reconhecimento decorre da correlação entre dados fragmentados coletados em fontes independentes.
    - *(Eliminação da instrução de "pausa dramática"; substituição por gancho lógico e direto para o próximo bloco).*
  - *Modelo Mental / Metáfora Funcional:* A montagem das peças: ter uma lista de nomes ou um mapa de satélite é como ter pedaços avulsos de metal; ao soldá-los na ordem certa, o analista constrói a chave que abre a porta.
  - *Roteiro e Tom do Apresentador:* "Sintetizando esses dois casos históricos: no incidente da RSA, o dado inicial foi uma lista pública de funcionários de RH no LinkedIn; no Strava, foram rotas públicas de exercícios. Isoladamente, nenhum desses dados parecia perigoso. O poder do reconhecimento está na capacidade do analista de correlacionar esses pontos com outras fontes. É exatamente essa metodologia prática que o João Pedro Almeida demonstrará agora no Bloco 05."
- **Fatos Técnicos Preservados:**
  - [x] Princípio técnico da correlação multivariada
  - [x] Síntese integrada dos casos RSA e Strava
  - [x] Eliminação da rubrica teatral "pausa dramática"
  - [x] Gancho de transição para o apresentador João Pedro Almeida

---

```
================================================================================
ARQUIVO 10 / 12: slides/05-geosint-osint.html
Bloco Temático: Bloco 05 — Demonstrações Práticas (GEOSINT & Grafo OSINT)
Apresentador: João Pedro Almeida
Slides: 45 a 48
================================================================================
```

### Slide 45 · Divisor do Bloco 05
- **Cabeçalho:** Slide 45 | Arquivo: `slides/05-geosint-osint.html` | Apresentador: João Pedro Almeida | Título Original: `Do dado público ao alvo provável.`
- **Objetivo Didático Central:** Abrir o Bloco 05 introduzindo as demonstrações práticas baseadas no rigor do método científico: dedução geográfica a partir de evidências observáveis em imagens (GEOSINT) e correlação relacional em grafo.
- **Diagnóstico de AI Slop & Engessamento:** Título com formulação simétrica de efeito ("Do dado público ao alvo provável.").
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Demonstrações Práticas de Reconhecimento` | Subtítulo: `Aplicação de técnicas de GEOSINT e correlação de entidades em grafo`.
  - *Proposta de Corpo de Texto e Tópicos:* `Bloco 05 · João Pedro Almeida`. Escopo operacional: "Neste bloco, aplicamos o método dedutivo a dois cenários reais de investigação: primeiro, determinamos a localização geográfica de uma fotografia com base em sombras solares e relevo; em seguida, fechamos o fio narrativo da Acme Pagamentos construindo um grafo de correlação relacional."
  - *Modelo Mental / Metáfora Funcional:* A reconstituição da cena: o perito chega ao local, analisa os indícios materiais deixados e reconstrói o que aconteceu passo a passo com evidências reprodutíveis.
  - *Roteiro e Tom do Apresentador:* "Obrigado, João Pedro. Assumo a condução do Bloco 05 para mostrar a prática em ação. Nós dividimos este bloco em duas partes: nas duas primeiras telas, realizaremos um exercício de inteligência geoespacial (GEOSINT) a partir de uma fotografia de estrada, calculando o horário e a orientação do sol. Na tela seguinte, fecharemos a narrativa da Acme Pagamentos demonstrando como uma investigação de OSINT estrutura um grafo relacional completo."
- **Fatos Técnicos Preservados:**
  - [x] Numeração do Bloco: 05
  - [x] Apresentador responsável: João Pedro Almeida
  - [x] Escopo das duas demonstrações: GEOSINT e Grafo OSINT

---

### Slide 46 · Demonstração GEOSINT 1 (A Foto da Ruta 40)
- **Cabeçalho:** Slide 46 | Arquivo: `slides/05-geosint-osint.html` | Apresentador: João Pedro Almeida | Título Original: `Onde foi tirada esta foto?`
- **Objetivo Didático Central:** Ensinar a metodologia de decomposição de pistas biogeográficas e análise astronômica/solar em uma fotografia de estrada para delimitação de região geográfica e validação instrumental.
- **Diagnóstico de AI Slop & Engessamento:** Contraste binário com travessão na linha 119 (*"Montanhas baixas, solo seco, vegetação rasteira — não é litoral."*); chip de interface com antítese simplista na linha 137 (*"confiança, não certeza"*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Investigação Geoespacial (GEOSINT): Análise de Evidências Visuais` | Subtítulo: `Extração de pistas ambientais, relevo e azimute solar na fotografia`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Fotografia sob investigação: Imagem de rodovia asfaltada sem marcações visíveis de GPS nos metadados EXIF.
    - Pistas técnicas extraídas metodologicamente e ferramentas combinadas:
      1. *Bioma e Relevo:* Cordilheira árida ao fundo, solo seco e vegetação rasteira espinhosa. Características indicativas da estepe pré-cordilheirana da América do Sul.
      2. *Indício Viário e Busca Reversa (Google Lens e Mapillary):* Placa de quilometragem e sinalização vertical com padrão de formato e cores da Argentina (Ruta Nacional 40 / Província de Mendoza), identificadas por busca visual com **Google Lens** e validadas por sequências de fotos de rua no **Mapillary**.
      3. *Análise Solar (SunCalc):* As sombras dos postes e árvores projetam-se alongadas para a esquerda (leste), indicando que o sol estava posicionado baixo no horizonte à direita (oeste), característico do final de tarde em rodovia com orientação norte-sul.
      4. *Cruzamento Espacial e Viário (Overpass):* Consultas estruturadas no **Overpass** para correlacionar segmentos de rodovias federais e orientações viárias na região andina.
    - Hipótese validada: **Mendoza, Argentina · 32.89°S 68.84°W**.
    - Nível de inferência: Estimativa probabilística calculada em **78% de confiança**, integrando o conjunto instrumental de **SunCalc**, **Google Lens**, **Mapillary** e **Overpass**.
  - *Modelo Mental / Metáfora Funcional:* A bússola natural: o sol e as sombras na fotografia funcionam exatamente como uma bússola e um relógio gravados no asfalto.
  - *Roteiro e Tom do Apresentador:* "Vejam esta foto. Suponham que ela foi publicada em uma rede social sem coordenadas de GPS. O analista de GEOSINT analisa pistas em camadas: primeiro, o bioma pré-cordilheirano e a placa rodoviária identificados com apoio de Google Lens e Mapillary apontam para a Argentina. Segundo, medimos com o SunCalc o comprimento e o azimute das sombras para determinar que era fim de tarde em uma rodovia norte-sul. Terceiro, via Overpass filtramos o traçado viário compatível. Com isso, validamos a hipótese na Ruta 40 em Mendoza, Argentina, nas coordenadas 32.89°S 68.84°W com 78% de confiança."
- **Fatos Técnicos Preservados:**
  - [x] Caso e local: Ruta 40, Mendoza, Argentina nas coordenadas exatas `32.89°S 68.84°W`
  - [x] Ferramentas instrumentais integradas: SunCalc, Google Lens, Mapillary e Overpass
  - [x] Pistas físicas: Sombras solares projetadas para leste, relevo árido pré-cordilheirano, placa de estrada
  - [x] Métrica de confiança probabilística: 78%

---

### Slide 47 · Demonstração GEOSINT 2 (Eliminação de Hipóteses)
- **Cabeçalho:** Slide 47 | Arquivo: `slides/05-geosint-osint.html` | Apresentador: João Pedro Almeida | Título Original: `Três hipóteses. Uma coordenada.`
- **Objetivo Didático Central:** Demonstrar o processo científico de descarte e validação sucessiva de hipóteses geográficas, comparando imagens de satélite e dados topográficos para chegar à coordenada exata da fotografia.
- **Diagnóstico de AI Slop & Engessamento:** Título com fragmentação dramática em números (`Três hipóteses. Uma coordenada.`); antíteses consecutivas no subtítulo e texto (*"Eliminar, não adivinhar"* e *"O que sobra não é certeza: é o próximo teste"*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Validação de Coordenadas e Descarte de Hipóteses` | Subtítulo: `Aplicação do método de eliminação baseado em azimute solar e dados topográficos`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Formulação de 3 hipóteses candidatas ao longo da Ruta 40:
      - *Hipótese A (Trecho Sul · Santa Cruz):* Descartada. A orientação da rodovia naquele segmento segue o sentido leste-oeste, o que geraria sombras em ângulo incompatível com a fotografia.
      - *Hipótese B (Trecho Norte · San Juan):* Descartada. O relevo montanhoso apresenta altitude e perfil de encosta divergentes das medições topográficas.
      - *Hipótese C (Mendoza Central · Km 3.210):* Validada. Coincidência total de traçado viário, curva de nível das colinas ao fundo e posição do acostamento visível em imagens orbitais de alta resolução (Google Earth / Overpass Turbo).
    - Conclusão do método: O analista não precisa adivinhar; ele elimina inconsistências físicas e matemáticas até restar a única coordenada compatível com as leis da ótica e da geografia.
  - *Modelo Mental / Metáfora Funcional:* O funil de eliminação: você despeja dez possibilidades no topo do funil; as leis da física e da geometria barram as hipóteses erradas e apenas a coordenada verdadeira passa pelo estreito do funil.
  - *Roteiro e Tom do Apresentador:* "Nesta segunda tela, vemos como o analista valida o resultado. Não se trata de dar palpites. Formulamos três hipóteses de trechos ao longo da rodovia. A Hipótese A foi descartada porque a orientação da estrada é incompatível com o azimute solar calculado no SunCalc. A Hipótese B foi descartada pelo perfil das montanhas. A Hipótese C, no quilômetro 3.210 em Mendoza, confirmou 100% dos elementos visuais: a curva do asfalto, o alinhamento das colinas e a projeção exata das sombras."
- **Fatos Técnicos Preservados:**
  - [x] As três hipóteses formuladas (A, B e C)
  - [x] Critérios de descarte: azimute solar incompatível e perfil topográfico divergente
  - [x] Coordenada final validada: Trecho de Mendoza na Ruta 40
  - [x] Ferramentas de validação: SunCalc e Overpass Turbo

---

### Slide 48 · Demonstração OSINT 3 (Construção do Grafo de Correlação)
- **Cabeçalho:** Slide 48 | Arquivo: `slides/05-geosint-osint.html` | Apresentador: João Pedro Almeida | Título Original: `Vinte minutos de coleta. Um grafo.`
- **Objetivo Didático Central:** Demonstrar a construção de um grafo relacional conectando nós de dados públicos e fechar de forma magistral o fio condutor da personagem Marina Sousa e da Acme Pagamentos (Slides 06 e 15), reforçando os limites éticos do engajamento.
- **Diagnóstico de AI Slop & Engessamento:** Título fragmentado ("Vinte minutos de coleta. Um grafo."); sequência telegráfica robótica com quádrupla negação defensiva na linha 293 (*"Não testamos a senha vazada. Não acessamos a VPN. Não enviamos nada ao alvo. Sem autorização, o grafo para aqui."*); contraste binário na linha 297.
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Construção do Grafo de Correlação OSINT` | Subtítulo: `Encadeamento relacional de fontes abertas sobre a analista Marina Sousa e Acme Pagamentos`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Estrutura dos nós e arestas no grafo relacional:
      1. *Nó 1 (Identificador Social):* `@marina.souza` (originado da postagem do Slide 06).
      2. *Nó 2 (E-mail Corporativo):* `marina@acme.com` (deduzido a partir do padrão de nomenclatura e buscas públicas).
      3. *Nó 3 (Bases de Vazamentos):* O e-mail consta em dois vazamentos históricos de bases de credenciais de terceiros.
      4. *Nó 4 (Domínio Institucional):* `acme.com` (revelando subdomínios de borda).
      5. *Nó 5 (Serviço Crítico):* Painel de VPN de borda exposto diretamente na internet.
      6. *Nó 6 (Privilégio do Alvo):* Cargo no departamento financeiro com alçada de aprovação de pagamentos (obtido via LinkedIn).
    - Princípio de Conformidade Ética e Limites de Engajamento:
      - O levantamento restringe-se estritamente à estruturação do grafo de relações públicas.
      - Testes de credenciais contra a VPN ou tentativas de login direto dependem de contrato formal de autorização (Rules of Engagement); o produto final desta etapa é o relatório de vulnerabilidade entregue à diretoria para correção imediata.
  - *Modelo Mental / Metáfora Funcional:* A teia da aranha: cada fio isolado é fino e quase invisível; quando os fios se entrecruzam na mesma armação, formam uma estrutura capaz de capturar o alvo.
  - *Roteiro e Tom do Apresentador:* "Chegamos ao fechamento prático da nossa narrativa. Vocês se lembram da analista Marina Sousa, que vimos no Slide 06 comemorando a entrega do datacenter da Acme Pagamentos? Aqui está o ciclo investigativo concluído em um grafo de correlação: o perfil `@marina.souza` levou ao e-mail institucional `marina@acme.com`. Esse e-mail constava em dois vazamentos antigos de credenciais. O domínio da empresa revelou uma VPN de acesso remoto desprotegida. E o LinkedIn confirmou que ela tem alçada para aprovar transferências financeiras. Em vinte minutos de correlação pública, desenhamos o caminho crítico de entrada. E aqui reforçamos o limite ético: não tentamos fazer login na VPN nem testar senhas; nosso objetivo é entregar o relatório para que a Acme revogue as credenciais e feche o acesso."
- **Fatos Técnicos Preservados:**
  - [x] Conexão explícita com o fio condutor: Marina Sousa (@marina.souza) e Acme Pagamentos
  - [x] Nós do grafo: `@marina.souza`, `marina@acme.com`, 2 vazamentos, `acme.com`, VPN exposta, cargo financeiro
  - [x] Conexão com o e-mail de phishing do Slide 15
  - [x] Delimitação de conformidade ética e regras de engajamento

---

```
================================================================================
ARQUIVO 11 / 12: slides/06-opsec-fechamento.html
Bloco Temático: Bloco 06 — Segurança Operacional (OpSec) & Fechamento
Apresentadora: Geovana
Slides: 49 a 52
================================================================================
```

### Slide 49 · Divisor do Bloco 06
- **Cabeçalho:** Slide 49 | Arquivo: `slides/06-opsec-fechamento.html` | Apresentadora: Geovana | Título Original: `O rastro que você deixa sem perceber.`
- **Objetivo Didático Central:** Transicionar para o bloco de encerramento e defesa, introduzindo a Segurança Operacional (OpSec) como a disciplina responsável por gerenciar e mitigar a geração de dados públicos cotidianos.
- **Diagnóstico de AI Slop & Engessamento:** Título fragmentado com efeito poético; quiasmo simétrico condicional no subtítulo (*"Se o reconhecimento coleta, a OpSec reduz o que existe para coletar."*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Segurança Operacional (OpSec) e Conclusão` | Subtítulo: `Minimização de rastros digitais e gestão da superfície de exposição`.
  - *Proposta de Corpo de Texto e Tópicos:* `Bloco 06 · Geovana`. Declaração fundamental: "A segurança operacional estabelece as práticas e configurações necessárias para reduzir a telemetria pública, dificultando o reconhecimento tanto para indivíduos quanto para organizações."
  - *Modelo Mental / Metáfora Funcional:* Fechar as cortinas da casa: quem não quer ser observado da rua não precisa construir muros de concreto armado; basta puxar as cortinas e apagar a luz da sala.
  - *Roteiro e Tom do Apresentador:* "Obrigado, João Pedro. Retomo a apresentação para conduzir nosso último bloco: Segurança Operacional, ou OpSec. Ao longo deste seminário, mostramos como atacantes e analistas usam redes sociais, ferramentas de rede e bases de OSINT para mapear vulnerabilidades. Agora invertemos a perspectiva: como nós, como estudantes, futuros profissionais e administradores de sistemas, podemos reduzir os rastros que deixamos na internet todos os dias?"
- **Fatos Técnicos Preservados:**
  - [x] Numeração do Bloco: 06
  - [x] Apresentadora responsável: Geovana
  - [x] Definição preliminar de OpSec (Operations Security)

---

### Slide 50 · OpSec Conceito
- **Cabeçalho:** Slide 50 | Arquivo: `slides/06-opsec-fechamento.html` | Apresentadora: Geovana | Título Original: `OpSec é sobre não virar dado.`
- **Objetivo Didático Central:** Conceituar a OpSec através do diagrama concêntrico de exposição, ensinando que a proteção eficaz baseia-se na priorização de controles proporcionais ao valor e ao risco do dado.
- **Diagnóstico de AI Slop & Engessamento:** Título com slogan pretensioso ("OpSec é sobre não virar dado."); antítese com colon reveal na linha 61 (*"Não é paranoia: é priorização por impacto."*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Princípios de Segurança Operacional` | Subtítulo: `Identificação de fluxos de telemetria e análise de impacto proporcional`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Diagrama concêntrico de pegada digital:
      - *Núcleo:* O indivíduo ou o sistema crítico da organização.
      - *Anel 1 (Identidade e Credenciais):* Contas de e-mail, senhas, documentos e certificados corporativos.
      - *Anel 2 (Telemetria Direta):* Endereços IP de conexão, check-ins de localização e metadados EXIF de arquivos.
      - *Anel 3 (Exposição Externa):* Postagens públicas, menções em redes sociais, cadastros em serviços de terceiros e logs de CT.
    - Metodologia de priorização: A OpSec não busca o anonimato absoluto irrealista; ela avalia quais dados são críticos e aplica controles específicos para mitigar a probabilidade de interceptação.
  - *Modelo Mental / Metáfora Funcional:* Os anéis de segurança de uma embaixada: a portaria externa recebe o público geral; o saguão intermediário exige crachá; a sala do cofre exige biometria dupla.
  - *Roteiro e Tom do Apresentador:* "Vejam este diagrama em anéis concêntricos. No centro está você ou o servidor central da empresa. A cada ação digital — seja postar uma foto ou registrar um domínio — emitimos dados que se propagam pelos anéis externos. OpSec não significa viver como um fantasma offline. Trata-se de avaliar quais informações são sensíveis, qual o impacto caso sejam expostas e aplicar controles rigorosos para proteger os anéis internos."
- **Fatos Técnicos Preservados:**
  - [x] Diagrama concêntrico em anéis de pegada digital (footprint rings)
  - [x] Níveis de propagação de telemetria
  - [x] Princípio de análise de risco e proporcionalidade de impacto

---

### Slide 51 · OpSec no Dia a Dia (Seis Hábitos)
- **Cabeçalho:** Slide 51 | Arquivo: `slides/06-opsec-fechamento.html` | Apresentadora: Geovana | Título Original: `Seis hábitos que mudam o seu rastro`
- **Objetivo Didático Central:** Apresentar seis hábitos práticos e cotidianos de higiene cibernética, conectando cada recomendação diretamente às vulnerabilidades exploradas ao longo do seminário.
- **Diagnóstico de AI Slop & Engessamento:** Aforismo de encerramento na linha 121 (*"O elo mais barato de atacar continua sendo o hábito."*); empilhamento de antíteses e aforismos na linha 124 (*"Nenhum desses itens é exótico. O difícil não é saber — é manter. OpSec é higiene, não evento."*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Seis Controles Práticos de Higiene Digital` | Subtítulo: `Medidas operacionais de mitigação contra vetores comuns de reconhecimento`.
  - *Proposta de Corpo de Texto e Tópicos:*
    1. `Autenticação em Dois Fatores (2FA/MFA):` Utilização preferencial de chaves FIDO2 ou aplicativos geradores de tokens (TOTP), mitigando vazamentos de credenciais como os do caso Smart Sampa e o grafo da Marina.
    2. `Gerenciadores e Cofres de Senhas:` Geração de senhas exclusivas, longas e aleatórias para cada serviço corporativo, eliminando a reutilização de credenciais.
    3. `Atualizações Automáticas de Software:` Aplicação contínua de patches no sistema operacional e navegadores, fechando vulnerabilidades exploradas por anexos maliciosos (como o exploit de Flash do caso RSA).
    4. `Revisão de Permissões e Compartilhamento:` Auditoria periódica em autorizações de aplicativos e restrição de visibilidade de perfis institucionais.
    5. `Segmentação de Identidades:` Separação estrita entre contas de e-mail pessoais e corporativas, impedindo o cruzamento de nós no grafo de OSINT.
    6. `Higienização de Metadados em Arquivos:` Remoção prévia de coordenadas GPS e dados EXIF antes da publicação de documentos ou imagens na internet.
  - *Modelo Mental / Metáfora Funcional:* *Higiene pessoal preventiva:* A higiene cibernética opera como lavar as mãos com sabão: hábitos rotineiros e simples repetidos diariamente que evitam a maioria dos riscos operacionais.
  - *Roteiro e Tom do Apresentador:* "Apresentamos aqui seis controles diretos que todos nós podemos adotar hoje. Se a analista Marina Sousa usasse um aplicativo de 2FA, a senha vazada no fórum não permitiria login. Se ela tivesse limpado os metadados EXIF da foto do plantão, as coordenadas do novo datacenter não estariam expostas. Segurança operacional é consistência de hábitos: gerenciar senhas em cofre, aplicar duplo fator, manter sistemas atualizados e revisar o que publicamos."
- **Fatos Técnicos Preservados:**
  - [x] Os seis controles operacionais: 2FA, cofre de senhas, patches, permissões, segmentação de identidades e remoção de EXIF
  - [x] Conexão causal direta com o caso da Acme Pagamentos (Marina Sousa)
  - [x] Conexão com os incidentes Smart Sampa e RSA
  - [x] Eliminação do aforismo "OpSec é higiene, não evento"

---

### Slide 52 · Conclusões Centrais (Takeaways)
- **Cabeçalho:** Slide 52 | Arquivo: `slides/06-opsec-fechamento.html` | Apresentadora: Geovana | Título Original: `Três coisas para levar`
- **Objetivo Didático Central:** Consolidar as três grandes conclusões técnicas e metodológicas do seminário, encerrando com uma mensagem afirmativa sobre a importância do reconhecimento para a segurança defensiva.
- **Diagnóstico de AI Slop & Engessamento:** Contraste binário no subtítulo (*"Recon é processo, não ferramenta."*); frase de efeito de mic-drop na linha 172 (*"Recon é a única fase do ataque que a defesa também pode praticar — e deveria."*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Conclusões do Seminário` | Subtítulo: `Princípios fundamentais para a prática de segurança ofensiva e defensiva`.
  - *Proposta de Corpo de Texto e Tópicos:*
    1. `O método precede a ferramenta:` Ferramentas automatizadas multiplicam a velocidade de coleta, mas a geração de inteligência efetiva depende da formulação prévia de hipóteses e da disciplina de análise temporal.
    2. `A superfície de ataque extrapola o perímetro de rede:` O firewall corporativo e as defesas de borda não conseguem proteger informações que colaboradores, fornecedores e certificados já expuseram publicamente na internet.
    3. `O reconhecimento é uma prática indispensável para a defesa:` A condução periódica e sistemática de exercícios de reconhecimento pela equipe de segurança permite identificar e corrigir exposições críticas antes que sejam mapeadas por atacantes hostis.
  - *Modelo Mental / Metáfora Funcional:* Olhar a própria casa com os olhos do ladrão: antes de dormir, você sai na calçada e olha para a sua casa para conferir se alguma janela ficou aberta.
  - *Roteiro e Tom do Apresentador:* "Para encerrar nosso conteúdo técnico, deixamos três conclusões: primeiro, ferramentas automatizadas não substituem a análise crítica e o método investigativo. Segundo, os melhores firewalls do mundo são inúteis se as credenciais e os organogramas estiverem abertos em redes sociais e logs de certificados. E terceiro: o reconhecimento não é exclusividade de quem ataca. A melhor defesa cibernética começa quando a própria organização audita sua superfície externa de forma contínua."
- **Fatos Técnicos Preservados:**
  - [x] As três teses centrais do seminário (Método, Superfície e Defesa Pró-ativa)
  - [x] Encerramento temático com declarações afirmativas
  - [x] Transição para as referências e arguição da banca

---

```
================================================================================
ARQUIVO 12 / 12: slides/07-referencias-perguntas.html
Bloco Temático: Fechamento & Sessão de Perguntas e Respostas (Q&A)
Apresentadores: Todos
Slides: 53 e 54
================================================================================
```

### Slide 53 · Referências Bibliográficas
- **Cabeçalho:** Slide 53 | Arquivo: `slides/07-referencias-perguntas.html` | Apresentadores: Todos | Título Original: `Referências e leituras`
- **Objetivo Didático Central:** Documentar o embasamento teórico, normativo e jornalístico que fundamentou todo o conteúdo do seminário em conformidade com o padrão acadêmico.
- **Diagnóstico de AI Slop & Engessamento:** Slide predominantemente limpo e técnico. Os travessões presentes nas referências bibliográficas atuam legitimamente como separadores padronizados de títulos de publicações formais (sem desvios de AI slop).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Referências Bibliográficas e Normativas` | Subtítulo: `Padrões técnicos, guias metodológicos e fontes documentais utilizadas`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Citações formais completas:
      1. *MITRE ATT&CK TA0043:* Enterprise Matrix — Reconnaissance Technique & Sub-techniques (2026).
      2. *OWASP Foundation:* Web Security Testing Guide (WSTG v4.2) — Information Gathering.
      3. *RFC 6962:* Certificate Transparency — IETF Standards Track.
      4. *RFC 5737:* IPv4 Address Blocks Reserved for Documentation (TEST-NET-1, 2 e 3).
      5. *Michael Bazzell:* Open Source Intelligence Techniques (10th Edition, 2023).
      6. *G1 Notícias (21/10/2026):* Reportagem sobre a exposição de credenciais do sistema de videomonitoramento Smart Sampa.
      7. *The Guardian / Nathan Ruser (2018):* Cobertura da descoberta de bases militares sigilosas via Strava Global Heatmap.
      8. *Zoho Workplace Reports (2011):* Documentação da anatomia do ataque de spear-phishing à RSA Security.
      9. *Manuais Técnicos de Ferramentas:* Documentação e guias oficiais de referência do Nmap, Wireshark, Shodan e Censys.
  - *Modelo Mental / Metáfora Funcional:* A fundação do edifício: a credibilidade da apresentação assenta-se sobre normas de engenharia e documentos oficiais verificáveis.
  - *Roteiro e Tom do Apresentador:* "Apresentamos aqui as referências que embasaram o nosso trabalho: matriz MITRE ATT&CK, padrões RFC da IETF, guias de teste da OWASP, a obra de referência de Michael Bazzell em OSINT, manuais de Nmap, Wireshark, Shodan e Censys, e os relatórios jornalísticos e técnicos dos estudos de caso analisados."
- **Fatos Técnicos Preservados:**
  - [x] MITRE ATT&CK TA0043
  - [x] OWASP WSTG v4.2
  - [x] RFC 6962 e RFC 5737
  - [x] Livro Open Source Intelligence Techniques (Michael Bazzell)
  - [x] Manuais técnicos oficiais: Nmap, Wireshark, Shodan e Censys
  - [x] Fontes documentais dos 3 casos reais (Smart Sampa 2026, RSA 2011 e Strava 2018)

---

### Slide 54 · Sessão de Perguntas e Respostas (Q&A)
- **Cabeçalho:** Slide 54 | Arquivo: `slides/07-referencias-perguntas.html` | Apresentadores: Todos | Título Original: `Perguntas ?`
- **Objetivo Didático Central:** Finalizar formalmente a apresentação perante a banca examinadora e a turma, abrindo a sessão de arguição técnica de forma receptiva, colaborativa e profissional.
- **Diagnóstico de AI Slop & Engessamento:** Aforismo pretensioso na legenda (*"A parte mais interessante do recon é o que a gente não pensou em perguntar"*).
- **Proposta de Reformulação Didática ("Dessengessada"):**
  - *Proposta de Título / Manchete:* `Sessão de Perguntas e Discussão Técnica` | Subtítulo: `Agradecemos a atenção da banca examinadora e dos colegas`.
  - *Proposta de Corpo de Texto e Tópicos:*
    - Mensagem de encerramento direta:
      - "Estamos à disposição dos professores e colegas para esclarecimentos técnicos, aprofundamento metodológico e debate sobre os tópicos apresentados."
      - Exibição dos nomes dos cinco apresentadores e dados de contato institucional.
    - *(Eliminação do aforismo pretensioso de fechamento).*
  - *Modelo Mental / Metáfora Funcional:* A mesa-redonda acadêmica: o fim da exposição unilateral e o início do debate de alto nível entre pesquisadores e engenheiros.
  - *Roteiro e Tom do Apresentador:* "Concluímos aqui a nossa exposição de 45 minutos. Agradecemos a atenção do professor e de toda a turma e abrimos a palavra para a banca para perguntas, observações e discussão técnica sobre qualquer um dos tópicos abordados. Muito obrigado."
- **Fatos Técnicos Preservados:**
  - [x] Sessão de perguntas e respostas (Q&A)
  - [x] Presença dos cinco integrantes da equipe no encerramento
  - [x] Tom respeitoso e acadêmico para avaliação perante a banca

---
# 3. Matriz de Rastreabilidade e Preservação Técnica Integral

Para garantir a conformidade absoluta com o **Mandato de Integridade** e o requisito R2 do projeto, a tabela abaixo consolida todos os artefatos técnicos, métricas quantitativas, parâmetros de linha de comando, serviços de rede, estudos de caso e normas abordados na apresentação original, comprovando sua **preservação integral de 100%** no plano didático formulado.

### 3.1. Matriz Consolidada de Ferramentas, Comandos e Flags

| Ferramenta / Plataforma | Categoria / Escopo | Slide(s) | Parâmetros, Comandos e Sintaxes Preservados | Status de Preservação |
| :--- | :--- | :---: | :--- | :---: |
| **Nmap** (v7.95) | Varredura Ativa | 12 | `nmap -sS -sV -p- 10.10.14.23 -oA recon_alvo`<br />Flags: `-sS` (SYN scan), `-sV` (versões), `-p-` (todas as 65.535 portas), `-oA` (três saídas). | **100% Preservado** |
| **Wireshark** | Inspeção de Pacotes | 13, 14 | Filtro de exibição: `ip.addr == 10.10.14.23 && tcp.port == 80`<br />Interface: `eth0`; dissecação de Frame, Ethernet II, IPv4 e TCP; Follow TCP Stream 0. | **100% Preservado** |
| **Shodan** | Busca de Dispositivos | 31, 32 | Consulta ao IP de documentação `192.0.2.10`, identificação da porta HTTPS 443 e banner de serviço. | **100% Preservado** |
| **Censys** | Busca de Infraestrutura | 31, 32 | Indexação de certificados SSL/TLS associados ao domínio institucional `example.com`. | **100% Preservado** |
| **WHOIS / RDAP** | Registros de Domínio | 31, 33 | Consulta cadastral de `example.com`, nameservers `ns1.example.com`, dados protegidos por GDPR/LGPD. | **100% Preservado** |
| **SecurityTrails** | DNS Passivo | 31, 34 | Resolução histórica do IP `198.51.100.20` em 2023 para o domínio `example.com`. | **100% Preservado** |
| **VirusTotal** | Reputação e Relações | 31, 34 | Relações de infraestrutura e correlação com o endereço IP `192.0.2.10`. | **100% Preservado** |
| **crt.sh** | Certificate Transparency | 31, 35 | Operador curinga `%.example.com` para enumeração de subdomínios e identificação do SAN `teste.example.com`. | **100% Preservado** |
| **Subfinder** | Enumeração de Nomes | 31, 36 | Agregação passiva com flag `-passive` para retorno de subdomínios (ex: `www.example.com`). | **100% Preservado** |
| **OWASP Amass** | Grafos de Superfície | 31, 36 | Mapeamento passivo de relações (`amass enum -passive`) entre domínios, ASNs e blocos de rede. | **100% Preservado** |
| **ExifTool** | Extração de Metadados | 31, 37 | Leitura de metadados forenses no arquivo `relatorio.pdf` (Autor: `Equipe Exemplo`). | **100% Preservado** |
| **FOCA** | Análise de Documentos | 31, 37 | Fingerprinting de arquivos corporativos (Software: `Editor de PDF v2.4`, caminhos de rede locais). | **100% Preservado** |
| **Google Dorks (GHDB)** | Busca Web Avançada | 27 | Operadores: `site:example.com`, `filetype:pdf/xls/env`, `inurl:admin`, `intitle:"index of /"`. | **100% Preservado** |
| **SunCalc** | Análise Solar / GEOSINT | 46, 47 | Cálculo de azimute solar e inclinação de sombras na fotografia da Ruta 40 em Mendoza (32.89°S 68.84°W). | **100% Preservado** |
| **Overpass / Overpass Turbo** | Consulta Geoespacial OSM | 46, 47 | Extração vetorial de rodovias e validação de traçados viários e relevo no OpenStreetMap. | **100% Preservado** |
| **Google Lens** | Busca Visual Reversa | 46, 53 | Reconhecimento de padrões em elementos viários e sinalizações de estrada na estepe argentina. | **100% Preservado** |
| **Mapillary** | Imagens ao Nível da Rua | 46, 53 | Validação colaborativa de imagens ao nível da via para confirmação de trecho na Ruta 40. | **100% Preservado** |
| **Wayback Machine** | Arquivo Histórico Web | 18, 53 | Recuperação de versões arquivadas de páginas web institucionais e dados históricos fora do ar. | **100% Preservado** |
| **Have I Been Pwned / HIBP** | Consulta a Vazamentos | 18, 48, 53 | Verificação passiva de exposição de endereços de e-mail e credenciais corporativas em breaches. | **100% Preservado** |

---

### 3.2. Matriz de Endereçamento de Rede, Portas e Credenciais

| Ativo / Elemento | Valor Técnico Exato | Contexto no Deck | Papel Didático |
| :--- | :--- | :---: | :--- |
| **IP do Alvo (Lab)** | `10.10.14.23` | Slides 12, 13, 14 | Host alvo da varredura Nmap e da captura de tráfego no Wireshark. |
| **IP do Atacante (Lab)** | `10.10.14.5` | Slides 13, 14 | Host de origem da conexão TCP e da requisição HTTP `/admin/`. |
| **Rede de Laboratório** | `10.10.14.0/24` | Slides 12, 13 | Rede interna autorizada para o teste de intrusão prático. |
| **IP de Documentação 1** | `192.0.2.10` | Slides 23, 32, 34 | Endereço reservado RFC 5737 (TEST-NET-1) simulando host no Shodan e Censys. |
| **IP de Documentação 2** | `198.51.100.20` | Slide 34 | Endereço reservado RFC 5737 (TEST-NET-2) simulando registro DNS histórico em 2023. |
| **Porta 22/tcp** | `OpenSSH 8.9p1 Ubuntu 3ubuntu0.6` | Slide 12 | Porta SSH aberta identificada no scan Nmap. |
| **Porta 80/tcp** | `nginx 1.24.0` | Slides 12, 13, 14 | Servidor web HTTP e alvo da captura de pacotes no Wireshark. |
| **Porta 443/tcp** | `nginx 1.24.0 (ssl/http)` | Slides 12, 32 | Servidor web HTTPS seguro com certificado digital ativo. |
| **Porta 3306/tcp** | `MySQL 8.0.35` | Slide 12 | Banco de dados exposto diretamente na rede externa (vulnerabilidade perimetral). |
| **Porta 8080/tcp** | `Jetty 9.4.53` | Slides 12, 14 | Aplicação web secundária com autenticação básica no realm `Jetty Admin`. |
| **Porta 3389/tcp** | `RDP (filtered)` | Slide 12 | Porta de Área de Trabalho Remota filtrada por firewall. |
| **Porta de Origem TCP** | `49812` | Slides 13, 14 | Porta efêmera do cliente na negociação do Three-Way Handshake. |
| **String Base64** | `Authorization: Basic YWRtaW46YWRtaW4=` | Slide 14 | Cabeçalho HTTP decodificado para as credenciais `admin:admin`. |
| **MAC Address Origem** | `00:1a:2b:3c:4d:5e` | Slide 13 | Endereço físico da interface de rede do cliente no pacote 1. |
| **MAC Address Destino** | `00:0c:29:aa:bb:cc` | Slide 13 | Endereço físico da interface de rede do servidor no pacote 1. |

---

### 3.3. Matriz dos Estudos de Caso, Fio Narrativo e Disciplinas INT

| Evento / Caso | Ano / Período | Atores e Elementos Centrais | Dados Técnicos Preservados |
| :--- | :---: | :--- | :--- |
| **Smart Sampa** | Outubro de 2026 | Cidade de São Paulo, 58 mil câmeras municipais de vigilância urbana, reportagem de 21/10/2026. | Exposição contínua por 11 meses de credenciais de acesso em repositórios abertos sem rotação. |
| **RSA SecurID** | Março de 2011 | RSA Security, funcionários de RH, anexo `2011_Recruitment_Plan.xls` (corrigido do anacrônico 2021). | Exploit de Adobe Flash embutido em Excel (CVE-2011-0609), backdoor Poison Ivy, comprometimento de sementes criptográficas e substituição de 40 milhões de tokens. |
| **Strava Global Heatmap** | 2017–2018 | Strava, Nathan Ruser, bases militares no Afeganistão, Síria e Somália. | Agregação de 3 trilhões de pontos GPS e 13 bilhões de km, mapeamento involuntário de postos sigilosos e coordenadas exatas da base militar no Afeganistão (`34.5°N 69.2°E`) por sobreposição com satélite. |
| **GEOSINT Ruta 40** | Exemplo Didático | Fotografia de rodovia na pré-cordilheira andina, analista de GEOSINT. | Coordenadas exatas `32.89°S 68.84°W` (Mendoza, Argentina), 78% de confiança, conjunto instrumental integrado `SunCalc`, `Google Lens`, `Mapillary` e `Overpass` (Slides 46 e 47). |
| **Fio Narrativo Acme** | Outubro de 2026 | Analista Marina Sousa (@marina.souza), empresa Acme Pagamentos, novo datacenter. | Encadeamento contínuo: Post social (Slide 06) $\rightarrow$ Phishing com `Formulario_Plano_2026.xlsx` (Slide 15) $\rightarrow$ Certificado `datacenter-sp.acme.com` (Slides 21/28/35) $\rightarrow$ Grafo OSINT completo (Slide 48). |
| **As 9 Disciplinas INT** | Formal | HUMINT, GEOINT, FININT, ELINT, IMINT, TECHINT, CYBINT/DNINT, SOCMINT, SIGINT. | Taxonomia integral de disciplinas de inteligência militar e sua correlação com OSINT (Slide 40). |

---

### 3.4. Matriz Normativa e Padrões Internacionais

| Norma / Referencial | Órgão Emissor | Tópico Técnico | Localização no Plano |
| :--- | :--- | :--- | :---: |
| **MITRE ATT&CK TA0043** | MITRE Corporation | Tática de Reconhecimento na Matriz Enterprise | Slides 09, 52, 53 |
| **RFC 6962** | IETF | Certificate Transparency (Estrutura de Logs TLS) | Slides 21, 28, 35, 53 |
| **RFC 5737** | IETF | Blocos de IP Reservados para Documentação (TEST-NET-1 e 2) | Slides 20, 23, 32, 34, 53 |
| **OWASP WSTG v4.2** | OWASP Foundation | Guia de Teste de Segurança em Aplicações Web (Information Gathering) | Slides 31, 36, 53 |
| **GDPR / LGPD** | UE / Brasil | Proteção e Anonimização de Dados Pessoais em Registros WHOIS | Slides 33, 50, 51 |

---

# 4. Verificação de Não Alteração dos Slides e Integridade do Repositório

### 4.1. Certificação Formal de Não Intervenção em `slides/`
Em estrito cumprimento às restrições do projeto e ao mandato de integridade, **nenhum arquivo contido no diretório `slides/` foi modificado, criado ou renomeado durante o Milestone M2**. O escopo desta etapa limitou-se à produção do documento mestre de planejamento `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md` e aos metadados protocolares no diretório `.agents/teamwork/worker_m2/`.

### 4.2. Evidência de Validação do Build e Testes Automatizados
A suíte de verificação automatizada foi executada para atestar que o repositório mantém integridade estrita e que todos os validadores de build continuam passando sem erros:

1. **Validador de Integridade dos Slides (`scripts/build.py --check`):**
   ```bash
   $ python3 scripts/build.py --check
   index.html está atualizado e os blocos são válidos.
   ```
   *Resultado:* Retorno código 0. Todos os 54 slides e 12 arquivos HTML mantêm formatação horizontal estrita, tags `<aside class="notes">` íntegras e sincronia total com `slides/manifest.json`.

2. **Suíte de Testes Unitários (`python3 -m unittest discover -s tests -v`):**
   ```bash
   $ python3 -m unittest discover -s tests -v
   test_all_slides_are_horizontal_and_have_notes (test_build.PresentationBuildTests.test_all_slides_are_horizontal_and_have_notes) ... ok
   test_build_does_not_remove_unknown_files (test_build.PresentationBuildTests.test_build_does_not_remove_unknown_files) ... ok
   test_root_index_matches_modules (test_build.PresentationBuildTests.test_root_index_matches_modules) ... ok
   test_static_site_contains_referenced_resources (test_build.PresentationBuildTests.test_static_site_contains_referenced_resources) ... ok
   test_theme_shortcut_has_no_persistent_button (test_build.PresentationBuildTests.test_theme_shortcut_has_no_persistent_button) ... ok
   test_tool_groups_are_sequential_slides (test_build.PresentationBuildTests.test_tool_groups_are_sequential_slides) ... ok
   test_validator_rejects_nested_slides_and_missing_notes (test_build.PresentationBuildTests.test_validator_rejects_nested_slides_and_missing_notes) ... ok

   ----------------------------------------------------------------------
   Ran 7 tests in 0.103s

   OK
   ```
   *Resultado:* 7 de 7 testes executados com 100% de sucesso.

3. **Status do Repositório Git:**
   ```bash
   $ git status --short slides/
   # (Nenhum retorno - zero modificações na pasta slides/)
   ```

Com estas confirmações, o **Plano Mestre de Implementação Didática** conclui o Milestone M2 e fica plenamente homologado para orientar com segurança e clareza a execução do próximo marco de trabalho.

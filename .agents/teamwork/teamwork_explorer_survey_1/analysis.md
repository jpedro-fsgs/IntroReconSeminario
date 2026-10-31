# Relatório de Análise: Estrutura, Fluxo Narrativo e Inventário Técnico dos Slides

**Data:** 31 de Outubro de 2026  
**Agente:** Explorer 1 (`teamwork_explorer_survey_1`)  
**Missão:** Investigação aprofundada read-only da apresentação de seminário em `slides/` (`IntroReconSeminário`), mapeamento de arquivos, arquitetura HTML, fluxo narrativo global, inventário factual/técnico exaustivo e avaliação textual preliminar orientada pela skill `/no-ai-slop`.

---

## 1. Visão Geral do Deck e Estrutura de Arquivos

A apresentação é construída sobre o framework **Reveal.js**, configurada com navegação **exclusivamente horizontal** (slides verticais são expressamente proibidos pelo validador do projeto em `scripts/build.py`).

O deck é composto por **54 slides sequenciais** distribuídos modularmente em **12 arquivos HTML** dentro da pasta `slides/`, ordenados pelo manifesto oficial `slides/manifest.json`. Cada slide é encapsulado em uma tag `<section class="slide ...">` e contém obrigatoriamente exatamente uma tag `<aside class="notes">` contendo as notas do orador e instruções de palco.

### Tabela Geral de Arquivos e Divisão por Bloco

| Ordem | Arquivo HTML | Qtd Slides | Slides | Bloco Temático | Apresentador(es) | Tema Central |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- |
| **00** | `00-abertura.html` | 2 | 01–02 | Capa & Agenda | Todos | Abertura do seminário, enquadramento ("o que o alvo já contou?") e visão geral dos 6 blocos. |
| **01** | `01-conceito-contexto.html` | 7 | 03–09 | Bloco 01: Conceito & Contexto | Geovana | Era das mídias sociais, timeline de redes, superexposição, casos Twitter e Smart Sampa, definição formal de Recon (MITRE TA0043). |
| **02** | `02-recon-ativo.html` | 6 | 10–15 | Bloco 02: Reconhecimento Ativo | Emilio | Fundamentos de redes (IP, porta, pacote), simulação do Nmap (SYN scan), simulação do Wireshark (3-way handshake e stream), engenharia social (phishing). |
| **03** | `03a-passivo-introducao.html` | 3 | 16–18 | Bloco 03 (Parte 1): Recon Passivo | Daniel | Princípio de coletar sem tocar, zero pacotes ao alvo, definição e escopo de OSINT (método, propósito, fontes públicas). |
| **04** | `03b-ciclo-osint.html` | 7 | 19–25 | Bloco 03 (Parte 2): Ciclo de OSINT | Daniel | As 6 etapas do ciclo de inteligência: Planejar, Coletar, Processar, Analisar, Disseminar e Feedback (estudo de caso com `example.com`). |
| **05** | `03c-tecnicas-ferramentas.html` | 6 | 26–31 | Bloco 03 (Parte 3): Técnicas Passivas | Daniel | As 4 portas de entrada (Busca/indexação, DNS/certificados, Registros/infraestrutura, Pessoas/vazamentos) e visão geral das ferramentas. |
| **06** | `03c1-ferramentas-detalhes.html` | 6 | 32–37 | Bloco 03 (Parte 4): Detalhes de Ferramentas | Daniel | Telas e fluxos dedicados: Shodan/Censys, WHOIS, SecurityTrails/VirusTotal, crt.sh, Subfinder/Amass, ExifTool/FOCA. |
| **07** | `03d-fisico-ecossistema.html` | 3 | 38–40 | Bloco 03 (Parte 5): Recon Físico & INTs | Daniel | Reconhecimento físico (Dumpster diving e Shoulder surfing) e o Ecossistema de Inteligência (9 disciplinas INT). |
| **08** | `04-estudos-caso.html` | 4 | 41–44 | Bloco 04: Estudos de Caso | João Pedro Gonçalves | Casos reais de grande impacto: RSA SecurID (2011, spear-phishing) e Strava Heatmap (2018, correlação geográfica), síntese de aprendizados. |
| **09** | `05-geosint-osint.html` | 4 | 45–48 | Bloco 05: Demonstrações Práticas | João Pedro Almeida | Casos práticos demonstrados: GEOSINT 1 (Ruta 40 Mendoza), GEOSINT 2 (eliminação por sombras/sol), OSINT Demo (Grafo de correlação). |
| **10** | `06-opsec-fechamento.html` | 4 | 49–52 | Bloco 06: OpSec & Fechamento | Geovana | Conceito de OpSec (anéis de exposição), 6 hábitos cotidianos de higiene digital, 3 conclusões centrais (takeaways). |
| **11** | `07-referencias-perguntas.html` | 2 | 53–54 | Fechamento & Q&A | Todos | Bibliografia/referências normativas e encerramento para sessão de perguntas e respostas. |

---

## 2. Análise da Arquitetura HTML e Padrões de Layout

### 2.1. Estrutura do Contêiner do Slide
Todos os slides seguem uma anatomia padronizada e semântica:
```html
<!-- XX · TÍTULO DO SLIDE -->
<section class="slide [classes-adicionais]">
  <div class="slide-inner">
    <div class="slide-head">
      <div class="kicker"><span class="who">Nome</span> · Tema</div>
      <h2 class="h-lg ou h-md">Título principal</h2>
      <p class="lede">Texto de apoio / frase guia (opcional)</p>
    </div>
    <div class="slide-body [grid-especifico]">
      <!-- Conteúdo visual, cards, diagramas, terminais -->
    </div>
    <aside class="notes">
      <p class="who">Nome</p>
      Texto com orientações de fala, tempo, alertas e ganchos.
    </aside>
  </div>
</section>
```

### 2.2. Tipologia de Classes de Seção e Componentes
A apresentação utiliza uma tipografia altamente modular estilizada via CSS customizado em `css/`:
1. **Divisores de Bloco (`class="slide divider center"`):**
   - Slides 03, 10, 16, 41, 45, 49.
   - Apresentam número gigante transparente (`<span class="ghost-num">XX</span>`), linha vermelha decorativa (`<div class="red-rule"></div>`), kicker do apresentador, headline em destaque (`<h2 class="statement">`) e rodapé do capítulo (`<div class="divider-foot">`).
2. **Cards e Mockups de Interface:**
   - **Simulação de Terminal:** Nmap (slide 12) usa janelas estilizadas (`<div class="window fill">`) com botões decorativos macOS (`.dot.r`, `.dot.y`, `.dot.g`), barra de status e saída monospace.
   - **Simulação de Wireshark:** Slide 13 usa estrutura completa de GUI (`<div class="ws fill">`) com barra de menu, campo de filtro verde (`ip.addr == ...`), lista de pacotes colunar, árvore de dissecação de protocolos e dump hexadecimal.
   - **Simulação de E-mail de Phishing:** Slide 15 usa layout de cliente de e-mail corporativo (`<div class="mail">`) com remetente falso, anexo perigoso e anotações numéricas de alerta.
   - **Simulação de Redes Sociais:** Slide 06 (card estilo Instagram com foto e localização) e Slide 07 (card estilo Twitter/X com tweet em tempo real).
   - **Simulação de Ferramentas de OSINT (slides 32–37):** Grid comparativo padronizado (`.tool-detail-grid`) dividindo a esquerda conceitual ("O que responde", "Cenário fictício", "Limite") e a direita como janela simulada da ferramenta.
3. **Diagramas SVG Nativos:**
   - Slide 11: Diagrama de topologia de rede (notebook, roteador gateway, servidor, pacote SYN).
   - Slide 14: Diagrama sequencial de TCP Three-Way Handshake (`<svg class="hs-svg">`).
   - Slide 19: Anel orbital do ciclo de OSINT (`<svg class="orbit-ring">`).
   - Slide 46 e 47: Fotos e mapas vetoriais para análise geográfica e sombras solares.
   - Slide 48: Grafo de relações OSINT vetorial conectando pessoa, e-mail, vazamentos e VPN corporativa.
   - Slide 50: Círculos concêntricos de pegada digital (`.footprint .ring`).

### 2.3. Notas do Orador (`<aside class="notes">`)
- Cada slide possui rigorosamente uma única tag `<aside class="notes">`.
- As notas contêm orientações didáticas precisas para cada integrante, definindo:
  - Tom de voz e postura cênica (ex: "narrar como analista", "pausa dramática de alguns segundos", "não ler os itens do slide").
  - O que enfatizar e o que evitar (ex: não afirmar invasão no caso Smart Sampa, ressaltar dados agregados no caso Strava).
  - Ganchos de transição entre apresentadores e blocos.

---

## 3. Mapeamento do Fluxo Narrativo Global

O seminário foi arquitetado com uma curva dramática e pedagógica que vai do cotidiano individual à técnica pura, passa por crises reais corporativas e culmina em postura defensiva pessoal:

```
[Abertura: O Alvo já Contou]
        │
        ▼
[Bloco 1: Da Vida Digital ao Conceito de Recon] (Geovana)
        │  * Rotina de redes sociais → Superexposição → Casos reais → MITRE ATT&CK
        ▼
[Bloco 2: Reconhecimento Ativo — Tocando no Alvo] (Emilio)
        │  * Pacotes na rede → Nmap (portas/serviços) → Wireshark (tráfego/auth) → Phishing
        ▼
[Bloco 3: Reconhecimento Passivo & OSINT — Invisibilidade] (Daniel)
        │  * Princípio "sem tocar" → Ciclo OSINT em 6 fases → 4 Portas de entrada
        │  * Detalhamento de ferramentas (Shodan, Censys, WHOIS, crt.sh, etc.)
        │  * Reconhecimento físico (lixo, telas) & As 9 disciplinas INT
        ▼
[Bloco 4: Quando o Reconhecimento Vira Manchete] (João Pedro G.)
        │  * Caso RSA 2011 (o phishing que roubou tokens de segurança)
        │  * Caso Strava 2018 (o mapa fitness que revelou bases secretas)
        │  * A lição: O perigo do dado inofensivo
        ▼
[Bloco 5: Demonstração Prática Controlada] (João Pedro A.)
        │  * GEOSINT: Análise de sombras e pistas visuais (Ruta 40)
        │  * Eliminação de hipóteses geográficas com rigor analítico
        │  * Grafo OSINT correlacionando dados públicos sem invadir
        ▼
[Bloco 6: OpSec e Fechamento — Olhando para Si Mesmo] (Geovana & Todos)
        │  * Mudança de ótica: não virar dado
        │  * 6 hábitos práticos de higiene cibernética
        │  * 3 Takeaways finais: Recon é processo; o firewall tem limites; defesa age antes
        ▼
[Encerramento, Bibliografia & Q&A] (Todos)
```

### Transições Chave entre Integrantes:
- **Todos → Geovana (Slides 02 → 03):** Sai da visão panorâmica da agenda e mergulha na pergunta fundamental que inicia qualquer ataque.
- **Geovana → Emilio (Slides 09 → 10):** Do conceito de entender sem tocar para a ação de enviar pacotes reais e colher respostas da infraestrutura ativa.
- **Emilio → Daniel (Slides 15 → 16):** Do vetor de intrusão ativo/phishing de volta para a disciplina investigativa passiva (OSINT), onde o alvo não sabe que está sendo observado.
- **Daniel → João Pedro Gonçalves (Slides 40 → 41):** Da teoria metodológica e ferramental de inteligência para os desastres históricos reais (RSA e Strava).
- **João Pedro Gonçalves → João Pedro Almeida (Slides 44 → 45):** Do impacto das notícias para a bancada prática: como um analista opera GEOSINT e grafos passo a passo.
- **João Pedro Almeida → Geovana (Slides 48 → 49):** Do papel de analista ofensivo para a proteção própria (OpSec) e higiene digital pessoal e corporativa.

---

## 4. Inventário Meticuloso de Fatos Técnicos, Dados e Ferramentas a Preservar

Abaixo está o inventário de dados factuais, técnicos e metodológicos que **NÃO PODEM** ser removidos, adulterados ou suavizados em qualquer intervenção textual posterior.

### 4.1. Ferramentas e Tecnologias Catalogadas

| Categoria | Ferramenta / Tecnologia | Slides de Ocorrência | Contexto / Função Específica no Slide |
| :--- | :--- | :---: | :--- |
| **Scanner de Rede** | **Nmap** | 01, 02, 09, 11, 12, 53, 54 | Execução do comando `nmap -sS -sV -p- 10.10.14.23 -oA recon_alvo`, versão 7.95, SYN scan sem completar handshake, varredura de todas as 65.535 portas TCP. |
| **Análise de Pacotes** | **Wireshark** | 01, 02, 11, 13, 14, 53, 54 | Inspeção passiva de interface `eth0`, captura de 1.284 pacotes filtrada para 7 pacotes com `ip.addr == 10.10.14.23 && tcp.port == 80`, dissecação de Ethernet II, IPv4, TCP e HTTP. |
| **Motores de Busca IoT** | **Shodan** | 18, 31, 32, 53 | Consulta a índices de serviços e portas abertas previamente indexados na Internet sem contato direto com o alvo. |
| **Motores de Busca IoT** | **Censys** | 18, 31, 32, 53 | Análise comparativa com Shodan, mapeamento de certificados e serviços web indexados. |
| **Registros de Domínio** | **WHOIS** | 17, 18, 29, 31, 33 | Consulta cadastral de registradores, servidores de nomes (NS), dados de contato e proteções de privacidade em domínios. |
| **DNS & Reputação** | **SecurityTrails** | 31, 34 | Histórico de resoluções de DNS e associações históricas entre domínios e IPs ao longo dos anos. |
| **Inteligência de Ameaças**| **VirusTotal** | 31, 34 | Consulta de relações observadas, resoluções passadas e dados contextuais de infraestrutura. |
| **Transparência de Cert.** | **crt.sh** | 18, 28, 31, 35 | Consulta pública aos logs de Certificate Transparency (CT) para enumeração de subdomínios e Subject Alternative Names (SAN). |
| **Enumeração de Nomes** | **Subfinder** | 31, 36 | Ferramenta de enumeração rápida e passiva de subdomínios agregando múltiplas APIs externas. |
| **Mapeamento de Superfície**| **Amass (OWASP)** | 31, 36 | Mapeamento detalhado e estruturação de grafos de relações de subdomínios e infraestrutura em modo passivo. |
| **Análise de Metadados** | **ExifTool** | 31, 37, 51 | Extração forense de metadados de arquivos (PDFs, imagens EXIF: modelo de câmera/smartphone, GPS, software, data). |
| **Extração de Metadados** | **FOCA** | 31, 37 | Análise automatizada de metadados em lote em documentos corporativos públicos para levantamento de usuários e sistemas operacionais. |
| **Cálculo Solar / Sombras**| **SunCalc** | 46 | Análise astronômica de azimute e comprimento de sombras para determinação de horário solar e orientação geográfica. |
| **Reconhecimento Visual** | **Google Lens** | 46 | Busca reversa de imagens, placas, tipografia e elementos de cena em investigações de GEOSINT. |
| **Mapeamento de Rua** | **Mapillary** | 46 | Plataforma de fotos de nível de rua crowdsourced para validação de estradas e paisagens. |
| **Consultas OSM** | **Overpass Turbo** | 46 | Ferramenta de mineração de dados vetoriais do OpenStreetMap para localização por filtros espaciais. |
| **Globo Virtual** | **Google Earth** | 47 | Validação de relevo 3D, linhas de horizonte e imagens históricas de satélite. |
| **Vazamentos de Contas** | **Have I Been Pwned (HIBP)**| 18 | Base de verificação de exposição de contas e e-mails em vazamentos de dados históricos. |
| **Arquivo Histórico Web** | **Wayback Machine** | 18 | Consulta a snapshots históricos de páginas desativadas ou modificadas. |
| **Plataformas de OSINT** | **LinkedIn, GitHub** | 06, 18, 30 | Fontes de engenharia reversa de organograma, vagas abertas, tecnologias internas e credenciais acidentalmente commitadas. |

### 4.2. Dados de Redes, IPs, Portas e Artefatos Técnicos

- **Topologia de Laboratório Simulado (Slides 11, 12, 13, 14):**
  - IP Origem (Atacante/Emilio): `10.10.14.23`
  - IP Destino (Servidor Alvo): `10.10.14.5` (hostname `alvo.local`)
  - Sub-rede do Laboratório Autorizado: `10.10.14.0/24`
  - Porta de Origem Efêmera: `49812`
  - Portas do Alvo e Serviços Identificados:
    - `22/tcp open ssh`: OpenSSH 8.9p1 Ubuntu 3ubuntu0.6
    - `80/tcp open http`: nginx 1.24.0
    - `443/tcp open ssl/http`: nginx 1.24.0
    - `3306/tcp open mysql`: MySQL 8.0.35
    - `8080/tcp open http-proxy`: Jetty 9.4.53
    - `3389/tcp filtered`: RDP (filtrada pelo firewall)
  - Estatísticas do Scan Nmap: 65.535 portas testadas, 65.529 portas fechadas (reset), latência de `0.0021s`, duração total de `41.72 segundos`.
  - Arquivos gerados pelo flag `-oA`: `recon_alvo.nmap` (18 KB), `recon_alvo.xml` (42 KB).
- **Wireshark & Detalhes de Protocolo:**
  - Sintaxe de Filtro de Exibição: `ip.addr == 10.10.14.23 && tcp.port == 80`
  - Endereços MAC no Frame 1: `00:1a:2b:3c:4d:5e` (origem) e `00:0c:29:aa:bb:cc` (destino)
  - Flags TCP: `0x002 (SYN)`, Window Size `64240`, MSS `1460`, `SACK_PERM`
  - Sequência do Handshake:
    1. `Time 0.000000`: `49812 → 80 [SYN] Seq=0`
    2. `Time 0.000187`: `80 → 49812 [SYN, ACK] Seq=0 Ack=1`
    3. `Time 0.000203`: `49812 → 80 [ACK] Seq=1 Ack=1` (Conexão aberta em apenas `0.000203s` ou ~0,2 ms)
    4. `Time 0.000310`: `49812 → 80 [HTTP GET /admin/ HTTP/1.1]`
    5. `Time 0.000531`: `80 → 49812 [HTTP/1.1 401 Unauthorized]` com cabeçalho `WWW-Authenticate: Basic realm="Jetty Admin"`
    6. `Time 0.000612`: Envio de credenciais em Base64: `Authorization: Basic YWRtaW46YWRtaW4=`
    7. Decodificação da credencial em texto claro: `admin:admin`.
- **IPs Reservados de Documentação (RFC 5737 / RFC 6890):**
  - `192.0.2.10:443` (TEST-NET-1) usado nas demonstrações do Ciclo OSINT e Shodan/Censys.
  - `198.51.100.20` (TEST-NET-2) usado no exemplo histórico do SecurityTrails.
- **Domínios e E-mails Simulados:**
  - `example.com`, `portal.example.com`, `teste.example.com`.
  - Phishing do Slide 15: De `rh@beneficios-acme.com` para `voce@acme.com.br`, anexo malicioso `Formulario_Plano_2026.xlsx` (84 KB, macros habilitadas), canal falso de dúvidas `suporte@acme-beneficios-suporte.net`.
  - Demo de Grafo OSINT (Slide 48): Alvo fictício `@marina.souza`, e-mail `marina@acme.com`, 2 vazamentos históricos, VPN de borda corporativa em `acme.com`, cargo Financeiro.

### 4.3. Frameworks, Padrões e Metodologias

- **MITRE ATT&CK:** Tática **TA0043 (Reconnaissance)** — categorizada como a tática inicial preparatória que antecede qualquer vetor de intrusão (`Initial Access`).
- **OWASP:** *Web Security Testing Guide (WSTG)* e projeto Amass.
- **Ciclo de Inteligência OSINT (6 Etapas):**
  1. *Planejar* (definição de requisitos, escopo, perguntas específicas e limites legais).
  2. *Coletar* (obtenção metódica de fontes públicas preservando procedência e timestamps).
  3. *Processar* (normalização de dados, desduplicação, descarte de ruído sem perda de contexto histórico).
  4. *Analisar* (cruzamento de evidências, validação de hipóteses vs certezas, coocorrência vs causalidade).
  5. *Disseminar* (entrega de inteligência acionável e estruturada para tomada de decisão).
  6. *Feedback* (identificação de lacunas e refinamento de novos ciclos investigativos).
- **Certificate Transparency (CT):** Logs públicos de auditoria imutáveis mantidos pelo ecossistema de Autoridades Certificadoras (CAs) previstos em padrões de transparência TLS.
- **As 9 Disciplinas de Inteligência (Slide 40):**
  - `HUMINT` (Human Intelligence): inteligência de fontes humanas, relacionamentos, entrevistas.
  - `GEOINT` (Geospatial Intelligence): análise espacial, cartográfica e de terreno.
  - `FININT` (Financial Intelligence): fluxos financeiros e transações.
  - `ELINT` (Electronic Intelligence): sinais eletromagnéticos não comunicativos.
  - `IMINT` (Imagery Intelligence): satélites, drones e sensores de imagem.
  - `TECHINT` (Technical Intelligence): análise de equipamentos e hardware adversário.
  - `CYBINT` (Cyber Intelligence): infraestrutura de rede, malware e atores de ameaça digital.
  - `SOCMINT` (Social Media Intelligence): inteligência derivada de mídias e plataformas sociais.
  - `SIGINT` (Signals Intelligence): interceptação e análise de comunicações cifradas/transmitidas.

### 4.4. Estatísticas e Métricas Numéricas
- Média do brasileiro em telas: quase **9 horas por dia** totais, sendo quase **3 horas por dia** dedicadas a redes sociais, acumulando **116 horas conectadas por semana**.
- Linha do tempo das redes sociais: **1974** (Usenet), **1997** (SixDegrees), **2003** (LinkedIn), **2004** (Facebook & Orkut), **2005** (YouTube), **2006** (Twitter), **2010** (Instagram).
- Duração estimada da apresentação: **45 minutos** de fala + sessão de perguntas.
- Janela de revisão de OpSec: hábitos revisados a cada **90 dias**.
- Regra de ouro do Reconhecimento Passivo: **0 pacotes enviados ao alvo**.

### 4.5. Casos de Estudo Reais Documentados
1. **Caso Twitter / Encontro no Cinema (Slide 07):**
   - Post publicado às 21:04 com o texto: *"acabando de chegar no cinema pra ver o filme das 21h 🍿 📍 cinema · zona sul"*.
   - Vetor: Superexposição em tempo real sem necessidade de invasão ou rastreadores de hardware; exploração contextual imediata em situação de atrito pessoal.
2. **Caso Smart Sampa — São Paulo (Slide 08 & 53):**
   - Sistema integrado de videomonitoramento da capital paulista com **58 mil câmeras**.
   - Credenciais administrativas de acesso expostas publicamente por **11 meses** sem rotação (`admin / ••••••`).
   - Fonte documental: *G1 Tecnologia / Cibersegurança, 21 de outubro de 2026*.
3. **Caso RSA SecurID (Slide 42 & 53):**
   - Ano: **Março de 2011**.
   - Alvo: Fabricante dos tokens corporativos de autenticação multifator SecurID (RSA / EMC).
   - Vetor inicial: Spear-phishing com planilha anexa `2021_Recruitment_Plan.xlsx` explorando vulnerabilidade zero-day no Adobe Flash Player em endpoint de usuário comum.
   - Consequência: Movimentação lateral, comprometimento dos segredos criptográficos de sementes (seeds) dos tokens SecurID e necessidade de substituição global dos tokens para clientes críticos de defesa (incluindo Lockheed Martin).
   - Fonte documental: *Zoho Workplace — "RSA spear-phishing attack"*.
4. **Caso Strava Global Heatmap (Slide 43 & 53):**
   - Período dos dados: **2015 a 2017**; publicação do Heatmap global em **novembro de 2017**; descoberta pública em **28 de janeiro de 2018**.
   - Vetor: Publicação de dados de exercícios agregados de milhões de usuários. Soldados e agentes militares correram em rotas circulares em bases militares remotas no exterior (ex: FOB em coordenadas `34.5°N 69.2°E` no Afeganistão).
   - Lição: Cruzamento de calor de GPS com imagens de satélite desvendou o layout de instalações sigilosas sem que nenhuma senha ou rede tenha sido quebrada.
   - Fonte documental: *The Guardian, 28 de janeiro de 2018*.
5. **Caso Prático GEOSINT (Slides 46 e 47):**
   - Localização confirmada: **Ruta 40, Mendoza, Argentina** (coordenadas `32.89°S 68.84°W`).
   - Evidências: Sombra alongada projetada à esquerda sugerindo fim de tarde / sol poente no oeste; placa viária "Ruta 40 · Mendoza"; relevo pré-cordilheirano seco; sol compatível com as 15h locais; grau de confiança analítica de **78%** no primeiro momento e **92%** após eliminação das alternativas A e B.

---

## 5. Avaliação Preliminar da Estrutura Textual e AI-Slop

Com base nas diretrizes da skill `/no-ai-slop`, analisamos minuciosamente o estilo de redação atual dos slides e das notas do orador.

### 5.1. Pontos Fortes Notáveis da Redação Atual
- **Rigor Técnico Excepcional:** Os comandos do Nmap, o cabeçalho HTTP 401 do Jetty, os pacotes do Wireshark com flags e tempos e as terminologias de CT/OSINT são precisos, realistas e livres de generalismos ocos.
- **Concisão Visual:** Os slides não sofrem de "paredes de texto". Há uma distribuição inteligente entre kickers, ledes e cards gráficos.
- **Postura Ética e Jurídica:** Há uma insistência pedagógica contínua em distinguir o que é legalmente permitido, o que exige escopo/autorização e o que é simulação controlada.

### 5.2. Ocorrências e Sintomas de "AI Slop" Detectados
Apesar do bom nível técnico, o texto exibe marcas evidentes de escrita assistida por LLM que o deixam por vezes "engessado", hiper-simétrico e com cadência artificial:

1. **Repetição de Contrastes Binários Estilizados ("Não é X, é Y"):**
   - Slide 07: *"Não foi invasão. Foi leitura de contexto em tempo real."*
   - Slide 09: *"Recon não é invadir. É entender."*
   - Slide 15: *"O exploit é a confiança"*
   - Slide 16: *"Coletar sem tocar."*
   - Slide 18: *"Informação pública não é informação inofensiva."*
   - Slide 21: *"Coletar: reúna evidências, não certezas."*
   - Slide 22: *"Processar: separe sinal de ruído."*
   - Slide 23: *"Analisar: conecte sem presumir."*
   - Slide 44: *"Reconhecimento é correlação, não coleta."*
   - Slide 47: *"Eliminar, não adivinhar."*
   - Slide 50: *"OpSec é sobre não virar dado."*
   - Slide 52: *"Recon é processo, não ferramenta."*
   *Diagnóstico `/no-ai-slop`:* O padrão de contraste binário aparece em quase todos os blocos como muleta retórica para simular profundidade. Deve-se afirmar a conclusão diretamente ou variar a estrutura frasal.

2. **Repetição de Palavras Marcadoras e Jargão Corporativo de IA:**
   - O termo *"ecossistema"* aparece de forma repetitiva: no Slide 02 (*"ecossistema de inteligência"*), no Slide 08 (*"ecossistema do Smart Sampa"*) e no Slide 40 (*"ecossistema INT"*).
   - Frases vazias ou atalhos de transição como *"não é apenas / não é só"* (Slide 06), *"no final das contas"*, *"no seu cerne"*.

3. **Frases de Efeito "Falso-Profundas" (Fake-Profound Kickers):**
   - Slide 44: *"O dado mais perigoso é aquele que parece inofensivo."*
   - Slide 51: *"OpSec é higiene, não evento."*
   - Slide 52: *"Recon é a única fase do ataque que a defesa também pode praticar — e deveria."*
   - Slide 54: *"A parte mais interessante do recon é o que a gente não pensou em perguntar."*
   *Diagnóstico `/no-ai-slop`:* Embora soem bem em um pitch, quando empilhadas criam uma sensação de artificialidade. Devem ser ancoradas em consequências pragmáticas.

4. **Cadência Hiper-Engessada nos Títulos do Ciclo OSINT (Slides 19–25):**
   - Todos os títulos dos slides 20 a 25 foram forçados exatamente na mesma fôrma: `[Verbo]: [Frase de efeito]`:
     - *Planejar: faça a pergunta certa.*
     - *Coletar: reúna evidências, não certezas.*
     - *Processar: separe sinal de ruído.*
     - *Analisar: conecte sem presumir.*
     - *Disseminar: entregue algo acionável.*
     - *Feedback: a resposta abre outra pergunta.*
   *Diagnóstico `/no-ai-slop`:* O paralelismo estrito e repetido cansa a audiência e soa como template gerado por prompt ("Gere 6 títulos no formato Verbo: frase de impacto").

5. **Notas do Orador Prescritivas Demais / Teatrais:**
   - Notas contêm marcações como *"Pausa dramática: deixar a frase no telão por alguns segundos"* (Slide 44), *"Virar a chave: até agora olhamos o alvo; agora olhamos para nós"* (Slide 49), *"Ler o e-mail como se fosse real"* (Slide 15).
   - Soa como um roteiro de ator em vez de uma fala humana e natural de universitários apresentando um seminário técnico de segurança.

---

## 6. Recomendações Estruturadas para a Fase de Planejamento e Auditoria

1. **Preservação Sagrada dos Fatos Técnicos:** Qualquer proposta de reescrita deve preservar 100% dos nomes de ferramentas, portas (ex: 22, 80, 443, 3306, 8080), IPs (`10.10.14.23`, `10.10.14.5`), comandos (`nmap -sS -sV -p-`), anos (2011, 2018, 2026) e métricas (58 mil câmeras, 11 meses, 41.72s).
2. **Quebra da Simetria Robótica:** Variar as estruturas dos títulos das etapas de OSINT e dos divisores, adotando uma linguagem técnica mais direta, explicativa e coloquial.
3. **Substituição de Aforismos por Mecanismos:** Onde houver uma frase de efeito genérica ("O exploit é a confiança"), substituir pelo mecanismo real que opera ("Phishing explora a rotina e a autoridade para contornar defesas perimetrais").
4. **Naturalidade nas Notas do Orador:** Transformar as orientações de palco teatrais em tópicos de raciocínio lógico que o estudante possa explicar com suas próprias palavras na banca.
5. **Conformidade com Reveal.js:** Manter estritamente os 54 slides horizontais e o manifesto inalterado para não quebrar a suíte de testes de regressão do projeto (`python3 scripts/build.py --check`).

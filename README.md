# 🎯 Red Team 1 — Recon & OSINT: Roteiro & Write-up da Apresentação

> **Status:** Template em Branco / Estrutura Inicial  
> **Tema:** Reconhecimento (Recon) & Inteligência de Fontes Abertas (OSINT)  
> **Equipe:** Red Team 1  
> **Duração Estimada:** [Ex: 30 a 45 minutos + 10 min Q&A]  

---

## 👥 1. Identificação da Equipe & Papéis

| Integrante | Papel na Apresentação | Tópico(s) de Responsabilidade |
| :--- | :--- | :--- |
| **[Nome 1]** | [Ex: Abertura & Metodologia] | [Tópicos X e Y] |
| **[Nome 2]** | [Ex: Técnicas de OSINT Passivo] | [Tópicos Z e W] |
| **[Nome 3]** | [Ex: Recon Ativo & Tooling] | [Tópicos A e B] |
| **[Nome 4]** | [Ex: Demonstração / PoC & Fechamento] | [Tópicos C e D] |

---

## 🎯 2. Objetivos da Apresentação

- **Objetivo Geral:** [Definir o propósito principal da apresentação — ex: demonstrar a importância e as fases de reconhecimento em um ciclo de ataque do Red Team].
- **Objetivos Específicos:**
  1. [Objetivo 1 — ex: Diferenciar inteligência passiva de reconhecimento ativo]
  2. [Objetivo 2 — ex: Apresentar o framework/metodologia adotada pela equipe]
  3. [Objetivo 3 — ex: Demonstrar fluxo de coleta e correlação de dados]
  4. [Objetivo 4 — ex: Abordar limites éticos/legais e medidas de contra-inteligência]

---

## ⏱️ 3. Distribuição de Tempo Sugerida

| Bloco | Seção | Tempo Sugerido | Responsável |
| :---: | :--- | :---: | :---: |
| 1 | Abertura, Contexto & Objetivos | [00:00 - 05:00] | [Nome] |
| 2 | Fundamentos de Recon & Ciclo de OSINT | [05:00 - 12:00] | [Nome] |
| 3 | Técnicas de OSINT Passivo | [12:00 - 20:00] | [Nome] |
| 4 | Reconhecimento Ativo & Mapeamento de Superfície | [20:00 - 28:00] | [Nome] |
| 5 | Demonstração Prática / Estudo de Caso (PoC) | [28:00 - 38:00] | [Nome] |
| 6 | Visão Defensiva (Blue Team) & Ética / Legalidade | [38:00 - 43:00] | [Nome] |
| 7 | Conclusão & Sessão de Dúvidas (Q&A) | [43:00 - 50:00] | Todos |

---

## 📝 4. Roteiro Detalhado (Write-up dos Slides)

### Bloco 1: Abertura e Introdução
* **Slides correspondentes:** `01 - 03`
* **Pontos-chave a abordar:**
  - [ ] Boas-vindas e introdução da equipe Red Team 1.
  - [ ] Contextualização do Recon dentro da cadeia do ciberataque (Cyber Kill Chain / MITRE ATT&CK - TA0043: Reconnaissance).
  - [ ] Por que 80% do sucesso de uma invasão reside na fase de reconhecimento?
* **Notas de fala do apresentador:**
  > *[Inserir guia de fala / speech da abertura aqui]*

---

### Bloco 2: Fundamentos & Metodologia
* **Slides correspondentes:** `04 - 06`
* **Pontos-chave a abordar:**
  - [ ] Definição e distinção: Reconhecimento Passivo vs. Semi-Passivo vs. Ativo.
  - [ ] O ciclo de inteligência OSINT (Planejamento, Coleta, Processamento, Análise, Disseminação).
  - [ ] Vetores de superfície de ataque: Pessoas, Infraestrutura, Aplicações e Terceiros/Cadeia de suprimentos.
* **Notas de fala do apresentador:**
  > *[Inserir guia de fala aqui]*

---

### Bloco 3: Técnicas de OSINT Passivo
* **Slides correspondentes:** `07 - 10`
* **Pontos-chave a abordar:**
  - [ ] Fontes públicas e busca avançada (Dorks de Google/Bing/GitHub).
  - [ ] Enumeração de domínio, DNS histórico, WHOIS, registros BGP/ASN e certificados (Certificate Transparency logs).
  - [ ] Engenharia Social & Perfilamento de Pessoas (redes sociais corporativas, vazamentos de credenciais, repositórios públicos).
  - [ ] Metadados de arquivos públicos (FOCA, ExifTool, documentos indexados).
* **Notas de fala do apresentador:**
  > *[Inserir guia de fala aqui]*

---

### Bloco 4: Reconhecimento Ativo & Footprinting
* **Slides correspondentes:** `11 - 14`
* **Pontos-chave a abordar:**
  - [ ] Probing e descoberta de portas/serviços (sem disparar alertas precoces).
  - [ ] Varredura de tecnologias e fingerprinted web (Wappalyzer, Nuclei templates de recon, headers HTTP).
  - [ ] Mapeamento de diretórios, endpoints e APIs não documentadas.
  - [ ] Identificação de defesas perimetrais (WAF, IDS/IPS, CDN).
* **Notas de fala do apresentador:**
  > *[Inserir guia de fala aqui]*

---

### Bloco 5: Ferramentas, Frameworks & Automação
* **Slides correspondentes:** `15 - 17`
* **Pontos-chave a abordar:**
  - [ ] Frameworks integrados (ex: SpiderFoot, Recon-ng, Maltego, theHarvester).
  - [ ] Pipelines de automação modernos do Red Team (ex: Amass, Subfinder, httpx, Naabu, Katana).
  - [ ] Armazenamento e correlação de dados coletados (Bancos grafos, Neo4j, Obsidian, Elastic).
* **Notas de fala do apresentador:**
  > *[Inserir guia de fala aqui]*

---

### Bloco 6: Estudo de Caso / Demonstração Prática (PoC)
* **Slides correspondentes:** `18 - 20`
* **Pontos-chave a abordar:**
  - [ ] Cenário simulado (alvo fictício autorizado ou ambiente de laboratório).
  - [ ] Demonstração do fluxo de ataque: do primeiro dado público até o vetor de entrada viável.
  - [ ] Lições aprendidas da demonstração.
* **Notas de fala do apresentador:**
  > *[Inserir descrição da demonstração e comandos executados aqui]*

---

### Bloco 7: Contramedidas (Blue Team) & Aspectos Legais/Éticos
* **Slides correspondentes:** `21 - 23`
* **Pontos-chave a abordar:**
  - [ ] O que o Blue Team pode fazer para dificultar a coleta (Hardening de superfícies, redução de pegada digital, Threat Intelligence).
  - [ ] Limites éticos e legislações vigentes (LGPD, Marco Civil, termos de serviço das plataformas).
  - [ ] Boas práticas para um engajamento seguro de Red Team (Escopo e RoE - Rules of Engagement).
* **Notas de fala do apresentador:**
  > *[Inserir guia de fala aqui]*

---

### Bloco 8: Conclusão, Referências & Perguntas
* **Slides correspondentes:** `24 - 25`
* **Pontos-chave a abordar:**
  - [ ] Recapitulação das principais conclusões.
  - [ ] Referências bibliográficas e links úteis.
  - [ ] Espaço aberto para dúvidas da audiência (Q&A).
* **Notas de fala do apresentador:**
  > *[Inserir mensagem final de encerramento]*

---

## 📋 5. Checklist Pré-Apresentação

- [ ] Todos os integrantes sincronizados com a ordem de fala e limites de tempo.
- [ ] Slides revisados e notas de orador preenchidas.
- [ ] Se houver demonstração prática: gravada previamente em vídeo ou testada localmente em ambiente isolado.
- [ ] Servidor de slides testado no navegador.
- [ ] Pontos de transição entre apresentadores alinhados.

---

## 🚀 6. Como Rodar e Visualizar a Apresentação (Reveal.js)

A apresentação foi construída com [Reveal.js](https://revealjs.com/) via CDN, dispensando compilação ou instalação pesada.

### Opção 1: Via Servidor Local Python (Recomendado)
Para ter acesso completo ao **Speaker Notes (Modo Apresentador com tecla `S`)**, execute um servidor local:

```bash
# Na raiz deste repositório:
python3 -m http.server 8000
```
Em seguida, acesse no navegador:
👉 `http://localhost:8000/`

### Opção 2: Via Node / NPX
```bash
npx serve .
```

### Opção 3: Abertura Direta
Abra o arquivo [index.html](file:///home/myoui/T/Projects/IntroReconSeminário/index.html) diretamente no seu navegador preferido (dois cliques). *(Nota: O modo de anotações do orador pode requerer servidor local em alguns navegadores devido a políticas de CORS).*

---

## ⌨️ Atalhos Úteis do Reveal.js Durante a Apresentação

| Tecla | Ação |
| :---: | :--- |
| `Espaço` / `→` | Próximo slide |
| `←` | Slide anterior |
| `S` | **Modo Orador (Speaker View)** com cronômetro e anotações |
| `F` | Tela Cheia (Fullscreen) |
| `O` ou `Esc` | Visão geral dos slides (Overview grid) |
| `B` ou `.` | Pausar / Tela preta (Blackout) |
| `Alt + Clique` | Zoom no elemento clicado |

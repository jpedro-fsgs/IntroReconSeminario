# Handoff Report: Survey de Estrutura e Inventário Técnico de Slides

**Agente:** Explorer 1 (`teamwork_explorer_survey_1`)  
**Data:** 31 de Outubro de 2026  
**Tipo de Handoff:** Hard (Tarefa Concluída)  
**Destinatário:** Parent Orchestrator (`27364f4c-03e8-47bd-a270-e22444d4a0d9`)

---

### 1. Observation

- **Arquivos e Manifesto:**
  - O arquivo `/home/myoui/T/Projects/IntroReconSeminário/slides/manifest.json` lista exatamente 12 arquivos HTML na ordem de apresentação: `00-abertura.html`, `01-conceito-contexto.html`, `02-recon-ativo.html`, `03a-passivo-introducao.html`, `03b-ciclo-osint.html`, `03c-tecnicas-ferramentas.html`, `03c1-ferramentas-detalhes.html`, `03d-fisico-ecossistema.html`, `04-estudos-caso.html`, `05-geosint-osint.html`, `06-opsec-fechamento.html`, `07-referencias-perguntas.html`.
  - A execução de `python3 scripts/build.py --check` e `python3 -m unittest discover -s tests -v` atesta 54 seções `<section class="slide ...">` sequenciais estritamente horizontais (sem slides verticais), cada qual com exatamente um elemento `<aside class="notes">`.
- **Arquitetura de Layout HTML:**
  - Padrão uniforme em todos os 54 slides: contêiner raiz `<div class="slide-inner">`, cabeçalho semântico `<div class="slide-head">` (com `<div class="kicker">` e `<p class="who">`), títulos de nível `h1` ou `h2` (`.cover-title`, `.h-lg`, `.h-md`, `.statement`, `.def-quote`), e corpo estruturado `<div class="slide-body [variante]">`.
  - Interfaces mockadas complexas: terminal interativo do Nmap (`slide 12`), interface com dissecação de pacotes e dump hexadecimal do Wireshark (`slide 13`), card de e-mail de spear-phishing (`slide 15`), boards conceituais das etapas de OSINT (`slides 20–25`), cartões padronizados de ferramentas (`slides 32–37`), e vetores SVG para topologias e grafos (`slides 11, 14, 19, 46, 47, 48, 50`).
- **Inventário Técnico Rigoroso:**
  - **Ferramentas:** Nmap (v7.95), Wireshark, Shodan, Censys, WHOIS, SecurityTrails, VirusTotal, crt.sh, Subfinder, Amass, ExifTool, FOCA, SunCalc, Mapillary, Overpass Turbo, Google Lens, Google Earth, Have I Been Pwned (HIBP), Wayback Machine.
  - **Dados & Redes:** IPs `10.10.14.23` (atacante) e `10.10.14.5` (`alvo.local`), sub-rede `10.10.14.0/24`, portas abertas `22/SSH`, `80/HTTP`, `443/HTTPS`, `3306/MySQL`, `8080/Jetty`, porta filtrada `3389/RDP`; IPs de documentação `192.0.2.10` e `198.51.100.20`; Handshake TCP medido em `0.000203s` e autenticação básica HTTP com credencial `admin:admin` (`YWRtaW46YWRtaW4=`).
  - **Casos Reais:** Twitter/Cinema (tempo real, 21:04); Smart Sampa (G1, 21 out. 2026, 58 mil câmeras, 11 meses de senhas expostas); RSA SecurID (março de 2011, spear-phishing `2021_Recruitment_Plan.xlsx`, exploit zero-day de Flash, comprometimento de seeds); Strava Heatmap (The Guardian, 28 jan. 2018, dados agregados 2015-2017 revelando FOB militar em `34.5°N 69.2°E`).
  - **Metodologias:** MITRE ATT&CK TA0043; Ciclo OSINT em 6 fases (Planejar, Coletar, Processar, Analisar, Disseminar, Feedback); 9 disciplinas INT (HUMINT, GEOINT, FININT, ELINT, IMINT, TECHINT, CYBINT, SOCMINT, SIGINT).
- **Evidências de AI-Slop (Diretrizes `/no-ai-slop`):**
  - Múltiplas ocorrências de antitheses binárias no formato "Não é X, é Y" (ex: slides 07, 09, 16, 18, 44, 47, 50, 52).
  - Títulos do Ciclo OSINT forçados em paralelismo idêntico `[Verbo]: [Frase de impacto]` em 6 slides consecutivos (slides 20–25).
  - Repetição excessiva de palavras-chave corporativas de IA, com destaque para "ecossistema" (slides 02, 08, 40).
  - Instruções prescritivas e artificiais de palco nas notas do orador (ex: slide 44 "Pausa dramática: deixar a frase no telão por alguns segundos").

---

### 2. Logic Chain

1. **Premissa de Integridade e Validação:** Os scripts de build e teste do projeto (`scripts/build.py` e `tests/test_build.py`) exigem exatamente 54 seções horizontais e uma tag `<aside class="notes">` por slide, além da presença dos títulos exatos do grupo de ferramentas nos slides 32 a 37.
2. **Implicação Arquitetural:** Qualquer trabalho de reescrita ou reformulação didática não pode alterar o número de slides, a sequência definida em `manifest.json`, ou a tag `<aside class="notes">`. As alterações devem ser estritamente no conteúdo textual (headings, parágrafos, ledes, listas e corpo das notas).
3. **Preservação de Conteúdo:** O inventário identificou 20 ferramentas formais, parâmetros de execução realistas de Nmap/Wireshark, dados numéricos e fatos históricos de 4 estudos de caso essenciais. Perder ou distorcer qualquer um desses parâmetros enfraqueceria o valor acadêmico/técnico do seminário ofensivo.
4. **Alinhamento com `/no-ai-slop`:** O deck já possui excelente concisão visual e terminologia sólida. O problema central diagnosticado não é falta de informação, mas a presença de padrões de linguagem gerados por IA que engessam o tom (paralelismos forçados, contrastes binários mecânicos e notas do orador excessivamente teatrais). O plano de implementação subsequente deve "dessengessar" essas passagens sem alterar os fatos técnicos subjacentes.

---

### 3. Caveats

- **Escopo Exclusivo de Leitura:** Em conformidade com o papel de Explorer, nenhum arquivo de slide em `slides/`, nem o template `src/presentation.html` ou arquivos de script/estilo foram modificados nesta etapa.
- **Roteiro dos Slides em PDF:** O arquivo `Roteiro dos slides.pdf` na raiz contém 1,5 MB de material de referência prévio. A análise focou nos artefatos de código-fonte reais implementados na pasta `slides/` e no README de governança da equipe.
- **Detecção de AI Slop:** A auditoria textual exaustiva slide a slide com citação entre aspas e recomendação pontual de ajuste será complementada e operacionalizada nos artefatos da equipe técnica de auditoria e planejamento.

---

### 4. Conclusion

O deck de 54 slides está tecnicamente maduro, consistente e funcional em Reveal.js, mas necessita de uma intervenção textual direcionada para remover vícios estilísticos de IA ("slop"), eliminar simetrias robóticas nas manchetes e tornar o tom pedagógico, natural e fluido para a banca avaliadora. Todos os componentes HTML, classes CSS de layout e o inventário completo de parâmetros técnicos a serem preservados estão catalogados e disponíveis para consulta imediata em `analysis.md`.

---

### 5. Verification Method

Para conferir independentemente as observações e conclusões deste relatório:
1. **Conferência de Integridade do Deck:**
   ```bash
   python3 scripts/build.py --check
   python3 -m unittest discover -s tests -v
   ```
   *Critério de validação:* Deve retornar código 0 e passar em todos os 7 testes de integridade.
2. **Inspeção dos Artefatos de Análise Gerados pelo Explorer 1:**
   - Visualizar o relatório completo: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/analysis.md`
   - Inspecionar os dados brutos estruturados: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json`
   - Inspecionar o sumário executivo: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/slide_inventory_summary.json`

# Handoff Report — Explorer 3 (Didática e Comunicação Técnica Dessengessada)

**Agent:** Explorer 3 (`teamwork_explorer_survey_3`)  
**Data:** 2026-10-31  
**Missão:** Análise didática e de comunicação técnica dessengessada dos slides do seminário sobre Reconhecimento e OSINT, aplicando os princípios da skill `/no-ai-slop`.  
**Status:** Hard Handoff (Análise Concluída)

---

## 1. Observation

Durante a investigação exaustiva dos 12 arquivos de slides (`slides/00-abertura.html` a `slides/07-referencias-perguntas.html`), do manifesto (`slides/manifest.json`), do arquivo `README.md` e das diretrizes da skill `/no-ai-slop`, foram observados diretamente os seguintes fatos:

1. **Volume Desbalanceado de Apresentação:**
   - O arquivo `slides/manifest.json` e o `README.md` distribuem os slides entre 5 integrantes: Geovana (03–09, 49–52), Emilio (10–15), Daniel (16–40), João Pedro G. (41–44), João Pedro A. (45–48).
   - O bloco de Daniel (slides 16 a 40) possui **25 slides consecutivos** (`slides/03a-passivo-introducao.html`, `slides/03b-ciclo-osint.html`, `slides/03c-tecnicas-ferramentas.html`, `slides/03c1-ferramentas-detalhes.html`, `slides/03d-fisico-ecossistema.html`). Isso representa 46% da apresentação total (54 slides).

2. **Inconsistência Numérica no Slide 04 (`slides/01-conceito-contexto.html:42-58`):**
   - O slide apresenta simultaneamente: `9h de tela por dia`, `3h em redes sociais` e `116h conectado por semana`.
   - A nota de rodapé afirma: *"Métricas de pesquisas diferentes: use como ordem de grandeza, não como cronômetro."* Contudo, $116 \div 7 = 16,57\text{ horas/dia}$, gerando contradição direta com o valor de 9h/dia.

3. **Anacronismo no Slide 42 (`slides/04-estudos-caso.html:75`):**
   - O cabeçalho estipula *"Caso 01 · 2011 · RSA SecurID"*, mas o anexo da reprodução do e-mail exibe: `📎 2021_Recruitment_Plan.xlsx` (anacronismo de dez anos).

4. **Tripla Repetição do Conceito de Certificate Transparency:**
   - `slides/03b-ciclo-osint.html:69` (Slide 21): *"Certificate Transparency (CT): um log público que permite auditar a emissão de certificados. portal.example.com"*.
   - `slides/03c-tecnicas-ferramentas.html:70` (Slide 28): *"Certificate Transparency (CT) mantém registros públicos para auditar a emissão de certificados digitais."*
   - `slides/03c1-ferramentas-detalhes.html:130` (Slide 35): *"crt.sh: Quais nomes aparecem em registros públicos que permitem auditar a emissão de certificados digitais?"*

5. **Excesso de Ressalvas Defensivas ("AI Slop" e Burocracia Textual):**
   - Nos slides 20 a 25 (`slides/03b-ciclo-osint.html`) e 32 a 37 (`slides/03c1-ferramentas-detalhes.html`), a expressão *"CASO FICTÍCIO"*, *"DADOS FICTÍCIOS"* ou *"observações anteriores não confirmam a situação atual"* aparece repetida em quase todas as caixas de texto e subtítulos, enrijecendo a fluidez verbal da apresentação.

6. **Presença de Fio Narrativo Unificador Não Explorada em Plenitude:**
   - Slide 06 (`slides/01-conceito-contexto.html:187-236`): Post fictício de Marina Sousa (@marina.souza) da *Acme Pagamentos* no novo datacenter.
   - Slide 15 (`slides/02-recon-ativo.html:434-457`): E-mail de phishing simulado usando o domínio `beneficios-acme.com` e a conta `voce@acme.com.br`.
   - Slide 48 (`slides/05-geosint-osint.html:255-278`): Grafo de OSINT correlacionando `@marina.souza`, `marina@acme.com`, `acme.com` e VPN exposta.

---

## 2. Logic Chain

1. **Premissa de Atenção e Carga Cognitiva:** Em apresentações de 45 minutos para bancas acadêmicas, a atenção da audiência decai exponencialmente após 10 a 12 minutos sob o mesmo estímulo visual e mesmo tom de voz.
2. **Da Observação 1:** Daniel apresentando 25 slides consecutivos com estruturas visuais quase idênticas (cartões cinzas, caixas de fluxo horizontal) induz à fadiga e perda de foco do público na metade do seminário.
3. **Da Observação 2 e 3:** Discrepâncias matemáticas (9h/dia vs 116h/semana) e anacronismos históricos (2021 em caso de 2011) são imediatamente percebidos por avaliadores rigorosos, distraindo do mérito do conteúdo e enfraquecendo a credibilidade do grupo.
4. **Da Observação 4:** A tripla repetição de CT Logs sem diferenciação de ângulo (mecanismo vs. dado vs. ferramenta) desperdiça tempo precioso de fala e transmite a sensação de conteúdo inflado.
5. **Da Observação 5:** De acordo com a skill `/no-ai-slop`, rodeios protocolares (*"é importante ressaltar que..."*, *"em um cenário fictício..."*) e nominalizações abstratas roubam dinamismo do texto. A intenção de ser ético e responsável foi expressa como burocracia textual defensiva.
6. **Da Observação 6:** A narrativa transversal da Marina Sousa e da Acme Pagamentos é o recurso didático de maior potencial pedagógico do projeto. Ela transforma conceitos dispersos em uma história de causa e efeito compreensível em tempo real.

---

## 3. Caveats

- A análise ateve-se estritamente à perspectiva didática, pedagógica e de comunicação técnica falada/visual, sem executar alterações nos arquivos `.html`, `.css` ou `.js`.
- O tempo de fala real depende do ensaio presencial dos alunos; as estimativas de 45 minutos baseiam-se em uma cadência média de apresentação técnica (1 a 1,5 minuto por slide dinâmico, 20 a 30 segundos por slide de detalhe de ciclo).
- As propostas preservam 100% das ferramentas, protocolos, métricas e normas éticas originais, conforme estipulado nos critérios de aceitação.

---

## 4. Conclusion

A apresentação possui altíssimo valor visual e conceitual, mas necessita de uma intervenção de desengessamento didático focada em:
1. **Unificação da Narrativa (Fio Condutor Acme/Marina):** Amarrar explicitamente os slides 06, 15 e 48 como uma única investigação forense continuada.
2. **Eliminação do Ruído Burocrático:** Substituir nominalizações passivas por verbos diretos de ação e consolidar as ressalvas legais e éticas nos rodapés e notas, deixando o corpo dos slides focado na mecânica operacional.
3. **Agilização do Bloco 03:** Tratar os slides 20 a 25 como um passo a passo ágil e cinematográfico, diferenciando a explicação teórica de Certificate Transparency (slide 28) da aplicação prática via `crt.sh` (slide 35).
4. **Correção de Precisão Concreta:** Alinhar as métricas do slide 04 para um dado consistente (9h de tela diárias, 3h em redes sociais) e corrigir o nome do anexo do slide 42 para 2011.

---

## 5. Verification Method

Para verificar independentemente as análises e constatações deste relatório:
1. **Verificação de Textos e Trechos Citados:**
   - Consultar `slides/01-conceito-contexto.html` (linhas 42–58) via `view_file` para constatar as métricas de 9h, 3h e 116h.
   - Consultar `slides/04-estudos-caso.html` (linha 75) para constatar o nome `2021_Recruitment_Plan.xlsx` no caso RSA de 2011.
   - Consultar `slides/03b-ciclo-osint.html`, `slides/03c-tecnicas-ferramentas.html` e `slides/03c1-ferramentas-detalhes.html` para constatar as menções repetidas a Certificate Transparency.
2. **Verificação de Regras da Skill:**
   - Conferir `/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md` nos itens "Make verbs do the work", "Be concrete and specific" e "Words/Patterns to cut".
3. **Verificação de Integridade dos Slides:**
   - Executar `python3 scripts/build.py --check` e `python3 -m unittest discover -s tests -v` para certificar que nenhum arquivo da pasta `slides/` foi modificado nesta fase exploratória.

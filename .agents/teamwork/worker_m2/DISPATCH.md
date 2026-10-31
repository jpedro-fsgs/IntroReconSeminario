## 2026-10-31T02:36:43Z
Você é o Worker 2 (Especialista em Comunicação Técnica e Elaboração do Plano de Implementação Didático).
Seu diretório de trabalho exclusivo é: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m2/`.
Você é o PROPRIETÁRIO EXCLUSIVO do arquivo: `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md`.
ATENÇÃO CRÍTICA: Você NUNCA deve alterar arquivos fonte na pasta `slides/`. O escopo é estritamente a elaboração do plano de implementação e reformulação didática.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Insumos obrigatórios:
1. Requisitos originais: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/ORIGINAL_REQUEST.md`.
2. Projeto e contratos: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/PROJECT.md`.
3. Relatório oficial de auditoria de AI Slop: `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md`.
4. Relatórios analíticos prévios:
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/analysis.md` (Inventário técnico exaustivo)
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_2/analysis.md` (Catálogo de padrões linguísticos)
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_3/analysis.md` (Diagnóstico pedagógico, modelos mentais e anacronismos)
5. Skill `/no-ai-slop`: `/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md`.

Sua missão (Milestone M2):
Elaborar o plano mestre `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md` estruturado slide a slide e seção a seção.

Estrutura obrigatória do documento:
1. **Sumário Executivo e Diretrizes Pedagógicas Globais**:
   - Princípios de "dessengessamento": linguagem natural, direta, substantiva, transformando fórmulas negativas/passivas ("Recon não é invadir...") em declarações afirmativas causais e técnicas.
   - Resolução da sobrecarga cognitiva do bloco de Daniel (25 slides seguidos, 16 a 40): variação de ritmo, quebra de gabaritos clônicos e agilização.
   - Costura do fio narrativo condutor contínuo: o caso da analista Marina Sousa e Acme Pagamentos nos slides 06, 15 e 48.
   - Resolução de dados conflitantes: harmonização do slide 04 (9h de tela/dia vs 116h/semana) e correção do anacronismo do slide 42 (RSA de 2011 com arquivo `2021_Recruitment_Plan.xlsx` -> `2011_Recruitment_Plan.xlsx`).
   - Diferenciação funcional da tríade de Certificate Transparency (slide 21 conceito, slide 28 mecânica técnica de logs, slide 35 ferramenta prática `crt.sh`).
2. **Plano Detalhado Slide a Slide (cobrindo TODOS os 54 slides de forma exaustiva)**:
   Para CADA UM dos 54 slides, incluir estritamente:
   - **Cabeçalho**: Número do slide (01 a 54), Arquivo correspondente (`slides/*.html`), Apresentador responsável e Título original.
   - **Objetivo Didático Central**: O que o público deve aprender e reter neste slide.
   - **Diagnóstico de AI Slop & Engessamento**: Padrões detectados em `AUDITORIA_AI_SLOP.md` e problemas de legibilidade/cadência.
   - **Proposta de Reformulação Didática ("Dessengessada")**:
     * Proposta de Título / Manchete (sem fórmulas robóticas ou colon reveals forçados).
     * Proposta de Corpo de Texto e Tópicos (redação direta, ativa, eliminando palavras banidas como `acionável`, travessões excessivos e disclaimers defensivos repetitivos).
     * Modelo Mental / Metáfora Funcional aplicada (ex: "Vitrine da Loja", "Bater e correr no SYN scan", "Diário Oficial do SSL", "Trilha de Formigas no Strava", etc.).
     * Roteiro e Tom do Apresentador (orientações para fala falada, descontraída mas com rigor técnico de graduação, eliminando rubricas teatrais artificiais como "pausa dramática").
   - **Fatos Técnicos Preservados**: Checklist explícito de ferramentas, parâmetros, portas, IPs, comandos, métricas, normas e estudos de caso que são mantidos integralmente.
3. **Matriz de Rastreabilidade e Preservação Técnica**:
   - Tabela consolidando todas as ferramentas, métricas e casos demonstrando 100% de preservação.
4. **Verificação de Não Alteração dos Slides**:
   - Certificação explícita de que os arquivos em `slides/` permaneceram inalterados.

Ao finalizar:
1. Execute `python3 scripts/build.py --check` e `python3 -m unittest discover -s tests -v` para certificar que nenhum arquivo da pasta `slides/` foi modificado.
2. Escreva o relatório protocolar em `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m2/handoff.md` (Observation, Logic Chain, Caveats, Conclusion, Verification Method).
3. Notifique-me via `send_message`.

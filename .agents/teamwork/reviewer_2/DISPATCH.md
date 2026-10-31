## 2026-10-31T02:49:19Z
Sender: 27364f4c-03e8-47bd-a270-e22444d4a0d9
Priority: MESSAGE_PRIORITY_HIGH

Você é o Reviewer 2 (Revisor Independente do Plano de Implementação Didático).
Seu diretório de trabalho exclusivo é: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/reviewer_2/`.
Você NUNCA deve alterar arquivos fonte na pasta `slides/`.

Insumos obrigatórios:
1. Requisitos: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/ORIGINAL_REQUEST.md`.
2. Projeto: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/PROJECT.md`.
3. Skill `/no-ai-slop`: `/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md`.
4. Artefato a revisar: `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md`.
5. Handoff do Worker 2: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m2/handoff.md`.
6. Inventário técnico prévio: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/analysis.md`.

Sua missão:
Examinar criticamente `PLANO_IMPLEMENTACAO_DIDATICO.md` contra todos os critérios de aceitação de R2:
- Detalhamento exaustivo slide a slide de todos os 54 slides da apresentação.
- Eficácia didática das intervenções (linguagem natural, afirmativa, eliminação de clichês e tom professoral/robótico, uso de modelos mentais e metáforas funcionais).
- Preservação integral de 100% dos fatos técnicos, ferramentas, portas, IPs, parâmetros, estudos de caso e métricas originais (sem simplificar ou omitir dados).
- Verificação de resolução do conflito de tempo de tela (slide 04) e anacronismo (slide 42).
- Garantia de que NENHUMA alteração direta foi aplicada aos arquivos em `slides/`.
- Execução de testes de conformidade (`python3 scripts/build.py --check` e `python3 -m unittest discover -s tests -v`).

Veredito obrigatório:
No seu relatório de handoff (`/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/reviewer_2/handoff.md`), emita explicitamente seu veredito: `APPROVE` ou `REQUEST_CHANGES`, com justificativa detalhada. Notifique-me via `send_message`.

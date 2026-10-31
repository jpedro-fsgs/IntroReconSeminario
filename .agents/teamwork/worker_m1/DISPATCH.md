## 2026-10-31T02:28:00Z
Você é o Worker 1 (Especialista em Auditoria Textual de AI Slop).
Seu diretório de trabalho exclusivo é: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m1/`.
Você é o PROPRIETÁRIO EXCLUSIVO do arquivo: `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md`.
ATENÇÃO: Você NUNCA deve alterar arquivos fonte na pasta `slides/`. O escopo é estritamente a geração do relatório de auditoria e análise.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Insumos obrigatórios:
1. Requisitos originais: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/ORIGINAL_REQUEST.md`.
2. Projeto e contratos: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/PROJECT.md`.
3. Diretrizes da skill `/no-ai-slop`: `/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md`.
4. Relatórios analíticos prévios:
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/analysis.md` (Inventário técnico)
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_2/analysis.md` (Auditoria linguística profunda com dezenas de trechos verbatim)
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_3/analysis.md` (Diagnóstico didático)

Sua missão (Milestone M1):
Escrever o relatório exaustivo e profissional `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md`.
Critérios de Aceitação Obrigatórios (R1):
- Cobrir TODOS os 12 arquivos HTML contidos na pasta `slides/` e todos os 54 slides.
- Para cada ocorrência apontada, citar expressamente:
  a) Arquivo e número do slide correspondente.
  b) Trecho original exato entre aspas.
  c) Padrão nomeado exato da skill `/no-ai-slop` (ex: Binary contrasts, Colon reveals, Superficial analysis, Importance puffery, Interpretive metadiscourse, Weasel attribution, Robotic rhythm, Dramatic fragmentation, Banned words, Em dashes, Throat-clearing openers, etc.).
  d) Recomendação clara e objetiva de ajuste/correção.
- Não utilizar pontuações arbitrárias de detectores automatizados externos; fundamentar-se estritamente nas evidências textuais da skill `/no-ai-slop`.
- Incluir sumário executivo com a distribuição quantitativa dos padrões encontrados e mapa de calor dos blocos mais afetados.

Ao finalizar:
1. Execute `python3 scripts/build.py --check` e `python3 -m unittest discover -s tests -v` no terminal para certificar que nenhum arquivo de `slides/` foi corrompido ou alterado.
2. Escreva seu relatório protocolar em `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m1/handoff.md` (Observation, Logic Chain, Caveats, Conclusion, Verification Method).
3. Notifique-me via `send_message`.

## 2026-10-31T02:49:27Z
Você é o Challenger 1 (Verificador Empírico e Adversarial da Auditoria de AI Slop).
Seu diretório de trabalho exclusivo é: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/challenger_1/`.
Você NUNCA deve alterar arquivos fonte na pasta `slides/`.

Insumos:
1. Requisitos: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/ORIGINAL_REQUEST.md`.
2. Skill `/no-ai-slop`: `/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md`.
3. Relatório a auditar: `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md`.
4. Slides originais: `/home/myoui/T/Projects/IntroReconSeminário/slides/`.

Sua missão adversarial:
Desenvolver e executar scripts de validação empírica para estressar e verificar a exatidão factual de `AUDITORIA_AI_SLOP.md`:
1. Validação de Citações: Escreva um script (ex: Python) que leia cada trecho entre aspas listado no relatório e verifique se ele existe literalmente no respectivo arquivo HTML da pasta `slides/`.
2. Validação de Cobertura: Verifique se todos os 54 slides e todos os 12 arquivos HTML possuem seções dedicadas no relatório.
3. Validação de Padrões: Verifique se cada padrão classificado pertence formalmente ao vocabulário da skill `/no-ai-slop`.
4. Ausência de Scores: Verifique programmaticamente que termos como "GPTZero", "AI score", "% AI" ou pontuações inventadas não aparecem no relatório.
5. Verificação de Integridade: Confirme que `git status --short slides/` está vazio e `python3 scripts/build.py --check` passa.

Veredito obrigatório:
No seu relatório de handoff (`/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/challenger_1/handoff.md`), emita explicitamente seu veredito: `APPROVE` ou `REQUEST_CHANGES`, detalhando os resultados empíricos dos seus testes. Notifique-me via `send_message`.

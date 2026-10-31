## 2026-10-31T02:49:45Z
Você é o Forensic Auditor (Auditor Forense de Integridade).
Seu diretório de trabalho exclusivo é: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/auditor_1/`.
Você NUNCA deve alterar arquivos fonte na pasta `slides/`.

Insumos:
1. Requisitos: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/ORIGINAL_REQUEST.md`.
2. Projeto: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/PROJECT.md`.
3. Entregáveis do projeto:
   - `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md`
   - `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md`
4. Handoffs de Worker 1 e Worker 2:
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m1/handoff.md`
   - `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m2/handoff.md`
5. Código fonte da apresentação: `/home/myoui/T/Projects/IntroReconSeminário/slides/`.

Sua missão de auditoria forense:
Executar verificações forenses rigorosas e independentes de integridade:
1. Inalterabilidade da Apresentação: Verificar através do histórico do Git e status de arquivos (`git diff`, `git status --short slides/`) se algum arquivo em `slides/` foi modificado, corrompido, adulterado ou excluído. Qualquer alteração em `slides/` constitui VIOLAÇÃO DE INTEGRIDADE.
2. Autenticidade do Trabalho: Auditar se os relatórios `AUDITORIA_AI_SLOP.md` e `PLANO_IMPLEMENTACAO_DIDATICO.md` representam trabalho genuíno, substancial e exaustivo, ou se contêm atalhos fraudulentos, mocks vazios, stubs superficiais, ou repetição mecânica de texto sem substância.
3. Não Utilização de Detectores Arbitrários: Verificar se há uso espúrio ou inventado de detectores de IA automatizados externos (GPTZero, ZeroGPT, etc.).
4. Preservação Factual Completa: Auditar se os dados técnicos foram mantidos com precisão cirúrgica ou se houve degradação do valor técnico.
5. Verificação da Suíte de Build e Testes: Executar `python3 scripts/build.py --check` e `python3 -m unittest discover -s tests -v`.

Veredito obrigatório:
No seu relatório de handoff (`/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/auditor_1/handoff.md`), emita o veredito formal: `CLEAN` ou `INTEGRITY VIOLATION`.
Se detectar qualquer violação, forneça evidências irrefutáveis. Notifique-me via `send_message`.

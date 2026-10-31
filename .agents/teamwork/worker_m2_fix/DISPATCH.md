## 2026-10-31T02:59:14Z
Você é o Worker 4 (Especialista em Refinamento e Preservação Técnica do Plano Didático).
Seu diretório de trabalho exclusivo é: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m2_fix/`.
Você é o PROPRIETÁRIO EXCLUSIVO do arquivo: `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md`.
ATENÇÃO: Você NUNCA deve alterar arquivos fonte na pasta `slides/`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Insumos de correção:
- Relatório de Challenger 2: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/challenger_2/handoff.md`
- Relatório de Reviewer 2: `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/reviewer_2/handoff.md`
- Arquivo a retificar: `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md`
- Código dos slides: `/home/myoui/T/Projects/IntroReconSeminário/slides/`

Sua missão:
Executar pontual e cirurgicamente em `PLANO_IMPLEMENTACAO_DIDATICO.md` os seguintes ajustes requeridos pelo Challenger 2:
1. **Slide 43 (Caso Strava Heatmap):**
   - Adicionar expressamente as coordenadas geográficas da base militar no Afeganistão: `34.5°N 69.2°E` tanto na proposta de corpo de texto/tópicos quanto no checklist de *Fatos Técnicos Preservados* e na Tabela 3.3.
2. **Slide 46 (Demonstração GEOSINT):**
   - Adicionar as coordenadas geográficas exatas `32.89°S 68.84°W` (Mendoza, Argentina) e reincluir formalmente as ferramentas `Google Lens`, `Mapillary` e `Overpass` (junto a `SunCalc`) no corpo de tópicos e no checklist de *Fatos Técnicos Preservados*, atualizando também as Tabelas 3.1 e 3.3.
3. **Slide 18 (Conceito de OSINT):**
   - Adicionar explicitamente as ferramentas/bases `Wayback Machine` (arquivo histórico web) e `Have I Been Pwned / HIBP` (consulta a credenciais vazadas) no corpo de tópicos propostos e no checklist de *Fatos Técnicos Preservados*.
4. **Slides 14 e 51 (Modelos Mentais):**
   - Eliminar a fórmula residual "não é X, é Y", tornando as metáforas puramente afirmativas e funcionais:
     * *Slide 14:* "HTTP Basic Authentication opera como um envelope transparente de celofane: apenas codifica caracteres em base64 para transporte, permitindo que qualquer analisador na rede recupere a senha em texto claro."
     * *Slide 51:* "A higiene cibernética opera como lavar as mãos com sabão: hábitos rotineiros e simples repetidos diariamente que evitam a maioria dos riscos operacionais."
5. Manter integralmente a estrutura de todos os 54 slides e a alta qualidade pedagógica do plano.
6. Executar `python3 scripts/build.py --check` e `python3 -m unittest discover tests -v` para certificar que nenhum arquivo da pasta `slides/` foi modificado.
7. Escrever o relatório protocolar em `/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/worker_m2_fix/handoff.md` e me notificar via `send_message`.

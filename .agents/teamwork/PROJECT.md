# Project: Auditoria de AI Slop e Plano de Implementação Didático para Seminário de Reconhecimento e OSINT

## Architecture
- **Domínio**: Análise textual e pedagógica de apresentação técnica em Reveal.js (`slides/`).
- **Fontes de Verdade**:
  - `slides/manifest.json` e 12 arquivos HTML (54 slides sequenciais com `<aside class="notes">`).
  - `/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md` (Catálogo de padrões, palavras proibidas e princípios de edição).
  - Relatórios dos Explorers 1, 2 e 3 (`.agents/teamwork/teamwork_explorer_survey_*/analysis.md`).
  - `scripts/build.py` e `tests/test_build.py` (Suíte de validação e integridade).
- **Entregáveis Finais**:
  - `AUDITORIA_AI_SLOP.md` (Relatório exaustivo de auditoria de AI Slop conforme R1 e critérios de aceitação).
  - `PLANO_IMPLEMENTACAO_DIDATICO.md` (Plano estruturado slide a slide e seção a seção conforme R2 e critérios de aceitação).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| F01 | Mapeamento estrutural dos slides | Inventário dos 12 arquivos HTML, 54 seções e manifesto | M1 | Survey (Explorer 1) |
| F02 | Auditoria Bloco 01 (Intro & Contexto) | Identificação de padrões nos slides 01 a 09 (`00`, `01`) | M1 | Survey (Explorer 2) |
| F03 | Auditoria Bloco 02 (Recon Ativo) | Identificação de padrões nos slides 10 a 15 (`02`) | M1 | Survey (Explorer 2) |
| F04 | Auditoria Bloco 03A/B (Passivo & Ciclo) | Identificação de padrões nos slides 16 a 25 (`03a`, `03b`) | M1 | Survey (Explorer 2) |
| F05 | Auditoria Bloco 03C (Técnicas & Ferramentas) | Identificação de padrões nos slides 26 a 37 (`03c`, `03c1`) | M1 | Survey (Explorer 2) |
| F06 | Auditoria Bloco 04 & GEOSINT | Identificação de padrões nos slides 38 a 48 (`03d`, `04`, `05`) | M1 | Survey (Explorer 2) |
| F07 | Auditoria Bloco Fechamento & OpSec | Identificação de padrões nos slides 49 a 54 (`06`, `07`) | M1 | Survey (Explorer 2) |
| F08 | Publicação do Relatório `AUDITORIA_AI_SLOP.md` | Documento estruturado com citações exatas, padrões e recomendações | M1 | R1 |
| F09 | Plano Didático Bloco 01 (Intro & Contexto) | Resolução de métricas conflitantes (slide 04) e antíteses mecânicas | M2 | Survey (Explorer 3) |
| F10 | Plano Didático Bloco 02 (Recon Ativo) | Metáforas funcionais e eliminação de retórica artificial | M2 | Survey (Explorer 3) |
| F11 | Plano Didático Bloco 03 (Passivo, Ciclo, Ferramentas) | Resolução de redundância de CT logs e dinamização da cadência do Daniel | M2 | Survey (Explorer 3) |
| F12 | Plano Didático Bloco 04 (Casos & GEOSINT) | Correção do anacronismo RSA (2011) e costura do fio narrativo Acme | M2 | Survey (Explorer 3) |
| F13 | Plano Didático Bloco Fechamento (OpSec) | Afirmações diretas funcionais e preparação da banca | M2 | Survey (Explorer 3) |
| F14 | Publicação de `PLANO_IMPLEMENTACAO_DIDATICO.md` | Plano slide a slide preservando 100% dos dados técnicos | M2 | R2 |
| F15 | Validação E2E, Revisão Crítica e Auditoria Forense | Verificação estrita de critérios de aceitação e integridade | M3 | Verificação |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Auditoria Exaustiva de AI Slop | Features F01 a F08: Conduzir a auditoria completa de todos os 54 slides e compilar `AUDITORIA_AI_SLOP.md` | Survey | DONE |
| M2 | Plano de Implementação Didático e Dessengessado | Features F09 a F14: Elaborar o plano detalhado por slide em `PLANO_IMPLEMENTACAO_DIDATICO.md` | M1 | DONE |
| M3 | Revisão por Pares, Desafio e Auditoria de Integridade | Feature F15: Reviewers, Challengers e Auditoria Forense independente | M1, M2 | DONE |

## Interface Contracts
### Survey ↔ Milestone 1 (Auditoria)
- Insumos: `detailed_slides.json`, `analysis.md` dos Explorers 1, 2 e 3.
- Saída esperada: Arquivo `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md`.
- Formato obrigatório: Tabela e detalhamento por slide contendo:
  1. Arquivo e número do slide.
  2. Trecho original exato entre aspas.
  3. Padrão nomeado da skill `/no-ai-slop`.
  4. Recomendação de ajuste direto.
  5. Proibição absoluta de notas ou percentuais de detectores automatizados externos.

### Milestone 1 ↔ Milestone 2 (Plano Didático)
- Insumos: `AUDITORIA_AI_SLOP.md` e diagnósticos do Explorer 3.
- Saída esperada: Arquivo `/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md`.
- Formato obrigatório: Estruturado por bloco e slide, contendo para cada um:
  1. Identificação do Slide (Número, Título, Arquivo, Apresentador).
  2. Objetivo Didático Central (O que a audiência deve compreender).
  3. Diagnóstico de Engessamento / Padrão AI Slop Identificado.
  4. Proposta de Reformulação Didática ("Dessengessada"):
     - Proposta de Título / Subtítulo / Manchete.
     - Proposta de Corpo de Texto e Tópicos.
     - Modelo Mental / Metáfora Funcional aplicada.
     - Proposta de Notas do Orador (fala natural e fluida para o estudante).
  5. Fatos Técnicos Preservados (checklist explícito de ferramentas, IPs, portas, casos e dados).
  6. Garantia de Inalterabilidade dos Arquivos (nenhuma edição direta em `slides/`).

### Milestone 2 ↔ Milestone 3 (Validação & Auditoria)
- Insumos: `AUDITORIA_AI_SLOP.md` e `PLANO_IMPLEMENTACAO_DIDATICO.md`.
- Critérios de Aceitação:
  - 100% dos 54 slides cobertos em ambos os documentos.
  - Zero arquivos em `slides/` alterados (`git status` limpo em `slides/`).
  - Suíte de validação (`python3 scripts/build.py --check` e `python3 -m unittest discover -s tests -v`) com 100% de sucesso.
  - Ausência total de notas arbitrárias de detectores.
  - Verificação forense de integridade pelo `teamwork_auditor`.

## Code Layout
- `.agents/teamwork/`: Metadados da equipe de orquestração, relatórios de handoff e planos de trabalho.
- `AUDITORIA_AI_SLOP.md`: Relatório executivo e detalhado de auditoria de AI Slop em todo o deck.
- `PLANO_IMPLEMENTACAO_DIDATICO.md`: Plano mestre de implementação pedagógica e reformulação didática.
- `slides/*.html`: Arquivos de slides originais (INTOCÁVEIS nesta etapa).

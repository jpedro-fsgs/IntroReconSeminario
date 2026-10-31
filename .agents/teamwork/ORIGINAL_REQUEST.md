# Original User Request

## Approved Task Prompt — 2026-10-31T02:17:00Z

Análise e identificação de texto com padrões de "AI slop" em todos os slides da apresentação (`slides/`) com base na skill `/no-ai-slop`, e criação de um plano detalhado de implementação para adequar os textos tornando-os didáticos, naturais ("dessengessados") e de fácil interpretação, mantendo o conteúdo técnico e a informatividade.

Working directory: /home/myoui/T/Projects/IntroReconSeminário
Integrity mode: development

## Verification Resources
- Diretrizes, catálogo de padrões e regras da skill `/no-ai-slop` (`/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md`).

## Requirements

### R1. Auditoria e Identificação de AI Slop nos Slides
Realizar uma auditoria textual completa de todos os slides da apresentação na pasta `slides/`, identificando e catalogando ocorrências de padrões de AI slop conforme definidos na skill `/no-ai-slop`. Para cada ocorrência identificada, registrar o arquivo, o trecho original exato, o padrão correspondente da skill e a recomendação de correção.

### R2. Plano de Implementação Didático e Dessengessado
Elaborar um plano detalhado de implementação estruturado por slide e seção para adequar a linguagem dos slides, tornando o texto didático, fluido e natural ("dessengessado"), garantindo a preservação integral de todo o conteúdo técnico, dados, fatos e informatividade original, sem modificar diretamente os arquivos da apresentação nesta etapa.

## Acceptance Criteria

### Auditoria de AI Slop
- [ ] O relatório de auditoria cobre todos os arquivos HTML contidos na pasta `slides/`.
- [ ] Cada ocorrência apontada cita o arquivo, o trecho original exato entre aspas, o padrão nomeado da skill `/no-ai-slop` e a recomendação de ajuste.
- [ ] O relatório não utiliza pontuações arbitrárias de detectores automatizados externos, fundamentando-se nas evidências textuais da skill `/no-ai-slop`.

### Plano de Implementação Didático
- [ ] O plano detalha as intervenções propostas por slide, com orientações de reescrita ou reformulação que tornem o conteúdo didático e de fácil interpretação.
- [ ] O plano preserva integralmente os fatos técnicos, dados estatísticos, nomes de ferramentas, estudos de caso e conceitos presentes nos slides originais.
- [ ] Nenhuma alteração direta é aplicada aos arquivos da pasta `slides/` (o escopo é estritamente a análise e o plano de implementação).

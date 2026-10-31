# Handoff Report: Revisão Independente e Auditoria Adversarial (M1)

**Data:** 31 de Outubro de 2026  
**Agente:** Reviewer 1 (`reviewer_1` — Revisor Independente e Crítico Adversarial de AI Slop)  
**Parent / Orquestrador:** `27364f4c-03e8-47bd-a270-e22444d4a0d9`  
**Artefato Avaliado:** `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md`  
**Veredito Formal:** **REQUEST_CHANGES**

---

## 1. Observation

1. **Cobertura Estrutural e Arquivos:**
   - O repositório contém 12 arquivos HTML listados em `slides/manifest.json`.
   - A contagem de tags `<section>` via script Python confirmou exatamente 54 slides no total:
     `00-abertura.html` (2), `01-conceito-contexto.html` (7), `02-recon-ativo.html` (6), `03a-passivo-introducao.html` (3), `03b-ciclo-osint.html` (7), `03c-tecnicas-ferramentas.html` (6), `03c1-ferramentas-detalhes.html` (6), `03d-fisico-ecossistema.html` (3), `04-estudos-caso.html` (4), `05-geosint-osint.html` (4), `06-opsec-fechamento.html` (4), `07-referencias-perguntas.html` (2).
   - O documento `AUDITORIA_AI_SLOP.md` cobre nominalmente todos os 54 slides (Slides 01 a 19 individuais, 20 a 25 agrupados com subitens por slide, 26 individual, 27 a 30 com subitens por slide, 31 individual, 32 a 37 com subitens por slide, 38 a 54 individuais).

2. **Integridade de Código e Testes:**
   - Comando `git status --porcelain slides/` executado com código de saída 0 e saída vazia (zero modificações na pasta de slides).
   - Comando `python3 scripts/build.py --check`:
     `index.html está atualizado e os blocos são válidos.`
   - Comando `python3 -m unittest discover -s tests -v`:
     7 testes executados com status `OK` (0.107s).

3. **Inconsistência Aritmética na Tabela Estatística (Seção 1.1 e 1.2):**
   - Na linha 20 de `AUDITORIA_AI_SLOP.md`:
     `"A auditoria identificou **152 ocorrências catalogadas** distribuídas por todo o deck..."`
   - Na tabela das linhas 28 a 42 de `AUDITORIA_AI_SLOP.md`:
     - As contagens por categoria somam: `29 + 22 + 18 + 15 + 14 + 38 + 12 + 8 + 8 + 4 + 5 + 7 = 180`.
     - A linha de total declara: `| **TOTAL DE OCORRÊNCIAS CATALOGADAS** | **180** | **100%** |`.
     - Porém, cada porcentagem individual foi calculada sobre 152:
       `29 / 152 = 19,1%`, `22 / 152 = 14,5%`, `18 / 152 = 11,8%`, `15 / 152 = 9,9%`, `14 / 152 = 9,2%`, `38 / 152 = 25,0%`, `12 / 152 = 7,9%`, `8 / 152 = 5,3%`, `8 / 152 = 5,3%`, `4 / 152 = 2,6%`, `5 / 152 = 3,3%`, `7 / 152 = 4,6%`.
     - A soma das porcentagens da coluna totaliza **118,5%**.

4. **Inexatidões Textuais nas Citações entre Aspas:**
   - **Slide 07 (Linha 231):** Cita-se `Trecho Citado: "Twitter · agora — tempo real" (Linha 271)` e classifica-se como `Em dash as rhythmic crutch`. Em `slides/01-conceito-contexto.html:270-271`, o código original é:
     ```html
     <div class="tw-user"><b>@....</b><span>Twitter · agora</span></div>
     <span class="tw-live"><i></i>tempo real</span>
     ```
     Não existe caractere de travessão (`—`) no código fonte. O travessão foi inserido na citação pelo auditor e classificado como desvio.
   - **Slide 12 (Linhas 321–323):** Cita-se `"-oA — gera três formatos de saída..." (Linha 143) e "-p- — varre todas as 65.535 portas..." (Linha 153)` e classifica-se como `Em dashes decorativos como separadores`. Nos arquivos fonte `slides/02-recon-ativo.html:143` (`<div class="window-body">`) e `:153` (`<div class="head">`), esse texto inexiste. O texto original é a nota da Linha 215: `-sS (SYN), -sV (versões), -p- (todas as portas), -oA (salvar em três formatos)`. O auditor parafraseou o texto criando citações inexistentes com travessões.
   - **Slide 17 (Linha 406):** Cita-se `Trecho Citado: "OSINT, fontes abertas e o ecossistema" (Linha 48)`. No arquivo `slides/03a-passivo-introducao.html`, a linha 48 é `</div>` e a palavra `ecossistema` inexiste no arquivo. O trecho literal reside em `slides/00-abertura.html:95` (Slide 02).

5. **Aderência às Diretrizes e Recomendações:**
   - 96 de 103 trechos verificados coincidem 100% de forma literal com o código dos slides.
   - Ausência absoluta de detectores automatizados externos (GPTZero, CopyLeaks, etc.) para emissão de scores.
   - As 100 recomendações didáticas são construtivas, aplicáveis e preservam 100% dos dados técnicos (IPs, portas, flags Nmap, sintaxe Wireshark, casos reais e 9 disciplinas INT).

---

## 2. Logic Chain

1. **Premissa 1 (R1 & Acceptance Criteria):** O requisito R1 e os critérios de aceitação estipulam expressamente que:
   - "Cada ocorrência apontada cita o arquivo, o trecho original exato entre aspas, o padrão nomeado da skill `/no-ai-slop` e a recomendação de ajuste."
   - "O relatório não utiliza pontuações arbitrárias de detectores automatizados externos."
2. **Premissa 2 (Evidência de Auditoria Forense):** A auditoria adversarial confirmou que nos Slides 07 e 12 as citações entre aspas não correspondem textualmente aos arquivos originais, contendo travessões interpolados pelo próprio auditor que foram subsequentemente penalizados como infrações estilísticas.
3. **Premissa 3 (Evidência Aritmética):** A tabela do sumário executivo apresenta erro formal de cálculo, dividindo valores pela base preliminar de 152 em vez do total consolidado de 180, resultando em uma soma de 118,5%.
4. **Premissa 4 (Integridade Global vs. Correções Necessárias):** Não foram detectadas violações intencionais de integridade (não há trapaças ou fachadas, os testes reais passaram e o trabalho tem substância sólida). Todavia, as falhas identificadas nos passos 2 e 3 constituem não conformidades objetivas frente aos critérios de aceitação de R1.
5. **Conclusão Lógica:** O trabalho não pode ser aprovado tacitamente no estado atual, impondo o veredito formal de **REQUEST_CHANGES** com instruções pontuais e circunscritas para correção imediata pelo Worker 1 / Orquestrador.

---

## 3. Caveats

- A auditoria não exige refazer o relatório de 921 linhas, pois 96% das citações e 100% das recomendações pedagógicas e técnicas estão corretas e válidas.
- A contagem de 38 travessões no conteúdo (`slides/*.html`) foi verificada e validada como precisa, desconsiderando os 8 travessões de normas bibliográficas no Slide 53 e os 2 travessões em títulos de janelas de terminal.
- Não foram modificados arquivos pelo Revisor, em obediência estrita à restrição de perfil `review-only`.

---

## 4. Conclusion

**Veredito:** **REQUEST_CHANGES**

O artefato `/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md` é aprovável mediante a execução das seguintes correções pontuais:
1. **Recalcular a coluna de porcentagens na Tabela da Seção 1.2** com base no denominador 180 (totalizando 100,0%), e corrigir a redação da Linha 20 de "152 ocorrências" para "180 ocorrências catalogadas".
2. **Sanear a citação do Slide 07 (Linha 231):** remover o travessão artificial e citar literalmente os spans de `01-conceito-contexto.html:270-271`.
3. **Sanear a citação do Slide 12 (Linhas 321–323):** citar textualmente a nota da Linha 215 (`-sS (SYN), -sV (versões)...`) sem os travessões interpolados.
4. **Realocar a citação do Slide 17 (Linha 406):** transferir a referência de `"OSINT, fontes abertas e o ecossistema"` para o Slide 02 (`00-abertura.html:95`), onde ela efetivamente ocorre.

---

## 5. Verification Method

Para reproduzir e verificar independentemente os achados deste relatório:
1. **Verificação da Inconsistência Matemática da Tabela:**
   ```bash
   python3 -c '
   counts = [29, 22, 18, 15, 14, 38, 12, 8, 8, 4, 5, 7]
   pcts_in_table = [19.1, 14.5, 11.8, 9.9, 9.2, 25.0, 7.9, 5.3, 5.3, 2.6, 3.3, 4.6]
   print("Soma das contagens:", sum(counts))
   print("Soma das porcentagens na tabela:", sum(pcts_in_table))
   print("Valores calculados sobre 152:", [round(c/152*100, 1) for c in counts])
   print("Valores corretos sobre 180:", [round(c/180*100, 1) for c in counts])
   '
   ```
2. **Verificação dos Trechos Inexatos nos Slides 07 e 12:**
   ```bash
   # Slide 07: conferir ausência de travessão em Twitter / tempo real
   sed -n '268,274p' slides/01-conceito-contexto.html

   # Slide 12: conferir ausência de texto citado nas linhas 143 e 153
   sed -n '143,155p' slides/02-recon-ativo.html
   sed -n '213,218p' slides/02-recon-ativo.html
   ```
3. **Verificação do Trecho do Slide 17 vs Slide 02:**
   ```bash
   grep -n "ecossistema" slides/03a-passivo-introducao.html slides/00-abertura.html
   ```
4. **Verificação da Suíte de Testes:**
   ```bash
   python3 scripts/build.py --check
   python3 -m unittest discover -s tests -v
   git status --porcelain slides/
   ```

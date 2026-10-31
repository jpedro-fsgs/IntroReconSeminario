#!/usr/bin/env python3
"""Script de verificação aritmética rigorosa da tabela em AUDITORIA_AI_SLOP.md."""

from pathlib import Path
import re
import sys

AUDIT_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/AUDITORIA_AI_SLOP.md")
content = AUDIT_PATH.read_text(encoding="utf-8")

# Extração da tabela da Seção 1.2
table_pattern = re.compile(r"\|\s*\*\*([^*]+)\*\*\s*\|\s*(?:\*\*)?(\d+)(?:\*\*)?\s*\|\s*(?:\*\*)?([\d,]+)%(?:\*\*)?\s*\|\s*([^|]*)\|\s*([^|]*)\|")
matches = table_pattern.findall(content)

print(f"Total de linhas capturadas na tabela: {len(matches)}")
rows = []
total_row = None

for m in matches:
    name, freq_str, pct_str, gravidade, loc = [x.strip() for x in m]
    if "TOTAL" in name:
        total_row = (name, int(freq_str), pct_str, gravidade, loc)
    else:
        rows.append((name, int(freq_str), float(pct_str.replace(",", ".")), pct_str))

print("\n--- Linhas de Padrões ---")
sum_freq = 0
sum_pct = 0.0
errors = []

for name, freq, pct, pct_str in rows:
    sum_freq += freq
    sum_pct += pct
    expected_pct = round((freq / 180.0) * 100, 1)
    match_status = "OK" if abs(pct - expected_pct) < 1e-6 else f"MISMATCH (esperado {expected_pct}%)"
    if match_status != "OK":
        errors.append(f"{name}: freq={freq}, pct={pct}%, esperado={expected_pct}%")
    print(f"| {name:<42} | freq={freq:>2} | pct={pct_str:>5}% | calc={expected_pct:>5.1f}% | {match_status}")

print("\n--- Validação do Total ---")
print(f"Soma das frequências: {sum_freq} (Esperado: 180)")
print(f"Soma das porcentagens arredondadas: {sum_pct:.1f}% (Esperado: 99.9% ~ 100.0% devido a arredondamento de 12 frações)")
unrounded_sum = sum(freq / 180.0 * 100 for _, freq, _, _ in rows)
print(f"Soma exata das porcentagens não-arredondadas: {unrounded_sum:.6f}%")

if total_row:
    print(f"Linha de total no Markdown: freq={total_row[1]}, pct={total_row[2]}%")
    if total_row[1] != 180:
        errors.append(f"Total registrado na tabela é {total_row[1]}, esperado 180")
    if total_row[2] != "100,0":
        errors.append(f"Total % registrado é {total_row[2]}%, esperado 100,0%")
else:
    errors.append("Linha de TOTAL não encontrada na tabela!")

if sum_freq != 180:
    errors.append(f"Soma das frequências é {sum_freq}, esperado 180")
if abs(sum_pct - 100.0) > 0.2:
    errors.append(f"Soma das porcentagens arredondadas desvia de 100%: {sum_pct:.1f}%")
if abs(unrounded_sum - 100.0) > 1e-9:
    errors.append(f"Soma teórica das porcentagens sobre 180 não é 100%: {unrounded_sum}%")

# Checar menções a ocorrências no documento
occ_mentions = re.findall(r"(\d+)\s+ocorrências\s+catalogadas", content, re.IGNORECASE)
print(f"\nMenções a 'X ocorrências catalogadas': {occ_mentions}")
for mention in occ_mentions:
    if int(mention) != 180:
        errors.append(f"Menção inconsistente no texto: {mention} ocorrências catalogadas (deveria ser 180)")

if errors:
    print("\nERROS ENCONTRADOS:")
    for e in errors:
        print(f" - {e}")
    sys.exit(1)
else:
    print("\nTODAS AS CHECAGENS ARITMÉTICAS PASSARAM COM SUCESSO (180 ocorrências, 100,0% soma exata)!")
    sys.exit(0)

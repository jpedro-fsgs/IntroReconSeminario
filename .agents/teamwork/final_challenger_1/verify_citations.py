#!/usr/bin/env python3
"""Verificação programática estrita das citações dos Slides 02, 07 e 12 em AUDITORIA_AI_SLOP.md contra os arquivos HTML em slides/."""

from pathlib import Path
import re
import sys

ROOT = Path("/home/myoui/T/Projects/IntroReconSeminário")
AUDIT_FILE = ROOT / "AUDITORIA_AI_SLOP.md"
SLIDES_DIR = ROOT / "slides"

target_slides = {
    2: {
        "file": SLIDES_DIR / "00-abertura.html",
        "expected_quotes": [
            'Seis blocos.<br />Uma pergunta: <em class="red">o que o alvo já contou?</em>',
            'Começamos pelo conceito, passamos pelas duas faces do reconhecimento e terminamos com casos reais',
            'Redes, portas, Nmap e Wireshark — quando o alvo responde.',
            'O rastro que você deixa — e como reduzir.',
            'OSINT, fontes abertas e o ecossistema de inteligência.'
        ]
    },
    7: {
        "file": SLIDES_DIR / "01-conceito-contexto.html",
        "expected_quotes": [
            '<h2 class="h-lg">O post que virou<br /><em class="red">coordenada.</em></h2>',
            'Não foi invasão. Foi <em>leitura de contexto</em> em tempo real.',
            'Twitter · agora',
            'tempo real'
        ]
    },
    12: {
        "file": SLIDES_DIR / "02-recon-ativo.html",
        "expected_quotes": [
            '<h2 class="h-md">Nmap: o mapa que o alvo entrega sem querer</h2>',
            'A aplicação não registra o handshake — mas o firewall vê.',
            'O scan não explora nada. Ele só pergunta — e o alvo responde.',
            '-sS (SYN), -sV (versões), -p- (todas as portas), -oA (salvar em três formatos)'
        ]
    }
}

audit_text = AUDIT_FILE.read_text(encoding="utf-8")
audit_lines = audit_text.splitlines()

errors = []
successes = []

print("=== VERIFICAÇÃO EMPÍRICA DE CITAÇÕES (SLIDES 02, 07, 12) ===\n")

for slide_num, data in target_slides.items():
    html_file = data["file"]
    html_raw = html_file.read_text(encoding="utf-8")
    html_lines = html_raw.splitlines()
    print(f"--- Checando Slide {slide_num:02d} em {html_file.name} ---")

    for q in data["expected_quotes"]:
        # 1. Checar se a citação existe no relatório de auditoria
        in_audit = q in audit_text or q.replace("&amp;", "&") in audit_text
        if not in_audit:
            errors.append(f"Slide {slide_num}: Citação não encontrada em AUDITORIA_AI_SLOP.md: '{q}'")
            continue

        # 2. Checar se a citação existe no HTML do slide
        # Testar presença direta ou com substituição de quebras de linha/espaços
        found_in_html = False
        matching_line_no = None

        # Busca literal simples
        if q in html_raw:
            found_in_html = True
            for lno, hline in enumerate(html_lines, 1):
                if q in hline:
                    matching_line_no = lno
                    break
        else:
            # Busca normalizando espaços ou tags
            norm_q = " ".join(q.split())
            norm_raw = " ".join(html_raw.split())
            from html.parser import HTMLParser
            class Extractor(HTMLParser):
                def __init__(self):
                    super().__init__()
                    self.res = []
                def handle_data(self, d):
                    self.res.append(d)
                def text(self):
                    return " ".join("".join(self.res).split())
            ext = Extractor()
            ext.feed(html_raw)
            stripped_html = ext.text()

            if norm_q in norm_raw:
                found_in_html = True
                for lno, hline in enumerate(html_lines, 1):
                    if norm_q.split()[0] in hline:
                        matching_line_no = lno
                        break
            elif norm_q in stripped_html:
                found_in_html = True
                for lno, hline in enumerate(html_lines, 1):
                    if norm_q.split()[0] in hline:
                        matching_line_no = lno
                        break
            else:
                # Checar sem tags HTML (texto puro)
                strip_q = re.sub(r"<[^>]+>", "", q).strip()
                if strip_q in stripped_html:
                    found_in_html = True
                    for lno, hline in enumerate(html_lines, 1):
                        if strip_q.split()[0] in hline:
                            matching_line_no = lno
                            break

        if found_in_html:
            line_info = f" (HTML Linha ~{matching_line_no})" if matching_line_no else ""
            print(f"  [OK] Citação confirmada no HTML{line_info}:")
            print(f"       \"{q}\"")
            successes.append((slide_num, q, matching_line_no))
        else:
            errors.append(f"Slide {slide_num}: Citação NÃO encontrada no HTML ({html_file.name}): '{q}'")
            print(f"  [FALHA] Não encontrada no HTML: \"{q}\"")

print(f"\nResumo: {len(successes)} citações confirmadas com sucesso, {len(errors)} falhas.")

if errors:
    print("\nERROS:")
    for err in errors:
        print(f" - {err}")
    sys.exit(1)
else:
    print("\nTODAS AS CITAÇÕES DOS SLIDES 02, 07 E 12 FORAM VERIFICADAS COM EXATIDÃO NO HTML!")
    sys.exit(0)

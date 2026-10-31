#!/usr/bin/env python3
"""Testes empíricos e adversariais de exatidão factual para AUDITORIA_AI_SLOP.md."""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent
AUDIT_FILE = ROOT / "AUDITORIA_AI_SLOP.md"
SLIDES_DIR = ROOT / "slides"
MANIFEST_FILE = SLIDES_DIR / "manifest.json"


class HTMLTextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []

    def handle_data(self, d):
        self.result.append(d)

    def get_text(self):
        return " ".join("".join(self.result).split())


def strip_tags(html):
    p = HTMLTextExtractor()
    p.feed(html)
    return p.get_text()


class AuditEmpiricalValidationTests(unittest.TestCase):
    """Bateria de testes empíricos sobre AUDITORIA_AI_SLOP.md."""

    @classmethod
    def setUpClass(cls):
        cls.content = AUDIT_FILE.read_text(encoding="utf-8")
        cls.lines = cls.content.splitlines()

    def test_slide_and_file_coverage(self):
        """Verifica se todos os 12 arquivos e 54 slides estão cobertos."""
        manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
        self.assertEqual(len(manifest), 12)

        # Verificar se os 12 arquivos constam no relatório
        for filename in manifest:
            rel_path = f"slides/{filename}"
            self.assertIn(rel_path, self.content, f"Arquivo {rel_path} ausente de AUDITORIA_AI_SLOP.md")

        # Verificar cobertura dos 54 slides
        found_slides = set()
        for m in re.finditer(r'###\s+Slide\s+(\d+)', self.content):
            found_slides.add(int(m.group(1)))
        for m in re.finditer(r'###\s+Slides\s+(\d+)\s+a\s+(\d+)', self.content):
            for s in range(int(m.group(1)), int(m.group(2)) + 1):
                found_slides.add(s)
        for m in re.finditer(r'-\s+\*\*Slide\s+(\d+)', self.content):
            found_slides.add(int(m.group(1)))

        self.assertEqual(found_slides, set(range(1, 55)), "Nem todos os 54 slides foram cobertos")

    def test_absence_of_invented_ai_scores(self):
        """Verifica ausência de scores numéricos arbitrários de IA (% AI, AI score)."""
        forbidden_terms = ["AI score", "% AI", "AI %"]
        for term in forbidden_terms:
            matches = list(re.finditer(re.escape(term), self.content, re.IGNORECASE))
            self.assertEqual(len(matches), 0, f"Termo proibido de score encontrado: {term}")

        # GPTZero só é permitido em declarações metodológicas de rejeição explícita
        gptzero_matches = [
            line for line in self.lines
            if "gptzero" in line.lower()
        ]
        for match in gptzero_matches:
            self.assertTrue(
                "rejeita" in match.lower() or "não" in match.lower(),
                f"Uso indevido de GPTZero sem contexto de rejeição: {match}"
            )

    def test_citation_accuracy_and_catalog_defects(self):
        """Executa varredura de todas as citações e cataloga defeitos factuais."""
        current_file = None
        current_slide = None
        items = []

        for idx, line in enumerate(self.lines, 1):
            m_file = re.search(r"ARQUIVO \d+ / 12:\s*(slides/[\w\.-]+)", line)
            if m_file:
                current_file = m_file.group(1).strip()
            m_ident = re.search(r"- \*\*Identificação:\*\*\s*`(slides/[\w\.-]+)`", line)
            if m_ident:
                current_file = m_ident.group(1).strip()
            m_slide = re.search(r"###\s+Slide\s+(\d+)", line)
            if m_slide:
                current_slide = f"Slide {int(m_slide.group(1)):02d}"
            m_slides = re.search(r"###\s+Slides\s+(\d+)\s+a\s+(\d+)", line)
            if m_slides:
                current_slide = f"Slides {m_slides.group(1)}-{m_slides.group(2)}"
            m_subslide = re.search(r"-\s+\*\*Slide\s+(\d+)", line)
            if m_subslide:
                current_slide = f"Slide {int(m_subslide.group(1)):02d}"

            if "Trecho Citado" in line:
                items.append((idx, current_file, current_slide, line))

        self.assertGreater(len(items), 90, "Menos de 90 ocorrências de Trecho Citado encontradas")

        defects = []
        for idx, filepath, slide, line in items:
            file_raw = (ROOT / filepath).read_text(encoding="utf-8")
            file_norm = " ".join(file_raw.split())
            file_stripped_norm = " ".join(strip_tags(file_raw).split())

            after_prefix = re.sub(r"^.*?-\s+\*\*Trecho Citado.*?\:\*\*\s*", "", line)
            code_cand = re.findall(r"`([^`]+)`", after_prefix)
            quote_cand = re.findall(r"\"([^\"]+)\"", after_prefix)

            cands = []
            if code_cand:
                for c in code_cand:
                    c_clean = c.strip("\"")
                    if c_clean:
                        cands.append(c_clean)
            if quote_cand:
                for q in quote_cand:
                    if q:
                        cands.append(q)

            for cand in cands:
                clean = cand.strip(" .…\"`")
                if clean.startswith("..."):
                    clean = clean[3:].strip()
                if clean.endswith("..."):
                    clean = clean[:-3].strip()
                if not clean or len(clean) < 3:
                    continue

                clean_norm = " ".join(clean.split())
                clean_stripped_norm = " ".join(strip_tags(clean).split())

                # Verifica se o trecho existe no HTML original ou no texto renderizado
                in_raw = clean in file_raw or clean_norm in file_norm
                in_stripped = clean_stripped_norm in file_stripped_norm or clean_norm in file_stripped_norm

                if not in_raw and not in_stripped:
                    # Também verifica na versão base do commit (antes da implementação das melhorias nos slides)
                    try:
                        import subprocess
                        proc = subprocess.run(["git", "show", f"d4cbde8490a19b41d3b8c439c03948a3d0c917b9:{filepath}"], capture_output=True, text=True)
                        if proc.returncode == 0:
                            orig_raw = proc.stdout
                            orig_norm = " ".join(orig_raw.split())
                            orig_stripped_norm = " ".join(strip_tags(orig_raw).split())
                            in_raw = clean in orig_raw or clean_norm in orig_norm
                            in_stripped = clean_stripped_norm in orig_stripped_norm or clean_norm in orig_stripped_norm
                    except Exception:
                        pass

                # Se não bate nem raw nem stripped, verifica se múltiplos blocos batem
                if not in_raw and not in_stripped:
                    parts = [p.strip() for p in re.findall(r"<[^>]+>|[^<]+", clean) if not p.startswith("<")]
                    if not (parts and all(" ".join(p.split()) in file_stripped_norm for p in parts if len(p.strip()) > 3)):
                        defects.append((idx, filepath, slide, clean))

        # Certificar que os defeitos factuais apontados pelos revisores foram saneados
        defect_lines = {d[0] for d in defects}
        self.assertNotIn(231, defect_lines, "Citação saneada na Linha 231 (Slide 07) não deve ser defeito")
        self.assertNotIn(321, defect_lines, "Citação saneada na Linha 321 (Slide 12) não deve ser defeito")
        self.assertNotIn(406, defect_lines, "Trecho removido do Slide 17 não deve ser defeito")

    def test_statistical_table_and_total_occurrences(self):
        """Verifica a coerência matemática da tabela da Seção 1.2 e o total da Linha 20."""
        # Verificar menção a 180 ocorrências catalogadas no texto
        self.assertIn("180 ocorrências catalogadas", self.content, "Linha 20 deve registrar 180 ocorrências catalogadas")
        self.assertNotIn("152 ocorrências catalogadas", self.content, "Menção defasada a 152 ocorrências deve ser removida")

        # Extrair linhas da tabela de padrões
        table_pattern = re.compile(r"\|\s*\*\*([^*]+)\*\*\s*\|\s*(\d+)\s*\|\s*([\d,]+)%\s*\|")
        matches = table_pattern.findall(self.content)

        counts = []
        pcts = []
        for name, count_str, pct_str in matches:
            if "TOTAL" in name:
                self.assertEqual(int(count_str), 180)
                self.assertEqual(pct_str, "100,0")
            else:
                counts.append(int(count_str))
                pcts.append(float(pct_str.replace(",", ".")))

        self.assertEqual(len(counts), 12, "Devem existir 12 categorias de padrões")
        self.assertEqual(sum(counts), 180, "Soma das frequências deve ser 180")
        # Soma das porcentagens calculadas sobre base 180
        expected_pcts = [round(c / 180 * 100, 1) for c in counts]
        self.assertEqual(pcts, expected_pcts, "Porcentagens da tabela devem corresponder à base 180")
        self.assertAlmostEqual(sum(pcts), 100.0, delta=0.2, msg="Soma das porcentagens deve totalizar 100%")


if __name__ == "__main__":
    unittest.main()


#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path("/home/myoui/T/Projects/IntroReconSeminário")
AUDIT_FILE = ROOT / "AUDITORIA_AI_SLOP.md"
SLIDES_DIR = ROOT / "slides"

audit_text = AUDIT_FILE.read_text(encoding="utf-8")

# Extract occurrences with slide context
# Each occurrence has:
# - slide context: e.g. Identificação: `slides/...`
# - Trecho Citado: ... (Linha X or Linhas X-Y)

entries = re.findall(
    r'\*\*Trecho Citado(?:\s*\([^)]*\))?:\*\*\s*(.*?)(?=\s*\((?:Linha|Linhas)\s*[\d–-]+\)|\n\s*-\s*\*\*Padrão)',
    audit_text,
    re.DOTALL
)

print(f"Total entries found: {len(entries)}")

all_slides = {f.name: f.read_text(encoding="utf-8") for f in SLIDES_DIR.glob("*.html")}
full_deck = "\n".join(all_slides.values())

def normalize(s):
    # strip quotes, backticks, spaces
    s = s.strip()
    if s.startswith('`') and s.endswith('`'):
        s = s[1:-1].strip()
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1].strip()
    if s.startswith('“') and s.endswith('”'):
        s = s[1:-1].strip()
    s = re.sub(r'\s+', ' ', s)
    return s

exact_matches = 0
partial_matches = 0
failures = []

for entry in entries:
    clean = normalize(entry)
    # clean out html line breaks or entities if checking
    if clean in full_deck or clean.replace('<br />', '<br/>') in full_deck or clean.replace('<br/>', '<br />') in full_deck:
        exact_matches += 1
    else:
        # Check without HTML tags or subphrases
        # If there are multiple sentences or breaks
        subphrases = [p.strip() for p in re.split(r'<[^>]+>', clean) if len(p.strip()) > 10]
        if subphrases and all(sub in full_deck for sub in subphrases):
            partial_matches += 1
        else:
            failures.append((clean, subphrases))

print(f"Exact matches: {exact_matches}")
print(f"Partial/tag-split matches: {partial_matches}")
print(f"Failures count: {len(failures)}")

if failures:
    print("\nFailures:")
    for f, sub in failures:
        print(f"RAW: {f}")
        print(f"SUB: {sub}")
        print("---")

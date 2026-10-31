#!/usr/bin/env python3
"""
validate_antislop_pedagogy.py - Adversarial audit for AI Slop patterns in PLANO_IMPLEMENTACAO_DIDATICO.md proposals.
Author: Challenger 2
Target: PLANO_IMPLEMENTACAO_DIDATICO.md
"""

import re
from pathlib import Path

PLAN_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md")

BANNED_WORDS = [
    r"\bdelve\b", r"\bfoster\b", r"\bleverage\b", r"\butilize\b", r"\bfacilitate\b",
    r"\bempower\b", r"\bstreamline\b", r"\brobust[oa]?s?\b", r"\bcutting[- ]edge\b",
    r"\bparadigm shift\b", r"\bgame changer\b", r"\btapestry\b", r"\brealm\b",
    r"\bbeacon\b", r"\bmultifaceted\b", r"\bmeticulous\b", r"\bintricate\b",
    r"\bparamount\b", r"\btransformative\b", r"\belevate\b", r"\bembark\b",
    r"\bsupercharge\b", r"\bharness\b", r"\bever[- ]evolving\b",
    r"\bacionável\b", r"\bacionáveis\b", r"\balavancar\b", r"\bmergulhar\b"
]

def audit_antislop():
    text = PLAN_PATH.read_text(encoding="utf-8")
    
    # Split by slide
    slide_pattern = re.compile(r"^### Slide\s+(\d+)\s+[·-–—]\s*(.+)$", re.MULTILINE)
    matches = list(slide_pattern.finditer(text))
    
    findings = []
    
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i+1 < len(matches) else len(text)
        snum = int(matches[i].group(1))
        stitle = matches[i].group(2).strip()
        block = text[start:end]
        
        # We only want to test the PROPOSAL part (not the Diagnóstico which quotes the original slop!)
        prop_match = re.search(r"-\s+\*\*Proposta de Reformulação Didática.*?\:\*\*(.*?)(?=-\s+\*\*Fatos Técnicos|\Z)", block, re.DOTALL)
        if not prop_match:
            continue
        proposal_text = prop_match.group(1)
        
        # 1. Banned words in proposal
        for bw in BANNED_WORDS:
            matches_bw = re.finditer(bw, proposal_text, re.IGNORECASE)
            for m in matches_bw:
                # Check if it's explicitly discussing the word or in quotes
                snippet = proposal_text[max(0, m.start()-30):min(len(proposal_text), m.end()+30)]
                if 'termo banido' in snippet.lower() or 'elimina' in snippet.lower() or f'"{m.group()}"' in snippet or f'`{m.group()}`' in snippet:
                    continue
                findings.append((snum, "Banned Word in Proposal", m.group(), snippet.strip()))
                
        # 2. Binary contrasts in proposal ("não é ..., é ...", "não se trata de ..., mas ...")
        binary_patterns = [
            r"não\s+(?:é|foi|se trata|são)\s+[^.,;\n]+[.,;\n]\s*(?:é|são|mas|trata-se)",
            r"não\s+apenas\s+[^.,;\n]+,\s*mas\s+também",
        ]
        for bp in binary_patterns:
            for m in re.finditer(bp, proposal_text, re.IGNORECASE):
                snippet = proposal_text[max(0, m.start()-20):min(len(proposal_text), m.end()+20)]
                findings.append((snum, "Binary Contrast in Proposal", m.group(), snippet.strip()))
                
        # 3. Teatral / melodrama notes in proposal
        theatrical = [r"pausa dramática", r"tom conspiratório", r"olhar firme", r"provocar:"]
        for th in theatrical:
            for m in re.finditer(th, proposal_text, re.IGNORECASE):
                snippet = proposal_text[max(0, m.start()-20):min(len(proposal_text), m.end()+20)]
                findings.append((snum, "Theatrical Direction in Proposal", m.group(), snippet.strip()))

    print(f"=== ADVERSARIAL AI-SLOP SCAN IN PROPOSALS ({len(findings)} findings) ===")
    for snum, cat, matched, snip in findings:
        print(f"Slide {snum:02d} | [{cat}] '{matched}'\n    Context: {snip}")
        
    return findings

if __name__ == "__main__":
    audit_antislop()

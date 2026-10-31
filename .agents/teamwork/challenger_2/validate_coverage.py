#!/usr/bin/env python3
"""
validate_coverage.py - Empirical test for slide coverage and required schema fields.
Author: Challenger 2
Target: PLANO_IMPLEMENTACAO_DIDATICO.md
"""

import sys
import re
import json
from pathlib import Path

PLAN_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md")
MANIFEST_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/slides/manifest.json")
DETAILED_SLIDES_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json")

def test_coverage():
    assert PLAN_PATH.exists(), f"Plan file not found: {PLAN_PATH}"
    content = PLAN_PATH.read_text(encoding="utf-8")
    
    # Extract all Slide sections
    slide_pattern = re.compile(r"^### Slide\s+(\d+)\s+[·-–—]\s*(.+)$", re.MULTILINE)
    matches = list(slide_pattern.finditer(content))
    
    print(f"[*] Found {len(matches)} slide headers in {PLAN_PATH.name}")
    
    errors = []
    
    # 1. Total count check
    if len(matches) != 54:
        errors.append(f"Expected 54 slides, found {len(matches)}")
        
    # 2. Contiguity check
    found_nums = [int(m.group(1)) for m in matches]
    expected_nums = list(range(1, 55))
    if found_nums != expected_nums:
        missing = set(expected_nums) - set(found_nums)
        extra = set(found_nums) - set(expected_nums)
        errors.append(f"Slide numbering mismatch! Missing: {missing}, Extra: {extra}")
        
    # Split text into slide blocks
    slide_blocks = {}
    for i in range(len(matches)):
        start_pos = matches[i].start()
        end_pos = matches[i+1].start() if i + 1 < len(matches) else len(content)
        slide_num = int(matches[i].group(1))
        slide_blocks[slide_num] = {
            "title": matches[i].group(2).strip(),
            "text": content[start_pos:end_pos]
        }
        
    # Load manifest and detailed_slides for ground truth comparison
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8")) if MANIFEST_PATH.exists() else []
    detailed_slides = json.loads(DETAILED_SLIDES_PATH.read_text(encoding="utf-8")) if DETAILED_SLIDES_PATH.exists() else []
    
    ground_truth = {int(s["num"]): s for s in detailed_slides}
    
    # Required field regex patterns
    req_fields = {
        "Cabecalho": re.compile(r"-\s+\*\*Cabeçalho:\*\*", re.IGNORECASE),
        "Objetivo Didatico": re.compile(r"-\s+\*\*Objetivo Didático.*?\:\*\*", re.IGNORECASE),
        "Diagnostico AI Slop": re.compile(r"-\s+\*\*Diagnóstico.*?(?:AI Slop|Engessamento).*?\:\*\*", re.IGNORECASE),
        "Proposta Didatica": re.compile(r"-\s+\*\*Proposta de Reformulação Didática.*?\:\*\*", re.IGNORECASE),
        "Checklist Preservados": re.compile(r"-\s+\*\*Fatos Técnicos Preservados:\*\*", re.IGNORECASE)
    }
    
    req_subfields_proposta = {
        "Titulo/Manchete": re.compile(r"\*(?:Proposta de Título|Manchete)\*?", re.IGNORECASE),
        "Corpo/Topicos": re.compile(r"\*(?:Proposta de Corpo|Corpo de Texto|Tópicos)\*?", re.IGNORECASE),
        "Modelo Mental": re.compile(r"\*(?:Modelo Mental|Metáfora Funcional)\*?", re.IGNORECASE),
        "Roteiro/Tom": re.compile(r"\*(?:Roteiro e Tom|Roteiro Falado|Tom do Apresentador|Proposta de Notas)\*?", re.IGNORECASE),
    }

    schema_failures = []
    file_mismatches = []
    
    for num in range(1, 55):
        block = slide_blocks.get(num)
        if not block:
            schema_failures.append(f"Slide {num:02d}: Missing block completely")
            continue
            
        text = block["text"]
        
        # Check mandatory fields
        for field_name, pat in req_fields.items():
            if not pat.search(text):
                schema_failures.append(f"Slide {num:02d}: Missing required field '{field_name}'")
                
        # Check subfields in Proposta Didatica
        for sub_name, pat in req_subfields_proposta.items():
            if not pat.search(text):
                schema_failures.append(f"Slide {num:02d}: Missing proposal subfield '{sub_name}'")
                
        # Check checklist has at least one checked item
        checked_items = re.findall(r"-\s+\[x\]\s+(.+)", text, re.IGNORECASE)
        if not checked_items:
            schema_failures.append(f"Slide {num:02d}: Checklist of preserved facts has no checked items '- [x]'")
            
        # Ground truth file comparison
        if num in ground_truth:
            gt_file = ground_truth[num]["file"]
            # Look for file in header
            file_match = re.search(r"Arquivo:\s*`?(?:slides/)?([^`\s|]+)`?", text)
            if file_match:
                plan_file = Path(file_match.group(1)).name
                if plan_file != gt_file:
                    file_mismatches.append(f"Slide {num:02d}: Plan file '{plan_file}' != ground truth '{gt_file}'")
            else:
                schema_failures.append(f"Slide {num:02d}: Could not parse 'Arquivo:' from header")

    print("\n--- RESULTS OF COVERAGE TEST ---")
    print(f"Total slides evaluated: {len(slide_blocks)}")
    print(f"Schema failures count: {len(schema_failures)}")
    print(f"File mismatches count: {len(file_mismatches)}")
    
    if schema_failures:
        print("\n[!] SCHEMA FAILURES (first 10):")
        for f in schema_failures[:10]:
            print("  -", f)
            
    if file_mismatches:
        print("\n[!] FILE MISMATCHES:")
        for m in file_mismatches:
            print("  -", m)
            
    success = (len(errors) == 0 and len(schema_failures) == 0 and len(file_mismatches) == 0)
    print(f"\nFinal Coverage Verdict: {'PASS' if success else 'FAIL'}")
    return success, {
        "total_slides": len(slide_blocks),
        "errors": errors,
        "schema_failures": schema_failures,
        "file_mismatches": file_mismatches
    }

if __name__ == "__main__":
    success, res = test_coverage()
    sys.exit(0 if success else 1)

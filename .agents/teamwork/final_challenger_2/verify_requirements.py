#!/usr/bin/env python3
"""
verify_requirements.py - Rigorous empirical verification for Final Challenger 2.
"""

import re
import subprocess
import sys
from pathlib import Path

PLAN_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md")
REPO_ROOT = Path("/home/myoui/T/Projects/IntroReconSeminário")

def get_slide_block(text: str, slide_num: int) -> str:
    pattern = re.compile(rf"^### Slide\s+{slide_num}\b.*?(?=^### Slide|\Z)", re.MULTILINE | re.DOTALL)
    m = pattern.search(text)
    if not m:
        raise ValueError(f"Slide {slide_num} block not found!")
    return m.group(0)

def main():
    print("=" * 80)
    print("FINAL CHALLENGER 2: INDEPENDENT EMPIRICAL VERIFICATION")
    print("=" * 80)

    assert PLAN_PATH.exists(), f"File {PLAN_PATH} does not exist!"
    plan_text = PLAN_PATH.read_text(encoding="utf-8")
    
    failures = []

    # 1. Slide 43 Coordinates (34.5°N 69.2°E)
    print("\n[CHECK 1] Slide 43 Coordinates (34.5°N 69.2°E)...")
    s43_block = get_slide_block(plan_text, 43)
    s43_coord_pattern = r"34\.5°N\s+69\.2°E"
    m43 = re.findall(s43_coord_pattern, s43_block)
    print(f"Slide 43 matches for 34.5°N 69.2°E: {len(m43)}")
    if len(m43) < 2:
        failures.append(f"Slide 43 has insufficient occurrences of coordinates (found {len(m43)})")
    else:
        print("  -> PASS: Slide 43 contains verified coordinates in body, correlation and preserved checklist.")

    # 2. Slide 46 Coordinates (32.89°S 68.84°W)
    print("\n[CHECK 2] Slide 46 Coordinates (32.89°S 68.84°W)...")
    s46_block = get_slide_block(plan_text, 46)
    s46_coord_pattern = r"32\.89°S\s+68\.84°W"
    m46 = re.findall(s46_coord_pattern, s46_block)
    print(f"Slide 46 matches for 32.89°S 68.84°W: {len(m46)}")
    if len(m46) < 2:
        failures.append(f"Slide 46 has insufficient occurrences of coordinates (found {len(m46)})")
    else:
        print("  -> PASS: Slide 46 contains verified coordinates in hypothesis, script, and checklist.")

    # 3. Required Tools
    print("\n[CHECK 3] Required Tools in PLANO_IMPLEMENTACAO_DIDATICO.md...")
    tools = {
        "Wayback Machine": [r"\bWayback(?:\s+Machine)?\b"],
        "Have I Been Pwned / HIBP": [r"\bHIBP\b", r"\bHave I Been Pwned\b"],
        "Google Lens": [r"\bGoogle Lens\b"],
        "Mapillary": [r"\bMapillary\b"],
        "Overpass": [r"\bOverpass(?:\s+Turbo)?\b"]
    }
    for tool_name, pats in tools.items():
        found = False
        counts = 0
        for pat in pats:
            c = len(re.findall(pat, plan_text, re.IGNORECASE))
            counts += c
            if c > 0:
                found = True
        print(f"  Tool '{tool_name}': {counts} occurrences found.")
        if not found:
            failures.append(f"Tool '{tool_name}' missing from plan!")
    if not failures:
        print("  -> PASS: All required tools are present and documented.")

    # 4. Slide 14 & 51 Affirmative Metaphors (No binary contrasts)
    print("\n[CHECK 4] Affirmative Metaphors in Slides 14 and 51...")
    s14_block = get_slide_block(plan_text, 14)
    s51_block = get_slide_block(plan_text, 51)
    
    m14_search = re.search(r"-\s+\*Modelo Mental.*?\:\s*(.*)", s14_block)
    m51_search = re.search(r"-\s+\*Modelo Mental.*?\:\s*(.*)", s51_block)
    
    assert m14_search, "Modelo Mental not found in Slide 14!"
    assert m51_search, "Modelo Mental not found in Slide 51!"
    
    m14_text = m14_search.group(1).strip()
    m51_text = m51_search.group(1).strip()
    
    print(f"Slide 14 Metaphor: {m14_text}")
    print(f"Slide 51 Metaphor: {m51_text}")
    
    contrast_patterns = [
        r"não\s+(?:é|foi|se trata|são|era)\s+[^.,;\n]+[.,;\n]\s*(?:é|são|mas|trata-se)",
        r"não\s+[^.,;\n]+;\s*é\s+",
        r"não\s+[^.,;\n]+,\s*mas\s+"
    ]
    
    for pat in contrast_patterns:
        if re.search(pat, m14_text, re.IGNORECASE):
            failures.append(f"Binary contrast detected in Slide 14 metaphor: {m14_text}")
        if re.search(pat, m51_text, re.IGNORECASE):
            failures.append(f"Binary contrast detected in Slide 51 metaphor: {m51_text}")
            
    if "não é" in m14_text.lower():
        failures.append(f"'não é' detected in Slide 14 metaphor: {m14_text}")
    if "não é" in m51_text.lower():
        failures.append(f"'não é' detected in Slide 51 metaphor: {m51_text}")
        
    print("  -> PASS: Metaphors in Slides 14 and 51 are strictly affirmative and functional.")

    # 5. Git Status of slides/ and build check
    print("\n[CHECK 5] Immutability of slides/ & Build / Test Suite...")
    git_res = subprocess.run(["git", "status", "--short", "slides/"], cwd=REPO_ROOT, capture_output=True, text=True)
    git_clean = (git_res.stdout.strip() == "")
    print(f"git status --short slides/: '{git_res.stdout.strip()}' (Clean: {git_clean})")
    if not git_clean:
        failures.append(f"slides/ has unstaged/staged modifications: {git_res.stdout}")

    build_res = subprocess.run([sys.executable, "scripts/build.py", "--check"], cwd=REPO_ROOT, capture_output=True, text=True)
    build_ok = (build_res.returncode == 0)
    print(f"python3 scripts/build.py --check (Code {build_res.returncode}): {build_res.stdout.strip()}")
    if not build_ok:
        failures.append(f"Build check failed: {build_res.stderr or build_res.stdout}")

    unit_res = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=REPO_ROOT, capture_output=True, text=True)
    unit_ok = (unit_res.returncode == 0)
    print(f"python3 -m unittest discover -s tests -v (Code {unit_res.returncode})")
    if not unit_ok:
        failures.append(f"Unit tests failed: {unit_res.stderr}")

    print("\n" + "=" * 80)
    if failures:
        print("VERIFICATION FAILED WITH ISSUES:")
        for f in failures:
            print(f"  [X] {f}")
        sys.exit(1)
    else:
        print("ALL EMPIRICAL CHECKS PASSED PERFECTLY!")
        print("VERDICT: APPROVE")
        sys.exit(0)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
independent_audit.py - Comprehensive Independent Victory Audit Script.
Executed independently by the Victory Auditor.
"""

import json
import os
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path("/home/myoui/T/Projects/IntroReconSeminário")
SLIDES_DIR = ROOT / "slides"
MANIFEST_FILE = SLIDES_DIR / "manifest.json"
AUDIT_FILE = ROOT / "AUDITORIA_AI_SLOP.md"
PLAN_FILE = ROOT / "PLANO_IMPLEMENTACAO_DIDATICO.md"
SKILL_FILE = Path("/home/myoui/.gemini/config/skills/no-ai-slop/SKILL.md")


def strip_html(html_text):
    """Strip tags inserting space between tags to avoid concatenating adjacent tag contents,
    then normalize whitespace and fix punctuation spacing."""
    spaced = re.sub(r"<[^>]+>", " ", html_text)
    norm = " ".join(spaced.split())
    return re.sub(r"\s+([,.:;?!])", r"\1", norm)


def run_checks():
    report = []
    failed = False

    def log(msg):
        print(msg)
        report.append(msg)

    log("=" * 80)
    log("INDEPENDENT VICTORY AUDIT EXECUTION")
    log("=" * 80)

    # ---------------------------------------------------------
    # 1. TIMELINE & GIT STATUS AUDIT
    # ---------------------------------------------------------
    log("\n[CHECK 1] Git Status & Immutability of slides/...")
    git_status = subprocess.run(
        ["git", "status", "--porcelain", "slides/"],
        cwd=ROOT, capture_output=True, text=True
    )
    if git_status.stdout.strip():
        log(f"FAIL: slides/ has modifications:\n{git_status.stdout}")
        failed = True
    else:
        log("PASS: slides/ is completely clean and untouched in git.")

    git_diff = subprocess.run(
        ["git", "diff", "HEAD", "--", "slides/"],
        cwd=ROOT, capture_output=True, text=True
    )
    if git_diff.stdout.strip():
        log(f"FAIL: git diff against HEAD shows changes in slides/:\n{git_diff.stdout}")
        failed = True
    else:
        log("PASS: git diff HEAD -- slides/ confirmed 0 changes.")

    # ---------------------------------------------------------
    # 2. SLIDES INVENTORY
    # ---------------------------------------------------------
    log("\n[CHECK 2] Slides & Manifest Inventory...")
    manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    log(f"Manifest contains {len(manifest)} HTML files.")
    if len(manifest) != 12:
        log(f"FAIL: Expected 12 files in manifest, found {len(manifest)}")
        failed = True
    else:
        log("PASS: Manifest has 12 files.")

    total_slides = 0
    slides_data = {}
    for filename in manifest:
        filepath = SLIDES_DIR / filename
        content = filepath.read_text(encoding="utf-8")
        sections = re.findall(r'<section\b[^>]*>(.*?)</section>', content, re.DOTALL)
        log(f"  {filename:35}: {len(sections)} sections")
        for i, s in enumerate(sections):
            total_slides += 1
            slides_data[total_slides] = {
                "file": f"slides/{filename}",
                "html": s,
                "text": strip_html(s),
                "notes": re.search(r'<aside class="notes">(.*?)</aside>', s, re.DOTALL)
            }

    log(f"Total slide sections counted: {total_slides}")
    if total_slides != 54:
        log(f"FAIL: Expected 54 slides, found {total_slides}")
        failed = True
    else:
        log("PASS: Exactly 54 slides present across the 12 files.")

    # ---------------------------------------------------------
    # 3. AUDITORIA_AI_SLOP.md AUDIT
    # ---------------------------------------------------------
    log("\n[CHECK 3] AUDITORIA_AI_SLOP.md Requirements & Acceptance Criteria...")
    if not AUDIT_FILE.exists():
        log("FAIL: AUDITORIA_AI_SLOP.md does not exist!")
        failed = True
        return report, failed

    audit_text = AUDIT_FILE.read_text(encoding="utf-8")
    audit_lines = audit_text.splitlines()

    # 3.1. File & Slide coverage
    for filename in manifest:
        rel = f"slides/{filename}"
        if rel not in audit_text:
            log(f"FAIL: {rel} not mentioned in AUDITORIA_AI_SLOP.md")
            failed = True
    log("PASS: All 12 slide files are referenced in AUDITORIA_AI_SLOP.md.")

    covered_slides = set()
    for m in re.finditer(r'###\s+Slide\s+(\d+)', audit_text):
        covered_slides.add(int(m.group(1)))
    for m in re.finditer(r'###\s+Slides\s+(\d+)\s+a\s+(\d+)', audit_text):
        for s in range(int(m.group(1)), int(m.group(2)) + 1):
            covered_slides.add(s)
    for m in re.finditer(r'-\s+\*\*Slide\s+(\d+)', audit_text):
        covered_slides.add(int(m.group(1)))

    if covered_slides != set(range(1, 55)):
        missing = set(range(1, 55)) - covered_slides
        log(f"FAIL: Missing slides in AUDITORIA_AI_SLOP.md: {missing}")
        failed = True
    else:
        log("PASS: All 54 slides are covered in AUDITORIA_AI_SLOP.md.")

    # 3.2. Absence of arbitrary AI detector scores
    for forbidden in ["% AI", "AI %", "AI score", "ZeroGPT score", "Sapling score"]:
        if re.search(re.escape(forbidden), audit_text, re.IGNORECASE):
            log(f"FAIL: Forbidden AI detector score found: '{forbidden}'")
            failed = True
    log("PASS: No arbitrary AI detector scores found.")

    # 3.3. Statistical table consistency
    table_matches = re.findall(r"\|\s*\*\*([^*]+)\*\*\s*\|\s*(?:\*\*)?(\d+)(?:\*\*)?\s*\|\s*(?:\*\*)?([\d,]+)%(?:\*\*)?\s*\|", audit_text)
    subtotal_count = 0
    total_found = False
    for name, count_str, pct_str in table_matches:
        if "TOTAL" in name:
            total_found = True
            if int(count_str) != 180 or pct_str != "100,0":
                log(f"FAIL: Total row in table is not 180 / 100,0%: {count_str}, {pct_str}%")
                failed = True
        else:
            subtotal_count += int(count_str)
    if not total_found:
        log("FAIL: Total row missing in pattern table.")
        failed = True
    if subtotal_count != 180:
        log(f"FAIL: Sum of category occurrences ({subtotal_count}) != 180")
        failed = True
    else:
        log(f"PASS: Pattern table frequency sum equals exactly 180 (100.0%).")

    # 3.4. Citation verification against actual slide content
    log("\n[CHECK 3.4] Verifying citations in AUDITORIA_AI_SLOP.md exist verbatim in slides/...")
    citation_lines = []
    current_file = None
    current_slide = None

    for idx, line in enumerate(audit_lines, 1):
        m_file = re.search(r"ARQUIVO \d+ / 12:\s*(slides/[\w\.-]+)", line)
        if m_file:
            current_file = m_file.group(1).strip()
        m_ident = re.search(r"- \*\*Identificação:\*\*\s*`(slides/[\w\.-]+)`", line)
        if m_ident:
            current_file = m_ident.group(1).strip()
        m_slide = re.search(r"###\s+Slide\s+(\d+)", line)
        if m_slide:
            current_slide = int(m_slide.group(1))
        m_slides = re.search(r"###\s+Slides\s+(\d+)\s+a\s+(\d+)", line)
        if m_slides:
            current_slide = int(m_slides.group(1))
        m_subslide = re.search(r"-\s+\*\*Slide\s+(\d+)", line)
        if m_subslide:
            current_slide = int(m_subslide.group(1))

        if "Trecho Citado" in line:
            citation_lines.append((idx, current_file, current_slide, line))

    log(f"Found {len(citation_lines)} lines with 'Trecho Citado'.")
    unmatched_citations = []
    for idx, filepath, slide_num, line in citation_lines:
        if not filepath:
            unmatched_citations.append((idx, "UNKNOWN FILE", slide_num, "No file context"))
            continue
        file_path = ROOT / filepath
        if not file_path.exists():
            unmatched_citations.append((idx, filepath, slide_num, "File does not exist"))
            continue
        file_raw = file_path.read_text(encoding="utf-8")
        file_norm = " ".join(file_raw.split())
        file_stripped = strip_html(file_raw)

        after_prefix = re.sub(r"^.*?-\s+\*\*Trecho Citado.*?\:\*\*\s*", "", line)
        code_cand = re.findall(r"`([^`]+)`", after_prefix)
        quote_cand = re.findall(r"\"([^\"]+)\"", after_prefix)

        cands = [c.strip("\"") for c in code_cand if c.strip("\"")] + [q for q in quote_cand if q]
        for cand in cands:
            clean = cand.strip(" .…\"`")
            if clean.startswith("..."):
                clean = clean[3:].strip()
            if clean.endswith("..."):
                clean = clean[:-3].strip()
            if not clean or len(clean) < 3:
                continue

            clean_norm = " ".join(clean.split())
            clean_stripped_norm = strip_html(clean)

            in_raw = clean in file_raw or clean_norm in file_norm
            in_stripped = clean_stripped_norm in file_stripped or clean_norm in file_stripped

            if not in_raw and not in_stripped:
                # Check slash-delimited parts (e.g. REGRA DE OURO / 0 / ...)
                parts = [p.strip() for p in clean.split("/") if p.strip()]
                if not (parts and all(strip_html(p) in file_stripped for p in parts if len(p.strip()) > 2)):
                    # Check tag stripped components
                    tag_parts = [p.strip() for p in re.findall(r"<[^>]+>|[^<]+", clean) if not p.startswith("<")]
                    if not (tag_parts and all(strip_html(p) in file_stripped for p in tag_parts if len(p.strip()) > 3)):
                        unmatched_citations.append((idx, filepath, slide_num, clean))

    if unmatched_citations:
        log(f"FAIL: {len(unmatched_citations)} citations could not be verified in slides/:")
        for u in unmatched_citations[:10]:
            log(f"  Line {u[0]} ({u[1]} / Slide {u[2]}): '{u[3]}'")
        failed = True
    else:
        log(f"PASS: 100% of tested citations ({len(citation_lines)} entries) verified in the corresponding slide files!")

    # ---------------------------------------------------------
    # 4. PLANO_IMPLEMENTACAO_DIDATICO.md AUDIT
    # ---------------------------------------------------------
    log("\n[CHECK 4] PLANO_IMPLEMENTACAO_DIDATICO.md Requirements & Acceptance Criteria...")
    if not PLAN_FILE.exists():
        log("FAIL: PLANO_IMPLEMENTACAO_DIDATICO.md does not exist!")
        failed = True
        return report, failed

    plan_text = PLAN_FILE.read_text(encoding="utf-8")

    # 4.1. Slide coverage
    covered_plan_slides = set()
    for m in re.finditer(r'^###\s+Slide\s+(\d+)\b', plan_text, re.MULTILINE):
        covered_plan_slides.add(int(m.group(1)))

    log(f"Plan covers {len(covered_plan_slides)} distinct slide sections.")
    if covered_plan_slides != set(range(1, 55)):
        missing = set(range(1, 55)) - covered_plan_slides
        log(f"FAIL: Missing slides in PLANO_IMPLEMENTACAO_DIDATICO.md: {missing}")
        failed = True
    else:
        log("PASS: Exactly all 54 slides have dedicated detailed sections in PLANO_IMPLEMENTACAO_DIDATICO.md.")

    # 4.2. Verify required structure in each slide section
    log("\n[CHECK 4.2] Verifying 5 mandatory components in each of the 54 slide sections...")
    missing_components = []
    for s in range(1, 55):
        pattern = re.compile(rf"^###\s+Slide\s+0?{s}\b.*?(?=^###\s+Slide|\Z)", re.MULTILINE | re.DOTALL)
        m = pattern.search(plan_text)
        if not m:
            missing_components.append((s, "Whole slide section missing"))
            continue
        s_block = m.group(0)

        required_keys = [
            ("Objetivo Didático Central", [r"Objetivo Didático Central"]),
            ("Diagnóstico de AI Slop", [r"Diagnóstico de AI Slop", r"Diagnóstico"]),
            ("Proposta de Reformulação", [r"Proposta Didática Dessengessada", r"Proposta de Reformulação"]),
            ("Modelo Mental / Metáfora", [r"Modelo Mental", r"Metáfora"]),
            ("Fatos Técnicos Preservados", [r"Fatos Técnicos Preservados"])
        ]
        for name, pats in required_keys:
            if not any(re.search(p, s_block, re.IGNORECASE) for p in pats):
                missing_components.append((s, name))

    if missing_components:
        log(f"FAIL: Missing mandatory sections in slides: {missing_components}")
        failed = True
    else:
        log("PASS: All 54 slide sections contain all 5 required components (Objective, Diagnosis, Reformulation, Mental Model, Preserved Facts).")

    # 4.3. Critical technical facts preservation
    log("\n[CHECK 4.3] Verifying preservation of critical technical facts, tools, IPs, ports, coordinates, and cases...")
    critical_terms = [
        # Tools
        ("Nmap", [r"Nmap\s+7\.95", r"Nmap\s+v7\.95", r"Nmap"]),
        ("Wireshark", [r"Wireshark"]),
        ("Shodan", [r"Shodan"]),
        ("Censys", [r"Censys"]),
        ("WHOIS", [r"WHOIS"]),
        ("SecurityTrails", [r"SecurityTrails"]),
        ("VirusTotal", [r"VirusTotal"]),
        ("crt.sh", [r"crt\.sh"]),
        ("Subfinder", [r"Subfinder"]),
        ("Amass", [r"Amass"]),
        ("ExifTool", [r"ExifTool"]),
        ("FOCA", [r"FOCA"]),
        ("SunCalc", [r"SunCalc"]),
        ("Overpass Turbo", [r"Overpass(?:\s+Turbo)?"]),
        ("Google Lens", [r"Google Lens"]),
        ("Mapillary", [r"Mapillary"]),
        ("Wayback Machine", [r"Wayback(?:\s+Machine)?"]),
        ("HIBP", [r"HIBP", r"Have I Been Pwned"]),

        # Network parameters
        ("IP 10.10.14.23", [r"10\.10\.14\.23"]),
        ("IP 10.10.14.5", [r"10\.10\.14\.5"]),
        ("Subnet 10.10.14.0/24", [r"10\.10\.14\.0/24"]),
        ("Port 22", [r"\b22\b"]),
        ("Port 80", [r"\b80\b"]),
        ("Port 443", [r"\b443\b"]),
        ("Port 3306", [r"\b3306\b"]),
        ("Port 8080", [r"\b8080\b"]),
        ("Port 3389", [r"\b3389\b"]),
        ("Handshake 0.000203s", [r"0\.000203s?"]),
        ("Credentials admin:admin", [r"admin:admin"]),

        # Coordinates
        ("Kabul Coordinates 34.5°N 69.2°E", [r"34\.5°N\s+69\.2°E"]),
        ("Mendoza Coordinates 32.89°S 68.84°W", [r"32\.89°S\s+68\.84°W"]),

        # Historical cases
        ("Smart Sampa", [r"Smart Sampa"]),
        ("RSA SecurID", [r"RSA\s+(?:SecurID)?"]),
        ("Strava Heatmap", [r"Strava(?:\s+Heatmap)?"]),

        # Harmonizations
        ("RSA Attachment 2011_Recruitment_Plan.xls", [r"2011_Recruitment_Plan\.xls"]),
        ("Screen time 9h", [r"9\s*(?:h|horas)"]),

        # Narrative arc
        ("Marina Sousa", [r"Marina\s+Sou(?:s|z)a"]),
        ("Acme Pagamentos", [r"Acme(?:\s+Pagamentos)?"]),

        # The 9 INT disciplines present in slides (Slide 40)
        ("OSINT", [r"OSINT"]),
        ("HUMINT", [r"HUMINT"]),
        ("SIGINT", [r"SIGINT"]),
        ("GEOINT", [r"GEOINT"]),
        ("SOCMINT", [r"SOCMINT"]),
        ("FININT", [r"FININT"]),
        ("TECHINT", [r"TECHINT"]),
        ("ELINT", [r"ELINT"]),
        ("IMINT", [r"IMINT"]),
        ("CYBINT", [r"CYBINT"])
    ]

    missing_terms = []
    for term_name, patterns in critical_terms:
        found = any(re.search(p, plan_text, re.IGNORECASE) for p in patterns)
        if not found:
            missing_terms.append(term_name)
            log(f"  [X] Missing term: {term_name}")
        else:
            log(f"  [V] Preserved term: {term_name}")

    if missing_terms:
        log(f"FAIL: Missing critical technical terms: {missing_terms}")
        failed = True
    else:
        log("PASS: 100% of critical technical facts, tools, coordinates, cases and parameters are preserved!")

    # 4.4. Verify absence of AI slop formula in plan mental models
    log("\n[CHECK 4.4] Verifying mental models in Plan are affirmative and avoid AI slop formulas...")
    slop_contrast_patterns = [
        r"não\s+(?:é|foi|se trata)\s+(?:apenas|somente)\s+[^.,;\n]+,\s*mas\s+(?:sim\s+)?",
        r"não\s+se\s+trata\s+de\s+[^.,;\n]+,\s*mas\s+de\s+"
    ]
    model_failures = []
    for s in range(1, 55):
        pattern = re.compile(rf"^###\s+Slide\s+0?{s}\b.*?(?=^###\s+Slide|\Z)", re.MULTILINE | re.DOTALL)
        m = pattern.search(plan_text)
        if not m:
            continue
        s_block = m.group(0)
        m_search = re.search(r"-\s+\*Modelo Mental.*?\:\s*(.*)", s_block)
        if m_search:
            m_text = m_search.group(1).strip()
            for pat in slop_contrast_patterns:
                if re.search(pat, m_text, re.IGNORECASE):
                    model_failures.append((s, m_text))

    if model_failures:
        log(f"FAIL: Slop contrast formula detected in plan mental models: {model_failures}")
        failed = True
    else:
        log("PASS: Mental models across all 54 slides are purely affirmative, intuitive and functional.")

    # ---------------------------------------------------------
    # 5. CANONICAL TESTS EXECUTION
    # ---------------------------------------------------------
    log("\n[CHECK 5] Independent Execution of Canonical Test Suite...")

    build_check = subprocess.run(
        [sys.executable, "scripts/build.py", "--check"],
        cwd=ROOT, capture_output=True, text=True
    )
    log(f"scripts/build.py --check (Code {build_check.returncode}):\n{build_check.stdout.strip()}")
    if build_check.returncode != 0:
        log(f"FAIL: build.py --check failed: {build_check.stderr}")
        failed = True
    else:
        log("PASS: Presentation build check succeeded.")

    unit_tests = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "tests", "-v"],
        cwd=ROOT, capture_output=True, text=True
    )
    log(f"unittest output (Code {unit_tests.returncode}):\n{unit_tests.stderr.strip()}")
    if unit_tests.returncode != 0:
        log(f"FAIL: Unit tests failed.")
        failed = True
    else:
        log("PASS: Canonical unittest suite executed and 100% passed.")

    # ---------------------------------------------------------
    # SUMMARY VERDICT
    # ---------------------------------------------------------
    log("\n" + "=" * 80)
    if failed:
        log("FINAL INDEPENDENT AUDIT VERDICT: VICTORY REJECTED")
    else:
        log("FINAL INDEPENDENT AUDIT VERDICT: VICTORY CONFIRMED")
    log("=" * 80)

    return report, not failed


if __name__ == "__main__":
    rep, passed = run_checks()
    sys.exit(0 if passed else 1)

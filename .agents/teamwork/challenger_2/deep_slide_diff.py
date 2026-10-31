#!/usr/bin/env python3
"""
deep_slide_diff.py - Compare detailed technical entities between original slides and the plan.
Author: Challenger 2
"""

import re
import json
from pathlib import Path

PLAN_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md")
DETAILED_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json")

def analyze():
    plan_text = PLAN_PATH.read_text(encoding="utf-8")
    detailed = json.loads(DETAILED_PATH.read_text(encoding="utf-8"))
    
    # Split plan into slides
    slide_pattern = re.compile(r"^### Slide\s+(\d+)\s+[·-–—]\s*(.+)$", re.MULTILINE)
    matches = list(slide_pattern.finditer(plan_text))
    
    plan_slides = {}
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i+1 < len(matches) else len(plan_text)
        snum = int(matches[i].group(1))
        plan_slides[snum] = plan_text[start:end]
        
    findings = []
    
    for s in detailed:
        snum = int(s["num"])
        body = s["body_html"] + " " + s["notes_html"]
        plan_sec = plan_slides.get(snum, "")
        
        # Check specific entities in original slide
        # 1. Coordinates
        coords = re.findall(r"\b\d{1,3}\.\d+[°\s]*[NSEW]\s+\d{1,3}\.\d+[°\s]*[NSEW]\b", body)
        for c in coords:
            # normalize space
            c_clean = re.sub(r"\s+", " ", c)
            if not re.search(re.escape(c_clean.split()[0]), plan_sec):
                findings.append((snum, "Coordinate", c, "Missing in plan section"))
                
        # 2. Tools mentioned in original HTML
        tools_to_check = [
            "Nmap", "Wireshark", "Shodan", "Censys", "WHOIS", "SecurityTrails", 
            "VirusTotal", "crt.sh", "Subfinder", "Amass", "ExifTool", "FOCA", 
            "SunCalc", "Overpass", "Mapillary", "Google Lens", "Google Earth", 
            "HIBP", "Wayback"
        ]
        for t in tools_to_check:
            if re.search(r"\b" + re.escape(t) + r"\b", body, re.IGNORECASE):
                if not re.search(r"\b" + re.escape(t) + r"\b", plan_sec, re.IGNORECASE):
                    findings.append((snum, "Tool", t, f"Present in original HTML slide {snum:02d} but missing in plan proposal for this slide"))
                    
        # 3. IPs
        ips = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d+)?\b", body)
        for ip in set(ips):
            if ip not in plan_sec:
                findings.append((snum, "IP", ip, f"Present in original HTML slide {snum:02d} but missing in plan section"))
                
        # 4. Ports
        ports = re.findall(r"\b(?:port[a]?\s*|:)(\d{2,5})\b", body, re.IGNORECASE)
        for p in set(ports):
            if p not in plan_sec:
                findings.append((snum, "Port", p, f"Port {p} present in original slide {snum:02d} but missing in plan section"))

    print(f"=== DEEP SLIDE-BY-SLIDE COMPARISON FINDINGS ({len(findings)} items) ===")
    for snum, cat, item, desc in findings:
        print(f"Slide {snum:02d} | [{cat}] {item:20} -> {desc}")

if __name__ == "__main__":
    analyze()

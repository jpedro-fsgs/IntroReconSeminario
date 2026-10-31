#!/usr/bin/env python3
import json
import re
from pathlib import Path

JSON_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json")
slides = json.loads(JSON_PATH.read_text(encoding="utf-8"))

catalog = {
    "tools": set(),
    "protocols_standards": set(),
    "frameworks_methodologies": set(),
    "case_studies": set(),
    "ports_ips_commands": set(),
    "metrics_statistics": set(),
    "dates_years": set()
}

# Extraction patterns
for s in slides:
    text = s['plain_body'] + " " + s['plain_notes']
    
    # Dates/Years
    years = re.findall(r'\b(19\d\d|20\d\d)\b', text)
    for y in years:
        catalog["dates_years"].add(y)
        
    # Ports
    ports = re.findall(r'\b(?:port\w*|porta[s]?|:)\s*(\d{2,5})\b', text, re.IGNORECASE)
    for p in ports:
        catalog["ports_ips_commands"].add(f"Porta {p}")
        
    # IPs
    ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d+)?\b', text)
    for ip in ips:
        catalog["ports_ips_commands"].add(f"IP {ip}")

print("=== DETAILED SLIDE-BY-SLIDE TECHNICAL INVENTORY SCRIPT ===")

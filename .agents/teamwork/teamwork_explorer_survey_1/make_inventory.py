#!/usr/bin/env python3
import json
import re
from pathlib import Path

JSON_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json")
slides = json.loads(JSON_PATH.read_text(encoding="utf-8"))

report = []

for s in slides:
    num = s['num']
    fn = s['file']
    who = s['who']
    title = s['title'].strip()
    h = s['h1'] or s['h2'] or ""
    body = s['plain_body']
    notes = s['plain_notes']
    
    # Extract technical items
    tools = []
    known_tools = [
        "nmap", "wireshark", "shodan", "censys", "whois", "securitytrails", "virustotal",
        "crt.sh", "subfinder", "amass", "exiftool", "foca", "suncalc", "google lens",
        "mapillary", "overpass", "google earth", "bing", "brave", "linkedin", "github",
        "hibp", "wayback", "have i been pwned", "maltego", "spiderfoot"
    ]
    for kt in known_tools:
        if re.search(r'\b' + re.escape(kt) + r'\b', (body + " " + notes).lower()):
            tools.append(kt)
            
    # Technical elements: IPs, ports, commands, standards, frameworks
    ips = re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d+)?\b', body + " " + notes)
    ports = re.findall(r'\b(?:port\w*|porta[s]?|:)\s*(\d{2,5})\b', body + " " + notes, re.IGNORECASE)
    metrics = re.findall(r'\b(?:\d+[\.,]\d+\s*(?:s|ms|h|KB|%)?|\d+\s*(?:h|min|segundos|mil|milhões|câmeras|portas|pacotes|dias|anos))\b', body + " " + notes, re.IGNORECASE)
    frameworks = []
    for fw in ["mitre att&ck", "ta0043", "owasp", "wstg", "certificate transparency", "ct", "tcp/ip", "asn", "dns", "http", "https", "ssh", "mysql", "rdp", "exif", "2fa", "sms", "cve"]:
        if re.search(r'\b' + re.escape(fw) + r'\b', (body + " " + notes).lower()):
            frameworks.append(fw.upper())
            
    report.append({
        "num": num,
        "file": fn,
        "who": who,
        "title": title,
        "header": h,
        "tools": sorted(list(set(tools))),
        "ips": sorted(list(set(ips))),
        "ports": sorted(list(set(ports))),
        "metrics": sorted(list(set(metrics))),
        "frameworks": sorted(list(set(frameworks)))
    })

with open("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/slide_inventory_summary.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=2, ensure_ascii=False)

print("Inventory summary generated successfully.")

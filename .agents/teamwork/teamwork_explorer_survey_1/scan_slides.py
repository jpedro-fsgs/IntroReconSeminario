#!/usr/bin/env python3
import json
import re
from pathlib import Path

JSON_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json")
slides = json.loads(JSON_PATH.read_text(encoding="utf-8"))

# Terms to track
tools_list = [
    "nmap", "wireshark", "shodan", "censys", "whois", "securitytrails", "virustotal",
    "crt.sh", "subfinder", "amass", "exiftool", "foca", "maltego", "spiderfoot",
    "theharvester", "sherlock", "ghunt", "recon-ng", "osint framework", "tinfoleak",
    "geocreepy", "creepy", "overpass turbo", "suncalc", "google dorking", "dorking",
    "wayback machine", "dnsdumpster", "sublist3r", "masscan", "zmap", "tcpdump"
]

banned_words_pt_en = [
    "delve", "foster", "leverage", "utilize", "facilitate", "empower", "streamline",
    "robust", "cutting-edge", "paradigm shift", "game changer", "tapestry", "realm",
    "beacon", "multifaceted", "meticulous", "intricate", "paramount", "transformative",
    "elevate", "embark", "supercharge", "harness", "ever-evolving",
    # Portuguese equivalents commonly seen in AI slop:
    "robusto", "robusta", "robustez", "crucial", "cruciais", "fundamental", "fundamentais",
    "essencial", "essenciais", "ecossistema", "paradigma", "transformador", "meticuloso",
    "multifacetado", "intrincado", "alavancar", "otimizar", "potencializar", "revolucionário",
    "divisor de águas", "vital", "vitais", "reino", "farol", "tapeçaria", "em constante evolução"
]

empty_adverbs_phrases_pt = [
    "simplesmente", "literalmente", "fundamentalmente", "inerentemente", "inevitavelmente",
    "vale notar", "é importante notar", "no final das contas", "quando se trata de",
    "no seu cerne", "no mundo de hoje", "na era de", "na era da", "a realidade é",
    "a verdade é", "em termos de", "a fim de", "daqui para frente", "vamos mergulhar",
    "aqui está o ponto", "não é apenas", "não é só", "destacando", "sublinhando"
]

print("=== SLIDE BY SLIDE ANALYSIS ===")
for s in slides:
    num = s['num']
    title = s['title']
    fn = s['file']
    who = s['who']
    h1 = s['h1']
    h2 = s['h2']
    h3 = ", ".join(s['h3'])
    plain = (s['plain_body'] + " " + s['plain_notes']).lower()
    
    found_tools = [t for t in tools_list if t in plain]
    found_banned = [w for w in banned_words_pt_en if re.search(r'\b' + re.escape(w) + r'\b', plain)]
    found_empty = [p for p in empty_adverbs_phrases_pt if p in plain]
    
    # check for numbers / stats / dates
    stats = re.findall(r'\b(?:\d+[\.,]\d+|\d+%\b|\d{4}\b|\d+\s*(?:mil|milhões|bilhões|câmeras|portas|segundos|minutos|dias|alvos))\b', s['plain_body'] + " " + s['plain_notes'], re.IGNORECASE)
    
    print(f"Slide {num} [{fn}] | {who} | Title: {title}")
    if h1 or h2:
        print(f"   Header: {h1 or h2} {f'({h3})' if h3 else ''}")
    if found_tools:
        print(f"   Tools: {', '.join(found_tools)}")
    if stats:
        print(f"   Stats/Numbers: {list(set(stats))[:6]}")
    if found_banned:
        print(f"   [Slop Alert] Banned/buzzwords: {found_banned}")
    if found_empty:
        print(f"   [Slop Alert] Empty phrases: {found_empty}")
    print()

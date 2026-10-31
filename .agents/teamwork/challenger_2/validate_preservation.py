#!/usr/bin/env python3
"""
validate_preservation.py - Empirical test for exhaustive technical term preservation.
Author: Challenger 2
Target: PLANO_IMPLEMENTACAO_DIDATICO.md
"""

import sys
import re
import json
from pathlib import Path

PLAN_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/PLANO_IMPLEMENTACAO_DIDATICO.md")

CRITICAL_TERMS = {
    # Ferramentas Primárias
    "Nmap": [r"\bNmap\b"],
    "Nmap v7.95": [r"7\.95"],
    "Wireshark": [r"\bWireshark\b"],
    "Shodan": [r"\bShodan\b"],
    "Censys": [r"\bCensys\b"],
    "WHOIS": [r"\bWHOIS\b"],
    "SecurityTrails": [r"\bSecurityTrails\b"],
    "VirusTotal": [r"\bVirusTotal\b"],
    "crt.sh": [r"\bcrt\.sh\b"],
    "Subfinder": [r"\bSubfinder\b"],
    "Amass": [r"\b(?:OWASP\s+)?Amass\b"],
    "ExifTool": [r"\bExifTool\b"],
    "FOCA": [r"\bFOCA\b"],
    "SunCalc": [r"\bSunCalc\b"],
    "Overpass Turbo": [r"\bOverpass(?:\s+Turbo)?\b"],
    
    # Ferramentas Secundárias
    "Mapillary": [r"\bMapillary\b"],
    "Google Lens": [r"\bGoogle Lens\b"],
    "Google Earth": [r"\bGoogle Earth\b"],
    "HIBP / Have I Been Pwned": [r"\b(?:HIBP|Have I Been Pwned)\b"],
    "Wayback Machine": [r"\bWayback(?:\s+Machine)?\b"],

    # IPs e Sub-redes
    "IP 10.10.14.23": [r"10\.10\.14\.23"],
    "IP 10.10.14.5": [r"10\.10\.14\.5\b"],
    "Sub-rede 10.10.14.0/24": [r"10\.10\.14\.0/24"],
    "IP RFC 192.0.2.10": [r"192\.0\.2\.10"],
    "IP RFC 198.51.100.20": [r"198\.51\.100\.20"],

    # Portas
    "Porta 22 (SSH)": [r"\b22(?:/tcp)?\b.*?(?:ssh|OpenSSH)?"],
    "Porta 80 (HTTP)": [r"\b80(?:/tcp)?\b.*?(?:http|nginx)?"],
    "Porta 443 (HTTPS)": [r"\b443(?:/tcp)?\b"],
    "Porta 3306 (MySQL)": [r"\b3306(?:/tcp)?\b.*?(?:mysql|MySQL)?"],
    "Porta 8080 (Jetty)": [r"\b8080(?:/tcp)?\b.*?(?:jetty|Jetty)?"],
    "Porta 3389 (RDP filtrada)": [r"\b3389(?:/tcp)?\b.*?(?:rdp|RDP|filtrada)?"],
    "65.535 portas": [r"65\.?535"],

    # Protocolos e Artefatos
    "Handshake 0.000203s": [r"0\.000203(?:s)?|0,2\s*ms"],
    "Credencial admin:admin": [r"admin:admin"],
    "Base64 YWRtaW46YWRtaW4=": [r"YWRtaW46YWRtaW4="],
    "Comando nmap -sS -sV -p-": [r"nmap\s+-sS"],

    # Estudos de Caso
    "Caso RSA SecurID (2011)": [r"RSA\s+SecurID", r"2011"],
    "Caso Smart Sampa (58 mil câmeras, 11 meses)": [r"Smart\s+Sampa", r"58\s*(?:mil|\.000)", r"11\s+meses"],
    "Caso Strava Heatmap (34.5°N 69.2°E)": [r"Strava", r"34\.5[°\s]*N\s*69\.2[°\s]*E|34\.5.*?69\.2"],
    "Caso Twitter / Cinema (21:04)": [r"Twitter|21:04|cinema"],
    "Caso GEOSINT Ruta 40 / Mendoza (32.89°S 68.84°W)": [r"Ruta\s+40", r"Mendoza", r"32\.89.*?68\.84"],

    # As 9 Disciplinas INT
    "HUMINT": [r"\bHUMINT\b"],
    "GEOINT": [r"\bGEOINT\b"],
    "FININT": [r"\bFININT\b"],
    "ELINT": [r"\bELINT\b"],
    "IMINT": [r"\bIMINT\b"],
    "TECHINT": [r"\bTECHINT\b"],
    "CYBINT": [r"\bCYBINT\b"],
    "SOCMINT / OSINT": [r"\bSOCMINT\b", r"\bOSINT\b"],
    "SIGINT": [r"\bSIGINT\b"],

    # Metodologias e Padrões
    "MITRE ATT&CK TA0043": [r"TA0043|MITRE\s+ATT&CK"],
    "Certificate Transparency (CT)": [r"Certificate\s+Transparency|logs?\s+(?:de\s+)?CT\b"]
}

def test_preservation():
    assert PLAN_PATH.exists(), f"Plan file not found: {PLAN_PATH}"
    lines = PLAN_PATH.read_text(encoding="utf-8").splitlines()
    full_text = "\n".join(lines)
    
    results = {}
    missing = []
    
    for term_name, patterns in CRITICAL_TERMS.items():
        term_matches = []
        all_patterns_satisfied = True
        
        for pat in patterns:
            regex = re.compile(pat, re.IGNORECASE)
            pat_found = False
            for i, line in enumerate(lines, 1):
                if regex.search(line):
                    term_matches.append((i, line.strip()))
                    pat_found = True
            if not pat_found:
                all_patterns_satisfied = False
                
        if all_patterns_satisfied:
            results[term_name] = term_matches
        else:
            missing.append(term_name)
            
    print("=== EMPIRICAL PRESERVATION TEST RESULTS ===")
    print(f"Total critical technical items evaluated: {len(CRITICAL_TERMS)}")
    print(f"Items successfully preserved: {len(results)}")
    print(f"Items missing: {len(missing)}")
    
    if missing:
        print("\n[!] MISSING CRITICAL ITEMS:")
        for m in missing:
            print(f"  - FAIL: {m}")
    else:
        print("\n[+] ALL CRITICAL TECHNICAL TERMS ARE 100% PRESERVED!")
        
    print("\nSample of verified occurrences:")
    for term in list(results.keys())[:15]:
        first_line_num, first_snippet = results[term][0]
        count = len(results[term])
        print(f"  - {term:35} | {count:2d} matches (first at L{first_line_num}: {first_snippet[:60]}...)")
        
    success = (len(missing) == 0)
    return success, {
        "total_evaluated": len(CRITICAL_TERMS),
        "preserved_count": len(results),
        "missing": missing,
        "results": {k: len(v) for k, v in results.items()}
    }

if __name__ == "__main__":
    success, res = test_preservation()
    sys.exit(0 if success else 1)

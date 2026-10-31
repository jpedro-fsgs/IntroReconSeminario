#!/usr/bin/env python3
import json
import re
from pathlib import Path

JSON_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json")
slides = json.loads(JSON_PATH.read_text(encoding="utf-8"))

with open("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/all_slides_dump.txt", "w", encoding="utf-8") as out:
    for s in slides:
        out.write(f"================================================================================\n")
        out.write(f"SLIDE {s['num']} | File: {s['file']} | Speaker: {s['who']}\n")
        out.write(f"Title: {s['title'].strip()}\n")
        out.write(f"H1: {s['h1']} | H2: {s['h2']} | H3: {', '.join(s['h3'])}\n")
        out.write(f"Kicker: {s['kicker']} | Lede: {s['lede']}\n")
        out.write(f"--------------------------------------------------------------------------------\n")
        out.write(f"BODY TEXT:\n{s['plain_body']}\n")
        out.write(f"--------------------------------------------------------------------------------\n")
        out.write(f"SPEAKER NOTES:\n{s['plain_notes']}\n")
        out.write(f"--------------------------------------------------------------------------------\n")
        out.write(f"HTML SNIPPET (first 500 chars):\n{s['body_html'][:500]}\n\n")

print("Dumped all slides to all_slides_dump.txt")

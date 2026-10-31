#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path("/home/myoui/T/Projects/IntroReconSeminário")
SLIDES_DIR = ROOT / "slides"
MANIFEST = SLIDES_DIR / "manifest.json"

manifest_files = json.loads(MANIFEST.read_text(encoding="utf-8"))

all_slides = []

for filename in manifest_files:
    filepath = SLIDES_DIR / filename
    content = filepath.read_text(encoding="utf-8")
    
    # Split by section
    # Slides start with <section and end with </section>
    # Note: build validator ensures horizontal only (no nested sections)
    raw_sections = re.findall(r'(<!--\s*(\d{2})\s*·\s*(.*?)\s*-->\s*<section\b[^>]*>(.*?)</section>)', content, re.DOTALL)
    if not raw_sections:
        # maybe comment is inside section or different format
        raw_sections_alt = re.findall(r'(<section\b[^>]*>(.*?)</section>)', content, re.DOTALL)
        print(f"Warning: file {filename} matched {len(raw_sections_alt)} sections with alt regex")
    
    # Let's parse each section more robustly
    pos = 0
    file_slides = []
    # Find all <!-- XX · Title --> or <section
    pattern = re.compile(r'(?:<!--\s*(\d{2})\s*·\s*(.*?)\s*-->\s*)?<section\b([^>]*)>(.*?)</section>', re.DOTALL)
    for m in pattern.finditer(content):
        num_comment = m.group(1)
        title_comment = m.group(2)
        section_attrs = m.group(3)
        inner_html = m.group(4)
        
        # extract notes
        notes_match = re.search(r'<aside\s+class=["\']notes["\']>(.*?)</aside>', inner_html, re.DOTALL)
        notes = notes_match.group(1).strip() if notes_match else ""
        
        # extract content excluding notes
        body_html = re.sub(r'<aside\s+class=["\']notes["\']>.*?</aside>', '', inner_html, flags=re.DOTALL).strip()
        
        # headers
        h1_match = re.search(r'<h1\b[^>]*>(.*?)</h1>', body_html, re.DOTALL)
        h2_match = re.search(r'<h2\b[^>]*>(.*?)</h2>', body_html, re.DOTALL)
        h3_matches = re.findall(r'<h3\b[^>]*>(.*?)</h3>', body_html, re.DOTALL)
        
        h1 = h1_match.group(1).strip() if h1_match else ""
        h2 = h2_match.group(1).strip() if h2_match else ""
        
        file_slides.append({
            "file": filename,
            "num_comment": num_comment,
            "title_comment": title_comment,
            "section_attrs": section_attrs.strip(),
            "h1": h1,
            "h2": h2,
            "h3": [h.strip() for h in h3_matches],
            "body_html": body_html,
            "notes": notes
        })
    print(f"File {filename}: {len(file_slides)} slides found.")
    all_slides.extend(file_slides)

print(f"Total slides found across all files: {len(all_slides)}")

out_path = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/parsed_slides.json")
out_path.write_text(json.dumps(all_slides, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Saved to {out_path}")

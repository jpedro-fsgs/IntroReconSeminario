#!/usr/bin/env python3
import json
import re
from pathlib import Path
from html import unescape

JSON_PATH = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/parsed_slides.json")
slides = json.loads(JSON_PATH.read_text(encoding="utf-8"))

def strip_tags(html):
    text = re.sub(r'<[^>]+>', ' ', html)
    text = unescape(text)
    return ' '.join(text.split())

detailed_inventory = []

for s in slides:
    num = s['num_comment']
    title = s['title_comment']
    fn = s['file']
    body_html = s['body_html']
    notes_html = s['notes']
    
    # Speaker indicator
    who_match = re.search(r'<p\s+class=["\']who["\']>([^<]+)</p>', body_html)
    who = who_match.group(1).strip() if who_match else ""
    if not who:
        who_notes_match = re.search(r'<p\s+class=["\']who["\']>([^<]+)</p>', notes_html)
        who = who_notes_match.group(1).strip() if who_notes_match else ""
        
    kicker_match = re.search(r'<p\s+class=["\']kicker["\']>([^<]+)</p>', body_html)
    kicker = kicker_match.group(1).strip() if kicker_match else ""
    
    h1 = s['h1']
    h2 = s['h2']
    h3_list = s['h3']
    
    lede_match = re.search(r'<p\s+class=["\']lede["\']>(.*?)</p>', body_html, re.DOTALL)
    lede = strip_tags(lede_match.group(1)) if lede_match else ""
    
    plain_body = strip_tags(body_html)
    plain_notes = strip_tags(notes_html)
    
    detailed_inventory.append({
        "num": num,
        "title": title,
        "file": fn,
        "who": who,
        "kicker": kicker,
        "h1": strip_tags(h1),
        "h2": strip_tags(h2),
        "h3": [strip_tags(h) for h in h3_list],
        "lede": lede,
        "plain_body": plain_body,
        "plain_notes": plain_notes,
        "body_html": body_html,
        "notes_html": notes_html
    })

out_file = Path("/home/myoui/T/Projects/IntroReconSeminário/.agents/teamwork/teamwork_explorer_survey_1/detailed_slides.json")
out_file.write_text(json.dumps(detailed_inventory, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Detailed inventory saved: {len(detailed_inventory)} slides.")

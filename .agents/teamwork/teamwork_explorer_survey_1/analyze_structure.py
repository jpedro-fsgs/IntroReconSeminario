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

for s in slides:
    s['plain_body'] = strip_tags(s['body_html'])
    s['plain_notes'] = strip_tags(s['notes'])

print(f"Loaded {len(slides)} slides.")

# Summary by file
files = {}
for s in slides:
    fn = s['file']
    files.setdefault(fn, []).append(s)

print("\n=== SUMMARY BY FILE ===")
for fn, s_list in files.items():
    nums = f"{s_list[0]['num_comment']} - {s_list[-1]['num_comment']}"
    print(f"{fn} ({len(s_list)} slides: {nums})")

# Check common classes and layout patterns
classes_counts = {}
for s in slides:
    attrs = s['section_attrs']
    m = re.findall(r'class=["\']([^"\']+)["\']', attrs)
    for cls_str in m:
        for c in cls_str.split():
            classes_counts[c] = classes_counts.get(c, 0) + 1

print("\n=== TOP SECTION CLASSES ===")
for c, count in sorted(classes_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
    print(f"  {c}: {count}")

# Check layout elements inside slides
layout_elements = {}
for s in slides:
    body = s['body_html']
    tags = re.findall(r'class=["\']([^"\']+)["\']', body)
    for tag_str in tags:
        for t in tag_str.split():
            layout_elements[t] = layout_elements.get(t, 0) + 1

print("\n=== TOP INNER CLASSES ===")
for t, count in sorted(layout_elements.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"  {t}: {count}")

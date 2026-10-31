import importlib.util
from html.parser import HTMLParser
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("presentation_build", ROOT / "scripts" / "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class ResourceCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.local = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        name = "src" if tag in ("img", "script") else "href" if tag == "link" else None
        if not name or not attrs.get(name):
            return
        parsed = urlsplit(attrs[name])
        if not parsed.scheme and not parsed.netloc and parsed.path:
            self.local.append(unquote(parsed.path))


class PresentationBuildTests(unittest.TestCase):
    def test_root_index_matches_modules(self):
        self.assertEqual(build.assemble(), (ROOT / "index.html").read_text(encoding="utf-8"))

    def test_all_slides_are_horizontal_and_have_notes(self):
        html = build.assemble()
        validator = build.SlideValidator()
        validator.feed(html)
        validator.close()
        self.assertEqual(validator.slides, 66)
        self.assertEqual(validator.depth, 0)
        self.assertEqual([int(number) for number in re.findall(r'<!-- (\d{2}) ·', html)], list(range(1, 67)))

    def test_validator_rejects_nested_slides_and_missing_notes(self):
        with self.assertRaisesRegex(ValueError, "aninhadas"):
            build.SlideValidator().feed('<section><section></section></section>')
        with self.assertRaisesRegex(ValueError, "notas"):
            build.SlideValidator().feed('<section></section>')

    def test_tool_groups_are_sequential_slides(self):
        sections = re.findall(r'<section\b[^>]*>.*?</section\s*>', build.assemble(), re.S)
        names = [
            "Shodan / Censys", "WHOIS", "SecurityTrails / VirusTotal",
            "crt.sh", "Subfinder / Amass", "ExifTool / FOCA",
        ]
        titles = [re.search(r'<h2\b[^>]*>(.*?)</h2>', section, re.S).group(1) for section in sections[31:37]]
        self.assertEqual(titles, names)
        self.assertNotIn('role="dialog"', sections[30])

    def test_theme_shortcut_has_no_persistent_button(self):
        html = build.assemble()
        self.assertNotIn('class="theme-toggle"', html)
        self.assertIn('<script src="js/theme.js"></script>', html)
        self.assertIn('keyCode: 84', (ROOT / "js" / "reveal-init.js").read_text())

    def test_static_site_contains_referenced_resources(self):
        html = build.assemble()
        collector = ResourceCollector()
        collector.feed(html)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            build.build_site(output, html)
            self.assertEqual((output / "index.html").read_text(encoding="utf-8"), html)
            self.assertTrue((output / ".nojekyll").is_file())
            for reference in collector.local:
                with self.subTest(reference=reference):
                    self.assertTrue((output / reference).is_file())
            imports = re.findall(r'@import\s+url\(["\']([^"\']+)["\']\)', (output / "css" / "main.css").read_text())
            self.assertEqual(len(imports), 7)
            for name in imports:
                with self.subTest(css=name):
                    self.assertTrue((output / "css" / name).is_file())
            self.assertTrue((output / "css" / "08-speaker-theme.css").is_file())
            self.assertFalse((output / "slides").exists())
            self.assertFalse((output / "src").exists())

    def test_build_does_not_remove_unknown_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "site"
            output.mkdir()
            user_file = output / "notas-pessoais.txt"
            user_file.write_text("não remover", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "não será removido"):
                build.build_site(output, build.assemble())
            self.assertEqual(user_file.read_text(encoding="utf-8"), "não remover")


if __name__ == "__main__":
    unittest.main()

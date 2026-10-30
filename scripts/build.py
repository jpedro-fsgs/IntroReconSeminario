#!/usr/bin/env python3
"""Monta o deck estático a partir dos blocos horizontais de slides."""

import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import sys


ROOT = Path(__file__).resolve().parent.parent
SLIDES = ROOT / "slides"
TEMPLATE = ROOT / "src" / "presentation.html"
MANIFEST = SLIDES / "manifest.json"
MARKER = "<!-- SLIDES -->"
STATIC_DIRS = ("css", "js", "assets")


class SlideValidator(HTMLParser):
    """Verifica slides horizontais e uma seção de notas por slide."""

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.slides = 0
        self.notes = 0

    def handle_starttag(self, tag, attrs):
        if tag == "section":
            if self.depth:
                raise ValueError("Seções verticais aninhadas não são permitidas")
            self.depth = 1
            self.slides += 1
            self.notes = 0
        elif tag == "aside" and self.depth:
            classes = dict(attrs).get("class", "").split()
            if "notes" in classes:
                self.notes += 1

    def handle_endtag(self, tag):
        if tag == "section":
            if not self.depth:
                raise ValueError("Fechamento de section sem abertura")
            if self.notes != 1:
                raise ValueError(f"O slide {self.slides} precisa de exatamente uma seção de notas")
            self.depth = 0


def slide_modules():
    names = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if not isinstance(names, list) or not names or any(not isinstance(name, str) for name in names):
        raise ValueError("O manifesto precisa conter uma lista de arquivos de slides")
    if len(set(names)) != len(names):
        raise ValueError("O manifesto contém arquivos duplicados")
    unlisted = {path.name for path in SLIDES.glob("*.html")} - set(names)
    if unlisted:
        raise ValueError(f"Arquivos de slides ausentes do manifesto: {', '.join(sorted(unlisted))}")
    modules = []
    for name in names:
        if Path(name).name != name or not name.endswith(".html"):
            raise ValueError(f"Caminho inválido no manifesto: {name}")
        path = SLIDES / name
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Arquivo de slides ausente ou inválido: {name}")
        text = path.read_text(encoding="utf-8")
        validator = SlideValidator()
        validator.feed(text)
        validator.close()
        if validator.depth or not validator.slides:
            raise ValueError(f"O bloco {name} está incompleto ou não contém slides")
        modules.append(text)
    return modules


def assemble():
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count(MARKER) != 1:
        raise ValueError("O template precisa conter exatamente um marcador de slides")
    return template.replace(MARKER, "".join(slide_modules()))


def static_files():
    files = {}
    for dirname in STATIC_DIRS:
        source = ROOT / dirname
        if not source.is_dir() or source.is_symlink():
            raise ValueError(f"Diretório estático ausente ou inválido: {dirname}")
        for path in sorted(source.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Links simbólicos não são publicados: {path}")
            if path.is_file():
                files[path.relative_to(ROOT)] = path
    for required in ("css/main.css", "js/reveal-init.js"):
        if Path(required) not in files:
            raise ValueError(f"Arquivo estático obrigatório ausente: {required}")
    return files


def build_site(output, html):
    """Publica sem remover arquivos existentes que não pertençam ao site."""
    output = Path(output)
    if output.is_symlink():
        raise ValueError("O diretório de saída não pode ser um link simbólico")
    output = output.resolve()
    if output == ROOT or output in ROOT.parents:
        raise ValueError("O diretório de saída não pode ser a raiz do projeto ou seu ancestral")
    for dirname in (*STATIC_DIRS, "slides", "src", "scripts"):
        source = (ROOT / dirname).resolve()
        if output == source or source in output.parents:
            raise ValueError(f"O diretório de saída não pode estar dentro de {dirname}/")

    files = static_files()
    allowed = set(files) | {Path("index.html"), Path(".nojekyll")}
    if output.exists():
        if not output.is_dir():
            raise ValueError("O diretório de saída não é uma pasta")
        for path in output.rglob("*"):
            if path.is_symlink():
                raise ValueError(f"O diretório de saída contém um link simbólico: {path}")
            if path.is_file() and path.relative_to(output) not in allowed:
                raise ValueError(f"Arquivo não reconhecido no diretório de saída; não será removido: {path}")

    output.mkdir(parents=True, exist_ok=True)
    (output / "index.html").write_text(html, encoding="utf-8")
    for relative, source in files.items():
        destination = output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    (output / ".nojekyll").touch()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="verifica se o index.html gerado está atualizado")
    mode.add_argument("--site-only", action="store_true", help="gera _site/ sem alterar o index.html da raiz")
    args = parser.parse_args()
    try:
        html = assemble()
        static_files()
        if args.check:
            index = ROOT / "index.html"
            if not index.is_file() or index.read_text(encoding="utf-8") != html:
                raise ValueError("index.html está desatualizado; execute python3 scripts/build.py")
            print("index.html está atualizado e os blocos são válidos.")
            return
        build_site(ROOT / "_site", html)
        if not args.site_only:
            (ROOT / "index.html").write_text(html, encoding="utf-8")
        print("Site montado em _site/" + ("." if args.site_only else " e index.html atualizado."))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Erro ao montar apresentação: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()

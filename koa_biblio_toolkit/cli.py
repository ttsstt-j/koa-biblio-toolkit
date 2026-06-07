from __future__ import annotations

import argparse
import json
from pathlib import Path

from .ontology import load_acupuncture_ontology
from .parsers import parse_records_from_file
from .pipeline import list_comorbidity_templates


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="koa-biblio-toolkit")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("templates", help="List KOA comorbidity templates")
    subparsers.add_parser("ontology", help="Show acupuncture ontology summary")

    parse_parser = subparsers.add_parser("parse", help="Parse a bibliographic export")
    parse_parser.add_argument(
        "source", choices=["cnki", "wanfang", "wos", "pubmed"], help="Data source"
    )
    parse_parser.add_argument("path", type=Path, help="Path to export file")

    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "templates":
        print("\n".join(list_comorbidity_templates()))
        return 0

    if args.command == "ontology":
        ontology = load_acupuncture_ontology()
        terms = ontology.get("canonical_terms", {})
        print(f"canonical_terms={len(terms)}")
        for term, variants in terms.items():
            print(f"{term}: {', '.join(variants)}")
        return 0

    if args.command == "parse":
        records = parse_records_from_file(args.source, args.path)
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

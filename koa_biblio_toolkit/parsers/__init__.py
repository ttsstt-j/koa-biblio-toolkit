from __future__ import annotations

from pathlib import Path
from typing import Callable

from .endnote import parse_wanfang_endnote
from .pubmed import parse_pubmed_nbib
from .ris import parse_cnki_ris, parse_wos_ris

ParserFunc = Callable[[str | Path], list[dict[str, object]]]


def get_parser(source: str) -> ParserFunc:
    normalized = source.strip().lower()
    parser_map: dict[str, ParserFunc] = {
        "cnki": parse_cnki_ris,
        "wanfang": parse_wanfang_endnote,
        "wos": parse_wos_ris,
        "pubmed": parse_pubmed_nbib,
    }
    if normalized not in parser_map:
        raise ValueError(f"Unsupported source: {source}")
    return parser_map[normalized]


def parse_records_from_file(source: str, path: str | Path) -> list[dict[str, object]]:
    parser = get_parser(source)
    return parser(path)

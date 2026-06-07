from __future__ import annotations

from pathlib import Path

RIS_TAG_MAP = {
    "TI": "title",
    "T1": "title",
    "AU": "authors",
    "A1": "authors",
    "KW": "keywords",
    "PY": "year",
    "Y1": "year",
    "AB": "abstract",
    "JO": "journal",
    "T2": "journal",
}

LIST_FIELDS = {"authors", "keywords"}


def _assign_field(record: dict[str, object], key: str, value: str) -> None:
    if key in LIST_FIELDS:
        values = record.setdefault(key, [])
        if not isinstance(values, list):
            raise TypeError(f"Expected list for field '{key}', got {type(values)!r}")
        values.append(value)
        return
    record[key] = value


def parse_ris_records(text: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    current: dict[str, object] = {}
    last_key: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("ER  -"):
            if current:
                records.append(current)
            current = {}
            last_key = None
            continue

        if len(line) >= 6 and line[2:6] == "  - ":
            tag = line[:2]
            value = line[6:].strip()
            field = RIS_TAG_MAP.get(tag)
            if field and value:
                _assign_field(current, field, value)
                last_key = field
            continue

        if last_key and line.startswith(" "):
            continuation = line.strip()
            if not continuation:
                continue
            existing = current.get(last_key)
            if isinstance(existing, list):
                if existing:
                    existing[-1] = f"{existing[-1]} {continuation}".strip()
            elif isinstance(existing, str):
                current[last_key] = f"{existing} {continuation}".strip()

    if current:
        records.append(current)

    return records


def parse_ris_file(path: str | Path) -> list[dict[str, object]]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return parse_ris_records(handle.read())


def parse_cnki_ris(path: str | Path) -> list[dict[str, object]]:
    return parse_ris_file(path)


def parse_wos_ris(path: str | Path) -> list[dict[str, object]]:
    return parse_ris_file(path)

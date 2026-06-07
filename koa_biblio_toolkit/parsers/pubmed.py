from __future__ import annotations

from pathlib import Path

PUBMED_TAG_MAP = {
    "TI": "title",
    "FAU": "authors",
    "OT": "keywords",
    "DP": "year",
    "AB": "abstract",
    "JT": "journal",
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


def parse_pubmed_nbib_records(text: str) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    current: dict[str, object] = {}
    last_key: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line:
            if current:
                records.append(current)
            current = {}
            last_key = None
            continue

        if len(line) >= 6 and line[4:6] == "- ":
            tag = line[:4].strip()
            value = line[6:].strip()
            field = PUBMED_TAG_MAP.get(tag)
            if field and value:
                _assign_field(current, field, value)
                last_key = field
            continue

        if last_key and line.startswith("      "):
            continuation = line.strip()
            existing = current.get(last_key)
            if continuation and isinstance(existing, str):
                current[last_key] = f"{existing} {continuation}".strip()
            elif continuation and isinstance(existing, list) and existing:
                existing[-1] = f"{existing[-1]} {continuation}".strip()

    if current:
        records.append(current)

    return records


def parse_pubmed_nbib(path: str | Path) -> list[dict[str, object]]:
    with Path(path).open("r", encoding="utf-8") as handle:
        return parse_pubmed_nbib_records(handle.read())

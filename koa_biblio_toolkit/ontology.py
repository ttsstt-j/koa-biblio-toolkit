from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

DEFAULT_ONTOLOGY_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "ontology"
    / "acupuncture_variants.yaml"
)


def load_acupuncture_ontology(path: str | Path | None = None) -> dict[str, Any]:
    ontology_path = Path(path) if path else DEFAULT_ONTOLOGY_PATH
    with ontology_path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data

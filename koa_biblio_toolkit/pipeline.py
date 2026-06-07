from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates" / "comorbidity"


def list_comorbidity_templates() -> list[str]:
    return sorted(path.stem for path in TEMPLATE_DIR.glob("*.yaml"))


def load_comorbidity_template(name: str) -> dict[str, Any]:
    template_path = TEMPLATE_DIR / f"{name}.yaml"
    if not template_path.exists():
        raise FileNotFoundError(f"Unknown comorbidity template: {name}")
    with template_path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}

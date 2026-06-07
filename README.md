# koa-biblio-toolkit

Reproducible bibliometric pipeline for Knee Osteoarthritis (KOA) and acupuncture
research, with first-class support for Chinese-language databases.

## Scope

- KOA + acupuncture bibliometric workflows
- Native parsing scaffolds for CNKI RIS, Wanfang EndNote, WoS RIS, PubMed NBIB
- Curated acupuncture terminology ontology
- Ready-to-use KOA comorbidity templates:
  - sleep disorders
  - depression
  - sarcopenia
  - obesity

## Quick start

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
koa-biblio-toolkit templates
```

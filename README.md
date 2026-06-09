# koa-biblio-toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
[![CI](https://github.com/ttsstt-j/koa-biblio-toolkit/actions/workflows/ci.yml/badge.svg)](https://github.com/ttsstt-j/koa-biblio-toolkit/actions/workflows/ci.yml)

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

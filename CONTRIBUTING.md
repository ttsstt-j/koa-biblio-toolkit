# Contributing

Thank you for improving `koa-biblio-toolkit`.

## Development setup

```bash
python -m pip install -e ".[dev]"
```

## Running tests

```bash
pytest -q
```

## Code style

- Run lint checks with `ruff check .`
- Keep formatting compatible with `black` defaults

## Pull request workflow

1. Create a focused branch for your change.
2. Run `ruff check .` and `pytest -q` locally.
3. Open a pull request with a clear summary and rationale.
4. Address review feedback and keep scope focused on the issue.

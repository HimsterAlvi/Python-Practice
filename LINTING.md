# Linting & formatting

This project uses **Ruff** for both linting and formatting. Rules are defined in `pyproject.toml`.

## Rules (summary)

| Rule | Value |
|------|--------|
| **Max line length** | 100 characters |
| **Indent** | 4 spaces |
| **Quotes** | Double `"` |
| **Target** | Python 3.11+ |

Ruff also enforces: pycodestyle (E/W), Pyflakes (F), import sorting (I), naming (N), pyupgrade (UP), bugbear (B), comprehensions (C4).

## Setup

Install Ruff (in your venv or globally):

```bash
pip install ruff
```

Or with uv:

```bash
uv pip install ruff
```

## Run

**Format code (auto-fix style, wrap long lines):**

```bash
ruff format .
```

**Lint (find issues, auto-fix when possible):**

```bash
ruff check . --fix
```

**Both in one go:**

```bash
ruff format . && ruff check . --fix
```

## Editor integration

- **VS Code / Cursor:** Install the “Ruff” extension. It will use the repo’s `pyproject.toml` and can format on save.
- To enable format on save: set `"editor.formatOnSave": true` and choose Ruff as the default Python formatter.

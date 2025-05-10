# Environment Setup & Reproducibility

## System Info & Tech Stack

- **Hardware**: No hardware limitations. This project is lightweight and runnable on any modern machine, including local setups, Google Colab, and Kaggle.
- **OS**: This project was developed on an Ubuntu-based machine. I tried to maintain this project OS independent. But there is no guarantee that it is.
- **Python Version**: 3.12
- **Python Dependency Manager**: `uv` (v0.6.16)
- **Project Configuration and Dependencies**: Listed in [`pyproject.toml`](../pyproject.toml)

---

## Setup Guides

---

## Reproducibility Notes

- Set seed (`random_state=37`) wherever applicable to ensure consistent results.
- Use `uv sync` to guarantee the same dependency versions across machines.
- Configurations and paths are managed via [`config.yaml`](../src/house_price_prediction/config.yaml)

---

## Pre-commit Hooks

To maintain code quality and consistency, this project uses [pre-commit](https://pre-commit.com/). These hooks run automatically before each commit to catch common issues and enforce standards.

### Setup Instructions

```bash
uv add --dev pre-commit # First, ensure `pre-commit` is installed via `uv`
uv run pre-commit install # Install the git hooks
uv run pre-commit run --all-files # Run all hooks manually (recommended on first setup)
```

### Active Hooks

Configured in the [`.pre-commit-config.yaml`](../.pre-commit-config.yaml) file:

- `trailing-whitespace` - Remove trailing spaces
- `end-of-file-fixer` - Ensure every file ends with a newline
- `check-yaml` - Validate YAML file format
- `check-added-large-files` - Prevent committing large files
- `ruff` - Lint and fix code
- `ruff-format` - Format code

You can view and customize the hooks in the `.pre-commit-config.yaml` file.

### Usage Tips

- Hooks run automatically when you try to `git commit`
- To manually lint or format your code, you can run:

```bash
uv run pre-commit run --all-files
```

- If a hook fails, fix the issue and re-stage the changes before committing again
- For more hooks and usage tips, visit [pre-commit hooks](https://pre-commit.com/hooks.html).
- `pre-commit` hooks ensures code cleanliness and consistency across all contributors and environments.

---

# Contributing Guide

Welcome! Thanks for taking the time to contribute to this project. Your help is greatly appreciated! This document outlines guidelines and best practices to contribute effectively. If you haven't already, please visit [README.md](./README.md) file first before contributing. Get a sense about the project.

## :compass: Table of Contents

- [:rocket: Getting Started](#rocket-getting-started)
- [:gear: Project Development Workflow](#gear-project-development-workflow)
- [:hammer_and_wrench: Tools](#hammer_and_wrench-tools)
- [:question: FAQ](#question-faq)
- [:warning: Known Issues](#warning-known-issues)

---

## :rocket: Getting Started

Follow these steps to set up the project and get it running locally.

### 1. Install Prerequisites

Make sure the following tools are installed and working on your system:

- [Git](https://git-scm.com/downloads) - Version control
- [VS Code](https://code.visualstudio.com/download) - Code editor
- [Docker](https://docs.docker.com/engine/install/) - Containerization platform
- [Dev Containers Extension](https://code.visualstudio.com/docs/devcontainers/containers#_installation) - VS Code extension
- [Dev Container CLI](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli#_installation) - CLI for opening dev containers

> [!NOTE] Using the latest stable versions for best compatibility is recommended.

### 2. Fork the Repository

Fork the upstream repo: [althaf-07/house-price-pred-ml](https://github.com/althaf-07/house-price-pred-ml)

Follow the [GitHub Flow](https://docs.github.com/en/get-started/using-github/github-flow) branching strategy.

### 3. Clone Your Fork

- **HTTPS**

    ```bash
    git clone https://github.com/<your-username>/house-price-pred-ml.git
    ```

- **SSH**

    ```bash
    git clone git@github.com:<your-username>/house-price-pred-ml.git
    ```

### 4. Navigate to the Project Directory

```bash
cd house-price-pred-ml
```

### 5. Add the Upstream Remote

This links your fork to the original repo so you can pull updates later.

- **HTTPS**

    ```bash
    git remote add upstream https://github.com/althaf-07/house-price-pred-ml.git
    ```

- **SSH**

    ```bash
    git remote add upstream git@github.com:althaf-07/house-price-pred-ml.git
    ```

### 6. Set Up the Development Environment

#### Option 1 - Dev Containers (Recommended)

If you want to remove the base Docker image used to build the devcontainer image later, run the following command first:

```bash
docker pull mcr.microsoft.com/vscode/devcontainers/python:3.12-bookworm
```

Then start the devcontainer:

```bash
devcontainer up
```

> **Note:** The first build may take several minutes. Make sure Docker is running before starting.

#### Option 2 - Manual Setup

> [!CAUTION] You can manually replicate the `.devcontainer/` settings locally, but this approach is **not recommended**.

### 7. Create a Local Branch

Always work on a branch - never commit directly to main.

```bash
git checkout -b feature/<short-description>
```

Example:

```bash
git checkout -b feature/add-data-visualization
```

Follow the [Conventional Branch](https://conventional-branch.github.io/) naming specification.

### 8. Make Your Changes

Edit or add files following coding standards and project guidelines.

### 9. Save Your Changes Locally

**Stage changes:**

```bash
git add .
```

**Commit with a clear message:**

```bash
git commit -m "feat: add data visualization for house prices"
```

Follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.

### 10. Push Changes to GitHub

```bash
git push origin feature/<short-description>
```

### 11. Open a Pull Request

1. Go to your fork on GitHub
1. Click **Compare & pull request**
1. Set:
    - **Base branch:** `main` (upstream repo)
    - **Compare branch:** your `feature/...` branch
1. Fill in:
    - **Title:** Short summary of the change
    - **Description:** What you changed and why
    - **Issue links:** `Closes #\<issue-number\>` if applicable

### 12. Get Feedback

- Review comments may be added by maintainers.
- Make requested changes by editing code locally, commit, and push to the same branch - the PR updates automatically.

### 13. Merge

Once approved, a maintainer will merge your PR. If squash merge is used, your PR title will becomes the commit message.

### 14. Keep Your Fork Updated

Regularly sync your fork to avoid merge conflicts:

```bash
git checkout main
git pull --rebase upstream main
git push origin main
```

---

## :gear: Project Development Workflow

1. Build the dev container. This will automatically install and configure all required tools, VS Code extensions, settings, and environment variables. If you need to check how it was built, inspect the files inside the `.devcontainer/` directory. Only contact the author or maintainers if you encounter issues.
1. Define configurations in [src/house_price_pred_ml/config.yaml](./src/house_price_pred_ml/config.yaml). These are grouped and formatted in [src/house_price_pred_ml/config.py](./src/house_price_pred_ml/config.py) for easy importing in other Python files.
1. Run [src/house_price_pred_ml/ingest_data.py](./src/house_price_pred_ml/ingest_data.py) to download the dataset using gdown and save it locally.
1. Use Jupyter Notebooks to explore the dataset interactively and note any issues that need fixing.
1. Implement the cleaning steps in [src/house_price_pred_ml/clean_data.py](./src/house_price_pred_ml/clean_data.py) based on the findings from step 4, then run the script to save the cleaned dataset.
1. Split the cleaned dataset into training and test sets by running [src/house_price_pred_ml/split_data.py](./src/house_price_pred_ml/split_data.py).

---

## :hammer_and_wrench: Tools

Here we specify all the tools and technologies along with their docs that helped to make this project possible.

### Miscellaneous Tools

- [Python](https://docs.python.org/3.12/) - Programming language used widely in ML
- [VS Code](https://code.visualstudio.com/docs) - Advanced code editor
- [Docker](https://docs.docker.com/) - ML API containerization and makes Dev Containers possible
- [Dev Container](https://containers.dev/) - Develop project inside containers
- [Dev Container CLI](https://containers.dev/implementors/reference/) - CLI tool for Dev Container
- [Git](https://git-scm.com/doc) - Version control
- [Github](https://docs.github.com/en) - Git repository hosting platform
- [uv](https://docs.astral.sh/uv/) - Python dependency manager
- [GCP](https://cloud.google.com/docs) - Cloud platform that provides VM to deploy ML service API

### Python Libraries

If you want to see versions of Python libraries, inspect the [pyproject.toml](./pyproject.toml) file.

#### Development-only Libraries

Development-only libraries are those libraries that are not used in [src/house_price_pred_ml/app.py](./src/house_price_pred_ml/app.py) and [src/house_price_pred_ml/predict.py](./src/house_price_pred_ml/predict.py).

- [Gdown](https://github.com/wkentaro/gdown) - Download dataset from Google Drive
- [IPykernel](https://ipython.readthedocs.io/en/latest/) - Kernel for running Jupyter notebooks
- [Klib](https://klib.readthedocs.io/en/stable/) - Provides some helpful utilities
- [Matplotlib](https://matplotlib.org/stable/index.html) - Low-level data visualization library
- [Pre-commit](https://pre-commit.com/) - Enforce code standards
- [Pytest](https://docs.pytest.org/en/stable/contents.html) - Python testing framework
- [PyYaml](https://pyyaml.org/wiki/PyYAMLDocumentation) - Parse, Read, and Interact with YAML files using Python
- [Ruff](https://docs.astral.sh/ruff/) - Python code linter and formatter
- [Seaborn](https://seaborn.pydata.org/) - High-level data visualization library
- [Tabulate](https://github.com/astanin/python-tabulate) - Used with Pandas to make Markdown table of Pandas DataFrames
- [Ty](https://docs.astral.sh/ty/) - Python static type checker

Command to install:

```bash
uv sync --only-dev
```

#### Production-only Libraries

Production-only libraries are those libraries that are only used in [src/house_price_pred_ml/app.py](./src/house_price_pred_ml/app.py) and [src/house_price_pred_ml/predict.py](./src/house_price_pred_ml/predict.py).

- [FastAPI](https://fastapi.tiangolo.com/) - To build APIs
- [Uvicorn](https://www.uvicorn.org/) - ASGI server for serving FastAPI applications
- [Pydantic](https://docs.pydantic.dev/latest/) - Data validation and settings management using Python type hints

Command to install:

```bash
uv sync --no-dev
```

#### Development and Production Libraries (excluding those that are already mentioned in [Development-only Libraries](#development-only-libraries) and [Production-only Libraries](#production-only-libraries))

Development and Production libraries are those libraries that are used throughout the project.

- [NumPy](https://numpy.org/doc/) - Fast and efficient array operations
- [Pandas](https://pandas.pydata.org/docs/) - DataFrame and DataFrame operations
- [Scikit-learn](https://scikit-learn.org/stable/) - Provides algorithms and utilities used in Machine Learning
- [Joblib](https://joblib.readthedocs.io/en/stable/) - Serialize Sklearn estimators

### VS Code Extensions

- [autoDocstring - Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) - Generate template for docstring
- [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker) - Detect typos
- [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) - Dev Container support
- [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) - EditorConfig support
- [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) - TOML file support
- [IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) - Code suggestions and completions
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) - Jupyter notebooks support
- [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one) - Provides some keyboard shortcuts and makes it easy to edit Markdown files
- [Markdown Preview Github Styling](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-preview-github-styles) - Github style Markdown preview
- [markdownlint](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) - Linting for Markdown
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python support
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent) - Correct indentation for Python
- [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) - YAML file support

---

## :question: FAQ

**Q: Can I use my own dotfiles inside a dev container?** **A:** Yes! You can configure your dev container to automatically apply your personal dotfiles. Just point it to your dotfiles repository on GitHub, and they’ll be set up when the container starts. Learn more in the official docs: [Personalizing with dotfile repositories](https://code.visualstudio.com/docs/devcontainers/containers#_personalizing-with-dotfile-repositories).

---

## :warning: Known Issues

- Links in Table of Contents doesn't work in VS Code Markdown Preview because of the emojis in the headers. This problem is not caused by any extensions, as this behavior is still the same when extensions are disabled. Though, this problem is not present in Markdown rendered by GitHub.

---

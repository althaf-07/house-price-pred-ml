import sys
from io import StringIO
from pathlib import Path

import yaml

from house_price_pred_ml.utils.functions import auto_generate


def build_project_tree(
    root_path: Path,
    exclude: set[str],
    ignore_dirs: set[str],
) -> list[tuple[str, str]]:
    """
    Generate a list of formatted directory tree lines and summary dict keys.

    Args:
        root_path: The root directory path to scan.
        exclude: File or directory names to skip entirely.
        ignore_dirs: Directories to show but not traverse.

    Returns:
        A list of (formatted_line, summary_dict_key) tuples.
    """
    lines: list[tuple[str, str]] = []

    def walk_dir(path: Path, prefix: str = ""):
        # Filter excluded entries before sorting
        entries = [e for e in path.iterdir() if e.name not in exclude]
        entries.sort(key=lambda e: (not e.is_dir(), e.name.lower()))

        for i, entry in enumerate(entries):
            connector = "└── " if i == len(entries) - 1 else "├── "
            line = f"{prefix}{connector}{entry.name}{'/' if entry.is_dir() else ''}"
            summary_key = str(entry.relative_to(root_path)) + (
                "/" if entry.is_dir() else ""
            )

            lines.append((line, summary_key))

            # Only recurse if it's a dir and not in ignore list
            if entry.is_dir() and summary_key.rstrip("/") not in ignore_dirs:
                extension = "    " if i == len(entries) - 1 else "│   "
                walk_dir(entry, prefix + extension)

    walk_dir(root_path)
    return lines


def main():
    root_path = Path("./").resolve()
    project_name = root_path.name

    exclude = {"__pycache__", ".directory"}
    ignore_dirs = {
        ".git",
        ".venv",
        "logs",
        "private",
        "reports/figures/univariate",
        "notebooks",
    }

    # Build tree
    lines = build_project_tree(root_path, exclude, ignore_dirs)

    # Calculate alignment
    max_line_len = max(len(line) for line, _ in lines)

    # Load summary descriptions
    tree_yaml_path = Path("./src/house_price_pred_ml/utils/tree.yaml").resolve()
    try:
        with tree_yaml_path.open("r") as file:
            summary_dict = yaml.safe_load(file) or {}
    except FileNotFoundError:
        print(f"Error: Missing {tree_yaml_path}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing {tree_yaml_path}: {e}")
        sys.exit(1)

    # Generate output
    with StringIO() as output:
        output.write("```bash\n")
        output.write(f"{project_name:<{max_line_len}}  # Root project directory\n")
        for line, summary_key in lines:
            description = summary_dict.get(summary_key)
            if description is None:
                print(f"Warning: Missing description for '{summary_key}'")
                description = ""
            if description:
                line = f"{line:<{max_line_len}}  # {description}"
            output.write(line + "\n")
        output.write("```")

        # Update README
        auto_generate(Path("README.md"), output.getvalue(), "PROJECT_STRUCTURE")


if __name__ == "__main__":
    main()

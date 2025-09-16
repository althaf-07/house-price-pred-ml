#!/usr/bin/env bash

echo "Installing dependencies using uv..."
uv sync
echo "Installed dependencies using uv."

echo "Installing dependencies using npm..."
npm install
echo "Installed dependencies using npm."

echo "Installing git hooks..."
uv run pre-commit install
echo "Installed git hooks."

FILE="./private/devcontainer/devcontainer_script.sh"
if [ -f "$FILE" ]; then
    "$FILE"
fi

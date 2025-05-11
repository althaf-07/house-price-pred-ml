#!/bin/bash

FILE="data/raw/entire_data.csv"

if [ ! -f "$FILE" ]; then
    echo "Downloading dataset..."
    uvx gdown \
        --fuzzy "https://drive.google.com/file/d/1y7ZwhqZAKoSLRhYJkebAbi9QXUj0RZcx/view?usp=sharing" \
        -O $(dirname "$FILE")/
    echo "Dataset downloaded"
else
    echo "Dataset already exists at $FILE"
fi

echo "Installing dependencies..."
uv sync
echo "Installed all dependencies"

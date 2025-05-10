#!/usr/bin/bash

# Install dependencies
uv sync

# Download dataset
uvx gdown \
    --fuzzy "https://drive.google.com/file/d/1y7ZwhqZAKoSLRhYJkebAbi9QXUj0RZcx/view?usp=sharing" \
    -O data/raw/

#!/bin/bash

# Directory to copy the dist files to
TARGET_DIR="/Users/maartenderuyter/Documents/development/production/pypi_server/packages"

# Build the project
python -m build

# Create the target directory if it doesn't exist
mkdir -p "$TARGET_DIR"

# Copy the dist files to the target directory
cp dist/* "$TARGET_DIR"
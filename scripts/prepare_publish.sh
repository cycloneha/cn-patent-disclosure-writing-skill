#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[1/2] Running release audit..."
python3 "$ROOT_DIR/skills/cn-patent-disclosure-docx/scripts/public_release_audit.py" "$ROOT_DIR/skills/cn-patent-disclosure-docx"

echo "[2/2] Building release archive..."
python3 "$ROOT_DIR/scripts/package_release.py"

echo "Publish preparation completed."
echo "If you have git installed on your own machine, upload this directory or the generated zip package to GitHub."

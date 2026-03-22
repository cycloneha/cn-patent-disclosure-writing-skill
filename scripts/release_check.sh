#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$ROOT_DIR/skills/cn-patent-disclosure-docx"

python3 "$SKILL_DIR/scripts/public_release_audit.py" "$SKILL_DIR"
echo "Release check completed."

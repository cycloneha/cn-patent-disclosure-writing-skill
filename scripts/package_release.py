#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT.parent / "dist"
ARCHIVE_BASENAME = DIST_DIR / ROOT.name


def main() -> int:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = shutil.make_archive(
        base_name=str(ARCHIVE_BASENAME),
        format="zip",
        root_dir=str(ROOT.parent),
        base_dir=ROOT.name,
    )
    print(f"Created release archive: {archive_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

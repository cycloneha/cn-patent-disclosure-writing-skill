#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def find_generator(explicit: str | None) -> Path | None:
    if explicit:
        path = Path(explicit).expanduser().resolve()
        return path if path.exists() else None

    current = Path.cwd().resolve()
    for directory in [current, *current.parents]:
        candidate = directory / "generate_patent_docx.py"
        if candidate.exists():
            return candidate
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="调用工作区本地 generate_patent_docx.py 渲染专利 DOCX。")
    parser.add_argument("--source", required=True, help="Markdown 主稿路径")
    parser.add_argument("--output", required=True, help="输出 docx 路径")
    parser.add_argument("--template", help="可选模板 docx 路径")
    parser.add_argument("--formula-mode", default="latex", help="公式模式，默认 latex")
    parser.add_argument("--generator", help="显式指定 generate_patent_docx.py 路径")
    args = parser.parse_args()

    generator = find_generator(args.generator)
    if generator is None:
        print("未找到 generate_patent_docx.py。请在工作区根目录提供该脚本，或通过 --generator 显式指定。", file=sys.stderr)
        return 1

    cmd = [
        sys.executable,
        str(generator),
        "--source",
        args.source,
        "--formula-mode",
        args.formula_mode,
        "--output",
        args.output,
    ]
    if args.template:
        cmd.extend(["--template", args.template])

    print("Running:", " ".join(cmd))
    completed = subprocess.run(cmd, check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())

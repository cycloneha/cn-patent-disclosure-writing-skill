#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".py",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".gitignore",
}

FORBIDDEN_FILE_SUFFIXES = {
    ".docx",
    ".pdf",
    ".pptx",
    ".xlsx",
    ".zip",
    ".rar",
    ".7z",
}

PATTERNS = {
    "absolute_path_unix": re.compile(r"(?<!\w)/(home|Users|var|private|tmp)/[^\s\"']+"),
    "absolute_path_windows": re.compile(r"[A-Za-z]:\\\\[^\s\"']+"),
    "relative_parent_ref": re.compile(r"\.\./"),
    "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    "ipv4": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "phone_like": re.compile(r"\b(?:\+?\d[\d -]{7,}\d)\b"),
    "date_like": re.compile(r"\b(?:20\d{2}[-_./]\d{1,2}[-_./]\d{1,2}|\d{2,4}[._-]\d{1,2})\b"),
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        yield path


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in {".gitignore"}


def audit(root: Path) -> list[str]:
    issues: list[str] = []
    for path in iter_files(root):
        suffix = path.suffix.lower()
        rel = path.relative_to(root)

        if suffix in FORBIDDEN_FILE_SUFFIXES:
            issues.append(f"[file] 不建议公开发布二进制或导出文件：{rel}")

        if not is_text_file(path):
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            issues.append(f"[file] 文本文件解码失败，需人工检查：{rel}")
            continue

        for label, pattern in PATTERNS.items():
            for match in pattern.finditer(text):
                snippet = match.group(0)
                issues.append(f"[text:{label}] {rel}: {snippet}")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="公开发布前对技能目录做通用安全与泄露风险审计。")
    parser.add_argument("path", nargs="?", default=".", help="待检查的技能目录")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print("提供的路径不存在或不是目录。", file=sys.stderr)
        return 1

    issues = audit(root)
    if not issues:
        print("未发现明显的公开发布风险项。仍建议进行人工复核。")
        return 0

    print("发现以下需要人工复核的项目：")
    for issue in issues:
        print(issue)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

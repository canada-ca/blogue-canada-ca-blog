#!/usr/bin/env python3
"""Build the PR preview markdown comment body."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote


MARKER = "<!-- preview-urls -->"
PAGE_EXTENSIONS = {".md", ".markdown", ".html"}
POST_RE = re.compile(r"^_posts/(\d{4})-(\d{2})-(\d{2})-([^/]+)\.(md|markdown|html)$")
MAX_OTHER_FILES = 15


@dataclass(frozen=True)
class PreviewTarget:
    base_url: str
    staging_dir: Path


@dataclass(frozen=True)
class PagePreview:
    source_path: str
    language: str
    built_path: str
    url: str


def markdown_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")


def url_path(value: str) -> str:
    return quote(value, safe="/:@")


def markdown_link(label: str, url: str) -> str:
    return f"[{markdown_text(label)}]({url})"


def built_relative_path(language_relative_path: str) -> str | None:
    extension = Path(language_relative_path).suffix.lower()
    if extension not in PAGE_EXTENSIONS:
        return None

    post_match = POST_RE.match(language_relative_path)
    if post_match:
        year, month, day, slug = post_match.groups()[:4]
        return f"{year}/{month}/{day}/{slug}.html"

    if extension in {".md", ".markdown"}:
        return f"{language_relative_path[: -len(extension)]}.html"

    return language_relative_path


def file_exists_under(root: Path, relative_path: str) -> bool:
    return (root / Path(*relative_path.split("/"))).is_file()


def classify_path(path: str, repo: str, sha: str, en: PreviewTarget, fr: PreviewTarget) -> tuple[str, PagePreview | str]:
    target: PreviewTarget | None = None
    language_relative_path: str | None = None
    language: str | None = None

    if path.startswith("en/"):
        target = en
        language_relative_path = path[3:]
        language = "en"
    elif path.startswith("fr/"):
        target = fr
        language_relative_path = path[3:]
        language = "fr"

    if target is not None and language_relative_path is not None and language is not None:
        built_path = built_relative_path(language_relative_path)
        if built_path and file_exists_under(target.staging_dir, built_path):
            url = f"{target.base_url}/{url_path(built_path)}"
            return "page", PagePreview(path, language, built_path, url)

    blob_url = f"https://github.com/{repo}/blob/{sha}/{url_path(path)}"
    return "other", markdown_link(path, blob_url)


def build_other_rows(other_files: list[str]) -> list[str]:
    shown = other_files[:MAX_OTHER_FILES]
    rows = [f"| {item} |" for item in shown]
    overflow = len(other_files) - len(shown)
    if overflow > 0:
        overflow_word = "file" if overflow == 1 else "files"
        rows.append(f"| *...and {overflow} more {overflow_word}* |")
    return rows


def build_page_rows(page_previews: list[PagePreview], en_base: str, fr_base: str) -> list[str]:
    rows_by_page: dict[str, dict[str, PagePreview]] = {}

    for preview in page_previews:
        language_previews = rows_by_page.setdefault(preview.built_path, {})
        existing = language_previews.get(preview.language)
        if existing is None or preview.source_path < existing.source_path:
            language_previews[preview.language] = preview

    rows = [
        f"| Site home | {markdown_link(f'{en_base}/', f'{en_base}/')} | {markdown_link(f'{fr_base}/', f'{fr_base}/')} |"
    ]

    for built_path in sorted(rows_by_page):
        language_previews = rows_by_page[built_path]
        en_preview = language_previews.get("en")
        fr_preview = language_previews.get("fr")
        en_cell = markdown_link(en_preview.source_path, en_preview.url) if en_preview else "—"
        fr_cell = markdown_link(fr_preview.source_path, fr_preview.url) if fr_preview else "—"
        rows.append(f"| {markdown_text(built_path)} | {en_cell} | {fr_cell} |")

    return rows


def build_comment(
    *,
    pr_number: str,
    repo: str,
    sha: str,
    preview_host: str,
    staging_en: str,
    staging_fr: str,
    changed_paths: list[str],
) -> str:
    preview_host = preview_host.rstrip("/")
    en_base = f"{preview_host}/blog/pr-preview/pr-{pr_number}"
    fr_base = f"{preview_host}/blogue/pr-preview/pr-{pr_number}"
    en = PreviewTarget(en_base, Path(staging_en))
    fr = PreviewTarget(fr_base, Path(staging_fr))

    page_previews: list[PagePreview] = []
    other_files: list[str] = []

    for path in changed_paths:
        if not path:
            continue
        kind, preview_or_link = classify_path(path, repo, sha, en, fr)
        if kind == "page":
            if isinstance(preview_or_link, PagePreview):
                page_previews.append(preview_or_link)
        else:
            if isinstance(preview_or_link, str):
                other_files.append(preview_or_link)

    page_rows = build_page_rows(page_previews, en_base, fr_base)
    other_rows = build_other_rows(other_files)
    short_sha = sha[:7]

    lines = [
        MARKER,
        "## 🚀 PR Preview",
        "",
        f"Latest commit: {markdown_link(short_sha, f'https://github.com/{repo}/commit/{sha}')}",
        "",
        "| Page | English | French |",
        "| --- | --- | --- |",
        *page_rows,
        "",
        "## 📁 Other changed files",
        "",
    ]
    if other_rows:
        lines.extend(["| File |", "| --- |", *other_rows, ""])
    else:
        lines.extend(["_None_", ""])

    lines.extend([
        "---",
        "",
        "<sub><em>Preview updates automatically with each commit.</em></sub>",
    ])
    return "\n".join(lines) + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pr", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--sha", required=True)
    parser.add_argument("--preview-host", required=True)
    parser.add_argument("--staging-en", required=True)
    parser.add_argument("--staging-fr", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    changed_paths = [line.rstrip("\r\n") for line in sys.stdin]
    sys.stdout.write(
        build_comment(
            pr_number=args.pr,
            repo=args.repo,
            sha=args.sha,
            preview_host=args.preview_host,
            staging_en=args.staging_en,
            staging_fr=args.staging_fr,
            changed_paths=changed_paths,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

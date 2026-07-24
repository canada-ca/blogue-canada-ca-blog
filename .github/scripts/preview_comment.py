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
MAX_PAGE_PREVIEWS = 25
MAX_OTHER_FILES = 15


@dataclass(frozen=True)
class PreviewTarget:
    base_url: str
    staging_dir: Path


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


def classify_path(path: str, repo: str, sha: str, en: PreviewTarget, fr: PreviewTarget) -> tuple[str, str]:
    target: PreviewTarget | None = None
    language_relative_path: str | None = None

    if path.startswith("en/"):
        target = en
        language_relative_path = path[3:]
    elif path.startswith("fr/"):
        target = fr
        language_relative_path = path[3:]

    if target is not None and language_relative_path is not None:
        built_path = built_relative_path(language_relative_path)
        if built_path and file_exists_under(target.staging_dir, built_path):
            link = markdown_link(path, f"{target.base_url}/{url_path(built_path)}")
            return "page", link

    blob_url = f"https://github.com/{repo}/blob/{sha}/{url_path(path)}"
    return "other", markdown_link(path, blob_url)


def capped_list(items: list[str], maximum: int, overflow_singular: str, overflow_plural: str) -> str:
    if not items:
        return ""

    shown = items[:maximum]
    rendered = "<br>".join(f"- {item}" for item in shown)
    overflow = len(items) - len(shown)
    if overflow > 0:
        overflow_word = overflow_singular if overflow == 1 else overflow_plural
        rendered = f"{rendered}<br>*...and {overflow} more {overflow_word}*"
    return rendered


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

    page_previews: list[str] = []
    other_files: list[str] = []

    for path in changed_paths:
        if not path:
            continue
        kind, link = classify_path(path, repo, sha, en, fr)
        if kind == "page":
            page_previews.append(link)
        else:
            other_files.append(link)

    page_cell = capped_list(page_previews, MAX_PAGE_PREVIEWS, "page", "pages") or "_No content pages changed_"
    other_cell = capped_list(other_files, MAX_OTHER_FILES, "file", "files") or "_No other files changed_"
    short_sha = sha[:7]

    lines = [
        MARKER,
        "Preview published:",
        f"- English: {markdown_link(f'{en_base}/', f'{en_base}/')}",
        f"- French: {markdown_link(f'{fr_base}/', f'{fr_base}/')}",
        "",
        "## 🚀 PR Preview",
        "",
        "| Name | Link(s) |",
        "| --- | --- |",
        f"| **Latest commit** | {markdown_link(short_sha, f'https://github.com/{repo}/commit/{sha}')} |",
        f"| **Page preview** | {page_cell} |",
        f"| **Other changed files** | {other_cell} |",
        "",
        "---",
        "",
        "<sub><em>Preview updates automatically with each commit.</em></sub>",
    ]
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

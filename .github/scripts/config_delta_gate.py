#!/usr/bin/env python3
"""Config delta gate for the staging/production build split.

Compares two built site trees (a staging preview artifact and a same-SHA
production-config artifact) and exits 0 only when every difference is within
the enumerated config delta defined in the migration PRD (FR-33):

  * the baseurl prefix on URLs
  * robots noindex meta
  * robots.txt policy
  * sitemap/feed suppression
  * analytics IDs
  * urlalt canonical/alternate/language-toggle domain swaps

Any OTHER difference (content, layout, missing/extra files) prints the
offending path plus a short diff excerpt and exits 1.

Usage:
    python3 .github/scripts/config_delta_gate.py \
        --staging <dir> --production <dir> --baseurl <prefix>

<dir> trees are compared recursively. Files whose basename is in
IGNORED_FILES (robots.txt, sitemap.xml, feed.xml, flux.xml) are skipped
entirely because they are wholly part of the config delta. Every other file is
normalized (baseurl prefix stripped, noindex meta stripped, analytics ids and
urlalt domain swaps normalized) and then required to be byte-equal.
"""

import argparse
import difflib
import os
import re
import sys

# Files that are wholly part of the config delta: their entire contents are
# allowed to differ between staging and production, so they are not compared.
IGNORED_BASENAMES = {"robots.txt", "sitemap.xml", "feed.xml", "flux.xml"}

# Preview host that serves staging artifacts. Project-specific constant from
# the migration spec (gc-proto/gc-proto.github.io -> test.canada.ca).
STAGING_HOST = "https://test.canada.ca"

# Production urlalt domains, one per language.
PROD_URLALT = {
    "en": "https://blog.canada.ca",
    "fr": "https://blogue.canada.ca",
}

# Normalize the Adobe analytics tracking id URL to a placeholder so staging and
# production analytics ids compare equal (the id is an enumerated delta).
ANALYTICS_RE = re.compile(
    r"assets\.adobedtm\.com/[A-Za-z0-9_/\-]+\.min\.js"
)
ANALYTICS_PLACEHOLDER = "assets.adobedtm.com/ANALYTICS.min.js"

# The staging-only robots noindex meta tag, which the gate strips out.
NOINDEX_RE = re.compile(
    r'<meta name="robots" content="noindex, nofollow"\s*/?>\s*',
    re.IGNORECASE,
)


def collect_files(root):
    """Return {relative_path: absolute_path} for every file under root,
    excluding files whose basename is in IGNORED_BASENAMES."""
    files = {}
    if not os.path.isdir(root):
        return files
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            if name in IGNORED_BASENAMES:
                continue
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root)
            files[rel] = full
    return files


def read_bytes(path):
    with open(path, "rb") as fh:
        return fh.read()


def is_binary(raw):
    """A file is treated as binary (byte-compared, not normalized) when it
    contains NUL bytes. HTML/text files occasionally hold a stray non-UTF-8
    byte but never NUL, so they still get normalized via a latin-1 decode."""
    return b"\x00" in raw


def read_text(raw):
    """Decode bytes for normalization. latin-1 never fails and preserves every
    byte 1:1, so ASCII delta strings (baseurl, noindex, analytics ids, urlalt)
    are found/replaced correctly while any non-ASCII bytes are carried through
    identically in both trees."""
    return raw.decode("latin-1")


def urlalt_map(baseurl):
    """Build the staging->production urlalt replacement map.

    The staging build emits canonical/alternate/og URLs rooted at the preview
    host plus the language-specific preview baseurl:
      EN: <staging_host>/blog/pr-preview/pr-<n>
      FR: <staging_host>/blogue/pr-preview/pr-<n>
    Both language prefixes appear in every build (a build renders both
    languages), so we compute and map both regardless of which --baseurl was
    passed. The first path segment is swapped blog<->blogue to derive the
    other language's prefix.
    """
    en_baseurl = re.sub(r"^/blogue/", "/blog/", baseurl)
    fr_baseurl = re.sub(r"^/blog/", "/blogue/", baseurl)
    return {
        STAGING_HOST + en_baseurl: PROD_URLALT["en"],
        STAGING_HOST + fr_baseurl: PROD_URLALT["fr"],
    }


def normalize(text, baseurl):
    """Normalize a text file's contents so that only non-delta differences
    remain. Order matters: urlalt swaps first (so the full staging urlalt
    prefix is replaced before the baseurl prefix is stripped from relative
    URLs), then baseurl strip, noindex strip, analytics id normalization."""
    # 1. urlalt domain swaps: staging preview host+baseurl -> production domain
    for staging_prefix, prod_prefix in urlalt_map(baseurl).items():
        text = text.replace(staging_prefix, prod_prefix)
    # 2. strip the baseurl prefix from remaining (relative) URLs
    if baseurl:
        text = text.replace(baseurl, "")
    # 3. strip the staging-only robots noindex meta line
    text = NOINDEX_RE.sub("", text)
    # 4. normalize analytics tracking ids to a shared placeholder
    text = ANALYTICS_RE.sub(ANALYTICS_PLACEHOLDER, text)
    return text


def read_normalized(raw, baseurl):
    return normalize(read_text(raw), baseurl)


def short_diff(rel, a_lines, b_lines):
    """Return a short unified-diff excerpt for reporting."""
    diff = list(
        difflib.unified_diff(
            a_lines, b_lines, fromfile=f"staging/{rel}", tofile=f"production/{rel}",
            lineterm="",
        )
    )
    if len(diff) > 40:
        diff = diff[:40] + ["... [truncated] ..."]
    return "\n".join(diff)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Config delta gate.")
    parser.add_argument("--staging", required=True, help="staging site tree")
    parser.add_argument("--production", required=True, help="production site tree")
    parser.add_argument("--baseurl", required=True, help="staging baseurl prefix")
    args = parser.parse_args(argv)

    staging = collect_files(args.staging)
    production = collect_files(args.production)

    staging_paths = set(staging)
    production_paths = set(production)

    only_staging = sorted(staging_paths - production_paths)
    only_production = sorted(production_paths - staging_paths)

    if only_staging or only_production:
        if only_staging:
            print("FAIL: files only in staging:", file=sys.stderr)
            for p in only_staging:
                print("  + " + p, file=sys.stderr)
        if only_production:
            print("FAIL: files only in production:", file=sys.stderr)
            for p in only_production:
                print("  - " + p, file=sys.stderr)
        return 1

    failures = 0
    for rel in sorted(staging_paths):
        s_raw = read_bytes(staging[rel])
        p_raw = read_bytes(production[rel])

        # Binary files (images, fonts, ...): compare raw bytes.
        if is_binary(s_raw) or is_binary(p_raw):
            if s_raw != p_raw:
                print("FAIL: binary file differs outside config delta: " + rel, file=sys.stderr)
                failures += 1
            continue

        s_norm = read_normalized(s_raw, args.baseurl)
        p_norm = read_normalized(p_raw, args.baseurl)
        if s_norm != p_norm:
            print("FAIL: difference outside enumerated config delta: " + rel, file=sys.stderr)
            print(short_diff(rel, s_norm.splitlines(), p_norm.splitlines()), file=sys.stderr)
            failures += 1

    if failures:
        print(f"\n{failures} file(s) differ outside the config delta.", file=sys.stderr)
        return 1

    print("PASS: staging and production differ only within the enumerated config delta.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

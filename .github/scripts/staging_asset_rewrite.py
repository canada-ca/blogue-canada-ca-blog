#!/usr/bin/env python3
"""Staging-only asset reference rewriter.

PR previews of this bilingual Jekyll site are served under a per-PR subpath
(e.g. /blog/pr-preview/pr-224/). The staging Jekyll build already prefixes
template/theme asset references (those that go through Liquid filters like
`relative_url` or baseurl-aware includes) with the preview baseurl, but
CONTENT-authored references in posts -- raw `<img src="/images/foo.png">` in
Markdown/HTML, plus `href` links to local files -- stay root-absolute and so
resolve to the domain root under the preview subpath, 404'ing. Production is
unaffected because its baseurl is empty.

This script is a post-processing pass run ONLY on staging build trees. It walks
the built site and, in `*.html` files, prepends the baseurl to root-absolute
values of `src`, `href`, `poster` and `srcset` attributes; in `*.css` files it
prepends the baseurl to root-absolute `url(...)` values. It is deliberately
conservative: it only rewrites values that start with a single `/` and are not
already prefixed with the baseurl, leaving protocol-relative `//` external URLs
(prefixing them would corrupt them into a path on the preview host and break
analytics/survey assets -- they resolve correctly on their own), full http/https
URLs, anchors `#`, `mailto:`, `tel:` and `data:` untouched. The rewrite is
idempotent -- running it twice is a no-op because already-prefixed values are
skipped.

The companion config delta gate (config_delta_gate.py) normalizes the staging
tree by stripping the baseurl prefix before comparing to production, so the
extra prefixed references this script introduces normalize back to the
production form and the gate keeps passing.

Usage:
    python3 .github/scripts/staging_asset_rewrite.py \
        --root <built-site-dir> --baseurl <prefix>
"""

import argparse
import os
import re
import sys


# Attribute names whose double-quoted values we rewrite. The negative
# lookbehind prevents matching the tail of a hyphenated attribute such as
# `data-src` or `data-href` (which are out of scope). Captures the attribute
# name (group 1) and the value (group 2).
ATTR_RE = re.compile(r'(?<![\w-])(src|href|poster)\s*=\s*"([^"]*)"', re.IGNORECASE)

# srcset is rewritten separately because its value is a comma-separated list of
# candidate URLs (each optionally followed by a width/density descriptor).
SRCSET_RE = re.compile(r'(?<![\w-])srcset\s*=\s*"([^"]*)"', re.IGNORECASE)

# CSS url(...) values. The optional quote char (group 1) is mirrored back; the
# URL is group 2.
CSS_URL_RE = re.compile(r'url\(\s*(["\']?)([^"\')]+)\1\s*\)', re.IGNORECASE)


def needs_prefix(value, baseurl):
    """True when `value` is a root-absolute path that should receive the
    baseurl prefix.

    A value is rewritten only when it starts with a single `/` (root-absolute)
    and is not already prefixed with the baseurl (which keeps the pass
    idempotent). Values starting with `//` are protocol-relative external URLs
    and are left alone -- prefixing them would corrupt them into a path on the
    preview host (breaking analytics/survey assets); they resolve correctly on
    their own under the preview subpath. Everything else (http/https URLs,
    anchors, mailto:, tel:, data:, relative paths) does not start with `/` and
    is left alone.
    """
    if not value.startswith('/'):
        return False
    if value.startswith('//'):
        return False
    if value == baseurl or value.startswith(baseurl + '/'):
        return False
    return True


def prefix_value(value, baseurl):
    return baseurl + value if needs_prefix(value, baseurl) else value


def rewrite_srcset(value, baseurl):
    """Rewrite each comma-separated candidate URL in a srcset value.

    Each candidate is `URL` or `URL descriptor`. The URL is the
    whitespace-separated leading token; the remainder (descriptor) is preserved
    verbatim. Empty srcset values are returned unchanged.
    """
    candidates = value.split(',')
    out = []
    for candidate in candidates:
        stripped = candidate.strip()
        if not stripped:
            out.append(candidate)
            continue
        parts = stripped.split(None, 1)
        url = parts[0]
        descriptor = parts[1] if len(parts) > 1 else ''
        new_url = prefix_value(url, baseurl)
        # Preserve leading whitespace from the original candidate so comma
        # alignment is unchanged; trailing whitespace before the descriptor is
        # collapsed to a single space.
        leading = candidate[:len(candidate) - len(candidate.lstrip())]
        if descriptor:
            out.append(leading + new_url + ' ' + descriptor)
        else:
            out.append(leading + new_url)
    return ','.join(out)


def rewrite_html(text, baseurl):
    def attr_repl(m):
        return m.group(1) + '="' + prefix_value(m.group(2), baseurl) + '"'

    def srcset_repl(m):
        return 'srcset="' + rewrite_srcset(m.group(1), baseurl) + '"'

    text = SRCSET_RE.sub(srcset_repl, text)
    text = ATTR_RE.sub(attr_repl, text)
    return text


def rewrite_css(text, baseurl):
    def url_repl(m):
        quote = m.group(1)
        return 'url(' + quote + prefix_value(m.group(2), baseurl) + quote + ')'

    return CSS_URL_RE.sub(url_repl, text)


def process_file(path, baseurl, stats):
    lower = path.lower()
    if lower.endswith('.html'):
        kind = 'html'
    elif lower.endswith('.css'):
        kind = 'css'
    else:
        return

    stats['scanned'] += 1
    try:
        with open(path, 'rb') as fh:
            raw = fh.read()
    except OSError as exc:
        print(f"ERROR: could not read {path}: {exc}", file=sys.stderr)
        raise

    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError:
        # Not a UTF-8 text file (e.g. mislabelled binary); leave untouched.
        return

    if kind == 'html':
        new_text = rewrite_html(text, baseurl)
    else:
        new_text = rewrite_css(text, baseurl)

    if new_text == text:
        return

    try:
        with open(path, 'wb') as fh:
            fh.write(new_text.encode('utf-8'))
    except OSError as exc:
        print(f"ERROR: could not write {path}: {exc}", file=sys.stderr)
        raise

    stats['changed'] += 1
    # Count rewritten references by diffing matches before/after is awkward;
    # approximate by counting qualifying root-absolute references in the
    # original text.
    stats['rewritten'] += count_rewritten_refs(text, baseurl)


def count_rewritten_refs(text, baseurl):
    n = 0

    def attr_count(m):
        nonlocal n
        if needs_prefix(m.group(2), baseurl):
            n += 1
        return m.group(0)

    def srcset_count(m):
        nonlocal n
        for candidate in m.group(1).split(','):
            stripped = candidate.strip()
            if not stripped:
                continue
            url = stripped.split(None, 1)[0]
            if needs_prefix(url, baseurl):
                n += 1
        return m.group(0)

    SRCSET_RE.sub(srcset_count, text)
    ATTR_RE.sub(attr_count, text)

    def url_count(m):
        nonlocal n
        if needs_prefix(m.group(2), baseurl):
            n += 1
        return m.group(0)

    CSS_URL_RE.sub(url_count, text)
    return n


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Staging-only asset reference rewriter.",
    )
    parser.add_argument('--root', required=True,
                        help='built site directory to rewrite in place')
    parser.add_argument('--baseurl', required=True,
                        help='preview baseurl prefix to prepend (e.g. /blog/pr-preview/pr-224)')
    args = parser.parse_args(argv)

    baseurl = args.baseurl.rstrip('/')
    if not baseurl.startswith('/'):
        print("ERROR: --baseurl must start with '/'", file=sys.stderr)
        return 2

    root = args.root
    if not os.path.isdir(root):
        print(f"ERROR: --root is not a directory: {root}", file=sys.stderr)
        return 2

    stats = {'scanned': 0, 'changed': 0, 'rewritten': 0}
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            process_file(os.path.join(dirpath, name), baseurl, stats)

    print(
        "staging_asset_rewrite: scanned {scanned} files, "
        "changed {changed} files, rewrote {rewritten} references".format(**stats)
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())

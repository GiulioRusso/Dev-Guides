"""MkDocs hook: generate heading ids the way GitHub does, so the in-guide anchor links work on both."""
import re
import unicodedata

from markdown.extensions import toc


def github_slug(value, separator="-"):
    value = value.strip().lower()
    return "".join(c for c in value if c in " -_" or unicodedata.category(c)[0] in "LMN").replace(" ", "-")


def github_unique(id, ids):
    # GitHub dedupes as name, name-1, name-2 (Python-Markdown uses name_1)
    base, n = id, 0
    while id in ids or not id:
        n += 1
        id = f"{base}-{n}"
    ids.add(id)
    return id


toc.unique = github_unique


def on_config(config):
    config.mdx_configs.setdefault("toc", {})["slugify"] = github_slug
    return config

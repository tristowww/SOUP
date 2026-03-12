#!/usr/bin/env python3
"""
normalize_text.py — Normalize common PDF-extraction character artifacts in markdown.

Usage:
    python normalize_text.py INPUT.md OUTPUT.md

Handles:
    - Curly/smart quotes → straight quotes
    - En-dashes in page ranges → hyphens
    - Ligatures (fi, fl) → separate characters
    - Non-breaking spaces → regular spaces
    - Soft hyphens → removed (word rejoined)
    - Zero-width characters → removed
    - Multiple consecutive blank lines → single blank line
"""

import re
import sys


def normalize(text: str) -> str:
    """Apply all character normalizations to text."""

    # ── Smart/curly quotes → straight quotes ──
    text = text.replace("\u2018", "'")   # left single curly
    text = text.replace("\u2019", "'")   # right single curly / apostrophe
    text = text.replace("\u201C", '"')   # left double curly
    text = text.replace("\u201D", '"')   # right double curly
    text = text.replace("\u201A", "'")   # single low-9
    text = text.replace("\u201E", '"')   # double low-9
    text = text.replace("\u2039", "'")   # single left angle
    text = text.replace("\u203A", "'")   # single right angle
    text = text.replace("\u00AB", '"')   # left guillemet
    text = text.replace("\u00BB", '"')   # right guillemet

    # ── En-dashes in page/number ranges → hyphens ──
    # Match patterns like 60–84, 2019–2023, pp. 12–45
    text = re.sub(r'(\d)\u2013(\d)', r'\1-\2', text)

    # ── Ligatures → separate characters ──
    text = text.replace("\uFB01", "fi")
    text = text.replace("\uFB02", "fl")
    text = text.replace("\uFB03", "ffi")
    text = text.replace("\uFB04", "ffl")

    # ── Non-breaking spaces → regular spaces ──
    text = text.replace("\u00A0", " ")   # standard NBSP
    text = text.replace("\u202F", " ")   # narrow NBSP
    text = text.replace("\u2007", " ")   # figure space
    text = text.replace("\u2060", "")    # word joiner (zero-width NBSP)

    # ── Soft hyphens → remove (rejoin word) ──
    text = text.replace("\u00AD", "")

    # ── Zero-width characters → remove ──
    text = text.replace("\u200B", "")    # zero-width space
    text = text.replace("\u200C", "")    # zero-width non-joiner
    text = text.replace("\u200D", "")    # zero-width joiner
    text = text.replace("\uFEFF", "")    # byte order mark

    # ── Collapse multiple blank lines → single blank line ──
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text


def main():
    if len(sys.argv) < 3:
        print("Usage: python normalize_text.py INPUT.md OUTPUT.md")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    result = normalize(content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Normalized: {input_path} -> {output_path}")


if __name__ == "__main__":
    main()

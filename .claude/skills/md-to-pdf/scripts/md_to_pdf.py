#!/usr/bin/env python3
"""
md_to_pdf.py — Convert a markdown file to a formatted PDF using reportlab.

Usage:
    python md_to_pdf.py INPUT.md OUTPUT.pdf

Handles: headings, bold/italic, bullet lists, tables, horizontal rules,
inline code, blockquotes, and metadata lines.
"""

import re
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable,
)

# ── Configurable colors ──────────────────────────────────────────────────────
COLORS = {
    "title": "#1a1a2e",
    "h2": "#2c3e50",
    "h3": "#34495e",
    "h4": "#2c3e50",
    "header_bg": "#2c3e50",
    "header_fg": "#f5f5f5",
    "alt_row": "#f5f6fa",
    "grid": "#bdc3c7",
    "hr": "#cccccc",
    "meta": "#555555",
    "sub_bullet": "#333333",
}

PAGE_WIDTH = letter[0] - 1.5 * inch  # usable width with 0.75in margins


# ── Build styles (prefixed with md_ to avoid reportlab collisions) ────────
def build_styles():
    """Create custom ParagraphStyles that won't collide with built-in names.

    reportlab's getSampleStyleSheet() already defines: Title, Heading1-6,
    Normal, Bullet, Code, Italic, Definition, OrderedList, UnorderedList.
    We prefix everything with 'md_' to stay safe.
    """
    base = getSampleStyleSheet()
    s = {}

    def add(name, parent_name, **kw):
        s[name] = ParagraphStyle(name, parent=base[parent_name], **kw)

    add("md_title", "Title", fontSize=20, spaceAfter=4,
        textColor=colors.HexColor(COLORS["title"]))
    add("md_meta", "Normal", fontSize=10, spaceAfter=2,
        textColor=colors.HexColor(COLORS["meta"]))
    add("md_h2", "Heading2", fontSize=14, spaceBefore=18, spaceAfter=8,
        textColor=colors.HexColor(COLORS["h2"]))
    add("md_h3", "Heading3", fontSize=12, spaceBefore=12, spaceAfter=6,
        textColor=colors.HexColor(COLORS["h3"]))
    add("md_h4", "Heading4", fontSize=11, spaceBefore=10, spaceAfter=4,
        textColor=colors.HexColor(COLORS["h4"]))
    add("md_body", "Normal", fontSize=9.5, leading=13, spaceAfter=6)
    add("md_bullet", "Normal", fontSize=9.5, leading=13,
        leftIndent=18, bulletIndent=6, spaceAfter=3)
    add("md_sub_bullet", "Normal", fontSize=9, leading=12,
        leftIndent=36, bulletIndent=24, spaceAfter=2,
        textColor=colors.HexColor(COLORS["sub_bullet"]))
    add("md_code_block", "Code", fontSize=8.5, leading=11,
        leftIndent=12, spaceAfter=6, spaceBefore=4,
        backColor=colors.HexColor("#f4f4f4"))
    add("md_blockquote", "Italic", fontSize=9.5, leading=13,
        leftIndent=24, spaceAfter=6, textColor=colors.HexColor("#555555"))
    return s


# ── Text processing helpers ───────────────────────────────────────────────

def escape_xml(text):
    """Escape characters that break reportlab's XML paragraph parser.

    Must be called BEFORE applying inline markup (bold/italic/code tags),
    because those tags use < and > intentionally.
    """
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def apply_inline_markup(text):
    """Convert markdown inline formatting to reportlab XML tags.

    Call AFTER escape_xml so that our generated tags aren't escaped.
    Order matters: bold before italic to handle **nested *markup***.
    """
    # Inline code: `code` → <font name="Courier">code</font>
    text = re.sub(r'`([^`]+)`', r'<font name="Courier">\1</font>', text)
    # Bold: **text** or __text__
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'__(.+?)__', r'<b>\1</b>', text)
    # Italic: *text* or _text_  (but not inside words like file_name)
    text = re.sub(r'(?<!\w)\*([^*]+?)\*(?!\w)', r'<i>\1</i>', text)
    text = re.sub(r'(?<!\w)_([^_]+?)_(?!\w)', r'<i>\1</i>', text)
    return text


def process_text(raw):
    """Full pipeline: escape then apply markup."""
    return apply_inline_markup(escape_xml(raw))


# ── Table builder ─────────────────────────────────────────────────────────

def build_table(rows, styles):
    """Convert parsed markdown table rows into a styled reportlab Table."""
    if not rows or len(rows) < 1:
        return None

    # Wrap each cell in a Paragraph for word-wrap support
    cell_style = styles["md_body"]
    para_data = []
    for i, row in enumerate(rows):
        para_row = []
        for cell in row:
            txt = process_text(cell.strip())
            para_row.append(Paragraph(txt, cell_style))
        para_data.append(para_row)

    # Compute proportional column widths
    n_cols = max(len(r) for r in rows)
    col_w = PAGE_WIDTH / n_cols

    t = Table(para_data, colWidths=[col_w] * n_cols, repeatRows=1)

    hdr_bg = colors.HexColor(COLORS["header_bg"])
    hdr_fg = colors.HexColor(COLORS["header_fg"])
    alt_bg = colors.HexColor(COLORS["alt_row"])
    grid_c = colors.HexColor(COLORS["grid"])

    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), hdr_bg),
        ("TEXTCOLOR", (0, 0), (-1, 0), hdr_fg),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("FONTSIZE", (0, 1), (-1, -1), 8.5),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("GRID", (0, 0), (-1, -1), 0.5, grid_c),
    ]
    for i in range(1, len(para_data)):
        if i % 2 == 0:
            cmds.append(("BACKGROUND", (0, i), (-1, i), alt_bg))
    t.setStyle(TableStyle(cmds))
    return t


# ── Markdown parser ───────────────────────────────────────────────────────

def parse_md_to_story(md_text, styles):
    """Parse markdown text into a list of reportlab flowables."""
    lines = md_text.split("\n")
    story = []
    i = 0
    # Track whether we've passed the first heading (metadata zone)
    past_first_section = False

    def hr():
        return HRFlowable(
            width="100%", thickness=0.5,
            color=colors.HexColor(COLORS["hr"]),
            spaceAfter=10, spaceBefore=6,
        )

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # ── Blank line ──
        if not stripped:
            i += 1
            continue

        # ── Horizontal rule ──
        if re.match(r'^-{3,}$|^\*{3,}$|^_{3,}$', stripped):
            story.append(hr())
            i += 1
            continue

        # ── Headings ──
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if heading_match:
            level = len(heading_match.group(1))
            text = process_text(heading_match.group(2))
            if level == 1:
                story.append(Paragraph(text, styles["md_title"]))
                past_first_section = True
            elif level == 2:
                story.append(Paragraph(text, styles["md_h2"]))
                past_first_section = True
            elif level == 3:
                story.append(Paragraph(text, styles["md_h3"]))
            else:
                story.append(Paragraph(text, styles["md_h4"]))
            i += 1
            continue

        # ── Table ──
        if "|" in stripped and stripped.startswith("|"):
            table_rows = []
            while i < len(lines) and "|" in lines[i].strip() and lines[i].strip().startswith("|"):
                row_text = lines[i].strip()
                # Skip separator rows like |---|---|
                if re.match(r'^\|[\s\-:|]+\|$', row_text):
                    i += 1
                    continue
                cells = [c.strip() for c in row_text.split("|")[1:-1]]
                table_rows.append(cells)
                i += 1
            tbl = build_table(table_rows, styles)
            if tbl:
                story.append(tbl)
                story.append(Spacer(1, 8))
            continue

        # ── Blockquote ──
        if stripped.startswith(">"):
            quote_text = process_text(stripped.lstrip("> "))
            story.append(Paragraph(quote_text, styles["md_blockquote"]))
            i += 1
            continue

        # ── Code block (fenced) ──
        if stripped.startswith("```"):
            i += 1
            code_lines = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(escape_xml(lines[i]))
                i += 1
            if i < len(lines):
                i += 1  # skip closing ```
            code_text = "<br/>".join(code_lines)
            story.append(Paragraph(code_text, styles["md_code_block"]))
            continue

        # ── Bullet list ──
        bullet_match = re.match(r'^(\s*)[*\-+]\s+(.+)$', stripped)
        if bullet_match:
            # Check indent level from the original line, not stripped
            indent = len(line) - len(line.lstrip())
            text = process_text(bullet_match.group(2))
            if indent >= 2:
                story.append(Paragraph(f"\u2013  {text}", styles["md_sub_bullet"]))
            else:
                story.append(Paragraph(f"\u2022  {text}", styles["md_bullet"]))
            i += 1
            continue

        # ── Metadata lines (bold-key: value pattern near top of doc) ──
        if not past_first_section and re.match(r'^\*\*[^*]+\*\*', stripped):
            text = process_text(stripped)
            story.append(Paragraph(text, styles["md_meta"]))
            i += 1
            continue

        # ── Regular paragraph ──
        # Accumulate consecutive non-special lines into one paragraph
        para_lines = [stripped]
        i += 1
        while i < len(lines):
            next_stripped = lines[i].strip()
            if (not next_stripped
                    or next_stripped.startswith("#")
                    or next_stripped.startswith("|")
                    or next_stripped.startswith(">")
                    or next_stripped.startswith("```")
                    or re.match(r'^-{3,}$|^\*{3,}$|^_{3,}$', next_stripped)
                    or re.match(r'^[*\-+]\s+', next_stripped)):
                break
            para_lines.append(next_stripped)
            i += 1
        full_text = process_text(" ".join(para_lines))
        story.append(Paragraph(full_text, styles["md_body"]))

    return story


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 3:
        print("Usage: python md_to_pdf.py INPUT.md OUTPUT.pdf")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    styles = build_styles()

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
    )

    story = parse_md_to_story(md_text, styles)

    if not story:
        print("Warning: no content parsed from markdown.")
        sys.exit(1)

    doc.build(story)
    print(f"PDF created: {output_path}")


if __name__ == "__main__":
    main()

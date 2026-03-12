---
name: md-to-pdf
description: Convert markdown files to nicely formatted PDFs using reportlab. Use this skill whenever the user wants to convert a .md file to .pdf output. Handles headings, bold/italic, bullet lists, tables, horizontal rules, and code blocks.
---

# Markdown to PDF Conversion Skill

## Overview

Converts markdown (.md) files to professionally formatted PDFs using Python's `reportlab` library. The process parses markdown elements and maps them to reportlab flowables with consistent styling.

## When to Use

- User asks to convert a `.md` file to PDF
- User asks to "make a PDF" from markdown content
- User wants a formatted/printable version of a markdown document

## Process

### Step 1: Ensure reportlab is installed

```bash
pip install reportlab
```

### Step 2: Run the converter script

```bash
python .claude/skills/md-to-pdf/scripts/md_to_pdf.py INPUT.md OUTPUT.pdf
```

The script handles all markdown parsing and PDF generation automatically.

### Step 3: Verify output

Read/open the generated PDF to confirm it rendered correctly.

## What the Converter Handles

| Markdown Element | PDF Rendering |
|-----------------|---------------|
| `# Heading 1` | Title style, 20pt, dark navy |
| `## Heading 2` | Section header, 14pt, dark slate |
| `### Heading 3` | Subsection, 12pt |
| `#### Heading 4` | Sub-subsection, 11pt |
| `**bold**` | Bold inline text |
| `*italic*` | Italic inline text |
| `- item` / `* item` | Bulleted list with indent |
| `  - sub-item` | Sub-bullet with deeper indent |
| `\| col \| col \|` tables | Styled tables with header row, alternating row colors, grid |
| `---` | Horizontal rule divider |
| `` `code` `` | Monospace inline text |
| `> blockquote` | Indented italic block |
| Body text | 9.5pt with comfortable leading |
| `**Key:** value` metadata lines | Smaller meta style at document top |

## Known Issues & Edge Cases

### 1. Reserved Style Names (CRITICAL)

reportlab's `getSampleStyleSheet()` pre-defines these style names: `Title`, `Heading1`–`Heading6`, `Normal`, `Bullet`, `Definition`, `Code`, `Italic`, `OrderedList`, `UnorderedList`.

**Fix:** The script prefixes all custom styles with `md_` (e.g., `md_bullet`, `md_title`) to avoid collisions.

### 2. HTML Entity Encoding

reportlab Paragraphs use an XML parser internally. Bare `&` characters cause XML parse errors.

**Fix:** The script escapes `&` to `&amp;` (and `<`/`>` outside of markup tags) before passing text to Paragraph.

### 3. Unicode Characters

reportlab's built-in Helvetica font lacks many Unicode glyphs (subscripts, superscripts, exotic symbols). They render as black boxes.

**Fix:** Stick to standard ASCII + common Unicode (em-dash, bullet, etc.). Use `<sub>`/`<super>` tags instead of Unicode sub/superscript characters.

### 4. Long Table Cells

Very long text in table cells can overflow or cause layout breaks.

**Fix:** The script wraps table cell content in Paragraph objects and uses proportional column widths based on page width.

### 5. Markdown Variations

Not all markdown is equal. The parser handles the most common patterns:
- ATX headings (`#`, `##`, etc.)
- Pipe tables with `|---|` separator rows
- Unordered lists with `-`, `*`, or `+`
- Bold with `**`, italic with `*` or `_`
- Inline code with backticks

**Not supported:** Nested tables, images, footnotes, definition lists, task lists.

### 6. Page Breaks

Very large documents may need manual page break hints. The script inserts automatic page breaks via reportlab's flow layout, but `---` (horizontal rules) serve as natural visual section breaks.

## Customization

To adjust styling, edit the color/size constants at the top of `md_to_pdf.py`:

```python
COLORS = {
    "title": "#1a1a2e",
    "h2": "#2c3e50",
    "h3": "#34495e",
    "header_bg": "#2c3e50",
    "alt_row": "#f5f6fa",
    "grid": "#bdc3c7",
    "hr": "#cccccc",
    "meta": "#555555",
}
```

---
name: pdf-to-md
description: Convert PDF documents to well-formatted, LLM-readability-optimized markdown. Use this skill when the user asks to convert a PDF to markdown, create a .md version of a PDF, or make a PDF "readable" or "LLM-friendly." Handles academic papers, book chapters, reports, slide decks, and general documents.
---

# PDF to Markdown Conversion Skill

## Overview

This skill converts PDF documents into structured, LLM-optimized markdown files. The conversion is an LLM-driven analytical process — the agent reads the PDF, understands its structure and domain, then authors clean markdown. This is NOT a mechanical text extraction; it is an intelligent restructuring for downstream LLM consumption.

## When to Use

- User asks to convert a `.pdf` to `.md`
- User asks for a "readable," "LLM-friendly," or "markdown version" of a PDF
- User wants to add a PDF to a reference library in markdown form

## Process

### Step 1: Read the PDF

Use the Read tool with the PDF file path. For large PDFs (>10 pages), you MUST paginate:

```
Read file_path="doc.pdf" pages="1-20"   # First batch (max 20 pages per request)
Read file_path="doc.pdf" pages="21-40"  # Second batch
```

**CRITICAL:** Read ALL pages before writing any markdown. Incomplete reads produce incomplete conversions. Check the total page count from the first read and plan your pagination.

### Step 2: Analyze Document Structure

Before writing, identify:

1. **Document type** — academic paper, book chapter, report, presentation, manual, etc.
2. **Structural elements** — headings, sections, subsections, abstract, tables, figures, references
3. **Noise markers** — proof annotations, page headers/footers, watermarks, line numbers, column markers (e.g., C18P1, C18S1 for OUP proofs)
4. **Citation style** — APA, numbered, footnotes
5. **Tables** — count them, note column structure, determine if they'll fit in markdown pipe format
6. **Special content** — equations, code, figures (describe if not reproducible), appendices

### Step 3: Write LLM-Optimized Markdown

Apply the optimizations listed below, writing the full document. Output the `.md` file alongside or in place of the original PDF depending on user instruction.

### Step 4: Verify

- Confirm all sections from the PDF appear in the markdown
- Confirm tables are complete (correct number of rows/columns)
- Confirm references are complete if the document had them
- For long documents, spot-check a section from the middle and end of the PDF

## LLM-Readability Optimizations

These optimizations make the markdown maximally useful when consumed by LLMs for retrieval, citation, summarization, or Q&A tasks.

### 1. Front Matter Summary Block

Add a structured header at the top of every document:

```markdown
# [Document Title]

**Authors:** [names]
**Source:** [journal/book, year]
**DOI/URL:** [if available]

---

## Document Summary

[2-4 sentence summary of the document's purpose, methods, and key findings/arguments]

### Key Concepts / Constructs

[Table or bullet list of the most important terms, theories, or frameworks in the document — acts as a lookup index for LLM retrieval]
```

This front matter lets an LLM determine relevance quickly without reading the full document.

### 2. Clean Heading Hierarchy

- Map the document's section structure to markdown headings: `#` (title) > `##` (major sections) > `###` (subsections) > `####` (sub-subsections)
- Strip all publisher/proof markers (e.g., `C18P1`, `C18S1`, section numbering artifacts)
- Strip page numbers, running headers, and footers
- Preserve the author's logical section order exactly

### 3. Tables as Markdown Pipe Tables

Convert all tables to markdown pipe format:

```markdown
| Column A | Column B | Column C |
|----------|----------|----------|
| data     | data     | data     |
```

**Edge cases:**
- **Very wide tables (5+ columns):** Still use pipe format, but consider abbreviating column headers or splitting into multiple tables if readability suffers
- **Merged cells / multi-row cells:** Flatten by repeating the spanning content or using line breaks within cells
- **Nested content in cells:** Use bullet-style lists within cells separated by semicolons, not literal line breaks (which break pipe tables)
- **Tables with long prose cells:** Summarize cell content to keep rows scannable; preserve full detail in a note below the table if needed

### 4. Dense Prose to Structured Lists

Academic documents often pack multiple concepts into single paragraphs. Restructure when:

- A paragraph lists 3+ distinct items, examples, or factors → convert to bullet list
- A paragraph describes impacts at multiple levels → split into labeled sub-sections (e.g., **Individual impact:** / **Organizational impact:**)
- A paragraph introduces a term then explains it → use **bold term** on first mention followed by its definition

**Do NOT bullet-ify** flowing argumentative prose or narrative; only restructure when the content is inherently list-like.

### 5. Bold Key Terms on First Introduction

Bold important terms, theories, frameworks, or constructs on their first appearance:

```markdown
**Diversity washing** represents one means through which this can manifest...
```

This helps LLMs identify and extract key terminology without full-text parsing.

### 6. Citation Preservation

- Keep inline citations exactly as the author wrote them: `(Author, Year)` or `(Author et al., Year)`
- Format the References section as a markdown list: `- Author (Year). Title. *Journal, Volume*(Issue), Pages.`
- Italicize journal/book titles using `*...*`
- Do NOT hyperlink DOIs (they clutter LLM context windows); keep them as plain text if present

### 7. Character Normalization

Run these normalizations on the extracted text:

- Curly/smart quotes → straight quotes (`"` and `'`)
- Em-dashes `—` → keep as-is (valid markdown/unicode)
- En-dashes in page ranges → regular hyphens: `60-84` not `60–84`
- Accented characters → preserve where they are part of names (e.g., Ståhl); normalize if they are OCR artifacts
- Ligatures (fi, fl) → separate characters
- Non-breaking spaces → regular spaces
- Soft hyphens from line-wrapping → remove entirely, rejoin the word

For automated normalization, use the helper script:

```bash
python .claude/skills/pdf-to-md/scripts/normalize_text.py INPUT.md OUTPUT.md
```

### 8. Figure and Image Handling

- If a figure is a chart/graph that can be described textually, write: `**Figure N:** [description of what the figure shows]`
- If a figure is essential and cannot be described, note: `**Figure N:** [See original PDF — visual content not reproducible in markdown]`
- Do NOT leave blank gaps where figures were

## Edge Cases

### Academic Proof Markers

Publisher proof systems inject markers like `C18P1`, `C18S1`, `OUP UNCORRECTED PROOF`, `FIRSTPROOFS`, etc. **Strip all of these.** They are not part of the document's content. Common patterns:

| Publisher | Marker Pattern | Example |
|-----------|---------------|---------|
| OUP (Oxford) | `C{chapter}P{para}`, `C{chapter}S{section}` | `C18P1`, `C18S3` |
| Elsevier | Proof line numbers in margins | `5`, `10`, `15` |
| Springer | `[AU1]`, `[AQ1]` (author queries) | `[AU1]: Please confirm...` |
| Wiley | Proof watermarks | `This article is protected by copyright` |

### Multi-Column Layouts

Some PDFs render in two columns. The Read tool typically linearizes them correctly, but watch for:
- Sentences that end mid-thought and resume after an unrelated paragraph (column break artifact)
- Table content interleaved with body text
- Footnotes displaced from their reference point

If column linearization is garbled, read the PDF page-by-page and manually reconstruct the reading order.

### Scanned / Image-Based PDFs

If the Read tool returns blank or garbled content, the PDF may be image-based. In that case:
1. Inform the user that the PDF appears to be scanned/image-based
2. If text is partially readable, do best-effort conversion with `[illegible]` markers
3. Suggest OCR preprocessing if high fidelity is needed

### Very Long Documents (50+ pages)

- Paginate reads in 20-page batches
- Consider splitting the output into multiple .md files by chapter/section if the user agrees
- At minimum, the front matter summary should capture the full document scope even if conversion is partial

### Documents with Heavy Math/Equations

- Simple inline equations: write in plain text with careful formatting (`E = mc^2`)
- Complex equations: describe in words or use LaTeX notation if the user's workflow supports it
- Note: markdown rendering varies; keep equation formatting simple unless the user requests LaTeX

## Quality Checklist

Before delivering the markdown file, verify:

- [ ] All pages of the PDF were read
- [ ] Front matter summary is present and accurate
- [ ] All sections from the original appear in the markdown
- [ ] All tables are complete with correct row/column counts
- [ ] Proof markers and page artifacts are stripped
- [ ] Key terms are bolded on first use
- [ ] References section is complete (if applicable)
- [ ] No orphaned sentences from column-break artifacts
- [ ] Special characters are normalized
- [ ] File is saved with `.md` extension alongside or replacing the original per user instruction

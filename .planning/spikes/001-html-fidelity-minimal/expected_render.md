# Expected Rendered Output

When you open the published post URL in a browser, the page body should show:

## 1. "Module 1: Structured Interviews" heading

A standard H2. No styling concerns.

## 2. Blue callout box

A light blue box with a thick blue left border, rounded corners, containing:
- Bold "Why this matters" header in dark navy
- A paragraph about Schmidt & Hunter 1998

**Fidelity check:** If the box is unstyled (plain text on white background with no border or background color), the `<style>` block was stripped.

## 3. Two yellow side-by-side panels ("Learning Objectives" / "Estimated time")

Two yellow/cream boxes side by side (flex layout), each taking ~50% width with a gap between them.

**Fidelity check:** If they stack vertically with no background color, either the `<style>` block was stripped OR the `class="soup-objectives"` attribute was stripped.

## 4. Dark navy-header table with alternating row shading

A table with white text on a dark navy header row, and alternating white / very-light-gray body rows.

Data:
| Format | Validity (r) | Bias risk |
|---|---|---|
| Unstructured | 0.20 | High |
| Semi-structured | 0.33 | Medium |
| Structured | 0.51 | Low |

**Fidelity check:** If the header is plain (white bg, black text) and rows are uniformly white, the `.soup-table` CSS didn't apply.

## 5. Dark terminal-style code block

A near-black box with light gray monospace text, holding the "tell me about a time" behavioral question and its rubric. Line breaks inside the `<pre>` should be preserved exactly — no `<br>` injection, no collapse of whitespace.

**Fidelity check:**
- Background should be dark slate (#0f172a), NOT white
- Text indentation should match the source (4-space indent on "5 —", "3 —", "0 —" lines)
- No auto-inserted `<br>` tags breaking the layout

## 6. Trailing paragraph

A normal paragraph: "When you see a candidate struggle with this, don't fill the silence. Let them think."

---

## Success criteria for VALIDATED verdict

All six elements above render with the intended styling. Specifically:
1. `<style>` block survived the POST (verified by both the stored-content diff in the script output AND the visible styling in the browser).
2. `class` attributes on `<div>`, `<table>`, and `<pre>` survived.
3. `<pre>` whitespace not mangled by `wpautop`.
4. No `<br>` injection inside block elements.

## PARTIAL verdict if

Styles partially apply (e.g., `<style>` survives but `wpautop` broke the `<pre>`). Document what survived and what didn't — there may be a WP filter we can disable.

## INVALIDATED verdict if

`<style>` block is stripped entirely or class attributes are removed. This kills the pipeline — WP's content filters are too aggressive for our use case even as admin. Pivot to Thinkific or Kajabi.

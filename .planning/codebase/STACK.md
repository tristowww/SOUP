# Technology Stack

**Analysis Date:** 2026-04-13

## File Format

**Primary:**
- Markdown (.md) - All content files (420+ files across 10 courses and reference materials)
- Single HTML file (`Online Courses/COURSE_STRATEGY_DASHBOARD.html`) - Course strategy dashboard with embedded CSS and JavaScript

**Secondary:**
- CSV - Data outputs from Python assignments (e.g., `Assignment 4_Excel Answers.csv`)

## Languages

**Primary:**
- Markdown - All course materials, syllabi, notes, articles, CLAUDE.md documentation
- HTML - Dashboard interface
- CSS - Embedded in dashboard HTML
- JavaScript - Embedded in dashboard HTML

**Secondary:**
- Python - Referenced in academic assignments and course content (not executable files, but assignment tutorials and answer keys)

## Content Format & Platform

**Publishing Target:**
- Kajabi platform - All 10 commercial courses will be hosted on Kajabi
- No custom build step or local development server required
- Content is designed for direct upload/adaptation to Kajabi's course structure

**Dashboard:**
- Self-contained HTML5 application
- No external dependencies beyond Google Fonts CDN
- Uses CSS custom properties (variables) for design tokens
- Embedded fonts: DM Serif Display, Inter, JetBrains Mono (loaded from googleapis.com)
- CSS animations and transitions for interactive elements

## Python Tools & Libraries (Referenced in Assignments)

**Data Analysis & Visualization:**
- pandas - Data manipulation and analysis (PM Assignments 4-5, Org Assignments 2/5/6)
- numpy - Numerical computing
- matplotlib - Visualization (bar charts, plots)
- seaborn - Statistical data visualization

**Natural Language Processing:**
- TextBlob - Sentiment analysis and text processing (Org Assignment 5 for employee feedback analysis)

**Machine Learning:**
- scikit-learn - Machine learning algorithms (referenced in Course 5 - AI-Powered HR curriculum)

**Statistical Analysis:**
- scipy - Scientific computing
- SPSS-compatible output generation (PM assignments generate SPSS-style statistical tables)

**Execution Environment:**
- Google Colab - Primary environment for hands-on coding labs (Course 5 includes 5 Google Colab notebooks)
- Jupyter notebooks - Referenced for course content delivery (`Actual_Sample_Size_Power_Analysis.ipynb`, `Proposed_Study_3_Power_Analysis.ipynb`)

## Development & Content Management

**Version Control:**
- Git - GitHub Desktop + Git CLI on macOS
- Branch: `main` is primary branch

**Editor:**
- VS Code - Default editor for content team

**Documentation:**
- CLAUDE.md format - Project instructions at root and per-directory levels
- No package manager required
- No build step or compilation process

## Configuration & Design System

**Design Tokens (Dashboard):**
- CSS custom properties (--variables) defined in dashboard
- Color palette: Plum (#3D2C5E), Sage, Peach, Lavender, Gold, Coral, Mint, Sky
- Typography: Serif (DM Serif Display), Sans-serif (Inter), Monospace (JetBrains Mono)
- Border radius: 20px, 14px, 999px
- Shadows and transitions defined as variables
- No external CSS framework

**Content Style Guide:**
- Brand voice documentation in `Online Courses/00-Voice and Tone/Brand Voice and Tone.md`
- Naming conventions for course files, assignments, and materials specified in CLAUDE.md

## Data Sources & External Tools (Mentioned in Content)

**Research & Analytics:**
- ChatGPT / OpenAI - Referenced in assignment guidance (Org Assignments) as optional AI helper tool
- Semantic Scholar - Referenced for literature review
- SPSS - Statistical software referenced for comparison (assignments generate SPSS-compatible output)
- Cropster - Referenced as roasting software (external context from parent repository)
- Airtable - Referenced as potential data source (parent repository uses for subscriptions/CRM)

**Third-Party Libraries Used in Dashboard:**
- None in critical path (pure HTML/CSS/JS, fonts from CDN)

## Platform Requirements

**Development:**
- macOS
- VS Code editor
- Git (GitHub Desktop + CLI)
- Browser with modern CSS/JavaScript support (for dashboard)

**Content Delivery:**
- Kajabi platform account
- Domain name (to be registered)
- Email infrastructure (Kajabi-native)

**Optional (For Advanced Course 5 - AI-Powered HR):**
- Google account (for Google Colab access)
- Python environment (local or Colab-based)
- Optional API keys for OpenAI/Claude for NLP demonstrations (to be integrated)

## Build & Deployment

**No Build Process:**
- All content is static markdown files
- HTML dashboard is self-contained (no bundling required)
- Direct file upload to Kajabi or Git-based workflow for version control

**File Organization:**
- `/Online Courses/` - 10 course subdirectories + reference materials
- `/Online Courses/Reference Materials/` - Source academic materials (syllabi, slides, articles, assignments)
- `.planning/codebase/` - Planning and analysis documents
- `.claude/skills/` - AI skill definitions (humanizer2, ui-ux-pro-max, frontend-design, etc.)

---

*Stack analysis: 2026-04-13*

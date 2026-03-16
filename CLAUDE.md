# CLAUDE.md - SOUP Repository (I/O Psychology Course Materials)

## Project Purpose

This repository contains graduate-level Industrial/Organizational Psychology course materials being converted into commercial online courses for the Kajabi platform. The subject matter expert is Dr. Teresa Ristow (Virginia Tech PhD, I/O Psychology), whose differentiator is the intersection of traditional I/O psychology with applied AI, NLP, and data science methods.

---

## Repository Structure

| Directory | Contents | Course Code | Key Content Types |
|-----------|----------|-------------|-------------------|
| `Employee Selection Materials/` | Hiring and selection science | PSYC 656 | Slides, articles, exams, textbook, syllabus |
| `Performance Mgmt Materials/` | Performance management systems | PSYC 654 | Slides, articles, assignments (Python/Excel), syllabi |
| `Employee Training Materials/` | Training and development | PSYC 652 | Slides, articles, assignments, guest speaker materials, syllabus |
| `Organizational Psych Materials/` | Organizational behavior | PSYC 650 | Slides, articles, assignments (Python/SPSS), datasets, exams, syllabi |
| `Publications/` | Teresa's research output | N/A | Dissertation, thesis, journal articles, book chapters |
| `Social Psych Materials/` | Social psychology lectures | PSYC 343 | Slides |

**Total files:** ~409 markdown files

---

## Task Domain Classification

Use this taxonomy to route work correctly:

**T1: CONTENT ADAPTATION** - Converting academic materials to commercial course modules
- Constraint-first: Kajabi platform structure, practitioner audience level, module length targets (15-20 min)
- Source files: Slides (`*slides.md`, `*slides_me.md`), Notes (`*Notes*.md`), topic summaries
- Output: Practitioner-friendly module scripts, assessment questions, template designs

**T2: STRATEGIC ANALYSIS** - Market research, competitor analysis, pricing, audience segmentation
- Framework-first: See `COURSE_STRATEGY_DELIVERABLE.md` for baseline analysis
- Data dependencies: Keyword research CSVs, competitor audit data, survey responses
- Output: Updated segment matrices, pricing recommendations, launch sequencing

**T3: COURSE DESIGN** - Architecture of Kajabi course products
- Interface-first: Kajabi module structure, lesson flow, assessment design, template/tool creation
- Reference: Course product templates in `COURSE_STRATEGY_DELIVERABLE.md` Step 4
- Output: Module outlines, lesson scripts, downloadable template designs

**T5: RESEARCH SYNTHESIS** - Analyzing academic articles, extracting practitioner insights
- Source-first: Academic articles are in week subdirectories (e.g., `Campion et al. (1997).md`)
- Files named `*slides_me.md` contain Teresa's annotated/expanded versions of slides
- Output: Practitioner summaries, key finding extractions, framework simplifications

---

## File Naming Conventions

- **Slides:** `Week N slides.md` (original) and `Week N slides_me.md` (Teresa's annotated version)
- **Notes:** `Week N Notes & Position Paper.md` or topic-named files (e.g., `Coaching & Mentoring.md`)
- **Articles:** `Author et al. (Year).md` format
- **Assignments:** `Assignment N.md` with corresponding `Assignment N KEY.md` or `Assignment N Answers.md`
- **Syllabi:** `Syllabus_PSYCNNN_SemesterYear.md`

---

## Teresa's Unique IP (Competitive Moat)

When working on course differentiation, reference these proprietary contributions:

1. **AIRA Framework** (`Publications/Chapter 18.md`) - AI-enabled workplace inclusion. Forthcoming OUP chapter. Five pillars: Autonomy, Individualization, Representation, Anonymity, Belonging.
2. **LPA + NLP for Job Ads** (`Publications/Ristow_TL_D_2023.md`) - Dissertation combining latent profile analysis with transformer-based NLP for analyzing deception perception in job advertisements. Directly applicable to job seekers (Courses 8-10) without perspective flip — powers the "Decoding Job Ads" and "Red Flag Toolkit" modules.
3. **Curbstoning Detection** (`Publications/Curbing-Curbstoning*.md`) - Novel survey data fabrication detection methods (Psychological Methods).
4. **VOIS Framework** (`Publications/13428_2022_Article_2045.md`) - Voice Over Internet Surveys methodology (Behavior Research Methods).
5. **Python-Integrated HR Analytics Curriculum** - Assignments across PM (4-5) and Org Psych (2, 5, 6) courses teaching pandas, matplotlib, TextBlob, scikit-learn for HR applications.

---

## Commercial Course Lineup

Ten courses planned across two verticals (see `COURSE_STRATEGY_DELIVERABLE.md` for full details):

**Employer-Side Vertical (Courses 1-7):**

| # | Course Title | Priority | Price Tier | Primary Sources |
|---|-------------|----------|------------|-----------------|
| 1 | Structured Hiring That Works | Launch first | $197-297 | Selection W3-14 |
| 2 | Performance Management That Actually Works | Launch first | $197-297 | PM W2-13 |
| 3 | Training That Transfers | Phase 2 | $197-297 | Training W2-15 |
| 4 | Leadership Development by Design | Phase 2 | $397-697 | Training W3,W9; PM W6-7; Thesis |
| 5 | AI-Powered HR (Flagship) | Phase 2 | $497-797 | Cross-repo; Publications; Assignments |
| 6 | Data-Driven DEI | Phase 2 | $497-997 | Training W14; Org W13; Chapter 18 |
| 7 | Workplace Psychology Essentials | Gateway | $49-97 | Org W4-12 |

**Job-Seeker Vertical (Courses 8-10):**

| # | Course Title | Priority | Price Tier | Primary Sources |
|---|-------------|----------|------------|-----------------|
| 8 | The Science of Getting Hired | Phase 3 | $97-197 | Selection W10-14; W5; Dissertation |
| 9 | Choose Wisely | Phase 3 | $97-197 | Selection W3-4; Org W4,W6,W8,W12; Dissertation |
| 10 | The Hiring Insider's Toolkit | Phase 3 | $297-997 (B2B: $5K-25K) | Courses 8-9 content; Training W3; Course 1 |

**Bundle:** Courses 8+9 at $247-347

---

## Audience Segments

Twelve target segments identified across two verticals. When creating content, consider which segment(s) the output serves:

**Employer-Side Segments (Courses 1-7):**
1. **HR Professionals** - PHR/SPHR certified, continuing education seekers
2. **People Managers** - Non-HR managers taking on HR duties
3. **Small Business Owners** - Sub-50 employees, building HR from scratch
4. **I/O Psych Students/Early-Career** - Graduate students, new practitioners
5. **Nonprofit Leaders** - Mission-driven orgs with limited budgets
6. **DEI Practitioners** - CDOs, DEI consultants needing data-driven approaches
7. **Tech/Startup People Ops** - First HR hires building processes
8. **HR Consultants** - Building advisory practices
9. **L&D Professionals** - Training managers, instructional designers

**Job-Seeker Segments (Courses 8-10):**
10. **Recent Graduates & Career Starters** - 0-3 years post-graduation, actively job seeking, high volume/high price sensitivity ($49-197)
11. **Mid-Career Professionals Seeking Change** - 5-20 years experience, career pivots/transitions, moderate price sensitivity ($97-397)
12. **Career Coaches, Outplacement, & University Career Centers** - B2B buyers, low price sensitivity ($297-997+), licensing potential

---

## Content Adaptation Rules

When converting academic content to commercial courses:

**MUST:**
- Strip academic citation format from main flow; move to "Further Reading" sections
- Replace psychometric terminology with plain-language equivalents
- Add actionable templates, checklists, or tools to every module
- Include real-world examples appropriate to the target segment
- Maintain evidence-based accuracy (cite the research, just don't write like a journal article)

**MUST NOT:**
- Fabricate statistics or research findings
- Use copyrighted article text verbatim (summarize and cite)
- Include exam questions from academic courses without modification
- Claim certification or credit without proper accreditation
- Remove nuance from research findings to oversimplify

**LANGUAGE:**
- Use "evidence shows" not "studies suggest" (more authoritative)
- Use "practitioners" not "students"
- Use "your organization" not "the organization"
- Active voice, second person, imperative mood for instructions
- Keep sentences under 25 words where possible
- No academic hedging language ("it could be argued that...")

---

## Key Reference Files

- `COURSE_STRATEGY_DELIVERABLE.md` - Full market analysis, content inventory, and go-to-market roadmap
- `IO_Psych_Course_Strategy_Prompt.md` - Original strategy prompt (reference for methodology)
- Syllabi in each course directory define the canonical topic sequence
- `Publications/` directory contains Teresa's unique research contributions

---

## Humanizer Requirement

**ALL generated content intended as human-readable or final-draft output MUST be run through `/skills humanizer` before delivery.** This includes but is not limited to:

- Module scripts and lesson content
- Assessment questions and answer keys
- Practitioner summaries and research syntheses
- Templates, checklists, and tool descriptions
- Marketing copy, course descriptions, and email drafts
- Any other prose the end user or customer will read

Internal/structural outputs (code, data tables, file listings, status updates, CLAUDE.md edits, etc.) are exempt.

---

## Design, UI/UX & Frontend Skill Routing

**All design, UI/UX, and frontend work must use the installed design skills.** This applies to Kajabi course page design, sales page builds, template visual design, slide deck layouts, and any work where layout, color, typography, or visual hierarchy decisions are being made.

**Required skills:**
- `/ui-ux-pro-max` for design system generation (style recommendations, color palettes, typography pairing, layout patterns, accessibility, anti-patterns)
- `/frontend-design` for production-grade frontend implementation with high design quality

**When to invoke:** Any task involving visual design decisions, page layout, color selection, typography pairing, component styling, landing page or sales page builds, course page design, or UI reviews. This directive is inherited by all child directories including `Online Courses/`.

---

## Working Conventions

- All files are markdown (.md) format
- No build step or package manager required
- Git is used for version control (GitHub Desktop + CLI on macOS)
- Branch: `main` is the primary branch

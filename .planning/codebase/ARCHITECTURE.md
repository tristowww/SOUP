# Architecture

**Analysis Date:** 2026-04-13

## Pattern Overview

**Overall:** Content-to-Course Pipeline — Academic Source → Commercial Module

The SOUP repository implements a structured pipeline that converts graduate-level Industrial/Organizational Psychology academic materials into commercially viable online courses for the Kajabi platform. The architecture separates three layers: *academic source materials*, *voice/strategy foundation*, and *commercial course builds*.

**Key Characteristics:**
- **Source-first design** — All commercial courses trace back to specific academic source materials (selections, readings, assignments)
- **Template-driven course structure** — Each commercial course follows a standard architecture: overview document, module scripts, templates/tools, assessments, case studies
- **Vertical separation** — Two distinct product lines (Employer-side: Courses 1-7, Job-Seeker: Courses 8-10) with overlapping source materials but different learner perspectives
- **Voice-gate foundation** — All course content must reflect Dr. Teresa Ristow's intellectual voice (evidence-anchored, framework-thinking, practitioner-bridging) defined in foundational docs before any module scripts are generated

## Layers

**Academic Source Layer:**
- Purpose: Store original I/O Psychology course materials and Teresa Ristow's research publications that will be adapted into commercial content
- Location: `Online Courses/Reference Materials/`
- Contains: Original course lecture slides (`Week N slides.md`, `Week N slides_me.md`), reading notes, academic articles in `Author et al. (Year).md` format, assignments with answer keys, and dissertations/publications
- Depends on: None (terminal source layer)
- Used by: Course Design Layer

**Course Strategy & Voice Layer:**
- Purpose: Establish commercial differentiation, audience segmentation, pricing, and brand voice/tone before any course module work begins
- Location: `Online Courses/` root directory and `Online Courses/00-Voice and Tone/`
- Contains: 
  - `COURSE_STRATEGY_DELIVERABLE.md` — Full market analysis, 10-course product roadmap, audience segments, pricing, competitive positioning
  - `IO_Psych_Course_Strategy_Prompt.md` — Original strategy methodology
  - `Brand Voice and Tone.md` — Voice fingerprint of Teresa Ristow (five core traits: Evidence-Anchored Authority, Progressive Scaffolding, Quantitative Precision, Framework Thinking, Practitioner Bridge)
  - `CLAUDE.md` files (root and Online Courses/ subdirectory) — Content adaptation rules, task domain classification, file naming conventions
- Depends on: Academic Source Layer (provides research grounding for strategy)
- Used by: Course Design Layer and all downstream modules

**Course Design Layer:**
- Purpose: Implement individual commercial courses by selecting and adapting academic source materials to practitioner-friendly modules
- Location: `Online Courses/Course N - [Title]/` (10 directories)
- Contains: 
  - `overview.md` — Course architecture, target audience segments, core topic clusters, content effort estimates, MVP scope, and cross-sell paths
  - (Future) Module scripts adapted from academic materials
  - (Future) Downloadable templates, checklists, worksheets, scorecards
  - (Future) Assessment questions (adapted from academic exams, not copied)
  - (Future) Case studies with real-world scenarios
  - (Future) Video script outlines and talking point decks
- Depends on: Academic Source Layer (specific weeks/materials cited in overview) and Course Strategy & Voice Layer (brand voice, audience segment, pricing tier)
- Used by: Kajabi platform build-out

## Data Flow

**Academic Material → Course Design:**

1. **Selection Analysis** — Course owner reads `COURSE_STRATEGY_DELIVERABLE.md` to identify which academic course materials map to this commercial course
   - Example: Course 1 (Structured Hiring) sources from `Employee Selection Materials/Week 3`, `Week 6`, `Week 9-14` (see `Course 1/overview.md` lines 46-50)

2. **Source Material Review** — Read relevant weeks in `Reference Materials/` to extract:
   - Slide decks (`Week N slides.md` and Teresa's annotated version `Week N slides_me.md`)
   - Academic articles in week subdirectories (`Author et al. (Year).md` format)
   - Assignments and supporting materials
   - Teresa's voice patterns (found especially in `*_me.md` files and Publications)

3. **Voice Gating** — Before writing any module script:
   - Read `00-Voice and Tone/Brand Voice and Tone.md` to understand evidence-anchored authority, progressive scaffolding, and theory-naming patterns
   - Read `00-Voice and Tone/CLAUDE.md` for content review checklist
   - Verify all claims will be evidence-anchored and connected to practitioner implications

4. **Content Adaptation** — Convert academic materials to practitioner language following rules in `SOUP/CLAUDE.md` and `Online Courses/CLAUDE.md`:
   - Strip academic citation format; move to "Further Reading" sections
   - Replace psychometric terminology with plain-language equivalents
   - Add actionable templates, checklists, or tools to every module
   - Use "evidence shows" not "studies suggest"
   - Use "practitioners" and "your organization" not "students" and "the organization"

5. **Module Script Generation** — Write 15-20 minute video scripts in Teresa's voice following the tone spectrum (measured authority with warmth for core teaching modules)

6. **Template Creation** — Every module ends with a downloadable tool: interview scorecard, job analysis worksheet, DEI tracking dashboard, etc.

7. **Assessment & Case Studies** — Create knowledge checks and practitioner scenarios adapted from academic content

8. **Humanizer 2 Pass** — All human-readable output passes through `/humanizer2` before delivery (required by root `CLAUDE.md` line 159-170)

**State Management:**
- **Draft state:** Module scripts stored in `Course N/` subdirectories as `.md` files
- **Review state:** Content run through voice and tone checklist from `00-Voice and Tone/CLAUDE.md`
- **Ready-to-publish state:** Humanizer 2 verified, signed off, ready for Kajabi platform import
- No centralized state tracking; versions controlled via Git on main branch

## Key Abstractions

**Course Overview Document:**
- Purpose: Captures course architecture, target audience, content effort estimates, and source material mapping in a single reference
- Location: `Course N/overview.md` (all 10 courses)
- Pattern: Fixed structure with sections for Audience, Differentiator, Core Topics, Format, Effort Estimate, MVP Scope, Cross-sell Path, Content Gaps, Keyword Targets, and Readiness Summary
- Example: `Course 1/overview.md` shows Selection course sources from Weeks 3, 6, 9-14 of Employee Selection Materials

**Week-Organized Academic Material:**
- Purpose: Store original I/O Psychology course materials grouped by course curriculum week
- Examples: 
  - `Reference Materials/Employee Selection Materials/Week 3- Intro to Selection/` contains `Week 3 slides.md`, `Week 3 slides_me.md` (Teresa's annotations), and referenced articles (`Polyhart et al. (2017).md`)
  - `Reference Materials/Performance Mgmt Materials/Week 2/` through `Week 13/` follow the same pattern
  - `Reference Materials/Organizational Psych Materials/` covers Weeks 2-13
  - `Reference Materials/Employee Training Materials/` covers Weeks 2-15

**Publication/IP Repository:**
- Purpose: Store Teresa Ristow's original research (dissertation, journal articles, book chapters) that provide competitive differentiation
- Location: `Reference Materials/Publications/`
- Contains:
  - `Ristow_TL_D_2023.md` — Dissertation: LPA + NLP analysis of deception perception in job ads (directly applicable to Courses 8-10)
  - `Chapter 18.md` — Forthcoming OUP chapter on AIRA Framework (AI-enabled workplace inclusion; used in Course 6)
  - `Curbing-Curbstoning-Distributional-Methods-to-Detect-Survey-Data-Fabrication-by-Third-Parties.md` — Novel fabrication detection methods
  - `13428_2022_Article_2045.md` — VOIS Framework (Voice Over Internet Surveys)
  - `TRistow_Thesis_FINAL.md` — Master's thesis

**Brand Voice and Tone Guide:**
- Purpose: Codify Teresa Ristow's intellectual voice across all commercial content
- Location: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md`
- Pattern: Five core voice traits (Evidence-Anchored Authority, Progressive Scaffolding, Quantitative Precision, Framework Thinking, Practitioner Bridge) with tone spectrum by content type (module scripts, blogs, white papers, assessments, templates, sales pages, email, community)
- Non-negotiable rules: Every claim evidence-anchored, concepts build progressively, quantify over qualify, name the theory, connect to practice, acknowledge nuance, no hype

## Entry Points

**Course Strategy Document:**
- Location: `Online Courses/COURSE_STRATEGY_DELIVERABLE.md`
- Triggers: Anyone planning a new course or understanding market positioning
- Responsibilities: Defines 10-course product roadmap, audience segments (12 total), pricing tiers, launch sequencing (7 phases over 10 months), competitive differentiation, content inventory mapping

**Root Course Strategy Documentation:**
- Location: `Online Courses/CLAUDE.md`
- Triggers: Any work in Online Courses/ directory
- Responsibilities: Establishes course directory structure, defines task domain classification (T1 content adaptation, T2 strategic analysis, T3 course design, T5 research synthesis), references voice guide, outlines content adaptation rules

**Voice Foundation:**
- Location: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` and `Online Courses/00-Voice and Tone/CLAUDE.md`
- Triggers: Before generating any course content
- Responsibilities: Gate all module scripts, templates, assessments, and sales copy through voice pattern analysis; ensure claims are evidence-anchored and theory-grounded

**Individual Course Overview:**
- Location: `Online Courses/Course N - [Title]/overview.md`
- Triggers: When building out a specific course
- Responsibilities: Maps academic source materials (specific weeks in Reference Materials/), defines MVP scope, lists content gaps, establishes cross-sell paths

## Error Handling

**Strategy:** Evidence-anchor-first with progressive scaffolding. Claims without backing research are flagged and rewritten.

**Patterns:**
- Weak claim: "Research shows structured interviews are better" → Rewritten with specifics: "Schmidt & Hunter's 85-year meta-analysis (1998) found structured interviews average .63 validity, compared to .38 for unstructured interviews"
- Oversimplified claim: "Simplify job descriptions for clarity" → Rewritten with nuance: "Simplify language below graduate reading level, but preserve technical accuracy. Oversimplification risks attracting unqualified candidates and creates adverse impact exposure"
- Ungrounded assertion: "AI will transform hiring" → Grounded: "AI-assisted resume screening shows promise in early studies (e.g., [citation]) but raises fairness concerns with predictive bias (e.g., [citation]). Current evidence suggests AI works best paired with human oversight rather than as standalone gatekeeper"

## Cross-Cutting Concerns

**Logging:** No formal logging system. Course development tracked via Git commits on `main` branch.

**Validation:** All course overviews follow a fixed template with required sections (Audience, Differentiator, Content Effort Estimate, MVP Scope). Missing sections are flagged before publication.

**Authentication:** Not applicable — content repository, no user auth required.

**Content Authenticity:** Voice review checklist (`00-Voice and Tone/CLAUDE.md` lines 28-33) verifies:
- Claims are evidence-anchored (theory named or finding cited)
- Concepts build progressively
- Numbers are precise, not vague
- Every theoretical point connects to practitioner action
- Limitations and nuance acknowledged
- Tone is measured confidence

---

*Architecture analysis: 2026-04-13*

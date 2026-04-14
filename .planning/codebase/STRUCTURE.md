# Codebase Structure

**Analysis Date:** 2026-04-13

## Directory Layout

```
/Users/Christopher/Documents/GitHub/SOUP/
├── .claude/                                          # Internal Claude configuration
├── .git/                                             # Git version control
├── .planning/                                        # Planning documents (this file's parent)
│   └── codebase/                                     # Codebase analysis documents
├── CLAUDE.md                                         # Root project instructions (Teresa Ristow, content adaptation rules, task domain classification)
└── Online Courses/                                   # Commercial course builds and source materials
    ├── CLAUDE.md                                     # Online Courses directory instructions
    ├── COURSE_STRATEGY_DELIVERABLE.md                # Market analysis, 10-course roadmap, audience segments, pricing, launch sequencing
    ├── COURSE_STRATEGY_DASHBOARD.html                # Interactive dashboard version of strategy
    ├── Course_Strategy_Presentation.pdf              # Strategic presentation
    ├── IO_Psych_Course_Strategy_Prompt.md            # Original strategy methodology
    ├── 00-Voice and Tone/                            # Brand voice foundation (read first before writing any course content)
    │   ├── Brand Voice and Tone.md                   # Voice fingerprint analysis (5 traits, tone spectrum, sentence patterns, prohibited language)
    │   └── CLAUDE.md                                 # Voice and tone agent instructions
    ├── Course 1 - Structured Hiring That Works/      # Commercial course 1/10 (Employer-side vertical)
    │   └── overview.md                               # Course architecture, audience, differentiators, content effort, source materials
    ├── Course 2 - Performance Management That Actually Works/
    │   └── overview.md
    ├── Course 3 - Training That Transfers/
    │   └── overview.md
    ├── Course 4 - Leadership Development by Design/
    │   └── overview.md
    ├── Course 5 - AI-Powered HR/
    │   └── overview.md
    ├── Course 6 - Data-Driven DEI/
    │   └── overview.md
    ├── Course 7 - Workplace Psychology Essentials/
    │   └── overview.md
    ├── Course 8 - The Science of Getting Hired/      # Commercial course 8/10 (Job-Seeker vertical)
    │   └── overview.md
    ├── Course 9 - Choose Wisely/
    │   └── overview.md
    ├── Course 10 - The Hiring Insiders Toolkit/
    │   └── overview.md
    └── Reference Materials/                          # Academic source materials (Professor Teresa Ristow's original course materials)
        ├── Publications/                             # Teresa's research output (7 files)
        │   ├── Ristow_TL_D_2023.md                   # Dissertation: LPA + NLP deception perception in job ads
        │   ├── Chapter 18.md                         # Forthcoming OUP chapter: AIRA Framework
        │   ├── Chapter_18 summary.md
        │   ├── Curbing-Curbstoning-...md             # Data fabrication detection methods
        │   ├── 13428_2022_Article_2045.md            # VOIS Framework
        │   ├── TRistow_Thesis_FINAL.md               # Master's thesis
        │   └── leader-thinking-skills-...md
        ├── Employee Selection Materials/             # PSYC 656 course materials (73 files)
        │   ├── Week 3- Intro to Selection/           # 7 files
        │   │   ├── Week 3 slides.md                  # Original slides
        │   │   ├── Week 3 slides_me.md               # Teresa's annotated version (use for voice patterns)
        │   │   ├── Intro to Selection.md
        │   │   ├── Selection Timeline.md
        │   │   ├── Polyhart et al. (2017).md         # Academic article
        │   │   ├── Ryan & Polyhart (2014).md
        │   │   └── Van Iddekinge et al. (2023).md
        │   ├── Week 4- Applicant Reactions to Recruiting/ (5 files)
        │   ├── Week 5- Legal Issues, Fairness, and Bias in Selection/ (6 files)
        │   ├── Week 6- Reliability and Validity/ (8 files)
        │   ├── Week 9- Measurement and Decision Making/ (8 files)
        │   ├── Week 10- Selection Measures 1 Biodata, Resumes, and Application Forms/ (7 files)
        │   ├── Week 11- Selection Measures 2 Interviews/ (10 files)
        │   ├── Week 12- Selection Measures 3 Cognitive Ability Tests and Personality Tests/ (8 files)
        │   ├── Week 13- Selection Measures 4 Work Simulations/ (4 files)
        │   ├── Week 14- The Future of Selection/ (4 files)
        │   ├── personnel-selection-procedures.md
        │   ├── Robert Gatewood, Hubert S. Feild, Murray Barrick - Human Resource Selection...md
        │   └── Spring 2024 Final.md
        ├── Performance Mgmt Materials/               # PSYC 654 course materials (102 files)
        │   ├── Week 2/ (9 files)
        │   ├── Week 3/ (8 files)
        │   ├── Week 4/ (9 files)
        │   ├── Week 5/ (9 files)
        │   ├── Week 6/ (9 files)
        │   ├── Week 7/ (8 files)
        │   ├── Week 8/ (7 files)
        │   ├── Week 9/ (8 files)
        │   ├── Week 10/ (7 files)
        │   ├── Week 11/ (8 files)
        │   ├── Week 12/ (9 files)
        │   ├── Week 13/ (8 files)
        │   └── Assignments/ (3 files: Python/Excel assignments)
        ├── Employee Training Materials/              # PSYC 652 course materials (114 files)
        │   ├── Week 2- Overview of Training & Development/ (9 files)
        │   ├── Week 3- Coaching & Mentoring/ (9 files)
        │   ├── Week 4- Needs Assessment/ (8 files)
        │   ├── Week 5- Learning & Transfer of Training/ (8 files)
        │   ├── Week 6- Training Design/ (8 files)
        │   ├── Week 9- Leadership Training/ (7 files)
        │   ├── Week 10- Traditional Training Delivery Methods/ (8 files)
        │   ├── Week 12- Tech-Based Training Delivery Methods/ (8 files)
        │   ├── Week 13- Training Evaluation & Outcomes/ (8 files)
        │   ├── Week 14- Diversity, Equity, & Inclusion Training/ (8 files)
        │   ├── Week 15- Emerging Approaches & The Future of Training Development/ (8 files)
        │   └── Assignments/ (4 files)
        ├── Organizational Psych Materials/           # PSYC 650 course materials (117 files)
        │   ├── Week 2/ (9 files)
        │   ├── Week 3/ (8 files)
        │   ├── Week 4/ (9 files)
        │   ├── Week 5/ (9 files)
        │   ├── Week 6/ (8 files)
        │   ├── Week 7/ (8 files)
        │   ├── Week 8/ (8 files)
        │   ├── Week 9/ (9 files)
        │   ├── Week 10/ (9 files)
        │   ├── Week 11/ (8 files)
        │   ├── Week 12/ (8 files)
        │   ├── Week 13/ (8 files)
        │   └── Assignments/ (4 files: Python/SPSS assignments)
        ├── Social Psych Materials/                   # PSYC 343 course materials
        │   └── SLIDES/ (1 file)
        └── Microsoft Blogs/                          # (Empty stub)
```

## Directory Purposes

**`Online Courses/`:**
- Purpose: Home directory for all ten commercial course projects and supporting strategy/voice documentation
- Contains: Course directories (Course 1-10), strategy documents, voice/tone guide, reference academic materials
- Key files: `COURSE_STRATEGY_DELIVERABLE.md` (entry point for market positioning and go-to-market roadmap)

**`Online Courses/00-Voice and Tone/`:**
- Purpose: Brand voice foundation that must be read before any course content is written
- Contains: `Brand Voice and Tone.md` (voice fingerprint analysis), `CLAUDE.md` (voice agent instructions)
- Key files: `Brand Voice and Tone.md` — mandatory reading for all content generation
- Not generated; written once and consulted for every module script, template, assessment, and sales page

**`Online Courses/Course N - [Title]/`** (10 directories)
- Purpose: Commercial course build directory for each of the ten courses
- Current contents: Only `overview.md` exists (course architecture, audience, differentiators, source material mapping, MVP scope)
- Future contents: Module scripts, templates/tools, assessments, case studies, video materials
- Status: In architecture phase; overview documents written, module development not yet started

**`Online Courses/Reference Materials/`:**
- Purpose: Store all graduate-level I/O Psychology academic course materials and Teresa Ristow's research publications used as source material for commercial courses
- Contains: 414 markdown files organized by course and week
- Does NOT contain the actual academic courses (Employee Selection Materials, Performance Mgmt Materials, etc.) at the repository root; they were moved here during SOUP setup

**`Online Courses/Reference Materials/Publications/`:**
- Purpose: Store Teresa Ristow's original research output (dissertation, journal articles, book chapters) providing competitive differentiation
- Contains: 7 files
- Key files:
  - `Ristow_TL_D_2023.md` — Dissertation (LPA + NLP analysis of deception in job ads; used in Courses 8-10)
  - `Chapter 18.md` — Forthcoming OUP chapter on AIRA Framework (used in Course 6)
  - `TRistow_Thesis_FINAL.md` — Master's thesis
  - `13428_2022_Article_2045.md` — VOIS Framework article
  - `Curbing-Curbstoning-*.md` — Data fabrication detection methods

**`Online Courses/Reference Materials/Employee Selection Materials/`:**
- Purpose: PSYC 656 (Hiring and Selection Science) original course materials
- Contains: 73 files organized into 9 week subdirectories (Weeks 3-6, 9-14) plus textbook references and exams
- File patterns:
  - `Week N slides.md` — Original lecture slides
  - `Week N slides_me.md` — Teresa's annotated version (reference for voice patterns and expanded thinking)
  - `Author et al. (Year).md` — Academic article files (e.g., `Campion et al. (1997).md`, `Schmidt & Hunter (1998).md`)
  - Topic summaries (e.g., `Intro to Selection.md`, `Selection Timeline.md`)
- Source for: Courses 1 (Structured Hiring), 8 (Science of Getting Hired), 10 (Hiring Insider's Toolkit)

**`Online Courses/Reference Materials/Performance Mgmt Materials/`:**
- Purpose: PSYC 654 (Performance Management Systems) original course materials
- Contains: 102 files organized into 12 week subdirectories (Weeks 2-13) plus assignments
- File patterns: Same as Selection Materials (slides, slides_me, articles, assignments with answer keys)
- Source for: Courses 2 (Performance Management That Actually Works), 5 (AI-Powered HR), 9 (Choose Wisely)

**`Online Courses/Reference Materials/Employee Training Materials/`:**
- Purpose: PSYC 652 (Training and Development) original course materials
- Contains: 114 files organized into 11 week subdirectories (Weeks 2-6, 9-10, 12-15) plus guest speaker materials and assignments
- File patterns: Slides, slides_me, articles, topic summaries, assignments
- Source for: Courses 3 (Training That Transfers), 4 (Leadership Development), 10 (Hiring Insider's Toolkit coaching methodology)

**`Online Courses/Reference Materials/Organizational Psych Materials/`:**
- Purpose: PSYC 650 (Organizational Behavior) original course materials
- Contains: 117 files organized into 12 week subdirectories (Weeks 2-13) plus assignments
- File patterns: Same pattern as other course materials
- Source for: Courses 5 (AI-Powered HR), 7 (Workplace Psychology Essentials), 9 (Choose Wisely)

**`Online Courses/Reference Materials/Social Psych Materials/`:**
- Purpose: PSYC 343 (Social Psychology) original lectures
- Contains: 1 file (lecture slides)
- Status: Minimal content; not heavily used in current course roadmap

## Key File Locations

**Entry Points:**
- `Online Courses/COURSE_STRATEGY_DELIVERABLE.md` — Start here to understand market positioning, audience segments, and 10-course roadmap
- `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` — Start here before writing any course content
- `Online Courses/CLAUDE.md` — Course directory conventions and adaptation rules

**Configuration:**
- `/Users/Christopher/Documents/GitHub/SOUP/CLAUDE.md` — Root project instructions, content adaptation rules, task domain classification
- `Online Courses/00-Voice and Tone/CLAUDE.md` — Voice and tone agent instructions and content review checklist

**Core Logic (Commercial Courses):**
- `Online Courses/Course 1 - Structured Hiring That Works/overview.md` — Course 1 architecture
- `Online Courses/Course 2 - Performance Management That Actually Works/overview.md` — Course 2 architecture
- (Similar pattern for all 10 courses)

**Academic Source Materials:**
- `Online Courses/Reference Materials/Employee Selection Materials/` — Selection course materials (73 files, 9 weeks)
- `Online Courses/Reference Materials/Performance Mgmt Materials/` — PM course materials (102 files, 12 weeks)
- `Online Courses/Reference Materials/Employee Training Materials/` — Training course materials (114 files, 11 weeks)
- `Online Courses/Reference Materials/Organizational Psych Materials/` — Org Psych course materials (117 files, 12 weeks)
- `Online Courses/Reference Materials/Publications/` — Teresa's research publications (7 files)

**Testing:**
- No test files present (content repository, not code)

## Naming Conventions

**Files - Slides:**
- `Week N slides.md` — Original lecture slides (e.g., `Week 3 slides.md`)
- `Week N slides_me.md` — Teresa's annotated version with expanded thinking (e.g., `Week 3 slides_me.md`)
- Usage: The `_me.md` versions are especially valuable for understanding voice patterns, theory naming practices, and how Teresa bridges academic to practitioner contexts

**Files - Articles:**
- `Author et al. (Year).md` format (e.g., `Campion et al. (1997).md`, `Schmidt & Hunter (1998).md`)
- Capitalization: Authors capitalized, years in parentheses
- Stored within relevant week subdirectories

**Files - Assignments:**
- `Assignment N.md` — Assignment prompt (e.g., `Assignment 1.md`)
- `Assignment N KEY.md` or `Assignment N Answers.md` — Answer key
- Files: Assignment solutions often use Python (pandas, matplotlib, scikit-learn) or Excel/SPSS

**Files - Syllabi:**
- `Syllabus_PSYCNNN_SemesterYear.md` format
- Example: `Syllabus_PSYC656_Spring2024.md`
- Not yet found in current repository structure; documented in root CLAUDE.md for reference

**Files - Notes:**
- `Week N Notes & Position Paper.md` or topic-named files (e.g., `Coaching & Mentoring.md`)
- Stored within week subdirectories

**Directories:**
- Week-based: `Week N- [Topic Name]/` (e.g., `Week 3- Intro to Selection/`)
- Course-based: `Course N - [Title]/` (e.g., `Course 1 - Structured Hiring That Works/`)
- Category-based: `[Domain] Materials/` (e.g., `Employee Selection Materials/`)
- Hyphenated for multi-word topics

**Course Directories:**
- Format: `Course N - [Full Title]/` where N is 1-10
- Numbering follows the strategic priority and product roadmap in COURSE_STRATEGY_DELIVERABLE.md
- All use kebab-case for spaces in subdirectory names (though the directory names themselves use hyphens)

## Where to Add New Code

**New Commercial Course Module Scripts:**
- Primary code: `Online Courses/Course N/` — Create `Module N.md` or `Module N - [Title].md` with video script, learning objectives, practitioner implications
- Tests/Assessments: `Online Courses/Course N/` — Create `Course N Module N Assessment.md` with knowledge checks and scenario-based questions
- Templates/Tools: `Online Courses/Course N/` — Create downloadable tools as `.md` with instructions (e.g., `Course 1 Interview Scorecard Template.md`)

**New Voice Pattern Documentation:**
- Primary location: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` — Add to relevant section (Voice Identity, Tone Spectrum, Sentence-Level Patterns)
- No new voice files should be created; all voice guidance consolidated in the two files in this directory

**New Academic Source Material:**
- Academic articles: Add to relevant week subdirectory in `Online Courses/Reference Materials/[Course Name]/Week N/` in `Author et al. (Year).md` format
- Assignments: Add to `Assignments/` subdirectory with corresponding `KEY.md` file
- Research publications: Add to `Online Courses/Reference Materials/Publications/`

**Utilities/Shared Resources:**
- Cross-course templates: `Online Courses/` root level with descriptive name (e.g., `Standard Module Template.md`)
- Strategic documents: `Online Courses/` root level (but already comprehensively covered by COURSE_STRATEGY_DELIVERABLE.md and strategy presentation)

## Special Directories

**`Online Courses/00-Voice and Tone/`:**
- Purpose: Voice foundation layer — read first before writing any course content
- Generated: No; written once and maintained
- Committed: Yes; part of core repository
- Immutability: Changes only by explicit decision (voice patterns should be stable across all 10 courses)

**`.planning/codebase/`:**
- Purpose: Codebase analysis documents (this directory)
- Generated: Yes; created by gsd-map-codebase agent
- Committed: Yes; committed to version control for reference by planning/execution agents
- Contents: ARCHITECTURE.md, STRUCTURE.md, and (in other focus areas) CONVENTIONS.md, TESTING.md, CONCERNS.md, STACK.md, INTEGRATIONS.md

**`Online Courses/Reference Materials/`:**
- Purpose: Academic source material repository
- Generated: No; imported from original course repositories
- Committed: Yes; full content committed to Git
- Versioning: No separate versioning; changes tracked via Git commits

**`Online Courses/`** root directory files:
- `COURSE_STRATEGY_DELIVERABLE.md` — Generated once by strategy analysis; not auto-updated
- `COURSE_STRATEGY_DASHBOARD.html` — Generated companion to strategy document
- `Course_Strategy_Presentation.pdf` — Presentation format of strategy
- All three documents maintained in sync when strategy changes

---

*Structure analysis: 2026-04-13*

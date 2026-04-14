# Coding Conventions (Content Repository)

**Analysis Date:** 2026-04-13

This repository contains academic-to-commercial content adaptation work. "Conventions" here refers to markdown structure, file naming patterns, voice/tone rules, and content quality standards for course materials.

---

## File Naming Patterns

### Source Materials (Academic)

**Slides:**
- `Week N slides.md` - Original/compiled slides (from course readings)
- `Week N slides_me.md` - Teresa's annotated/expanded version of slides
- Location: Course material directories (e.g., `Online Courses/Reference Materials/Performance Mgmt Materials/`)

**Notes and Lectures:**
- `Week N Notes & Position Paper.md` - Weekly lecture notes
- Topic-named files: `Coaching & Mentoring.md`, `Legal Issues, Fairness, and Bias.md`, `Validity.md`
- Location: Week subdirectories within course materials

**Articles:**
- `Author et al. (Year).md` format
- Example: `Campion et al. (1997).md`, `Schmidt & Hunter (1998).md`, `Ployhart et al. (2017).md`
- Location: Week subdirectories or root course material directory

**Assignments:**
- `Assignment N.md` - Student assignment prompt
- `Assignment N Answers.md` or `Assignment N KEY.md` - Answer key/rubric
- Variations: `Assignment N_Python Answers.md`, `Assignment N_Excel Answers.csv`
- Location: `Assignments/` subdirectory within course material directory

**Syllabi:**
- `Syllabus_PSYCNNN_SemesterYear.md`
- Example: `Syllabus_PSYC656_Spring2024.md`, `Syllabus_PSYC654_Fall2024.md`
- Location: Root of course material directory

### Commercial Course Output

**Course Directories:**
- Pattern: `Course N - Course Title/`
- Examples: 
  - `Online Courses/Course 1 - Structured Hiring That Works/`
  - `Online Courses/Course 5 - AI-Powered HR/`
  - `Online Courses/Course 8 - The Science of Getting Hired/`

**Course Overview:**
- `overview.md` - Course strategy, audience, scope, content effort estimate
- Location: Root of course directory
- See: `Online Courses/Course 1 - Structured Hiring That Works/overview.md`

**Voice and Tone Guidance:**
- Location: `Online Courses/00-Voice and Tone/`
- Primary document: `Brand Voice and Tone.md` (comprehensive 340-line voice guide)
- Secondary: `CLAUDE.md` (agent instructions)
- Read before generating any course content

**Strategy and Planning:**
- `COURSE_STRATEGY_DELIVERABLE.md` - Market analysis, content inventory, go-to-market roadmap
- Location: `Online Courses/` directory root
- Contains full content audit, topic clustering, commercial readiness assessment

### Directory Naming

**Kebab-case for course directories** (with numbers):
- `Course N - Course Title/` (numbers 1-10)
- Example: `Course 5 - AI-Powered HR/`

**PascalCase or Title Case for topical/reference directories:**
- `00-Voice and Tone/`
- `Reference Materials/`

---

## Markdown Structure and Style

### Document Headers

**Top-level metadata block:**
```markdown
# Title

> Last updated: [Date]
> Status: [Active/Draft/Archived]
> [Optional context line]
```

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` (lines 1-6)

**Section headers (heading levels 2-4):**
```markdown
## Section Name

### Subsection Name

#### Sub-subsection Name
```

No heading level 1 in body content (reserved for title).

### Tables for Comparison and Reference

Tables are used extensively for organizing complex information:

**Voice/Tone mapping tables:**
- Trait-to-description mapping: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 19-25
- Tone-by-context: Lines 45-54
- Dimension guardrails: Lines 60-67

**Content inventory tables:**
- Course/directory-to-content mapping: `COURSE_STRATEGY_DELIVERABLE.md` lines 15-23
- Topic-to-frameworks mapping: Lines 29-50
- Commercial readiness assessment: Multiple columns showing file type, depth, and notes

**Example: Topic cluster table**
```markdown
| Audience | Depth | Vocabulary | Sentence Length | Theory Naming |
|----------|-------|------------|-----------------|---------------|
| HR Professionals | Full depth | Technical I/O terms | Longer, multi-clause | Full theory names |
| People Managers | Moderate | Plain language + technical | Medium | Theory as anchors |
```

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 191-198

### Blockquotes for Emphasis or Examples

Blockquotes highlight guidelines, cautions, or illustrative examples:

```markdown
> "This is a direct quote showing evidence-anchored authority."
```

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 280-288 (tone calibration examples with "Wrong" and "Right" patterns)

### Lists (Unordered and Ordered)

**Unordered lists** for attributes, characteristics, or non-sequential items:
```markdown
**Key Characteristics:**
- Evidence-Anchored Authority
- Progressive Scaffolding
- Quantitative Precision
```

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 22-25

**Ordered lists** for sequential steps or ranked items:
```markdown
1. Frame the problem with stakes
2. Define terms precisely
3. Review the evidence systematically
```

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 154-159

### Inline Formatting

**Bold** for key terms, voice traits, emphasis:
- `**Evidence-Anchored Authority**` - Voice trait definition
- `**MUST:**` - Requirement labels in content rules

**Italics** for publication titles, file paths, or conceptual names:
- `*Teresa's voice guide* governs course content`
- `*The Teresa Ristow Argument Structure*`

**Code blocks** for actual code, file paths (backticks), or structured examples:
- `Assignment 1.md` - File path
- `\`Online Courses/00-Voice and Tone/Brand Voice and Tone.md\`` - Reference

See usage throughout: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 18-142

---

## Voice and Tone Standards

### Single Source of Truth

**File:** `Online Courses/00-Voice and Tone/Brand Voice and Tone.md`

This 340-line document defines Teresa Ristow's intellectual voice and writing patterns. It is mandatory reference for all course content generation.

### Five Core Voice Traits (Non-Negotiable)

1. **Evidence-Anchored Authority** - Every claim connects to named research, theory, or data
2. **Progressive Scaffolding** - Concepts build layer by layer: define → contextualize → evidence → apply
3. **Quantitative Precision** - Exact numbers over vague qualifiers
4. **Framework Thinking** - Complex problems organized into named, structured systems
5. **Practitioner Bridge** - Every theoretical point resolves to organizational/individual implication

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 17-35

### Tone by Content Type

Tone adapts by audience while staying within bounded range:

| Content Type | Tone | Key Pattern | Reference |
|---|---|---|---|
| Module scripts (core teaching) | Measured authority with warmth | First-person plural; direct address; concepts with care | Lines 47 |
| Professional blogs | Direct authority, problem-first | Named problem; structured findings; labeled takeaways | Lines 48 |
| Assessment questions | Clear, precise, scenario-grounded | Realistic framing; no trick questions | Lines 50 |
| Templates/tools | Direct, instructional | Imperative mood; step-by-step; no hedging | Lines 51 |
| Sales pages | Confident expertise, anti-hype | Lead with learner outcomes; backed by research base | Lines 52 |
| Email sequences | Conversational authority | First person (Teresa); one-idea-per-email; warmth | Lines 53 |

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 43-54

### Sentence-Level Patterns (Preserved)

**Theory naming before application:**
- Name the psychological theory before applying it
- Academic: "Drawing upon Impression Management Theory (Goffman, 1949)..."
- Practitioner adaptation: "Impression Management Theory explains why..."

**Evidence-first claim structure:**
- Evidence appears before or alongside the claim
- "When researchers audited 7,500 survey interviewers, between 0.2% and 3.5% had fabricated their data."

**Implications spelled out explicitly:**
- Never leave implications implicit
- "For the individual employee, this means less daily stress. For your organization, it means lower absenteeism."

**Progressive definitions:**
- Define terms before using them in arguments, building from general to specific
- See: Lines 97-99 of voice guide (access to work definition)

**Labeled practical takeaways:**
- Use explicit labels: "What this means for design:", "How to use CAPTUR"
- See: Lines 114-116 of voice guide

**Real voices as evidence:**
- Integrate direct quotes from workers/practitioners as form of evidence alongside citations
- Example: Line 120

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 71-125

### Prohibited Patterns

Never use in any course content:

| Pattern | Why It Violates Voice |
|---------|----------------------|
| Exclamatory enthusiasm ("This is incredible!") | Confidence is quiet and evidence-based, not performative |
| Vague evidence ("Studies show...") | Must name the study and finding |
| Em-dashes | Universal ban inherited from root CLAUDE.md |
| Oversimplified prescriptions ("Just do X") | Must acknowledge tradeoffs and context |
| Forced casualness ("So here's the deal...") | Naturally accessible, not performatively informal |
| Rhetorical questions as transitions | Use declarative transitions; questions only when genuine |
| Inspirational register ("You can change the world!") | Pragmatic, not aspirational |
| Fear-based urgency ("If you don't do this...") | Present evidence; reader draws own urgency |

See full list: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 127-142

### Unique Intellectual Signatures (Integrate Naturally)

Teresa's writing reflects these perspectives — integrate into course content:

1. **Person-Centered Over One-Size-Fits-All** - Acknowledge heterogeneity; avoid blanket prescriptions
2. **Evidence-Based Skepticism** - Question whether common practices actually work
3. **Bridging Quantitative Rigor and Human Stakes** - Connect methods to human outcomes
4. **AI as Tool, Not Solution** - Evaluate AI with same rigor as any method; neither hype nor dismiss
5. **Multi-Source Evidence Integration** - Triangulate academic citations + industry data + practitioner voices
6. **Systems Thinking About Unintended Consequences** - Map second-order effects of interventions

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 202-241

---

## Content Adaptation Rules

When converting academic materials to commercial courses, follow these mandatory rules:

### MUST DO

- **Strip academic citation format** - Move parenthetical (Author, Year) citations to "Further Reading" sections; keep researcher names and findings in prose
- **Replace psychometric terminology** - Translate specialist language for practitioner audience
- **Add actionable tools to every module** - Downloadable templates, checklists, scorecards, worksheets, calculators
- **Include real-world examples** - Appropriate to target segment; grounded in realistic detail
- **Maintain evidence-based accuracy** - Cite the research; don't write like a journal article

### MUST NOT DO

- **Fabricate statistics or research findings** - Every number must be traceable to source
- **Use copyrighted article text verbatim** - Summarize and cite instead
- **Include unmodified exam questions** - Adapt academic assessments before reuse
- **Claim certification or credit** - Without proper accreditation
- **Remove nuance for oversimplification** - Respect complexity; name limitations

### Language Substitutions

| Use | Don't Use | Why |
|-----|-----------|-----|
| "evidence shows" | "studies suggest" | More authoritative |
| "practitioners" | "students" | Commercial context |
| "your organization" | "the organization" | Direct address; second person |
| Active voice, imperative mood | Passive voice in instructions | Clarity; directness |
| Sentences under 25 words | Run-on sentences | Readability for digital |
| No hedging language | "it could be argued that..." | Clear, direct voice |

See: Root `CLAUDE.md` lines 140-146

### Module Target Length

**Video module:** 15-20 minutes of content
- Includes: Lesson script, examples, key takeaways
- Not: Full academic depth or every citation

**Downloadable template/tool:** 1-3 pages
- Actionable and usable in actual work contexts

See: Course overview files (e.g., `Course 1/overview.md` line 37)

---

## Audience Calibration

Adjust depth, vocabulary, and theory naming based on target audience:

| Audience Segment | Depth | Vocabulary | Theory Naming |
|---|---|---|---|
| HR Professionals (Segment 1) | Full depth | Technical I/O terms with brief glossing | Full theory names with explanation |
| People Managers (Segment 2) | Moderate; application-focused | Plain language + technical intro | Theory as anchors ("Psychologists call this...") |
| Small Business Owners (Segment 3) | Application-heavy | Everyday business language | Theory by implication ("80+ years of selection science") |
| I/O Psych Students (Segment 4) | Full academic depth | Full technical vocabulary assumed | Full names; no glossing |
| Job Seekers (Segments 10-11) | Moderate; "what's in it for me" | Consumer-friendly; glossed jargon | Insider knowledge framing |
| Career Coaches/B2B (Segment 12) | Full depth; teach-ability focus | Professional vocabulary | Full theory names as tools |

See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 191-198

---

## Required Quality Gates

### Humanizer 2 Requirement

**Mandatory.** All content intended as human-readable or final-draft output must be run through `/humanizer2` before delivery.

**Scope:**
- Module scripts and lesson content
- Assessment questions and answer keys
- Practitioner summaries and research syntheses
- Templates, checklists, tool descriptions
- Course descriptions, sales pages, email sequences
- Video script outlines

**Exempt:**
- Internal/structural outputs (file listings, status updates, CLAUDE.md edits)
- Data tables
- Code samples

See: Root `CLAUDE.md` lines 193-201

### Voice Compliance Checklist

Before generating any course content, verify:

- [ ] Claims are evidence-anchored (theory named or finding cited)
- [ ] Concepts build progressively (define → contextualize → evidence → apply)
- [ ] Numbers are precise, not vague
- [ ] Every theoretical point connects to practitioner action/implication
- [ ] Limitations and nuance acknowledged, not hidden
- [ ] Tone is measured confidence: authoritative without dismissiveness, accessible without dumbing down
- [ ] No prohibited patterns (see prohibited list above)
- [ ] Humanizer 2 pass completed

See: `Online Courses/00-Voice and Tone/CLAUDE.md` lines 27-33

### Content Adaptation Verification

Before submitting adapted content:

- [ ] Academic citations moved to "Further Reading" (not removed)
- [ ] Psychometric terms translated to plain language
- [ ] At least one downloadable template/tool included
- [ ] Real-world examples grounded in specifics (not hypothetical)
- [ ] Evidence accuracy verified against source materials
- [ ] No copyrighted article text used verbatim
- [ ] Exam questions adapted (not copied directly)
- [ ] No fabricated numbers or claims

---

## Template and Tool Patterns

### Module Script Template

Standard structure observed in course overviews and strategic planning:

```markdown
# Module [N]: [Topic Name]

## Overview
[1-2 sentences on what learner will know/do]

## Key Concepts
[3-5 major concepts with definitions]

## Evidence and Frameworks
[Named theory or research finding with data]

## Practitioner Implications
[What this means for your organization]

## Key Takeaway
[Single, actionable insight]

## Downloadable Resource
[Link to template/checklist/tool]
```

See structure inferred from: `Online Courses/Course 1 - Structured Hiring That Works/overview.md` (MVP scope section, lines 60-66)

### Assignment and Answer Key Structure

**Assignment prompt format:**
- Header with assignment number and course code
- Instructions section (highlighted or marked)
- Case study or scenario (if applicable)
- Numbered questions with specific prompts
- Word/page count or response guidance

See: `Online Courses/Reference Materials/Performance Mgmt Materials/Assignments/Assignment 1.md` (lines 1-32)

**Answer key format:**
- Repeats assignment prompt for reference
- For each question:
  - **Question restated in bold**
  - "Key Points Students Should Address:" section
  - Bulleted key concepts and examples
  - (Optional) Rubric or scoring guidance

See: `Online Courses/Reference Materials/Performance Mgmt Materials/Assignments/Assignment 1 Answers.md` (lines 1-73)

### Templates for Downloadables

Common formats for course resources:

**Scorecard/Rating Scale:**
- Column headings: [Criterion], [Definition], [Rating Scale]
- Rows: Specific behaviors or competencies to assess
- Includes: Instructions for use, scoring guidance

Example reference: `Structured interview framework` mentioned in Course 1 overview (line 46) points to `Selection Measures 2 Interviews.md` in reference materials

**Checklist:**
- Series of yes/no items or action steps
- Can include: Importance weighting, completion status tracking
- Format: Markdown list or simple table

**Worksheet:**
- Guided questions or fill-in-the-blank structure
- Progressive depth (foundational → advanced)
- Includes: Space for notes or responses

**Calculator/Spreadsheet:**
- Excel or CSV format with formulas
- Instructions for input parameters
- Outputs summary statistics or recommendations

Example: `Adverse impact calculator spreadsheet` (Course 1 MVP, line 70)

---

## Hyperlinks and References

### Linking to Files

Use relative paths in backticks for file references within SOUP repo:

```markdown
See: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` (lines [N-N])
```

### Referencing Frameworks and Models

When referencing Teresa's unique intellectual frameworks:

**AIRA Framework:**
- Location: `Publications/Chapter 18.md`
- Context: AI-enabled workplace inclusion; five pillars (Autonomy, Individualization, Representation, Anonymity, Belonging)

**LPA + NLP for Job Ads:**
- Location: `Publications/Ristow_TL_D_2023.md`
- Context: Dissertation on deception perception in job ads; directly applicable to job-seeker courses (8-10)

**CAPTUR Framework:**
- Location: `Microsoft Blogs/CAPTUR HITS.md`
- Context: Human evaluation of conversational AI; six dimensions with behavioral anchors

**Curbstoning Detection:**
- Location: `Publications/Curbing-Curbstoning*.md`
- Context: Survey data fabrication detection methods

---

## Cross-Reference Navigation

**Voice and Tone Rules:**
- Primary: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` (comprehensive)
- Secondary: `Online Courses/00-Voice and Tone/CLAUDE.md` (agent instructions; quick reference)
- Root constraint: `/root CLAUDE.md` (universal rules: no em-dashes, no fabricated numbers, language bans)

**Content Inventory and Strategy:**
- `Online Courses/COURSE_STRATEGY_DELIVERABLE.md` - Full market analysis, topic clusters, commercial readiness
- Individual course `overview.md` files - Specific course scope, audience, effort estimate

**Course Architecture:**
- `Online Courses/Course N - Course Title/overview.md` - Course-level specifications
- Course subdirectories (to be created) - Module scripts, templates, assessments

---

## Markdown Formatting Rules

### Consistent Styling

- **Headings:** Use `#` for document title; `##` for sections; `###` for subsections
- **Emphasis:** Bold for key terms and requirements; italics for titles and concepts
- **Lists:** Unordered for attributes; ordered for sequences
- **Tables:** Use for comparison, mapping, reference matrices
- **Code/Paths:** Inline backticks for file paths and code references
- **Blockquotes:** For evidence, examples, cautions

### No Fabrication or Hedging

- **Exact numbers:** "48%-90% detection accuracy" not "high accuracy"
- **Named sources:** "Schmidt and Hunter (1998) found" not "research suggests"
- **Direct language:** "This approach works best when" not "might possibly work in some cases"

---

## Summary: Key Documents to Read Before Creating Content

1. **`Online Courses/00-Voice and Tone/Brand Voice and Tone.md`** (mandatory) - Teresa's voice fingerprint
2. **Root `CLAUDE.md`** (mandatory) - Content adaptation rules and audience segmentation
3. **`Online Courses/COURSE_STRATEGY_DELIVERABLE.md`** - Content inventory and topic clusters
4. **Specific course `overview.md`** - Scope and audience for that course

---

*Convention analysis: 2026-04-13*

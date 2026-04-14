# Testing and Quality Assurance (Content Repository)

**Analysis Date:** 2026-04-13

This document describes QA processes, review gates, and content validation patterns for SOUP course materials.

---

## Quality Framework Overview

For a content repository (not software), "testing" means:

1. **Content accuracy verification** - Claims are evidence-anchored; numbers traceable to sources
2. **Voice/tone compliance** - Matches Teresa Ristow's intellectual voice standards
3. **Pedagogical structure** - Concepts build progressively; learning objectives clear
4. **Audience appropriateness** - Terminology and depth calibrated to target segment
5. **Humanizer2 pass** - All human-facing content passes through humanizer before delivery
6. **Assignment/assessment design** - Answer keys align with questions; rubrics are clear

---

## Voice and Tone Compliance (Primary QA Gate)

### Quick Compliance Checklist

**Before any content leaves your workspace, verify all items:**

- [ ] **Claims are evidence-anchored** - Every substantive claim names a theory, cites a finding, or references data
- [ ] **Concepts build progressively** - Define → contextualize → evidence → apply (not dropped conclusions)
- [ ] **Numbers are precise** - "6.3% of interviewers" not "a significant portion"; exact percentages, sample sizes
- [ ] **Theory is named** - Psychological theories referenced explicitly (even in practitioner content)
- [ ] **Practitioner bridge is explicit** - Every theoretical point resolves to "what this means for your organization"
- [ ] **Nuance is acknowledged** - Limitations, tradeoffs, and contextual factors stated, not hidden
- [ ] **Tone is measured confidence** - Authoritative without dismissiveness; accessible without dumbing down
- [ ] **No prohibited patterns** - See prohibited list below
- [ ] **Humanizer 2 pass complete** - Final pass before delivery

**Location of standards:** `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` (comprehensive); `Online Courses/00-Voice and Tone/CLAUDE.md` (quick reference)

### Prohibited Patterns (Hard Stops)

Never release content with these patterns:

| Pattern | Violation | Example |
|---------|-----------|---------|
| Em-dashes | Universal ban | "The interview—" should be "The interview." or "The interview; it..." |
| Vague evidence appeals | No "studies show..." without naming study and finding | "Research shows structured interviews work" → "Schmidt & Hunter's 85-year meta-analysis found validity coefficients of .51 for structured vs. .38 for unstructured" |
| Fabricated statistics | All numbers traceable to source | Any invented percentage or sample size |
| Exclamatory enthusiasm | Violates measured confidence | "This is incredible!" → Remove or reframe with evidence |
| Oversimplified advice | Ignores complexity | "Just do X" → "This approach works best when [conditions], with limitations of [constraints]" |
| Forced casualness | Violates natural voice | "So here's the deal..." → Rewrite in conversational authority |
| Rhetorical questions as transitions | Use declarative statements | "But what about...?" → "Consider the alternate scenario..." |
| Inspirational register | Pragmatic, not aspirational | "You can change the world of hiring!" → "The evidence supports this approach for these reasons..." |
| Fear-based urgency | No scarcity tactics | "If you don't do this, you're doomed" → Present evidence; reader determines urgency |

**Reference:** `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 127-142

### Tone by Content Type Verification

Verify content tone matches its context:

| Content Type | Expected Tone | Verification Questions |
|---|---|---|
| **Module scripts** | Measured authority with warmth | Does it use first-person plural? Are concepts introduced with care? Is warmth expressed through specificity, not cheerleading? |
| **Assessment questions** | Clear, precise, scenario-grounded | Are questions realistic and fair? Do they test understanding, not memorization? Are scenarios specific and believable? |
| **Templates/tools** | Direct, instructional | Is every instruction clear and actionable? Does it use imperative mood? Does it avoid hedging? |
| **Sales pages** | Confident expertise, anti-hype | Does it lead with learner outcomes? Are claims backed by research base? Does it avoid scarcity tactics or inflated promises? |
| **Email sequences** | Conversational authority | Does it use first person (Teresa speaking)? Is one idea per email? Are sentences shorter than module prose? |

**Reference:** `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 43-54

### Unique Intellectual Signature Integration

Content should reflect these Teresa Ristow perspectives (verify at least 2-3 are evident):

1. **Person-Centered Over Blanket Solutions** - Does it acknowledge heterogeneity within groups or contexts?
2. **Evidence-Based Skepticism** - Does it question whether common practices actually work, backed by evidence?
3. **Bridging Quantitative Rigor and Human Stakes** - Does it connect methods/data to human outcomes?
4. **AI as Tool, Not Solution** - If AI is discussed, is it evaluated rigorously? Neither hyped nor dismissed?
5. **Multi-Source Evidence** - Does it triangulate academic citations + industry data + practitioner voices?
6. **Systems Thinking** - Does it map second-order consequences of interventions?

**Reference:** `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 202-241

---

## Content Accuracy Verification

### Evidence-Anchoring Standards

Every substantive claim must pass one of these tests:

#### Test 1: Named Theory or Research Finding
```
PASS: "Self-Determination Theory, developed by Ryan and Deci, identifies three psychological needs..."
FAIL: "People need autonomy" (without theoretical foundation)
```

#### Test 2: Specific Data with Source
```
PASS: "Schmidt and Hunter's 1998 meta-analysis of 85 years of selection research found validity coefficients of .51 for structured interviews compared to .38 for unstructured."
FAIL: "Studies show structured interviews work better"
```

#### Test 3: Precise Percentages or Metrics
```
PASS: "Between 1% and 2% of interviewers fabricate data in most U.S. contexts"
FAIL: "A small percentage of interviewers have integrity issues"
```

### Fact-Checking Process

When adapting academic materials to commercial content:

1. **Locate original source** - Track academic citations back to source materials (usually in `Online Courses/Reference Materials/`)
2. **Verify claim accuracy** - Compare commercial version against academic source
3. **Check numbers** - Confirm percentages, sample sizes, effect sizes are exact and traceable
4. **Validate interpretation** - Ensure claim represents the actual research finding, not an overinterpretation

**Example verification chain:**

- Academic source: `Online Courses/Reference Materials/Performance Mgmt Materials/Assignment 1 Answers.md` (line 29) cites "Pulakos, 2009"
- Claim to verify: "Company uses episodic appraisal rather than continuous performance management"
- Verification: Check that `Pulakos (2009).md` exists in reference materials and contains this distinction
- Output: Cite as "Drawing from performance management research (Pulakos, 2009)..." in practitioner content

### Citation Handling

**Academic content:** Full citations with Author, Year, and details
- Location: Source materials in week subdirectories
- Example: `Assignment 1.md` includes parenthetical citations like "(Pulakos, 2009)"

**Commercial content:** Strip parenthetical format; weave into prose
- Location: Module scripts, lesson content
- Pattern: "Pulakos (2009) distinguished between episodic appraisal and continuous performance management" → "Performance management research distinguishes between reactive annual reviews and continuous feedback systems (Pulakos, 2009)"
- Further Reading: Move full citations to end-of-module reference list

**Rule:** No claim loses its citation; format changes from academic to practitioner register.

---

## Assessment and Assignment QA

### Assignment Structure Validation

When creating or adapting assignments, verify this structure:

**Assignment Prompt File (`Assignment N.md`):**
- [ ] Header with assignment number and course code
- [ ] Clear instructions (highlighted or marked)
- [ ] Case study or scenario (realistic, specific details)
- [ ] Numbered questions with precise prompts
- [ ] Word/page count or length guidance
- [ ] Due date or submission format (if applicable)

**Example:** `Online Courses/Reference Materials/Performance Mgmt Materials/Assignments/Assignment 1.md` (lines 1-32)

**Answer Key File (`Assignment N Answers.md` or `Assignment N KEY.md`):**
- [ ] Repeats assignment prompt for reference context
- [ ] For each question:
  - [ ] Question restated in bold
  - [ ] "Key Points Students Should Address:" section
  - [ ] Bulleted key concepts and examples
  - [ ] Scoring guidance or rubric (if applicable)
- [ ] Cites relevant theories, frameworks, research
- [ ] Includes sample student response (if appropriate)

**Example:** `Online Courses/Reference Materials/Performance Mgmt Materials/Assignments/Assignment 1 Answers.md` (lines 1-80)

### Assessment Question Design Standards

All assessment questions (module quizzes, knowledge checks, final assessments) should:

**Clarity & Fairness:**
- [ ] Question is unambiguous; no trick wording
- [ ] Multiple choice options are mutually exclusive
- [ ] Question tests understanding, not just memorization
- [ ] Scenario (if included) is realistic and grounded in specifics

**Alignment with Learning Objectives:**
- [ ] Question matches module topic and depth level
- [ ] For practitioner courses: Tests ability to apply concept to real situation
- [ ] For academic learners: Tests conceptual understanding and nuance

**Tone Appropriateness:**
- [ ] Scenario uses inclusive language and realistic contexts
- [ ] No assumptions about learner background knowledge (beyond course level)
- [ ] Phrasing is direct and professional

**Example (from reference materials):**

```markdown
**GOOD (scenario-grounded, tests application):**
"A hiring manager tells you their structured interview 'doesn't feel natural.' 
Based on what the research shows about structured vs. unstructured interviews, 
what is the most evidence-based response?"

BAD (vague, tests memorization):**
"What is something about structured interviews?"
```

### Rubric and Scoring Guidance

For open-ended assignments (case study responses, essays):

**Rubric should include:**
- [ ] Clear criteria for evaluation (e.g., evidence use, application, clarity)
- [ ] Point values or proficiency levels (e.g., Beginning, Developing, Proficient, Advanced)
- [ ] Specific descriptors for each level (what does Proficient look like?)
- [ ] Examples of strong vs. weak responses (if appropriate)

**Example observed in answer keys:**
- Line 27 of `Assignment 1 Answers.md`: "Key Points Students Should Address:" followed by bulleted expected content
- Implicit rubric: Responses that address these points at full depth receive full credit

---

## Humanizer 2 Quality Gate

### Mandatory Requirement

**ALL content intended as human-readable or final-draft output must pass Humanizer 2 before delivery.**

**What requires Humanizer 2:**
- Module scripts and lesson content
- Assessment questions and answer explanations
- Practitioner summaries and research syntheses
- Templates, checklists, tool descriptions
- Course descriptions, sales pages, email sequences
- Video script outlines and talking points
- Community posts and student-facing communication

**What does NOT require Humanizer 2:**
- Internal file listings or status updates
- CLAUDE.md edits or metadata
- Data tables or spreadsheets
- Code samples or technical documentation
- File organization or directory structure notes

### Humanizer 2 Process

Humanizer 2 is an AI writing quality service that evaluates content for:

**Composition:**
- Logical flow and organization
- Paragraph coherence
- Transition effectiveness
- Argument development

**Sentence-Level Quality:**
- Clarity and directness
- Variety in structure
- Elimination of redundancy
- Active voice and imperative mood

**Content & Messaging:**
- Claim support and evidence
- Audience appropriateness
- Tone consistency
- Message clarity and impact

**Language & Formatting:**
- Word choice precision
- Grammar and mechanics
- Punctuation effectiveness
- Consistent style and formatting

**Communication Effectiveness:**
- Reader engagement
- Persuasiveness (where appropriate)
- Accessibility to target audience
- Call-to-action clarity

**Reference:** Root `CLAUDE.md` lines 193-201; `Online Courses/00-Voice and Tone/CLAUDE.md` lines 25-27

### Humanizer 2 in Your Workflow

1. **Write content** following voice/tone standards
2. **Self-review** using compliance checklist above
3. **Pass through Humanizer 2** (`/humanizer2` skill)
4. **Implement Humanizer2 recommendations** that align with Teresa's voice
5. **Deliver** final version

**Note:** Humanizer 2 recommendations are advisory. If a suggestion conflicts with Teresa's voice standards, prioritize voice. Example: If Humanizer 2 recommends shorter sentences but Teresa's pattern uses multi-clause sentences to show logical progression, keep the longer sentence.

---

## Template and Tool QA

### Downloadable Template Standards

Every commercial module should include at least one downloadable tool. QA checklist:

**Scorecards/Rating Scales:**
- [ ] Clear column headings (Criterion, Definition, Rating Scale, etc.)
- [ ] Behavioral anchors for each rating level (not just numbers)
- [ ] Instructions for use (how to complete, when to use)
- [ ] Example or sample completion (if complex)
- [ ] Scoring guidance (how to interpret results)

**Checklists:**
- [ ] Sequential or logical grouping of items
- [ ] Clear language; each item is independently understandable
- [ ] Actionable (yes/no questions or concrete actions)
- [ ] Can include: weighting, priority levels, timeline
- [ ] Instructions on how/when to use

**Worksheets:**
- [ ] Progressive depth (foundational questions → advanced)
- [ ] Guided prompts with space for responses
- [ ] Instructions for completion
- [ ] Can include: reflection prompts, planning sections, space for examples

**Calculators (Excel/CSV):**
- [ ] Clear input parameters with instructions
- [ ] Formulas working correctly
- [ ] Output summary with interpretation guidance
- [ ] Example data showing expected output

**Example reference:** `Online Courses/Course 1 - Structured Hiring That Works/overview.md` (lines 67-70) lists MVP deliverables:
- Interview scorecard template
- Sample structured interview guide
- Adverse impact calculator spreadsheet

### Practical Usability Test

Before releasing a template:

1. **Can a practitioner complete it without additional training?** (Assumed audience: HR professional, manager, or career coach — not a specialist)
2. **Is the output actionable?** (Does completion lead to a decision or action?)
3. **Is the format accessible?** (Markdown table, downloadable PDF, Excel spreadsheet — matches audience tech comfort)

---

## Audience Calibration Verification

### Depth and Vocabulary Check

For each course or module, verify audience calibration:

**HR Professionals (Segment 1) — Full Depth:**
- [ ] Technical I/O psychology terms used with assumption of baseline knowledge
- [ ] Theories named without extensive explanation: "Expectancy Theory explains..."
- [ ] Research depth includes methodology, effect sizes, confidence intervals where relevant
- [ ] Example language: "This approach leverages person-job fit principles to..."

**People Managers (Segment 2) — Moderate, Application-Focused:**
- [ ] Plain language with technical terms introduced as vocabulary: "In I/O psychology, we call this..."
- [ ] Theories as anchors: "Psychologists found that..."
- [ ] Practical application foregrounded; theory as credibility backing
- [ ] Example language: "Managers often struggle with [problem]. Research on Equity Theory shows why..."

**Small Business Owners (Segment 3) — Application-Heavy:**
- [ ] Everyday business language; no jargon without explanation
- [ ] Theory by implication: "The hiring methods backed by 80+ years of research..."
- [ ] Focus on ROI and immediate applicability
- [ ] Example language: "Your hiring decisions affect your bottom line. Here's what works..."

**Job Seekers (Segments 10-11) — Moderate, "What's in It for Me":**
- [ ] Consumer-friendly tone; no unexplained jargon
- [ ] Insider knowledge framing: "Here's what the hiring side knows that candidates usually don't..."
- [ ] Emphasis on decision-making: "When evaluating an offer, look for..."
- [ ] Example language: "Job descriptions are written in a specific way. Understanding that language helps you..."

**Full reference:** `Online Courses/00-Voice and Tone/Brand Voice and Tone.md` lines 187-198

---

## Content Inventory and Readiness Tracking

### Commercial Readiness Levels

The `COURSE_STRATEGY_DELIVERABLE.md` categorizes all existing content by commercial readiness. When QAing adapted content, note readiness level:

| Readiness | Meaning | QA Focus |
|-----------|---------|----------|
| **Introductory** | Foundational, accessible to broad audience | Verify clarity and no jargon |
| **Intermediate** | Practitioner-ready with minimal translation | Verify audience calibration and practical application |
| **Advanced** | Academic depth; needs translation | Verify evidence-anchoring and audience appropriateness after adaptation |
| **High commercial value** | Unique, market-differentiating content | Verify accuracy and Teresa's voice integrity |

**Example:** `COURSE_STRATEGY_DELIVERABLE.md` line 43 rates "Selection Measures 2 Interviews" as "Advanced" with "Highest commercial value in selection cluster."

---

## Revision and Feedback Cycles

### What to Check in Revised Content

When reviewing revised or updated content:

1. **Compliance checklist** - Re-verify all voice/tone items (revisions often introduce violations)
2. **Evidence integrity** - Confirm citations weren't lost or changed
3. **Audience appropriateness** - Check that edits maintain correct depth for target segment
4. **Tool usability** - If templates were modified, re-test practical usability
5. **Humanizer 2 re-pass** - If substantive content changes, run through Humanizer 2 again

---

## Content Types and Their QA Patterns

### Module Scripts (Core Lesson Content)

**Structure to verify:**
- [ ] Opener frames the problem or learning objective (not just "today we'll discuss...")
- [ ] Concepts introduced with definitions before application
- [ ] Evidence woven throughout (not lumped at end)
- [ ] Examples are specific and realistic to target audience
- [ ] Practitioner implications stated explicitly ("What this means for you...")
- [ ] Closer reinforces key takeaway and points to downloadable resource

**Length:** 15-20 minute read/watch (approximately 2,000-3,000 words for scripts)

**Humanizer 2 requirement:** YES

### Assessment Questions (Quizzes, Knowledge Checks)

**QA checklist:**
- [ ] Question is clear and unambiguous
- [ ] Scenario (if included) is realistic and specific
- [ ] Tests understanding, not just recall
- [ ] Appropriate difficulty level for module
- [ ] No trick wording or multiple correct answers (unless intentional)

**Humanizer 2 requirement:** YES (for wording clarity)

### Answer Keys and Rubrics

**QA checklist:**
- [ ] Repeats question for context
- [ ] Identifies key concepts to address
- [ ] Provides sample strong response (if appropriate)
- [ ] Scoring guidance is clear and objective
- [ ] Cites relevant theories or research
- [ ] Balanced: not favoring one view if research is mixed

**Humanizer 2 requirement:** YES (for clarity)

### Downloadable Templates and Tools

**QA checklist:**
- [ ] Instructions are clear and complete
- [ ] Layout is professional and usable
- [ ] Tool is functional (formulas work, logic is clear)
- [ ] Can be completed/used without additional training
- [ ] Output is actionable or interpretable

**Humanizer 2 requirement:** YES (for instruction clarity only; not data tables)

### Sales Pages and Course Descriptions

**QA checklist:**
- [ ] Lead with learner outcomes (what will they know/do?)
- [ ] Back claims with evidence or research base
- [ ] Avoid hype or scarcity tactics
- [ ] Voice is confident expertise, not desperation
- [ ] Tone is direct and problem-centric (not aspirational)
- [ ] Call-to-action is clear

**Humanizer 2 requirement:** YES

---

## Review Gate Workflow

### Pre-Submission Checklist (For Content Creators)

Before delivering any course content:

```
VOICE & TONE
[ ] Claims are evidence-anchored (theory named or finding cited)
[ ] Concepts build progressively (define → evidence → apply)
[ ] Numbers are precise (not vague qualifiers)
[ ] Theories are named explicitly
[ ] Practitioner implications are stated
[ ] Limitations and nuance are acknowledged
[ ] Tone matches content type expectations
[ ] No prohibited patterns (em-dashes, vague appeals, hype, etc.)

ACCURACY
[ ] All numbers are traceable to sources
[ ] No copyrighted text used verbatim
[ ] Citations are accurate (not paraphrased incorrectly)
[ ] Research findings represent actual studies (not misquoted)

AUDIENCE
[ ] Depth is appropriate for target segment
[ ] Vocabulary is calibrated correctly
[ ] Theory naming matches audience level
[ ] Examples are relevant to audience

STRUCTURE
[ ] Learning objective is clear
[ ] Concepts introduced before application
[ ] Downloadable tool/resource is included
[ ] Key takeaway is reinforced at close

QUALITY
[ ] No grammatical errors or typos
[ ] Formatting is consistent
[ ] Headings use appropriate levels
[ ] Tables/lists are organized logically
[ ] Humanizer 2 pass completed (if human-facing)

FINAL GATE
[ ] This content represents Teresa's voice and expertise accurately
[ ] I would be comfortable with this bearing her name on a Kajabi course
[ ] Content passes all compliance checks above
```

---

## Documentation and Tracking

### Content QA Log

When significant content is completed or revised, document:

- **Date:** [Completion date]
- **Content:** [Module/template name and type]
- **Source:** [Academic source material, if adapted]
- **QA Lead:** [Name/agent]
- **Compliance:** [Passed all checks / Conditional on edits / Rejected]
- **Humanizer2:** [Passed / Pending / Not applicable]
- **Notes:** [Any concerns, edge cases, or follow-ups]

**Example entry:**
```
Date: 2026-04-13
Content: Course 1, Module 3: "The 15-Component Framework"
Source: Selection Measures 2 Interviews.md (W11)
Compliance: PASSED - Evidence anchored, voice consistent, practitioner examples included
Humanizer2: PENDING
Notes: Campion citations verified against original article. Scorecard template usable.
```

---

## Maintenance and Continuous Improvement

### When to Re-Review Content

Re-run QA checklist if:

1. **Academic source material is updated** - Verify claims still accurate
2. **Content is adapted for different audience segment** - Verify new audience calibration
3. **Humanizer 2 recommendations are implemented** - Confirm no unintended changes
4. **Course is bundled or cross-promoted** - Verify tone consistency across courses
5. **Seasonal or market changes occur** - Verify examples and case studies remain relevant

### Content Deprecation

Mark content for review/replacement if:

- [ ] Research cited is older than 10 years (unless foundational)
- [ ] Examples reference outdated tools or processes
- [ ] Audience feedback indicates examples don't resonate
- [ ] New research contradicts existing content

---

## Summary: Key QA Documents

**Voice and Tone Standards:**
- Primary: `Online Courses/00-Voice and Tone/Brand Voice and Tone.md`
- Quick reference: `Online Courses/00-Voice and Tone/CLAUDE.md`

**Content Adaptation Rules:**
- Root `CLAUDE.md` lines 122-146

**Humanizer 2 Requirement:**
- Root `CLAUDE.md` lines 193-201

**Assignment and Assessment Patterns:**
- Sample assignment: `Online Courses/Reference Materials/Performance Mgmt Materials/Assignments/Assignment 1.md`
- Sample answer key: `Online Courses/Reference Materials/Performance Mgmt Materials/Assignments/Assignment 1 Answers.md`

**Content Inventory and Readiness:**
- `Online Courses/COURSE_STRATEGY_DELIVERABLE.md` - Full readiness assessment of all existing materials

---

*Testing and QA analysis: 2026-04-13*

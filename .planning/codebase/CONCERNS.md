# Codebase Concerns

**Analysis Date:** 2026-04-13

## Critical Infrastructure Issues

### CLAUDE.md Path References Are Broken (HIGH SEVERITY)

**Issue:** Root repository `CLAUDE.md` references academic materials directories as if they exist at the root level, but they are actually located in `Online Courses/Reference Materials/`.

**Files:**
- `/Users/Christopher/Documents/GitHub/SOUP/CLAUDE.md` (lines 13-18, 64-67, 155)
- Referenced paths: `Publications/`, `Employee Selection Materials/`, `Performance Mgmt Materials/`, `Organizational Psych Materials/`, `Training Materials/`
- Actual paths: `Online Courses/Reference Materials/Publications/`, etc.

**Impact:** 
- Any Claude instance or automated process following the root CLAUDE.md will fail to locate source materials when building courses
- Course planners referencing these paths will be unable to navigate to actual files
- Blocks phase 2+ course development (Courses 3-10) that depend on cross-referencing these materials

**Fix Approach:**
1. Update `/Users/Christopher/Documents/GitHub/SOUP/CLAUDE.md` lines 13-18 to show correct paths under `Online Courses/Reference Materials/`
2. Update all path references throughout the file (e.g., line 64: `Publications/Chapter 18.md` → `Online Courses/Reference Materials/Publications/Chapter 18.md`)
3. Add a new section clarifying that these academic materials are now consolidated in `Online Courses/Reference Materials/` as a single reference library, not at repository root
4. Update `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/CLAUDE.md` to clarify this structure for agents working in the course directory tree

---

## Content Gaps: Module Scripts Missing

### All 10 Courses Lack Actual Module Scripts (PHASE-BLOCKING)

**Issue:** All ten course directories contain only `overview.md` files (strategic planning documents). Zero actual module scripts, lesson content, or video outlines exist.

**Files:**
- `Course 1 - Structured Hiring That Works/overview.md` (exists) → No module scripts
- `Course 2 - Performance Management That Actually Works/overview.md` (exists) → No module scripts
- `Course 3 - Training That Transfers/overview.md` (exists) → No module scripts
- `Course 4 - Leadership Development by Design/overview.md` (exists) → No module scripts
- `Course 5 - AI-Powered HR/overview.md` (exists) → No module scripts
- `Course 6 - Data-Driven DEI/overview.md` (exists) → No module scripts
- `Course 7 - Workplace Psychology Essentials/overview.md` (exists) → No module scripts
- `Course 8 - The Science of Getting Hired/overview.md` (exists) → No module scripts
- `Course 9 - Choose Wisely/overview.md` (exists) → No module scripts
- `Course 10 - The Hiring Insiders Toolkit/overview.md` (exists) → No module scripts

**Content Status by Course:**
| Course | Priority | Status | MVP Module Count | Progress |
|--------|----------|--------|-------------------|----------|
| 1 | Launch first | Planning only | 4 | 0% written |
| 2 | Launch first | Planning only | 5 | 0% written |
| 3 | Phase 2 | Planning only | 5 | 0% written |
| 4 | Phase 2 | Planning only | 4 | 0% written |
| 5 | Phase 2 | Planning only | 5 | 0% written |
| 6 | Phase 2 | Planning only | 4 | 0% written |
| 7 | Gateway | Planning only | 7 | 0% written |
| 8 | Phase 3 | Planning only | 5 | 0% written |
| 9 | Phase 3 | Planning only | 6 | 0% written |
| 10 | Phase 3 | Planning only | 4 | 0% written |

**Impact:**
- Cannot launch Courses 1-2 in "Month 3-4" as planned in overviews
- Cannot validate voice/tone compliance or Humanizer2 requirements
- No assessment questions, templates, or downloadable tools exist
- Video scripts do not exist (platform delivery blocked)

**Fix Approach:**
1. Prioritize module script creation for Courses 1-2 (launch-first tier) using academic source materials in `Online Courses/Reference Materials/Employee Selection Materials/` and `Online Courses/Reference Materials/Performance Mgmt Materials/`
2. Each module script must follow:
   - `00-Voice and Tone/Brand Voice and Tone.md` for Teresa Ristow's voice requirements
   - `Content Adaptation Rules` from root CLAUDE.md (strip academic format, add practitioner bridges, include templates)
   - **Mandatory Humanizer2 pass** before delivery
3. Create accompanying downloadable templates (scorecards, checklists, worksheets) for each module (specified in course overviews)
4. Establish module naming convention (suggest: `Module 1 - [Title].md`, `Module 1 - [Title] - Script.md`, `Module 1 - [Title] - Template.md`)

---

## Humanizer2 Compliance Gaps

### No Finalized Content Has Been Humanized (PROCESS GAP)

**Issue:** Root CLAUDE.md mandates Humanizer2 processing for all "generated content intended as human-readable or final-draft output," but:
- No module scripts exist yet to verify compliance
- Voice & Tone guide (`Brand Voice and Tone.md`) is comprehensive but was never humanized (though it is internal documentation)
- No process exists for confirming humanization before course materials are considered "done"

**Files:**
- `/Users/Christopher/Documents/GitHub/SOUP/CLAUDE.md` (lines 319-333 define Humanizer2 requirement)
- `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/00-Voice and Tone/CLAUDE.md` (lines 38-42 reference Humanizer2)

**Impact:**
- When module scripts are written, there is no gate ensuring they are humanized before being delivered to Kajabi
- Risk of robotic, AI-generated-sounding content being published under Teresa Ristow's name
- Violates both root CLAUDE.md and Online Courses CLAUDE.md requirements

**Fix Approach:**
1. Create a pre-commit checklist in `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/CLAUDE.md` that includes "Humanizer2 pass completed" as mandatory before module scripts are considered ready
2. Document in the Online Courses directory that module scripts must be structured as: (a) draft written by Claude, (b) passed through Humanizer2, (c) reviewed for voice compliance against `Brand Voice and Tone.md`, (d) committed only after all three gates pass
3. For each course, create a `_PROGRESS.md` file tracking which modules have been humanized

---

## IP / Copyright Risk: Dissertation and Publications

### Dissertation Heavily Cited in Multiple Courses (MODERATE RISK)

**Issue:** `Publications/Ristow_TL_D_2023.md` (Dissertation) is cited as primary content for Courses 8, 9, and 10. All three job-seeker courses depend on "perspective-flipped" application of dissertation findings.

**Files:**
- `Online Courses/Course 8 - The Science of Getting Hired/overview.md` (line 55): "Dissertation: NLP analysis of deceptive job ad language"
- `Online Courses/Course 9 - Choose Wisely/overview.md`: "Selection W3-4; ... Dissertation"
- `Online Courses/Course 10 - The Hiring Insiders Toolkit/overview.md`: References dissertation indirectly through Courses 8-9 repackaging

**Actual File:**
- `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/Reference Materials/Publications/Ristow_TL_D_2023.md` (364 KB, likely full dissertation text)

**Impact:**
- If dissertation is verbatim PDF-to-markdown conversion, direct copying into course modules would violate copyright (dissertation belongs to Virginia Tech or Teresa's copyright, not freely licensable for commercial reuse)
- Courses 8-10 cannot launch without clarity on what degree of dissertation content is available for commercial reuse

**Fix Approach:**
1. Verify copyright status: Does Teresa retain commercial rights to her dissertation, or do they belong to Virginia Tech?
2. Determine what dissertation content can be legally used in commercial courses (research findings are citable; verbatim text may not be)
3. Document in `Online Courses/CLAUDE.md` (new section): "IP Sourcing & Licensing"
   - Dissertation: What content is reusable and under what constraints
   - Chapter 18 (OUP 2026): Published book chapter; full reuse may be limited by publisher contract
   - Other publications: Copyright status of each
4. Create citation/attribution guidelines for Course 8-10 scripts that respect these constraints

---

### Chapter 18 / AIRA Framework Usage Across Multiple Premium Courses (MODERATE RISK)

**Issue:** The AIRA Framework from `Publications/Chapter 18.md` is positioned as Teresa's unique moat and is central to Courses 5 and 6 (both premium-priced at $497-997).

**Files:**
- `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/Reference Materials/Publications/Chapter 18.md` (published OUP 2026; DOI: 10.1093/9780197807309.003.0018)
- `Online Courses/Course 5 - AI-Powered HR/overview.md` (line 93-94 lists AIRA as IP #1)
- `Online Courses/Course 6 - Data-Driven DEI/overview.md` (line 23 references AIRA)
- `Online Courses/COURSE_STRATEGY_DELIVERABLE.md` (line 120 notes "Highest commercial potential")

**Impact:**
- Chapter 18 is published by Oxford University Press; commercial reuse may be restricted by publisher contract
- If Kajabi courses are not licensed/approved by OUP, course 5 and 6 could face takedown or licensing demands
- AIRA Framework is described as "forthcoming" in older materials, but Chapter 18 is now published (2026)

**Fix Approach:**
1. Review OUP contract for Chapter 18 to determine:
   - Derivative work restrictions (can she teach the framework in a commercial course?)
   - Attribution/citation requirements
   - Commercial use clauses
2. Add a section to `Online Courses/CLAUDE.md` documenting OUP terms
3. Build attribution into Courses 5 and 6 (e.g., course description: "Based on research published in [citation]")
4. If OUP prohibits direct commercial reuse, pivot Courses 5-6 to reference the framework while teaching practitioners to implement it using other tools/research (framework-inspired rather than framework-directly-taught)

---

## Source Material Coverage & Consistency Issues

### Organizational Psych Materials Exist but Not Referenced in Course Overviews (CONTENT GAP)

**Issue:** Full Organizational Psych Materials directory exists (`Online Courses/Reference Materials/Organizational Psych Materials/` with 14 weeks + assignments), but course overviews reference these materials inconsistently.

**Files:**
- `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/Reference Materials/Organizational Psych Materials/` (Weeks 2-13, Assignments 1-6)
- `Course 1 overview.md`: No reference to Org Psych materials
- `Course 2 overview.md`: No reference to Org Psych materials  
- `Course 7 - Workplace Psychology Essentials/overview.md`: Should heavily reference Org W4-12 per root CLAUDE.md (line 86) but not provided
- `Course 9 - Choose Wisely/overview.md`: Should reference Org W4, W6, W8, W12 per root CLAUDE.md (line 93) but not provided

**Impact:**
- Course 7 (gateway/lead magnet course) has no overview or content plan despite being scheduled for launch in "Month 2-3"
- Course 9 content mapping is incomplete
- Org Psych materials may be duplicative with other courses (e.g., Org W7 goal-setting overlaps with PM W7 goal-setting)

**Fix Approach:**
1. Create `Course 7 - Workplace Psychology Essentials/overview.md` immediately (required for gateway/lead magnet position)
2. Map Org Psych Materials weeks (2-13) to appropriate courses in the roadmap
3. Identify duplicative content between Org and PM materials (e.g., goal-setting, motivation, team PM) and consolidate sourcing strategy
4. Add cross-reference sections to course overviews showing which Org Psych weeks feed into which modules

---

### Social Psych Materials Completely Unused (LOW IMPACT)

**Issue:** `Online Courses/Reference Materials/Social Psych Materials/` exists with only 1 file (9 Helping and Altruism.md), not referenced in any course overview.

**Files:**
- `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/Reference Materials/Social Psych Materials/SLIDES/9 Helping and Altruism.md`

**Impact:** Low — PSYC 343 (Social Psychology) is not part of the commercial course lineup. This is orphaned reference material.

**Fix Approach:** Either archive or delete if not needed for future content.

---

## Fragile Areas: Heavy Reliance on Unwritten Adaptation Work

### Content Adaptation Requires Extensive Manual Conversion (EXECUTION RISK)

**Issue:** Course overviews specify content effort ratios (e.g., Course 1: 65% existing / 35% new), but the "existing" materials are academic slides, notes, and full-text journal articles that require significant practitioner translation.

**Examples:**
- Course 1 references "Selection W11 (Campion's 15 components)" — the source material exists but must be stripped of academic citation format, reframed for practitioners, combined with video scripts, templates, and self-assessment exercises
- Course 5 (AI-Powered HR) references "PM Assignments 4-5 (Python)" — these exist as academic assignment prompts but need video walkthroughs, simplified explanations, and real HR datasets

**Impact:**
- The "65% existing" metric is misleading: existing materials require 40-60% effort to transform into commercial content
- Without disciplined adherence to content adaptation rules and voice guidelines, modules will read as direct academic conversions rather than Teresa Ristow's voice
- High risk of Humanizer2-phase failures (AI-generated-sounding content that violates voice guidelines)

**Fix Approach:**
1. Create a "content adaptation template" in `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/CLAUDE.md` showing the workflow:
   - Identify source material (e.g., "PM W8 Slides on 360-degree feedback")
   - Extract key findings and frameworks
   - Identify practitioner bridge points (what does this mean for someone implementing 360?)
   - Draft module script using Brand Voice and Tone guide
   - Create downloadable template
   - Pass through Humanizer2
   - Review against content adaptation rules
2. Build a reusable "source material assessment checklist" to evaluate how much adaptation effort a given source actually requires before committing to effort estimates

---

## Voice & Tone Compliance Readiness

### Brand Voice and Tone Guide Is Comprehensive But Untested (PROCESS RISK)

**Issue:** `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/00-Voice and Tone/Brand Voice and Tone.md` is a detailed 340-line guide covering Teresa Ristow's voice patterns, but it has never been tested against actual module scripts (because none exist yet).

**Files:**
- `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/00-Voice and Tone/Brand Voice and Tone.md` (comprehensive)
- `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/00-Voice and Tone/CLAUDE.md` (implementation instructions)

**Risk:**
- When first module scripts are written, voice compliance may fail because the guide's prescriptions are too abstract or incomplete
- Agents may struggle to balance the five voice traits (evidence-anchored, progressive, precise, framework-oriented, practitioner-bridging) in live writing
- No test cases or example module scripts show what compliant content looks like at 15-minute video script length

**Fix Approach:**
1. Create sample module scripts for early courses (1-2) before full-scale production
2. Have these samples reviewed against both `Brand Voice and Tone.md` and `content_adaptation_rules` to identify gaps in guidance
3. Update the guide with concrete "before/after" examples showing non-compliant vs. compliant phrasing
4. Build voice-compliance examples into the CLAUDE.md instructions (e.g., "Module scripts should follow the structure shown in [example file]")

---

## Testing & Assessment Content Gaps

### No Assessment Questions or Knowledge Checks Drafted (DELIVERY GAP)

**Issue:** Course overviews mention "assessment questions," "self-assessments," and "knowledge checks," but none exist.

**Examples:**
- Course 1 overview (line 37): "Each module: 15-min video lesson + downloadable template + short quiz" — no quiz exists
- Course 2 overview: No mention of specific assessment strategy
- Online Courses CLAUDE.md (line 3): "Assessment questions and answer explanations" are in scope for course content

**Impact:**
- Cannot determine instructional design approach (formative vs. summative? auto-graded vs. practitioner-judged?)
- Unknown how quizzes will integrate with Kajabi platform
- Missing content for ~10% of total course delivery effort per module

**Fix Approach:**
1. In each course overview's "MVP Deliverables," add explicit assessment requirements
   - E.g., "Module 1 quiz: 5 scenario-based questions assessing understanding of structured interview components"
2. Create a Kajabi-specific assessment template (suggest: `.planning/templates/assessment_template.md`) showing question types, answer key format, grading rubrics
3. Reference this template in Online Courses CLAUDE.md as a requirement for module completeness

---

## Kajabi Platform Integration Unknowns

### No Documentation on Kajabi-Specific Constraints or Best Practices (BLOCKING)

**Issue:** Courses are being designed for "Kajabi platform" but no Kajabi-specific guidance exists (module length, file format requirements, video embedding format, interactive element support, etc.).

**Impact:**
- Agents writing module scripts may not know Kajabi's 15-minute recommendation
- Unknown if templates should be PDFs, embedded interactive worksheets, or downloadable Excel files
- Video scripts may not match Kajabi's platform constraints (aspect ratio, duration, interactivity features)

**Fix Approach:**
1. Create `/Users/Christopher/Documents/GitHub/SOUP/Online Courses/.planning/kajabi_platform_guide.md` documenting:
   - Module structure and length constraints
   - Video format and embedding specifications
   - Template/downloadable file format requirements
   - Assignment/quiz integration approach
   - Email sequence and sales page specifications
2. Reference this guide in Online Courses CLAUDE.md as a required reading before content creation

---

## Missing Foundational Documentation

### No Course Readiness Checklist or Delivery Standards (PROCESS GAP)

**Issue:** No definition of "ready to launch" exists. What makes a course complete?

**Missing Specifications:**
- How many modules = 1 course? (Overviews specify MVP ranges: 4-8 modules)
- Is a course "done" with just module scripts, or does it require video recordings, quizzes, community setup, email sequences, sales pages?
- What is the definition of "self-paced" vs. "cohort-based"? (Courses 1-5 are self-paced; Course 6 is cohort-based, but what does that mean structurally?)

**Impact:**
- No clear end state; risk of perpetual incomplete work
- Different courses may have vastly different content completeness standards

**Fix Approach:**
1. Create `/Users/Christopher/Documents/GitHub/SOUP/.planning/course_delivery_standards.md` defining:
   - MVP Delivery Checklist (what's required for minimum launch)
   - Premium Delivery Checklist (what adds value, optional)
   - Quality gates (voice compliance, Humanizer2, technical testing)
   - Platform-ready checklist (Kajabi integration specifics)
2. Include in Online Courses CLAUDE.md with priority clarity

---

## Phase 2-3 Course Risk Summary

**High Risk Courses (Require Earliest Clarity):**
- **Course 5 (AI-Powered HR):** 55% new creation needed, premium pricing ($497-797), IP licensing risk (AIRA Framework), code notebook complexity
- **Course 6 (Data-Driven DEI):** 60% new creation needed, premium pricing ($497-997), cohort-based complexity, IP licensing risk
- **Course 8-10 (Job Seeker Vertical):** Entirely new perspective (candidate-side), heavy dissertation dependence, 40-60% new creation each

**Recommendation:** Courses 1-2 should be fully drafted and launched before phase 2 work begins. Phase 2 should not start until path issues (CLAUDE.md, Kajabi integration) and delivery standards are clarified.

---

*Concerns audit: 2026-04-13*

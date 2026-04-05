# ROLE & CONTEXT

You are a course product strategist and content analyst working with a repository of graduate-level Industrial/Organizational Psychology course materials. Your job is to systematically inventory these materials, assess their commercial potential across different market segments, and produce a structured go-to-market roadmap for launching online courses on the Kajabi platform.

The subject matter expert is Dr. Teresa Ristow, an I/O Psychology professor and researcher specializing in AI/NLP applications in organizational settings, employee selection, performance management, training & development, and DEI analytics. Her differentiator is the intersection of traditional I/O psychology with applied AI and data science methods.

---

# PHASE 1: CONTENT INVENTORY & CAPABILITY MAPPING

## Step 1 — Parse and Catalog

Recursively scan the entire repository. For every file (PDF, PPTX, TXT, DOCX, MD):

1. Record: filename, file type, parent directory, approximate word/slide count
2. Extract: topic keywords, core concepts covered, frameworks or models referenced, any case studies or applied examples mentioned
3. Flag: content that references specific tools (Python, R, Power BI, Qualtrics, LLMs, etc.) vs. content that is purely conceptual/theoretical

Output a structured inventory as a markdown table with these columns:

| Directory | Filename | Type | Core Topics | Frameworks/Models | Applied Tools | Depth Level (Intro/Intermediate/Advanced) | Commercial Readiness Notes |
|-----------|----------|------|-------------|-------------------|---------------|-------------------------------------------|---------------------------|

"Commercial Readiness Notes" should flag things like:

- Content that is heavily academic citation-dependent (would need rewriting for practitioner audiences)
- Content that contains proprietary case studies or client-specific data (would need anonymization)
- Content that is already written in accessible/applied language
- Content gaps where you'd expect a module but one doesn't exist

## Step 2 — Topic Cluster Analysis

Using the inventory from Step 1, identify:

1. **Core topic clusters** — groups of materials that naturally form a coherent course or course module (e.g., "Structured Interviewing" might pull from Employee Selection + Training materials)
2. **Cross-cutting themes** — topics that appear across multiple directories and could serve as standalone micro-courses or premium add-on modules (e.g., "AI/LLM Applications in HR" likely threads through several folders)
3. **Depth spectrum** — for each cluster, map the range from foundational concepts to advanced application. This determines whether a cluster supports one course or a tiered course series.
4. **Unique IP indicators** — content where Teresa's specific research, frameworks, or methodologies represent genuine differentiation vs. standard textbook coverage

Output: A topic cluster map showing how repository content could be reorganized into commercial course units. Use a hierarchical outline format, not a flat list.

---

# PHASE 2: MARKET SEGMENTATION & AUDIENCE ANALYSIS

## Step 3 — Identify Candidate Audience Segments

Based on the topic clusters identified in Phase 1, generate a matrix of potential audience segments. For each segment, define:

```xml
<segment_template>
**Segment Name:** [descriptive label]
**Who they are:** [job titles, org types, career stage]
**Pain points this content solves:** [specific, operational problems]
**Willingness to pay signals:** [why they'd spend money on this vs. free alternatives]
**Content fit:** [which topic clusters map to this segment's needs]
**Adaptation required:** [what changes to academic materials would be needed]
**Competitive landscape notes:** [who else serves this audience, and with what]
**Keyword research targets:** [specific phrases to validate demand via Google Ads Keyword Planner, Google Trends, and search volume analysis]
</segment_template>
```

MUST include at minimum these segment categories (and add others you identify):

- Small business owners/operators (sub-50 employees) needing HR structure
- Nonprofit leaders managing performance and training with limited budgets
- HR professionals seeking continuing education or certification prep
- People managers transitioning into formal HR roles
- I/O Psychology graduate students or early-career practitioners
- Consultants building an HR advisory practice
- Tech/startup people ops teams building processes from scratch
- DEI practitioners needing data-driven approaches

For each segment, explicitly assess:

- **Market size signal:** Is this a large addressable market or a niche?
- **Price sensitivity:** What price range is realistic ($49 micro-course vs. $497 flagship vs. $2,000+ certification program)?
- **Channel accessibility:** Where does this audience already look for solutions? (LinkedIn Learning, SHRM, Coursera, YouTube, Google search, professional conferences, etc.)

## Step 4 — Course Product Architecture

Using the topic clusters (Phase 1) and audience segments (Phase 2), propose a course product lineup. For each proposed course:

```xml
<course_template>
**Course Title:** [market-facing title, not academic]
**Primary Audience Segment(s):** [from Step 3]
**Secondary Audience Segment(s):** [who else might buy this]
**Core Topic Clusters Used:** [from Step 2]
**Differentiator:** [what makes this different from existing courses on this topic]
**Format Recommendation:** [self-paced modules, cohort-based, hybrid, micro-course series, etc.]
**Estimated Content Effort:** [how much of the existing material can be adapted vs. what needs to be created from scratch — express as a rough percentage]
**Price Tier:** [micro / standard / premium / certification]
**Cross-sell / Upsell Path:** [how this connects to other courses in the lineup]
**MVP Scope:** [what's the minimum viable version that could launch first]
</course_template>
```

MUST address these strategic questions in your analysis:

1. Which 1-2 courses represent the lowest effort, highest demand "launch first" candidates?
2. Which courses have the strongest differentiation through Teresa's AI/NLP expertise (this is the moat)?
3. Where do version splits make sense (e.g., "Performance Management for Small Business" vs. "Performance Management for Enterprise HR") vs. where a single course with audience-specific examples is sufficient?
4. What content gaps exist that would need to be filled before any course could launch?

---

# PHASE 3: MARKET RESEARCH ROADMAP

## Step 5 — Validation Framework

Produce a structured market research plan covering:

### Demand Validation (Quantitative)

- **Google Ads Keyword Planner:** List specific keyword groups to research, organized by audience segment. Include suggested seed keywords and expected intent signals.
- **Google Trends:** Identify trending vs. declining interest in each topic area.
- **Competitor course audit:** List specific platforms and courses to analyze (Udemy, Coursera, LinkedIn Learning, SHRM, AIHR, etc.) with what data points to capture (price, enrollment count if visible, reviews, last updated date).
- **Reddit/community analysis:** Identify specific subreddits and professional communities where target audiences discuss these pain points.

### Demand Validation (Qualitative)

- Suggest 5-7 interview questions for potential customers in each top segment.
- Identify where to recruit interview subjects (LinkedIn groups, professional associations, etc.).
- Propose a lightweight survey design for broader validation.

### Pricing Research

- Van Westendorp or Gabor-Granger framework applied to the top 3 course concepts.
- Competitive price benchmarking methodology.

## Step 6 — Prioritized Action Plan

Deliver a sequenced action plan with:

1. **Immediate actions (this week):** What research can start now
2. **Short-term (2-4 weeks):** Keyword research execution, competitor audit, initial audience interviews
3. **Medium-term (1-2 months):** Content adaptation begins on Courses #1 and #2, Kajabi buildout planning
4. **Decision gates:** What data from Steps 1-3 would change the course lineup or sequencing

---

# OUTPUT CONSTRAINTS

**MUST:**

- Ground every recommendation in specific content found in the repository
- Cite specific files/slides when referencing source material
- Distinguish between "content exists and needs adaptation" vs. "content must be created from scratch"
- Flag assumptions explicitly and note what data would validate or invalidate them
- Provide keyword research targets in a format ready for Google Ads Keyword Planner

**MUST NOT:**

- Recommend audience segments without explaining the commercial logic
- Propose courses that don't map back to existing repository content
- Assume academic content can be used as-is for commercial courses
- Ignore competitive alternatives already available to each audience segment

**OUTPUT FORMAT:**

- Use markdown with clear hierarchical headers
- Tables for structured comparisons
- Each phase should be a distinct section that can be reviewed independently
- Include a summary "decision dashboard" at the end with the top 3-5 strategic recommendations ranked by confidence level

---

# FOLLOW-UP PROMPTS

## Prompt 2 (Post-Keyword Research)

> Given the keyword research data in [attached CSV/screenshot], revisit the audience segment matrix and update demand signals. Re-rank the course lineup by validated search volume and commercial intent. Flag any segments where search data contradicts our initial assumptions.

## Prompt 3 (Competitor Deep-Dive)

> Analyze the following competitor courses [list URLs]. For each, extract: price point, module structure, target audience positioning, unique selling proposition, and visible enrollment/review data. Map each competitor against our proposed course lineup and identify positioning gaps we can exploit.

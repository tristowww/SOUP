# Voice & Tone Agent Instructions

Any agent working in the `Online Courses/` directory tree is generating, reviewing, or adapting content that represents Dr. Teresa Ristow's expertise and intellectual voice. This directory is the single source of truth for how that voice is expressed across all ten courses.

**Before generating any course content, read `Brand Voice and Tone.md` in this directory.** The rules in that document are requirements, not suggestions.

---

## Scope

This guide governs all content produced for the Kajabi course platform under Teresa Ristow's name, including:

- Module scripts and lesson content
- Assessment questions and answer explanations
- Practitioner summaries and research syntheses
- Templates, checklists, and tool descriptions
- Course descriptions, sales pages, and email sequences
- Video script outlines and talking points
- Community posts and student-facing communication

Internal/structural outputs (file listings, status updates, CLAUDE.md edits, data tables) are exempt.

---

## Priority Chain

When voice and tone guidance conflicts with other instructions:

1. **This directory's `Brand Voice and Tone.md`** governs Teresa's intellectual voice and writing patterns
2. **Root `SOUP/CLAUDE.md`** governs content adaptation rules (academic-to-practitioner conversion, language substitutions, Kajabi constraints)
3. **`Online Courses/CLAUDE.md`** governs course structure, launch sequencing, and directory conventions

Voice and tone take priority over generic adaptation rules. If the root CLAUDE.md says "use active voice, second person, imperative mood" but the voice guide specifies a pattern that uses first-person plural for a particular context, follow the voice guide.

---

## Quick Reference: Non-Negotiable Voice Rules

These are the highest-priority constraints. Violating any one of these produces copy that does not sound like Teresa:

1. **Every substantive claim must be evidence-anchored.** Name the theory, cite the finding, or reference the data. "Research shows" is not enough; say what the research actually found.
2. **Build concepts progressively.** Define before you apply. Contextualize before you extend. Never drop a conclusion without scaffolding.
3. **Quantify over qualify.** "48%-90% detection accuracy" beats "strong detection capability." Exact numbers, sample sizes, effect sizes when available.
4. **Name the theory.** Teresa grounds her arguments in named psychological theories (Self-Determination Theory, Optimal Distinctiveness Theory, Person-Environment Fit). She does this even in practitioner content. Adapt the depth, but keep the anchor.
5. **Connect every concept to practice.** Every theoretical point must resolve to "what this means for your organization" or "how you can use this." Teresa is not a pure theorist; she is an applied scientist.
6. **Do not oversimplify.** Acknowledge nuance and limitations. If the research is mixed, say so. If a tool has tradeoffs, name them. Teresa pushes back on reductive advice.
7. **No hype, no fluff, no filler.** See the full prohibited patterns list in `Brand Voice and Tone.md`.

---

## Content Review Checklist

Before delivering any course content, verify:

- [ ] Claims are evidence-anchored (theory named or finding cited)
- [ ] Concepts build progressively (define → contextualize → evidence → apply)
- [ ] Numbers are precise, not vague ("6.3% of interviewers" not "a significant portion")
- [ ] Every theoretical point connects to a practitioner action or implication
- [ ] Limitations and nuance are acknowledged, not hidden
- [ ] Tone is measured confidence: authoritative without being dismissive, accessible without being dumbed down
- [ ] No prohibited patterns (see `Brand Voice and Tone.md`)
- [ ] Humanizer 2 pass completed (per root CLAUDE.md requirement)

---

## Humanizer 2 Requirement

All generated content intended as human-readable or final-draft output must be run through `/humanizer2` before delivery. This is inherited from the root `SOUP/CLAUDE.md`. Run Humanizer 2 as the final pass after all voice and tone compliance checks are complete.

---

## Reference Documents

- **`Brand Voice and Tone.md`** (this directory): Full voice analysis, tone spectrum, sentence-level patterns, and prohibited language. Read first, always.
- **`Publications/`** (parent repository): Teresa's original research. Reference for verifying voice authenticity and sourcing unique IP.
- **`COURSE_STRATEGY_DELIVERABLE.md`** (repository root): Audience segments, pricing, differentiation. Reference for audience-appropriate tone calibration.

# SOUP — I/O Psychology Course Conversion

## What This Is

A content repository that converts Dr. Teresa Ristow's graduate-level Industrial/Organizational Psychology course materials into ten commercial online courses for the Kajabi platform. Audience spans employer-side HR/L&D professionals and job seekers. The competitive moat is the intersection of traditional I/O psychology with applied AI, NLP, and data science.

## Core Value

Translate rigorous academic I/O psychology into practitioner-ready, evidence-anchored course modules that preserve research nuance while delivering actionable templates, checklists, and tools to paying customers.

## Requirements

### Validated

- ✓ Academic source materials organized under `Reference Materials/` (414+ files across Employee Selection, Performance Mgmt, Employee Training, Organizational Psych, Publications, Social Psych) — existing
- ✓ Ten-course commercial lineup scaffolded under `Online Courses/Course 1-10/` with per-course CLAUDE.md routing — existing
- ✓ Voice and tone foundation under `Online Courses/00-Voice and Tone/` — existing
- ✓ Course strategy baseline (`COURSE_STRATEGY_DELIVERABLE.md`, `COURSE_STRATEGY_DASHBOARD.html`) — existing
- ✓ Content adaptation rules and humanizer2 gate defined in root `CLAUDE.md` — existing

### Active

- [ ] LearnDash content pipeline built and proven end-to-end via Course 1 import (milestone 1.0)
- [ ] Production LearnDash host chosen + license activated (decision expected during Phase 1 planning)
- [ ] Mu-plugin shipped: disables `wpautop` + `wptexturize` on `sfwd-lessons` (from spike 001 findings)
- [ ] Roadmap reflects the priority tiers from `COURSE_STRATEGY_DELIVERABLE.md` so future `/gsd-plan-phase` calls have the right sequencing — see `ROADMAP.md`

### Validated (added 2026-04-18)

- ✓ Platform evaluated across nine options (`Online Courses/PLATFORM_API_COMPARISON.md`). LearnDash won on raw HTML support, lowest cost per seat, and native WP REST API maturity. Tradeoff: we operate WordPress.
- ✓ WP REST API preserves raw HTML + `<style>` blocks byte-for-byte for authenticated admins (spike 001). Two cosmetic filters (`wpautop`, `wptexturize`) need disabling via mu-plugin.
- ✓ Application Passwords are durable under bulk load; no rate-limiting observed (spike 003-lite). Production latency still needs measuring on real host.

### Out of Scope

- Course template/module format design — deferred; user explicitly scoped this initialization to planning scaffolding only, not course production infrastructure
- Content conversion pipeline definition (voice gates, humanizer workflow as a reusable process) — deferred; tracked separately if/when it becomes a phase
- Any actual course module drafting — future phase work, not initialization
- Front-end / Kajabi theme development — Kajabi is the publishing platform, not a dev target for this repo
- Cross-repo work with `loom-repo/` or `loom.coffee/` — this project is scoped to SOUP only

## Context

- **Subject matter expert:** Dr. Teresa Ristow (Virginia Tech PhD, I/O Psychology). Unique IP includes the AIRA framework (OUP chapter, forthcoming), dissertation LPA+NLP work on deception in job ads, curbstoning detection, VOIS methodology, and Python-integrated HR analytics assignments.
- **Source content:** ~414 markdown files, originally graduate coursework (PSYC 650/652/654/656/343). Each academic course has syllabi, weekly slides (`Week N slides.md` + annotated `Week N slides_me.md`), articles (`Author et al. (Year).md`), assignments with answer keys, and notes.
- **Target platform:** LearnDash on self-hosted WordPress (flipped from Kajabi 2026-04-18 — see Key Decisions). Module length target 15-20 min. Practitioner audience, not students.
- **Ten commercial courses (see `COURSE_STRATEGY_DELIVERABLE.md`):**
  - Employer-side vertical (Courses 1-7): Structured Hiring, Performance Management, Training That Transfers, Leadership Development, AI-Powered HR (flagship), Data-Driven DEI, Workplace Psychology Essentials (gateway)
  - Job-seeker vertical (Courses 8-10): Science of Getting Hired, Choose Wisely, Hiring Insider's Toolkit
- **Launch waves:**
  - Wave 1 (Launch first): Courses 1, 2
  - Wave 2 (Phase 2): Courses 3, 4, 5, 6, 7
  - Wave 3 (Phase 3): Courses 8, 9, 10
- **Existing guardrails:** Root `CLAUDE.md` defines content adaptation rules, voice constraints (no em-dashes, no banned language, specific subscription and tasting-note rules inherited from loom-repo), and a mandatory humanizer2 pass for all reader-facing prose.
- **Codebase map:** `.planning/codebase/` (7 docs, mapped 2026-04-13). CONCERNS.md flagged that root-level `Employee Selection Materials/`, `Performance Mgmt Materials/`, etc. directories referenced in root `CLAUDE.md` are not present in the filesystem — actual source materials live under `Online Courses/Reference Materials/`. CLAUDE.md should be reconciled with reality at some point.

## Constraints

- **Scope:** Planning scaffolding only. This initialization does not build course content, templates, or pipelines. Those are future phase work.
- **Voice:** All customer-facing prose must pass humanizer2 and comply with `Online Courses/00-Voice and Tone/` plus root `CLAUDE.md` banned-language rules.
- **IP:** No verbatim reuse of copyrighted academic article text. Summarize and cite.
- **Evidence integrity:** "Evidence shows" language requires actual research backing. No fabricated stats. Research nuance must survive simplification.
- **Accreditation:** No claims of certification or CE credit without proper accreditation.
- **Authorship:** Teresa is the subject matter expert and credentialed author. Her unique IP (AIRA, dissertation, curbstoning, VOIS) is the differentiator.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Scope this initialization to GSD planning scaffolding only | User explicitly chose option 1 — no course templates, no pipeline definition. Keeps PROJECT.md honest about what's actually being set up. | — Pending |
| Roadmap structure: course-per-phase, 10 phases total | User explicitly chose option 1. Mirrors the ten-course commercial lineup; each phase is a self-contained course build when work starts. | — Pending |
| Phase sequencing follows `COURSE_STRATEGY_DELIVERABLE.md` launch waves | The strategy doc already prioritized Courses 1-2 (Launch first), 3-7 (Phase 2), 8-10 (Phase 3). No reason to re-litigate. | — Pending |
| Actual source materials path is `Online Courses/Reference Materials/`, not the root-level dirs in `CLAUDE.md` | Codebase map verified filesystem state. Root CLAUDE.md is out of date. | ⚠️ Revisit — reconcile CLAUDE.md when convenient |
| **Platform flip: Kajabi → LearnDash on self-hosted WordPress (2026-04-18)** | Nine-platform comparison (`Online Courses/PLATFORM_API_COMPARISON.md`) found Kajabi's API route content through a block editor that partially sanitizes custom HTML, and Pro-tier pricing is $399-499/mo. LearnDash stores raw HTML unchanged (spike 001 confirmed byte-for-byte round-trip), costs ~$199/yr for the license + $10-30/mo hosting, and its WP REST API is mature and widely documented. Cost of ownership tradeoff: we operate WordPress (updates, backups, security). | ✓ Decided — Phase 1 builds the LearnDash pipeline |
| **Roadmap structure revised: pipeline-first, not course-first** | Original plan had Course 1 as Phase 1. Revised to Phase 1 = LearnDash pipeline infrastructure, Phase 2 = Course 1 import as pipeline validation. Rationale: any of the 10 courses will be blocked without the pipeline; building it once up front means every subsequent course is a straight authoring task. | ✓ Decided — see `ROADMAP.md` |
| **Milestone 1.0 scoped to pipeline + one proof-of-concept course** | Shipping the pipeline alone is insufficient validation — the bugs that matter only appear under real authoring load. Including Course 1 inside 1.0 forces the pipeline to prove itself before we commit to scale. | ✓ Decided |
| **Host: WordPress.com Business plan (~$25/mo annual). No local staging. (2026-04-18)** | WordPress.com Business is the minimum WP.com tier that allows third-party plugins (needed for LearnDash). Managed hosting removes server/backup/SSL overhead. InstaWP and Local by Flywheel rejected as unnecessary intermediate layers — InstaWP is just a WP host with extra UX, and local staging duplicates what the draft-review workflow on production already provides. Total cost: ~$25 hosting + ~$17/mo amortized LearnDash = ~$42/mo. | ✓ Decided |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `/gsd-transition`):
1. Requirements invalidated? → Move to Out of Scope with reason
2. Requirements validated? → Move to Validated with phase reference
3. New requirements emerged? → Add to Active
4. Decisions to log? → Add to Key Decisions
5. "What This Is" still accurate? → Update if drifted

**After each milestone** (via `/gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check — still the right priority?
3. Audit Out of Scope — reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-04-13 after initialization*

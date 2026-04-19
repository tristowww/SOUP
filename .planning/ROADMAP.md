# SOUP Roadmap

**Last updated:** 2026-04-18
**Current milestone:** 1.0 — Pipeline Foundation
**Current phase:** 1 — LearnDash Content Pipeline (pending plan)

---

## How this roadmap works

Phases are ordered by dependency, not priority. Each phase is a self-contained unit of work that can be planned (`/gsd-plan-phase`) and executed (`/gsd-execute-phase`). Milestones group phases by release scope — milestone 1.0 ships when all its phases are verified complete.

When the shape of an unstarted phase changes materially, update it here rather than building around a stale plan. When a phase splits, insert a decimal (e.g., `72.1`) via `/gsd-insert-phase`.

---

## Milestone 1.0 — Pipeline Foundation

**Goal:** A CLI-driven pipeline that publishes SOUP's markdown course content to a LearnDash host, proven end-to-end by authoring and shipping the first course (Course 1: Structured Hiring That Works).

**Success criteria:**
- Running the CLI against `Online Courses/Course 1 - Structured Hiring That Works/` produces a fully structured LearnDash course on the target host with all lessons and topics, with HTML + custom CSS rendering faithfully in the student view.
- A content author (Teresa or Christopher) can edit a markdown file locally, run one command, and see the change on the LearnDash site within minutes.
- The pipeline is documented enough that a second contributor could use it without the original author present.

**Platform decision inheriting into this milestone:** LearnDash on self-hosted WordPress (supersedes the original Kajabi target — see `PROJECT.md` Key Decisions).

### Phases

| # | Phase | Status | Depends on | One-line goal |
|---|-------|--------|------------|---------------|
| 1 | LearnDash Content Pipeline | PENDING PLAN | — | Build the CLI + mu-plugin + authoring conventions that turn markdown into LearnDash lessons via REST |
| 2 | Course 1 Import (Structured Hiring) | FUTURE | Phase 1 | Author Course 1 in markdown + custom CSS, run it through the pipeline, validate rendered output on live host |

### Gate before closing milestone 1.0

- Spike 002 (course/lesson/topic hierarchy API with real LearnDash) must have been run and passed — this remains deferred pending LearnDash license purchase, and should be folded into Phase 1's plan rather than kept as a standalone spike.
- **Host:** WordPress.com Business plan (~$25/mo annual) + LearnDash license (~$199/yr). Decided 2026-04-18 — InstaWP and Local by Flywheel rejected as unnecessary intermediate layers. No local staging; draft-review workflow on production is sufficient.
- Mu-plugin (`remove_filter('the_content', 'wpautop')` + `wptexturize` on `sfwd-lessons` post type) shipped and verified on the production host.

---

## Phase 1 — LearnDash Content Pipeline

**Status:** Pending plan (next step: `/gsd-plan-phase 1`)

**Goal:** Ship a repeatable, CLI-driven pipeline that converts markdown course content in the SOUP repo into LearnDash lessons on a chosen host, with HTML and custom CSS rendering faithfully.

**Scope (tentative — plan phase will refine):**

- **Authoring conventions**
  - Directory layout per course: `Course N - Title/Module M/Lesson L.md` (or similar; confirm during plan)
  - YAML frontmatter for lesson metadata (title, order, custom CSS file, draft/published)
  - Shared CSS tokens and component classes (`.soup-callout`, `.soup-table`, `.soup-objectives`, `.soup-code`) centralized under `Online Courses/00-Voice and Tone/pipeline-css/`

- **Pipeline (CLI tool)**
  - Python package under `pipeline/` (or TBD during plan)
  - Markdown → HTML via `markdown-it-py` or `pandoc`, with custom CSS injected as inline `<style>` block
  - REST push to `/wp-json/wp/v2/sfwd-lessons` (and `sfwd-courses`, `sfwd-topic`) with Application Password Basic Auth
  - Idempotent: detects existing lessons by a frontmatter `slug` field, updates instead of duplicating
  - Supports dry-run mode (prints what would be pushed without hitting the API)
  - Exponential-backoff retry on transient failures (timeouts, 5xx)

- **LearnDash host setup**
  - Production host chosen and LearnDash license activated
  - Mu-plugin installed: disables `wpautop` + `wptexturize` on `sfwd-lessons`, extracts Basic Auth from `HTTP_AUTHORIZATION` if needed, allows Application Passwords on HTTP when environment type is `local` (for staging)
  - Service account created with Application Password scoped for the pipeline

- **Validation**
  - Spike 002 folded in: real LearnDash exercised for course/lesson/topic hierarchy via `ldlms/v2` endpoints with parent linkage confirmed
  - Smoke test: push one lesson, verify admin + student view render identically to source
  - Re-run `bulk_push.py` harness (from spike 003) against production host to get realistic latency numbers
  - Content-adaptation humanizer2 gate remains — pipeline must not bypass it for customer-facing prose

- **Developer experience**
  - `README.md` under `pipeline/` explaining setup, secrets management, run commands
  - Secrets (host URL, app password) via env vars or `.env` (gitignored); never committed
  - One-command "refresh course N" and "refresh single lesson" modes

**Dependencies on prior work:**
- Spike 001 (HTML fidelity) — ✓ PARTIAL/validated
- Spike 003-lite (bulk push) — ✓ PARTIAL/validated (auth durability confirmed; real perf TBD)
- Spike 002 (hierarchy API) — DEFERRED; folded into this phase's plan

**Open questions for the plan phase:**
- Python vs. TypeScript for the CLI? (Python leans toward SOUP's existing data-science orientation; TS gets faster bootstrap via `wpapi` npm package.)
- Do we build a frontmatter schema now, or start with directory-convention-only and add YAML later?
- How do custom per-course CSS themes get stored — per-course folder or shared library with overrides?
- Does the pipeline publish as draft or published? (Probably draft, with a separate "promote to published" command.)

---

## Phase 2 — Course 1 Import: Structured Hiring That Works

**Status:** Future (gated on Phase 1 completion)

**Goal:** Author the first full course in markdown + custom CSS using Phase 1's pipeline, push it to the LearnDash host, and validate end-to-end that a student can enroll and consume the course.

**Why this phase exists:** Proves the pipeline is actually usable, not just technically functional. The bugs that surface when you're trying to author real content (missing frontmatter fields, CSS conflicts, slug collisions, draft-vs-publish workflow gaps) only appear under production use. Keeping this inside milestone 1.0 ensures Phase 1 doesn't ship a half-finished tool.

**Scope (tentative):**
- Course structure derived from `Online Courses/Course 1 - Structured Hiring That Works/` (modules, lessons, topics per the course strategy)
- All lessons written in markdown with SOUP voice conventions applied
- Assessments and downloadable templates attached (LearnDash quiz API + media upload)
- Humanizer2 pass on all customer-facing prose
- Teresa does a full review on the live LearnDash site before sign-off

---

## Future Milestones (outline — not committed)

### Milestone 2.0 — Wave 1 Launch
Phase 3: Course 2 Import (Performance Management That Actually Works) + sales page + enrollment flow. Marks the first paying-customer launch.

### Milestone 3.0 — Wave 2 Expansion
Courses 3-7: Training That Transfers, Leadership Development by Design, AI-Powered HR (flagship), Data-Driven DEI, Workplace Psychology Essentials (gateway). Five phases. May split based on production capacity.

### Milestone 4.0 — Wave 3 (Job-Seeker Vertical)
Courses 8-10: Science of Getting Hired, Choose Wisely, Hiring Insider's Toolkit. Separate vertical — different sales pages, bundle strategy (Courses 8+9), B2B path for Course 10.

### Milestone 5.0+ — Backlog
- Lifetime content updates / versioning strategy
- Analytics dashboard (Kajabi-style metrics on self-hosted LearnDash)
- Affiliate program infrastructure
- University career center B2B licensing workflow (Course 10 spinoff)

---

## Change log

- **2026-04-18** — Roadmap created. Milestone 1.0 defined with Phase 1 (pipeline) + Phase 2 (Course 1 import) based on spike 001 + spike 003-lite findings. Platform flipped from Kajabi to LearnDash.
- **2026-04-18** — Host decided: WordPress.com Business plan. InstaWP and Local by Flywheel rejected as unnecessary intermediate layers. Draft-review on production replaces local staging.

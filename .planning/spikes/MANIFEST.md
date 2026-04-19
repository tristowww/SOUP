# Spike Manifest

## Idea

Validate LearnDash (self-hosted WordPress + LearnDash LMS plugin) as the backend for a CLI-driven course content pipeline for SOUP. Author courses in markdown, convert to HTML + custom CSS locally, and push via REST API. Before committing to build the pipeline, we need proof that (1) WP's content handling doesn't sanitize or mangle our HTML, (2) the LearnDash course/lesson/topic hierarchy is programmable via REST, and (3) bulk pushes are viable under real auth and rate limits. Prior platform comparison: `Online Courses/PLATFORM_API_COMPARISON.md`.

## Spikes

| # | Name | Validates | Verdict | Tags |
|---|------|-----------|---------|------|
| 001 | html-fidelity-minimal | WP REST API accepts raw HTML with `<style>` and renders faithfully in the student view, unsanitized | PARTIAL ⚠ | learndash, wordpress, rest-api, html, kill-switch |
| 002 | course-hierarchy-api | Course → Lesson → Topic hierarchy is creatable via `ldlms/v2` REST endpoints with correct parent linkage | PENDING | learndash, rest-api, hierarchy |
| 003 | bulk-push-auth-perf | Batch-pushing 10 markdown-authored lessons via Application Passwords lands cleanly within rate limits at usable throughput | PENDING | learndash, auth, rate-limits, performance |

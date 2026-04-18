# Course Platform API Comparison

**Date:** 2026-04-18
**Context:** Evaluating course hosting platforms for Dr. Teresa Ristow's commercial I/O Psychology course line (SOUP). Goal: build a CLI-driven content pipeline (`markdown → processed HTML → platform via API`) to accelerate authoring of ~10 courses.

## Evaluation Criteria

1. **Public API exists** and is documented (not partner-only gated)
2. **Write access to course content** — create courses, modules/sections, lessons via API
3. **Raw HTML/CSS support** in lesson bodies — can we POST an HTML blob and have it render, including custom CSS?
4. **Pricing tier required for API access** (many platforms gate this behind top-tier plans)
5. **Rate limits** and bulk-operation friendliness
6. **Auth model**

## Comparison Table

| Platform | Public API | Create courses / modules / lessons | Raw HTML support | Plan required for API | Price at API tier (monthly) | Rate limits | Notes |
|---|---|---|---|---|---|---|---|
| **Kajabi** | Yes (launched Sep 16, 2025; v1 at `api.kajabi.com/v1`) | Yes — OpenAPI spec + Postman published at developers.kajabi.com | Partial — Kajabi posts historically accept HTML, but content flows through their block editor; custom CSS typically scoped to theme, not per-lesson | Included in new Pro Plan; $25/mo add-on for Basic/Growth | **$399/mo (Pro, annual) or $499/mo monthly**; or lower plan + **$25** add-on | Not published in help docs; see OpenAPI spec | Brand new. Capabilities still maturing — verify specific course/lesson write endpoints against the llms.txt index before committing |
| **Thinkific** | Yes (mature, documented) | Yes — Courses, Chapters, Lessons (classic builder only) | Yes — Text Lessons accept styled HTML bodies | **Grow** plan | **$199/mo** (Grow); Expand $499; Plus custom | Documented tier-based limits (separate rate-limits page) | **CRITICAL:** New Course Builder (default for sites created after Jan 28, 2026) is excluded from most REST endpoints. Must opt into classic builder for programmatic creation |
| **Teachable** | Yes (historically limited, read-heavy) | Limited write — sections/lessons creation is thin; largely enrollment/user focused | Minimal — forced through block editor, HTML sanitized | **Growth** plan | **$139/mo** (annual) / $199 (monthly) | 10,000 requests/month hard cap | Request ceiling is low for a bulk backfill. Feasible for per-lesson drips, painful for mass publishes |
| **LearnWorlds** | Yes — RESTful, Stoplight docs, 15+ categories, 26 new endpoints as of Feb 2026 | Yes — courses, sections, learning activities | Yes — activity bodies accept HTML | **Learning Center** tier and up for extended API/Webhooks | Learning Center starts ~$299/mo; enterprise tiers custom | Not publicly specified; enterprise-friendly | Most "serious" API of the hosted platforms; best fit when you want both programmatic control and a polished student UX |
| **Podia** | **No public API** | N/A | N/A | N/A | N/A | N/A | Dead end. Zapier-only. Explicitly confirmed by Podia help center |
| **LearnDash** (WP plugin) | Yes — WP REST API + ldlms/v2 (beta) | Full CRUD on Courses, Lessons, Topics, Quizzes | **Yes — unlimited.** Lesson `content` is raw WP post HTML; custom CSS via theme or per-post `<style>` | LearnDash license + self-hosted WP | LearnDash ~$199/yr + hosting (~$10–30/mo) | You own the server — whatever your host allows | Maximum control, lowest cost, HTML is native. Tradeoff: you operate WordPress |
| **Tutor LMS** (WP plugin) | Yes — REST API for Free; Write/Delete endpoints require **Pro** | Full CRUD on courses & lessons (Pro for writes) | Yes — lesson content is WP post HTML | Tutor LMS Pro license + WP | Pro ~$199/yr + hosting | Host-dependent | Similar profile to LearnDash; slightly younger API, cheaper license, comparable raw-HTML capability |
| **Circle.so** | Yes (Headless/Admin API) | Courses module exists; API coverage of course content creation is partial | Limited — lessons go through Circle's block/WYSIWYG editor | **Business** plan (API + automations gated here) | Business ~$399/mo | Per-token limits, documented | Community-first; course authoring UX is not the strong suit for an HTML-first pipeline |
| **Mighty Networks** | Yes, but narrow | Limited — primarily members/spaces/events, not deep course authoring | No — course lessons authored in Mighty's block editor | **Scale** plan | **$179/mo** (Scale) | Not publicly specified | API is not the primary surface; not suited for bulk HTML ingestion |

## Recommendation

For a `markdown → processed HTML → API push` pipeline, the three real contenders are **LearnDash**, **Thinkific (classic builder)**, and **LearnWorlds**.

**LearnDash is the strongest technical fit.** Because lesson bodies are native WordPress posts, any HTML/CSS we generate renders verbatim — no sanitization, no block-editor translation layer. The WP REST API is the most stable, best-documented CRUD surface in this entire list, and total cost is the lowest (~$20–50/mo all-in). The tradeoff is operational: we run WordPress, which means we own updates, backups, and hosting.

**Thinkific Grow** at $199/mo gives us a hosted experience with genuine HTML support in Text Lessons and a clean API — but we must explicitly use the classic course builder, because sites defaulting to the new builder (post-Jan 2026) lose API write access to courses/chapters.

**LearnWorlds** is the premium hosted option with the most sophisticated API, but the Learning Center plan floor (~$299/mo) only makes sense if the polished student UX and native extended API matter more than cost.

**Kajabi (incumbent) is now viable but unproven** — the public API launched Sept 2025, so it's ~7 months old and the course-write endpoints should be verified against the OpenAPI spec before we commit the pipeline to it. At $399–499/mo Pro, it's the most expensive "hosted" option.

**Dead ends for this use case:** Podia (no public API), Mighty Networks (no HTML authoring via API), and Teachable's 10k/month request cap (too low for bulk backfill of 10 courses).

## Decision Tradeoff

LearnDash gives total HTML control at ~10% of hosted pricing, in exchange for running WordPress ourselves. Thinkific/LearnWorlds skip ops at 4–15x the monthly cost. Kajabi stays viable if we value incumbent familiarity over cost or API maturity.

## Next Steps (Candidates)

- Prototype a LearnDash pipeline (local WP + LearnDash + markdown→HTML→REST script) against a single SOUP week to validate end-to-end authoring speed
- Dig into Kajabi's OpenAPI spec to assess whether migration-in-place (stay on Kajabi, add API pipeline) is realistic
- Pick one SOUP course as the pilot target before committing to a platform

## Sources

- [Does Kajabi have a public API? — Kajabi Help](https://help.kajabi.com/hc/en-us/articles/28283307533595-Does-Kajabi-have-a-public-API)
- [Using Kajabi's Public API — Kajabi Help](https://help.kajabi.com/en/articles/12696419-using-kajabi-s-public-api)
- [Kajabi Developers Portal](https://developers.kajabi.com)
- [Kajabi Pricing](https://www.kajabi.com/pricing)
- [Thinkific Admin API Reference](https://developers.thinkific.com/api/api-documentation/)
- [Thinkific API Overview — new builder exclusion](https://support.thinkific.dev/hc/en-us/articles/5700872617111-API-Overview)
- [Thinkific Public API Rate Limits](https://developers.thinkific.com/api/rate-limits/)
- [Thinkific Pricing 2026 — Ruzuku](https://www.ruzuku.com/learn/articles/thinkific-pricing-plans)
- [Teachable Pricing 2026](https://www.teachable.com/pricing)
- [Teachable Pricing 2026 — Ruzuku](https://www.ruzuku.com/compare/teachable-pricing)
- [LearnWorlds API Documentation — Help Center](https://support.learnworlds.com/support/solutions/articles/12000017230-learnworlds-api-documentation)
- [LearnWorlds Extended API & Webhooks](https://www.learnworlds.com/extended-elearning-api/)
- [LearnWorlds Stoplight API Docs](https://www.learnworlds.dev/docs/api/17ce94ba40ba9-api)
- [Does Podia have a public API? — Podia Help](https://help.podia.com/en/articles/11371075-does-podia-have-a-public-api-or-webhooks)
- [LearnDash REST API v2 Docs](https://developers.learndash.com/rest-api/v2/)
- [Tutor LMS Pro REST API Docs](https://docs.themeum.com/tutor-lms/developer-documentation/rest-apis-for-tutor-lms-pro/)
- [Circle vs Mighty Networks comparison (API tier pricing)](https://www.mightynetworks.com/resources/circle-vs-mighty-networks)
- [Kajabi Pro Plan Pricing Update — bebosscreative](https://www.bebosscreative.com/blog/kajabi-pricing-and-features-update-september-2025)

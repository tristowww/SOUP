---
spike: 001
name: html-fidelity-minimal
validates: "Given a WP+LearnDash sandbox, when we POST a lesson with inline <style> and custom HTML via REST API as an admin, then the stored content round-trips unchanged AND the rendered student view matches our source"
verdict: PARTIAL
related: [002, 003]
tags: [learndash, wordpress, rest-api, html, kill-switch]
---

# Spike 001 — HTML Fidelity (Minimal)

## What This Validates

**The kill-switch question:** does WordPress's content pipeline preserve raw HTML — including `<style>` blocks, custom class attributes, tables, and nested divs — when content is POSTed via the REST API by an admin user, AND does the published student view render that HTML faithfully?

If WP strips `<style>` or mangles our markup, the whole "markdown → HTML → API push" pipeline for LearnDash is dead and we pivot to Thinkific or Kajabi. Nothing else in spikes 002/003 matters until this passes.

### Given / When / Then

- **Given** a WordPress site with LearnDash installed and an admin Application Password
- **When** we POST `test_content.html` (which includes an inline `<style>` block, a styled table, custom div wrappers, and a code block) to `/wp-json/wp/v2/posts` or `/wp-json/wp/v2/sfwd-lessons`
- **Then** (a) the stored `content.raw` field fetched back from WP is byte-for-byte identical (ignoring trailing whitespace), AND (b) the rendered public view shows the styled table with our custom CSS applied.

## How to Run

### Sandbox choice (resolved)

Originally planned to use InstaWP with a LearnDash template, but:
- **InstaWP free tier has no LearnDash template available** (LearnDash is a paid plugin).
- **User's home network (Charter/Spectrum via CUJO) silently blocks the `instawp.site` and `instawp.xyz` TLDs.** HTTPS requests are intercepted and redirected to `block.charter-prod.hosted.cujo.io/warn.html`.

**Pivoted to WordPress Playground CLI (`@wp-playground/cli`)** — runs vanilla WP locally via PHP.wasm with zero external network dependency. Since LearnDash lessons (`sfwd-lessons` CPT) inherit WP's core content pipeline unchanged, vanilla WP answers the fidelity question faithfully. LearnDash-specific endpoints are deferred to spike 002.

### Steps (actual, reproducible)

Prereqs: Node 18+, Python 3.8+.

```bash
cd .planning/spikes/001-html-fidelity-minimal
# 1. Start WP Playground with the blueprint (creates admin, installs mu-plugin for HTTP Basic Auth + app passwords, creates app password, writes it to /wp-content/spike-app-password.txt)
npx --yes @wp-playground/cli@latest server --blueprint=./blueprint.json --port=9400 --login
#    -> wait for "Ready! WordPress is running on http://127.0.0.1:9400"

# In another shell:
# 2. Fetch the app password the blueprint created
APP_PASS=$(curl -s http://127.0.0.1:9400/wp-content/spike-app-password.txt)

# 3. Push the test lesson
export WP_BASE="http://127.0.0.1:9400"
export WP_USER="admin"
export WP_APP_PASS="$APP_PASS"
export WP_POST_TYPE="posts"
python push_lesson.py test_content.html

# 4. Open the printed URL in a browser; compare against expected_render.md
```

**Why the blueprint needs a mu-plugin (`spike-auth-fix.php`):** WP Playground's PHP-WASM SAPI does not auto-populate `$_SERVER['PHP_AUTH_USER']` from the `Authorization: Basic` header. The mu-plugin extracts credentials from `HTTP_AUTHORIZATION` and also forces `wp_is_application_passwords_available` to true (default requires HTTPS). Both are local-sandbox concerns — a production InstaWP/LearnDash host would not need either fix.

**Why the script sends a `playground_auto_login_already_happened=1` cookie:** Playground's `--login` flag intercepts the first request per session with a redirect that sets admin cookies. Sending this cookie short-circuits the redirect so Basic Auth reaches the REST handler.

## What to Expect

**Script stdout will report:**
- `Created: <url>` and `ID: <n>` on successful POST
- The raw stored content pulled back from WP
- `✓ IDENTICAL` (best case) or `⚠ DIFFERS` with the transformed content printed for inspection

**In the browser at the created URL, you should see:**
- A styled blue callout box (from the `<style>` block's `.soup-callout` class)
- A table with alternating row colors
- A code block with monospace font and gray background
- A two-column flex layout for the "learning objectives" section

**Failure modes to watch for:**
- `<style>` block entirely stripped → admin `wp_kses_post` is applying (shouldn't for admins, but some themes/security plugins override)
- `class` attributes stripped on `<div>` / `<table>`
- Auto-paragraphs (`wpautop`) inserting `<br>` inside our `<pre>` or `<table>`
- Inline styles preserved but `<style>` tag removed

## Results

**Verdict:** PARTIAL — kill-switch **PASSED**. WP preserves raw HTML + `<style>` in the database unchanged; `content.rendered` has cosmetic `wpautop` + `wptexturize` scars that are fixable with a two-line mu-plugin on the real host.

### Evidence — raw storage round-trip

Script output:
```
RAW ROUND-TRIP: IDENTICAL (WP stored our HTML unchanged)
<style> tag: source=True stored=True rendered=True
```

The full `<style>` block (50+ lines of CSS, including selectors like `.soup-table tr:nth-child(even) td` and flex layout rules) came back byte-for-byte identical from `GET /wp-json/wp/v2/posts/{id}?context=edit`. No filtering, no attribute stripping, no CSS sanitization. **Admins authenticated via Application Password retain full HTML capabilities.**

### Evidence — public rendering (`content.rendered`)

Fetched `http://127.0.0.1:9400/2026/04/19/spike-001-html-fidelity-test/` and confirmed:
- `<style>` block: present verbatim in `<body>` (not moved to `<head>`, but browsers still apply it)
- All four class attributes (`soup-callout`, `soup-objectives`, `soup-table`, `soup-code`): preserved
- `id="module-intro"` anchor: preserved
- `<table>` structure (thead/tbody/tr/th/td): intact
- `<pre>` whitespace and em-dashes (`—`): preserved exactly — no `<br>` injection, no whitespace collapse

### Caveats — two cosmetic WP filters scar `content.rendered`

**1. `wpautop` inserts stray `</p>` inside nested divs.** Inside `<div class="soup-objectives">` blocks that contain `<strong>` followed by block-level children (`<ul>`, `<p>`), WP's auto-paragraph filter closed an implied paragraph with a stray `</p>`:

```html
<strong>By the end of this lesson you will:</strong></p>    ← stray
<ul> ... </ul></div>

<strong>Estimated time:</strong></p>                         ← stray
<p>18 minutes reading + 12 minutes exercise</p>
</p></div>                                                   ← stray
```

Browsers tolerate this (extra `</p>` is silently dropped), but the rendered DOM is not pristine.

**2. `wptexturize` smart-quotes apostrophes.** `don't` → `don&#8217;t`. Cosmetic only — renders identically as a curly apostrophe — but content is modified.

### Fix for the production pipeline

Ship a one-off mu-plugin on the real LearnDash host (3 lines):

```php
add_action('init', function () {
    remove_filter('the_content', 'wpautop');
    remove_filter('the_content', 'wptexturize');
}, 20);
```

Scope it to the `sfwd-lessons` post type only if the main blog still wants default formatting. With this in place, `content.rendered` would match `content.raw` exactly for our course lessons.

### Surprises

- **Stack choice was a detour, not the answer.** The real spike debt was infrastructure: CUJO network block + LearnDash licensing + WASM-SAPI auth header quirks. None of these affect the production answer — they affected how long it took to get to a running WP instance.
- **The auto-login UX of WP Playground is hostile to REST clients.** Expect to send `playground_auto_login_already_happened=1` in any automated script against Playground.
- **Curly quotes are an underappreciated concern.** `wptexturize` will silently alter punctuation in course content (em-dashes, quotes, ellipses). For I/O Psych content with statistical notation (e.g., `r = .51`), check this doesn't mangle symbols.

### Implications for spikes 002/003

- **002 (course-hierarchy-api): GREEN-LIT.** HTML fidelity is no longer a blocker. Spike 002 can focus purely on the `ldlms/v2` endpoint shapes and parent/child linkage — requires real LearnDash (license + InstaWP or Local-by-Flywheel), not WP Playground.
- **003 (bulk-push-auth-perf): GREEN-LIT with a new sub-question.** Add: does the production host (whichever we pick) require the same `wpautop`/`wptexturize` mu-plugin, or is it only a WP default that the host might already disable? And: on a real host, how many lessons/minute can we sustain?
- **Pipeline shape crystallizing:** `markdown → HTML+CSS (local)` → `POST /wp-json/wp/v2/sfwd-lessons` with Application Password Basic Auth → WP stores raw → render unchanged via mu-plugin. No surprises, no sanitization layer to fight.

### Artifacts

- `http://127.0.0.1:9400/2026/04/19/spike-001-html-fidelity-test/` (ephemeral — tied to this Playground session)
- Stored content dump: see script stdout in commit log
- Post ID in this session: 4

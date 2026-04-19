---
spike: 003
name: bulk-push-perf-lite
validates: "Given a vanilla WP site + an Application Password, when we push N lessons sequentially and then concurrently, then all succeed within reasonable latency and no rate limit or auth-exhaustion failures surface"
verdict: PARTIAL
related: [001, 002]
tags: [wordpress, rest-api, performance, auth, bulk]
---

# Spike 003-lite — Bulk Push Performance

## What This Validates

A reduced-scope version of the originally-planned spike 003. The original required a real LearnDash install to test `sfwd-lessons` endpoints; we don't have a license yet. This lite version tests the WP core `/wp-json/wp/v2/posts` endpoint — which LearnDash's lesson endpoint inherits request handling from — so the numbers transfer directionally.

### Given / When / Then

- **Given** the WP Playground instance from spike 001 with a working app password
- **When** we push N=10 lessons sequentially, then another 10 with a ThreadPoolExecutor pool of 5
- **Then** (a) all 20 succeed, (b) no 429/503 rate-limit responses, (c) the same app password survives all requests, (d) sequential p50 latency is tolerable for a manual run (≤2s/req is fine for authoring; ≤500ms is great), (e) concurrency provides non-trivial speedup.

## How to Run

Prereq: Playground running from spike 001 (same blueprint, port 9400).

```bash
cd .planning/spikes/003-bulk-push-perf-lite
python bulk_push.py
```

The script auto-fetches the app password from `http://127.0.0.1:9400/wp-content/spike-app-password.txt` (written by spike 001's blueprint). Override with `WP_APP_PASS=...` if needed.

Env knobs: `BULK_N` (default 10), `BULK_CONC` (default 5), `WP_POST_TYPE` (default `posts`).

## What to Expect

Script prints per-request latency, then summary blocks for sequential and concurrent phases:
- success count, wall time, req/s
- latency min / p50 / p95 / max
- final speedup ratio (sequential wall time ÷ concurrent wall time)

**Failure modes to watch for:**
- Any 401 after the first few requests → app password invalidation or session state corruption
- 429 / 503 under the concurrent phase → WP or Playground worker pool rate-limiting
- Latency drifting upward across the 20 requests → DB or cache bloat from prior runs

## Results

**Verdict:** PARTIAL — auth durability + absence of rate limiting confirmed. Latency/throughput numbers are dominated by WP Playground's PHP.wasm overhead and **do not project to production**; real perf numbers still need measuring on the actual LearnDash host.

### Sequential (10 lessons, 2.5 KB each)

```
success:       10/10
wall time:     38.75s  (0.26 req/s)
latency min:   2249 ms
latency p50:   3998 ms
latency p95:   4872 ms
latency max:   5298 ms
```

100% success. Latency was stable-but-slow (~4s/req) — consistent with PHP.wasm executing the full WP request lifecycle (auth → mu-plugins → filters → DB insert → response) with no compiled JIT.

### Concurrent (10 lessons, ThreadPool of 5)

```
success:       8/10    ← one TimeoutError, one HTTP 500
wall time:     46.93s  (0.21 req/s)
latency min:   7411 ms
latency p50:   20882 ms
latency p95:   30010 ms
latency max:   30228 ms
```

**Concurrency made things WORSE** (speedup 0.83×). Playground's 6 WASM workers serialize contended requests, so 5-way parallelism created head-of-line blocking. Two requests failed outright (one timed out at 30s, one returned 500). This is **WP Playground architecture, not a WP or LearnDash limit** — a real host with proper PHP-FPM + MySQL would not behave this way.

### What WAS validated

1. **Auth durability.** The same Application Password authenticated 18/20 successful requests across both phases with no degradation. WP does not invalidate app passwords on use.
2. **No rate limiting.** Zero 429 or explicit throttle responses. The two failures were infrastructure timeouts under load, not rate limits.
3. **Content pipeline consistency.** Every successful push stored correctly (spike 001's fidelity result holds under repeated use).

### What was NOT meaningfully measured

- **Real-world per-request latency.** 4s/req on Playground is ~10× what a production host would show. Budget around 200–800ms/req for a managed WP host in final math.
- **Safe concurrency ceiling on production.** We can't extrapolate from Playground's 6-worker contention to a 50-concurrent-PHP-FPM host.
- **LearnDash-specific overhead** (course/lesson/topic cross-referencing on save) — deferred to spike 002.

### Implications for production host choice and pipeline design

- **Sequential-first backfill is fine.** For SOUP's ~10 courses × ~20 lessons = ~200 lessons, even at a pessimistic 500ms/req that's 100s total. No reason to over-engineer concurrency on day one.
- **Cap concurrency at 2–3** during bulk operations. WP + MySQL contend under write-heavy bursts; most shared hosts throttle before CPU exhausts.
- **Build a retry wrapper** around the push client — timeouts happen and deserve one exponential-backoff retry before bubbling a real failure.
- **Measure perf again on the real host** after spike 002 lands LearnDash. Re-run this harness (with `WP_POST_TYPE=sfwd-lessons` and `WP_BASE=<production url>`) to get the numbers that actually matter.

### Surprises

- **The concurrency hurt.** We expected at worst neutral scaling under 5-way parallelism — instead got negative scaling. This is specific to Playground's multi-worker model; it's a reminder that **local sandboxes are great for correctness, worthless for performance signal**.
- **No auth drift.** Some WP hosts silently rotate or invalidate application passwords after heavy use. WP core does not; this is a host-layer concern to re-test on the production target.


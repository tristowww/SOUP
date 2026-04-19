#!/usr/bin/env python3
"""Spike 003-lite — bulk-push N lessons to vanilla WP REST API.

Measures sequential per-request latency and concurrent throughput.
Uses the same auth mechanism as spike 001 (Application Password, bypass cookie).

Env vars:
    WP_BASE        default http://127.0.0.1:9400
    WP_USER        default admin
    WP_APP_PASS    required — fetched automatically if WP_BASE hosts the spike password file
    WP_POST_TYPE   default posts
    BULK_N         default 10 — how many lessons to push in each phase
    BULK_CONC      default 5 — parallelism for the concurrent phase

Usage:
    python bulk_push.py [path-to-template-html]

If no template path is given, uses ../001-html-fidelity-minimal/test_content.html.
"""
import base64
import json
import os
import statistics
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


BASE = os.environ.get("WP_BASE", "http://127.0.0.1:9400").rstrip("/")
USER = os.environ.get("WP_USER", "admin")
POST_TYPE = os.environ.get("WP_POST_TYPE", "posts")
N = int(os.environ.get("BULK_N", "10"))
CONC = int(os.environ.get("BULK_CONC", "5"))

COOKIE = "playground_auto_login_already_happened=1"


def fetch_app_password() -> str:
    explicit = os.environ.get("WP_APP_PASS")
    if explicit:
        return explicit
    try:
        req = urllib.request.Request(
            f"{BASE}/wp-content/spike-app-password.txt",
            headers={"User-Agent": "bulk-push/1.0"},
        )
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.read().decode().strip()
    except Exception as e:
        print(f"error: WP_APP_PASS not set and could not auto-fetch: {e}", file=sys.stderr)
        sys.exit(2)


def build_headers(app_pass: str) -> dict:
    tok = base64.b64encode(f"{USER}:{app_pass}".encode()).decode()
    return {
        "Authorization": f"Basic {tok}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "bulk-push/1.0",
        "Cookie": COOKIE,
    }


def push_one(i: int, content: str, headers: dict) -> tuple[int, float, int | None]:
    """Returns (lesson_index, elapsed_seconds, post_id_or_None)."""
    body = json.dumps(
        {
            "title": f"SOUP bulk lesson {i:03d}",
            "content": content,
            "status": "publish",
        }
    ).encode()
    url = f"{BASE}/wp-json/wp/v2/{POST_TYPE}"
    t0 = time.perf_counter()
    try:
        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        return i, time.perf_counter() - t0, data.get("id")
    except urllib.error.HTTPError as e:
        print(f"  lesson {i}: HTTP {e.code}: {e.read().decode()[:150]}", file=sys.stderr)
        return i, time.perf_counter() - t0, None
    except Exception as e:
        print(f"  lesson {i}: {type(e).__name__}: {e}", file=sys.stderr)
        return i, time.perf_counter() - t0, None


def summarize(label: str, latencies: list[float], ok: int, total: int, wall: float) -> None:
    if not latencies:
        print(f"\n{label}: NO DATA")
        return
    lat_ms = sorted(x * 1000 for x in latencies)
    p50 = statistics.median(lat_ms)
    p95 = lat_ms[int(0.95 * (len(lat_ms) - 1))]
    print(f"\n{label}")
    print(f"  success:       {ok}/{total}")
    print(f"  wall time:     {wall:.2f}s  ({total/wall:.2f} req/s)")
    print(f"  latency min:   {min(lat_ms):.0f} ms")
    print(f"  latency p50:   {p50:.0f} ms")
    print(f"  latency p95:   {p95:.0f} ms")
    print(f"  latency max:   {max(lat_ms):.0f} ms")


def main() -> int:
    template_path = Path(sys.argv[1]) if len(sys.argv) > 1 else (
        Path(__file__).parent.parent / "001-html-fidelity-minimal" / "test_content.html"
    )
    content = template_path.read_text(encoding="utf-8")
    print(f"template: {template_path} ({len(content):,} bytes)")

    app_pass = fetch_app_password()
    headers = build_headers(app_pass)
    print(f"target:   {BASE}/wp-json/wp/v2/{POST_TYPE}")
    print(f"plan:     {N} sequential, then {N} concurrent (x{CONC})")

    # --- Phase 1: sequential ---
    print(f"\n[sequential] pushing {N} lessons one at a time...")
    seq_latencies: list[float] = []
    seq_ok = 0
    seq_ids: list[int] = []
    t_wall = time.perf_counter()
    for i in range(1, N + 1):
        idx, elapsed, pid = push_one(i, content, headers)
        seq_latencies.append(elapsed)
        if pid is not None:
            seq_ok += 1
            seq_ids.append(pid)
        print(f"  lesson {i:02d}: {elapsed*1000:.0f} ms  id={pid}")
    seq_wall = time.perf_counter() - t_wall
    summarize("SEQUENTIAL", seq_latencies, seq_ok, N, seq_wall)

    # --- Phase 2: concurrent ---
    print(f"\n[concurrent] pushing {N} lessons with pool of {CONC}...")
    conc_latencies: list[float] = []
    conc_ok = 0
    conc_ids: list[int] = []
    t_wall = time.perf_counter()
    with ThreadPoolExecutor(max_workers=CONC) as ex:
        futures = [ex.submit(push_one, 100 + i, content, headers) for i in range(1, N + 1)]
        for f in as_completed(futures):
            idx, elapsed, pid = f.result()
            conc_latencies.append(elapsed)
            if pid is not None:
                conc_ok += 1
                conc_ids.append(pid)
            print(f"  lesson {idx:03d}: {elapsed*1000:.0f} ms  id={pid}")
    conc_wall = time.perf_counter() - t_wall
    summarize(f"CONCURRENT (pool={CONC})", conc_latencies, conc_ok, N, conc_wall)

    print("\n--- summary ---")
    print(f"total created: {seq_ok + conc_ok}/{2*N}")
    print(f"sequential:    {seq_wall:.2f}s  ({N/seq_wall:.2f} req/s)")
    print(f"concurrent:    {conc_wall:.2f}s  ({N/conc_wall:.2f} req/s)")
    speedup = seq_wall / conc_wall if conc_wall > 0 else 0
    print(f"speedup:       {speedup:.2f}x")
    return 0 if seq_ok + conc_ok == 2 * N else 1


if __name__ == "__main__":
    sys.exit(main())

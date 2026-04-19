#!/usr/bin/env python3
"""Spike 001 — push a raw HTML file to a WP/LearnDash post via REST API.

Uses only stdlib (urllib) so no pip install needed.

Env vars required:
    WP_BASE        e.g. https://your-sandbox.instawp.xyz
    WP_USER        admin username
    WP_APP_PASS    Application Password (4-word format, spaces preserved)
    WP_POST_TYPE   "posts" (plain WP) or "sfwd-lessons" (LearnDash lesson) — default: posts

Usage:
    python push_lesson.py test_content.html
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def env(name: str, default: str | None = None) -> str:
    val = os.environ.get(name, default)
    if val is None:
        print(f"error: set env var {name}", file=sys.stderr)
        sys.exit(2)
    return val


def main() -> int:
    base = env("WP_BASE").rstrip("/")
    user = env("WP_USER")
    app_pass = env("WP_APP_PASS")
    post_type = env("WP_POST_TYPE", "posts")

    if len(sys.argv) < 2:
        print("usage: push_lesson.py <html-file>", file=sys.stderr)
        return 2

    html_path = Path(sys.argv[1])
    content = html_path.read_text(encoding="utf-8")

    token = base64.b64encode(f"{user}:{app_pass}".encode()).decode()
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "spike-001/1.0",
        # Bypass WP Playground's auto-login redirect interceptor
        "Cookie": "playground_auto_login_already_happened=1",
    }

    # Create the post
    create_url = f"{base}/wp-json/wp/v2/{post_type}"
    body = json.dumps(
        {
            "title": "Spike 001 — HTML Fidelity Test",
            "content": content,
            "status": "publish",
        }
    ).encode()

    print(f"POST {create_url}")
    try:
        req = urllib.request.Request(create_url, data=body, headers=headers, method="POST")
        with urllib.request.urlopen(req) as r:
            created = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode(errors='replace')}", file=sys.stderr)
        return 1

    link = created.get("link", "<no link>")
    post_id = created.get("id", "?")
    print(f"  -> created id={post_id}")
    print(f"  -> public url: {link}")

    # Fetch it back in edit context to see raw stored HTML
    get_url = f"{base}/wp-json/wp/v2/{post_type}/{post_id}?context=edit"
    print(f"\nGET {get_url}")
    try:
        req = urllib.request.Request(get_url, headers=headers, method="GET")
        with urllib.request.urlopen(req) as r:
            stored = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode(errors='replace')}", file=sys.stderr)
        return 1

    raw = stored.get("content", {}).get("raw", "")
    rendered = stored.get("content", {}).get("rendered", "")

    print("\n--- STORED (content.raw from WP DB) ---")
    print(raw)
    print("--- END STORED ---")

    print("\n--- RENDERED (content.rendered, post-filters) ---")
    print(rendered[:2000] + ("\n…(truncated)" if len(rendered) > 2000 else ""))
    print("--- END RENDERED ---\n")

    # Verdict
    if raw.strip() == content.strip():
        print("RAW ROUND-TRIP: IDENTICAL (WP stored our HTML unchanged)")
    else:
        print("RAW ROUND-TRIP: DIFFERS (WP transformed our HTML on store)")
        print("  -> Check above for what changed: <style> stripped? classes removed?")

    style_in = "<style" in content.lower()
    style_stored = "<style" in raw.lower()
    style_rendered = "<style" in rendered.lower()
    print(f"\n<style> tag: source={style_in} stored={style_stored} rendered={style_rendered}")

    print(f"\nNow open in a browser and visually verify:\n  {link}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""
Haggadah Text Analytics + Visualization Generator
===================================================
1. Fetches the Pesach Haggadah from Sefaria's API
2. Fetches Psalms 113-118, 136 and Deuteronomy 26 for cross-referencing
3. Runs computational analysis on every section
4. Outputs: analysis table, JSON data, and a complete HTML visualization

Usage:
    pip install requests
    python haggadah_generate.py

Outputs:
    haggadah_data.json          — raw analysis data
    haggadah_visualization.html — complete interactive radial visualization
"""

import requests
import json
import re
import time
import os

# ============================================================
# CONFIG
# ============================================================

API = "https://www.sefaria.org/api/texts/"

SECTIONS = [
    {"key": "Kadesh",       "ref": "Pesach Haggadah, Kadesh",       "sec": 0, "desc": "Kiddush. Gen 2:1-3 + Geonic blessings."},
    {"key": "Urchatz",      "ref": "Pesach Haggadah, Urchatz",      "sec": 0, "desc": "Silence. Hand-washing."},
    {"key": "Karpas",       "ref": "Pesach Haggadah, Karpas",       "sec": 0, "desc": "One blessing."},
    {"key": "Yachatz",      "ref": "Pesach Haggadah, Yachatz",      "sec": 0, "desc": "Breaking matzah."},
    {"key": "Ha Lachma",    "ref": "Pesach Haggadah, Magid, Ha Lachma Anya",                                    "sec": 1, "desc": "Aramaic. 'This is the bread of oppression.'"},
    {"key": "4 Questions",  "ref": "Pesach Haggadah, Magid, Four Questions",                                    "sec": 1, "desc": "Ma Nishtana. Children lead."},
    {"key": "Avadim",       "ref": "Pesach Haggadah, Magid, We Were Slaves in Egypt",                           "sec": 1, "desc": "'We were slaves.' Past tense = present identity."},
    {"key": "5 Rabbis",     "ref": "Pesach Haggadah, Magid, Story of the Five Rabbis",                          "sec": 1, "desc": "100% rabbi. Five sages, Bnei Brak."},
    {"key": "4 Sons",       "ref": "Pesach Haggadah, Magid, The Four Sons",                                     "sec": 1, "desc": "32% rabbi. Most multi-voiced section."},
    {"key": "Yechol",       "ref": "Pesach Haggadah, Magid, Yechol Me'rosh Chodesh",                            "sec": 1, "desc": "100% rabbi. Talmudic reasoning."},
    {"key": "Mitchila",     "ref": "Pesach Haggadah, Magid, In the Beginning Our Fathers Were Idol Worshipers",  "sec": 1, "desc": "24% rabbi. Joshua 24 quoted."},
    {"key": "First Fruits", "ref": "Pesach Haggadah, Magid, First Fruits Declaration",                          "sec": 1, "desc": "19 citations — 1 per 24 words. 53% of Deut 26:5-8."},
    {"key": "10 Plagues",   "ref": "Pesach Haggadah, Magid, The Ten Plagues",                                   "sec": 1, "desc": "72% rabbi. Plague multiplication debate."},
    {"key": "Dayenu",       "ref": "Pesach Haggadah, Magid, Dayenu",                                            "sec": 1, "desc": "14x illu / 14x dayenu. Pivot at stanza 11."},
    {"key": "R. Gamliel",   "ref": "Pesach Haggadah, Magid, Rabban Gamliel's Three Things",                     "sec": 1, "desc": "LAST named rabbi. Pesach/Matzah/Maror."},
    {"key": "Hallel 1st",   "ref": "Pesach Haggadah, Magid, First Half of Hallel",                              "sec": 1, "desc": "30% psalm cross-ref'd. Ps 113-114."},
    {"key": "Cup 2",        "ref": "Pesach Haggadah, Magid, Second Cup of Wine",                                "sec": 1, "desc": "Prophetic perfect: 'who HAS redeemed us.'"},
    {"key": "Rachtzah",     "ref": "Pesach Haggadah, Rachtzah",     "sec": 2, "desc": "Hand-washing with blessing."},
    {"key": "Motzi",        "ref": "Pesach Haggadah, Motzi Matzah", "sec": 2, "desc": "Two blessings over matzah."},
    {"key": "Maror",        "ref": "Pesach Haggadah, Maror",        "sec": 2, "desc": "Bitter herb."},
    {"key": "Korech",       "ref": "Pesach Haggadah, Korech",       "sec": 2, "desc": "Hillel's sandwich. Last rabbi echo."},
    {"key": "Meal",         "ref": "Pesach Haggadah, Shulchan Orech","sec": 2, "desc": "4 words. ~50 min. The great silence."},
    {"key": "Tzafun",       "ref": "Pesach Haggadah, Tzafun",       "sec": 2, "desc": "Afikoman eaten."},
    {"key": "Birkat",       "ref": "Pesach Haggadah, Barech, Birkat Hamazon",    "sec": 3, "desc": "767w. 89 'we' refs. 3 prophetic perfects."},
    {"key": "Cup 3",        "ref": "Pesach Haggadah, Barech, Third Cup of Wine",  "sec": 3, "desc": "Third cup."},
    {"key": "Shfoch",       "ref": "Pesach Haggadah, Barech, Pour Out Thy Wrath", "sec": 3, "desc": "'Pour out Your wrath.' Elijah's door."},
    {"key": "Hallel 2nd",   "ref": "Pesach Haggadah, Hallel, Second Half of Hallel",       "sec": 4, "desc": "27% psalm. 6 prophetic perfects. Ps 115-118."},
    {"key": "Songs",        "ref": "Pesach Haggadah, Hallel, Songs of Praise and Thanks",  "sec": 4, "desc": "chasdo 26x. 24% psalm. Ps 136 + Nishmat."},
    {"key": "Cup 4",        "ref": "Pesach Haggadah, Hallel, Fourth Cup of Wine",           "sec": 4, "desc": "Fourth cup."},
    {"key": "Chasal",       "ref": "Pesach Haggadah, Nirtzah, Chasal Siddur Pesach",       "sec": 5, "desc": "'The seder is complete.'"},
    {"key": "L'Shana",      "ref": "Pesach Haggadah, Nirtzah, L'Shana HaBa'a",            "sec": 5, "desc": "'Next year in Jerusalem!'"},
    {"key": "Vayehi",       "ref": "Pesach Haggadah, Nirtzah, And It Happened at Midnight","sec": 5, "desc": "Medieval piyyut."},
    {"key": "Zevach",       "ref": "Pesach Haggadah, Nirtzah, Zevach Pesach",              "sec": 5, "desc": "Medieval piyyut."},
    {"key": "Ki Lo",        "ref": "Pesach Haggadah, Nirtzah, Ki Lo Na'e",                 "sec": 5, "desc": "Medieval refrains."},
    {"key": "Adir Hu",      "ref": "Pesach Haggadah, Nirtzah, Adir Hu",                    "sec": 5, "desc": "Alphabetical acrostic."},
    {"key": "Echad Mi",     "ref": "Pesach Haggadah, Nirtzah, Echad Mi Yodea",             "sec": 5, "desc": "yodea 26x. Children return."},
    {"key": "Chad Gadya",   "ref": "Pesach Haggadah, Nirtzah, Chad Gadya",                 "sec": 5, "desc": "100% Aramaic. gadya 31x."},
]

# Voice mix assignments (editorial, informed by computed rabbi/psalm/blessing %)
VOICE_MIX = {
    "Kadesh":       {"liturgical":45,"collective":55},
    "Karpas":       {"collective":100},
    "Ha Lachma":    {"collective":100},
    "4 Questions":  {"children":90,"collective":10},
    "Avadim":       {"collective":85,"god":15},
    "5 Rabbis":     {"rabbis":95,"collective":5},
    "4 Sons":       {"rabbis":40,"god":35,"children":20,"collective":5},
    "Yechol":       {"rabbis":80,"god":20},
    "Mitchila":     {"collective":50,"god":40,"rabbis":10},
    "First Fruits": {"rabbis":55,"god":30,"collective":15},
    "10 Plagues":   {"rabbis":75,"god":10,"collective":15},
    "Dayenu":       {"collective":95,"god":5},
    "R. Gamliel":   {"rabbis":50,"collective":40,"god":10},
    "Hallel 1st":   {"liturgical":85,"collective":15},
    "Cup 2":        {"collective":70,"liturgical":30},
    "Rachtzah":     {"collective":100}, "Motzi": {"collective":100},
    "Maror":        {"collective":100},
    "Korech":       {"rabbis":55,"collective":45},
    "Tzafun":       {"collective":100},
    "Birkat":       {"collective":55,"liturgical":30,"god":10,"rabbis":5},
    "Cup 3":        {"collective":100},
    "Shfoch":       {"god":80,"collective":20},
    "Hallel 2nd":   {"liturgical":85,"collective":10,"god":5},
    "Songs":        {"liturgical":70,"collective":25,"god":5},
    "Cup 4":        {"collective":80,"liturgical":20},
    "Chasal":       {"collective":100}, "L'Shana": {"collective":100},
    "Vayehi":       {"collective":90,"god":10}, "Zevach": {"collective":90,"god":10},
    "Ki Lo":        {"collective":100}, "Adir Hu": {"collective":100},
    "Echad Mi":     {"children":40,"collective":60},
    "Chad Gadya":   {"children":35,"collective":65},
}

# Composition era (editorial)
AGE_MAP = {
    "Kadesh": {"biblical":10,"mishnaic":5,"geonic":55},
    "Urchatz": {"mishnaic":100}, "Karpas": {"mishnaic":60,"geonic":40},
    "Yachatz": {"mishnaic":100},
    "Ha Lachma": {"talmudic":80,"mishnaic":20},
    "4 Questions": {"mishnaic":100},
    "Avadim": {"mishnaic":80,"talmudic":20},
    "5 Rabbis": {"mishnaic":90,"talmudic":10},
    "4 Sons": {"mishnaic":60,"talmudic":30,"biblical":10},
    "Yechol": {"talmudic":100},
    "Mitchila": {"biblical":40,"mishnaic":30,"talmudic":30},
    "First Fruits": {"biblical":25,"mishnaic":25,"talmudic":30,"geonic":10},
    "10 Plagues": {"mishnaic":40,"talmudic":50,"biblical":10},
    "Dayenu": {"mishnaic":20,"talmudic":20,"geonic":40,"medieval_era":20},
    "R. Gamliel": {"mishnaic":70,"talmudic":20,"biblical":10},
    "Hallel 1st": {"psalms_era":85,"mishnaic":15},
    "Cup 2": {"mishnaic":50,"talmudic":30,"geonic":20},
    "Rachtzah": {"mishnaic":100}, "Motzi": {"mishnaic":95,"biblical":5},
    "Maror": {"mishnaic":100}, "Korech": {"mishnaic":65,"medieval_era":35},
    "Meal": {"mishnaic":100}, "Tzafun": {"mishnaic":80,"geonic":20},
    "Birkat": {"psalms_era":15,"biblical":10,"mishnaic":15,"talmudic":30,"geonic":25,"medieval_era":5},
    "Cup 3": {"mishnaic":100},
    "Shfoch": {"psalms_era":60,"geonic":40},
    "Hallel 2nd": {"psalms_era":80,"mishnaic":5,"geonic":15},
    "Songs": {"psalms_era":55,"geonic":30,"medieval_era":15},
    "Cup 4": {"mishnaic":80,"geonic":20},
    "Chasal": {"geonic":80,"medieval_era":20}, "L'Shana": {"geonic":100},
    "Vayehi": {"medieval_era":100}, "Zevach": {"medieval_era":100},
    "Ki Lo": {"medieval_era":100}, "Adir Hu": {"medieval_era":100},
    "Echad Mi": {"medieval_era":100}, "Chad Gadya": {"medieval_era":100},
}

RABBIS = ["rabbi","eliezer","yehoshua","elazar","akiva","tarfon","gamliel",
          "hillel","yose","yehuda","jose","judah","taught","said rabbi","expound"]
ARAMAIC = ["דא","די ","לחמא","ענייא","גדיא","דזבן","ואתא","השתא","יתי","דצריך","יפסח","חד "]
ARAM_FP = {"First Fruits","Kadesh","Birkat","Hallel 2nd"}
RABBI_FP = {"Echad Mi"}

# ============================================================
# UTILITIES
# ============================================================

def strip_html(t):
    if not t: return ""
    if isinstance(t, list): return " ".join(strip_html(x) for x in t if x)
    return re.sub(r'<[^>]+>', '', str(t)).strip()

def strip_nikkud(t):
    return re.sub(r'[\u0591-\u05C7]', '', t)

def wc(t):
    return len(t.split()) if t else 0

def flat(n):
    if isinstance(n, str):
        s = strip_html(n)
        return [s] if s else []
    if isinstance(n, list):
        r = []
        for x in n: r.extend(flat(x))
        return r
    return []

def ngram_overlap(src, tgt, mn=3):
    if not src or not tgt: return 0
    sw = src.split()
    m, i = 0, 0
    while i < len(sw):
        f = False
        for n in range(min(8, len(sw)-i), mn-1, -1):
            if ' '.join(sw[i:i+n]) in tgt:
                m += n; i += n; f = True; break
        if not f: i += 1
    return m

def fetch(ref):
    time.sleep(0.25)
    r = requests.get(f"{API}{requests.utils.quote(ref)}?context=0", timeout=15)
    r.raise_for_status()
    return r.json()

# ============================================================
# MAIN PIPELINE
# ============================================================

def run():
    print("=" * 70)
    print("HAGGADAH TEXT ANALYTICS — LIVE FROM SEFARIA")
    print("=" * 70)

    # 1. FETCH
    print("\n[1/3] Fetching from Sefaria API...")
    sections = []
    for i, s in enumerate(SECTIONS):
        print(f"  [{i+1:2d}/{len(SECTIONS)}] {s['key']}...", end="", flush=True)
        try:
            d = fetch(s["ref"])
            he = strip_html(d.get("he",""))
            en = strip_html(d.get("text",""))
            sections.append({**s, "he": he, "en": en,
                "he_s": strip_nikkud(he), "he_w": wc(he), "en_w": wc(en),
                "en_segs": flat(d.get("text",""))})
            print(f" {wc(he)} HE words")
        except Exception as e:
            print(f" ERROR: {e}")
            sections.append({**s,"he":"","en":"","he_s":"","he_w":0,"en_w":0,"en_segs":[]})

    print("\n  Fetching Psalms...", flush=True)
    psalms = {}
    for ref in ["Psalms.113","Psalms.114","Psalms.115","Psalms.116",
                 "Psalms.117","Psalms.118","Psalms.136"]:
        try:
            d = fetch(ref)
            psalms[ref] = strip_nikkud(strip_html(d.get("he","")))
            print(f"    {ref}: {wc(psalms[ref])} words")
        except: psalms[ref] = ""

    print("  Fetching Deuteronomy 26...", flush=True)
    try:
        d = fetch("Deuteronomy.26")
        deut_vs = [strip_nikkud(v) for v in flat(d.get("he",""))]
        print(f"    {len(deut_vs)} verses")
    except: deut_vs = []

    # 2. ANALYZE
    print("\n[2/3] Analyzing...")
    results = []
    for s in sections:
        el = s["en"].lower()
        ew = max(s["en_w"], 1)
        hw = max(s["he_w"], 1)
        k = s["key"]

        # Rabbi detection
        rw = sum(wc(seg) for seg in s["en_segs"]
                 if any(n in seg.lower() for n in RABBIS))
        if k in RABBI_FP: rw = 0
        rp = min(100, round(rw / ew * 100))

        # Psalm overlap
        pw = sum(ngram_overlap(pt, s["he_s"]) for pt in psalms.values())
        pp = min(100, round(pw / hw * 100))

        # Aramaic
        ac = sum(s["he_s"].count(m) for m in ARAMAIC)
        ap = min(100, ac * 8) if k not in ARAM_FP else 0

        # Citations
        cit = len(re.findall(r'שנאמר', s["he_s"]))

        # Pronouns
        we = len(re.findall(r'\b(we|our|us)\b', el))
        you = len(re.findall(r'\b(you|your|thou|thy)\b', el))
        he2 = len(re.findall(r'\b(he|his|him)\b', el))

        # Prophetic perfect
        ppf = len(re.findall(r'has (brought|redeemed|taken|done|given|chosen|made|delivered)', el))

        # Dayenu
        dayC = len(re.findall(r'דינו', s["he_s"]))
        ilC = len(re.findall(r'אלו', s["he_s"]))

        results.append({
            "k": k, "s": s["sec"], "d": s["desc"],
            "he": s["he_w"], "rP": rp, "pP": pp, "aP": ap,
            "cit": cit, "we": we, "you": you, "he2": he2,
            "ppf": ppf, "dayC": dayC, "ilC": ilC,
            "mx": VOICE_MIX.get(k, {}),
            "ag": AGE_MAP.get(k, {"mishnaic": 60, "geonic": 20}),
        })

    # Deut overlap
    if deut_vs and len(deut_vs) >= 8:
        ff = next((s for s in sections if s["key"] == "First Fruits"), None)
        if ff:
            d58 = ' '.join(deut_vs[4:8])
            ov = ngram_overlap(d58, ff["he_s"])
            print(f"  Deut 26:5-8 ({wc(d58)}w) -> {ov} words in First Fruits ({round(ov/wc(d58)*100)}%)")

    # 3. OUTPUT
    print("\n[3/3] Generating outputs...")

    # Print table
    total_he = sum(r["he"] for r in results)
    sec_names = {0:"Before",1:"Maggid",2:"Meal",3:"Barech",4:"Hallel",5:"Nirtzah"}
    print(f"\n{'Section':<18} {'':>6} {'Rabbi':>6} {'Psalm':>6} {'Aram':>5} {'Cit':>4} {'we':>4} {'you':>4} {'he':>4} {'PP':>3}")
    print("-" * 85)
    for r in results:
        print(f"{r['k']:<18} {r['he']:>5}w {r['rP']:>5}% {r['pP']:>5}% {r['aP']:>4}% {r['cit']:>4} {r['we']:>4} {r['you']:>4} {r['he2']:>4} {r['ppf']:>3}")
    print("-" * 85)
    print(f"{'TOTAL':<18} {total_he:>5}w")

    # Save JSON
    with open("haggadah_data.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\nSaved haggadah_data.json")

    # Generate HTML
    generate_html(results)
    print("Saved haggadah_visualization.html")
    print("\n" + "=" * 70)
    print("DONE. Open haggadah_visualization.html in a browser.")
    print("=" * 70)


# ============================================================
# HTML GENERATION
# ============================================================

def generate_html(results):
    """Generate complete HTML visualization with embedded data."""

    data_json = json.dumps(results, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Haggadah, Measured</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#ece4d0;font-family:'Cormorant Garamond',Georgia,serif;display:flex;flex-direction:column;align-items:center;padding:20px 10px 60px;color:#302810}}
h1{{font-size:36px;font-weight:600;text-align:center;margin-top:10px}}
.sub{{font-size:19px;font-style:italic;color:#504828;text-align:center;margin:4px 0 16px}}
canvas{{display:block;max-width:100%;height:auto;cursor:pointer}}
#tip{{display:none;position:fixed;pointer-events:none;z-index:99;max-width:420px}}
.tb{{background:#1e1a0e;color:#f0e8d0;padding:22px;border-radius:16px;font-size:16px;line-height:1.6;box-shadow:0 12px 40px rgba(0,0,0,0.35);border:1px solid rgba(200,170,80,0.1)}}
.tn{{font-size:28px;font-weight:600;color:#e0c860;margin-bottom:4px}}
.td{{font-size:15px;color:rgba(240,232,208,0.55);margin-bottom:10px}}
.tg{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:12px}}
.tsn{{font-size:22px;font-weight:600;color:#e0c860}}
.tsl{{font-size:11px;color:rgba(240,232,208,0.25);text-transform:uppercase}}
.tr{{display:flex;align-items:center;gap:8px;margin:4px 0}}
.trd{{width:14px;height:14px;border-radius:50%;flex-shrink:0}}
.trl{{font-size:16px;color:rgba(240,232,208,0.6);flex:1}}
.trv{{font-size:14px;color:rgba(240,232,208,0.35)}}
.tnt{{font-size:13px;color:rgba(240,232,208,0.3);font-style:italic;margin-top:10px;padding-top:10px;border-top:1px solid rgba(200,170,80,0.08)}}
.tsc{{font-size:11px;color:rgba(240,232,208,0.2);text-transform:uppercase;margin:10px 0 3px}}
.leg{{max-width:900px;width:100%;display:flex;flex-wrap:wrap;gap:20px;justify-content:center;margin-top:16px}}
.lg{{text-align:center}}
.lgt{{font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:#1a1008;margin-bottom:6px;font-family:'Fira Sans',sans-serif}}
.lgi{{display:flex;flex-wrap:wrap;gap:6px 18px;justify-content:center}}
.li{{display:flex;align-items:center;gap:6px;font-size:16px;color:#1a1008;font-weight:500;font-family:'Fira Sans',sans-serif}}
.lsq{{width:18px;height:18px;border-radius:4px}}
.ft{{max-width:700px;text-align:center;font-size:15px;color:#605838;font-style:italic;margin-top:18px;line-height:1.5}}
details{{max-width:920px;width:100%;margin-top:20px}}
summary{{cursor:pointer;font-size:16px;color:#605028;font-weight:500}}
table{{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px}}
th{{text-align:left;padding:5px 8px;border-bottom:2px solid #c0b890;color:#3a3010;font-weight:600;font-size:12px;text-transform:uppercase}}
td{{padding:4px 8px;border-bottom:1px solid #e0d8c0;color:#302810}}
</style>
</head>
<body>
<h1>The Haggadah, measured</h1>
<div class="sub">Generated from Sefaria API &middot; {time.strftime('%B %d, %Y')}</div>
<canvas id="cv" width="4000" height="4000"></canvas>
<div class="leg">
<div class="lg"><div class="lgt">Voice bars &mdash; who speaks</div><div class="lgi">
<div class="li"><div class="lsq" style="background:#7a3508"></div>Named rabbis</div>
<div class="li"><div class="lsq" style="background:#1e4a6a"></div>Collective &ldquo;we&rdquo;</div>
<div class="li"><div class="lsq" style="background:#5a2060"></div>Psalmic</div>
<div class="li"><div class="lsq" style="background:#b06008"></div>Children</div>
<div class="li"><div class="lsq" style="background:#2e4a10"></div>God / Torah</div>
</div></div>
<div class="lg"><div class="lgt">Era &mdash; composition period</div><div class="lgi">
<div class="li"><div class="lsq" style="background:#285888"></div>Psalms</div>
<div class="li"><div class="lsq" style="background:#4a6828"></div>Biblical</div>
<div class="li"><div class="lsq" style="background:#a04810"></div>Mishnaic</div>
<div class="li"><div class="lsq" style="background:#802848"></div>Talmudic</div>
<div class="li"><div class="lsq" style="background:#787020"></div>Geonic</div>
<div class="li"><div class="lsq" style="background:#6030a0"></div>Medieval</div>
</div></div>
<div class="lg"><div class="lgt">Seder phase &mdash; outer rim</div><div class="lgi">
<div class="li"><div class="lsq" style="background:#9a7818"></div>Before</div>
<div class="li"><div class="lsq" style="background:#b83030"></div>Maggid</div>
<div class="li"><div class="lsq" style="background:#287848"></div>Meal</div>
<div class="li"><div class="lsq" style="background:#2860a8"></div>Barech</div>
<div class="li"><div class="lsq" style="background:#7830a0"></div>Hallel</div>
<div class="li"><div class="lsq" style="background:#a85020"></div>Nirtzah</div>
</div></div></div>
<div class="ft">Bar height = Hebrew word count &middot; Bar fill = who is speaking &middot; Hover/click for full analysis</div>
<div id="statsPanel" style="max-width:900px;width:100%;margin-top:24px"></div>
<details><summary>Raw data table</summary><table id="dt"></table></details>
<div id="tip"><div class="tb" id="ti"></div></div>

<script>
const D = {data_json};

// Darker-to-lighter from center outward (ui-ux-pro-max sunburst guidance)
const V={{rabbis:'#7a3508',collective:'#1e4a6a',liturgical:'#5a2060',children:'#b06008',god:'#2e4a10'}};
const VN={{rabbis:'Named rabbis',collective:'Collective \\u201cwe\\u201d',liturgical:'Psalmic',children:'Children',god:'God / Torah'}};
const AC={{psalms_era:'#285888',biblical:'#4a6828',mishnaic:'#a04810',talmudic:'#802848',geonic:'#787020',medieval_era:'#6030a0'}};
const AN={{psalms_era:'Psalms ~1000 BCE',biblical:'Biblical',mishnaic:'Mishnaic ~200 CE',talmudic:'Talmudic',geonic:'Geonic ~800 CE',medieval_era:'Medieval ~1400 CE'}};
const SC=['#9a7818','#b83030','#287848','#2860a8','#7830a0','#a85020'];
const SN=['Before','Maggid','Meal','Barech','Hallel','Nirtzah'];
const SGC=['rgba(154,120,24,0.04)','rgba(184,48,48,0.04)','rgba(40,120,72,0.04)','rgba(40,96,168,0.04)','rgba(120,48,160,0.04)','rgba(168,80,32,0.04)'];

const cv=document.getElementById('cv'),ctx=cv.getContext('2d'),W=4000,H=4000,cx=W/2,cy=H/2;
const n=D.length,tH=D.reduce((a,d)=>a+d.he,0),mH=Math.max(...D.map(d=>d.he));
function sd(s){{let a=s;return()=>{{a|=0;a=a+0x6D2B79F5|0;let t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;}};}}
const R=sd(42);

// ===== MOSAIC TILE HELPERS =====
function hslFromHex(hex){{
  let r=parseInt(hex.slice(1,3),16)/255,g=parseInt(hex.slice(3,5),16)/255,b=parseInt(hex.slice(5,7),16)/255;
  const mx=Math.max(r,g,b),mn=Math.min(r,g,b),l=(mx+mn)/2;let h=0,s=0;
  if(mx!==mn){{const d=mx-mn;s=l>0.5?d/(2-mx-mn):d/(mx+mn);
    if(mx===r)h=((g-b)/d+(g<b?6:0))/6;else if(mx===g)h=((b-r)/d+2)/6;else h=((r-g)/d+4)/6;}}
  return[h*360,s*100,l*100];
}}
function hslToFill(h,s,l){{return `hsl(${{h}},${{s}}%,${{l}}%)`;}}
function drawMosaicArc(ctx,cx,cy,rInner,rOuter,a1,a2,baseColor,R){{
  const tileSize=11,groutW=1.8;
  const[bH,bS,bL]=hslFromHex(baseColor);
  const radDepth=rOuter-rInner,arcSpan=a2-a1;
  if(radDepth<2||arcSpan<0.001)return;
  const nRadial=Math.max(1,Math.round(radDepth/(tileSize+groutW)));
  const radStep=radDepth/nRadial;
  for(let ri=0;ri<nRadial;ri++){{
    const rI=rInner+ri*radStep+groutW/2,rE=rInner+(ri+1)*radStep-groutW/2;
    if(rE<=rI)continue;
    const midR=(rI+rE)/2,circ=midR*arcSpan;
    const nArc=Math.max(1,Math.round(circ/(tileSize+groutW)));
    const aStep=arcSpan/nArc;
    for(let ai=0;ai<nArc;ai++){{
      const aI=a1+ai*aStep+groutW/(2*midR),aE=a1+(ai+1)*aStep-groutW/(2*midR);
      if(aE<=aI)continue;
      const hV=bH+(R()-0.5)*6,sV=Math.max(0,Math.min(100,bS+(R()-0.5)*10)),lV=Math.max(5,Math.min(90,bL+(R()-0.5)*16));
      const jI=rI+(R()-0.5)*1.2,jE=rE+(R()-0.5)*1.2,jaI=aI+(R()-0.5)*0.001,jaE=aE+(R()-0.5)*0.001;
      ctx.beginPath();ctx.arc(cx,cy,jI,jaI,jaE);ctx.arc(cx,cy,jE,jaE,jaI,true);ctx.closePath();
      ctx.fillStyle=hslToFill(hV,sV,lV);ctx.fill();
    }}
  }}
}}
function drawDiamondBorder(ctx,cx,cy,radius,width,R){{
  const n2=90,grout='rgba(45,35,15,0.5)';
  const aStep=Math.PI*2/n2;
  for(let i=0;i<n2;i++){{
    const a=aStep*i,aMid=a+aStep/2;
    const rI=radius-width/2+1,rO2=radius+width/2-1,rM=(rI+rO2)/2;
    ctx.beginPath();
    ctx.moveTo(cx+Math.cos(a)*rM,cy+Math.sin(a)*rM);
    ctx.lineTo(cx+Math.cos(aMid)*rO2,cy+Math.sin(aMid)*rO2);
    ctx.lineTo(cx+Math.cos(a+aStep)*rM,cy+Math.sin(a+aStep)*rM);
    ctx.lineTo(cx+Math.cos(aMid)*rI,cy+Math.sin(aMid)*rI);
    ctx.closePath();
    const lV=i%2===0?35+R()*10:55+R()*10;
    const hV=i%2===0?38+R()*8:28+R()*8;
    ctx.fillStyle=`hsl(${{hV}},${{30+R()*15}}%,${{lV}}%)`;ctx.fill();
    ctx.strokeStyle=grout;ctx.lineWidth=1.2;ctx.stroke();
  }}
}}
function drawTriangleBorder(ctx,cx,cy,radius,width,R){{
  const n2=60,grout='rgba(45,35,15,0.5)';
  const aStep=Math.PI*2/n2;
  for(let i=0;i<n2;i++){{
    const a=aStep*i;
    const rI=radius-width/2+1,rO2=radius+width/2-1;
    ctx.beginPath();
    if(i%2===0){{
      ctx.moveTo(cx+Math.cos(a)*rI,cy+Math.sin(a)*rI);
      ctx.lineTo(cx+Math.cos(a+aStep/2)*rO2,cy+Math.sin(a+aStep/2)*rO2);
      ctx.lineTo(cx+Math.cos(a+aStep)*rI,cy+Math.sin(a+aStep)*rI);
    }}else{{
      ctx.moveTo(cx+Math.cos(a)*rO2,cy+Math.sin(a)*rO2);
      ctx.lineTo(cx+Math.cos(a+aStep/2)*rI,cy+Math.sin(a+aStep/2)*rI);
      ctx.lineTo(cx+Math.cos(a+aStep)*rO2,cy+Math.sin(a+aStep)*rO2);
    }}
    ctx.closePath();
    const lV=i%2===0?30+R()*12:50+R()*12;
    ctx.fillStyle=`hsl(${{40+R()*10}},${{25+R()*15}}%,${{lV}}%)`;ctx.fill();
    ctx.strokeStyle=grout;ctx.lineWidth=1;ctx.stroke();
  }}
}}
function drawZigzagBorder(ctx,cx,cy,radius,width,R){{
  const n2=120,grout='rgba(45,35,15,0.45)';
  const aStep=Math.PI*2/n2;
  for(let i=0;i<n2;i++){{
    const a=aStep*i;
    const rI=radius-width/2+1,rO2=radius+width/2-1;
    ctx.beginPath();
    if(i%2===0){{
      ctx.moveTo(cx+Math.cos(a)*rI,cy+Math.sin(a)*rI);
      ctx.lineTo(cx+Math.cos(a+aStep*0.5)*rO2,cy+Math.sin(a+aStep*0.5)*rO2);
      ctx.lineTo(cx+Math.cos(a+aStep)*rI,cy+Math.sin(a+aStep)*rI);
    }}else{{
      ctx.moveTo(cx+Math.cos(a)*rO2,cy+Math.sin(a)*rO2);
      ctx.lineTo(cx+Math.cos(a+aStep*0.5)*rI,cy+Math.sin(a+aStep*0.5)*rI);
      ctx.lineTo(cx+Math.cos(a+aStep)*rO2,cy+Math.sin(a+aStep)*rO2);
    }}
    ctx.closePath();
    const gold=i%3===0;
    const hV2=gold?42:22+R()*15;
    const sV2=gold?50+R()*15:20+R()*12;
    const lV2=gold?55+R()*10:32+R()*14;
    ctx.fillStyle=`hsl(${{hV2}},${{sV2}}%,${{lV2}}%)`;ctx.fill();
    ctx.strokeStyle=grout;ctx.lineWidth=1;ctx.stroke();
  }}
}}
function drawRosette(ctx,cx,cy,radius,R){{
  const grout='rgba(45,35,15,0.5)';
  const points=8,innerR=radius*0.35,midR=radius*0.7,outerR=radius*0.92;
  ctx.beginPath();ctx.arc(cx,cy,radius,0,Math.PI*2);
  const rG=ctx.createRadialGradient(cx,cy,10,cx,cy,radius);
  rG.addColorStop(0,'#ddd4b8');rG.addColorStop(1,'#c8bea0');
  ctx.fillStyle=rG;ctx.fill();
  for(let i=0;i<points;i++){{
    const a=Math.PI*2*i/points-Math.PI/2;
    const aNext=Math.PI*2*(i+1)/points-Math.PI/2;
    const aMid=(a+aNext)/2;
    ctx.beginPath();
    ctx.moveTo(cx+Math.cos(a)*midR,cy+Math.sin(a)*midR);
    ctx.lineTo(cx+Math.cos(aMid)*outerR,cy+Math.sin(aMid)*outerR);
    ctx.lineTo(cx+Math.cos(aNext)*midR,cy+Math.sin(aNext)*midR);
    ctx.closePath();
    ctx.fillStyle=`hsl(${{42+R()*6}},${{50+R()*15}}%,${{48+R()*12}}%)`;ctx.fill();
    ctx.strokeStyle=grout;ctx.lineWidth=1.8;ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(cx+Math.cos(a)*innerR,cy+Math.sin(a)*innerR);
    ctx.lineTo(cx+Math.cos(a)*midR,cy+Math.sin(a)*midR);
    ctx.lineTo(cx+Math.cos(aMid)*midR*0.6,cy+Math.sin(aMid)*midR*0.6);
    ctx.closePath();
    const bg=R()>0.5;
    ctx.fillStyle=bg?`hsl(${{200+R()*30}},${{40+R()*15}}%,${{25+R()*10}}%)`:`hsl(${{150+R()*30}},${{35+R()*15}}%,${{28+R()*10}}%)`;
    ctx.fill();ctx.strokeStyle=grout;ctx.lineWidth=1.5;ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(cx+Math.cos(aNext)*innerR,cy+Math.sin(aNext)*innerR);
    ctx.lineTo(cx+Math.cos(aNext)*midR,cy+Math.sin(aNext)*midR);
    ctx.lineTo(cx+Math.cos(aMid)*midR*0.6,cy+Math.sin(aMid)*midR*0.6);
    ctx.closePath();
    ctx.fillStyle=bg?`hsl(${{155+R()*30}},${{35+R()*15}}%,${{28+R()*10}}%)`:`hsl(${{205+R()*30}},${{40+R()*15}}%,${{25+R()*10}}%)`;
    ctx.fill();ctx.strokeStyle=grout;ctx.lineWidth=1.5;ctx.stroke();
  }}
  ctx.beginPath();
  for(let i=0;i<points;i++){{const a=Math.PI*2*i/points-Math.PI/2;ctx.lineTo(cx+Math.cos(a)*innerR,cy+Math.sin(a)*innerR);}}
  ctx.closePath();ctx.fillStyle=`hsl(${{40+R()*5}},${{45+R()*10}}%,${{52+R()*8}}%)`;ctx.fill();
  ctx.strokeStyle=grout;ctx.lineWidth=2;ctx.stroke();
}}

// Plaster background
const pG=ctx.createRadialGradient(cx,cy,200,cx,cy,2800);
pG.addColorStop(0,'#efe7d4');pG.addColorStop(0.5,'#ece4d0');pG.addColorStop(1,'#e4dcc4');
ctx.fillStyle=pG;ctx.fillRect(0,0,W,H);
for(let i=0;i<12000;i++){{const gx=R()*W,gy=R()*H;ctx.fillStyle=`rgba(${{60+R()*50}},${{50+R()*35}},${{15+R()*25}},${{0.008+R()*0.018}})`;ctx.fillRect(gx,gy,0.5+R()*1.5,0.5+R()*1.5);}}
for(let i=0;i<80;i++){{ctx.beginPath();const fx=R()*W,fy=R()*H;ctx.moveTo(fx,fy);ctx.lineTo(fx+R()*20-10,fy+R()*3);ctx.strokeStyle=`rgba(120,90,40,${{0.006+R()*0.008}})`;ctx.lineWidth=0.3+R()*0.4;ctx.stroke();}}
const vG=ctx.createRadialGradient(cx,cy,800,cx,cy,2900);
vG.addColorStop(0,'rgba(0,0,0,0)');vG.addColorStop(0.7,'rgba(0,0,0,0)');vG.addColorStop(1,'rgba(40,30,10,0.14)');
ctx.fillStyle=vG;ctx.fillRect(0,0,W,H);

const r0=220,r1=300,r2=780,r4i=820,r4o=890,rO=940,rL=1100;
const ap=Math.PI*2/n,sa=-Math.PI/2-ap/2,gp=0.008;

// Geometric tile borders
drawZigzagBorder(ctx,cx,cy,rO+52,18,R);
drawDiamondBorder(ctx,cx,cy,(r2+r4i)/2,16,R);
drawTriangleBorder(ctx,cx,cy,r0+10,14,R);
[r1,r2,r4i,r4o,rO].forEach(r=>{{ctx.beginPath();ctx.arc(cx,cy,r,0,Math.PI*2);ctx.strokeStyle='rgba(45,35,15,0.1)';ctx.lineWidth=1;ctx.stroke();}});

// Stained glass phase tinting
let ss=[],cs2=-1;D.forEach((d,i)=>{{if(d.s!==cs2){{ss.push({{s:d.s,i}});cs2=d.s;}}}});
ss.forEach((s2,si)=>{{
  const eI=si<ss.length-1?ss[si+1].i:n;
  const a1=sa+s2.i*ap,a2=sa+eI*ap;
  ctx.beginPath();ctx.moveTo(cx,cy);ctx.arc(cx,cy,rO-5,a1,a2);ctx.closePath();
  ctx.fillStyle=SGC[s2.s];ctx.fill();
}});

// Phase arcs — mosaic tile band
ss.forEach((s2,si)=>{{
  const eI=si<ss.length-1?ss[si+1].i:n,a1=sa+s2.i*ap,a2=sa+eI*ap;
  drawMosaicArc(ctx,cx,cy,rO,rO+50,a1+0.006,a2-0.006,SC[s2.s],R);
  // External bracket
  const bR=rO+54,bLen=18;
  ctx.strokeStyle=SC[s2.s];ctx.lineWidth=2;ctx.globalAlpha=0.6;
  ctx.beginPath();ctx.moveTo(cx+Math.cos(a1+0.012)*bR,cy+Math.sin(a1+0.012)*bR);
  ctx.lineTo(cx+Math.cos(a1+0.012)*(bR+bLen),cy+Math.sin(a1+0.012)*(bR+bLen));ctx.stroke();
  ctx.beginPath();ctx.moveTo(cx+Math.cos(a2-0.012)*bR,cy+Math.sin(a2-0.012)*bR);
  ctx.lineTo(cx+Math.cos(a2-0.012)*(bR+bLen),cy+Math.sin(a2-0.012)*(bR+bLen));ctx.stroke();
  ctx.beginPath();ctx.arc(cx,cy,bR+bLen,a1+0.012,a2-0.012);ctx.stroke();
  ctx.globalAlpha=1;
  // Phase name label
  const mA=(a1+a2)/2,pnR=rO+100;
  ctx.save();ctx.translate(cx+Math.cos(mA)*pnR,cy+Math.sin(mA)*pnR);
  const fl=mA>0.3&&mA<Math.PI*1.7;
  ctx.rotate(mA+(fl?Math.PI:0));
  ctx.font='700 48px "Fira Sans",sans-serif';ctx.fillStyle=SC[s2.s];ctx.textAlign='center';
  ctx.fillText(SN[s2.s].toUpperCase(),0,16);
  ctx.restore();
}});

// Center — geometric rosette
drawRosette(ctx,cx,cy,r0,R);
drawTriangleBorder(ctx,cx,cy,r0,12,R);
ctx.font='700 120px "Cormorant Garamond",serif';ctx.fillStyle='#1a0a02';ctx.textAlign='center';
ctx.shadowColor='rgba(230,220,190,0.7)';ctx.shadowBlur=8;
ctx.fillText('\\u05E7\\u05E2\\u05E8\\u05D4',cx,cy-10);
ctx.font='600 68px "Fira Sans",sans-serif';ctx.fillStyle='#1a2a08';
ctx.fillText(tH.toLocaleString()+' words',cx,cy+60);
ctx.font='italic 44px "Cormorant Garamond",serif';ctx.fillStyle='#2a1808';
ctx.fillText('The Passover Seder',cx,cy+116);
ctx.shadowColor='transparent';ctx.shadowBlur=0;

const hits=[];
D.forEach((d,i)=>{{
  const ang=sa+i*ap+ap/2,a1=sa+i*ap+gp,a2=sa+(i+1)*ap-gp;
  const sl=d.he<10,wF=Math.sqrt(d.he)/Math.sqrt(mH);
  const ents=Object.entries(d.mx||{{}}).filter(([k,v])=>v>0).sort((a,b)=>b[1]-a[1]);
  const bH=sl?3:(r2-r1)*wF;

  // Voice bars — mosaic tiles
  if(sl){{ctx.beginPath();ctx.arc(cx,cy,r1+1,a1,a2);ctx.arc(cx,cy,r1+5,a2,a1,true);ctx.closePath();ctx.strokeStyle='rgba(80,70,30,0.1)';ctx.lineWidth=0.8;ctx.setLineDash([3,4]);ctx.stroke();ctx.setLineDash([]);}}
  else{{let cR=r1;ents.forEach(([vk,pc])=>{{const sH=pc/100*bH,sE=cR+sH;if(sE-cR>2)drawMosaicArc(ctx,cx,cy,cR,sE,a1,a2,V[vk],R);cR=sE;}});}};

  // Era blocks — mosaic tiles
  const aE=Object.entries(d.ag||{{}}).filter(([k,v])=>v>0);
  if(aE.length>0&&!sl){{let aCu=a1;aE.forEach(([ak,av])=>{{const sp=av/100*(a2-a1);if(sp>0.002)drawMosaicArc(ctx,cx,cy,r4i,r4o,aCu,aCu+sp,AC[ak],R);aCu+=sp;}});}};

  // Labels
  const phase=d.s;const secInPhase=D.filter(x=>x.s===phase).length;
  const tiers=secInPhase>8?5:secInPhase>4?4:3;
  const labOff=[0,85,170,255,340].slice(0,tiers)[i%tiers];
  const labR=rO+150+labOff;
  const lx=cx+Math.cos(ang)*labR,ly=cy+Math.sin(ang)*labR;
  ctx.beginPath();ctx.moveTo(cx+Math.cos(ang)*(rO+120),cy+Math.sin(ang)*(rO+120));
  ctx.lineTo(cx+Math.cos(ang)*(labR-12),cy+Math.sin(ang)*(labR-12));
  ctx.strokeStyle='rgba(50,40,15,0.18)';ctx.lineWidth=1.2;ctx.stroke();
  ctx.beginPath();ctx.arc(cx+Math.cos(ang)*(rO+120),cy+Math.sin(ang)*(rO+120),2.5,0,Math.PI*2);ctx.fillStyle='rgba(50,40,15,0.25)';ctx.fill();

  ctx.save();ctx.translate(lx,ly);const fl=ang>0.35&&ang<Math.PI*1.65;
  ctx.rotate(ang+(fl?Math.PI:0));
  ctx.font=sl?'500 30px "Fira Sans",sans-serif':'700 38px "Fira Sans",sans-serif';
  ctx.fillStyle=sl?'#504030':'#0a0804';ctx.textAlign='center';ctx.fillText(d.k,0,-2);
  if(d.he>20&&!sl){{ctx.font='500 24px "Fira Sans",sans-serif';ctx.fillStyle='#504030';ctx.fillText(d.he+'w',0,26);}}
  ctx.restore();
  hits.push({{a1,a2,i}});
}});

// Ring-zone labels
ctx.font='italic 36px "Fira Sans",sans-serif';ctx.fillStyle='#403820';ctx.textAlign='center';
ctx.fillText('Voice bars',cx,cy-((r1+r2)/2));
ctx.fillText('Era',cx,cy-((r4i+r4o)/2));

// Corner mosaics
const fSz2=100,fMg2=55,cGrOut='rgba(45,35,15,0.4)';
[[fMg2,fMg2,0],[W-fMg2,fMg2,Math.PI/2],[W-fMg2,H-fMg2,Math.PI],[fMg2,H-fMg2,Math.PI*1.5]].forEach(([fx,fy,fr])=>{{
  ctx.save();ctx.translate(fx,fy);ctx.rotate(fr);
  const ts=20;
  for(let r2=0;r2<5;r2++)for(let c=0;c<5;c++){{
    if(r2+c>5)continue;
    const x=c*ts+2,y=r2*ts+2;
    const gold=(r2+c)%2===0;
    ctx.fillStyle=gold?`hsl(${{40+R()*8}},${{40+R()*15}}%,${{48+R()*12}}%)`:`hsl(${{20+R()*15}},${{20+R()*12}}%,${{32+R()*12}}%)`;
    ctx.fillRect(x,y,ts-3,ts-3);
    ctx.strokeStyle=cGrOut;ctx.lineWidth=1;ctx.strokeRect(x,y,ts-3,ts-3);
  }}
  ctx.restore();
}});

// Footer
ctx.beginPath();ctx.moveTo(cx-500,H-50);ctx.lineTo(cx+500,H-50);ctx.strokeStyle='rgba(100,80,30,0.1)';ctx.lineWidth=1;ctx.stroke();
ctx.font='italic 34px "Fira Sans",sans-serif';ctx.fillStyle='#605840';ctx.textAlign='center';
ctx.fillText('Generated from Sefaria API \\u00b7 Hover or click any section for full analysis',cx,H-20);

// HTML Stats Panel
const maxPron=Math.max(...D.map(d=>(d.we||0)+(d.you||0)+(d.he2||0)));
const statSections=D.filter(d=>(d.we||0)+(d.you||0)+(d.he2||0)>0||(d.cit||0)>0||(d.ppf||0)>0);
let sH2='<div style="font-family:Fira Sans,sans-serif">';
sH2+='<div style="font-size:18px;font-weight:700;color:#1a1008;margin-bottom:12px;text-transform:uppercase;letter-spacing:.06em">Pronouns, Citations & Prophetic Perfect</div>';
sH2+='<div style="display:grid;grid-template-columns:120px 1fr 60px 40px 30px;gap:4px 12px;align-items:center;font-size:14px">';
sH2+='<div style="font-weight:700;font-size:11px;color:#403820;text-transform:uppercase">Section</div>';
sH2+='<div style="font-weight:700;font-size:11px;color:#403820;text-transform:uppercase">Pronouns</div>';
sH2+='<div style="font-weight:700;font-size:11px;color:#403820;text-transform:uppercase;text-align:right">Total</div>';
sH2+='<div style="font-weight:700;font-size:11px;color:#403820;text-transform:uppercase;text-align:center">Cit</div>';
sH2+='<div style="font-weight:700;font-size:11px;color:#403820;text-transform:uppercase;text-align:center">PP</div>';
statSections.forEach(d=>{{
  const we=d.we||0,you=d.you||0,he2=d.he2||0,pT=we+you+he2;
  const wPct=maxPron>0?we/maxPron*100:0,yPct=maxPron>0?you/maxPron*100:0,hPct=maxPron>0?he2/maxPron*100:0;
  sH2+='<div style="font-weight:600;color:#1a1008">'+d.k+'</div>';
  sH2+='<div style="display:flex;height:18px;border-radius:3px;overflow:hidden;background:rgba(80,70,30,0.06)">';
  if(we>0)sH2+='<div style="width:'+wPct+'%;background:#1e4a6a;min-width:2px"></div>';
  if(you>0)sH2+='<div style="width:'+yPct+'%;background:#5a2060;min-width:2px"></div>';
  if(he2>0)sH2+='<div style="width:'+hPct+'%;background:#7a3508;min-width:2px"></div>';
  sH2+='</div>';
  sH2+='<div style="text-align:right;color:#302810;font-weight:600">'+(pT>0?pT:'')+'</div>';
  sH2+='<div style="text-align:center;color:#a04810;font-weight:700">'+(d.cit>0?d.cit:'')+'</div>';
  sH2+='<div style="text-align:center;color:#2e4a10;font-weight:700">'+(d.ppf>0?d.ppf:'')+'</div>';
}});
sH2+='</div>';
sH2+='<div style="display:flex;gap:16px;margin-top:10px;font-size:12px;color:#504030">';
sH2+='<span><span style="display:inline-block;width:12px;height:12px;background:#1e4a6a;border-radius:2px;vertical-align:middle;margin-right:4px"></span>we/our/us</span>';
sH2+='<span><span style="display:inline-block;width:12px;height:12px;background:#5a2060;border-radius:2px;vertical-align:middle;margin-right:4px"></span>you/your/thou</span>';
sH2+='<span><span style="display:inline-block;width:12px;height:12px;background:#7a3508;border-radius:2px;vertical-align:middle;margin-right:4px"></span>he/his/him</span>';
sH2+='</div></div>';
document.getElementById('statsPanel').innerHTML=sH2;

// Table
document.getElementById('dt').innerHTML='<tr><th>Section</th><th>Words</th><th>Rabbi%</th><th>Psalm%</th><th>Aram%</th><th>Cit</th><th>we/you/he</th><th>PP</th></tr>'+
  D.map(d=>'<tr><td><b>'+d.k+'</b></td><td>'+d.he+'</td><td>'+d.rP+'%</td><td>'+d.pP+'%</td><td>'+d.aP+'%</td><td>'+d.cit+'</td><td>'+d.we+'/'+d.you+'/'+d.he2+'</td><td>'+d.ppf+'</td></tr>').join('');

// Tooltip
const tip=document.getElementById('tip'),ti=document.getElementById('ti');
let frz=null;
function shT(d,ex,ey){{
  const es=Object.entries(d.mx||{{}}).filter(([k,v])=>v>0).sort((a,b)=>b[1]-a[1]);
  const vB=es.map(([k,v])=>'<div class="tr"><div class="trd" style="background:'+V[k]+'"></div><div class="trl">'+VN[k]+'</div><div class="trv">'+v+'% \\u00b7 ~'+Math.round(d.he*v/100)+'w</div></div>').join('')||'<div style="opacity:0.3;font-style:italic">silence</div>';
  const agB=Object.entries(d.ag||{{}}).filter(([k,v])=>v>0).map(([k,v])=>'<div class="tr"><div class="trd" style="background:'+AC[k]+'"></div><div class="trl">'+AN[k]+'</div><div class="trv">'+v+'%</div></div>').join('');
  const ns=[];
  if(d.cit>0)ns.push(d.cit+' citations');
  if(d.ppf>0)ns.push(d.ppf+' prophetic perfect');
  if(d.aP>20)ns.push(d.aP+'% Aramaic');
  const pT2=(d.we||0)+(d.you||0)+(d.he2||0);
  if(pT2>0)ns.push(pT2+' pronoun refs ('+d.we+'/'+d.you+'/'+d.he2+')');
  ti.innerHTML='<div class="tn">'+d.k+'</div><div class="td">'+d.d+'</div><div class="tg"><div><div class="tsn">'+d.he+'</div><div class="tsl">Hebrew words</div></div><div><div class="tsn">'+Math.round(d.he/tH*100)+'%</div><div class="tsl">of Haggadah</div></div><div><div class="tsn">'+pT2+'</div><div class="tsl">pronoun refs</div></div></div><div class="tsc">Voices</div>'+vB+'<div class="tsc">Composition era</div>'+agB+(ns.length?'<div class="tnt">'+ns.join(' \\u00b7 ')+'</div>':'');
  tip.style.display='block';tip.style.left=Math.min(ex+20,innerWidth-440)+'px';tip.style.top=Math.max(10,ey-30)+'px';
}}
cv.addEventListener('mousemove',function(ev){{if(frz!==null)return;const rect=cv.getBoundingClientRect(),mx=(ev.offsetX/rect.width)*W-cx,my=(ev.offsetY/rect.height)*H-cy,dist=Math.sqrt(mx*mx+my*my);let a2=Math.atan2(my,mx),hit=null;hits.forEach(h=>{{let a=a2;if(a<h.a1-0.1)a+=Math.PI*2;if(a>=h.a1&&a<=h.a2&&dist>r0&&dist<rO+400)hit=h;}});if(hit){{shT(D[hit.i],ev.clientX,ev.clientY);cv.style.cursor='pointer';}}else{{tip.style.display='none';cv.style.cursor='crosshair';}}}});
cv.addEventListener('click',function(ev){{const rect=cv.getBoundingClientRect(),mx=(ev.offsetX/rect.width)*W-cx,my=(ev.offsetY/rect.height)*H-cy,dist=Math.sqrt(mx*mx+my*my);let a2=Math.atan2(my,mx),hit=null;hits.forEach(h=>{{let a=a2;if(a<h.a1-0.1)a+=Math.PI*2;if(a>=h.a1&&a<=h.a2&&dist>r0&&dist<rO+400)hit=h;}});if(hit){{if(frz===hit.i){{frz=null;tip.style.display='none';}}else{{frz=hit.i;shT(D[hit.i],ev.clientX,ev.clientY);}}}}else{{frz=null;tip.style.display='none';}}}});
cv.addEventListener('mouseleave',()=>{{if(frz===null)tip.style.display='none';}});
</script>
</body>
</html>"""

    with open("haggadah_visualization.html", "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    run()

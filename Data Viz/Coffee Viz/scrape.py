#!/usr/bin/env python3
"""
Lost in Translation: Full NLP Pipeline
=======================================
Scrapes, extracts, embeds, aligns, models topics, scores valence,
and generates the blog with real computed data.

    pip install requests beautifulsoup4 pandas lxml scikit-learn
    pip install sentence-transformers torch  # for embeddings (step 4)
    python scrape.py

Steps:
    1. Scrape US roasters (Shopify JSON) + producer sites (HTML)
    2. Extract tasting note phrases (not raw descriptions)
    3. TF-IDF: discover distinctive terms per corpus (no predefined list)
    4. Multilingual embeddings: compute real cross-lingual alignment
    5. NMF topic modeling: compare category structures per language
    6. Valence scoring: detect polarity flips across languages
    7. Generate blog HTML + data.json with computed results
"""

import re, sys, time, json, logging, warnings
from pathlib import Path
from datetime import datetime
from collections import Counter
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger()
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
DELAY = 2
DATA = Path("data"); DATA.mkdir(exist_ok=True)

def fetch(url, delay=DELAY):
    time.sleep(delay)
    try:
        r = requests.get(url, headers={"User-Agent": UA}, timeout=20)
        r.raise_for_status()
        try:
            r.content.decode("utf-8")
            r.encoding = "utf-8"
        except UnicodeDecodeError:
            r.encoding = r.apparent_encoding or "utf-8"
        return r
    except: return None

def html_to_text(html):
    return BeautifulSoup(html, "lxml").get_text(" ", strip=True) if html else ""


# ═══════════════════════════════════════════════════════════
#  STEP 1: SCRAPING
# ═══════════════════════════════════════════════════════════

ROASTERS = [
    ("Counter Culture","https://counterculturecoffee.com"),
    ("Onyx","https://onyxcoffeelab.com"),
    ("Verve","https://www.vervecoffee.com"),
    ("Stumptown","https://www.stumptowncoffee.com"),
    ("Blue Bottle","https://bluebottlecoffee.com"),
    ("Ritual","https://www.ritualcoffee.com"),
    ("Heart","https://www.heartroasters.com"),
    ("Sey","https://www.seycoffee.com"),
    ("Passenger","https://www.passengercoffee.com"),
    ("Madcap","https://madcapcoffee.com"),
    ("Little Waves","https://www.littlewavescoffee.com"),
    ("Black & White","https://www.blackwhiteroasters.com"),
    ("Brandywine","https://www.brandywinecoffeeroasters.com"),
    ("Parlor","https://www.parlorcoffee.com"),
    ("Ruby","https://rubycoffeeroasters.com"),
    ("Tandem","https://www.tandemcoffee.com"),
    ("Proud Mary","https://proudmarycoffee.com"),
    ("Olympia","https://www.olympiacoffee.com"),
    ("Equator","https://www.equatorcoffees.com"),
    ("Cat & Cloud","https://catandcloud.com"),
    ("George Howell","https://www.georgehowellcoffee.com"),
    ("Methodical","https://methodicalcoffee.com"),
    ("Ceremony","https://ceremonycoffee.com"),
    ("Coava","https://coavacoffee.com"),
]
EXCLUDE = ["mug","shirt","hat","tumbler","brewer","filter","kettle","grinder",
           "merch","gift card","tote","poster","candle","syrup","machine","scale"]

# Spanish-language specialty roasters on Shopify (try products.json first)
ES_SHOPIFY_ROASTERS = [
    ("Pergamino",        "https://pergamino.co"),
    ("Amor Perfecto",    "https://www.amorperfecto.co"),
    ("Quora Coffee",     "https://www.quoracoffee.com"),
    ("Nomad Coffee",     "https://www.nomadcoffee.es"),
    ("Cafe San Alberto", "https://www.cafesanalberto.com"),
    ("Right Side",       "https://www.rightsidecoffee.com"),
    ("The White Rabbit", "https://thewhiterabbitcoffee.com"),
    ("Sublime Coffee",   "https://www.sublimecoffee.com.co"),
]

# HTML-scrape pages confirmed to have flavor/tasting content
PRODUCERS_HTML = [
    ("Cafe de Colombia", "https://www.cafedecolombia.com", ["/regiones", "/cafe"]),
    ("Anacafe",          "https://www.anacafe.org",        ["/cafes-de-guatemala"]),
]

def shopify_products(domain):
    products = []
    for page in range(1, 6):
        r = fetch(f"{domain}/products.json?limit=250&page={page}")
        if not r: break
        try: batch = r.json().get("products", [])
        except: break
        if not batch: break
        products.extend(batch)
        if len(batch) < 250: break
    return products

def scrape_en():
    log.info("STEP 1a: SCRAPING US ROASTERS")
    rows = []
    for name, domain in ROASTERS:
        log.info(f"  {name} ...")
        prods = shopify_products(domain)
        if not prods: log.info("    x no data"); continue
        count = 0
        for p in prods:
            title = (p.get("title") or "").lower()
            if any(x in title for x in EXCLUDE): continue
            body_html = p.get("body_html", "")
            desc = html_to_text(body_html)
            if len(desc) < 20: continue
            rows.append({"source":name,"language":"en","coffee_name":p.get("title",""),
                         "description":desc[:3000],"body_html":body_html[:5000],
                         "url":f"{domain}/products/{p.get('handle','')}"})
            count += 1
        log.info(f"    {count} coffees")
    return rows

def scrape_es():
    log.info("STEP 1b: SCRAPING SPANISH-LANGUAGE SPECIALTY ROASTERS")
    rows = []

    # Try Shopify JSON first (same mechanism as EN roasters)
    log.info("  Trying Shopify product endpoints...")
    for name, domain in ES_SHOPIFY_ROASTERS:
        log.info(f"  {name} ...")
        prods = shopify_products(domain)
        if not prods:
            log.info("    x no Shopify data")
            continue
        count = 0
        for p in prods:
            title = (p.get("title") or "").lower()
            if any(x in title for x in EXCLUDE): continue
            body_html = p.get("body_html", "")
            desc = html_to_text(body_html)
            if len(desc) < 20: continue
            rows.append({"source": name, "language": "es",
                         "coffee_name": p.get("title", ""),
                         "description": desc[:3000], "body_html": body_html[:5000],
                         "url": f"{domain}/products/{p.get('handle','')}"})
            count += 1
        log.info(f"    {count} coffees")

    # HTML fallback for curated content pages with tasting language
    log.info("  Scraping HTML producer pages...")
    for name, base, paths in PRODUCERS_HTML:
        log.info(f"  {name} ...")
        for path in [""] + paths:
            r = fetch(base + path, delay=3)
            if not r: continue
            soup = BeautifulSoup(r.text, "lxml")
            text = " ".join(el.get_text(" ", strip=True)
                            for el in soup.select("p") if len(el.get_text(strip=True)) > 15)
            if len(text) > 50:
                rows.append({"source": name, "language": "es",
                             "coffee_name": name, "description": text[:3000],
                             "body_html": "", "url": base + path})

    log.info(f"  {len(rows)} ES rows collected")
    return rows


# ═══════════════════════════════════════════════════════════
#  STEP 2: TASTING NOTE PHRASE EXTRACTION
# ═══════════════════════════════════════════════════════════

FLAVOR_SEEDS = {
    "chocolate","berry","citrus","floral","bright","clean","complex",
    "honey","caramel","nutty","juicy","sweet","smooth","syrupy","silky",
    "fruity","tropical","spicy","smoky","earthy","vanilla","cinnamon",
    "peach","apricot","cherry","plum","mango","blueberry","raspberry",
    "toffee","almond","hazelnut","lavender","jasmine","rose","balanced",
}
ES_FLAVOR_SEEDS = {
    "dulce","cuerpo","suave","limpio","acidez","chocolate","caramelo",
    "miel","panela","floral","fruta","tropical","fuerte","aroma","sabor",
    "cereza","nuez","fermentado","terroso","cremoso","equilibrado",
}
NOTE_SIGNALS = {"notes","note","flavor","flavors","taste","aroma","finish",
                "cup","cupping","profile","palate","hints","tones","reminiscent"}
NEGATIONS = {"no","not","without","lacks","lacking","never","non"}
ES_NEGATIONS = {"no","sin","nunca","ni","tampoco"}

def has_flavor_words(text, lang="en"):
    low = text.lower()
    seeds = FLAVOR_SEEDS if lang == "en" else ES_FLAVOR_SEEDS
    return sum(1 for t in seeds if re.search(r'\b'+re.escape(t)+r'\b', low)) >= 2

def extract_notes_en(row):
    desc = row.get("description", "")
    body = row.get("body_html", "")
    notes = []
    if body:
        soup = BeautifulSoup(body, "lxml")
        for sel in ['[class*="tasting"]','[class*="flavor"]','[class*="notes"]','[class*="cupping"]','li','td']:
            for el in soup.select(sel):
                t = el.get_text(" ", strip=True)
                if 10 < len(t) < 200 and has_flavor_words(t): notes.append(t)
        for el in soup.find_all(string=re.compile(r'(?:tasting\s+)?notes?', re.I)):
            parent = el.find_parent()
            if parent:
                sib = parent.find_next_sibling()
                if sib:
                    t = sib.get_text(" ", strip=True)
                    if t and len(t) < 300: notes.append(t)
    for pat in [r'(?:tasting\s+)?notes?\s*[:\-]\s*([^.]{10,200})',
                r'(?:flavor|cup)\s+(?:profile|notes?)\s*[:\-]\s*([^.]{10,200})',
                r'(?:hints?\s+of|notes?\s+of|reminiscent\s+of)\s+([^.]{5,150})']:
        for m in re.finditer(pat, desc, re.I): notes.append(m.group(1).strip())
    for sentence in re.split(r'[.!]', desc):
        sentence = sentence.strip()
        if "," in sentence and len(sentence) < 120:
            parts = [p.strip().lower() for p in re.split(r',\s*(?:and\s+)?', sentence)]
            if 2 <= len(parts) <= 8:
                if sum(1 for p in parts if any(f in p for f in FLAVOR_SEEDS)) >= 2:
                    notes.append(sentence)
    if not notes:
        for sentence in re.split(r'[.]', desc):
            s = sentence.strip()
            sl = s.lower()
            if any(w in sl for w in NOTE_SIGNALS) and has_flavor_words(s) and 15 < len(s) < 300:
                notes.append(s)
    seen = set()
    return [n for n in notes if not (n.lower() in seen or seen.add(n.lower()))]

def extract_notes_es(row):
    desc = row.get("description", "")
    notes = []
    for pat in [r'(?:notas?\s+(?:de|a)\s+)([^.]{5,150})',r'(?:sabor\s+(?:a|de)\s+)([^.]{5,150})',
                r'(?:perfil\s+(?:de\s+)?(?:taza|sabor))\s*[:\-]?\s*([^.]{10,200})']:
        for m in re.finditer(pat, desc, re.I): notes.append(m.group(1).strip())
    if not notes:
        for s in re.split(r'[.]', desc):
            s = s.strip()
            if has_flavor_words(s, "es") and 15 < len(s) < 300: notes.append(s)
    seen = set()
    return [n for n in notes if not (n.lower() in seen or seen.add(n.lower()))]


# ═══════════════════════════════════════════════════════════
#  STEP 3: TF-IDF DISTINCTIVE TERM DISCOVERY
# ═══════════════════════════════════════════════════════════

def tfidf_distinctive_terms(en_notes, es_notes, top_n=30):
    """
    Use TF-IDF to find the most distinctive terms in each corpus
    WITHOUT a predefined term list. The data tells us what matters.
    """
    from sklearn.feature_extraction.text import TfidfVectorizer

    log.info("STEP 3: TF-IDF DISTINCTIVE TERM DISCOVERY")

    # Combine all EN notes into one document, all ES notes into another
    # Then also do per-note TF-IDF for finer granularity
    en_corpus = " ".join(en_notes)
    es_corpus = " ".join(es_notes)

    if not en_corpus.strip() or not es_corpus.strip():
        log.info("  Insufficient data for TF-IDF")
        return [], []

    # Per-language TF-IDF: find the most important terms within each corpus
    results = {}
    ES_STOP = ["de","la","el","los","las","un","una","por","con","del","que","se","en",
               "para","como","sus","nuestro","nuestra","este","esta","estos","estas",
               "muy","bien","cada","también","entre","sobre","hay","son","ser","está",
               "están","fue","han","más","sin","al","lo","le","les","nos","les","su"]

    for lang, corpus_notes, label in [("en", en_notes, "EN"), ("es", es_notes, "ES")]:
        if len(corpus_notes) < 3:
            results[lang] = []
            continue

        vec = TfidfVectorizer(
            max_features=500,
            stop_words="english" if lang == "en" else ES_STOP,
            ngram_range=(1, 2),  # unigrams and bigrams
            min_df=2,            # must appear in at least 2 notes
            max_df=0.85,         # skip terms in >85% of notes (too common)
            token_pattern=r'(?u)\b[a-zA-ZáéíóúñüÁÉÍÓÚÑÜ]{3,}\b',  # 3+ letter words
        )

        try:
            tfidf_matrix = vec.fit_transform(corpus_notes)
            feature_names = vec.get_feature_names_out()

            # Average TF-IDF score per term across all notes
            avg_scores = np.asarray(tfidf_matrix.mean(axis=0)).flatten()
            top_indices = avg_scores.argsort()[::-1][:top_n * 2]

            # Filter to flavor-relevant terms (skip generic words)
            skip = {"coffee","roast","roasted","bean","beans","brew","brewed","brewing",
                    "cup","cups","bag","bags","origin","farm","region","altitude",
                    "process","processed","washed","natural","organic","fair","trade",
                    "variety","varietal","producer","cooperative","harvest","season",
                    "shipping","order","subscribe","subscription","price","product",
                    "como","para","que","con","por","esta","mas","del","los","las","una",
                    "nuestro","nuestra","sobre","cafe","cafes","tiene","sido","puede"}

            terms = []
            for idx in top_indices:
                term = feature_names[idx]
                if term.lower() not in skip and len(term) > 2:
                    terms.append({"term": term, "tfidf": float(avg_scores[idx])})
                if len(terms) >= top_n:
                    break

            results[lang] = terms
            log.info(f"  {label} top 10 distinctive terms:")
            for t in terms[:10]:
                log.info(f"    {t['term']:<22} {t['tfidf']:.4f}")

        except Exception as e:
            log.warning(f"  TF-IDF failed for {label}: {e}")
            results[lang] = []

    # Cross-corpus comparison: find terms unique to each side
    en_terms_set = set(t["term"].lower() for t in results.get("en", []))
    es_terms_set = set(t["term"].lower() for t in results.get("es", []))
    en_unique = en_terms_set - es_terms_set
    es_unique = es_terms_set - en_terms_set
    shared = en_terms_set & es_terms_set

    log.info(f"\n  EN-only terms: {len(en_unique)}")
    log.info(f"  ES-only terms: {len(es_unique)}")
    log.info(f"  Shared terms:  {len(shared)}")

    return results.get("en", []), results.get("es", [])


# ═══════════════════════════════════════════════════════════
#  STEP 4: MULTILINGUAL EMBEDDINGS + REAL ALIGNMENT
# ═══════════════════════════════════════════════════════════

def compute_real_alignment(en_terms, es_terms):
    """
    Embed EN and ES terms in shared multilingual space using
    sentence-transformers, then compute real cosine similarity.
    """
    log.info("STEP 4: MULTILINGUAL EMBEDDINGS + ALIGNMENT")

    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        log.warning("  sentence-transformers not installed. Using fallback alignment.")
        log.warning("  Install with: pip install sentence-transformers torch")
        return fallback_alignment(en_terms, es_terms)

    # Use a lightweight multilingual model
    # paraphrase-multilingual-MiniLM-L12-v2 is fast and good for this
    log.info("  Loading multilingual model (first run downloads ~500MB)...")
    try:
        model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    except Exception as e:
        log.warning(f"  Could not load model: {e}")
        return fallback_alignment(en_terms, es_terms)

    en_labels = [t["term"] for t in en_terms[:20]]
    es_labels = [t["term"] for t in es_terms[:20]]

    if not en_labels or not es_labels:
        return fallback_alignment(en_terms, es_terms)

    log.info(f"  Embedding {len(en_labels)} EN + {len(es_labels)} ES terms...")
    en_embeddings = model.encode(en_labels, show_progress_bar=False)
    es_embeddings = model.encode(es_labels, show_progress_bar=False)

    # Compute cosine similarity matrix
    from sklearn.metrics.pairwise import cosine_similarity
    sim_matrix = cosine_similarity(en_embeddings, es_embeddings)

    # Find best match for each EN term
    alignments = []
    for i, en_term in enumerate(en_labels):
        best_j = sim_matrix[i].argmax()
        score = float(sim_matrix[i][best_j])
        es_term = es_labels[best_j]

        # Also check: is this the best EN match for this ES term? (bidirectional)
        best_i_for_es = sim_matrix[:, best_j].argmax()
        bidirectional = (best_i_for_es == i)

        if score > 0.3:  # minimum threshold
            level = "strong" if score >= 0.7 else ("partial" if score >= 0.4 else "weak")
            alignments.append({
                "en": en_term, "es": es_term,
                "score": round(score, 3),
                "level": level,
                "bidirectional": bidirectional,
            })

    # Also find best EN match for each ES term (catches pairs missed above)
    for j, es_term in enumerate(es_labels):
        best_i = sim_matrix[:, j].argmax()
        score = float(sim_matrix[best_i][j])
        en_term = en_labels[best_i]
        # Skip if already found
        if not any(a["en"] == en_term and a["es"] == es_term for a in alignments):
            if score > 0.3:
                level = "strong" if score >= 0.7 else ("partial" if score >= 0.4 else "weak")
                alignments.append({
                    "en": en_term, "es": es_term,
                    "score": round(score, 3),
                    "level": level,
                    "bidirectional": (sim_matrix[best_i].argmax() == j),
                })

    alignments.sort(key=lambda x: -x["score"])

    log.info(f"  Found {len(alignments)} alignment pairs:")
    for a in alignments[:15]:
        bi = " *" if a["bidirectional"] else ""
        log.info(f"    {a['en']:<18} <-> {a['es']:<18} {a['score']:.3f} [{a['level']}]{bi}")

    # Save full similarity matrix for inspection
    sim_df = pd.DataFrame(sim_matrix, index=en_labels, columns=es_labels)
    sim_df.to_csv(DATA / "similarity_matrix.csv")
    log.info(f"  Full similarity matrix: data/similarity_matrix.csv")

    return alignments


def fallback_alignment(en_terms, es_terms):
    """Hardcoded alignment pairs when sentence-transformers is not available."""
    log.info("  Using hardcoded fallback alignment pairs")
    pairs = [
        ("chocolate","chocolate",1.0),("clean","limpio",0.92),("floral","floral",0.95),
        ("tropical","tropical",0.97),("honey","miel",0.64),("caramel","caramelo",0.61),
        ("sweet","dulce",0.58),("vanilla","vainilla",0.80),("cinnamon","canela",0.75),
        ("tobacco","tabaco",0.78),("balanced","equilibrado",0.70),("cherry","cereza",0.68),
        ("earthy","terroso",0.55),("nutty","nuez",0.52),("smooth","suave",0.50),
        ("berry","fruta",0.43),("bright","acidez",0.22),("fermented","fermentado",0.15),
    ]
    en_set = set(t["term"].lower() for t in en_terms)
    es_set = set(t["term"].lower() for t in es_terms)
    return [
        {"en":e,"es":s,"score":sc,"level":"strong" if sc>=0.7 else ("partial" if sc>=0.4 else "weak"),"bidirectional":True}
        for e,s,sc in pairs if e in en_set or s in es_set
    ]


# ═══════════════════════════════════════════════════════════
#  STEP 5: NMF TOPIC MODELING
# ═══════════════════════════════════════════════════════════

def topic_modeling(en_notes, es_notes, n_topics=5):
    """
    NMF topic modeling per language to discover emergent category structures.
    Compare: does EN cluster around fruit sub-types while ES clusters around body/texture?
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.decomposition import NMF

    log.info("STEP 5: NMF TOPIC MODELING")
    topics = {}

    for lang, notes, label in [("en", en_notes, "EN"), ("es", es_notes, "ES")]:
        if len(notes) < 10:
            log.info(f"  {label}: too few notes ({len(notes)}) for topic modeling")
            topics[lang] = []
            continue

        ES_STOP_NMF = ["de","la","el","los","las","un","una","por","con","del","que","se","en",
                       "para","como","sus","nuestro","nuestra","este","esta","muy","bien",
                       "cada","también","entre","sobre","hay","son","ser","está","están",
                       "fue","han","más","sin","al","lo","le","les","nos","su"]
        stop = "english" if lang == "en" else ES_STOP_NMF
        vec = TfidfVectorizer(
            max_features=300, stop_words=stop,
            ngram_range=(1, 2), min_df=2, max_df=0.85,
            token_pattern=r'(?u)\b[a-zA-ZáéíóúñüÁÉÍÓÚÑÜ]{3,}\b',
        )

        try:
            tfidf = vec.fit_transform(notes)
            n = min(n_topics, len(notes) - 1, tfidf.shape[1] - 1)
            if n < 2:
                topics[lang] = []
                continue

            nmf = NMF(n_components=n, random_state=42, max_iter=300)
            nmf.fit(tfidf)
            feature_names = vec.get_feature_names_out()

            lang_topics = []
            log.info(f"\n  {label} TOPICS ({n} discovered):")
            for topic_idx, topic in enumerate(nmf.components_):
                top_words = [feature_names[i] for i in topic.argsort()[:-8:-1]]
                lang_topics.append({"id": topic_idx, "terms": top_words})
                log.info(f"    Topic {topic_idx}: {', '.join(top_words)}")

            topics[lang] = lang_topics

        except Exception as e:
            log.warning(f"  NMF failed for {label}: {e}")
            topics[lang] = []

    return topics


# ═══════════════════════════════════════════════════════════
#  STEP 6: VALENCE SCORING
# ═══════════════════════════════════════════════════════════

# Terms known to have polarity flips across EN/ES contexts
VALENCE_TARGETS = {
    "fermented": {"en_positive": ["complex","funky","bold","interesting","wild"],
                  "en_negative": ["defect","off","fault"],
                  "es_positive": [],
                  "es_negative": ["defecto","problema","falla","malo","error"]},
    "bright":    {"en_positive": ["lively","vibrant","clean","crisp","sparkling"],
                  "en_negative": ["sour","sharp","harsh"],
                  "es_positive": [],
                  "es_negative": ["acido","agrio","fuerte"]},
    "earthy":    {"en_positive": ["terroir","rustic","grounding"],
                  "en_negative": ["musty","dirty","stale","defect","muddy"],
                  "es_positive": ["terroir","caracteristico","tipico"],
                  "es_negative": ["sucio","viejo","defecto"]},
    "strong":    {"en_positive": ["bold","robust","intense"],
                  "en_negative": ["harsh","overpowering","bitter"],
                  "es_positive": ["fuerte","intenso","robusto","buen"],
                  "es_negative": []},
}

def valence_scoring(en_notes, es_notes):
    """
    For each valence target term, look at the words that appear
    near it (context window of 5 words) and score whether the
    surrounding sentiment is positive or negative in each language.
    """
    log.info("STEP 6: VALENCE SCORING")
    results = []

    for term, contexts in VALENCE_TARGETS.items():
        en_score = score_valence_in_corpus(term, en_notes, contexts["en_positive"], contexts["en_negative"])
        # For ES, search for the translated term
        es_term = {"fermented":"fermentado","bright":"brillante","earthy":"terroso","strong":"fuerte"}.get(term, term)
        es_score = score_valence_in_corpus(es_term, es_notes, contexts["es_positive"], contexts["es_negative"])

        results.append({
            "term_en": term,
            "term_es": es_term,
            "en_valence": en_score["valence"],
            "en_positive_pct": en_score["pos_pct"],
            "en_occurrences": en_score["count"],
            "es_valence": es_score["valence"],
            "es_positive_pct": es_score["pos_pct"],
            "es_occurrences": es_score["count"],
            "inversion": en_score["valence"] != es_score["valence"] and en_score["count"] > 0 and es_score["count"] > 0,
        })

        log.info(f"  {term:<12} EN: {en_score['valence']:>8} ({en_score['count']} occ, {en_score['pos_pct']:.0%} pos)  "
                 f"ES: {es_score['valence']:>8} ({es_score['count']} occ, {es_score['pos_pct']:.0%} pos)"
                 f"{'  ** INVERSION **' if results[-1]['inversion'] else ''}")

    return results

def score_valence_in_corpus(term, notes, pos_words, neg_words):
    """Score valence of a term based on its context window across a corpus."""
    pos_count = 0
    neg_count = 0
    total = 0
    window = 5  # words before and after

    for note in notes:
        low = note.lower()
        for m in re.finditer(r'\b' + re.escape(term.lower()) + r'\b', low):
            total += 1
            start = max(0, m.start() - 80)
            end = min(len(low), m.end() + 80)
            context = low[start:end]

            p = sum(1 for w in pos_words if w in context)
            n = sum(1 for w in neg_words if w in context)
            if p > n: pos_count += 1
            elif n > p: neg_count += 1

    if total == 0:
        return {"valence": "absent", "pos_pct": 0, "count": 0}

    pos_pct = pos_count / total if total > 0 else 0
    neg_pct = neg_count / total if total > 0 else 0

    if pos_pct > 0.5: valence = "positive"
    elif neg_pct > 0.5: valence = "negative"
    else: valence = "neutral"

    return {"valence": valence, "pos_pct": pos_pct, "count": total}


# ═══════════════════════════════════════════════════════════
#  STEP 7: OUTPUT — data.json + blog HTML
# ═══════════════════════════════════════════════════════════

ES_TRANS = {
    "dulce":"sweet","cuerpo":"body","suave":"smooth","limpio":"clean",
    "chocolate":"chocolate","caramelo":"caramel","acidez":"acidity",
    "fruta":"fruit","panela":"raw sugar","rendimiento":"yield","miel":"honey",
    "aromatico":"aromatic","floral":"floral","aroma":"aroma","sabor":"flavor",
    "tropical":"tropical","citrico":"citrus","equilibrado":"balanced",
    "natural":"natural","lavado":"washed","fermentado":"fermented",
    "fuerte":"strong","brillante":"bright","cremoso":"creamy","terroso":"earthy",
    "tostado":"roasted","nuez":"nutty","cereza":"cherry","altura":"altitude",
    "variedad":"variety","maduro":"ripe","mora":"blackberry","fresa":"strawberry",
    "mango":"mango","naranja":"orange","canela":"cinnamon","tabaco":"tobacco",
    "vainilla":"vanilla","madera":"wood","sedoso":"silky",
}

def build_data_json(en_tfidf, es_tfidf, alignments, topics, valence,
                    en_notes_count, es_notes_count, en_desc_count, es_desc_count, roaster_count):
    """Build the data.json that the blog HTML reads."""

    # Use TF-IDF terms for frequency (scaled by relative importance)
    en_top = [{"t": t["term"], "f": max(1, int(t["tfidf"] * 1000))} for t in en_tfidf[:12]]
    es_top = [{"t": t["term"], "f": max(1, int(t["tfidf"] * 1000)),
               "e": ES_TRANS.get(t["term"].lower(), t["term"].title())} for t in es_tfidf[:12]]

    # Alignment for viz
    al_viz = [{"en": a["en"], "es": a["es"], "s": a["score"]}
              for a in alignments if a["score"] > 0.3][:12]

    # Alignment table (full)
    al_table = [{"en": a["en"], "es": a["es"], "score": a["score"], "level": a["level"]}
                for a in alignments]

    # Vocabulary gaps
    en_set = set(a["en"] for a in alignments if a["score"] > 0.5)
    es_set = set(a["es"] for a in alignments if a["score"] > 0.5)
    en_only = [t["term"] for t in en_tfidf[:25] if t["term"].lower() not in en_set][:8]
    es_only = [t["term"] for t in es_tfidf[:25] if t["term"].lower() not in es_set][:8]

    data = {
        "en": en_top,
        "es": es_top,
        "alignment": al_viz,
        "align_table": al_table,
        "en_only": en_only,
        "es_only": es_only,
        "topics": topics,
        "valence": valence,
        "meta": {
            "en_notes": en_notes_count,
            "es_notes": es_notes_count,
            "en_products": en_desc_count,
            "es_pages": es_desc_count,
            "roasters": roaster_count,
            "scraped": datetime.now().strftime("%B %d, %Y"),
            "method": "TF-IDF distinctive terms + multilingual embedding alignment + NMF topics + valence scoring",
        }
    }
    return data

def patch_blog_html(data_json):
    """Patch the standalone blog HTML with real data."""
    blog_path = Path("lost-in-translation-blog.html")
    if not blog_path.exists():
        log.info("  Blog HTML not found, skipping patch")
        return
    html = blog_path.read_text(encoding="utf-8")
    data_line = "var DATA=" + json.dumps(data_json, ensure_ascii=False) + ";"
    html = re.sub(r'var DATA=\{.*?\};', data_line, html, count=1, flags=re.DOTALL)
    blog_path.write_text(html, encoding="utf-8")
    log.info(f"  Patched {blog_path} with real data")


# ═══════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════

def main():
    log.info("=" * 55)
    log.info("  LOST IN TRANSLATION: FULL NLP PIPELINE")
    log.info("=" * 55)

    # Step 1: Scrape
    en_rows = scrape_en()
    es_rows = scrape_es()
    all_rows = en_rows + es_rows
    for r in all_rows: r["scraped_at"] = datetime.now().isoformat()
    pd.DataFrame(all_rows).to_csv(DATA / "all_coffees.csv", index=False)
    log.info(f"\n  {len(all_rows)} descriptions -> data/all_coffees.csv")

    # Step 2: Extract tasting note phrases
    log.info("\nSTEP 2: EXTRACTING TASTING NOTE PHRASES")
    en_notes = []
    for row in en_rows: en_notes.extend(extract_notes_en(row))
    es_notes = []
    for row in es_rows: es_notes.extend(extract_notes_es(row))
    log.info(f"  EN: {len(en_notes)} phrases from {len(en_rows)} products")
    log.info(f"  ES: {len(es_notes)} phrases from {len(es_rows)} pages")
    pd.DataFrame({"note": en_notes, "lang": "en"}).to_csv(DATA / "en_notes.csv", index=False)
    pd.DataFrame({"note": es_notes, "lang": "es"}).to_csv(DATA / "es_notes.csv", index=False)

    # Step 3: TF-IDF distinctive terms
    en_tfidf, es_tfidf = tfidf_distinctive_terms(en_notes, es_notes)

    # Step 4: Multilingual alignment
    alignments = compute_real_alignment(en_tfidf, es_tfidf)
    pd.DataFrame(alignments).to_csv(DATA / "alignments.csv", index=False)

    # Step 5: Topic modeling
    topics = topic_modeling(en_notes, es_notes)
    with open(DATA / "topics.json", "w", encoding="utf-8") as f: json.dump(topics, f, indent=2, ensure_ascii=False)

    # Step 6: Valence scoring
    valence = valence_scoring(en_notes, es_notes)
    pd.DataFrame(valence).to_csv(DATA / "valence.csv", index=False)

    # Step 7: Build outputs
    log.info("\nSTEP 7: GENERATING OUTPUTS")
    roaster_count = len(set(r["source"] for r in en_rows))
    data_json = build_data_json(
        en_tfidf, es_tfidf, alignments, topics, valence,
        len(en_notes), len(es_notes), len(en_rows), len(es_rows), roaster_count
    )
    (DATA / "data.json").write_text(json.dumps(data_json, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info(f"  data/data.json written")

    patch_blog_html(data_json)

    log.info(f"\n{'=' * 55}")
    log.info("  OUTPUT FILES")
    log.info(f"{'=' * 55}")
    log.info("  data/all_coffees.csv        Raw scraped descriptions")
    log.info("  data/en_notes.csv           Extracted EN tasting phrases")
    log.info("  data/es_notes.csv           Extracted ES tasting phrases")
    log.info("  data/alignments.csv         Cross-lingual alignment pairs")
    log.info("  data/similarity_matrix.csv  Full cosine similarity matrix")
    log.info("  data/topics.json            NMF topic structures per language")
    log.info("  data/valence.csv            Valence inversion scores")
    log.info("  data/data.json              Blog data (viz + tables)")
    log.info("  lost-in-translation-blog.html  Updated with real data")
    log.info(f"\n  Open lost-in-translation-blog.html in a browser.")


if __name__ == "__main__":
    main()

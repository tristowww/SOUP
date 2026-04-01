# Lost in Translation — Visualization Lookbook

**A concept mockup for Loom Coffee Co.**
*Teresa Ristow × Loom Coffee Co.*

---

## What This Is

This is a **concept prototype** — not a finished piece. The HTML file (`loom-all-12-viz.html`) contains 12 interactive data visualization options that could be used to tell the story of how coffee flavor language changes, misaligns, and sometimes inverts as it crosses linguistic and cultural borders in the specialty coffee supply chain.

**All data shown is illustrative mock data.** The numbers, frequencies, and alignments are plausible estimates used to demonstrate how each visualization type would look and feel with real data. The next step is to scrape and analyze actual tasting note language from the sources identified below.

## The Story We're Telling

Specialty coffee has built an entire sensory lexicon — largely codified through the SCA Flavor Wheel and Western cupping protocols — that gets applied universally regardless of where coffee is grown. But producers in Colombia, Guatemala, Honduras, and Ethiopia describing their own coffee use different conceptual frames, different priorities, and sometimes attach opposite emotional weight to the same terms.

This project explores three layers of that misalignment:

1. **Vocabulary gaps** — terms that exist in one language but have no equivalent in the other ("complex," "juicy," "panela," "rendimiento")
2. **Category differences** — English hyper-specifies fruit (blueberry, raspberry, meyer lemon) while Spanish uses broad categories; Spanish foregrounds sweetness and body while English prizes complexity and acidity
3. **Valence inversions** — the same word carries positive connotations in one context and negative in another ("fermented," "bright," "earthy," "strong")

## The 12 Visualization Options

Each visualization tells a different facet of the story. They are designed to be mixed and matched for a blog post, not used all at once.

| # | Name | Type | Best For |
|---|------|------|----------|
| 01 | **Woven Threads** | Canvas / generative | Hero visual — the loom/textile metaphor |
| 02 | **Force Network** | Canvas / physics sim | Deep interactive exploration |
| 03 | **Radial Bridge** | SVG | Clear structural comparison |
| 04 | **Supply Chain Flow** | Canvas | Narrative storytelling |
| 05 | **Dot Frequency** | Canvas | Quantitative scale and pattern |
| 06 | **Valence Divergence** | Canvas / scroll-triggered | The "aha moment" — same word, opposite feeling |
| 07 | **Bump Chart** | Canvas | Priority/rank gaps between languages |
| 08 | **Scatter Bubble** | Canvas | Correlation and the diagonal gap |
| 09 | **Category Heatmap** | Canvas | Structural differences at category level |
| 10 | **Waffle Grid** | Canvas | Proportional feel |
| 11 | **Vocabulary Venn** | Canvas | The big picture — simplest summary |
| 12 | **Beeswarm** | Canvas | Distribution shape |

### Recommended Combinations for Blog Post

- **Short post (3 viz):** Vocabulary Venn → Supply Chain Flow → Valence Divergence
- **Medium post (5 viz):** Vocabulary Venn → Woven Threads → Bump Chart → Supply Chain Flow → Valence Divergence
- **Deep dive (8+ viz):** Use the full set as a scrollytelling piece

## Where to Scrape the Real Data

### English (US Roaster / Importer) Sources

| Source | What to Scrape | Est. Volume | Method |
|--------|---------------|-------------|--------|
| US roaster websites (~50 roasters) | Bag descriptions, offering pages, tasting notes | ~2,000–4,000 notes | BeautifulSoup / Scrapy per-site |
| Royal Coffee "The Crown" | Green coffee lot listings with cupping notes | ~500–1,000 lots | Scrape offering archive |
| Cafe Imports | Lot detail pages with flavor descriptors | ~500–800 lots | Scrape catalog pages |
| Genuine Origin | Offering pages with sensory descriptions | ~300–500 lots | Scrape product listings |
| Ally Coffee | Lot listings with tasting notes | ~300–500 lots | Scrape catalog |
| Coffee Review | Professional cupping reviews with scores | ~2,000+ reviews | Scrape review archive (check ToS) |
| SCA Flavor Wheel | Canonical taxonomy of ~110 terms | Reference set | Manual entry / existing datasets |

### Spanish (Producer / Cooperative) Sources

| Source | What to Scrape | Est. Volume | Method |
|--------|---------------|-------------|--------|
| Cup of Excellence (cupofexcellence.org) | Bilingual jury notes — best cross-lingual source | ~1,500 entries | Scrape competition archives |
| Colombian cooperative sites | Producer descriptions in Spanish | ~300–500 | Scrape individual coop sites |
| Guatemalan cooperative sites (Anacafé members) | Farm and lot descriptions | ~200–400 | Scrape member listings |
| Honduran cooperative sites (IHCAFE members) | Producer marketing copy | ~200–300 | Scrape member listings |
| Federación Nacional de Cafeteros (Colombia) | Quality resources, educational materials | Qualitative | Scrape resource pages |
| Exporter catalogs (Volcafe, Expocafé) | Spanish-language lot descriptions | ~300–500 | Scrape catalog archives |

### Cross-Lingual and Supplementary Sources

| Source | Purpose | Notes |
|--------|---------|-------|
| World Coffee Research | Sensory science, variety descriptors | Academic supplement |
| Ethnobotanical literature | How producers describe flavor outside cupping | Qualitative — library access |
| Bilingual cupping forms | Direct translation artifacts | Request from Q-graders |
| Consumer reviews (Amazon, Reddit) | How retail consumers describe coffee | Contrast with specialty language |

## Analysis Pipeline

```
01 SCRAPE       → Python, Scrapy, BeautifulSoup
02 CLEAN        → spaCy, pandas, regex — deduplicate, tokenize, normalize synonyms
03 EXTRACT      → Custom NER for flavor terms, map to SCA taxonomy, tag language + source
04 ALIGN        → Multilingual embeddings (LABSE / mSBERT), cosine similarity, manual validation
05 SCORE        → Frequency counts, category aggregation, valence scoring per context
06 VISUALIZE    → D3.js, p5.js, or Observable — swap mock data arrays for real pipeline output
```

## How to Use This File

1. Open `loom-all-12-viz.html` in any modern browser
2. Scroll through all 12 visualizations — each lazy-loads when you reach it
3. Hover to interact with tooltips and highlighting
4. Use the sticky nav at the top to jump between visualizations
5. All visualizations are self-contained in the single HTML file (no dependencies except Google Fonts CDN)

## Technical Notes

- All visualizations render on HTML Canvas (except Radial Bridge which uses SVG)
- Lazy initialization via IntersectionObserver — only the visible canvas runs its draw loop
- The Force Network is the only continuously animated visualization; all others redraw on mouse events only
- High-contrast Loom-branded color palette: blue (#0b6d8c) for EN, terracotta (#c43a18) for ES, gold (#a07418) for cross-lingual links, green (#2e7228) for strong alignment
- Typography: Fraunces (serif headers), DM Sans (body), DM Mono (data labels) — selected to complement Loom's brand aesthetic

## Next Steps

1. **Pick 3–5 visualizations** for the blog post based on narrative priorities
2. **Build the scraping pipeline** starting with the easiest, richest sources (roaster sites + Cup of Excellence)
3. **Run NLP extraction** to generate real frequency counts and category tags
4. **Replace mock data arrays** in the HTML with pipeline output
5. **Write the blog narrative** around the real findings
6. **Coordinate with Andrew** (Loom's Head of Design) on final visual polish and brand alignment

---

*This project sits at the intersection of NLP, cross-cultural semantics, and data visualization — exploring how the language of coffee flavor serves (and sometimes fails) the people who grow it.*

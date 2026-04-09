# SCA Documentation Reference Agent

This directory contains the official SCA Coffee Value Assessment (CVA) system documentation. These are the authoritative standards for how specialty coffee quality is defined, evaluated, and communicated industry-wide. The CVA system replaced the legacy SCA cupping form (the 100-point scoring sheet) starting in 2024.

---

## Document Inventory

| File | Type | Year | Scope |
|---|---|---|---|
| `SCA-A-System-to-Assess-Coffee-Value-2024.md` | Framework overview | 2024 | The master document. Explains the full CVA system: why it was created, how the three assessment types (descriptive, affective, extrinsic) work together, and how they replace the single-score model. Start here. |
| `Attributes-Framework-Whitepaper-2021.md` | Research paper | 2021 | The foundational science. Defines the attributes-based approach to coffee evaluation, the research methodology, and the theoretical framework underlying the CVA. |
| `CVAS-Evolution-Report-2022.md` | Evolution report | 2022 | How the system developed from the legacy form. Documents the research process, stakeholder input, and design decisions that shaped the CVA. |
| `SCA-102-Sample-Preparation-2024.md` | Standard | 2024 | Protocol for preparing coffee samples for any SCA evaluation. Roast levels, resting time, water parameters, serving temperature, equipment requirements. |
| `SCA-103-Descriptive-Assessment-2024.md` | Standard | 2024 | The sensory vocabulary and methodology for describing what a coffee tastes like. Aroma, flavor, aftertaste, acidity, body, balance, uniformity, clean cup. Replaces the descriptive components of the old cupping form. |
| `SCA-104-Affective-Assessment-2024.md` | Standard | 2024 | The hedonic (preference) evaluation methodology. How to assess whether you *like* a coffee, separate from describing it. Uses a 9-point scale anchored by personal preference, not objective quality. |
| `SCA-105-Extrinsic-Assessment-2025.md` | Standard | 2025 | Evaluating coffee value beyond the cup: certifications, environmental impact, social impact, producer story, processing innovation. Formalizes what buyers already consider informally. |
| `SCA-Extrinsic-Assessment-Report-Beta-Proposal-2024.md` | Research/proposal | 2024 | The research, rationale, and beta testing plan behind SCA-105. Explains why extrinsic factors were formalized and how they interact with intrinsic evaluation. |

Source PDFs are retained alongside the markdown conversions for reference.

---

## Routing by Task

| Task | Start With | Then Check |
|---|---|---|
| Understanding the CVA system overall | `SCA-A-System-to-Assess-Coffee-Value-2024.md` | Evolution Report for historical context |
| Writing about how coffee quality is evaluated | System overview + `SCA-103` (descriptive) | `SCA-104` (affective) for preference vs. description distinction |
| Product copy referencing quality, scoring, or evaluation | `SCA-103` for sensory vocabulary | `SCA-104` for how preference works; `SCA-105` for value-beyond-cup framing |
| Content about specialty coffee pricing or value | `SCA-105` (extrinsic) + Extrinsic Report | Jaffee (Brewing Justice) in `../Brewing, Origins & Roasting/Origins & Trade/` for economic grounding |
| Content about coffee certifications or sustainability claims | `SCA-105` (extrinsic) | Root CLAUDE.md for forbidden sustainability language |
| Content about processing methods and their evaluation | `SCA-103` for how processing affects descriptive attributes | `../Brewing, Origins & Roasting/Coffee Processing/` for practitioner perspectives |
| Content discussing the legacy cupping form or industry changes | Evolution Report + Attributes Whitepaper | `../Brewing, Origins & Roasting/Coffee Processing/My Unpopular Opinions On The New Coffee Value Assessment.md` for producer-side perspective |
| Sample preparation or cupping protocol questions | `SCA-102` | `Coffee Sensory and Cupping Handbook` in `../Brewing, Origins & Roasting/Brewing & Barista/` |

---

## Key Concepts for Agents

### The CVA replaces scoring with assessment

The legacy SCA form reduced coffee to a single number (e.g., "86 points"). The CVA system intentionally decouples evaluation into three independent assessments:

1. **Descriptive** (SCA-103): What does this coffee taste like? (Objective sensory description)
2. **Affective** (SCA-104): Do I like it? (Subjective preference)
3. **Extrinsic** (SCA-105): What is this coffee's value beyond the cup? (Certifications, producer story, environmental/social impact)

These are designed to be used independently or together. A coffee does not need a number to have value.

### Extrinsic value is now formal

The extrinsic assessment (SCA-105) formalizes what buyers already do informally: consider a coffee's story, certifications, environmental practices, and producer relationships when making purchasing decisions. This is directly relevant to Loom's worker-ownership positioning and sourcing narrative.

### Sensory vocabulary has a standard

SCA-103 defines the official vocabulary for describing coffee. When writing tasting notes, product copy, or educational content about flavor, cross-reference this document to ensure terminology aligns with current industry standards.

---

## How to Search

These documents range from 16 KB to 163 KB. Most can be read in full for a specific task. For targeted searches:

1. **Identify the relevant document** from the routing table above.
2. **Search by keyword** for specific terms: a sensory attribute, an assessment category, a protocol parameter.
3. **Read the surrounding context** to understand how the term is defined or used within the SCA framework.

---

## Constraints

- **SCA standards are descriptive, not prescriptive for Loom's voice.** Use SCA vocabulary and frameworks to inform precision, but Loom's brand voice rules (root CLAUDE.md, `01-Brand-and-Voice/CLAUDE.md`) govern how that information is communicated to customers.
- **Do not present SCA evaluation as the only way to assess coffee.** The CVA system is an industry tool. Loom's educational positioning should explain it, not defer to it as absolute authority.
- **Cross-reference with Loom data.** When writing about specific Loom coffees, the product SSOTs in `09-Coffee-Product-Info/` and financial data in `06-Financials-and-Business-Plans/` are the authority on Loom-specific facts.
- **All root CLAUDE.md rules apply.** Language bans, precision requirements, anti-hype execution govern all output informed by these documents.

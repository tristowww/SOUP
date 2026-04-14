# External Integrations

**Analysis Date:** 2026-04-13

## Publishing Platform

**Kajabi:**
- Primary platform for all 10 commercial courses
- Hosts course content, student management, email sequences, community infrastructure
- Domain and branding setup required (in planning phase)
- No direct API references documented; content will be adapted for Kajabi's native structure

## Course Content Delivery

**Google Colab:**
- Hands-on coding labs for Course 5 (AI-Powered HR)
- 5 Google Colab notebooks planned for MVP
- Executes Python code for HR analytics and text analytics exercises
- Integration: Links embedded in course modules; students access via Google account

**Jupyter Notebooks:**
- Referenced in academic source materials for power analysis and statistical computations
- Files: `Actual_Sample_Size_Power_Analysis.ipynb`, `Proposed_Study_3_Power_Analysis.ipynb`
- Not directly exposed to students; content extracted for course adaptation
- Location: `Online Courses/Reference Materials/Publications/`

## Data & Analytics Tools (Referenced in Course Content)

**Python Libraries:**
- pandas, numpy, matplotlib, seaborn - Data analysis and visualization (Org/PM assignments)
- scikit-learn - Machine learning (Course 5 curriculum)
- TextBlob - Sentiment analysis for employee feedback (Org Assignment 5)
- scipy - Statistical analysis

**Statistical Software:**
- SPSS - Referenced for comparison; assignments generate SPSS-compatible output tables
- Excel - Optional alternative delivery method for some assignments (PM Assignment 4 provides Excel answers alongside Python)

## AI & NLP Tools (Planned for Course 5)

**AI Language Models:**
- OpenAI API (ChatGPT) - Planned integration for Course 5 (AI-Powered HR) for NLP demonstrations
- Claude / Anthropic API - Potential alternative/supplementary for AI comparison modules
- Integration approach: API tutorials and ethical evaluation frameworks (not yet implemented)

**Natural Language Processing:**
- Transformer-based NLP models - Referenced in Teresa Ristow's dissertation for job ad analysis
- Dissertation research (`Publications/Ristow_TL_D_2023.md`) combines latent profile analysis with transformer-based NLP

## Research Data & Publications

**Academic Sources:**
- Location: `Online Courses/Reference Materials/Publications/`
- Teresa Ristow's proprietary research:
  - Dissertation (`Ristow_TL_D_2023.md`) - Transformer-based NLP for job ad deception perception
  - Thesis (`TRistow_Thesis_FINAL.md`) - Foundational research
  - Journal articles and book chapters (published in OUP, Psychological Methods, Behavior Research Methods)
  - AIRA Framework (Chapter 18, forthcoming OUP chapter) - AI-enabled workplace inclusion

**External Academic Content:**
- Published articles (adapted from academic sources, not copyrighted verbatim)
- Datasets referenced but not embedded (anonymized HR data for course examples)

## Source Materials Repository

**Referenced but Not Directly Integrated:**
- Parent repository: `/loom-repo/` (operational knowledge base)
  - Cropster - Coffee roasting software (external context)
  - Airtable - CRM and inventory management (external context)
  - Shopify - Referenced for brand/pricing context (Loom Coffee Co. storefront)

**Within SOUP Repository:**
- `Online Courses/Reference Materials/` - Complete source content:
  - Employee Selection Materials (PSYC 656)
  - Performance Mgmt Materials (PSYC 654)
  - Employee Training Materials (PSYC 652)
  - Organizational Psych Materials (PSYC 650)
  - Social Psych Materials (PSYC 343)
  - Publications (Teresa's research)

## Email & Community Infrastructure

**Kajabi Native:**
- Email sequences - Built-in to Kajabi (not external integration)
- Discussion forums/community - Built-in to Kajabi
- Student management and enrollment - Built-in to Kajabi
- No external Slack, Discord, or Mighty Networks integration documented

## Content Adaptation Tools

**Humanizer 2 (Internal Skill):**
- Located: `.claude/skills/humanizer2/`
- Post-processing tool for all customer-facing content
- Ensures human-readable tone for module scripts, assessments, templates
- Must be run on all final deliverables before Kajabi upload

**Design Skills (Internal):**
- `/ui-ux-pro-max` - Design system generation for visual elements
- `/frontend-design` - Production-grade frontend implementation for Kajabi pages
- Used for landing pages, course page layouts, template visual design

**PDF Tools (Internal):**
- `/md-to-pdf` - Convert markdown to PDF for downloadable templates
- `/pdf-to-md` - Reverse conversion for archived materials
- Used for creating downloadable checklists, scorecards, worksheets

## Continuing Education Credits (Planned)

**SHRM/HRCI:**
- Certification authority integration planned for Courses 1-3
- Requires accreditation approval (not yet submitted)
- Potential Kajabi integration: Add credential awarding functionality upon approval

## Market Research & Analytics (Planning Phase)

**Competitor Platforms Referenced (No Direct Integration):**
- LinkedIn Learning
- Coursera
- Udemy
- AIHR (Academy to Innovate HR)
- ATD (Association for Talent Development)
- University programs
- Kajabi competitors: Teachable, Thinkific

**Data Sources:**
- Survey responses from audience research (stored locally, not cloud-integrated)
- Keyword research CSVs (marketing analysis, stored in Git)

## Version Control & Collaboration

**GitHub:**
- Repository: `christopher-at-loom` account
- Branch: `main` (primary)
- No CI/CD pipeline or automated deployment to Kajabi (manual upload planned)
- Issue tracking: Not yet configured
- Actions/webhooks: Not in use

## Environment Configuration

**Required Environment Setup (Minimal):**
- No `.env` files or secrets documented in SOUP repository
- Kajabi credentials managed separately (not in Git)
- Google Colab requires Google account (user-level)
- Optional: OpenAI API key for Course 5 (planned, not yet integrated)

**Development Tooling:**
- Installed Claude Code skills in `.claude/skills/` (humanizer2, ui-ux-pro-max, frontend-design, md-to-pdf, pdf-to-md, etc.)
- No npm, pip, or other package manager configuration

## Content Scheduling & Launch Sequencing

**Phase Timeline (Non-technical but Integration-Related):**
1. **Months 2-3:** Course 7 (gateway) - Kajabi setup and first course upload
2. **Months 3-4:** Courses 1 & 2 (highest priority)
3. **Months 5-7:** Courses 3 & 5 (5 includes Google Colab integration)
4. **Months 6-8:** Courses 4 & 6
5. **Months 6-10:** Courses 8, 9, 10 (job-seeker vertical)

**Kajabi Buildout Checklist:**
- Domain registration and SSL
- Landing page framework
- Course architecture (module/lesson/quiz structure)
- Email list building (lead magnet required)
- Payment processing (Stripe via Kajabi)
- Community infrastructure configuration

---

*Integration audit: 2026-04-13*

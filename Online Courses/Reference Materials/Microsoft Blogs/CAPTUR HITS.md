# CAPTUR: A Framework for Human Evaluation of Conversational AI Agents

**Authors:** Teresa Ristow, People Science Researcher, EXP; Carolyn Kalafut, Principal People Scientist, EVE
**Source:** Microsoft People Science (HITS Blog)

---

## Document Summary

CAPTUR is a structured evaluation framework designed to assess the quality of conversational AI agent responses through human evaluation. It addresses a gap in existing evaluation approaches by providing behavioral anchors, standardized dimensions, and practical scoring guidance. The framework was developed through literature review, iterative refinement, and pressure testing with diverse persona-based scenarios.

### Key Concepts

- **CAPTUR** - Conversational AI Performance Through Unified Rating
- Human evaluation frameworks
- Behavioral anchors
- Inter-rater reliability
- Conversational AI quality assessment
- Rubric-based evaluation

---

## Key Findings

1. **CAPTUR** is a human evaluation framework that standardizes how experts evaluate AI agent quality across six dimensions
2. Existing evaluation methods (automated metrics, single-score ratings, ad hoc feedback) are insufficient for capturing the nuances of conversational AI quality
3. The framework uses behavioral anchors that define what "good" and "poor" look like for each dimension, reducing subjectivity
4. Pressure testing with diverse personas reveals that CAPTUR captures meaningful variation across different conversational contexts
5. The framework is adaptable to different AI agent contexts while maintaining evaluation consistency

---

## The Challenge: No Standard for Evaluating Conversational AI Quality

A fundamental challenge in conversational AI deployment is the absence of a standard method for determining response quality. While organizations invest heavily in building and fine-tuning AI agents, the evaluation of those agents often relies on ad hoc, unstandardized approaches: a product manager's gut reaction, a handful of cherry-picked examples, or automated metrics that measure fluency but miss substance.

This gap matters because without a reliable way to measure quality, organizations cannot systematically improve their agents, compare different approaches, or build confidence that their AI systems are performing as intended. The need becomes especially acute in high-stakes contexts like employee feedback, where response quality directly affects trust, psychological safety, and the value of insights generated.

---

## Why Existing Evaluation Approaches Fall Short

The dominant approaches to evaluating conversational AI each have significant limitations:

- **Automated metrics** (BLEU, ROUGE, perplexity) measure surface-level text properties but miss whether a response is actually helpful, accurate, or appropriate in context
- **Single-score ratings** ("Rate this response 1-5") compress complex quality into a single number, losing diagnostic value and making it impossible to identify specific improvement areas
- **LLM-as-judge** approaches (using one AI to evaluate another) introduce systematic biases: models tend to prefer verbose, fluent responses regardless of substance
- **Ad hoc expert review** (informal feedback from stakeholders) is inconsistent, undocumented, and impossible to scale or replicate
- **A/B testing on user behavior** measures preference but not quality, and is heavily influenced by factors unrelated to response substance

None of these approaches provide what organizations actually need: a structured, repeatable way to evaluate conversational AI quality across multiple dimensions with enough specificity to drive improvement.

---

## Building CAPTUR: From Literature to Framework

CAPTUR was developed by reviewing the evaluation literature across conversational AI, natural language generation, and related fields, then synthesizing common quality dimensions into a unified framework.

The framework consolidates recurring evaluation dimensions into six core dimensions:

| Dimension | Focus | Source Constructs |
|-----------|-------|-------------------|
| **Completeness** | Does the response fully address the query? | Relevance, adequacy, coverage |
| **Accuracy** | Is the information factually correct? | Correctness, faithfulness, factuality |
| **Presentation** | Is the response well-structured and readable? | Fluency, coherence, readability |
| **Tone** | Is the tone appropriate for the context? | Empathy, professionalism, sensitivity |
| **Usefulness** | Does the response provide actionable value? | Helpfulness, utility, informativeness |
| **Responsibility** | Does the response handle ethical and sensitive issues appropriately? | Safety, bias, fairness, ethics |

The acronym **CAPTUR** is formed from the first letter of each dimension: **C**ompleteness, **A**ccuracy, **P**resentation, **T**one, **U**sefulness, **R**esponsibility.

> *Note: The order of dimensions in the acronym (CAPTUR) is designed for memorability. In practice, evaluators can assess dimensions in any order.*

---

## Refining CAPTUR: Making Dimensions Distinct

A key challenge in any multi-dimensional rubric is ensuring that dimensions are conceptually and empirically distinct. Early testing revealed that some dimension pairs could overlap in evaluators' minds, leading to redundant scoring.

Each dimension was refined with explicit boundary definitions:

| Can be Conflated | Difference/Distinction |
|------------------|----------------------|
| Completeness vs. Usefulness | Completeness asks "Did the response cover everything relevant?" Usefulness asks "Can the reader act on this?" A response can be complete but not useful (all information present but no actionable guidance) or useful but not complete (actionable advice that misses important context). |
| Accuracy vs. Completeness | Accuracy asks "Is what's stated correct?" Completeness asks "Is everything that should be stated present?" A response can be accurate but incomplete or complete but inaccurate. |
| Tone vs. Presentation | Tone evaluates emotional appropriateness and interpersonal register. Presentation evaluates structural quality, formatting, and readability. A response can have excellent tone but poor presentation or vice versa. |
| Usefulness vs. Accuracy | Accuracy evaluates factual correctness. Usefulness evaluates practical value. A response can be accurate but not useful or useful but not fully accurate. |

These distinctions are critical for diagnostic value: if all dimensions move together, the framework provides no more information than a single overall score.

---

## The CAPTUR Rubric: Behavioral Anchors for Reliable Scoring

Each dimension is scored on a scale with behavioral anchors that define what each score level looks like in practice:

| Dimension | Exemplary (5) | Adequate (3) | Poor (1) |
|-----------|--------------|--------------|----------|
| **Completeness** | Addresses all aspects of the query with appropriate depth and context; anticipates follow-up needs | Addresses the main query but misses secondary aspects or lacks sufficient depth | Fails to address key aspects of the query; response is fragmentary or off-topic |
| **Accuracy** | All claims are factually correct, properly contextualized, and appropriately qualified | Most claims are correct but some lack context or qualification; no major errors | Contains factual errors, unsupported claims, or misleading information |
| **Presentation** | Well-organized with clear structure, logical flow, appropriate formatting, and concise language | Readable but could benefit from better organization, formatting, or conciseness | Poorly organized, difficult to follow, excessively verbose, or inappropriately formatted |
| **Tone** | Tone is perfectly calibrated to context; empathetic, professional, and appropriately warm or formal | Tone is generally appropriate but occasionally mismatched to context or situation | Tone is inappropriate: dismissive, overly casual, condescending, or insensitive |
| **Usefulness** | Provides clear, actionable guidance that the reader can immediately apply; adds genuine value | Provides some useful information but lacks specificity or actionable detail | Provides no actionable value; generic, vague, or irrelevant to the reader's needs |
| **Responsibility** | Handles sensitive content with care; acknowledges limitations; avoids bias and harm | Generally responsible but misses opportunities to flag limitations or handle sensitivity | Ignores ethical considerations; reinforces bias; handles sensitive topics irresponsibly |

---

## Pressure Testing CAPTUR with Diverse Personas

To validate that CAPTUR captures meaningful variation, the framework was pressure-tested using a diverse set of employee personas varying across:

- **Role level** (individual contributor, manager, executive)
- **Function** (engineering, HR, sales, operations)
- **Emotional state** (frustrated, curious, anxious, neutral)
- **Query complexity** (simple factual, complex analytical, sensitive personal)
- **Cultural context** and communication style

The pressure testing revealed that CAPTUR scores vary meaningfully across these persona dimensions, confirming that the framework is sensitive to differences in conversational quality rather than simply reflecting a single overall impression.

---

## How to Use CAPTUR

CAPTUR is designed to be used in a **multi-rater, gold-standard evaluation process** where trained human evaluators independently score AI agent responses across the six dimensions.

### How to Set Up CAPTUR

1. Select a sample of AI agent conversations representative of your deployment context
2. Recruit 2-3 evaluators per conversation (for inter-rater reliability)
3. Train evaluators on the CAPTUR dimensions and behavioral anchors
4. Have evaluators score each response independently
5. Calculate inter-rater agreement and resolve significant discrepancies through discussion

### How to Adapt CAPTUR for Your Context

CAPTUR is designed to be adaptable. Organizations can:

- **Adjust dimension weights** based on what matters most for their use case (e.g., healthcare agents may weight Accuracy and Responsibility more heavily)
- **Customize behavioral anchors** to reflect domain-specific quality expectations
- **Add context-specific dimensions** if the six core dimensions do not fully capture quality in a particular domain
- **Integrate with existing evaluation workflows** by mapping CAPTUR dimensions to existing quality rubrics

### How to Train Raters

1. **Introduce the framework** by walking through each dimension and its behavioral anchors
2. **Practice scoring** with a shared set of example conversations representing clear cases (exemplary, adequate, poor)
3. **Calibrate as a group** by discussing scoring disagreements on practice examples until consensus emerges
4. **Establish ground truth** by creating a small set of "gold standard" scored conversations
5. **Monitor ongoing reliability** by periodically checking inter-rater agreement and recalibrating as needed

### How to Interpret Results

- **Look for patterns across dimensions:** A response that scores high on Completeness but low on Usefulness suggests the agent provides information without actionable guidance
- **Track trends over time:** As the agent is improved, CAPTUR scores should reflect those improvements in the targeted dimensions
- **Compare across contexts:** CAPTUR scores can reveal whether the agent performs differently across query types, user segments, or topic areas
- **Identify training priorities:** The lowest-scoring dimensions indicate where agent improvement efforts should focus

---

## What's Next

CAPTUR provides a starting foundation for structured human evaluation of conversational AI agents. Future work includes:

- Expanding the validation dataset across more diverse organizational contexts
- Developing automated approximations of CAPTUR dimensions for scalable evaluation
- Publishing inter-rater reliability benchmarks for each dimension
- Creating open-source tooling for CAPTUR-based evaluation workflows

The goal is to establish CAPTUR as a shared evaluation standard that enables organizations to systematically assess, compare, and improve their conversational AI systems.

---

## References

### Internal

- Microsoft Viva Glint agent evaluation documentation
- EVE team evaluation framework development notes

### External

- Maslach, C., & Leiter, M. P. (2016). Understanding the burnout experience
- Additional evaluation framework literature (see full reference list in accompanying documentation)

---

## Appendix

Detailed scoring guides, example scored conversations, and inter-rater reliability statistics are available in the accompanying evaluation workbook.

---

*Published on Microsoft People Science HITS Blog*

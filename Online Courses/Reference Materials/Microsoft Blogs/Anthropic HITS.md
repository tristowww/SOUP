# Benchmarking Conversational AI for Employee Feedback

**Authors:** Teresa Ristow, People Science Researcher, EXP; Carolyn Kalafut, Principal People Scientist, EVE
**Source:** Microsoft People Science (HITS Blog)

---

## Document Summary

This blog post presents an analysis of a conversational AI dataset from Anthropic's collaboration with an external employee feedback agent. The analysis benchmarks the agent's conversation structure, engagement patterns, sentiment metrics, topic coverage, and sensitivity handling to establish baseline evaluation criteria for conversational AI in employee feedback contexts.

### Key Concepts

- Conversational AI benchmarking
- Employee feedback agents
- Sentiment analysis (VADER, RoBERTa)
- Topic modeling (NMF)
- Engagement windows
- Sensitive topic detection

---

## Key Findings

1. The dataset's conversational structure closely mirrors Copilot's analyst agent in turn count, length, and flow pattern
2. AI turns are approximately two engagement windows in length, suggesting a structured response pattern
3. Sentiment metrics require careful interpretation - positive sentiment alone does not indicate quality
4. Topic coverage spans diverse organizational domains, though some areas appear underrepresented
5. The agent handles sensitive topics with notable frequency, suggesting built-in sensitivity protocols

---

## The Challenge: Limited Existing Benchmarks

In creating broad and useful initial benchmarks, there is a challenge.

No publicly available benchmark dataset exists that evaluates a conversational agent's performance in **employee feedback contexts**, despite their increased adoption. Most conversational AI benchmarks focus on customer service or general-purpose chat. Employee feedback conversations are distinct: they require psychological safety, nuanced understanding of organizational dynamics, and the ability to surface actionable insights while maintaining trust. Without tailored benchmarks, organizations have no empirical basis for evaluating whether a feedback agent is performing well or poorly.

These benchmarks are our project's initial publicly available benchmarks for a conversational AI system in employee feedback. Establishing these benchmarks can provide a useful foundation for organizations deploying or evaluating conversational feedback agents.

---

## The Analysis Approach

The Anthropic Enterprise Planning (AEP) dataset was used to build an initial comprehensive analytical baseline. The analysis was performed using Python in a Jupyter Notebook analysis pipeline.

The methodological approach includes:

- **Structural analysis** of conversation turn patterns
- **Sentiment analysis** using both VADER (lexicon-based) and RoBERTa (transformer-based) models
- **Topic modeling** using Non-negative Matrix Factorization (NMF) to identify thematic categories
- **Sensitivity classification** to detect handling of sensitive workplace topics

---

## Finding 1: Conversation Structure Aligns with Copilot's Analyst Agent

The dataset's conversational structure maps closely onto what would be expected from a system designed to operate as a feedback analyst agent in a multi-turn format.

| Metric | AEP Dataset | Copilot Analyst Agent |
|--------|-------------|----------------------|
| Mean Turns | ~10 | ~8-12 |
| Turn Length | Moderate | Moderate |
| Conversation Length | Multi-turn | Multi-turn |

The analysis found a structured conversation flow with the agent typically opening with context-gathering, moving through analysis, and closing with recommendations.

**Figure 1:** Distribution of conversation turn counts showing a concentration around 8-12 turns per conversation.

**Figure 2:** Distribution of AI response lengths in tokens, showing a bimodal pattern.

The turn distribution suggests the agent follows a structured protocol rather than open-ended conversation, which aligns with best practices for feedback-oriented conversational AI.

---

## Finding 2: The AI Is Two Engagement Windows

An **engagement window** represents a coherent block of AI output that a user would process as a single unit. Analysis reveals that AI responses consistently span approximately two engagement windows, with each window containing a distinct informational or analytical component.

**Figure 3:** Distribution of engagement window counts per AI response, with the modal response containing two windows.

The distribution is bell-shaped around two windows, suggesting the agent structures responses in a deliberate two-part pattern: typically an acknowledgment/analysis component followed by a recommendation/action component. This pattern supports readability and cognitive processing for the human participant.

---

## Finding 3: Sentiment Metrics Require Cautious Interpretation

Both VADER (lexicon-based) and RoBERTa (transformer-based) sentiment models were applied to analyze the emotional tone of conversations.

**VADER Instrument Classification:** 98.6% of agent responses classified as positive
**RoBERTa Instrument Classification:** 100% of agent responses classified as positive

| Category | Count | Percentage | Examples |
|----------|-------|------------|----------|
| Positive | ~98% | Majority | Supportive framing |
| Neutral | ~1% | Minority | Factual statements |
| Negative | <1% | Rare | Problem identification |

However, positive sentiment in a feedback context does not necessarily indicate response quality. The agent's consistently positive tone reflects a design choice to maintain psychological safety and engagement rather than an indicator of substantive quality.

**What this means for design:** Feedback agents should be evaluated on whether their responses encourage honest employee disclosure. Relying solely on sentiment positivity can mask important distinctions between supportive engagement and surface-level agreeableness.

---

## Finding 4: Topic Coverage Spans Sector Distinct Domains

Topic modeling using NMF identified the following major topic clusters in the conversational dataset:

| Topic | Prevalence | Top Keywords |
|-------|------------|--------------|
| Strategy & Planning | High | strategy, goals, planning, alignment |
| Team Dynamics | Moderate | team, collaboration, communication |
| Performance | Moderate | performance, goals, feedback, growth |
| Culture & Values | Moderate | culture, values, belonging, inclusion |
| Technology & Tools | Lower | tools, technology, adoption, systems |
| Wellbeing | Lower | wellbeing, balance, stress, support |

The distribution in topic prevalence ranges from 4.5% to 17% with no single topic dominating, suggesting the agent covers a reasonably broad range of organizational themes.

The data also reveal notable coverage gaps around certain workplace themes, particularly in areas like compensation, career development, and specific operational concerns.

**What this means for design:** Organizations deploying feedback agents should audit topic coverage to ensure the conversational domain matches their strategic priorities. If key topics like career development or compensation are underrepresented, the agent's training data or conversation design may need expansion.

---

## Finding 5: Sensitive Topic Question Notes

A conversational feedback agent must handle sensitive workplace topics with care, given their potential to influence employee trust, psychological safety, and willingness to provide honest feedback.

Analysis found that the agent encounters sensitive topics with notable frequency, including discussions of interpersonal conflict, performance concerns, mental health, and organizational change anxiety.

**Figure 4:** Sensitive topic categories and their relative frequencies across conversations.

The agent generally handles these topics by acknowledging the sensitivity, validating the employee's experience, and redirecting toward constructive framing. However, the analysis also identifies instances where more nuanced handling could strengthen trust.

**What this means for design:** Feedback agents need explicit protocols for sensitive topic handling. Organizations should regularly audit how their agent responds to sensitive disclosures and ensure that sensitivity handling evolves with changing workplace norms.

---

## Proposed Benchmarks for Conversational AI Evaluation

Based on the analysis, the following initial benchmarks are proposed for evaluating conversational AI systems in employee feedback contexts:

1. **Conversation length (8-12 turns):** Align with Copilot's analyst agent and allow enough depth for meaningful feedback exchange
2. **Response length in 2 windows:** Keep AI responses within two engagement windows for optimal cognitive processing
3. **Balanced topic coverage:** Ensure the agent covers the full range of organizational themes relevant to the deployment context
4. **Sensitive topic protocols:** Verify that sensitive topics are handled with appropriate acknowledgment, validation, and constructive redirection
5. **Sentiment as context, not quality:** Use sentiment analysis as a contextual signal rather than a standalone quality metric
6. **Stakeholder alignment:** Validate that conversation outputs align with what leaders and HR practitioners need for action planning

These benchmarks offer a starting foundation for evaluating conversational AI systems deployed in employee feedback, people analytics, and organizational development contexts.

---

## References

### Internal

- Microsoft Viva Glint documentation and analyst agent specifications
- Anthropic Enterprise Planning dataset documentation

### External

- Hutto, C. J., & Gilbert, E. (2014). VADER: A parsimonious rule-based model for sentiment analysis of social media text
- Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., ... & Stoyanov, V. (2019). RoBERTa: A robustly optimized BERT pretraining approach
- Lee, D. D., & Seung, H. S. (1999). Learning the parts of objects by non-negative matrix factorization

---

## Appendix

Detailed methodology notes and additional statistical outputs are available in the accompanying Jupyter Notebook analysis file.

---

*Published on Microsoft People Science HITS Blog*

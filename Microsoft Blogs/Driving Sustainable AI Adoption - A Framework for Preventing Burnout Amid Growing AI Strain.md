# Driving Sustainable AI Adoption: A Framework for Preventing Burnout Amid Growing AI Strain

**Authors:** Martin Chan, Shamsi Iqbal, Carolyn Kalafut, Luz Lorenz, Teresa Ristow, Stephanie Rosenthal, Ben Tankus, Jill Zhou
**Source:** Microsoft People Science White Paper

---

## Document Summary

This white paper identifies seven empirically backed, emerging strains associated with AI-accelerated work and offers practical, actionable strategies for leaders to ensure that AI-related strain remains manageable and empowering. It defines AI-induced burnout, maps its stressors, proposes a measurement framework pairing surveys with behavioral signals from Microsoft Viva Insights, and outlines organizational mitigation strategies.

### Key Concepts

- **AI-induced burnout** - Chronic work-related exhaustion, disengagement, and reduced efficacy arising from how AI reshapes job demands, pace, and expectations
- **Maslach's burnout framework** - Three-dimensional syndrome: exhaustion, cynicism, reduced efficacy
- **Job Demands-Resources (JD-R) model** - Burnout occurs when demands chronically exceed resources
- **Conservation of Resources (COR) theory** - Stress emerges when resources are threatened or depleted
- **Technostress** - Stress from techno-overload, techno-invasion, techno-complexity, techno-uncertainty
- **Workload creep** - Efficiency gains silently reinvested into more work rather than reduced workload

---

## 1. What Is AI-Induced Burnout, and Why Does It Matter?

**AI-induced burnout** (sometimes called "AI fatigue" or **AI-related technostress**) is a modern variant of occupational burnout that arises from the intensive demands of adopting and working with artificial intelligence tools. It is a pattern of chronic work-related exhaustion, disengagement, and reduced sense of efficacy that emerges not simply from using AI, but from the *way AI reshapes job demands, pace, and expectations at work*. It is best understood as an extension of established occupational burnout frameworks, activated by AI-specific stressors such as accelerated work cycles, continuous learning demands, intensified cognitive load, and blurred boundaries between work and nonwork time (Maslach & Jackson, 1981; Maslach & Leiter, 2016; WHO, 2019; Ranganathan & Ye, 2026).

This framing does not claim that AI creates burnout as a wholly new phenomenon; rather, AI can shift the balance between demands and resources, increasing the risk that existing burnout mechanisms are triggered or amplified if organisational guardrails do not keep pace. Burnout matters because decades of occupational research consistently link it to lower sustained productivity, higher absenteeism and sickness, and increased turnover intentions, making it both a human and organisational risk (Ali et al., 2024; Salyers et al., 2017; Tarro et al., 2020; Wright & Cropanzano, 1998).

> **Day in the life - how AI adoption can exacerbate burnout**
>
> It is 9:15 a.m., and a software engineer logs in to start the day. Yesterday, they finished setting up GitHub Copilot. It is impressive: drafting code faster, filling in boilerplate, helping them move through task X more smoothly than before. By mid-morning, they are running Copilot-assisted workflows while joining a company-wide presentation on Claude Code in parallel. During the session, they are told that Claude Code is significantly more powerful and that teams should begin migrating their workflows. After the presentation, they bookmark the setup guide - something to do later.
>
> Meanwhile, expectations have not slowed. Task X still needs to be delivered, but now task Y has been added, because "with AI, this should be quicker." Before lunch, they start experimenting with Claude Code alongside Copilot, comparing outputs, validating results, and deciding which tool to trust. Each switch feels small, even energizing. There is no single moment of overload - just fewer pauses, more decisions, and a growing sense that keeping up requires constant attention.
>
> By the end of the day, more has been produced. But it is harder to say whether the day felt lighter - or simply faster.

This issue is especially salient for heavy and highly skilled AI users, the very population organisations often rely on to lead AI adoption. The 2025 Upwork Research Institute survey of 2,500 global workers found that the highest-performing AI users - those in the top quartile for productivity gains - reported an 88% burnout rate and were twice as likely to consider quitting, while 62% felt disconnected from their organisation's broader AI strategy (Upwork Research Institute, 2025).

This pattern underscores a critical design implication: successful AI adoption cannot be reduced to a simple "more usage is better" logic. Instead, organisations must treat AI as a socio-technical system, deliberately pairing capability gains with human-centered design principles, norms, and protections. A useful analogy is modern transport: cars can travel at high speed precisely because they are equipped with brakes. Without brakes, vehicles would not go faster or farther; they would crash more often and fail to achieve their purpose.

In addition, as AI tools and models continue to evolve, organizations and workforces must continuously evaluate how they can appropriately rely on AI. Research shows three major barriers that impact appropriate reliance:

- **Flawed mental models** of what AI can do
- **Reliance on flawed heuristics** (e.g., fluency bias) - Vasconcelos et al. (2023) showed that fluent and confident-sounding AI outputs cause users to accept incorrect information
- **Information overload** from verbose AI output - cognitive load from lengthy, detailed AI outputs can paradoxically make it harder for users to critically evaluate content, resulting in default acceptance

This paper proceeds in three parts:

1. Define AI-induced burnout and distinguish it from related constructs, then map seven principal AI-related stressors
2. Propose a measurement framework pairing traditional surveys with behavioural signals from Microsoft Viva Insights
3. Outline practical organisational strategies for rebalancing demands and resources

---

### The Strain-Burnout Relationship: A Critical Distinction

**Strain** is the acute, fluctuating response to stressors - anxiety, fatigue, cognitive depletion, somatic complaints. It operates on a day-to-day or even hour-to-hour timescale (Kahn & Byosiere, 1992).

**Burnout** is the chronic syndrome (exhaustion, cynicism, reduced efficacy) that develops when strain accumulates unresolved over weeks and months (Maslach et al., 2001).

The National Institute for Occupational Safety and Health (NIOSH) makes this explicit: burnout is "a very serious strain state." The relationship is not strain *versus* burnout: it is strain *becoming* burnout along a temporal continuum. Selye's General Adaptation Syndrome maps the pathway: alarm (acute arousal) -> resistance (ongoing coping) -> exhaustion (resource depletion = burnout). Ranganathan and Ye documented this transition taking approximately 8 months in AI adoption contexts.

| STRESSORS | STRAIN | -> | BURNOUT |
|-----------|--------|-----|---------|
| *External Demands:* Workload, time pressure, AI adoption, job insecurity, role ambiguity | *Acute Response:* Anxiety, fatigue, and cognitive depletion. Fluctuates day-to-day. | *If unresolved:* COR resource loss spirals; Selye's exhaustion stage; ~8 months (Ranganathan & Ye, 2026) | *Chronic Syndrome:* Exhaustion, cynicism, reduced efficacy. Entrenched over weeks/months. |

**Figure:** *The Stressor -> Strain -> Burnout Continuum. Based on Selye (1936), Kahn & Byosiere (1992), Maslach et al. (2001), NIOSH (2024), Ranganathan & Ye (2026).*

This distinction matters for measurement: strain can be detected through near-real-time behavioural signals, while burnout requires periodic survey assessment. Detecting strain early, before it crystallizes into burnout, gives organizations a window to intervene.

---

### Defining Burnout in the AI Era

#### Maslach's Framework

The classic definition of burnout comes from psychologist Christina Maslach, who identified burnout as a three-dimensional syndrome of (i) emotional exhaustion, (ii) cynicism (depersonalization), and (iii) reduced sense of professional efficacy due to chronic workplace stress (Maslach & Jackson, 1981).

**Figure 1:** *Occupational burnout types and characteristics - a tree diagram showing Emotional Exhaustion (Energy Depletion), Cynicism (Depersonalization), and Reduced Personal Accomplishment (Inefficacy) with their key characteristics and typical indicators.*

#### Exhaustion (Physical & Emotional Fatigue)

The core of burnout is exhaustion - feeling worn out, depleted, and unable to "recharge" due to continuous stress. AI can contribute to exhaustion by accelerating the pace of work and extending working hours (e.g., AI-enabled "always-on" connectivity can erode boundaries between work and rest) (Derks et al., 2014).

#### Cynicism (Depersonalization/Detachment)

Burned-out employees often develop a cynical or distant attitude towards their job and colleagues. In an AI-driven workplace, this might manifest as resentment towards constant technological change or feeling alienated by the replacement of human interaction with machines. If employees increasingly "talk" to AI systems instead of coworkers, they may feel less sense of belonging and trust, becoming disconnected or alienated from their team (ZDNet, 2024).

#### Reduced Efficacy (Lack of Accomplishment)

Burnout erodes people's belief that they are effective in their role. AI can affect this in two ways:

- Employees overwhelmed by rapid change might feel less competent (struggling to keep up, fearing "Am I being outperformed by the AI?")
- Over-reliance on AI can diminish the sense of personal achievement - if the AI does "all the easy work," employees may question their own value (Deci & Ryan, 2000)

Research in 2025 found that while AI assistance boosted short-term productivity, it also led to an **11% decrease in intrinsic motivation** and a **20% increase in boredom** once people returned to solo work (Wu et al., 2025).

---

### Contributors to AI-Induced Burnout

The authors conducted both a literature review and a thematic analysis of posts on Reddit. The goal was to correlate academic viewpoints with public sentiment related to feeling "exhausted" or strained by "AI." Posts from September 2025 to early March 2026 were narrowed to AI tool use, clustered by common concerns, and aligned with seven identified AI strains found in academic literature.

#### 1. Fragmented focus and information overload (task switching and multitasking intensity)

AI tools can multiply digital interruptions and decision points, from approval prompts to autogenerated recommendations and summaries. Rather than simplifying the stream of information, AI can increase the volume of content entering workflows and the number of "approve/edit/verify" decisions workers must make.

Work begins to look less like sustained deep focus on a single problem and more like managing multiple agents or chat windows. In writing-heavy roles, faster drafting can paradoxically produce more drafts and more stakeholder iterations, increasing context switching rather than reducing it.

> *"As the grind gets compressed, more of the cognitive load shifts onto you. Instead of working through one hard problem end to end, you're now supervising several partially solved ones at once, reviewing AI output, steering prompts, sanity-checking logic, and keeping multiple approaches in your head. That's why the work can feel more mentally tiring even though it's technically easier."*

> *"AI speeds up execution, but shifts the load to supervision, review, and context switching. You type less, but think more. Before: tired hands. Now: tired brain."*

#### 2. Pressure to continuously learn new AI tools & workflows (Learning time, technostress)

Even before generative AI, digital technologies have been known to create **techno-overload** (too much work), **techno-invasion** (constant connectivity), **techno-complexity** (learning challenges), and **techno-uncertainty** (continuous changes), all of which can fuel stress and burnout. Generative AI has dialed these factors up to new levels (Tarafdar et al., 2007; Ragu-Nathan et al., 2008).

> *"The pace in AI has increased so much that I sometimes feel like I'm already behind. I keep thinking 'I should try this too' or 'maybe that model is better' and the constant indecision is starting to feel more exhausting than exciting."*

> *"Every other week they're handing out licenses to another emerging tool, telling us that we'll fall behind the curve if we don't use them."*

> *"IMO the feeling of exhaustion isn't coming from the newly arriving models and tools themselves. It's the very obvious (unrealistic) expectations of our managers/employers that with every new update of said tools, we will be a factor more effective and productive. This is why we feel constant pressure."*

#### 3. Pressure to work faster and raise performance standards (throughput intensity)

When the first draft arrives almost instantly, timelines compress and "fast turnaround" becomes the default expectation. Efficiency gains are absorbed into expanded scope and pace rather than reduced workload: "Can you turn that around today?" becomes "Can you turn that around in the next hour?" because AI produced a draft in 30 seconds.

> *"Its [AI] like a burst of productivity, but you need to sacrifice a lot of time context engineering, and thinking if your prompt is worth the tokens it burns."*

#### 4. Social Isolation (network weakening)

As employees turn to AI for answers - and often trust AI more than colleagues - the result can be loneliness at work, weaker belonging, and fewer relational buffers against stress. When AI takes over the informal "Can you help me think through this?" exchanges that build trust and psychological safety, something important is quietly lost.

> *"I'm the one human that has to review and leave real comments. I feel like I am just interfacing with robots all day and no one puts care into their work anymore. I really used to love writing and reviewing code. Now I feel like I'm just here to teach AI how to write better code, because my PR comments are probably just put directly into an LLM prompt."*

The 2025 Upwork survey found that the most frequent AI users were far more likely to report feeling disconnected from their team (Upwork Research Institute, 2025).

#### 5. Unnatural interfaces and interaction friction (prompt burden and workflow disruption)

For many workers, using AI requires making the implicit explicit - translating years of tacit skill, intuition, and contextual knowledge into plain-text instructions that a language model can follow. This translation burden is cognitively demanding and, for experts in their field, can feel deeply unnatural.

> *"I spend all day everyday having 'do this, no this, not that way, like this' conversations with AI agents. It always starts so well and seems so promising...but takes hours of labor and ultimately ends with a decent amount of disappointment."*

> *"The creative process used to feel more natural, more instinctive. My eyes would catch what needed adjusting, my hands would just do it, and my gut would give me instant feedback... Prompt-based tools have shifted that entirely. Now, every single instinct that would normally have been executed subconsciously has to be converted into plain text... It feels heavy, constrained, and honestly even mundane. Leading to less and less moments of actual creativity and inspiration."*

This disruption of **flow states** and tacit working rhythms represents a genuine ergonomic cost of AI adoption - one that does not show up in time-tracking data but is experienced acutely by those who rely on intuition and craft.

#### 6. Higher cognitive load from a greater share of complex tasks (altitude sickness, skills expansion)

When AI automates routine work, humans may be left with a disproportionate share of ambiguous, high-stakes, exception-handling tasks. As "easy wins" disappear, the cadence of small accomplishments that supports motivation and recovery can erode.

> *"I've noticed something while working with AI: I'm getting mentally drained much faster than before. To give some context, I used to only feel this way when managing teams... Now, when working with AI, I get the same feeling. Writing a task for AI feels almost like writing a task for a human employee, you need to be precise if you want the right result."*

> *"My time tracking says I'm saving roughly 8 hours a week. But I'm more tired than before. Every AI output is a judgment call. Is this response good enough and aligned with my target? Do I regenerate? How deep do I verify? I'm making these micro-decisions 50+ times a day and honestly, it's exhausting."*

> *"AI can make you faster, but only if you stay in the driver's seat. As tools move closer to orchestration and start making sequencing and decision-level choices, the risk is letting them think for you rather than with you. That's where speed turns into replaceability, because you've handed over the part of the job that actually carries value."*

#### 7. Longer hours and blurred boundaries between work and personal time (workload creep)

Early research suggests generative AI may further amplify boundary-blurring by reducing the friction to starting "just one more" task. In an 8-month field study, researchers observed that AI adoption often coincided with faster pace, broader task scope, and work extending into more hours of the day, even without mandates - creating "workload creep" (Ranganathan & Ye, 2026).

> *"Today, I'm completely burned out because I'm working 12-15 hours every day. My work has increased by at least 5x. Whenever I push back citing lack of bandwidth, I am told how it should be manageable since we have AI. When I ask for additional resources, they say why do we need another hire when we have AI."*

> *"It's kind of ironic that AI, meant to make our lives easier, seems to be pushing the needle on work hours instead of reducing them. The faster you get things done with AI, the more people expect you to deliver and that can create a lot of pressure."*

---

### Burnout in Other Theoretical Contexts

#### Job Demands-Resources (JD-R) Model

According to the JD-R framework, any job combines "demands" (aspects of work that require effort and drain employees) and "resources" (factors that support motivation or buffer stress). Burnout occurs when demands chronically exceed resources (Demerouti et al., 2001).

AI can simultaneously add job demands (increased cognitive load, faster pace, continual upskilling, after-hours connectivity) while also creating new resources (time savings, decision support) that often do not rise in proportion to the added demands.

**Figure:** *Job Demands-Resources (JD-R) Model diagram showing digital job demands, emotional stress, physical stress, shift work, and conflicts feeding into Job Demands (leading to Exhaustion, Strain, and Complaints), while Support, Autonomy, Reward, Feedback, and Digital job resources feed into Job Resources (leading to Motivation, Dissociation, and Binding), with Organizational implications as outcome.*

One recent longitudinal study found that AI adoption can function as both a resource and a demand at once: it may improve productivity yet also introduce technostress that increases exhaustion and work-family conflict (Scholze & Hecker, 2024).

#### Conservation of Resources (COR) Theory

**COR theory** posits that people strive to preserve and build resources such as time, energy, skills, and social support, and that stress and burnout emerge when these resources are threatened or depleted (Hobfoll, 1989).

From a COR perspective, AI-related burnout can be seen as a "resource loss spiral." An always-on assistant can erode time and cognitive energy: each after-hours alert or new tool to master draws on finite resources. Without sufficient recovery, employees experience net loss, intensifying burnout over time.

**Figure:** *Conservation of Resources (COR) Theory diagram showing Physical, Mental, Social, and Spiritual resources as containers, with unit and family members as containers of resources, and resources continually drained away by stress.*

#### Evolving Nature of Burnout

Maslach and Leiter's work shows that people can experience distinct burnout profiles (Leiter & Maslach, 2016):

- **Overextended** - primarily exhausted but still engaged with their work
- **Disengaged** - more cynical, withdrawn, or doubtful of their impact

For intervention design: someone who is overextended may need workload relief and clearer boundaries, whereas a disengaged employee may need reconnection to purpose, re-skilling, or role redesign.

---

### Why Does It Matter?

#### Employee Well-being & Mental Health

Burnout is officially recognized by the World Health Organization as an occupational phenomenon resulting from chronic workplace stress (WHO, 2019). By taking away "low-cognition" breaks and adding new pressures, AI might actually accelerate the path to burnout. In interviews, tech workers describe feeling like *"the AI doesn't get tired between problems - I do."*

#### Productivity Paradox

While AI promises efficiency, burnout undercuts productivity in the long run. Microsoft's Work Trend Index found that employees who feel exhausted are **3.5x more likely to struggle with creative and strategic thinking** (Microsoft, 2023). Peak productivity from AI use can be short-lived: initial excitement about AI time-savings gave way to "workload creep" (Ranganathan & Ye, 2026).

#### Retention and Talent Risk

Burnout is a leading driver of attrition (Schaufeli & Bakker, 2004). One-third of workers said they are considering leaving their jobs because of increased stress from AI-driven work demands (Upwork Research Institute, 2024). The talent most adept with AI may also be the most at risk of burnout and turnover.

#### Equity and Inclusion

Burnout doesn't affect everyone equally. Not all employees have equal access to resources like training, support, or control over their schedules. The **Intersectionality Burnout Inventory (IBI)** examines how factors like demographic identity and belonging can shape burnout risk.

---

## 2. How Can We Measure Strain from AI?

Measuring AI-related burnout requires a multi-faceted approach, combining *subjective data* (how employees feel) with *objective data* (how they work). Traditional burnout assessments - such as the **Maslach Burnout Inventory (MBI)** or modern survey tools like **Microsoft Viva Glint** - can be complemented by **Microsoft Viva Insights behavioral metrics** that reveal work patterns associated with overload or disconnection.

### Employee Surveys (Glint & Burnout Scales)

It's critical to use validated, multi-dimensional measures - as Maslach & Leiter (2021) caution, burnout is complex and cannot be captured by a single question.

A 2024 study found that AI adoption heightened job stress, which then led to more burnout - but crucially, this happened primarily for employees with low self-efficacy in learning new tech (Kim & Lee, 2024).

#### Table 1: Strain and Burnout Survey Pulse

| Item Name | Purpose | Survey Item |
|-----------|---------|-------------|
| Resilience | Employee's ability to cope with stress, strain, and burnout | I am able to cope effectively with work-related stress. |
| Happiness | Employee's overall satisfaction working at the company | I am happy working at my company. |
| Workload Management | Employee's sense that assigned workload is reasonable | In general, I feel that my workload is manageable. |
| Work-Life Balance | Employee's sense of balance between work and personal life | I am able to successfully balance my work and personal life. |
| Boundaries | Employee's ability to disconnect from work during non-work time | I am able to disconnect from work during non-work time. |
| Team Support | Employee's assessment of support from teammates | I can get the help I need from my teammates and colleagues. |
| Teamwork | Employee's sense of cooperation and shared direction | Where I work, we feel part of a team that works together. |
| Recognition | Employee's satisfaction with acknowledgement received | I feel satisfied with the recognition or praise I receive for my work. |
| Role Clarity | Employee's understanding of expectations in their role | I clearly understand what is expected of me in my role. |
| Empowerment | Employee's sense of authority and autonomy | I feel empowered to make decisions regarding my work. |
| AI Confidence | Employee's confidence in using new AI tools | I feel confident in my ability to use new AI tools. |
| Burnout (Dolan et al., 2014) | Single-item self-rated burnout measure on a 5-point scale | Overall, based on your definition of burnout, how would you rate your level of burnout? (1 = No symptoms; 2 = Occasional stress, not burned out; 3 = Definitely burning out; 4 = Symptoms persistent and frequent; 5 = Completely burned out, may need help) |

### Viva Insights

#### Table 2: Key AI-Related Burnout Mechanisms, Corresponding Metrics, and Links to Theory

| AI-Related Burnout Mechanism | Viva Insights Metrics to Monitor | Related Burnout + Strain Constructs & Theories |
|------------------------------|----------------------------------|-----------------------------------------------|
| **Longer hours and blurred boundaries** (workload creep) | After-hours collaboration hours; Weekend collaboration hours; Urgent email/meeting hours | **Job Demands:** Increased workload and overtime leading to exhaustion. **COR:** Working longer damages recovery time, causing resource loss. |
| **Fragmented focus and information overload** (task switching, multitasking) | Uninterrupted hours; Multitasking hours; Interrupted hours; Conflicting meeting hours | **Job Demands:** High cognitive load and multitasking contribute to mental fatigue. **Technostress:** Reflects techno-overload and techno-interruption. |
| **Pressure to continuously learn** (learning time, technostress) | Learning hours; Available-to-focus hours | **Job Demands:** Cognitive demand and role overload. **Technostress:** Techno-complexity is a documented stressor. **Personal Resources:** Employees with greater self-efficacy handle this better. |
| **Pressure to work faster** (throughput intensity) | Urgent meetings & emails; Focus time booked vs. kept | **Job Demands:** Pace of work leads to stress and exhaustion. **Cultural Expectations:** "What AI makes possible becomes what's expected." |
| **Social isolation** (network weakening) | Diverse ties; Network size; Collaboration hours by team vs. solo | **Job Resources:** Social support is a key resource protecting against burnout. **Research evidence:** Heavy AI users often feel less psychologically safe and connected. |
| **Unnatural interfaces and interaction friction** (prompt burden) | AI tool session length vs. task completion; self-reported frustration scores; Copilot assisted hours with re-prompt rates; qualitative signals from focus groups | **Technostress:** Prompt friction reflects techno-complexity. **Flow disruption:** Interruptions to intuitive workflows reduce intrinsic motivation and increase fatigue. |
| **Higher cognitive load** (altitude sickness, skills expansion) | Copilot assisted hours vs. total hours worked; employee feedback via surveys or focus groups | **Effort-Reward Imbalance:** Fewer moments of relief or accomplishment. **Motivation & Meaning:** AI assistance reduced sense of meaning and intrinsic motivation (Wu et al., 2025). |

#### After-hours Work

Rising after-hours activity despite AI "efficiencies" should raise a red flag. Excess after-hours work is so predictive of burnout that the latest *Job Demands-Resources 3.0* research explicitly calls out after-hours connectivity as a driver of psychological distress (Li et al., 2025).

#### Uninterrupted Hours and Multitasking Hours

Microsoft's research shows **68% of workers already complain of too little focus time** (Microsoft, 2023). If generative AI tools generate even more "digital chatter," these focus metrics could worsen.

#### Learning Hours

If AI-related training time is high, it could mean ongoing cognitive load; if it's zero, that might be worse - implying people are not being trained yet still expected to use new tools.

#### Urgent Email Hours, Urgent Meeting Hours

A culture where these metrics rise may indicate everything is becoming "urgent" - often a side effect of an AI-fueled acceleration culture. Ethnographic research observed that after AI tools were implemented, employees felt *no one had the "luxury" to slow down or do deep thinking manually anymore*.

#### Diverse Ties, Internal Network Size, Network Metrics

A drop in diverse ties or network size over time may suggest that an employee's collaboration circle is shrinking. A study concluded that AI adoption pushed people into more isolated, siloed working patterns and emphasized the need for creating an "AI etiquette" (Ranganathan & Ye, 2026).

#### Copilot Assisted Hours and Hours Worked

If 20% of an employee's time is now "AI-assisted," but their total work hours haven't decreased (or have even increased), it suggests the AI might have simply enabled additional output rather than reducing strain.

In summary: if AI is truly helping, total work hours should stabilize or drop, focus time should increase, and stress indicators should not spike. If instead you see rising after-hours work, high interruptions, and worsening sentiment, it's a warning that AI's benefits are being blunted by burnout risks.

---

## 3. What Can Organizations Do to Mitigate AI-Induced Burnout?

### Rebalance Job Demands and Resources

If AI increases output expectations, revise goals and workflows to prevent perpetual escalation. If an AI assistant saves an employee 2 hours per day, don't immediately fill that time with 2 extra hours of new tasks. Use those gains to allow more recovery and creative time. Microsoft's own experience suggests employees need at least **30% of their week for focused, strategic work** (Reclaim AI, 2025; Microsoft, 2023).

### Provide Resource Boosters

Accompany any AI rollout with ample training, support, and time to learn. One study found that employees with high "AI self-efficacy" managed AI-related changes without increased burnout, whereas those with low self-efficacy struggled significantly. Give employees autonomy in how they use (or don't use) AI.

### No-After-Hours Policy

Strongly signal that employees are not expected to engage in work communications at night or on weekends (and turn off Copilot suggestions during those hours). Some companies implement periods of digital downtime.

### Focus Time & Deep Work

Use Viva Insights to schedule focus time for employees and respect it. Encourage "quiet hours" or meeting-free mornings/afternoons. Perhaps designate an official "No-Meeting Day." Leaders should model this behavior.

### AI-Ethics and Etiquette Training

Create guidelines for AI usage that promote well-being:

- Discourage sending AI-generated content to colleagues outside of work hours
- Encourage transparency when content is AI-created
- Don't expect immediate turnarounds just because a generative AI could produce a draft quickly

### Leverage AI to Reduce, Not Add, Work

Ensure that the introduction of AI is truly helping employees do less tedious work, not just do more work. Leaders should be wary of the subtle message: *"We can do twice as much now, so let's raise targets."* Companies need to resist the reflex to continuously raise the bar and instead use AI to redesign work for sustainability.

### Promote Social Connection and Support

- **Team Touchpoints:** Ensure teams still have regular check-ins, mentorship sessions, and informal interactions. Create "AI user group" forums for peer learning.
- **Manager Awareness:** Train managers to watch for signs of digital burnout. With Viva Insights, managers can get aggregated (privacy-protected) insights on their team's workload and collaboration patterns.
- **Celebrate Human Value:** Combat employee fears of "being replaced" by consistently emphasizing the unique value of human skills. Recognize interpersonal contributions that AI cannot provide.

### Measure and Track Employee Strain

Organizations should embed the survey items outlined above into an existing employee survey to establish consistent measurement of strain and burnout.

### Use AI to Fight AI-related Burnout

Microsoft Viva uses AI to generate personalized recommendations for taking regular breaks, having focus time, and scheduling "virtual commutes" to disconnect at day's end. Some organizations are exploring AI-driven chatbots for mental health check-ins or digital coaches (Durden et al., 2023; Chang et al., 2024).

---

## Choosing the Right Term - "Burnout" vs. "Strain" vs. "Technostress"

**"Burnout"** is a strong term, traditionally reserved for a severe, prolonged condition of workplace depletion. We use "AI-induced burnout" here because early evidence suggests the end-state does mirror true burnout with serious consequences.

Other useful terms:

- **Technostress** (or "AI technostress") - academic term for stress responses to using new technologies
- **Digital exhaustion** and **AI fatigue** - popular terms in media and industry commentary

These phenomena exist on a spectrum. An employee may start by feeling "AI fatigue" (tired of constant changes and information load), which if unaddressed could progress to AI-induced burnout.

---

## Conclusion: Designing AI Adoption for Sustainable Performance

AI-induced burnout is not a forecast: it is already present in the workforce. The stressors described in this paper are not hypothetical risks; they are the lived experience of workers today.

The core insight is simple but consequential: AI does not create burnout from scratch. Instead, it shifts the balance between job demands and resources. Left unmanaged, efficiency gains are silently reinvested into more work, not less.

Addressing this requires action at three levels:

1. **Measurement level:** Pair traditional burnout surveys with behavioral signals from platforms like Viva Insights. Detecting strain before it crystallizes into burnout is the difference between proactive management and reactive crisis response.
2. **Design level:** Resist the reflex to absorb AI's efficiency gains into expanded task scope. Protecting focus time, enforcing after-hours boundaries, and treating time savings as workload reduction are structural burnout prevention.
3. **Cultural level:** Reinforce that human judgment, creativity, social connection, and expertise remain irreplaceable. AI is a tool to support those capacities, not a substitute.

Organizations that get this balance right will not only avoid the burnout trap; they will unlock AI's deepest value: a workforce that is both more capable and more human.

---

## Bibliography

- Ali, S. A., Alaghbari, M. A., & Al Astal, A. Y. (2024). *Burnout and its impact on employee performance: A comprehensive systematic review.* Springer.
- Atlassian (2021). *Data analysis: Has the length of the workday changed during COVID?* Atlassian Blog.
- Chang, C. L., Sinha, C., Roy, M., & Wong, J. C. M. (2024). AI-led mental health support (Wysa) for health care workers during COVID-19: Service evaluation. *JMIR Formative Research, 8,* e51858. doi:10.2196/51858
- Deci, E. L., & Ryan, R. M. (2000). The "what" and "why" of goal pursuits: Human needs and the self-determination of behavior. *Psychological Inquiry, 11*(4), 227-268. doi:10.1207/S15327965PLI1104_01
- Demerouti, E., Bakker, A. B., Nachreiner, F., & Schaufeli, W. B. (2001). The job demands-resources model of burnout. *Journal of Applied Psychology, 86*(3), 499-512. doi:10.1037/0021-9010.86.3.499
- Derks, D., van Mierlo, H., & Schmitz, E. B. (2014). A diary study on work-related smartphone use, psychological detachment and exhaustion. *Journal of Occupational Health Psychology, 19*(1), 74-84. doi:10.1037/a0035076
- Durden, E., Pirner, M. C., Rapoport, S. J., Williams, A., Robinson, A., & Forman-Hoffman, V. L. (2023). Changes in stress, burnout, and resilience associated with an 8-week intervention with relational agent "Woebot." *Internet Interventions, 33,* 100637. doi:10.1016/j.invent.2023.100637
- Hernandez, J., Das Swain, V., Suh, J., McDuff, D., Amores, J., Ramos, G., Rowan, K., Houck, B., Iqbal, S. T., & Czerwinski, M. (2025). Triple Peak Day: Work Rhythms of Software Developers in Hybrid Work. *IEEE Trans. Software Eng., 51*(2), 344-354.
- Hobfoll, S. E. (1989). Conservation of resources: A new attempt at conceptualizing stress. *American Psychologist, 44*(3), 513-524. doi:10.1037/0003-066X.44.3.513
- Kahn, R. L., & Byosiere, P. (1992). Stress in organizations. In M. D. Dunnette & L. M. Hough (Eds.), *Handbook of industrial and organizational psychology* (Vol. 3, 2nd ed., pp. 571-650). Consulting Psychologists Press.
- Kim, B., & Lee, J. (2024). The mental health implications of artificial intelligence adoption: The crucial role of self-efficacy. *Humanities and Social Sciences Communications, 11*(1), 1-15. doi:10.1057/s41599-024-04018-w
- Leiter, M. P., & Maslach, C. (2016). Latent burnout profiles: A new approach to understanding the burnout experience and its consequences. *Journal of Occupational Health Psychology, 21*(4), 489-498. doi:10.1037/ocp0000023
- Li, Y., Zhang, T., Dong, M., & Ren, Z. (2025). Evolving the job demands-resources framework to JD-R 3.0. *Journal of Vocational Behavior.* doi:10.1016/j.jvb.2025.023X
- Liu, Y., Wu, S., Ruan, M., Chen, S., & Xie, X. Y. (2025, May). Research: Gen AI makes people more productive - and less motivated. *Harvard Business Review.*
- Maslach, C., & Jackson, S. E. (1981). The measurement of experienced burnout. *Journal of Occupational Behavior, 2*(2), 99-113. doi:10.1002/job.4030020205
- Maslach, C., & Leiter, M. P. (2016). Understanding the burnout experience: Recent research and its implications. *World Psychiatry, 15*(2), 103-111. doi:10.1002/wps.20311
- Maslach, C., & Leiter, M. P. (2021, March 19). How to measure burnout accurately and ethically. *Harvard Business Review.*
- Maslach, C., Schaufeli, W. B., & Leiter, M. P. (2001). Job burnout. *Annual Review of Psychology, 52*(1), 397-422. doi:10.1146/annurev.psych.52.1.397
- Microsoft (2023). *2023 Work Trend Index Annual Report: Will AI Fix Work?* Microsoft WorkLab.
- National Institute for Occupational Safety and Health (NIOSH). (2024). *Occupational burnout.* Centers for Disease Control and Prevention.
- Ragu-Nathan, T. S., Tarafdar, M., Ragu-Nathan, B. S., & Tu, Q. (2008). The consequences of technostress for end users in organizations. *Information Systems Research, 19*(4), 417-433. doi:10.1287/isre.1070.0165
- Ranganathan, A., & Ye, X. M. (2026). AI doesn't reduce work - it intensifies it. *Harvard Business Review.*
- Reclaim AI (2025). *Survey of over 10,000 Microsoft Office users: Desired vs actual focus time.* Reported in CFO.com.
- Salyers, M. P., et al. (2017). The relationship between professional burnout and quality and safety in healthcare: A meta-analysis. *Journal of General Internal Medicine, 32*(4), 475-482. doi:10.1007/s11606-016-3886-9
- Schaufeli, W. B., & Bakker, A. B. (2004). Job demands, job resources, and their relationship with burnout and engagement. *Journal of Organizational Behavior, 25*(3), 293-315. doi:10.1002/job.248
- Scholze, A., & Hecker, A. (2024). The job demands-resources model as a theoretical lens for the bright and dark side of digitization. *Computers in Human Behavior, 155,* 108177. doi:10.1016/j.chb.2024.108177
- Selye, H. (1936). A syndrome produced by diverse nocuous agents. *Nature, 138,* 32. doi:10.1038/138032a0
- Tarafdar, M., Tu, Q., Ragu-Nathan, B. S., & Ragu-Nathan, T. S. (2007). The impact of technostress on role stress and productivity. *Journal of Management Information Systems, 24*(1), 301-328. doi:10.2753/MIS0742-1222240109
- Tarro, L., et al. (2020). Effectiveness of workplace interventions for improving absenteeism, productivity, and work ability. *IJERPH, 17*(6), 1901. doi:10.3390/ijerph17061901
- Upwork Research Institute (2024). Upwork Study Finds Employee Workloads Rising Despite Increased C-Suite Investment in Artificial Intelligence.
- Upwork Research Institute (2025). *From tools to teammates: Navigating the new human-AI relationship.*
- World Health Organization (2019). *Burn-out in the ICD-11.*
- Wright, T. A., & Cropanzano, R. (1998). Emotional exhaustion as a predictor of job performance and voluntary turnover. *Journal of Applied Psychology, 83*(3), 486-493. doi:10.1037/0021-9010.83.3.486
- Wright, W. (2025, July 9). Heavy AI use at work has a surprising relationship to burnout, new study finds. *ZDNet.*
- Wu, S., Liu, Y., Ruan, M., Chen, S., & Xie, X. Y. (2025). Human-generative AI collaboration enhances task performance but undermines human's intrinsic motivation. *Scientific Reports, 15*(1), 15105. doi:10.1038/s41598-025-98385-2

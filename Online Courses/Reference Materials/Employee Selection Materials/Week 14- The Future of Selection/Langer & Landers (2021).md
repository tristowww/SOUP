Computers in Human Behavior 123 (2021) 106878

Contents lists available at ScienceDirect

Computers in Human Behavior
journal homepage: www.elsevier.com/locate/comphumbeh

The future of artificial intelligence at work: A review on effects of decision
automation and augmentation on workers targeted by algorithms and
third-party observers
Markus Langer a, *, Richard N. Landers b
a
b

Fachrichtung Psychologie, Universität des Saarlandes, Saarbrücken, Germany
Department of Psychology, University of Minnesota, Minneapolis, MN, USA

A R T I C L E I N F O

A B S T R A C T

Keywords:
Automated and augmented decision-making
Artificial intelligence
Algorithmic decision-making
Perceptions
Attitudes
Review paper

Advances in artificial intelligence are increasingly leading to the automation and augmentation of decision
processes in work contexts. Although research originally generally focused upon decision-makers, the perspec­
tive of those targeted by automated or augmented decisions (whom we call “second parties”) and parties who
observe the effects of such decisions (whom we call “third parties”) is now growing in importance and attention.
We review the expanding literature investigating reactions to automated and augmented decision-making by
second and third parties. Specifically, we explore attitude (e.g., evaluations of trustworthiness), perception (e.g.,
fairness perceptions), and behavior (e.g., reverse engineering of automated decision processes) outcomes of
second and third parties. Additionally, we explore how characteristics of the a) decision-making process, b)
system, c) second and third party, d) task, and e) outputs and outcomes moderate these effects, and provide
recommendation for future research. Our review summarizes the state of the literature in these domains,
concluding a) that reactions to automated decisions differ across situations in which there is remaining human
decision control (i.e., augmentation contexts), b) that system design choices (e.g., transparency) are important
but underresearched, and c) that the generalizability of findings might suffer from excessive reliance on specific
research methodologies (e.g., vignette studies).

1. Introduction
For over half a century, research and practice have explored how
decision-making automation, which refers to automating decisionprocesses without remaining human control, and augmentation, which
refers to the addition of system-support for human decisions, can in­
crease decision quality and efficiency (Benbasat & Nault, 1990; Meehl,
1954; Parasuraman et al., 2000; Raisch & Krakowski, 2021). In psy­
chology, those concepts date back until at least Meehl (1954), who
argued that it could be possible to translate decisions made by humans in
a subjective and informal way (clinical or holistic decision-making) into
a structured and formal way (mechanical or actuarial decision-making).
Nowadays, advances in artificial intelligence (AI)1 help to realize this
structured way of decision-making in many application areas. For
example, AI-based systems increasingly automate or augment aspects of

decision-making in medicine and management (Burton et al., 2020;
Longoni et al., 2019).
With good design and adequate testing, decision automation and
augmentation systems can often provide better and more efficient de­
cisions than even the most experienced human experts (Grove et al.,
2000; Kuncel et al., 2013). However, these benefits can be undermined
by poor system design, misuse, and reluctance to adopt systems by
first-party users (Dietvorst et al., 2015; Parasuraman & Riley, 1997). We
use the term first party to refer to people who use or interact with the
output of such systems to make decisions that affect other people.
First-party users are distinct from developers, who develop systems and
then monitor, maintain, and update them. They are also distinct from
upper-level managers, who may be responsible for implementation in a
more abstract way but do not work directly with the systems. Our
definition of first parties refers to people who have at least some direct

* Corresponding author. Universität des Saarlandes, Arbeits- & Organisationspsychologie, Campus A1 3, 66123, Saarbrücken, Germany.
E-mail address: markus.langer@uni-saarland.de (M. Langer).
1
We use artificial intelligence as an umbrella term, subsuming both classical manifestations like expert systems and deterministic human-programmed algorithms
with more recent ones, like machine learning and deep learning.
https://doi.org/10.1016/j.chb.2021.106878
Received 31 October 2020; Received in revised form 13 May 2021; Accepted 24 May 2021
Available online 29 May 2021
0747-5632/© 2021 Elsevier Ltd. All rights reserved.

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

control over whether and to what degree an artificial system will alter
the decisions they personally make. A prototypical first party at work is a
manager who uses a system to augment aspects of their decision-making
process regarding the personnel they manage. First parties often have
the freedom to question the quality of the systems they are employing
and deviate from their recommendations, relying instead or more
heavily upon their own judgment (Benbasat & Nault, 1990; Highhouse,
2008).
To date, the majority of research has investigated the perspectives of
first parties (Benbasat & Nault, 1990; Burton et al., 2020; Hoff & Bashir,
2015), despite them being only one part of a complex network of
stakeholders for almost any automation or augmentation system
(Jungmann et al., 2020; Langer et al., 2021). For this paper, two other
types of stakeholders are central. We call them second parties and third
parties. Second parties are people whose lives, work, and well-being are
directly affected and targeted, often without their consent or knowledge,
by automated and augmented decisions. Second parties cannot choose
whether they want to be affected by systems, their outputs, or decisions
based on those outputs unless they exit the decision-making context
entirely, such as by quitting their job. Prototypical second parties are
employees who receive work tasks from automated systems (e.g., Uber
drivers; Lee et al., 2015), employees whose shifts are automatically
determined (Uhde et al., 2020), and job applicants whose application
information is evaluated by first parties supported by automated systems
(Langer, König, & Hemsing, 2020). Third parties are people who observe
an automated or augmented decision without being directly affected by
that decision. Third parties are not directly affected by a particular de­
cision but may feel that they could become a second party in the future
or are concerned for the well-being, privacy, or some other character­
istic of second parties. For example, prototypical third parties are people
reading news articles on automated personnel selection practices or
people who hear from friends who are working in jobs where they
receive performance evaluations by automated systems (e.g., in algo­
rithmic management contexts; Wesche & Sonderegger, 2019). At higher
levels of analysis, the label “third party” can even apply to average
group, cultural, or societal reactions to specific decisions or policies,
such as global reactions to Amazon’s failure to automate resume
screening procedures without undue bias (Lecher, 2019).
Understanding the perspectives of second and third parties to auto­
mated and augmented decision-making at work constitutes a crucial
emerging line of research as decision automation and augmentation
increasingly determine how work takes place (Kellogg et al., 2020;
Murray et al., 2020). Even if decision automation and augmentation is
accepted by first parties, second and third parties can either foster or
impair success in practice (Healy et al., 2020). Specifically, second
parties might be influential in improving or sabotaging first-party trust
in the accuracy, efficiency, and consistency of automated and
augmented decisions by providing direct feedback to those first parties
(Lee et al., 2015). Similarly, third parties could protest or use negative
word-of-mouth on social media to attempt to shape public opinion. Such
behavior can discourage first parties from employing automation or
augmentation, can affect policy makers and regulators in a way that
influences the application of decision automation and augmentation in
practice, can diminish organizational reputation and even spur litiga­
tion. Although previous research has investigated first-party perspec­
tives on decision automation and augmentation (at least in certain
application areas Benbasat & Nault, 1990; Burton et al., 2020; Hoff &
Bashir, 2015; Onnasch et al., 2014), researchers only began to explore
effects on second and third parties in the beginning of the 2000s.
We contend that this area of research is now at a stage where a re­
view is crucial to reveal systematic issues and blind spots that need to be
addressed in the future. Consequently, the primary research questions
targeted with this review are: (1) how do automated and augmented
decisions affect second and third parties? (2) what moderates these ef­
fects? and (3) what are the next crucial steps to advance this research
area? In the following section, we describe our review methodology.

Resulting from our review, we present effects (on attitudes, perceptions,
behavior) of decision automation and augmentation on second and third
parties, including moderation by characteristics of the decision-making
process, of the system, of the second and third parties themselves, of the
tasks, and of outputs and outcomes. We conclude by highlighting limi­
tations observed across the literature and by providing recommenda­
tions for future research.
2. Review methodology
Prior to our search we defined the following inclusion criteria for
records considered in our review. Specifically, we did not restrict our
search to any specific timeframe and only included records written in
English. Moreover, we determined to only include research referring to
the use of systems automating or augmenting decision processes with
the potential to directly affect an identified second party. We also
restricted our review to research that collected or interpreted empirical
data, whether qualitative or quantitative, investigating the effects of
decision automation or augmentation on second- or third-party experi­
ences and behavioral outcomes. Furthermore, we only included research
that presented a comprehensible description of their study procedures
and analysis methodology, which was not universal. Given our research
questions, we focused our initial review on research about decisions
affecting people in work-related contexts. However, in the course of that
review, we found a variety of papers in the field of medical decisionmaking that appeared to be relevant to work-related contexts. Medi­
cine is somewhat unique in that systems may automate or augment
medical employees’ (e.g., physicians, nurses, technicians) decisions
about patients instead of about workers or job applicants. Yet because
we observed that research on augmented and automated medical
decision-making can be more advanced than for managerial decisionmaking, we decided to explicitly include medicine in this review.
Recognizing potential challenges in the generalizability of this research
to management, we discuss these examples only where necessary to
illustrate trends and theoretical avenues not yet explored in manage­
ment yet relevant to management theory.
We conducted our primary literature search on the SCOPUS database
and followed up with a search on Google Scholar. On each database, we
first conducted a preliminary search in which we identified relevant
sources and search terms, and which revealed that research relevant to
this review could be found in a variety of disciplines with different
publishing traditions. For instance, in psychology, scholars generally
value journal publications as scholarly contributions whereas confer­
ence proceedings are often unavailable and conference presentations are
minimally valued. In comparison, although computer science journals
exist, the majority of scholarly work is published in conference pro­
ceedings. Given our goals for an interdisciplinary review, we acknowl­
edged these varying publishing traditions and included published or
accepted work in conference proceedings, academic journals, and books.
For work found in online repositories that also cover preprints (e.g.,
arXiv), the authors discussed whether those articles should be included
based upon their individual quality. Furthermore, we talked to subject
matter experts from various disciplines to ensure that we identified the
most relevant outlets and conferences.
We required for inclusion at least one hit in each category among
search terms referring to a) the system, b) where the system is used or
who is affected, c) terms referring to reactions or perceptions by second
and third parties, and d) the study methodology. Within each of the
following lists of final search terms, multi-word terms were treated as
one search term and logically separated by “or.” For (a), we used:
“automated, automation, algorithm*, artificial intelligence, autonomous
machine, computer-assisted, computer-based, decision support system,
expert system, intelligent system, machine learning”. For (b), we used:
“advisor*, employee, individuals, job, management, manager, mana­
gerial, office, organization, physician, patients, workplace.” For (c), we
used: “accept*, belief, fairness, perceiv*, perception, react*, respond*,
2

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

systems may support first parties by, for instance, providing processed or
evaluated information (Acikgoz et al., 2020; Suen et al., 2019), leaving
the final decision at the discretion of the first party. As system control
increases, there is greater interaction between system and human
(O’Neill et al., 2020). For instance, in human-in-the-loop augmentation,
first parties and systems exchange information before an action is taken,
meaning that the system might request information from the human or
vice-versa (van Dongen & van Maanen, 2013). As system control in­
creases further, human control diminishes, until reaching full system
control. Although taxonomies regarding the automation and augmen­
tation decision-making were developed with first parties in mind (see
also Makarius et al., 2020; Parasuraman et al., 2000), these strategies
describing how decisions are made could also affect reactions by second
and third parties and were thus considered important for our review.
Specifically, we anticipated that second- and third-party experiences of
automated decisions vary by decision agency as control shifts from a
human to an automated agent. In our review, we ultimately used this
framework as an organizational tool and moderator of interest, as
classified in Table 1. Specifically, we categorize the reviewed papers into
papers that investigate automated, system-controlled decision-making
(Auto), decision augmentation, where human and system interact in
decision-making (Augm), and human decision-making (Human).

satis*“. For (d), we used: “applicants, employee, experiment, field study,
laboratory study, participants, subjects, worker.” Among papers deemed
relevant, we used a snowball technique (Wohlin, 2014), seeking addi­
tional relevant articles by scanning references within already-identified
articles, as well as scanning papers citing the respective paper (via
Google Scholar) and repeating this process until relevant references
were exhausted. Fig. 1 provides a flowchart outlining search steps taken
and the number of sources at each stage of filtering. Table 1 summarizes
the final set of studies that served as the basis of this review and also
provides contextual information regarding those studies.
Virtually all research that we identified on automated and
augmented decision-making at work related to human resource man­
agement tasks such as personnel selection or scheduling. We also
became aware of a substantial number of papers that came from the
extensive area of algorithmic management. Duggan et al. (2020, p. 119)
defined algorithmic management “as a system of control where
self-learning algorithms are given the responsibility for making and
executing decisions affecting labour, thereby limiting human involve­
ment and oversight of the labour process.” Although we sought to
include this research where relevant, it was often unclear whether re­
ported findings referred to participant experiences with automated de­
cisions or with the general work environment (e.g., being self-employed,
not having a contract; Galière, 2020; Möhlmann et al., in press), and we
only included research that was unambiguously focused upon reactions
to the augmented or automated decision-making itself per our inclusion
criteria. As a result, we included few algorithmic management papers
relative to the overall size of that research literature.
One insight that emerged from our review was the many ways that
decision automation and augmentation could be realized, which might
ultimately affect second- and third-party reactions. Most critically, we
found that a continuum between full human and full system control (or
automation) can be conceptualized. To formalize this continuum, Kaber
and Endsley (2004) presented a taxonomy defining it across ten distinct
levels, ranging from human control, in which a first party is in complete
control of a decision and all information used to make it, to full system
control, in which decisions are fully automated without human oversight
or intervention. Between those extremes, the specific role of both
humans and systems vary widely. At the lower end of system control,

3. Effects of decision automation and augmentation on second
and third parties
Our review of the effects of decision automation and augmentation
based on the studies presented in Table 1 is summarized in Table 2. For
clarity, we structured the results of our research, both in that table and
in the remainder of this section, in three components: attitudes, per­
ceptions, and behavior. Considered from the perspective of the study
participant in which these constructs are studied, perceptions refer to
how people immediately feel about and understand a system’s actions,
whereas attitudes refer to conscious evaluations of systems when
queried. Behavior is defined as actions taken by second and third parties
in response to their experiences or observations, respectively, of auto­
mated or augmented decision-making. Importantly, all three outcome
categories are likely to recursively affect each other (Fazio & Williams,

Fig. 1. Flow diagram of search steps. Dashed lines indicate the paths where identified records were excluded.
3

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Table 1
Overview of the number of participants, the context, the decision process, methodology, words used to refer to the system and system function in the reviewed studies.
Study

Participants

Context

Auto

Augm

Human

Methodology

Words used to refer
to the system

System functioning

Personnel selection

(x)

(x)

(x)

All quantitative
vignette

AI software using
advanced algorithms

225 US students

Personnel selection

(x)

(x)

(x)

Binns et al. (2018)
Study 1

19 UK, no further
information

Promotion

x

Study 2 + 3

Study 2: 325
Study 3: 65
Both UK Prolific
2090 American
Trends Panel
participants

Promotion

x

Screens resumes, conducts
interviews, rates
interviews, makes
recommendation to
manager
Conducts interviews, rates
interviews, makes
recommendation to
manager
Evaluates whether a
person should receive a
promotion
Same as in Study 1

Personnel Selection

x

A: 122 MTurk
B: 241 Mturk
C: 241 Mturk
US, Canada
D: 1499 UK
representative
sample from
Prolific
240 MTurk
US, Canada
964 MTurk
US Canada
155 Norwegian
tech workers
76 US students

Personnel selection

x

x

CompNet an
artificialintelligence-based
computer program

Personnel selection

x

x

Same as in 2A-D

Hires applicants

Personnel selection

x

x

Same as in 2A-D

Hires applicants

Personnel selection

x

x

Same as in 2A-D

Hires applicants

Personnel selection

x

x

Quantitative vignette

Automated screening
system

Gonzalez et al.
(2019)
Höddinghaus et al.
(2020)

192 US MTurk

Personnel Selection

x

x

Quantitative vignette

AI/ML tool

Reviews applications,
informs applicants
whether they were chosen
Makes hiring decision

333 German
workers

Compensation,
training,
promotion

x

x

Quantitative vignette

Computer program

Hong et al. (2020)

233 US Qualtrics

Personnel Selection

x

Quantitative vignette

AI, algorithm,
program, system

Howard et al. (2020)

22 US physicians

Scheduling

x

x

Automated approach

Langer, König, and
Hemsing (2020)

124 German
students

Personnel selection

x

x

Langer, König, and
Papathanasiou
(2019)

123 German
students

Personnel selection

x

x

Quantitative, reactions
to actual decisions
Quantitative and
participants record
interviews
Quantitative and
participants watch a
video

Langer, König,
Sanchez, and
Samadi (2019)

148 German
students and
working
individuals
120 German
students
(psychology and
computer science)
228 US MTurk

Personnel selection

x

x

Quantitative and
participants watch a
video

Virtual interview tool

Allocates and selects
workshops and training
courses
Allocates and determines
monthly bonuses and
promotion decisions
Chats with participants,
evaluates interview
questions and resume
information
Makes schedules, assigns
people to shifts
Analyzes and evaluates
participants interview
responses
Evaluates people,
provides feedback to
people, decides whether
applicants proceed to next
stage
Interviews applicants

Personnel selection

x

x

Quantitative and
participants watch a
video

Virtual interview tool

Interviews applicants

Personnel
selection,
Scheduling,
Performance

x

x

Quantitative and
qualitative vignette

Algorithm

Assigns tasks
Decides who should come
to work
Reviews resumes and

Decision-makingat work (general)
Acikgoz et al., 2020
298 US MTurk
Study 1

Study 2

Bigman et al. (2020)
Pilot Study

Study 2A-D

Study 3
Study 4
Study 5
Dineen et al. (2004)

Langer et al. (2018)

M. K. Lee (2018)

AI software using
advanced algorithms
All quantitative
vignette

Computer system
based on a computer
model
Computer system,
predictive model

All quantitative
vignette

Computer program

Computer
Virtual interview tool

Reviews resume and
interview information,
gives applicant scores,
applicants are hired based
on these scores
Hires applicants

(continued on next page)

4

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Table 1 (continued )
Study

Participants

Context
evaluation
Work assignment
Selection of
students for
university
admission
Personnel selection

Auto

Marcinkowski et al.
(2020)

304 German
students

Mirowska (2020)

184 students

Nagtegaal (2021),
Study 1

109 Dutch alumni

Reimbursement,
performance
evaluation

x

126 UK Prolific,
employees of
governmental
organizations
199 US MTurk

Pension
calculation, hiring

x

Layoffs and
promotions

Study 3

1654 US
university
employees
189 US MTurk

Study 4

Study 5

Augm

Human

Methodology

Words used to refer
to the system

(x)

x

Quantitative vignette

AI technology

x

x

Quantitative vignette

x

x

Quantitative and
qualitative vignette

AI interview
assessment software
Computer, using an
automated algorithm

x

x

Quantitative and
qualitative vignette

Computer, using an
automated algorithm

x

x

All quantitative
vignette

Employee
evaluation

x

x

An algorithm (i.e., a
computerized
decision-making
tool)
Human resource
algorithm

Bonus payment
determination

x

197 US students

Employee
evaluation

x

x

An algorithm (a
computerized
decision-making
tool)
Algorithm

213 US students

Personnel selection

x

x

Algorithm

Nolan et al. (2016)
Study 1

468 US MTurk

Personnel selection

Ötting & Maier
(2018) Study 1
Study 2

149 German
students
145 German
students
144 German
students
180 actual Chinese
interviewees

Task allocation
Allocation of
vocational training
Personnel selection

Uhde et al. (2020),
Study 2

51 German
healthcare
workers

Scheduling (who
gets vacation)

x

van Esch & Black
(2019)
Wang et al. (2020)

293 non-specified

Recruitment

x

579 US MTurk

Work evaluation
and promotion

x

Study 2

Newman et al.
(2020), Study 1
Study 2

Schmoll & Bader
(2019)
Suen et al. (2019)

x

(x)

x

x

Quantitative vignette

x

x

x

x

x

x

Quantitative vignette
including pictures
Quantitative vignette
including pictures
Quantitative vignette

Personnel selection

x

x
x

Decision-making at work (algorithmic management in gig and platform work)
Anwar et al. (2021)
19 Indian workers
Algorithmic
x
management

Quantitative, real
interviews for
simulated job
Quantitative and
qualitative vignette

Computer program
that uses a
mathematical
formula
Intelligent computer
Humanoid robot
Intelligent computer
Humanoid robot
Self-learning
algorithm
AI algorithm
System

Quantitative vignette,
survey
Quantitative vignette

AI

Qualitative interviews

Algorithm

Algorithm

Bucher et al. (2021)

12,294 posts on
forum

Algorithmic
management

x

Qualitative analysis of
forum posts

Algorithm

Galière (2020)

21 interviews with
French workers

Algorithmic
management

x

Qualitative interviews

Algorithm

Griesbach et al.
(2019)

955 US workers
survey
55 US workers
interviews

Algorithmic
management

x

Quantitative survey,
qualitative interviews

Algorithm

System functioning
selects top candidates
Evaluates employees
Analyzes applicant data
and recommends
approval or rejection of
applicants
Reviews interviews
Decides about travel
reimbursement
Evaluated performance of
employees
Calculates pensions
Scans CVs, interviews
candidates, hiring
Determines who gets
promoted or laid off
Decisions regarding
promotions, layoffs,
raises, pay cuts
Determines how
employee bonuses should
be allocated
Evaluates employee
performance data and
comes to a final decision
on the performance
review
Evaluates recorded
responses, top scorers will
be put on a short list
Combines data and
calculates overall scores
for candidates
Decides about task
allocation
Decides about allocation
of vocational training
Screens applicants’ social
media profiles
Analyzes interviews,
serves as a reference for
hiring decisions
Decides who gets vacation
but also encourages
workers to find a solution
for themselves
Analyzes applicant
information
Processes MTurkers work
history, decides over who
will become a Master
worker
Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process
(continued on next page)

5

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Table 1 (continued )
Study

Participants

Context

Auto

Jarrahi and
Sutherland (2019)

33 workers
98 threads from
forums
Probably all US
20 probably US
workers
Forum posts

Algorithmic
management

Methodology

Words used to refer
to the system

System functioning

x

Qualitative interviews,
documents websites,
forum posts

Algorithm

Algorithmic
management

x

Qualitative interviews,
forum posts

Algorithm

20 workers
19 clients
125 forum
discussions
21 US drivers
12 US passengers
128 posts in online
forums
132 official blog
posts
15 informal, 4
formal interviews
with US and UK
workers
15 informal, 19
formal interviews
with US workers
8 formal
interviews with
employees and
engineers
32 interviews with
Scottish workers

Algorithmic
management

x

Qualitative interviews,
forum posts

Algorithm

Algorithmic
management

x

Algorithm

Algorithmic
management

x

Algorithmic
management

x

Qualitative data from
semi-structured
interviews, analysis of
posts in online forums,
analysis of blog posts
by the companies
Qualitative interviews,
post entries; informal
and formal interviews
and blog posts
Qualitative interviews

Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process

Algorithmic
management

x

Qualitative interviews

Algorithm

Ravenelle (2019)

31 US workers
from two
platforms

Algorithmic
management

x

Qualitative interviews

Algorithm

Wood et al. (2019)

107 interviews
with workers
679 workers in
survey
Southeast Asia and
Sub Saharan
countries
58 Australian
workers

Algorithmic
management

x

Qualitative interviews,
survey

Algorithm

Algorithmic
management

x

Qualitative interviews

Algorithm

Assigns work tasks,
provides information,
manages evaluation
process

All quantitative
vignette

Computer program

Tells the physician
whether they should order
an X-ray
Determines risk of
diseases, advices
treatment
Assigns likelihood of
diagnoses
Assigns likelihood of
diagnoses
Decides about medical
treatment

Jarrahi et al. (2020)

Kinder et al. (2019)

Lee et al. (2015)

Möhlmann and
Zalmanson (2017)
Möhlmann et al. (in
press)

Myhill et al. (2021)

Venn et al. (2020)

Decision-making in medicine
Arkes et al. (2007),
347 US students
Study 1

All diagnosis

Augm

Human

(x)

x

Algorithm

Algorithm

Study 2

128 US students

(x)

x

Computer program

Study 3

74 US patients

(x)

x

Computer program

Study 4

131 US medical
students
958 Dutch,
representative
sample

(x)

x

Computer program

Araujo et al. (2020)

Bigman & Gray
(2018), Study 3
Study 6
Study 7
Study 8
Study 9
Haan et al. (2019)

240 US MTurk

239 US MTurk
100 US MTurk
240 US MTurk
Within: 201
Between: 409
Both US MTurk
20 US patients

Treatment (and
others)

x

x

Quantitative vignette

Treatment

x

x

All quantitative
vignette

x
x
x
x
Diagnosis

(x)

x

x
x
x
x
x

Qualitative semistructured interviews

Artificial
intelligence,
computers, computer
programs
HealthComp an
autonomous
statistics-based
computer system
Same as in Study 3
Same as in Study 3
Same as in Study 3
Same as in Study 3
AI system, computer

Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process

Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process
Assigns work tasks,
provides information,
manages evaluation
process

Decides whether to
perform a surgery
Same as in Study 3
Same as in Study 3
Same as in Study 3
Same as in Study 3
Analyzes radiological
images and autonomously
evaluates scans
(continued on next page)

6

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Table 1 (continued )
Study

Participants

Context

Auto

Hamilton et al.
(2019)

46 US patients

Diagnosis and
treatment

x

Jutzi et al. (2020)

298 German
patients
2196 Swedish
women and actual
patients
98 Australian
patients
228 US students

Diagnosis

x

Methodology

Words used to refer
to the system

System functioning

Group interviews,
participants watched a
video
Qualitative and survey

IBM Watson for
oncology
AI

Analyzes patient data,
gives treatment
recommendation
Analyzes melanoma

Diagnosis

x

x

Qualitative survey

Computer-only

Breast cancer diagnosis

Diagnosis

x

x

Automated system

Diagnoses retinopathy

Diagnosis

x

x

Diagnosis

x

x

Study 3

3a: 205, 3b: 227,
3c: 235 all US
MTurk

Diagnosis

x

x

Study 4
Study 5

100 US MTurk
286 US MTurk

Diagnosis
Diagnosis

x
x

x
x

Study 6

243 US MTurk

Treatment

x

x

Computer uses an
algorithm
Computer capable of
artificial intelligence
3a: robotic
dermatologist is a
computer program
3b: robotic nurse,
interactive animated
avatar
3c: Robotic surgeon
Same as 3a
Robotic
dermatologist
Computer

Stress diagnosis

103 US MTurk

Quantitative, reactions
to actual decision
All quantitative
vignette

Study 7

294 US MTurk

Treatment

x

x

Study 8

401 US MTurk

Diagnosis

x

x

Study 9

179 US MTurk

Diagnosis

x

Study 10

No information

Diagnosis

Study 11

92 US MTurk

Various

x

Nelson et al. (2020)

48 US patients

Diagnosis

x

x

x

Palmeira & Spassova
(2015), Study 1
Study 2

36 US panel

University
admission
Diagnosis and
treatment

x

x

x

(x)

x

Diagnosis,
university
admission

x

x

x

Diagnosis and
treatment

x

Jonmarker et al.
(2019)
Keel et al. (2018)
Longoni et al. (2019)
Study 1
Study 2

Study 3

Palmisciano et al.
(2020)

Pezzo & Pezzo
(2006), Study 1
Study 2
Promberger & Baron,
2006, Study 1
Study 2

Between: 117 US
panel
Mixed: 75 US
panel
Medical: 41 US
panel
Admission: 42 US
panel
20 UK patients,
qualitative
107 UK patients
and relatives
59 US students
166 US medical
students and 154
students
68 US panel

All diagnosis

434 US students

Diagnosis and
treatment
Diagnosis and
treatment
Treatment

Study 2

109 US students

Study 3

Shaffer et al. (2013),
Study 1

Srivastava et al.
(2019)

80 US panel

Augm

x

x

Human

x

x

(x)

x

(x)

x

x

x

x

x

Qualitative semistructured interviews
All quantitative
vignette

Computer program
uses an algorithm
Computer program
uses an algorithm
AI dermatologist that
is an algorithm
Robotic
ophthalmologist,
computer that uses
an algorithm
Well-trained
algorithm
AI program, AI tool
Computer program
Computer program
and decision aid
Medical software

3a: skin cancer screening
3b: diagnosis
3c: helps human to
conduct surgery

Skin cancer screening
Skin cancer screening
Recommendation of
bypass operation
Recommendation of
bypass operation
Recommendation of
bypass operation
Skin cancer screening
Dry eyes diagnosis

Gives advice
Automated diagnosis or
support of diagnosis
Provides a favorability
score to rank candidates
Determines risk of
diseases advices treatment
Informs about symptoms/
candidate characteristics
and probability of illness/
success
Analyzes images, works
out surgical plan, alarms
about risks, supports
surgeon, operates patient
autonomously
Combines test results

Qualitative and
quantitative survey
with vignettes

AI system

All quantitative
vignette

Computer decision
aid
Computer decision
aid

All quantitative
vignette

Computer program

Provides recommendation

Computer program

All quantitative
vignette

Decision aid
[computer program]

Provides recommendation
or autonomous decision
Determines whether
patient should have an Xray
Determines whether
patient should have an Xray
Calculates a score that
tells the probability for
appendicitis
Skin cancer screening

(x)

x

Treatment

(x)

x

Decision aid
[computer program]

189 US students

Diagnosis

(x)

x

Computer-based
diagnostic aid

100 US MTurk

Diagnosis

x

Stress diagnosis

Quantitative, decision
between different
forms of algorithms

Data driven
algorithm

Makes a diagnosis

(continued on next page)

7

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Table 1 (continued )
Study

Participants

Context

Auto

Stai et al. (2020)

264 US
participants

Diagnosis and
treatment

x

Tobia et al. (2021)

1356 US
representative
sample
218 US IT students

Treatment

x

All diagnosis

(x)

x

(x)

x

Wolf (2014), Study 1
Study 2

101 US IT students

Yokoi et al. (2020)

272 Japanese
college graduates

Diagnosis and
treatment

York et al. (2020)

216 UK patients

Diagnosis and
treatment

Augm

x

x

Human

Methodology

Words used to refer
to the system

System functioning

x

Quantitative survey

AI

Quantitative vignette

AI

Analyzes images, gives
recommendation on
further treatment
Recommends
chemotherapy drug dosis

All quantitative
vignette

Computer program

x

Quantitative vignette

AI

x

Quantitative survey

AI

Computer program

Assigns likelihood of
diagnoses
Assigns likelihood of
diagnoses
Analyzes symptoms,
identifies disease,
suggests medical
treatment
Helps human to analyze
X-rays, helps deciding
how to manage injuries

Note. Auto = this study investigates automated, system-controlled decision-making; Augm = this study investigates decision augmentation, where humans and systems
interact in decision-making; Human = this study investigates human decision-making. (x) = unclear description of decision-making situation. The column “Words used
to refer to the system” consists of quotes of the respective papers. For papers including vignette studies, this highlights the words used to describe the system to
participants within the respective vignette studies.

1986), so none should be considered in isolation.

2019; Jutzi et al., 2020; Nelson et al., 2020).
Further important with respect to ability, in the case of fullyautomated decisions, second parties seem to be initially unsure about
the performance of automated systems in high-stakes decision contexts.
For example, in qualitative studies, several representatives of second
parties reported that they expect more accurate whereas others expect
less accurate diagnoses when using decision automation in medicine
(Jutzi et al., 2020; Nelson et al., 2020). People also seem to question the
validity of automated decisions, and patients may even explicitly call for
scientific evidence showing that they can trust automated systems (Haan
et al., 2019). Höddinghaus et al. (2020) found no differences regarding
people’s evaluation of human versus system data processing capabilities
in different managerial tasks. However, humans were evaluated as more
adaptable to changing circumstances which the authors consider
another facet of ability. Since automated systems might not only aim to
increase diagnostic accuracy but also decision-making efficiency, effi­
ciency perceptions can also contribute to overall evaluations of the
ability (i.e., performance) of automated systems. People’s expectations
are split regarding efficiency of automated systems as some studies
showed that people expect increasing diagnostic speed and earlier
detection of diseases (Haan et al., 2019; Hamilton et al., 2019; Jutzi
et al., 2020; Nelson et al., 2020) whereas others found no differences in
expectations regarding waiting time expectations (Arkes et al., 2007; V.
A.; Shaffer et al., 2013; Wolf, 2014). Similarly, high expectations
regarding efficiency were reported in studies investigating workers’
beliefs about algorithmic management (Galière, 2020).
Regarding the trustworthiness facet integrity, people seem to pre­
dominantly believe systems to possess high integrity. People seem to
believe that systems have less discrimination motivation than humans
(Bigman et al., 2020) which seems to be related to beliefs that systems
possess less agency (Bigman & Gray, 2018) and with the belief that
systems do not have an own agenda they follow (Myhill et al., 2021).
Furthermore, Höddinghaus et al. (2020) also found that people perceive
systems to be less biased than human decision-makers. It is important to
stress that attitudes regarding integrity of automated systems are closely
related to what we discuss under perceptions of consistency and objec­
tivity. Specifically, if people believe the decision agent to have less
discrimination motivation, to be less biased, they might also expect (at
least initially) that decision processes will be more consistent and
objective. However, this is contingent on second- and third-party beliefs
that systems can lead to lower bias, and this attitude in the population at
large is, given the lack of familiarity with automated decision-making,
likely unstable.

3.1. Attitudes
We identified three major types of attitudes in relation to decision
automation and augmentation: evaluations of trustworthiness, reduc­
tionism, as well as reluctance regarding automation of moral decisions.
3.1.1. Evaluations of trustworthiness
A number of studies investigate second- and third party evaluations
of trustworthiness facets that relate to the system or the decision-maker
receiving system support (J. D. Lee & See, 2004; Mayer et al., 1995).
Specifically, in the terminology of Mayer et al.’s (1995) facets of trust­
worthiness, the reviewed papers predominantly investigate evaluations
of ability and integrity, and some papers also evaluate benevolence. In
the reviewed studies, ability relates to perceived performance of a sys­
tem or the abilities of a decision-maker supported by a system. Integrity
refers to the believe that the first party or system is unbiased in their
decisions. Benevolence relates to the evaluation of how much a first
party or a system will consider humans’ needs and how much they
“care” about individuals. Second parties will consider the combination
of those trustworthiness facets when they decide whether to trust or rely
on the respective automated or augmented decision (Höddinghaus et al.,
2020; J. D. Lee & See, 2004).
Overall, results regarding assessment of the trustworthiness facet
ability are inconclusive. Performance and ability evaluations are central
to the trustworthiness of first parties and of automated systems (J. D. Lee
& See, 2004). In medical decision-making, there is research investi­
gating second-party perceptions of the ability of human experts using
systems for decision-making. For instance, research indicates that sec­
ond and third parties can ascribe lower ability to first parties that use
systems in their decisions (Arkes et al., 2007; Wolf, 2014). However,
there is no consensus whether those reactions are specific to first parties
consulting systems versus consulting other human experts (V. A. Shaffer
et al., 2013), if the magnitude of reactions is dependent upon the level of
automation (Palmeira & Spassova, 2015), or on the behavior of the first
party (Pezzo & Pezzo, 2006). When explicitly comparing augmented
decisions with unaided expert judgement, using systems can even result
in better perceptions of the abilities of the first party (Hamilton et al.,
2019; Palmeira & Spassova, 2015). In addition, second parties seem to
be concerned about human deskilling, such as by worrying that physi­
cians will become less able to diagnose without augmentation systems
and eventually lose their ability to detect system errors (Hamilton et al.,
8

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Table 2
Effects of decision automation and augmentation on second and third parties.
Outcome
Attitudes
Evaluations of
trustworthiness

Reductionism
Reluctance regarding
automation of moral
decisions
Perceptions
Fairness and Justice

Organizational
attractiveness
Accountability and
responsibility
Being under system
control vs. autonomy
Privacy concerns
Behavior
Reverse engineering of
automated decisions
Creating workarounds
Collective action
Embracing the system

Current consensus

Sample research question

Selected sources

People are sometimes unsure about the ability of humans using
systems, tend to question the ability of automated systems for
decisions, but also sometimes expect systems to be equally or
more able and efficient as humans. Additionally, people believe
that systems have higher integrity and are less biased than
humans. Furthermore, systems are perceived as less benevolent,
but evidence is limited.
Decision automation neglects unique conditions, qualitative
information, and decontextualizes as well as quantifies decision
processes.
Evidence is limited but people do not appear to want decision
automation for decisions with obvious moral components.

What are the contexts where people are
initially sceptical about ability of automated
systems for decisions?

Höddinghaus et al. (2020);
Nelson et al. (2020)

Is it possible to alter attitudes regarding
reductionism?

Longoni et al. (2019);
Newman et al. (2020)

Why are people sceptical about decision
automation for decisions with moral
components?

Bigman and Gray (2018)

Mixed results; more studies have found negative fairness
perceptions, but some have found positive effects or no effects,
this seems to depend on the task at hand. Decision automation
generally leads to negative interpersonal justice perceptions, to
better perceptions of consistency, and to lower perceived
controllability. Effects regarding informational justice are
inconclusive.
Mixed findings regarding organizational attractiveness.

What moderates effects on fairness and
justice perceptions?

Howard et al. (2020);
Newman et al. (2020); Ötting
& Maier (2018)

How do other perceptions and attitudes
translate to organizational attractiveness?

Research suggests that decision automation and augmentation
affect accountability and perceived responsibility but findings are
limited to vignette studies and mostly stem from the medical
domain.
In algorithmic management, there is a tension between being
under constant system control but at the same time feeling
autonomy because of having no human boss.
Automated decision-making appears to lead to greater privacy
concerns, but the literature is small.

What are practical implications of potentially
diffused responsibility between decisionmakers and automated systems?

Langer, König, &
Papathanasiou (2019);
Newman et al. (2020)
Pezzo & Pezzo (2006); Tobia
et al. (2021)

Some second parties appear to try to reverse engineer (e.g.,
through experimentation) the functioning of automated systems.
Some second parties try to use system peculiarities for their own
benefit or to circumvent control by the automated system if the
outcome is valued.
Some second parties use online forums to share knowledge,
complain, and engage in collective action against automated
systems.
People try to keep their own ratings within systems high, embrace
system functionality as being fair and efficient.

As a final facet of trustworthiness, reviewed papers also investigate
benevolence. In general, there are only few papers investigating this
facet, but those find that people ascribe lower benevolence to systems
than to human decision-makers. Specifically, people believe that sys­
tems do not consider individual needs and do not care about individuals
(Höddinghaus et al., 2020; Yokoi et al., 2020). This might also relate to
what we discuss in the section on reductionism as well as lower per­
ceptions of interpersonal justice.
Evaluations of trustworthiness finally result in effects on intentions
to trust. Regarding trust, automated decisions seem to predominantly
result in less trust compared to human decisions and this seems to apply
to decision-making at work (Höddinghaus et al., 2020; M. K. Lee, 2018)
and in medicine (Palmisciano et al., 2020; York et al., 2020). However,
this lack of trust might be contingent on a variety of moderator such as
characteristics of the task that is to be automated (e.g., personnel se­
lection vs. scheduling; M. K. Lee, 2018; image analysis vs. medical
treatment recommendations; Palmisciano et al., 2020).
In sum, existing research regarding decision automation and
augmentation and issues of trustworthiness as well as trust comes mostly
from the field of medical decision-making. Although questions emerge
in decision-making at work (Höddinghaus et al., 2020; Nolan et al.,
2016), it has not yet received the same empirical attention. Given un­
clear and sometimes contradictory results in the field of medical

How does the tension between control and
autonomy affect workers’ job satisfaction?

Möhlmann & Zalmanson
(2017); Griesbach et al., 2019

Why do people perceive privacy concerns for
automated decisions?

Langer, König, and
Papathanasiou (2019)

Does reverse engineering improve perceived
control of automated decisions?
How do automated systems and bypassing
behavior coevolve? Who seeks workarounds?

Kinder et al. (2019)Lee et al.
(2015)
Möhlmann et al. (in press);
Wood et al. (2019)

Would this kind of collective action also
translate to employees in organizations?

Möhlmann et al. (in press)

Does embracing the system undermine
scrutinizing of system outputs?

Galière (2020); Wood et al.
(2019)

decision-making, as well as given trustworthiness evaluations as po­
tential antecedents regarding perceptions of automated and augmented
decisions, this is as an important line of future research in the work
context.
3.1.2. Reductionism
Our review suggests that second and third parties believe that deci­
sion automation suffers from reductionism (Newman et al., 2020).
Specifically, people seem to believe that systems consider more factors
overall but neglect unique conditions, qualitative information, and de­
contextualize as well as quantify decision processes (Longoni et al.,
2019; Newman et al., 2020). This might also be a cause of several
negative perceptions by second and third parties as Newman et al.
(2020) found negative fairness perceptions to automated decisions due
to the fact that second parties believe that systems do not or cannot
adequately use qualitative information (e.g., leadership skills). Simi­
larly, Longoni et al. (2019) found that people are reluctant to use
automated systems for medical diagnoses as they think that those sys­
tems neglect their unique individual conditions (but see Yokoi et al.,
2020 who did not find significant differences regarding uniqueness
neglect). Similarly, Hamilton et al. (2019) report that their participants
believed that only human physicians have a holistic view of individual
patients which makes systems inadequate for personalized care. In sum,
9

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

those findings speak towards the attitude that automated decisions are
reductionist and dehumanizing. Importantly, this is also a reason for
resistance to use automated systems from the perspective of first parties
(Dawes et al., 1989; Grove & Meehl, 1996). First, second, and third
parties all appear to assume that automated decisions suffer from
reductionism.

Second, procedural justice perceptions were affected positively and
negatively. This mixed picture makes sense since procedural justice re­
fers to different facets where some are more likely to positively affected
by decision automation and augmentation, whereas others are more
likely impaired (Nagtegaal, 2021). On the positive side, automated de­
cisions improve perceptions of processes as being based on accurate
information, being performed consistently, as well as free of bias (Col­
quitt, 2001), for instance in the context of job interview performance
evaluations (Acikgoz et al., 2020; Langer, König, Sanchez, & Samadi,
2019; Marcinkowski et al., 2020). Even decision augmentation can lead
to more perceived consistency in decision-making (Jutzi et al., 2020;
Nelson et al., 2020; Nolan et al., 2016). Moreover, in algorithmic
management contexts, automated evaluation was perceived as an effi­
cient and objective way to evaluate workers’ performance (Galière,
2020).
On the negative side of procedural justice perceptions, automated
decisions seem to impair perceptions of whether it is possible to express
one’s views and feelings about a process, appeal processes (e.g., appeal
negative customer ratings; Griesbach et al., 2019; Möhlmann et al., in
press; Myhill et al., 2021), and more generally control decision processes
and outcomes. Specifically, reduced perceived control of automated
decisions was found for people in personnel selection (Langer, König, &
Papathanasiou, 2019; M. K. Lee, 2018), where they seem to be unsure
how to affect automated decision processes in a way that could improve
their performance ratings (Acikgoz et al., 2020; Langer, König, Sanchez,
& Samadi, 2019). In algorithmic management processes, perceived lack
of controllability was often associated with a lack of perceived trans­
parency of what contributes to decision outcomes by automated systems
(Möhlmann et al., in press; Myhill et al., 2021; Veen et al., 2020). In these
cases, the lack of transparency was usually described as an intentional
design choice by platform providers in order to better control the
workforce and to prevent people from gaming the system (Galière, 2020;
Möhlmann et al., in press). Future research could thus investigate
methods to increase perceived controllability without enabling workers
to game respective systems.
Third, results regarding informational justice, which refers to
perceived openness, honesty, and transparency in decision processes
(Colquitt, 2001), were inconclusive. As we have just mentioned, quali­
tative results in algorithmic management contexts indicate that people
might perceive low informational justice as they do not understand how
algorithmic management decisions work (Griesbach et al., 2019; Lee
et al., 2015 ; Möhlmann et al., in press; Myhill et al., 2021; Veen et al.,
2020). In personnel selection, there is tentative evidence that people
perceive automated decisions as less open towards the applicants than
human decisions, although there were no differences in perceived in­
formation known about the decision processes (Acikgoz et al., 2020).
Whereas those findings indicate that informational justice might be
lower in the case of automated decisions, there is also hope that auto­
mated processes could enhance informational justice (Höddinghaus
et al., 2020). Specifically, transparency of decisions could increase if
automated system were designed to be transparent (Lee et al., 2015) or
at least to provide better explanations of their recommendations than
humans do (Jutzi et al., 2020).

3.1.3. Reluctance regarding automation of moral decisions
Although empirical research is limited, both second and third parties
do not appear to want decision automation for decisions with obvious
moral components. Specifically, over a various set of studies, Bigman
and Gray (2018) found that people do not want systems to make moral
decisions in medicine (e.g., decisions about treatments) and attributed
this to reduced agency and reduced ability to feel and sense.
3.2. Perceptions
We identified five major types of perceptions: fairness and justice,
organizational attractiveness, accountability and responsibility, super­
vision vs. autonomy, and privacy invasion.
3.2.1. Fairness and justice
In line with growing interest regarding algorithmic fairness,
accountability, and transparency (Shin & Park, 2019), fairness and
justice perceptions reflect the most commonly investigated outcomes in
the reviewed papers. For perceptions of fairness, observed effects were
mixed but predominantly negative. Some of the studies in personnel
selection scenarios based on job interviews found no differences in
fairness perceptions between human and automated decisions (Langer,
König, & Hemsing, 2020; Suen et al., 2019). In a school admission
context, Marcinkowski et al. (2020) found stronger fairness perceptions
for automated compared to human decisions. Similarly, Howard et al.
(2020) reported stronger fairness perceptions after the implementation
of an automated scheduling system for residents at a hospital compared
to scheduling by human decision-makers. However, most of the
reviewed studies found that people perceive automated decisions as less
fair than human decisions across personnel selection, performance
evaluation, and scheduling scenarios (Dineen et al., 2004; Langer,
König, & Papathanasiou, 2019; M. K. Lee, 2018; Newman et al., 2020;
Uhde et al., 2020; Wang et al., 2020). Additional qualitative findings
indicate that fairness was a concern in algorithmic management contexts
(Lee et al., 2015; Myhill et al., 2021) where different design choices
resulted in more, or less perceived fairness (Griesbach et al., 2019).
Overall, the mixed findings regarding fairness suggest that there are
moderators that have not yet been sufficiently investigated, a concept
we revisit in greater detail later in this review.
Regarding justice, three of the four dimensions of organizational
justice theory (Colquitt, 2001) were commonly studied: interpersonal,
procedural, and informational justice. Overall, people seem to expect
both positive and negative effects regarding the single justice facets. This
seems to be closely related to what we have discussed regarding atti­
tudes towards decision automation (i.e., reductionism, evaluations of
trustworthiness) which supports previously found close relation be­
tween trustworthiness evaluations and perceptions of justice (Colquitt &
Rodell, 2011).
First, interpersonal justice, which refers to the perception of being
treated with dignity and human warmth in decision processes (Colquitt,
2001), was generally harmed by automation. Studies on automated job
interviews found lower social presence, two-way communication, and
less adequate interpersonal treatment in automated interviews (Acikgoz
et al., 2020; Langer, König, Sanchez, & Samadi, 2019; Langer, König, &
Papathanasiou, 2019). Similar findings come from the area of medical
decision-making where patients fear a lack of human touch, less ability
to ask questions, and that systems might not provide potentially nega­
tive outcomes (e.g., diagnoses) in a sensitive manner (Haan et al., 2019;
Nelson et al., 2020).

3.2.2. Organizational attractiveness
Organizational attractiveness refers to perceptions of how second
and third parties perceive organizations that sponsor algorithmic de­
cisions. In the case of personnel selection, organizational attractiveness
seemed to be partly driven by fairness and justice perceptions of the
algorithmic decision (Ötting & Maier, 2018) and were predominantly
negative. Similarly, Acikgoz et al. (2020) found lower organizational
attractiveness, job pursuit intentions, and stronger litigation intentions
when using decision automation in interviews with mediations princi­
pally through decreased chance to perform and decreased two-way
communication quality. Similarly, automated interviews have been
associated with reduced organizational attractiveness compared to
10

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

videoconference interviews, and social presence and fairness seem to be
the most important mediators in this effect (Langer, König, Sanchez, &
Samadi, 2019; Langer, König, & Papathanasiou, 2019). In contrast to the
negative findings from selection contexts in organizations, in university
admissions, the use of systems was associated with better organizational
reputation (Marcinkowski et al., 2020).
This suggests unexplored moderators affecting people’s perceptions
of organizational attractiveness. For instance, we could imagine that
interpersonal justice facets are especially important in the case of job
interviews (Langer, König, & Papathanasiou, 2019) such that in this
context, automated decisions impair organizational attractiveness. In
contrast, there might be situations where consistency and objectivity are
more important and where the perceived benefits of automated de­
cisions could result in higher attractiveness (e.g., in resume screening as
a situation where there is usually no human contact; Marcinkowski
et al., 2020).

system control can be perceived as providing more autonomy than
comparable supervision by a human boss (Anwar et al., 2021; Griesbach,
Reich, Elliott-Negri, & Milkman, 2019; Möhlmann et al., in press;
Möhlmann & Zalmanson, 2017; Wood et al., 2019). We need to
emphasize that parts of these perceptions could also be affected by the
overall work environment and by platform providers such as Uber or
Upwork selling jobs on their platforms as being “entrepreneurial”. This
might contribute to workers’ self-identity as being autonomous and
having flexible working hours when they are actually following strict
rules and algorithmic control (Galière, 2020; Jarrahi et al., 2020).
3.2.5. Privacy invasion
Automated decision-making can lead to perceptions of privacy in­
vasion under certain circumstances, but this conclusion is based on few
studies. Privacy concerns are commonly debated when using automated
decisions, as the technologies enabling decision automation and
augmentation often rely on automatic evaluation of sensitive data pro­
vided by second parties. In the context of personnel selection, privacy
concerns may be higher for decision automation (Gonzalez et al., 2019;
Langer, König, Sanchez, & Samadi, 2019; Langer, König, & Papathana­
siou, 2019). However, the reviewed literature provided no empirical
evidence as to the reasons why second parties would be more concerned
providing private data to an automated system than to a human
decision-maker evaluating the same data. Additionally, in algorithmic
management, there is significant discussion of worker concern with
constant surveillance, but privacy concerns seem to be of lesser impor­
tance in this area (Galière, 2020; Griesbach et al., 2019).

3.2.3. Accountability and responsibility
Accountability and responsibility are commonly discussed for the use
of automated systems for high-stakes decisions across disciplines (Flo­
ridi et al., 2018; Kellogg et al., 2020; Mittelstadt et al., 2016). A common
concern is that there will be an accountability gap when humans rely on
automated systems as there might be situations where it is not clear who
is accountable for errors (Raji et al., 2020). Whereas there is only scarce
research in work-related contexts, the question of who is accountable for
failures of automated systems in medicine was raised by participants in
the reviewed studies, although developers and first parties were
commonly believed to be ultimately accountable (Haan et al., 2019;
Nelson et al., 2020).
Whereas those results speak to perceptions of actual legal account­
ability, other studies found that people attributed different re­
sponsibility to decision-makers who use automated systems for decisionmaking. For instance, systems can deflect part of the blame for negative
medical outcomes but only if physicians follow system advice (Pezzo &
Pezzo, 2006; Tobia et al., 2021). Tobia et al. (2021) conclude that this
may constitute an incentive to follow recommendations by automated
systems as this could shield against legal accusations. On the side of
second parties, being affected by a decisions that was shared between
human and system can result in being unsure who to blame for negative
outcomes of decision automation and augmentation (Jutzi et al., 2020;
Nolan et al., 2016). Specifically, some second parties perceived less
decrease in their own perceived responsibility when systems provided
them with recommendations about medical treatment in comparison to
when humans gave this recommendation (Longoni et al., 2019; Prom­
berger & Baron, 2006). Authors of the respective papers argued that this
might be attributable to diffused responsibility; the second-party may
not know who to blame in the event of an unfavorable outcome resulting
from following and automated recommendation. Future work could
investigate whether those effects are moderated by characteristics of the
system (e.g., system accuracy; Lowe et al., 2002) as previous research
was unspecific about conditions that affect perceived responsibility.

3.3. Behavior
We identified four commonly studied classes of behavior in response
to automated decision-making: reverse engineering of automated de­
cisions, creating workarounds, collective action, and embracing the
system. Research that investigates behavioral reactions to decision
automation and augmentation predominantly comes from the area of
algorithmic management in gig and platform work, which focuses on
behaviors related to perceived controllability of automated decisions
(see Kellogg et al., 2020; or Möhlmann et al., in press, for overviews on
control in relation to algorithmic management). Second parties try to
enhance their understanding of automated management processes
through reverse engineering and knowledge sharing in online forums,
and building a personal or shared understanding this way may increase
perceived controllability (Jarrahi et al., 2020; Lee et al., 2015;
Möhlmann et al., in press; Myhill et al., 2021). Furthermore, based on
their understanding of automated processes, second parties may use
peculiarities of automated systems to create workarounds that either
avoid penalties or increase their income (Kinder et al., 2019; Myhill
et al., 2021; Veen et al., 2020; Wood et al., 2019), and success with such
methods may also increase perceived controllability. Other attempts to
increase perceived controllability may involve initiating collective ac­
tion in regard to automated processes that affect millions of other second
parties (Lee et al., 2015). However, in most studied situations, there was
a sufficient power imbalance so as to force second parties to embrace
automated decisions or give up their incomes. This lack of control
sometimes even led workers to describe automated decisions as the
fairest possible way to work assignment and evaluation (Galière, 2020).

3.2.4. Being under system control vs. autonomy
The tension between being controlled by an automated system versus
perceived autonomy at work it especially prevalent in algorithmic
management contexts. Specifically, workers are under constant sur­
veillance and controlled by algorithmic management but at the same
time perceive flexibility and autonomy in their work (Galière, 2020;
Griesbach et al., 2019; Möhlmann et al., in press). These perceptions
seem to be partly due to the fact that workers do not have a human boss
telling them what to do (Anwar et al., 2021; Griesbach et al., 2019;
Möhlmann et al., in press; Möhlmann & Zalmanson, 2017; Wood et al.,
2019). Instead, there is an automated system providing instructions,
information, and evaluation. Although this leads to workers being aware
of being under constant evaluation (Bucher et al., 2021; Kinder et al.,
2019; Ravenelle, 2019; Veen et al., 2020), it seems that being under

3.3.1. Reverse engineering of automated decisions
Second parties often do not understand how algorithmic manage­
ment systems work and do not know how they can affect system out­
comes favorably (Lee et al., 2015; Myhill et al., 2021; Veen et al., 2020).
To increase understanding, there are examples of second parties trying
to reverse engineer automated decision-making process through exper­
imentation (Kinder et al., 2019;Lee et al., 2015 ; Möhlmann et al., in
press). Workers may change inputs into the system in order to see how
outputs change and build a mental model of system functioning (Jarrahi
11

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

& Sutherland, 2019). Similarly, workers have logged in as alternative
user types in algorithmically managed systems to see how their changes
influence what potential customers see (Jarrahi & Sutherland, 2019).
Reverse engineering seems to serve the purpose of increasing under­
standing of the automated management system to increase controlla­
bility of the system.

moderators: system versus human control and first-party behavior in
decision process. Whereas there is only scarce research on work-related
decisions regarding these topics, results from medical decision-making
support them (Jutzi et al., 2020; Nelson et al., 2020). For future
research, it will be central to investigate psychological processes
explaining the effects reported in this section. For example, why do
people prefer human control in certain application contexts? An expla­
nation based on findings from the perspective of first parties (Grove &
Meehl, 1996) might be that humans fear that machines decide the fates
of human beings. Other interpretations in line with findings regarding
attitudes and perceptions might be that human control will improve
single case decision-making, will be less dehumanizing, and will allow
the consideration of qualitative factors (i.e., there might be hope that
humans can mitigate reductionism). Additionally, people might hope
that human decision-makers can be influenced to one’s own benefit (i.e.,
are more “controllable”). Furthermore, with a human decision-maker
available, second and third parties may perceive someone who is a
contact person to whom they can direct complaints and who is
accountable for negative outcomes.

3.3.2. Creating workarounds
Second parties may try to use bugs and (possibly undocumented)
features of algorithmic management systems to create workarounds. For
instance, a person may try to bring the interaction with their clients
away from the influence of the automated system, for instance, by
directly interacting with customers (Jarrahi & Sutherland, 2019;Lee
et al., 2015). Additionally, people try to use technical findings to their
own benefit. For instance, users may log out of a system that is tracking
them to receive better evaluations (e.g., because systems cannot track
reckless driving behavior or the actual time a worker spend on a task;
Jarrahi & Sutherland, 2019; Lee et al., 2015; Möhlmann & Zalmanson,
2017; Wood et al., 2019). In another example, Upwork workers who
inputted five 1-h blocks of work discovered they would have greater
system benefits than if they inputted those same hours as a single 5-h
block (Jarrahi & Sutherland, 2019). These ways of how to game the
system are under constant change as platform providers try to fix
respective loopholes which makes it necessary for workers to search for
new ways to create workarounds (Galière, 2020; Möhlmann et al., in
press).

4.1.1. System vs. human control
Earlier in this paper, we anticipated the distinction between
augmented and automated decision-making to be of importance. Indeed,
people call for human control in high-stake decisions and seem to pre­
dominantly perceive augmented as favorable to automated decisions.
For instance, second parties perceive decisions where first parties only
have the option to consult an automated system as fairer compared to
full automation or to decisions where first parties can only slightly
change automated decisions (Newman et al., 2020). Furthermore, Suen
et al.’s (2019) finding of no negative reactions to algorithmic
decision-making in personnel selection might be because participants
were informed that the algorithmic evaluation only served as a reference
for the human decision-maker. Another perspective on the effects of
human control comes from Nagtegaal (2021). She found in hiring or
performance evaluation that only automating decisions negatively
affected perceptions; augmentation had no negative effects. In contrast,
less human control led to stronger fairness perceptions in mathematical
tasks (e.g., travel reimbursement decisions). This suggests that there are
also tasks where more system control can be beneficial.
Additional evidence on system versus human control is generally
lacking for decisions at work; however, research in medical decisionmaking also suggests that humans prefer having a human involved in
decision-making for certain tasks. Second parties often specify that
systems should be more of an informant or second opinion than the final
trigger of a decision (Haan et al., 2019; Hamilton et al., 2019; Jutzi et al.,
2020; Palmisciano et al., 2020; Stai et al., 2020) and call for
human-system symbiosis (Nelson et al., 2020). Supporting those find­
ings, Bigman and Gray (Study 8; 2018) found that if systems only advice
human physicians, there is a higher likelihood that people accept de­
cisions. However, many people still preferred the human expert to
decide without automated support (see also York et al., 2020) (for
further support of the positive influence of human control see Jonmarker
et al., 2019; Longoni et al., 2019; Palmeira & Spassova, 2015).

3.3.3. Collective action
Numerous studies provide evidence that second parties are inclined
to share knowledge and evidence with other second parties and to keep
up to date about potential changes in functions of the systems they work
under (Jarrahi & Sutherland, 2019;Lee et al., 2015 ; Möhlmann & Zal­
manson, 2017; Myhill et al., 2021). This is often done via online forums,
which may also provide a feeling of social embeddedness. Second parties
use such forums to onboard new workers, to complain about the system,
to form alliances in protest, and to raise their collective voice against the
usually inaccessible layer of developers behind the system (Lee et al.,
2015). In such forums, second parties also sometimes organize resis­
tance against the automated management system or to try to collectively
game the system (Tassinari & Maccarrone, 2020). For instance,
Möhlmann and Zalmanson (2017) describes a case where Uber drivers
tried to collectively reduce work effort in order to increase demand
which would in turn increase surge pricing to the benefit of worker pay.
Even more drastic manifestations of collective actions are worker strikes
(Möhlmann et al., in press; Tassinari & Maccarrone, 2020).
3.3.4. Embracing the system
Several studies report that workers in algorithmic management
embrace algorithmic management systems. They try to keep their
evaluations within the system high (Bucher et al., 2021; Kinder et al.,
2019; Ravenelle, 2019; Wood et al., 2019). Furthermore, they perceive
systems as being efficient and objective and thus recommend other
workers to play along with the rules of the system as this is the fairest
possible evaluation of workers’ performance (Galière, 2020).

4.1.2. First-party behavior in decision processes
Following versus rejecting advice by automated systems seems to
affect second-party attitudes and perceptions with regard to the first
party. For instance, Arkes et al. (2007) found that rejecting automated
recommendations can lead to lower trustworthiness assessment of the
decision-maker. Furthermore, when augmented decision result in an
unfavorable outcome for second parties, people seem to ascribe more
fault to physicians when they reject automated advice compared to
when they follow the advice (see also Tobia et al., 2021). This finding
might be grounded in attributions of responsibility that might be lower
for when humans follow automated systems compared to when they
ignore the advice (Lowe et al., 2002).

4. Moderators of effects on second and third parties
Table 3 provides an overview of characteristics of the decisionmaking process, of the system, of the second- and third parties them­
selves, of the tasks, and of the outcomes. In each case, we either report
research directly testing these moderators or observed differences be­
tween studies adopting different approaches.
4.1. Characteristics of the decision-making process
We identified two process characteristics as potentially influential
12

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Table 3
Factors affecting the effects of decision automation and augmentation on second and third parties.
Category

Current consensus

Sample research question

Selected sources

Why do people prefer human control in certain
tasks?

Nagtegaal (2021);
Newman et al. (2020)

What are psychological processes underlying
different perceptions of first parties who reject
or follow advice?

Tobia et al. (2021);
Pezzo & Pezzo (2006)

All else being equal, humans prefer human control but when
system accuracy becomes better, humans start to prefer
system control.
Inconclusive findings.

How do different system performance measures
(e.g., accuracy, bias) affect perceptions of
systems?
What are trade-offs of providing explanations
and transparency to second parties?

Bigman & Gray (2018);
Longoni et al. (2019)

Information about the developer can affect reactions to the
system.
Characteristics of second and third parties
Experience, familiarity,
Mixed effects with some studies finding no effects other
education
finding better perceptions of automated decisions with more
experience, familiarity, education.
Personality and traits
Inconclusive effects of studies investigating a range of
potentially influential traits (e.g., perceived uniqueness, trait
privacy concerns)
Gender
There is a tendency that females react less favorable to
automated decisions.
Task characteristics
The respective task affects reactions, but it is unclear what
exactly it is about tasks that affect second- and third-party
reactions. Research indicates that it is a mix of stakes of the
task, tasks that require human versus mechanical skills,
perceived quantifiability, and familiarity with automated
systems for the respective tasks.
Output and outcome
Different kinds of outputs (e.g., standard vs. non-standard)
characteristics
affect perceptions. Unfavorable outcomes lead to negative
reactions irrespective of human or automated decisions.
However, overall research on effects of outputs and outcomes
is scarce.

Do information about the development process
(e.g., about training data) also affect reactions?

Binns et al. (2018);
Langer et al. (2018);
Newman et al. (2020)
Bigman et al. (2020);
Wang et al. (2020)

Does experience, familiarity, and education
affect perceived control and understanding?

Langer et al. (2018);
Wang et al. (2020)

What are influential personality facets and
traits and why are they influential?

Longoni et al. (2019)

What are the underlying influences that may
contribute to gender differences?
What are the dimensions of tasks that affect
second and third parties with respect to
automated and augmented decisions?

Araujo et al. (2020);
York et al. (2020)
M. K. Lee (2018);
Nagtegaal (2021)

What are further characteristics of system
outputs (e.g., output comprehensibility) that
affect perceptions?

Wang et al. (2020);
Hong et al. (2020)

Characteristics of the decision-making process
System vs. human control
People call for human control in high-stake decisions and
seem to perceive augmented as more favorable than
automated decisions. However, this evidence stems mainly
from medical decision-making and may depend on the focal
task.
First-party behavior in decision
Rejecting vs. following advice by automated systems seems to
process
affect second-party perceptions of the first party.
System characteristics
System performance
Understandability and
transparency through
information and explanation
Information about the developer

4.2. System characteristics

when system accuracy becomes better, humans start to prefer system
control (Longoni et al., 2019). For instance, patients would prefer
AI-based medical systems when they are more accurate than a human
expert (Haan et al., 2019; Jutzi et al., 2020). However, if systems are
similarly accurate like humans, people indicated that they would prefer
human over automated decisions. For instance, Bigman and Gray (2018,
Study 9) showed that it is necessary to make accuracy advantages of
automated systems salient (i.e., in a within-subject comparison to the
human expert) and strongly different (i.e., 75% human vs. 95% system)
in order to find preference for system decisions. Potentially, this could
indicate that expectations regarding system performance are unrealis­
tically high (Merritt et al., 2015). The study by Bigman and Gray even
showed that in the case of a clear advantage of the automated system,
28% of participants indicated that they still would prefer the inferior
human decision. In a similar vein, Longoni et al. (2019) showed that
people are less sensitive to accuracy when deciding between human and
automated decisions versus when deciding between two human
decision-makers. Specifically, they found that accuracy differences lead
to stronger effects when deciding between two humans (i.e., participants
more strongly favored the human showing higher accuracy) compared
to when deciding between a human and an automated system where the
system shows higher accuracy.

System characteristics that affect reactions to automated and
augmented decision processes are system performance, understand­
ability and transparency through information and explanation, as well
as information about the developer. Overall, only a small number of
specific system design features have received attention. In the context of
algorithmic management, research shows possible implications of
different design choices when comparing different algorithmic man­
agement platforms (Griesbach et al., 2019; Ravenelle, 2019). For
instance, design choices may affect perceived fairness, perceived au­
tonomy, job satisfaction, and overall work performance (Galière, 2020).
However, as respective papers compare different platforms, without
systematically investigating design options (see Ravenelle, 2019), it is
hard to tell which design differences between the platforms led to
different worker reactions. Consequently, systematically assessing ef­
fects of design options for automated systems in decision-making and
their effects on second and third parties could receive more attention
(Landers & Marin, 2021).
4.2.1. System performance
System performance affects second-party reactions to automated
decisions. Whereas, accuracy (e.g., prediction accuracy) is the pre­
dominant measure of system performance in the reviewed studies, there
are others (e.g., efficiency, lack of bias) that could also be considered to
be performance measures and that may become increasingly important
in new application areas of decision automation and augmentation (e.g.,
in management, medicine) (Srivastava et al., 2019).
All else being equal, humans prefer human control in decisions but

4.2.2. Understandability and transparency through information and
explanation
Whereas research, practice, regulatory bodies, and ethical guidelines
commonly call for understandability and transparency of systems and
their outputs, and assume that this positively affects outcomes for sec­
ond parties (e.g., Dineen et al., 2004; Jobin et al., 2019), the reviewed
13

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

findings in relation to understandability and transparency are incon­
clusive. For example, Wang et al. (2020) informed their participants that
there are “information online available” about an automated decision
process which led to participants perceiving biased procedures as even
less fair compared to where no such information was available. In a
more direct investigation of the effects of explanations, Binns et al.‘s
(2018) between-subject study showed only weak effects of different kind
of explanations on justice perceptions. In their within-subject study,
explicitly comparing different kinds of explanations resulted in more
negative justice perceptions for case-based explanations compared to
other explanations. On the one hand, this indicates that without direct
comparison between different versions of explanations, their effect on
justice perceptions might be negligible. On the other hand, it is impor­
tant to test the effects of different kinds of explanations as some might
lead to comparably negative outcomes. Furthermore, Langer et al.
(2018) found that providing information regarding what input variables
an automated interview system uses increases perceived transparency
but at the same time decreases perceived organizational attractiveness.
Similarly, Newman et al. (2020) findings indicate that whereas for
human decisions high transparency leads to more fairness, for auto­
mated systems this effect is reversed.
A possible explanation for the overall inconclusive effects is that
more understandability without also perceiving more controllability
might be negative (Ananny & Crawford, 2018). For instance, research
shows that only providing information about variables the system con­
siders as inputs might be detrimental if people see that they might not be
able to control those inputs (e.g., their voice tone) (Grgić-Hlača et al.,
2018; Langer et al., 2018; Newman et al., 2020). Another possible
interpretation is that people might have different expectations regarding
transparency of systems compared to humans as decision-makers. For
instance, people may not even expect explanations from systems
whereas explanations to increase transparency of a decision are some­
thing natural in the interaction with human decision-makers (Lombrozo,
2011; Zerilli et al., 2018) – a lack of explanations could be interpreted as
intentional distortion in the case of a human decision-maker (Schlicker
et al., 2021). Another possibility might be that people believe they un­
derstand human decision-making processes although those are eventu­
ally also black box decisions (Zerilli et al., 2018). We see potential
regarding research on understandability of systems which is also re­
flected in the current boom in research on explainable artificial intelli­
gence (XAI) (Miller, 2019). Future research needs to investigate how to
optimally induce understanding through the provision of explanation
and information. In this regard, we need to understand under what
conditions, in what contexts, and with what trade-offs (e.g., gaming
respective systems; Jarrahi & Sutherland, 2019; (Lee et al., 2015);
Möhlmann et al., in press) increasing understanding of systems happens
(Langer et al., 2021).

4.3.1. Experience, familiarity, education
Overall, experience, familiarity, and education are related to un­
derstandability or perceived control as people with more experience and
familiarity with computers, programming, and higher education might
believe that they understand how systems work which might give them
more confidence that they can control system processes and outputs
(Jonmarker et al., 2019; Langer et al., 2018). Intuitively, this could lead
to better perceptions of automated decisions. However, there are mixed
effects as some studies found no effects whereas others found better
perceptions of automated decisions with more experience, familiarity,
and education. For instance, Langer et al. (2018) found no correlation of
computer experience and any of their perceived justice variables. Wolf
(2014) showed that even IT students derogate physicians who use
automated systems. In contrast, Wang et al. (2020) showed that com­
puter literacy positively correlates with fairness perceptions regarding
automated decisions. Similarly, Jonmarker et al. (2019) found that
better understanding of new technology is associated with better re­
actions to decision automation in breast cancer screening. Furthermore,
Gonzalez et al. (2019) showed that familiarity with AI can mitigate
negative reactions to automated decisions. Additionally, Araujo et al.
(2020) showed that programming knowledge is associated with more
positive evaluations of usefulness and fairness of automated decisions.
Additionally, Bigman et al. (2020) showed that people with stronger AI
knowledge were less morally outraged by algorithmic bias which could
be interpreted as either more positive evaluations of automated de­
cisions or as a positivistic bias in relation to automated systems as they
assume that biased system outputs are not associated with the system
but maybe just reflect actual differences between people. Furthermore,
Wang et al. (2020) found that less educated participants react more
strongly to unfavorable outcomes by automated decision processes.
Relatedly, higher education levels seem to be associated with better
reactions to automated decisions in medicine (Jonmarker et al., 2019;
York et al., 2020).
4.3.2. Personality and traits
The reviewed papers investigated a range of traits potentially influ­
ential (e.g., perceived uniqueness, trait privacy concerns, locus of con­
trol) with inconclusive effects. For instance, Araujo et al. (2020) showed
that trait privacy concerns were negatively associated with fairness and
positively with perceived risk of using automated decisions. V. A. Shaffer
et al. (2013) showed that people with a high internal locus of control
react more negatively to physicians using computerized aid. Further­
more, Longoni et al. (2019) found that the more unique a person feels
the less they want to be assessed by automated systems.

4.2.3. Information about the developer
Information about the system developer might affect second and
third parties. For instance, Wang et al. (2020) showed stronger negative
effects of biased outcomes when a system was developed by an “out­
sourced team” compared to an in-house developer team. Similarly,
Bigman et al. (2020) found third parties perceive more moral outrage
regarding biases by automated systems when the developing organiza­
tion was describes as sexist. Finally, information about the prestige of
the developer can lead to better reactions when experts use respective
systems to augment their decisions (Arkes et al., 2007).

4.3.3. Gender
There is inconclusive evidence but a tendency that females react less
favorable to automated decisions. Whereas Hong et al. (2020) found no
differences between male and female participants with respect to
automated decisions involving unfair gender discrimination, Dineen
et al. (2004) and York et al. (2020) showed stronger preferences for
human versus automated decisions for female participants. Wang et al.
(2020) showed that females react more strongly towards unfavorable
outcomes in automated decisions. Finally, Araujo et al. (2020) report
that females tend to perceive automated decisions as less useful. Overall,
it might be possible that unconsidered confounding variables (e.g., fa­
miliarity with respective systems) might have contributed to the re­
ported effects of gender on reactions to automated decisions.

4.3. Characteristics of second and third parties

4.4. Task characteristics

We identified experience, familiarity, education, personality and
traits as well as gender as characteristics of second and third parties that
moderate effects of automation and augmentation.

Previous research indicates that it is a mix of the perceived stakes of
the task, perceptions of tasks requiring human versus mechanical skills,
perceived quantifiability of task-related information, and familiarity
with automated systems for the respective tasks that affect second- and
third-party perceptions. First, people might react differently to systems
14

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

used in high versus low-stakes contexts (Langer, König, & Papathana­
siou, 2019). Specifically, third parties reacted more negatively to auto­
mated decisions used for personnel selection (high-stakes) compared to
training situations (low-stakes) (Langer, König, & Papathanasiou, 2019).
Similarly, Longoni et al. (2019; Study 10,2 supplementary material)
showed more resistance to automated systems in high-stakes medical
decision (see also Palmisciano et al., 2020; York et al., 2020). In
contrast, Araujo et al. (2020) found that automated decisions are
perceived as fairer in high-stakes situations in health and justice.
Additionally, Ötting and Maier (2018) found no differences in reaction
to task allocation (low-stakes) and allocation of vocational training
(high-stakes) between human and automated decisions. A different
perspective on the influence of the stakes comes from Srivastava et al.
(2019) who showed that in high-stakes contexts, people value accuracy
more than unbiasedness of system decisions.
Second, perceptions might differ in tasks that require human versus
mechanical skills (M. K. Lee, 2018). For instance, human skills would be
subjective and intuitive judgement as well as emotional capabilities
whereas mechanical skills would be quick and potentially objective
processing of large amounts of data (Castelo et al., 2019; M. K. Lee,
2018). For example, systems seem to be more accepted for image pro­
cessing tasks in medicine compared to treatment recommendations
(Palmisciano et al., 2020; York et al., 2020). Furthermore, M. K. Lee
(2018) found that humans perceive less fairness, less trust, and more
negative emotional reactions when an automated system conducted a
task that required human skills (i.e., personnel selection, work evalua­
tion) compared to tasks that required mechanical skills (i.e., work
assignment, scheduling). Unfortunately, in all above examples (imaging
vs. treatment recommendation; selection vs. scheduling) the respective
tasks might not only differ with respect to requiring human skills, but
could also be perceived to differ with respect to the stakes involved.
Third, related to the idea of human vs. mechanical skills, quantifi­
ability may influence how people react to decision automation (Nagte­
gaal, 2021). Specifically, if it is difficult to measure task components (e.
g., predictors, criteria) with face valid numbers, people seem to believe
that it is a bad idea trying to automate it through systems using math­
ematical algorithms. This interpretation is in line with the reviewed
findings (Lee et al., 2015; Newman et al., 2020; Ötting & Maier, 2018).
Especially, Nagtegaal’s (2021) studies support this distinction; for
highly quantifiable, mathematically deterministic tasks (e.g., deter­
mining travel reimbursement given provided documentation), she
showed a decline in perceived fairness as human control increased. In
contrast, for less quantifiable (but also more complex; Nagtegaal, 2021)
tasks (e.g., hiring), decision automation was perceived as least fair, and
there was no difference in perceived fairness between human and
augmented decision-making, possibly because people did not believe
that adding the system would provide any benefit to such a task.
Additional support for this task dimension comes from research inves­
tigating first-party reactions. For first parties, previous research found
that they reject automated decisions in uncertain domains (Dietvorst &
Bharti, 2020) but prefer automated decisions for quantifiable tasks
(Castelo et al., 2019).
The complexities involved with task characteristics dimensions are
illustrated by Longoni et al. (2019; Study 11, supplementary material),
who found that participants preferred human decisions throughout all
investigated application areas but that the strength of this preference
differed across the areas in the following rank order from the greatest
difference between human and automated decisions to the smallest:
legal, health, home, fashion, home décor, restaurants, movies, music,
financial decisions. This rank order reveals that high versus low-stakes is
a potentially central distinction that affects human reactions to auto­
mated decisions, yet it is clearly not the only meaningful distinction,

considering financial decisions would usually also be considered
high-stakes. Instead, financial decisions may represent a quantifiable
task requiring mechanical skills, one done better by a system than by a
human. Familiarity with automated decisions might be another
dimension which could explain the rather favorable reactions to auto­
mated decisions for movies and music. Overall, we conclude that a
necessary theoretical advance to move forward is the development of a
taxonomy of task differences relevant to algorithmic decision-making.
Without such a taxonomy, distinctions like these will continue to pla­
gue unambiguous conclusions in such experiments.
4.5. System output and decision outcome characteristics
System outputs and decision outcomes serve as stimuli for secondparty perceptions. We distinguish here between the outputs of a sys­
tem (i.e., the actual recommendation, decision) and outcomes for in­
dividuals (e.g, favorable vs. unfavorable). Although research on the
recursive effects of outputs and outcomes on attitudes, perceptions, and
behaviors remains scarce, future research should investigate such effects
given previous research on first-party perceptions showing that outputs
and outcomes affect first-party attitudes, perceptions, and behavior in
relation to systems (e.g., evaluations of trustworthiness, trust, accep­
tance, use) (Hoff & Bashir, 2015; J. D. Lee & See, 2004). It is likely that
these effects persist in the second- and third-party context.
Hong et al. (2020) showed that biased outputs by systems can have
comparably stronger negative effects on people’s perceptions of decision
automation compared to descriptions referring to system quality.
Additionally, Tobia et al. (2021) showed that following versus rejecting
standard versus non-standard treatment recommendations (i.e., out­
puts) by automated systems differently affected physicians’ perceived
responsibility. On the side of outcomes for second parties, unfavorable
and unjust outcomes lead to negative reactions irrespective of human or
automated decisions (Gonzalez et al., 2019; Hong et al., 2020). For
example, Gonzalez et al. (2019) found no difference in organizational
attractiveness in the case of negative outcomes (i.e., imagine a job
application was rejected) but that participants preferred human de­
cisions in the case of positive outcomes. Even expected outcome favor­
ability seems to have an effect (Wang et al., 2020). Specifically, Wang
et al. (2020) showed that participants who expect to fail an automated
evaluation also perceive the general process to be less fair than the ones
who expect to pass.
5. Limitations and guidelines for future research
Overall, our review revealed inconsistencies in findings with respect
to several commonly investigated attitudes and perceptions and high­
lighted important moderators (see Tables 2 and 3 for related sample
research questions). For instance, findings regarding trustworthiness
attitudes (especially for the facet ability) differed between the studies,
perceptions of fairness seem to be moderated by the task at hand, and
there are ambiguous effects of transparency and explanation provision.
Furthermore, few researchers explicitly examine the relationships
among attitudes, perceptions, and behavior, generally focusing upon
either perceptions, or attitudes, or behaviors. Moreover, although
research indicates that human control in decision processes alters sec­
ond- and third-party attitudes and perceptions, the psychological pro­
cesses underlying this effect remain open for investigation. In addition
to the inconsistencies found in the reviewed studies that hopefully
stimulate future research, the following subsections present five broad
observations regarding limitations of the reviewed studies together with
guidelines to advance future research on decision automation and
augmentation.
5.1. Research design that allows for generalizability

2

We thank the authors for providing us with additional unpublished results
from their study.

Overall, the generalizability of the reviewed studies is unclear.
15

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Specifically, most relied on vignettes, generally asking research partic­
ipants to imagine being in or observing an automated or augmented
decision process. Vignette studies can be difficult to design in order to
draw meaningful conclusions, and they often do not accurately mirror
real-world processes (Atzmüller & Steiner, 2010). Furthermore, for most
studies it remained unclear how familiar people were regarding decision
automation or augmentation. For example, a vignette study may ask for
participant reactions to “AI” but if participants do not know what the
term AI means, knowledge of AI, novelty effects, technological anxiety,
and a variety of other constructs are potentially confounded. Moving
forward, researchers should prioritize research designs that allow more
generalizable conclusions, especially because specific algorithm design
and implementation details in real-world decision-making may have
large effects on relevant outcomes for both second and third parties
(Galière, 2020).
This reframing potentially influences interpretations of the reviewed
research in two major ways. First, imagining how a second party might
feel when a decision is made about them by a first party and/or system
may more directly reflect third-party reactions than second-party re­
actions. A consequence of this might be that most vignette-based studies
show a preference for human over automated medical decisions,
whereas Keel et al.’s (2018) study of authentic second-party reactions
found the opposite. Second, systems are generally developed iteratively,
refined over time through hundreds or thousands of versions to maxi­
mize positive outcomes and minimize negative outcomes over a long
time period for narrowly defined subpopulations (Landers & Marin,
2021). Thus, development research conducted by technology companies
and held privately often refines real-world systems for targeted outcome
in ways that vignette studies of such systems cannot replicate. In short,
researchers may often be studying automated or augmented
decision-making as researchers imagine it, not as it is realized in
authentic organizational contexts. In these ways, a literature relying
entirely upon vignettes risks being ungeneralizable to real-world
decision-making.
The most informative designs in the literature that we identified
were studies investigating algorithmic management in gig or platform
work and studies directly investigating the implementation of auto­
mated systems for decision (Howard et al., 2020; Keel et al., 2018;
Ravenelle, 2019). Yet, such insights predominantly stem from qualita­
tive interviews with second parties or from the analysis of online forums
where workers exchange their experiences. Future studies might try to
use experiments and quantitative analyses to broaden the insights. For
instance, algorithmic management could affect employees in organiza­
tions who have more interaction with their colleagues and supervisors
compared to Uber drivers, who almost always work alone (Wesche &
Sonderegger, 2019). Additionally, if people know that automated sys­
tems will evaluate them in application processes or in performance
evaluations within organizations, this might lead to similar reactions
like the ones found in studies in our review (e.g., reverse engineer
algorithmic evaluation processes). Since the same automated system
could be used in different organizations, it would be interesting to
investigate whether this could lead to collective action or attempts to
share knowledge about the involved systems across organizations. For
instance, similar behavior is already common in automated systems for
personnel selection where there are online discussions where people
share knowledge and folk theories about to positively affect evaluation
by automated interview systems.3

automated systems at work (e.g., expert systems) might reoccur for
current AI-based systems (Gill, 1995). In fact, despite expert systems
sparking significant attention in the 1980s and 1990s, they have not
been widely adopted in workplaces. Instead, problems transitioning
from development to implementation, and more problematically the
lack of system acceptance by users, hindered the use of this earlier
manifestation of workplace AI (Gill, 1995). Although current AI-based
automated systems may have significant advantages over expert sys­
tems in terms of flexibility and accuracy, it is unclear if the fundamental
psychological processes affected by the use of these systems and the
design concerns faced in their development to address such processes
are substantially different. Additionally, litigation against automated
decision systems has become a concern that will likely affect attitudes
towards such systems (Harwell, 2019), national ethical and legal
guidelines are evolving, and there have been several high profile ex­
amples of public outrage about the use of automated decisions for
work-related decisions (Lecher, 2019). Furthermore, the new generation
of AI-based automated systems comes with new technical challenges,
such as the detection and response to biased decision-making (Raghavan
et al., 2020), the opacity of decision-processes (Burrell, 2016), and
increased demand for explainability (Floridi et al., 2018).
To understand the effects of automated and augmented decisionmaking in this context, it is necessary to take a multi-stakeholder
view, considering their perspectives both holistically and individually
when making research design decisions (Jungmann et al., 2020; Langer
et al., 2021). As it stands currently, there is a notable stream of research
assessing first-party acceptance (at least in certain areas of application;
Burton et al., 2020; Hoff & Bashir, 2015), and our review summarizes
research on second and third parties. In addition to the use of authentic
decision-making to enhance our understanding of those parties, a more
complete treatment of stakeholders would include supervisors of people
using automated decisions (e.g., how to best assess the work of direct
reports when those use automated systems; Holstein et al., 2019), team
members (e.g., how does the implementation of an automated decision
agent into a team affect team collaboration; O’Neill et al. 2020), de­
velopers (e.g., how developers should be involved in redesign to
improve automated systems once they are implemented; Landers &
Marin, 2021), and regulatory bodies (e.g., how policy maker actions
influence these networks of relationships; Arrieta et al., 2020).
5.3. Inconsistency in terminology
Substantial variation in terminology (see Table 1) between and even
within studies sometimes harms the coherence of conclusions. The
reviewed studies used terms including AI/ML (Gonzalez et al., 2019),
automated system (Dineen et al., 2004), super computer (Bigman &
Gray, 2018), and algorithm (Newman et al., 2020) to refer to similar
concepts. Without explicitly defining terms, construct proliferation (J.
A. Shaffer et al., 2016) becomes a substantial and troubling risk, risking
unnecessary splits in the literature and wasted researcher resources.
This problem especially applies to study designs themselves, when
considering the specific prompts provided to participants in vignette
studies. Studies varied greatly in terms of the amount and clarity of
explanatory information concerning the system studied. For instance, M.
K. Lee (2018) used the term “algorithm” with participants without
providing any additional information, whereas Newman et al.’s (2020)
participants read “algorithm (i.e., a computerized decision-making
tool)”. Similarly, if participants are more familiar with the word “com­
puter program,” this might result in different reactions compared to
when describing the same system as an “algorithm” due to their personal
familiarity rather than the general idea of automated or augmented
decision-making. Supporting this, Gray and Wegner (2012) show that
uneasy feelings about systems result from ascribing the ability to sense
and feel (i.e., experience) to machines but not from perceived agency of
systems. Ascribing sensing and feeling abilities might be more likely for
some terms (e.g., “robot”) compared to others (e.g., “computer

5.2. Multi-stakeholder view
The stakes associated with accurately investigating real-world pro­
cesses are high. Consider that many problems associated with earlier
3
https://www.reddit.com/r/recruitinghell/comments/e5eyw5/duke_univer
sity_is_preparing_students_for/.

16

Computers in Human Behavior 123 (2021) 106878

M. Langer and R.N. Landers

program”). As such, we believe that investigating the consequences of
terminological differences when referring to a system that enables de­
cision automation or augmentation is important for future research, as
effects across studies may vary due to such differences.

third parties can be exceptionally influential on organizations consid­
ering the implementation of systems enabling the automation or
augmentation of decisions; understanding second- and third-party re­
sponses has never been more critical as society continues its march to­
wards automation and augmentation.
At the beginning of this review, we proposed three research ques­
tions: (1) how do automated and augmented decisions affect second and
third parties? (2) what moderates these effects? and (3) what are the
next crucial steps to meaningfully advance this research area? With
respect to (1) we can conclude that there are manifold influences of
decision automation and augmentation related to second and third
parties regarding topics such as trust, fairness, responsibility, control­
lability, and autonomy. With regard to (2), we found that those in­
fluences appear to be qualified in numerous underexplored ways,
especially by the characteristics of the decision process (i.e., different
effects for automation compared to augmentation contexts), the system,
the second and third parties, the focal task, and outputs/outcome
characteristics. Regarding (3), our review revealed that most of our
current understanding of second- and third-party effects is driven by
vignette studies, by studies of independent contractors reporting their
experiences with algorithmic management systems, and by generalizing
from the field of medical decision-making. The literature neglects the
manifold system design choices that enable decision automation and
augmentation, making the generalizability of this literature to broader
work contexts with more complex decision-making systems unclear.
Thus, it is critical for future research to tackle these issues of general­
izability directly, by more carefully considering their choice of termi­
nology, research design, and methodology, as well as by integrating
interdisciplinary literature. Dramatic and substantial augmentation and
automation of work by “the system” is coming quickly, and researchers
must be better prepared.

5.4. Considering design-features of systems and levels of automation
A large range of papers that refer to “the system” that augments or
automates decisions consider “the system” to be a monolithic concept.
This ignores the large range of design possibilities for such systems that
might influence effects for second and third parties (Landers & Marin,
2021). For instance, automated systems vary in their development
process (e.g., what kind of training data are provided for the automated
system), in their interface design (e.g., feedback affordances), or in their
performance (e.g., predictive accuracy). The studies already available in
this domain suggest that system design and system characteristics affect
second- and third-party perceptions of automated and augmented de­
cisions (Griesbach et al. 2019; Hong et al., 2020; Longoni et al., 2019;
Ravenelle, 2019), and as such, studying this issue haphazardly is no
longer informative to theory.
Furthermore, decision processes vary in the human and system
control and contribution to the decision, and the difference between
fully-automated and augmented decisions seems to strongly affect sec­
ond and third parties. However, only a subset of the various possible
configurations for decision augmentation (Kaber & Endsley, 2004) have
received attention, and even less so in the area of work-related decisions.
On the one hand, it could be possible that the exact configuration of how
humans and systems interact might not matter for second and third
parties who may have little insight into the specific decision-making
process. On the other hand, this might indicate a neglect of many of
the possible configurations between the extremes human control and
full automation. Indeed, the few papers that allow a conclusion about
whether the extent of human control matters indicate that there are
psychological consequences that seem to be associated with either the
extent of human control or whether human decision-makers have the
final say over decisions (Newman et al., 2020). Future research should
thus explicitly investigate the implications of different levels of human
control on second and third parties and thus contrast their potential
psychological consequences.

Credit author statement
Markus Langer: Conceptualization, Methodology, Conducting the
Review, Interpretation, Writing – original draft preparation, Writing –
Reviewing and Editing, Richard N. Landers: Conceptualization, Inter­
pretation, Writing - Reviewing and editing.
Acknowledgements

5.5. Theoretical integration

Work on this paper was funded by the Volkswagen Foundation grant
AZ 98513.

The reviewed research either refrained from referring to a broader
theoretical frame or mainly focused on justice or signalling theory
(Bangerter et al., 2012; Colquitt et al., 2001) to derive hypotheses and to
embed into the research landscape. Work characteristics and work
design research (Parker & Grote, 2020) might provide another valuable
theoretical lens for the implementation of decision automation and
augmentation into work contexts (Langer, König, & Busch, 2020) but is
currently underutilized. Because those theories focus on work processes
and not necessarily on system design or decision-process-based conse­
quences that affect psychological processes, future researchers should
focus upon the creation of interdisciplinary theory. This involves
combining the technical and system design insights of computer science
and human-computer interaction with the human processes insights of
psychology and the applied theory insights of management to enable
more generalizable work for understanding decision automation and
augmentation (Landers & Marin, 2021).

References
Acikgoz, Y., Davison, K. H., Compagnone, M., & Laske, M. (2020). Justice perceptions of
artificial intelligence in selection. International Journal of Selection and Assessment, 28
(4), 399–416. https://doi.org/10.1111/ijsa.12306
Ananny, M., & Crawford, K. (2018). Seeing without knowing: Limitations of the
transparency ideal and its application to algorithmic accountability. New Media &
Society, 20(3), 973–989. https://doi.org/10.1177/1461444816676645
Anwar, I. A., Pal, J., & Hui, J. (2021). Watched, but moving: Platformization of beauty
work and its gendered mechanisms of control. Proceedings of the ACM on HumanComputer Interaction, 4, 1–20. https://doi.org/10.1145/3432949
Araujo, T., Helberger, N., Krulkmeier, S., de Vreese, C. H., et al. (2020). In AI we trust?
Perceptions about automated decision‑making by artificial intelligence. AI & Society,
35(3), 611–623. https://doi.org/10.1007/s00146-019-00931-w
Arkes, H. R., Shaffer, V. A., & Medow, M. A. (2007). Patients derogate physicians who
use a computer-assisted diagnostic aid. Medical Decision Making, 27(2), 189–202.
https://doi.org/10.1177/0272989X06297391
Arrieta, A. B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., Barbado, A.,
Garcia, S., Gil-Lopez, S., Molina, D., Benjamins, R., Chatila, R., & Herrera, F. (2020).
Explainable artificial intelligence (XAI): Concepts, taxonomies, opportunities and
challenges toward responsible AI. Information Fusion, 58, 82–115. https://doi.org/
10.1016/j.inffus.2019.12.012
Atzmüller, C., & Steiner, P. M. (2010). Experimental vignette studies in survey research.
Methodology, 6(3), 128–138. https://doi.org/10.1027/1614-2241/a000014
Bangerter, A., Roulin, N., & König, C. J. (2012). Personnel selection as a signaling game.
Journal of Applied Psychology, 97(4), 719–738. https://doi.org/10.1037/a0026078

6. Conclusion
Research in the area of automated and augmented decision-making
has focused principally upon first parties (Burton et al., 2020; Grove &
Meehl, 1996; Hoff & Bashir, 2015). This review extends this research by
investigating the effects of decision automation and augmentation on
second and third parties. In our highly connected society, second and
17

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Benbasat, I., & Nault, B. R. (1990). An evaluation of empirical research in managerial
support systems. Decision Support Systems, 6(3), 203–226. https://doi.org/10.1016/
0167-9236(90)90015-J
Bigman, Y. E., & Gray, K. (2018). People are averse to machines making moral decisions.
Cognition, 181, 21–34. https://doi.org/10.1016/j.cognition.2018.08.003
Bigman, Y. E., Gray, K., Waytz, A., Arnestad, M., & Wilson, D. (2020). Algorithmic
discrimination causes less moral outrage than human discrimination [Preprint]. https://
doi.org/10.31234/osf.io/m3nrp. PsyArXiv.
Binns, R., van Kleek, M., Veale, M., Lyngs, U., Zhao, J., & Shadbolt, N. (2018). “It”s
reducing a human being to a percentage’; Perceptions of justice in algorithmic
decisions. Proceedings of the CHI 2018 Conference on Human Factors in Computing
Systems. https://doi.org/10.31235/osf.io/9wqxr
Bucher, E. L., Schou, P. K., & Waldkirch, M. (2021). Pacifying the algorithm –
Anticipatory compliance in the face of algorithmic management in the gig economy.
Organization, 1, 44–67. https://doi.org/10.1177/1350508420961531
Burrell, J. (2016). How the machine “thinks”: Understanding opacity in machine
learning algorithms. Big Data & Society, 3(1), Article 205395171562251. https://doi.
org/10.1177/2053951715622512
Burton, J. W., Stein, M., & Jensen, T. B. (2020). A systematic review of algorithm
aversion in augmented decision making. Journal of Behavioral Decision Making, 33(2),
220–239. https://doi.org/10.1002/bdm.2155
Castelo, N., Bos, M. W., & Lehmann, D. R. (2019). Task-dependent algorithm aversion.
Journal of Marketing Research, 56(5), 809–825. https://doi.org/10.1177/
0022243719851788
Colquitt, J. A. (2001). On the dimensionality of organizational justice: A construct
validation of a measure. Journal of Applied Psychology, 86(3), 386–400. https://doi.
org/10.1037/0021-9010.86.3.386
Colquitt, J. A., Conlon, D. E., Wesson, M. J., Porter, C. O. L. H., & Ng, K. Y. (2001). Justice
at the millennium: A meta-analytic review of 25 years of organizational justice
research. Journal of Applied Psychology, 86(3), 425–445. https://doi.org/10.1037//
0021-9010.86.3.425
Colquitt, J. A., & Rodell, J. B. (2011). Justice, trust, and trustworthiness: A longitudinal
analysis integrating three theoretical perspectives. Academy of Management Journal,
54(6), 1183–1206. https://doi.org/10.5465/amj.2007.0572
Dawes, R. M., Faust, D., & Meehl, P. E. (1989). Clinical versus actuarial judgment.
Science, 243(4899), 1668–1674. https://doi.org/10.1126/science.2648573
Dietvorst, B. J., & Bharti, S. (2020). People reject algorithms in uncertain decision
domains because they have diminishing sensitivity to forecasting error. Psychological
Science, 31(10), 1302–1314. https://doi.org/10.1177/0956797620948841
Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm aversion: People
erroneously avoid algorithms after seeing them err. Journal of Experimental
Psychology: General, 144(1), 114–126. https://doi.org/10.1037/xge0000033
Dineen, B. R., Noe, R. A., & Wang, C. (2004). Perceived fairness of web-based applicant
screening procedures: Weighing the rules of justice and the role of individual
differences. Human Resource Management, 43(2–3), 127–145. https://doi.org/
10.1002/hrm.20011
van Dongen, K., & van Maanen, P.-P. (2013). A framework for explaining reliance on
decision aids. International Journal of Human-Computer Studies, 71(4), 410–424.
https://doi.org/10.1016/j.ijhcs.2012.10.018
Duggan, J., Sherman, U., Carbery, R., & McDonnell, A. (2020). Algorithmic management
and app-work in the gig economy: A research agenda for employment relations and
HRM. Human Resource Management Journal, 30(1), 114–132. https://doi.org/
10.1111/1748-8583.12258
Fazio, R. H., & Williams, C. J. (1986). Attitude accessibility as a moderator of the
attitude–perception and attitude–behavior relations: An investigation of the 1984
presidential election. Journal of Personality and Social Psychology, 51(3), 505–514.
https://doi.org/10.1037/0022-3514.51.3.505
Floridi, L., Cowls, J., Beltrametti, M., Chatila, R., Chazerand, P., Dignum, V., Luetge, C.,
Madelin, R., Pagallo, U., Rossi, F., Schafer, B., Valcke, P., & Vayena, E. (2018).
AI4People—an ethical framework for a good AI society: Opportunities, risks,
principles, and recommendations. Minds and Machines, 28(4), 689–707. https://doi.
org/10.1007/s11023-018-9482-5
Galière, S. (2020). When food-delivery platform workers consent to algorithmic
management: A Foucauldian perspective. New Technology, Work and Employment, 35
(3), 357–370. https://doi.org/10.1111/ntwe.12177
Gill, T. G. (1995). Early expert systems: Where are they now? MIS Quarterly, 19(1), 51.
https://doi.org/10.2307/249711
Gonzalez, M. F., Capman, J. F., Oswald, F. L., Theys, E. R., & Tomczak, D. L. (2019).
“Where’s the I-O?” Artificial intelligence and machine learning in talent
management systems. Personnel Assessment and Decisions, 3, 5. https://doi.org/
10.25035/pad.2019.03.005
Gray, K., & Wegner, D. M. (2012). Feeling robots and human zombies: Mind perception
and the uncanny valley. Cognition, 125(1), 125–130. https://doi.org/10.1016/j.
cognition.2012.06.007
Grgić-Hlača, N., Redmiles, E. M., Gummadi, K. P., & Weller, A. (2018). Human
perceptions of fairness in algorithmic decision making: A case study of criminal risk
prediction. In Proceedings of the 2018 world wide web conference on world wide web
(pp. 903–912). https://doi.org/10.1145/3178876.3186138
Griesbach, K., Reich, A., Elliott-Negri, L., & Milkman, R. (2019). Algorithmic control in
platform food delivery work. Socius: Sociological Research for a Dynamic World, 5,
Article 237802311987004. https://doi.org/10.1177/2378023119870041
Grove, W. M., & Meehl, P. E. (1996). Comparative efficiency of informal (subjective,
impressionistic) and formal (mechanical, algorithmic) prediction procedures: The
clinical–statistical controversy. Psychology, Public Policy, and Law, 2(2), 293–323.
https://doi.org/10.1037/1076-8971.2.2.293

Grove, W. M., Zald, D. H., Lebow, B. S., Snitz, B. E., & Nelson, C. (2000). Clinical versus
mechanical prediction: A meta-analysis. Psychological Assessment, 12(1), 19–30.
https://doi.org/10.1037//1040-3590.12.1.19
Haan, M., Ongena, Y. P., Hommes, S., Kwee, T. C., & Yakar, D. (2019). A qualitative
study to understand patient perspective on the use of artificial intelligence in
radiology. Journal of the American College of Radiology, 16(10), 1416–1419. https://
doi.org/10.1016/j.jacr.2018.12.043
Hamilton, J. G., Genoff Garzon, M., Westerman, J. S., Shuk, E., Hay, J. L., Walters, C., …
Kris, M. G. (2019). “A tool, not a crutch”: Patient perspectives about IBM Watson for
oncology trained by memorial sloan kettering. Journal of Oncology Practice, 15(4),
e277–e288. https://doi.org/10.1200/JOP.18.00417
Harwell, D. (2019). Rights group files federal complaint against AI-hiring firm HireVue, citing
‘unfair and deceptive’ practices. The Washington Post. https://www.washingtonpost.
com/technology/2019/11/06/prominent-rights-group-files-federal-complaint-aga
inst-ai-hiring-firm-hirevue-citing-unfair-deceptive-practices/.
Healy, J., Pekarek, A., & Vromen, A. (2020). Sceptics or supporters? Consumers’ views of
work in the gig economy. New Technology, Work and Employment, 35(1), 1–19.
https://doi.org/10.1111/ntwe.12157
Highhouse, S. (2008). Stubborn reliance on intuition and subjectivity in employee
selection. Industrial and Organizational Psychology, 1(3), 333–342. https://doi.org/
10.1111/j.1754-9434.2008.00058.x
Höddinghaus, M., Sondern, D., & Hertel, G. (2020). The automation of leadership
functions: Would people trust decision algorithms? Computers in Human Behavior,
116, 106635. https://doi.org/10.1016/j.chb.2020.106635
Hoff, K. A., & Bashir, M. (2015). Trust in automation: Integrating empirical evidence on
factors that influence trust. Human Factors, 57(3), 407–434. https://doi.org/
10.1177/0018720814547570
Holstein, K., Wortman Vaughan, J., Daumé, H., Dudik, M., & Wallach, H. (2019).
Improving fairness in machine learning systems: What do industry practitioners
need? Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems,
1–16. https://doi.org/10.1145/3290605.3300830
Hong, J.-W., Choi, S., & Williams, D. (2020). Sexist AI: An experiment integrating CASA
and ELM. International Journal of Human-Computer Interaction, 36(20), 1928–1941.
https://doi.org/10.1080/10447318.2020.1801226
Howard, F. M., Gao, C. A., & Sankey, C. (2020). Implementation of an automated
scheduling tool improves schedule quality and resident satisfaction. PloS One, 15(8),
Article e0236952. https://doi.org/10.1371/journal.pone.0236952
Jarrahi, M. H., & Sutherland, W. (2019). Algorithmic management and algorithmic
competencies: Understanding and appropriating algorithms in gig work. In
N. G. Taylor, C. Christian-Lamb, M. H. Martin, & B. Nardi (Eds.), Information in
contemporary society, lecture notes in computer science (11420th ed., pp. 578–589).
Springer. https://doi.org/10.1007/978-3-030-15742-5_55.
Jarrahi, M. H., Sutherland, W., Nelson, S. B., & Sawyer, S. (2020). Platformic
management, boundary resources for gig work, and worker autonomy. Computer
Supported Cooperative Work, 29(1–2), 153–189. https://doi.org/10.1007/s10606019-09368-7
Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines.
Nature Machine Intelligence, 1(9), 389–399. https://doi.org/10.1038/s42256-0190088-2
Jonmarker, O., Strand, F., Brandberg, Y., & Lindholm, P. (2019). The future of breast
cancer screening: What do participants in a breast cancer screening program think
about automation using artificial intelligence? Acta Radiologica Open, 8(12). https://
doi.org/10.1177/2058460119880315, 205846011988031.
Jungmann, F., Jorg, T., Hahn, F., Pinto dos Santos, D., Jungmann, S. M., Düber, C.,
Mildenberger, P., & Kloeckner, R. (2020). Attitudes toward artificial intelligence among
radiologists, IT specialists, and industry. Academic Radiology. https://doi.org/
10.1016/j.acra.2020.04.011. S1076633220302038.
Jutzi, T. B., Krieghoff-Henning, E. I., Holland-Letz, T., Utikal, J. S., Hauschild, A.,
Schadendorf, D., Sondermann, W., Fröhling, S., Hekler, A., Schmitt, M., Maron, R. C.,
& Brinker, T. J. (2020). Artificial intelligence in skin cancer diagnostics: The
patients’ perspective. Frontiers of Medicine, 7. https://doi.org/10.3389/
fmed.2020.00233
Kaber, D. B., & Endsley, M. R. (2004). The effects of level of automation and adaptive
automation on human performance, situation awareness and workload in a dynamic
control task. Theoretical Issues in Ergonomics Science, 5(2), 113–153. https://doi.org/
10.1080/1463922021000054335
Keel, S., Lee, P. Y., Scheetz, J., Li, Z., Kotowicz, M. A., MacIsaac, R. J., & He, M. (2018).
Feasibility and patient acceptability of a novel artificial intelligence-based screening
model for diabetic retinopathy at endocrinology outpatient services: A pilot study.
Scientific Reports, 8(1). https://doi.org/10.1038/s41598-018-22612-2
Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new
contested terrain of control. The Academy of Management Annals, 14(1), 366–410.
https://doi.org/10.5465/annals.2018.0174
Kinder, E., Jarrahi, M. H., & Sutherland, W. (2019). Gig platforms, tensions, alliances and
ecosystems: An actor-network perspective. Proceedings of the ACM on HumanComputer Interaction, 3, 1–26. https://doi.org/10.1145/3359314
Kuncel, N. R., Klieger, D. M., Connelly, B. S., & Ones, D. S. (2013). Mechanical versus
clinical data combination in selection and admissions decisions: A meta-analysis.
Journal of Applied Psychology, 98(6), 1060–1072. https://doi.org/10.1037/a0034156
Landers, R. N., & Marin, S. (2021). Theory and technology in organizational psychology:
A review of technology integration paradigms and their effects on the validity of
theory. Annual Review of Organizational Psychology and Organizational Behavior, 8(1),
235–258. https://doi.org/10.1146/annurev-orgpsych-012420-060843
Langer, M., König, C. J., & Busch, V. (2020). Changing the means of managerial work:
Effects of automated decision-support systems on personnel selection tasks. In

18

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Journal of business and psychology. Advance Online Publication. https://doi.org/
10.1007/s10869-020-09711-6.
Langer, M., König, C. J., & Fitili, A. (2018). Information as a double-edged sword: The
role of computer experience and information on applicant reactions towards novel
technologies for personnel selection. Computers in Human Behavior, 81, 19–30.
https://doi.org/10.1016/j.chb.2017.11.036
Langer, M., König, C. J., & Hemsing, V. (2020). Is anybody listening? The impact of
automatically evaluated job interviews on impression management and applicant
reactions. Journal of Managerial Psychology, 35(4), 271–284. https://doi.org/
10.1108/JMP-03-2019-0156
Langer, M., König, C. J., & Papathanasiou, M. (2019). Highly-automated job interviews:
Acceptance under the influence of stakes. International Journal of Selection and
Assessment, 27(3), 217–234. https://doi.org/10.1111/ijsa.12246
Langer, M., König, C. J., Sanchez, D. R.-P., & Samadi, S. (2019). Highly automated
interviews: Applicant reactions and the organizational context. Journal of Managerial
Psychology, 35(4), 301–314. https://doi.org/10.1108/JMP-09-2018-0402
Langer, M., Oster, D., Speith, T., Hermanns, H., Kästner, L., Schmidt, E., Sesing, A., &
Baum, K. (2021). What do we want from explainable artificial intelligence (XAI)? A
stakeholder perspective on XAI and a conceptual model guiding interdisciplinary
XAI research. Artificial Intelligence, 296, 103473. https://doi.org/10.1016/j.
artint.2021.103473
Lecher, C. (2019). How Amazon automatically tracks and fires warehouse workers for
‘productivity. The Verge. https://www.theverge.com/2019/4/25/18516004/amazo
n-warehouse-fulfillment-centers-productivity-firing-terminations.
Lee, M. K. (2018). Understanding perception of algorithmic decisions: Fairness, trust, and
emotion in response to algorithmic management. Big Data & Society, 5(1). https://
doi.org/10.1177/2053951718756684, 205395171875668.
Lee, J. D., & See, K. A. (2004). Trust in automation: Designing for appropriate reliance.
Human Factors, 46(1), 50–80. https://doi.org/10.1518/hfes.46.1.50.30392
Lee, M. K., Kusbit, D., Metsky, E., & Dabbish, L. (2015). Working with machines: The
impact of algorithmic and data-driven management on human workers. Proceedings
of the 2015 CHI Conference on Human Factors in Computing Systems. https://doi.org/
10.1145/2702123.2702548
Lombrozo, T. (2011). The instrumental value of explanations. Philosophy Compass, 6(8),
539–551. https://doi.org/10.1111/j.1747-9991.2011.00413.x
Longoni, C., Bonezzi, A., & Morewedge, C. K. (2019). Resistance to medical artificial
intelligence. Journal of Consumer Research, 46(4), 629–650. https://doi.org/
10.1093/jcr/ucz013
Lowe, D. J., Reckers, P. M. J., & Whitecotton, S. M. (2002). The effects of decision-aid use
and reliability on jurors’ evaluations of auditor liability. The Accounting Review, 77
(1), 185–202. https://doi.org/10.2308/accr.2002.77.1.185
Makarius, E. E., Mukherjee, D., Fox, J. D., & Fox, A. K. (2020). Rising with the machines:
A sociotechnical framework for bringing artificial intelligence into the organization.
Journal of Business Research, 120, 262–273. https://doi.org/10.1016/j.
jbusres.2020.07.045
Marcinkowski, F., Kieslich, K., Starke, C., & Lünich, M. (2020). Implications of AI (un-)
fairness in higher education admissions: The effects of perceived AI (un-)fairness on
exit, voice and organizational reputation. Proceedings of the 2020 FAT* conference on
fairness, accountability and transparency. https://doi.org/10.1145/3351095.3372867
Mayer, R. C., Davis, J. H., & Schoorman, F. D. (1995). An integrative model of
organizational trust. Academy of Management Review, 20(2), 709–726. https://doi.
org/10.2307/258792
Meehl, P. E. (1954). Clinical versus statistical prediction: A theoretical analysis and a review
of the evidence. University of Minnesota Press.
Merritt, S. M., Unnerstall, J. L., Lee, D., & Huber, K. (2015). Measuring individual
differences in the perfect automation schema. Human Factors, 57(5), 740–753.
https://doi.org/10.1177/0018720815581247
Miller, T. (2019). Explanation in artificial intelligence: Insights from the social sciences.
Artificial Intelligence, 267, 1–38. https://doi.org/10.1016/j.artint.2018.07.007
Mirowska, A. (2020). AI evaluation in selection: Effects on application and pursuit
intentions. Journal of Personnel Psychology, 19(3), 142–149. https://doi.org/
10.1027/1866-5888/a000258
Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L. (2016). The ethics of
algorithms: Mapping the debate. Big Data & Society, 3(2), Article 205395171667967.
https://doi.org/10.1177/2053951716679679
Möhlmann, M., & Zalmanson, L. (2017). Hands on the Wheel: Navigating algorithmic
management and Uber drivers’ autonomy. In Proceedings of the 2017 international
conference on information system. https://aisel.aisnet.org/icis2017/DigitalPlatforms/
Presentations/3.
Möhlmann, M., Zalmanson, L., & Gregory, R. W. (in press). Algorithmic management of
work on online labor platforms: When matching meets control. MIS Quarterly.
Advance Online Publication.
Murray, A., Rhymer, J., & Sirmon, D. G. (2020). Humans and technology: Forms of
conjoined agency in organizations. Academy of Management Review. Advance Online
Publication. https://doi.org/10.5465/amr.2019.0186
Myhill, K., Richards, J., & Sang, K. (2021). Job quality, fair work and gig work: The lived
experience of gig workers. In International journal of human resource management.
Advance Online Publication. https://doi.org/10.1080/09585192.2020.1867612.
Nagtegaal, R. (2021). The impact of using algorithms for managerial decisions on public
employees’ procedural justice. Government Information Quarterly, 38(1), 101536.
https://doi.org/10.1016/j.giq.2020.101536
Nelson, C. A., Pérez-Chada, L. M., Creadore, A., Li, S. J., Lo, K., Manjaly, P.,
Pournamdari, A. B., Tkachenko, E., Barbieri, J. S., Ko, J. M., Menon, A. V.,
Hartman, R. I., & Mostaghimi, A. (2020). Patient perspectives on the use of artificial
intelligence for skin cancer screening: A qualitative study. JAMA Dermatology, 156
(5), 501. https://doi.org/10.1001/jamadermatol.2019.5014

Newman, D. T., Fast, N. J., & Harmon, D. J. (2020). When eliminating bias isn’t fair:
Algorithmic reductionism and procedural justice in human resource decisions.
Organizational Behavior and Human Decision Processes, 160, 149–167. https://doi.
org/10.1016/j.obhdp.2020.03.008
Nolan, K., Carter, N., & Dalal, D. (2016). Threat of technological unemployment: Are
hiring managers discounted for using standardized employee selection practices?
Personnel Assessment and Decisions, 2(1), 4. https://doi.org/10.25035/pad.2016.004
O’Neill, T., McNeese, N., Barron, A., & Schelble, B. (2020). Human–autonomy teaming: A
review and analysis of the empirical literature. Human Factors. Advance Online
Publication.. https://doi.org/10.1177/0018720820960865, 001872082096086.
Onnasch, L., Wickens, C. D., Li, H., & Manzey, D. (2014). Human performance
consequences of stages and levels of automation: An integrated meta-analysis.
Human Factors, 56(3), 476–488. https://doi.org/10.1177/0018720813501549
Ötting, S. K., & Maier, G. W. (2018). The importance of procedural justice in humanmachine-interactions: Intelligent systems as new decision agents in organizations.
Computers in Human Behavior, 89, 27–39. https://doi.org/10.1016/j.
chb.2018.07.022
Palmeira, M., & Spassova, G. (2015). Consumer reactions to professionals who use
decision aids. European Journal of Marketing, 49(3/4), 302–326. https://doi.org/
10.1108/EJM-07-2013-0390
Palmisciano, P., Jamjoom, A. A. B., Taylor, D., Stoyanov, D., & Marcus, H. J. (2020).
Attitudes of patients and their relatives toward Artificial Intelligence in
neurosurgery. World Neurosurgery, 138, e627–e633. https://doi.org/10.1016/j.
wneu.2020.03.029
Parasuraman, R., & Riley, V. (1997). Humans and automation: Use, misuse, disuse,
abuse. Human Factors, 39(2), 230–253. https://doi.org/10.1518/
001872097778543886
Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). A model for types and levels
of human interaction with automation. IEEE Transactions on Systems, Man, and
Cybernetics - Part A: Systems and Humans, 30(3), 286–297. https://doi.org/10.1109/
3468.844354
Parker, S., & Grote, G. (2020). Automation, algorithms, and beyond: Why work design
matters more than ever in a digital world. Applied Psychology. Advance Online
Publication.. https://doi.org/10.1111/apps.12241
Pezzo, M. V., & Pezzo, S. P. (2006). Physician evaluation after medical errors: Does
having a computer decision aid help or hurt in hindsight? Medical Decision Making,
26(1), 48–56. https://doi.org/10.1177/0272989X05282644
Promberger, M., & Baron, J. (2006). Do patients trust computers? Journal of Behavioral
Decision Making, 19(5), 455–468. https://doi.org/10.1002/bdm.542
Raghavan, M., Barocas, S., Kleinberg, J., & Levy, K. (2020). Mitigating bias in
algorithmic hiring: Evaluating claims and practices. Proceedings of the 2020 FAT*
conference on fairness, accountability and transparency. https://doi.org/10.1145/
3351095.3372828
Raisch, S., & Krakowski, S. (2021). Artificial intelligence and management: The
automation-augmentation paradox. Academy of Management Review, 46(1), 192–210.
https://doi.org/10.5465/amr.2018.0072
Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., … Barnes, P.
(2020). Closing the AI accountability gap: Defining an end-to-end framework for
internal algorithmic auditing. Proceedings of the 2020 FAT* conference on fairness,
accountability and transparency. https://doi.org/10.1145/3351095.3372873
Ravenelle, A. J. (2019). “We’re not uber:” control, autonomy, and entrepreneurship in
the gig economy. Journal of Managerial Psychology, 34(4), 269–285. https://doi.org/
10.1108/JMP-06-2018-0256
Schlicker, N., Langer, M., Ötting, S. K., König, C. J., Baum, K., & Wallach, D. (2021).
What to expect from opening “black boxes”? Comparing perceptions of justice
between human and automated agents. Computers in Human Behavior, 122, Article
106837. https://doi.org/10.1016/j.chb.2021.106837
Schmoll, R., & Bader, V. (2019). Who or what screens which one of me? The differential
effects of algorithmic social media screening on applicants’ job pursuit intention.
Proceedings of the ICIS 2019.
Shaffer, J. A., DeGeest, D., & Li, A. (2016). Tackling the problem of construct
proliferation: A guide to assessing the discriminant validity of conceptually related
constructs. Organizational Research Methods, 19(1), 80–110. https://doi.org/
10.1177/1094428115598239
Shaffer, V. A., Probst, C. A., Merkle, E. C., Arkes, H. R., & Medow, M. A. (2013). Why do
patients derogate physicians who use a computer-based diagnostic support system?
Medical Decision Making, 33(1), 108–118. https://doi.org/10.1177/
0272989X12453501
Shin, D., & Park, Y. J. (2019). Role of fairness, accountability, and transparency in
algorithmic affordance. Computers in Human Behavior, 98, 277–284. https://doi.org/
10.1016/j.chb.2019.04.019
Srivastava, M., Heidari, H., & Krause, A. (2019). Mathematical notions vs. human
perception of fairness: A descriptive approach to fairness for machine learning.
Proceedings of the 2019 ACM SIGKDD International Conference on Knowledge Discovery
& Data Mining, 2459–2468. https://doi.org/10.1145/3292500.3330664
Stai, B., Heller, N., McSweeney, S., Rickman, J., Blake, P., Vasdev, R., Edgerton, Z.,
Tejpaul, R., Peterson, M., Rosenberg, J., Kalapara, A., Regmi, S.,
Papanikolopoulos, N., & Weight, C. (2020). Public perceptions of artificial
intelligence and robotics in medicine. Journal of Endourology, 34(10), 1041–1048.
https://doi.org/10.1089/end.2020.0137
Suen, H.-Y., Chen, M. Y.-C., & Lu, S.-H. (2019). Does the use of synchrony and artificial
intelligence in video interviews affect interview ratings and applicant attitudes?
Computers in Human Behavior, 98, 93–101. https://doi.org/10.1016/j.
chb.2019.04.012

19

M. Langer and R.N. Landers

Computers in Human Behavior 123 (2021) 106878

Tassinari, A., & Maccarrone, V. (2020). Riders on the storm: Workplace solidarity among
gig economy couriers in Italy and the UK. Work, Employment & Society, 34(1), 35–54.
https://doi.org/10.1177/0950017019862954
Tobia, K., Nielsen, A., & Stremitzer, A. (2021). When does physician use of AI increase
liability? Journal of Nuclear Medicine, 62(1), 17–21. https://doi.org/10.2967/
jnumed.120.256032
Uhde, A., Schlicker, N., Wallach, D. P., & Hassenzahl, M. (2020). Fairness and decisionmaking in collaborative shift scheduling systems. Proceedings of the 2020 CHI
Conference on Human Factors in Computing Systems, 1–13. https://doi.org/10.1145/
3313831.3376656
van Esch, P., & Black, J. S. (2019). Factors that influence new generation candidates to
engage with and complete digital, AI-enabled recruiting. Business Horizons, 62(6),
729–739. https://doi.org/10.1016/j.bushor.2019.07.004
Veen, A., Barratt, T., & Goods, C. (2020). Platform-capital’s ‘app-etite’ for control: A
labour process analysis of food-delivery work in Australia. Work, Employment &
Society, 34(3), 388–406. https://doi.org/10.1177/0950017019836911
Wang, R., Harper, F. M., & Zhu, H. (2020). Factors influencing perceived fairness in
algorithmic decision-making algorithm outcomes, development procedures, and
individual differences. Proceedings of the 2018 CHI Conference on Human Factors in
Computing Systems, 14. https://doi.org/10.1145/3313831.3376813

Wesche, J. S., & Sonderegger, A. (2019). When computers take the lead: The automation
of leadership. Computers in Human Behavior, 101, 197–209. https://doi.org/
10.1016/j.chb.2019.07.027
Wohlin, C. (2014). Guidelines for snowballing in systematic literature studies and a
replication in software engineering. Proceedings of the 18th International Conference
on Evaluation and Assessment in Software Engineering - EASE, 14, 1–10. https://doi.
org/10.1145/2601248.2601268
Wolf, J. R. (2014). Do IT students prefer doctors who use IT? Computers in Human
Behavior, 35, 287–294. https://doi.org/10.1016/j.chb.2014.03.020
Wood, A. J., Graham, M., Lehdonvirta, V., & Hjorth, I. (2019). Good gig, bad gig:
Autonomy and algorithmic control in the global gig economy. Work, Employment &
Society, 33(1), 56–75. https://doi.org/10.1177/0950017018785616
Yokoi, R., Eguchi, Y., Fujita, T., & Nakayachi, K. (2020). Artificial intelligence is trusted
less than a doctor in medical treatment decisions: Influence of perceived care and
value similarity. International Journal of Human-Computer Interaction, 1–10. https://
doi.org/10.1080/10447318.2020.1861763
York, T., Jenney, H., & Jones, G. (2020). Clinician and computer: A study on patient
perceptions of artificial intelligence in skeletal radiography. BMJ Health & Care
Informatics, 27(3), Article e100233. https://doi.org/10.1136/bmjhci-2020-100233
Zerilli, J., Knott, A., Maclaurin, J., & Gavaghan, C. (2018). Transparency in algorithmic
and human decision-making: Is there a double standard? Philosophy & Technology, 32
(4), 661–683. https://doi.org/10.1007/s13347-018-0330-6

20


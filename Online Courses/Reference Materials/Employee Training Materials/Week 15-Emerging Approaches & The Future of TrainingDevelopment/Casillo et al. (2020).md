2020 IEEE International Conference on Teaching, Assessment, and Learning for Engineering (TALE) | 978-1-7281-6942-2/20/$31.00 ©2020 IEEE | DOI: 10.1109/TALE48869.2020.9368339

Chatbot in Industry 4.0: An Approach for Training
New Employees
Mario Casillo
DIIn
University of Salerno
Fisciano (SA), Italy
mcasillo@unisa.it

Francesco Colace
DIIn
University of Salerno
Fisciano (SA), Italy
fcolace@unisa.it

Loretta Fabbri
DSFUCI
University of Siena
Arezzo (AR), Italy
loretta.fabbri@unisi.it

Marco Lombardi
DIIn
University of Salerno
Fisciano (SA), Italy
malombardi@unisa.it

Alessandra Romano
DSFUCI
University of Siena
Arezzo (AR), Italy
alessandra.romano2@unisi.it

Domenico Santaniello
DIIn
University of Salerno
Fisciano (SA), Italy
dsantaniello@unisa.it

Abstract—With the advent of new technological systems, the
industry is also undergoing considerable change. In what is now
called Industry 4.0, human-machine interaction is the crucial
aspect of improving production activity. Useful tools, which are
sometimes used profitably, are chatbots. Modern chatbots can
be used as virtual assistants to guide workers through different
stages of company production. Such systems can interact with
users directly and can assist workers by acting as simple
reminders to follow them in training activities.
This work aims to propose a framework capable of
developing chatbots for the training of employees in a company.
This tool aims to be a proactive virtual assistant that simplifies
and follows the employee during the learning phase of new tasks,
which sometimes may be complicated. In order to validate the
proposed framework, a prototype was developed, and an
experimental campaign was conducted involving a group of new
employees to be trained, obtaining promising results.
Keywords— chatbot, context-aware computing, e-Learning,
industry 4.0, recommender systems

I. INTRODUCTION
The integration of complex machines and devices with
software and sensors to monitor, control and plan for better
business and societal outcomes [1], is one of the Industry 4.0
definition. This transformation occurred due to the advent of
several paradigms, such as the Internet of Things [2] and Big
Data [3]. These concepts are strongly linked [4] [5] [6] [7],
and can turn a conventional industry into a Smart Industry.
The increasing use of technology has brought the rise of
new strategies and methods to communicate and share
knowledge between humans and machines [8].
Employ training phase plays a crucial role. The company
"know-how" should be effectively shared and used by
employees during their daily practical activities. Making this
information accessible in a simple way, often also on
movement and outside working hours has become an actual
need for many companies, which invest in updating the
professional ability of their human capital. Companies are
searching for learning tools that create an open system of
opportunity in which all employees have access to
information, resources, and capacity to fully contribute to their
professional growth. In particular, e-learning solutions can
satisfy business training needs, creating projects of which it is
possible to evaluate and measure the effects correctly. This
commitment allows building agile, engaging, collaborative
and meaningful educational experiences for the companies

that use them and, at the same time, for the people who use
them directly. In this regard, there is a new set of emerging
technologies
that
introduce
new
human-machine
communication paradigms: the Chatbots.
II.

BACKGROUND

The possibility of developing intelligent agents that are
able to converse in natural language has been the subject of
debate since the birth of artificial intelligence and, to date, is
one of the central themes of Natural Language Processing.
With the term chatbot, we refer, from the nineties until
today, to a software product able to simulate an intelligent
conversation with a human being, mainly through the use of
text or voice. It can constitute a new type of user interface
(UI), called conversational interface, which allows users to
interact with services, organizations, and companies through
a series of questions and answers articulated within a
conversation, which can be referred to with the term "chat".
Therefore, the chatbot concept is often associated with that of
the conversational interface: a type of hybrid user interface
that enables the interaction between man and machine,
combining text and voice with graphic elements typical of UI
(such as buttons, menus and images).
In 1964 Joseph Weizenbaum developed a prototype of
what can be considered the first chatbot, named ELIZA [9]
(from the name of the florist protagonist of the Pygmalion
comedy George Bernard Shaw, Eliza Doolittle), was able to
simulate the conversation with a psychotherapist. ELIZA is
considered by many as one of the first chatbots (and software
in general) able to pass the Turing test: the conversation and
the chatbot's emotional involvement allowed to deceive some
users about the fact that the dialogue took place with a human
being.
In 1995, the scientist Richard S. Wallace created
A.L.I.C.E., Artificial Linguistic Internet Computer Entity, an
"open source" chatbot, programmed with A.I.M.L. (Artificial
Intelligence Markup Language) [10].
In 2006, Watson's turn developed within the IBM DeepQA
project, created to compete against Jeopardy's champions, a
very successful American TV quiz [11]. Moreover, he
succeeded in his intent. It was later used in many other much
more relevant contexts, such as decision management in lung
cancer treatment at the Memorial Sloan-Kettering Cancer
Center.

978-1-7281-6942-2/20/$31.00 ©2020 IEEE
December 8–11, 2020, Online
IEEE TALE2020 – An International Conference on Engineering, Technology and Education
Page
371 20,2024 at 23:44:23 UTC from IEEE Xplore. Restrictions apply.
Authorized licensed use limited to: Radford University. Downloaded
on January

From 2010 onwards, we have seen the proliferation of a
whole series of virtual assistants based on intelligent software
capable of interpreting natural language, the language we all
use when we speak or write: from Siri(2010), Apple's voice
assistant able to provide road or weather information, answer
questions, send messages to Google Now (2012), a technology
capable of understanding what the user wants, interpreting
requests and sometimes anticipating them, to offer a punctual,
precise and complete service that does not force those who use
it to a rigid and limiting syntax from the point of view of
expressiveness [12].
Today, however, new cases of use are emerging in the
most disparate sectors, including Industry 4.0 and e-learning
[13]. In the Industry 4.0 field, FinderBuddyis [14] was
proposed like a chatbot to support the procurement process in
industries. This chatbot…
In education, many resources (time, funds, etc.) are usually
limited. In this scenario, the possibility for a user to have a
personal chatbot available brings many advantages [15] [16]
[17]. To name a few:
-

chatbots can answer questions about delivery times,
lesson plans, and curriculum;

-

chatbots can help teachers stay up to date with new
standards and evaluation models, i.e., optimize the
data analysis process;

-

chatbots can help students understand difficult
concepts during the individual study;

Using Machine Learning and, in general, artificial
intelligence techniques allows chatbots to extract context from
a conversation and respond in a personal, engaging,
conversational way - a significant advantage in the world of elearning [18] [19]. Moreover, using natural language in the
learning process can be helpful in the self-assessment process
[20].
Tutoring is one of the most used in chatbot field.
AutoTutor [21] is an example of an intelligent assistance
system based on man-machine conversation. Such system has
been able to demonstrate that learning through computer
systems of interaction that provide natural language is
equivalent to the traditional learning process. A practical
learning support tool is represented by Ms Lindquist [22]. This
assistant, through interaction with the user, offers a practical
didactic path able to motivate the students.
Against this background, Chatbots could represent the best
tool in personalized training in the workplace that does not
involve high costs for the company. That makes the learning
activity pleasant and not boring at the same time [23]. If an
employee needs support for a given activity, an e-learning
chatbot could effectively guide him towards a specific training
path [24]. According to the company's directives, the material
and the courses can be freely consulted by the user based on
their personal needs or the chatbot - communicate a mandatory
training course and the time to complete it. Companies will be
able to monitor the status of employee training in real-time.
A chatbot can also act as a virtual assistant in a training
path: if the user has not completed a course provided by the
company, the bot can remind him to proceed indicating the
possible terms to do so. This type of function always puts the
users in a position to correctly complete their training and help
them to not forget a required course.

III.

SYSTEM ARCHITECTURE

A. Modules
The Inferential Motor includes several submodules:
-

Text pre-processing

-

LDA Analyzer

-

Query classifier

-

Interaction manager

Submodules allow ontology mapping and attribution of
meaning by providing a user response. This response can be
final or intermediate. All this relies on the Knowledge Base
(KB). The KB represents the database of knowledge
containing the provided services and teaching materials.
Other modules that make up the architecture are:
•

Topics & Dictionary Builder: the module that allows
to define key terms to be identified in user questions
and the annotated lexicon of equivalent terms.

Fig. 1. System Architecture.

•

Domain Ontology Builder: the module that, through a
web-based interface, allows to build and manage the
domain ontology.

•

Dialogue Ontology Builder: it allows the
identification of the topic that characterizes a
dialogue, in order to be able to subsequently build
adequate answers.

• Interaction Quality Tracker: the module that allows
monitoring of the communications between the user
and the system. This module allows to highlight
critical aspects of the interactions and the
improvement.
• Human-Computer Interaction Supervisor: the module
that has the objective of supervising the dialogue,
keeps track of the interaction times, identifies asked
questions ambiguously, non-convergent, or too long
dialogue sessions, etc.
• Context-aware Information Manager: it allows to
guide the dialogue based on the user profile and its
environment (including the user's location); it is based
on the representation of all possible contexts, through
the Context Dimension Tree [25].
• Starting Context Integration: it takes care of
transforming the initial context into useful information

978-1-7281-6942-2/20/$31.00 ©2020 IEEE
December 8–11, 2020, Online
IEEE TALE2020 – An International Conference on Engineering, Technology and Education
Page
372 20,2024 at 23:44:23 UTC from IEEE Xplore. Restrictions apply.
Authorized licensed use limited to: Radford University. Downloaded
on January

for the bot, using information such as the navigation
path, the current page, etc.
• Personalization: in the case of an authenticated user, it
takes care of correlating the user with the dialogue and
its status, that is "remember" information about the
user himself (training courses already followed, etc.).
• Post-chat Integration: it allows to manage the chat
output to other systems (eg: chat with human-tutor,
send mail, etc.) passing all the information collected
during the chat.
• Post-chat reply form: the module that enables the user
to provide feedback on the quality level of the
interaction performed.
• Anti-pranks: it detects, and limits attempts to divert the
bot and generate deliberately ridiculous or
embarrassing responses; it manages the exit in case of
offensive user behavior.
• Spell-corrector: it takes care of recognizing and
correcting typing errors by users and continuing the
dialogue; it is dependent on the language adopted.
• Chat recording & warning: the module that analyses
the conversations carried out, identifies anomalous
situations (sudden lowering of the success rate,
lengthening of conversations, etc.) and allows to
broaden the Knowledge Base or the interaction
methods.
B. Features
The main features are:
• Real-time assistance/Live Support: the inference
engine with that of context awareness will be able to
process the questions asked by users in real time,
offering precise explanations and advice with respect
to what is required.
• Efficient training: users will be guided towards the
discovery of new teaching materials; in doing so,
research costs will be reduced and the learning process
accelerated, which will be improved in terms of
efficiency.
• Personalized/Customized and contextualised training:
through the context-aware module, the system will be
able to analyse user behaviour to determine interests
and the context in which it is located, in order to search
for “custom-made” training material and provide it at
the most appropriate time.
C. Core
The Inference Engine represents the core of the proposed
architecture It includes the processing of textual information,
the deduction of the real needs and intentions of the user. This
is achieved through several sub-modules, in particular,
through a module based on Context Dimension Tree (CDT)
[26] [27], which deals with context extraction. Thanks to the
CDT the system is able to generate chats relevant to contextual
information. In this scenario, the appropriate model for
analysis and correlation between keywords and topics is the
Latent Dirichlet Allocation (LDA) [28]. Each topic, in fact,
refers to a contextual element.
The proposed system, therefore, through the analysis of
textual information and then through the elaboration of the

context defines the user's reality. In this way the chatbot is able
to recommend the services necessary to satisfy users in a
tailored way. The textual analysis allows to know the
employee through hierarchical information of employment,
location, tasks and real needs [29].
The interaction process between user and system is
divided into sentences. These sentences, defined clusters, are
identified through keywords and ontological filters.
The proposed system identifies the probability P that a W
word belongs to an NC concept node in the CDT [26]. This
probability P is proportional to the number of times the word
W has been used within that argument. This system is able to
analyze chats automatically, regardless of the semantic value
of the words[30].
The LDA approach has also been used in our field of
interest, Industry 4.0, by automatically extracting the Mixed
Graph of Terms (mGT). The mGT is able to contribute to the
design of the Context Dimension Tree (CDT) by identifying,
in real-time, context constraints. The LDA approach has been
useful in generating and identifying the CDT's chat topics
[20].
Wanting to go into detail, the LDA considers, for each
argument ݅, a distribution of terms ߮௜ taken from a symmetric
Dirichlet distribution with parameter ȕ:
ௐ

߁ሺܹߚሻ
ఉିଵ
‫݌‬ሺᢥ௜ ȁߚሻ ൌ
ෑ ‫׎‬௜௩
ሾ߁ߚሿௐ
௩ୀଵ

As before, ȣୢ represents the topic distribution for a
document ݀ represented by a Dirichlet distribution with
parameter ߙ:
௄

‫݌‬ሺߠௗ ȁߙሻ ൌ

߁ሺσ௄
ఈ ିଵ
௜ୀଵ ߙ௜ ሻ
ෑ ‫׎‬ௗ௜೔
௄
ς௜ୀଵ ߁ሺߙ௜ ሻ
௜ୀଵ

The topic ‫ݖ‬ௗ௡ is chosen from the distribution of the topics
as:
‫݌‬ሺ‫ݖ‬ௗ௡ ൌ ݅ȁߠௗ ሻ ൌ ߠௗ௜
Each token ‫ ݓ‬is chosen from a multinomial distribution
associated with the selected topic:
‫݌‬ሺ‫ݓ‬ௗ௡ ൌ ‫ݒ‬ȁ‫ݖ‬ௗ௡ ൌ ݅ǡ ᢥ௜ ሻ ൌ ‫׎‬௜௩
The LDA approach is used to find co-occurrences and
define the topics. The Mixed Graph of Terms (mGT), which
represents a complex graph structure, is able to collect
contextual information containing a series of texts related to
a specific field of interest. This structure can also represent
such contextual information and extract information
automatically, improving the extraction of a specific context.
The graph structure can be formally defined as ݃ ൌ൏
ܰǡ ‫ ܧ‬൐ where:
• ܰ ൌ  ሼܴǡ ܹሽ represents a set of nodes.
•

‫ ܧ‬ൌ  ሼ‫ܧ‬ோோ ǡ ‫ܧ‬ோௐ ሽ represents a set of arcs.

The methodology presented is composed of two essential
modules within the inference engine. These modules, as
shown in figure 2 (a), deal with the construction of the Mixed
Graph of Terms and the extraction of the context elements
[29].
•

Mixed Graph of Terms construction module: this module
deals with the automatic construction of the mGT. From
a series of documents related to the same field of interest,
it is possible to extract contextual information. In

978-1-7281-6942-2/20/$31.00 ©2020 IEEE
December 8–11, 2020, Online
IEEE TALE2020 – An International Conference on Engineering, Technology and Education
Page
373 20,2024 at 23:44:23 UTC from IEEE Xplore. Restrictions apply.
Authorized licensed use limited to: Radford University. Downloaded
on January

addition, mGT can contribute to the development phase
of the CDT.
•

Context Extraction Module: This module takes care of
the extraction of context elements and uses the mGT as
a context filter. The output of this module is the context
related to the chat, which is administered as input.

Inside the system database, each context element is
associated with a dedicated section. The context extraction is
done automatically by composing various partial views of
each section. This methodology, as shown in figure 2(b) can
be used to extract useful services with respect to the current
context.

After this preliminary experimental phase, also the
employees of Group 2 had the opportunity to interact with the
prototype. All new employees participated in a final
evaluation questionnaire according to the Likert scale. The
questionnaire covered five sections, and each answer was
associated to 5 possible answers: "I totally disagree" - TD, "I
disagree" - D, "Undecided" - U, "I agree" - A, "I totally agree".
The five sections had the aim to understand better and analyse
the advantages and disadvantages of the prototype realised.

Fig. 3. Questionnaire answer trend

Fig. 2. Mixed Graph of Terms (mGT) and Context Dimension Tree
(CDT) at work.

IV.

EXPERIMENTAL RESULTS

This section deals with the experimental phase, which was
conducted through a prototype. This prototype includes a
mobile app developed according to the methodology proposed
in the system architecture section.
In this first experimental phase, 30 newly hired employees
were involved in a company, who at different times were
asked to interact with Chatbot. A heterogeneous group made
up of 50% of the new employees (15) was involved in the
experimental phase by undergoing training only through the
Chatbot concerning the new tasks to be covered, the remaining
part followed a traditional training pathway. The experimental
phase, relating to the first group, provided for the employees
to develop the theoretical training through the Chatbot in
autonomy concerning regular working hours. At the end of
this experimental phase, a test was conducted to assess the
learning difference between the different groups.
The test covered seven specific sections of a company
training process, and for this reason, the content of the test
cannot be disclosed. However, we have available the
anonymous numerical data of the correct answers percentage
for each section divided by Group 1 that participated in the
experimental training phase and Group 2 that participated in
the traditional training phase. The results obtained have been
summarized in a graph in Figure 3, which shows the potential
of the proposed system. In particular, this graph shows that in
several sections, the results obtained by Group 1 are better
than those obtained by Group 2 and in the remaining sections
are comparable. These results are very encouraging and
maybe due both to the effectiveness of the system developed
and to the possibility that Group 1 participants have had in
managing their organization and learning times.

In particular, section A concerns usability; in this section,
it was possible to understand if the developed prototype is
intuitive and easy to use and if its speed is adequate. Section
B concerns the recommendation; in this section, it was
possible to understand if the information received was in line
with the user profile and context information. Section C is
about the presentation; this section has to do with the quality
of the information presented and its completeness. Section D
deals with the quality of the dialogue that the prototype is able
to maintain; the linearity and understanding it shows in
interacting with users is evaluated. Section E deals with future
developments; in this section, it was possible to understand
whether users were interested in the development of a
prototype for other work purposes and professional training,
or the application in different scenarios. Below, in the Table
1, are reported all the assertions.
TABLE I.

QUESTIONNAIRE ASSERTIONS

Section

n

Assertion

A

1

The Chatbot interface is userfriendly

2

Response times are adequate

1

The proposed contents have
satisfied the needs of the user

2

The system has managed to
adapt based on personal
preferences and the current
context

1

The information provided by
the system has been adequately
presented

2

The information provided by
the system has been exhaustive

Usability

B
Recommendation

C
Presentation

978-1-7281-6942-2/20/$31.00 ©2020 IEEE
December 8–11, 2020, Online
IEEE TALE2020 – An International Conference on Engineering, Technology and Education
Page
374 20,2024 at 23:44:23 UTC from IEEE Xplore. Restrictions apply.
Authorized licensed use limited to: Radford University. Downloaded
on January

1

The dialogue with the Chatbot
took place smoothly and
without unexpected jumps

2

The system was able to
understand the intentions of the
user correctly

1

It would be useful to include the
Chatbot for other company
training activity and refresher
training

2

It would be interesting to apply
the same approach to other
scenarios.

D
Dialogue

E
Future
development

advantages of the proposed system is the simplification of
learning and the reduction of this process.
Future developments include a more robust experimental
phase and the use of the chatbot to update employees
concerning new facilities or new production processes. It is
also under implementation a version of the chatbot for
employees with disabilities, who have specific training needs
due to their impairments. The characteristics of the chatbot
could also facilitate novices to understand and access expert
employees practices in workplaces, exercising a tutorship
function. In this way, the proposed system could represent a
new means of enrichment and innovation of modern
Intelligent Industries.

Table 2, Table 3 and figure 4 show the results of the
following questionnaire. As can be seen from the reports, the
product system has to be improved in the dialogue section. On
the other hand, in the sections concerning the recommendation
according to the context, in particular, the management of the
right training courses at the right time, very encouraging
results were obtained.
TABLE II.

QUESTIONNAIRE ANSWERS

Section

Answer

Fig. 4. Trend of responses to statements.

TD

D

U

A

TA

A

3

2

5

21

29

B

2

2

0

19

37

C

0

6

3

20

31

D

6

5

5

23

21

E

3

4

0

24

29

TABLE III.
Section

Y. Lu, “Industry 4.0: A survey on technologies, applications and
open research issues,” J. Ind. Inf. Integr., vol. 6, pp. 1–10, Jun.
2017 DOI:10.1016/j.jii.2017.04.005.

[2]

K. Ashton, “That ‘internet of things’ thing,” RFID J., vol. 22, no.
7, pp. 97–114, 2009.

[3]

L. Da Xu and L. Duan, “Big data for cyber physical systems in
industry 4.0: a survey,” Enterp. Inf. Syst., vol. 13, no. 2, pp. 148–
169, Feb. 2019 DOI:10.1080/17517575.2018.1442934.

[4]

M. Gaeta, V. Loia, and S. Tomasiello, “A generalized functional
network for a classifier-quantifiers scheme in a gas-sensing
system,” Int. J. Intell. Syst., 2013 DOI:10.1002/int.21613.

[5]

F. Colace, M. De Santo, M. Lombardi, F. Pascale, D. Santaniello,
and A. Tucker, “A Multilevel Graph Approach for Predicting
Bicycle Usage in London Area,” in Fourth International Congress
on Information and Communication Technology. Advances in
Intelligent Systems and Computing, vol 1027, vol. 1027, Y. XS., S.
S., D. N., and J. A, Eds. Springer, Singapore, 2020, pp. 353–362
DOI:10.1007/978-981-32-9343-4_28.

[6]

F. Abate, M. Carratù, C. Liguori, M. Ferro, and V. Paciello, “Smart
meter for the IoT,” in I2MTC 2018 - 2018 IEEE International
Instrumentation and Measurement Technology Conference:
Discovering New Horizons in Instrumentation and Measurement,
Proceedings, 2018, pp. 1–6 DOI:10.1109/I2MTC.2018.8409838.

[7]

F. Amato, F. Moscato, V. Moscato, and F. Colace, “Improving
security in cloud by formal modeling of IaaS resources,” Futur.
Gener. Comput. Syst., vol. 87, pp. 754–764, Oct. 2018
DOI:10.1016/j.future.2017.08.016.

[8]

D. Gorecky, M. Schmitt, M. Loskyll, D. Zuhlke, and D. Zühlke,
“Human-machine-interaction in the industry 4.0 era,” in 2014 12th
IEEE International Conference on Industrial Informatics (INDIN),
2014, pp. 289–294 DOI:10.1109/INDIN.2014.6945523.

[9]

H. Shah, K. Warwick, J. Vallverdú, and D. Wu, “Can machines
talk? Comparison of Eliza with modern dialogue systems,”
Comput. Human Behav., vol. 58, pp. 278–295, May 2016
DOI:10.1016/j.chb.2016.01.004.

[10]

R. S. Wallace, “The Anatomy of A.L.I.C.E.,” in Parsing the

ANALYSIS OF RESULTS
Percentage

Negative

Neutral

Positive

A

8,33%

8,33%

83,33%

B

6,67%

0,00%

93,33%

C

10,00%

5,00%

85,00%

D

18,33%

8,33%

73,33%

E

11,67%

0,00%

88,33%

V.

REFERENCES
[1]

CONCLUSIONS

In this article, a chatbot framework has been presented,
which aims to be an innovative solution in employee training
in industry 4.0. According to the experimental results, this
application suggests important implications for both the
company and the employee.
The experimental results were obtained on a group of new
employees who were able to learn the latest training processes
through chatbot with promising results. One of the main

978-1-7281-6942-2/20/$31.00 ©2020 IEEE
December 8–11, 2020, Online
IEEE TALE2020 – An International Conference on Engineering, Technology and Education
Page
375 20,2024 at 23:44:23 UTC from IEEE Xplore. Restrictions apply.
Authorized licensed use limited to: Radford University. Downloaded
on January

Turing Test, Dordrecht: Springer Netherlands, 2009, pp. 181–210
DOI:10.1007/978-1-4020-6710-5_13.
[11]

D. Ferrucci, E. Brown, J. Chu-Carroll, J. Fan, D. Gondek, A. A.
Kalyanpur, A. Lally, J. W. Murdock, E. Nyberg, J. Prager, N.
Schlaefer, and C. Welty, “Building Watson: An Overview of the
DeepQA Project,” AI Mag., vol. 31, no. 3, p. 59, Jul. 2010
DOI:10.1609/aimag.v31i3.2303.

DOI:10.1007/978-1-84882-215-3_13.
[21]

A. C. Graesser, P. Chipman, B. C. Haynes, and A. Olney, “Auto
tutor: An intelligent tutoring system with mixed-initiative
dialogue,”
2005
IEEE
Trans.
Educ.,
DOI:10.1109/TE.2005.856149.

[22]

N. T. Heffernan and E. A. Croteau, “Web-Based Evaluations
Showing Differential Learning for Tutorial Strategies Employed
by the Ms. Lindquist Tutor,” in Lecture Notes in Computer Science
(including subseries Lecture Notes in Artificial Intelligence and
Lecture Notes in Bioinformatics), 2004, pp. 491–500
DOI:10.1007/978-3-540-30139-4_46.

[12]

M. Horowitz, “1.1 Computing’s energy problem (and what we can
do about it),” in 2014 IEEE International Solid-State Circuits
Conference Digest of Technical Papers (ISSCC), 2014, pp. 10–14
DOI:10.1109/ISSCC.2014.6757323.

[13]

S. Quarteroni, “Natural Language Processing for Industry,”
Informatik-Spektrum, vol. 41, no. 2, pp. 105–112, Apr. 2018
DOI:10.1007/s00287-018-1094-1.

[23]

D. Griol and Z. Callejas, “An Architecture to Develop Multimodal
Educative Applications with Chatbots,” Int. J. Adv. Robot. Syst.,
vol. 10, no. 3, p. 175, Mar. 2013 DOI:10.5772/55791.

[14]

A. Chawla, A. Varshney, M. S. Umar, and H. Javed, “ProBot: An
Online Aid to Procurement,” in 2018 International Conference on
System Modeling & Advancement in Research Trends (SMART),
2018, pp. 268–273 DOI:10.1109/SYSMART.2018.8746954.

[24]

N. Zalake and G. Naik, “Generative Chat Bot Implementation
Using Deep Recurrent Neural Networks and Natural Language
Understanding,”
Mar.
2019
SSRN
Electron.
J.,
DOI:10.2139/ssrn.3362123.

[15]

F. Colace, M. De Santo, M. Lombardi, R. Mosca, and D.
Santaniello, “A multilayer approach for recommending contextual
learning paths,” J. Internet Serv. Inf. Secur., vol. 10, no. 2, pp. 91–
102, 2020 DOI:10.22667/JISIS.2020.05.31.091.

[25]

M. Casillo, F. Clarizia, F. Colace, M. Lombardi, F. Pascale, and D.
Santaniello, “An Approach for Recommending Contextualized
Services in e-Tourism,” Information, vol. 10, no. 5, p. 180, May
2019 DOI:10.3390/info10050180.

[16]

K. Schulz, A. Beyer, M. Dreyer, and S. Kipf, “A data-driven
platform for creating educational content in language learning,” in
CEUR Workshop Proceedings, 2020.

[26]

[17]

J. N. Davies, M. Verovko, O. Verovko, and I. Solomakha,
“Personalization of E-Learning Process Using AI-Powered
Chatbot Integration,” 2021, pp. 209–216 DOI:10.1007/978-3-03058124-4_20.

F. Daniel, M. Matera, E. Quintarelli, L. Tanca, and V. Zaccaria,
“Context-Aware Access to Heterogeneous Resources Through
On-the-Fly Mashups,” Springer, 2018, pp. 119–134
DOI:10.1007/978-3-319-91563-0_8.

[27]

F. Colace, M. Lombardi, F. Pascale, and D. Santaniello, “A
Multilevel Graph Representation for Big Data Interpretation in
Real Scenarios,” in Proceedings - 2018 3rd International
Conference on System Reliability and Safety, ICSRS 2018, 2019,
pp. 40–47 DOI:10.1109/ICSRS.2018.8688834.

[28]

R. Krestel, P. Fankhauser, and W. Nejdl, “Latent dirichlet
allocation for tag recommendation,” in Proceedings of the third
ACM conference on Recommender systems - RecSys ’09, 2009, p.
61 DOI:10.1145/1639714.1639726.

[29]

F. Clarizia, M. De Santo, M. Lombardi, and D. Santaniello, Elearning and industry 4.0: A chatbot for training employees, vol.
1184. 2021 DOI:10.1007/978-981-15-5859-7_44.

[30]

V. Cassani, S. Gianelli, M. Matera, R. Medana, E. Quintarelli, L.
Tanca, and V. Zaccaria, “On the role of context in the design of
mobile mashups,” in Communications in Computer and
Information Science, 2017, pp. 108–128 DOI:10.1007/978-3-31953174-8_7.

[18]

[19]

[20]

F. Colace, M. De Santo, M. Lombardi, and D. Santaniello,
“CHARS: a Cultural Heritage Adaptive Recommender System,”
in Proceedings of the 1st ACM International Workshop on
Technology Enablers and Innovative Applications for Smart Cities
and Communities - TESCA’19, 2019, pp. 58–61
DOI:10.1145/3364544.3364830.
F. Clarizia, F. Colace, M. Lombardi, F. Pascale, and D.
Santaniello, “Sentiment Analysis in Social Networks: A
Methodology Based on the Latent Dirichlet Allocation Approach,”
in Proceedings of the 2019 Conference of the International Fuzzy
Systems Association and the European Society for Fuzzy Logic and
Technology (EUSFLAT 2019), 2019 DOI:10.2991/eusflat19.2019.36.
A. Kerry, R. Ellis, and S. Bull, “Conversational Agents in ELearning,” in Applications and Innovations in Intelligent Systems
XVI, London: Springer London, 2009, pp. 169–182

978-1-7281-6942-2/20/$31.00 ©2020 IEEE
December 8–11, 2020, Online
IEEE TALE2020 – An International Conference on Engineering, Technology and Education
Page
376 20,2024 at 23:44:23 UTC from IEEE Xplore. Restrictions apply.
Authorized licensed use limited to: Radford University. Downloaded
on January


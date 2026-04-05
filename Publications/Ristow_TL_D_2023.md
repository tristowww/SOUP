# A Person-Centered Approach to Understanding Perceived Deception in Job Advertisement Text

Teresa Lauren Ristow

Virginia Polytechnic Institute and State University
Doctor of Philosophy in Psychology
April 24, 2023, Blacksburg, VA

Committee: Ivan Hernandez (Chair), Charles Calderwood, Rachel Diana, Neil Hauenstein

Keywords: Recruiting, Job Advertisement, Perception, Deception, Natural Language Processing, Latent Profile Analysis

## Abstract

Regardless of industry or job type, most organizations aim to recruit large qualified
applicant pools via job advertisements or postings. With little control over those individuals that
choose to apply and those that do not, organizations and their recruiters are likely to do what they
can to increase their applicant pool. This allows for more options in potential hires during the
selection process. In order to control the applicant pool as much as possible, recruiters can try
and influence potential applicants through the posted job advertisement. Therefore, it is
reasonable to assume that many recruiters will write a slightly inflated or overly positive view of
the job in order to appeal to more applicants. However, individuals job searching may perceive
this attempt as misleading or deceptive. In order to understand perceived deception in job
advertisements and what features of their text elicits an overall negative attitude towards the
advertisement, this study proposes a mainly exploratory approach to discover if there is a
homogenous higher-level construct of perceived deceptiveness or if there is a more personcentered approach via latent profile analysis (LPA) to explain what applicants perceived as
deceptive. After the nature of perceived deceptiveness is better understood, this study aims to
utilize natural language processing (NLP) topic modeling to find common deceptive topics
within different dimensions of the job posting such as, pay, benefits, qualifications, etc. With the
limited empirical guidance provided to practitioners, the proposed study can help facilitate
research on best practices in job advertisement writing to gain qualified and quality candidates.
In turn, those candidates will tend to maintain positive attitudes towards the job and organization,
which can persist even after being hired.

## General Audience Abstract

In today's job market, organizations aim to attract qualified applicants through appealing
job advertisements. However, some applicants may perceive these attempts as misleading or
deceptive. This study explores whether there is a common view of what is deceptive within the
text of a job advertisement or if it varies based on individualized perceptions. This study aims to
classify different types of applicants and their associated perception of deception in job ads. This
study also employs natural language processing techniques to analyze the language used in job
advertisements, pinpointing common deceptive themes in various sections of the job posting,
such as pay, benefits, and qualifications. By uncovering how people perceive deception in job
ads, this study hopes to provide valuable insights to organizations for crafting more honest and
transparent job postings. This can attract high-quality candidates who maintain positive attitudes
towards the job and organization, ultimately contributing to improved hiring practices and
fostering a more positive work environment.

## Acknowledgements

I have so many people in my life to thank for their support, effort, and encouragement
throughout this process. All whom this final dissertation and successful defense could not have
come to fruition without. I specifically want to say thank you to Dr. Ivan Hernandez for being an
incredibly influential advisor, whose unwavering support and experience guided me through a
final dissertation I can feel proud of. I also want to thank the members of my committee: Dr.
Charles Calderwood, Dr. Neil Hauenstein, Dr. Rachel Diana, and Dr. Danny Axsom, who all
never hesitated to provide advice and expertise to guide my dissertation process. I also want to
thank all of the members of the CORE lab including Emily Kim, Christopher Huyn, Fabrice
Delice, and Yasmine Elfeki. A special thanks to the CORE lab members, Kelsi Cornett and Amal
Chekili, who were always in the lab space with me and provided endless support. I owe huge
amounts of thank yous to Brandon Minton for being my dissertation buddy and going through
this process at the same time; you have been an invaluable source of encouragement and
reassurance. I want to thank Emily Rost, Molly Minnen, Tanya Mitropoulos, and many others for
cultivating a climate of community in Virginia Tech’s Industrial/Organizational Psychology
program. A major thank you to my mother, Diana Ristow, brother, Evan Ristow, and father, Paul
Ristow, whose love and support helped get me through the tough times. Finally, a massive thank
you to my partner Rick Baldwin for his endless tolerance and calm demeanor to keep me
grounded, as well as my dog, Luna, who spent many hours sleeping on the couch besides me as I
worked on this manuscript.

## 1 Introduction

This dissertation seeks to further the understanding of the type of phrases, statements, and
text features in online job advertisements that applicants perceive as deceitful or misleading.
This project, foremost, examines whether deceptiveness is universally perceived by respondents,
or whether perceptions fall into smaller more cohesive groupings that emphasize different
aspects of a job advertisement such as pay, benefits, job duties, and qualifications that seem to
lead to perceptions of deceit. By using a Latent Profile Analysis (LPA) on the deceptiveness
ratings across various job advertisements and their dimensions, this research can demonstrate the
homogeneity/heterogeneity of people’s perceptions of deception. Following that analysis with a
Natural Language Processing (NLP) transformer model can illustrate what features of text and
the text itself produce deceptive perceptions for individuals. Modeling the different sections in a
job advertisement using topic analysis techniques in NLP can help identify the specific text of
each job dimension that make up misleading advertisements. From these results, the project has
the potential to inform future organizational recruitment practices and improve job seekers’
perceptions of online job postings.

## 2 Literature Review

### 2.1 Job Postings as a Form of Advertising

The existing literature on advertising predominantly focuses on product or service-based
advertising, leaving more unconventional types underexplored. One such area with limited
research is the understanding of factors that motivate potential employees to apply for jobs based
on job advertisements (Breaugh & Starke, 2000; Rynes & Cable, 2003). Recent reviews of
recruiting research acknowledge the persistent knowledge gap in comprehending the process and
factors influencing applicants' decision-making based on job postings (Rozario et al., 2019).

Applied research has progressed towards using machine learning to predict applicants' likelihood
to apply (Reddy et al., 2020) and developing algorithms for candidate-job matching (Faliagka et
al., 2012). However, these contemporary data analytic approaches have yet to fully explain the
recruitment process from a perceptual standpoint. The literature often assumes potential
applicants evaluate recruitment messages based on attribute-claim matching, rather than
assessing the truthfulness or deceptiveness of the claims. This perspective overlooks the
importance of the perceived credibility of job advertisements in influencing candidates' decisionmaking processes.
Various terms, such as job postings, job ads, or job announcements, refer to an
organization's effort to attract prospective employees and communicate information about job
openings. Regardless of the terminology used, these advertisements play a crucial role in shaping
potential applicants' perceptions and interest in pursuing job opportunities with the organization
(Kim & Angnakoon, 2016). In this process, employers are motivated to achieve a goal of
obtaining a large and qualified applicant pool, which would be mutually beneficial for both
parties (Collins & Han, 2004). With the outcome of this process being an individual’s application
to a job, job advertisements function very similarly to more generic advertisements for products
and services that can lead to buying behavior. Both types of advertisements involve a decisionmaking process in that the individual takes into account their attitude formed towards the
advertisement and associated job (or product/service). Further relating job advertisements to
more traditional advertising, job advertisements seek to promote an overall perception and
attitude towards the organization or job based on the job advertisement (Cable & Graham, 2000).
These perceptions formed by a potential candidate can be due to just the job posting and
typically require no additional outside knowledge (Borstorff et al., 2007).

Attitudes formed from a job advertisement can come from cognitively processed or
affectively processed cues within the job advertisement. That is, a variety of features can result
in a positive or negative attitude towards an advertised job and impact an applicant’s decision to
apply (Roberson et al., 2005). Cognitive information could come in the form of an employee
analyzing the skills the job requires and matching it to the skills they currently possess or skills
typically required of the job type. More affective information could be signaled via the nuance in
words the advertisement chooses. For example, the use of a statement like, “we are like a family”
versus using a statement like, “we have a collaborative culture” could make a potential employee
feel differently despite their similar meaning. Additionally, job advertisements may even be
more relevant to research because outcomes for both applicants and employers can be high
stakes.

### 2.2 Perceived Deception in Job Advertisements

The goal result of an organization that posts a job advertisement is to get a larger number
of qualified applicants. From a successful hiring perspective, assuming the validity of selection
measures is equal across organizations as well as cut-off thresholds, these two variables are the
primary determinants of hiring quality (Taylor & Russel, 1939). To achieve this goal,
organizations may present the best version of themselves and the job opening with the job
advertisement. This display of the organization’s “best self” can be viewed as a tactic to achieve
a competitive advantage (Fomburn & Shanley, 1990; Rindova & Fomburn, 1999). Displaying
positive aspects of the job and organization such as, work life balance options, wellness
programs, or competitive benefits enables an organization to gain a competitive advantage
beyond the competition of similar organizations offering similar job opportunities (Bradley et al.,
2008). Due to the impact recruiting and advertising messages have on a job searcher’s intentions

to apply to a job, there is a strong motivation for organizations to post job advertisements that
applicants would be most likely to apply to (Cable & Graham, 2000; Gatewood et al., 1993; Lee
et al., 2013).
Applicants tend to form their initial attitudes towards a job and organization from the job
advertisement (Rynes & Cable, 2003; Zottoli & Wanous, 2000). Due to the job advertisement
acting as the source of primary influence on the attitude formation process of an applicant,
organizations may not only be motivated to present the most attractive information about the job
and organization, but also to inflate those features as well. This may lead to a fine line between
an organization designing a job advertisement that is realistic but focused on positive
information and a job advertisement that slightly inflates those positive features to appear more
attractive to applicants and increase the applicants’ job pursuit intentions.
With common goals of the recruitment process being an increase in applicant interest,
attractiveness of the job and organization, and applicant attention, this slight inflation of positive
attributes is not uncommon in job advertising (Karim et al., 2021). This process mirrors the
deception found commonly amongst more traditional advertising of products and services.
Similar to the impact an individual’s attitude has on their decision to buy a product or not, an
individual’s reliance on job advertisement content enables them to make a decision on whether
they will apply to the job or not (Becker et al., 2019). In the case of perceived deception in a job
advertisement, an individual can be expected to form a negative attitude towards the job and
organization if they feel some aspect of the job advertisement is deceptive, this could lead to
subsequent negative effects.
When numerous individuals perceive job advertisements as containing deceptive or
misleading information, this perception can negatively affect the organization's reputation on a

broader scale. The rapid dissemination of information through social media can further amplify
this effect, as deceptive advertisements can be quickly shared and discussed among many
individuals, casting the organization in a negative light (Sivertzen et al., 2013). A job
advertisement that is viewed negatively or perceived as deceptive may also have a substantial
adverse effect on both the size and quality of the applicant pool. Given the ease to which job
seekers can apply for positions online, a large number of potential applicants may come across a
job posting. So, even minor elements perceived as deceptive could significantly influence their
decision to apply.

### 2.3 Defining Deception in Advertising

A nuanced but important aspect of discussing deception in advertising is understanding
the language typically used within this recruitment context. This project adopts the consumer
perspective of deception (Haefner, 1972), because job advertisements are developed to attract
qualified applicant pools, and thus, the self-selection and de-selection of job applicants play a
major role in the final organizational outcome (Taylor & Russell, 1939). In the consumer
perspective of advertisements, deception is commonly measured in a single-item asking
individuals on their feelings of how misleading the advertisement seems. It can be assumed that
perceived deception can be equated with the term misleading in terms of measurement (Gardner,
1976; Haefner, 1972). Indeed, deception and misleading perceptions are used interchangeably in
measuring deception in experimental studies as well (Mitra et al., 2008). Therefore, the
subsequent discussion of deception focuses on a perceptual element, defined by the target of the
advertisement, and their belief of the intent of the advertiser. This consumer-focused definition
distinguishes the concept from “inauthenticity,” which is thought of as an active impression
management process that includes deceptive behaviors (Chawla et al., 2021). Therefore, it is not

all encompassing to use these words interchangeably, and the term deception in subsequent
sections refers to perceptions of it that advertisements elicit.
A company or organization’s motivation to generate a positive or favorable attitude
towards their product or service can lead to presenting only positive information in an
advertisement (Marks & Kamins, 1988). With the competitive nature of advertising, companies
may find that it is not enough to just present the benefits of their product, but it is also necessary
to exaggerate those benefits to gain a competitive advantage. These exaggerated benefits tend to
produce an advertisement that is overly positive. When inflating the true nature of what is
advertised, it can border deception. Deception in advertising is so prevalent that the Federal
Trade Commission (FTC) has been involved in regulating advertising, including deceptive
advertising, since its beginning in 1914 (Gardner, 1975).
There are other factors that can lead to deceptive feelings besides the overt claim being
made. This is similar to how advertisements take different appeals to presenting information to a
consumer (emotional and rational) (Johar & Sirgy, 1991; Stafford, 2005). In both emotional and
rational appeal, advertisements can depend on more than just the message delivered to influence
a consumer’s attitude. For example, the speaker delivering the message, the graphics included in
the advertisement, the tone of voice, the specific words chosen to convey the message, or even
music used in the advertisement can be used (covering potential ads of several different formats).
In order to capture more nuanced forms of deception, it is important to take a consumer
perspective approach in defining deception. While this may not be the most effective approach
for legal purposes, it is the most effective way to define deception for research and explain the
deception or feeling of being misled that people experience when viewing certain advertisements
(Haefner, 1972). Taking a consumer-focused approach to defining deception places emphasis on

the perception someone has of an advertisement. That is, there is not necessarily a need to verify
if the claims stated in the advertisement are true or not (Haefner, 1972). Additionally, an
individual may be able to perceive things that lead to deceptive feelings that cannot be as easily
fact checked in the more legal based definitions of deception in advertising (Armstrong et al.,
1980). This type of consumer-focused deception can be more specifically referenced as
perceived deception (Román, 2010). The term perceived deception maintains the consumerfocused definition of deception and emphasizes the role of the ad viewer.

### 2.4 Perceived Deception as an Attitudinal Component

In the context of attitude formation, what someone perceives in an advertisement impacts
their processing and evaluation of whatever is perceived. Armstrong et al. (1980) elaborates on
deception as it relates to attitude formation and states that due to beliefs formed about an
advertisement, consumers are able to readily access their attitudes towards an advertisement. In
this belief/attitude relationship, ad viewers will form an attitude towards a product as a function
of an initial belief developed from what they perceive in an advertisement (Gardner, 1975).
Therefore, deception in advertisements can be viewed as a component of an overall negative
attitude formed towards that ad perceived in a certain way by the consumer (Gardner, 1976).
Attitudinal evaluations are typically categorized into either favorable or unfavorable
feelings (Eagly et al., 1998; Eagly & Chaiken, 2007). So, if a consumer feels they are being
deceived when viewing an advertisement, that deception will contribute to an overall
unfavorable attitude. Scale development of authenticity perceptions as a part of a favorable
attitude, provides evidence that the alternative of deceptive beliefs towards an advertisement
exist and can contribute to an overall unfavorable attitude (Stepchenkova & Park, 2021).
Additional support for perceived deception as a component of an individual’s attitude towards an

advertisement is provided by Held & Germelmann (2018) in their review of attitudinal theories
of deception.

### 2.5 Mental Processes Associated with Perceived Deception

The attitudinal component that encompasses perceived deception implies that deception
processes include the same components, per Fishbein's definition of attitudes, as used in an
attitude formation process. Specifically, the evaluative components of attitudes include beliefs
about the object and their evaluations (Fishbein & Ajzen, 1974). These beliefs and evaluations
can come as antecedents or consequences of an attitude and are drawn on as a basis of the
attitude formation process. In the context of advertising, the behavioral component is included
primarily as an outcome. The behavior that is most relevant to predict in this relationship is
typically buying behaviors. Due to this behavioral component in the attitude formed based on the
consumer-focused definition of deception, this definition can also be referenced as the behavioral
meaning of deception. This definition can be seen as the behavioral component in that a
consumer’s attitude impacts their buying behavior, especially that of a salient negative attitude in
the case of deception (Haefner, 1972). This relationship between attitudes and behaviors displays
an effect where an attitude correlates with a behavior. Meaning that the behavior can come either
before or after, but there is a strong correlation between the two (Kim & Hunter, 1993). This
relationship between attitudes and behavioral effects of deception in advertising holds within the
context of both overtly deceptive advertising as defined by the FTC and more consumer
perception-based definitions (Oliver, 1979).
In Fishbein's perspective on attitude formation, perceived deception is a piece of an
attitude that fits into a traditional attitude formation framework. In this framework, deception in
advertising is viewed from a dual process perspective. This implies that some perceptions of

deception come from effortful thinking and processing, which are based on an individual's
beliefs about the object and evaluations of those beliefs (Fishbein & Ajzen, 1974), and some
from more automatic feelings towards the advertisement (Darke & Ritchie, 2007).
In the attitude formation framework, examples of perceived deception from a consumer’s
perception may not be viewed as deceptive in legal definitions or by FTC standards. This is,
individuals may process beliefs about the object and evaluations of those beliefs from an
advertisement in a way that the actual presentation of the information is not considered directly
deceptive in legal standards (whether the claim differs from reality). These beliefs and
evaluations can lead to the formation of a negative attitude based on a deceptive feeling the
consumer gets in response to the advertisement.
In addition to the cognitive component in the attitude formation process, there can exist
an affective component as well. While it is not necessary to have both in an attitude formation
process, it is relevant to advertising due to the different appeals advertising tends to take
(emotional and rational). Fishbein's perspective on attitudes recognizes that individuals' beliefs
about an object, and evaluations of those beliefs, can be influenced by affective factors such as
emotions or feelings (Fishbein & Ajzen, 1974). These affective factors can come from features
of the ad that are not direct facts or claims made but instead generate a feeling towards the
product. Some affective sources of information can come from features such as the speaker
delivering a message in an ad, graphics included in the ad, or the tone of voice used to deliver the
message. These features are typically aimed at generating a positive attitude towards the product.
However, it is possible that instead, a consumer may have a negative affect towards a feature in
an ad due to the feeling of deceptiveness.

Overall, perceived deception is a piece of an attitude that fits into Fishbein’s attitude
formation framework. In a similar vein, both rational and emotional appeals to a consumer in an
ad can promote different processing and recall upon decision-making situations. Therefore,
perceived deception can come from explicit claims in an advertisement or from a more general
impression of an advertisement.

### 2.6 The Dimensionality and Measurement of Deception in Advertising

When defining deception from a consumer’s perception, it takes a claim-belief stance.
That is, deception is referenced to by what the advertisement claims and then what the consumer
believes or perceives from that claim (Armstrong et al., 1980). Some conceptualizations of
deception break down the perception into several dimensions that analyze the specific claims
made in the advertisement and compare them to the reported beliefs of the consumer (Johar,
1991). However, these dimensions are not easily utilized because they do not generalize across a
variety of product types. Deception is also thought to be broken into dimensions based on intent
of the advertiser and comparisons to the reality of the product (Chaouachi & Rached, 2012). In
this perspective, the dimensions based on intent fail to address that consumers’ perceptions of
deception are typically unaffected by intent of the advertiser and often consumers cannot
distinguish between intentional deception and their perception of deception (Nath and Gardner,
1986). Also, including dimensions of deception related to the reality of the product may not be
known to the individual. Thus, perceived deception can be conceptualized as a component of an
overall feeling of inauthenticity towards an advertisement (Haefner, 1972). While the other
factors of inauthenticity include consumers’ reports of feelings such as enjoyment, monotony,
information, dislike, and brand loyalty, these are difficult for consumers to report on when they
have no prior knowledge, experience, or exposure to the advertisement or product being

advertised. Therefore, the dimensionality of true perceived deception is best collapsed to a single
dimension (Haefner, 1972; Nath & Gardner, 1986). This perspective ensures that the consumers
do not need prior exposure to the ad. A single dimension of perceived deception also enables
consumers to disregard features such as intentions of the advertiser and details of the specific
product that may be difficult for the consumer to perceive or pick up on.
General methods to capture an individual’s perceived deception towards an advertisement
are similar in structure. The procedure used to measure deception is typically formatted where
the participant is shown a series of real or constructed advertisements and the participant is asked
follow up questions regarding the viewed advertisement. The advertisement can be in a variety
of formats and can be designed to be deceptive or unknown to the researcher. These
advertisements can be a random sample of different brands of a single product or a pair of
experimentally manipulated deceptive and non-deceptive versions of a single advertisement
(Gardner, 1975; Harris, 1977). The nature of the advertisements shown depends on the
researcher’s question of interest. Additionally, the questions asked of the participants after
viewing the advertisements depend on the way that deception is measured by the researcher.
Deception is mainly measured in three ways: the normative belief technique, the
expectation screening procedure, and the consumer impression technique (Armstrong et al.,
1980; Gardner, 1975). The normative belief technique focuses on attributes of a product that are
necessary for its class. Any reported additional or excessive levels of an attribute by a
knowledgeable consumer of the product class can deem there is evidence of deception. Further
investigation into acceptable ranges of these attributes is then needed for support of deception.
While this procedure and measurement of deception is thorough for a specific product class, it
requires prior knowledge and may skew the perception of deception in that case.

The expectation screening procedure compares expected norms of a product class to the
norms of an advertised product. That is, an expectation is developed by the consumer and
compared to the perception of a given advertisement. If the expectation exceeds a reasonable
level for the product class, then there is evidence for deception in the advertisement. This method
still suffers from participants having to form an educated expectation of a product and may not
generalize to products the participant is unfamiliar with. With prior expectations potentially
impacting perceptions in the normative belief and expectation screening procedures, it is difficult
to separate deception perceived from the advertisement and deception formed from experience
with the product class.
However, the consumer impression technique takes a more general approach and is based
on consumer’s perceptions of stimuli and the impressions they form. This is thought to be the
most direct measure of perceived deception and can be measured via a simple single question
survey based on reported feelings of deception (Armstrong et al., 1980; Gardner, 1975).
Additionally, this method is most directly related to the definition of perceived deception as a
part of an overall negative attitude formed towards an advertisement stimulus. A modified form
of the consumer impression technique called the salient belief technique, initially used by
Armstrong et al. (1980), focuses on the attitude formation process and then includes its impact
on potential buying behavior. Thus, the one-item deception survey to measure perceived
deception can sometimes be supplemented by an intention to purchase question (Johar & Sirgy,
1991). These methods most directly measure perceived deception as a piece of a negative
attitude towards an advertisement a consumer may have no prior experience with. While many
features in an advertisement can lead to perceptions of deception and may be captured by the
normative belief technique and the expectation screening procedure, the consumer impression

technique and more specifically, the salient belief technique best measure true perceptions of
feeling deceived when viewing an advertisement.
Using a one-item perceived deception measure to assess an individual’s attitude formed
towards an advertisement that they may be unfamiliar with allows for a more generalizable
measure of deception. Specifically, participants are asked to report how misleading they feel the
advertisement is as a whole, to get an overall deception rating. Additional factors of the ad can
be reported by individuals in the same manner to find specific information on what the
participants feel is misleading within the advertisement. This helps to direct them to the different
components that are of research interest, because many individuals will form an overall
impression of deception without knowing the individual factors in the advertisement contributing
to that perception (Gardner, 1976; Haefner, 1972).
Typically, the single deception item can be worded by asking outright whether the
advertisement seems deceptive, misleading, or if claims made in the advertisement were
unbelievable (Haefner, 1972). This single item of measuring deception is best reported by the
participants themselves, as they are the individuals that can most readily report their attitudes
upon viewing an advertisement (Gardner 1976; Nath & Gardner, 1986). Additionally, an overall
score of perceived deception for an advertisement can be computed by averaging the ratings of
deception of all participants viewing the advertisement. This can be useful in comparing levels of
deception across multiple different advertisements but may not provide much insight as a standalone score of deception (Gardner, 1976). Another means of computing deception is by using a
difference score or similarity measure in participants’ perceived deception ratings (Harris, 1977).
In studies of deception outside of advertising, in contexts of dating profiles, perceived deception
is also measured using a similar single-item scale (Toma & Hancock, 2012).

Support for using a single item of perceived deception as a part of an overall negative
attitude is found in other verified measures of attitudes. One such example is the use of a single
item to measure an employee’s job satisfaction. The single item measure is found to be valid in
correlating to relevant measures and predicting turnover intentions (Nagy; 2002; Wanous et al.,
1997). Single item attitude scales can also effectively measure affect by asking participants their
beliefs on something, which directly influences their attitude (Bodur et al., 2000; Beal et al.,
2005). Additionally, single-item scales are more commonly used in organizational research and
there is empirical evidence for their effectiveness in measuring attitudinal constructs (Fisher et
al., 2016; Matthews et al., 2022).

#### 2.6.1 Relevance of Text in Job Advertisements

In understanding the process of perceived deception in advertising, specifically in the
form of job postings, it is relevant to indicate the form of the advertisement. Designating what
applicants are forming their perception of deception from allows for a better understanding of
what features applicants tend to perceive as deceptive. In reviewing the current state of
organizational recruitment, many organizations and companies are moving towards a
technologically based recruitment method. That is, online recruitment is becoming increasingly
prevalent as a means for organizations to advertise their job postings. Specifically, about 50% of
job recruitment was done online as of 2000 (Zottoli & Wanous, 2000) and is likely much higher
as recruitment/network sites like LinkedIn launched later in the decade, and work has shifted
more remotely. Online job advertisements enable the sharing of information on the organization
and job to the applicants in an efficient and effective way (Borstoff et al., 2007). The internet
allows organizations to maximize the range of applicants that see their job postings, creating a
more diverse, qualified, and larger applicant pool. Additionally, one survey shows that 85

percent of companies with 500 or more employees in North America maintain an online
recruiting presence (Schweyer, 2004).
On the other side, job seekers are also relying on online recruitment sources; as over 52
million Americans have used online job searches and 4 million searches online daily for job
openings (Jansen et al., 2005). Not only is online recruitment prevalent, but it is low cost and
efficient for the candidate and organization (Borstorff et al., 2007). Millennial job candidates that
are dominating the workforce, are more likely to apply to jobs online and view organizations
positively that maintain an online presence (Allen et al., 2007; Zusman & Landis, 2002).
The online nature of the majority of job advertisements comes from recruitment websites,
such as Indeed.com, Monster.com, Ziprecruiter.com, and many others (Baum & Kabst, 2014).
These make it even easier for an applicant to click and apply via provided templates for
organizations to convey relevant information to job seekers. These templates are primarily textbased and allow the organization to communicate a large amount of information in a single job
advertisement. Therefore, text plays a salient role in the job advertisement that applicants use to
form an attitude or to perceive deception.

#### 2.6.2 Text Cues in Advertisements

Understanding the text in job advertisements that cue deception or misleading feelings to
job seekers enables organizations to avoid seemingly deceptive text in posting a job
advertisement online. The relevance of job advertisement text in applicant’s perceptions, attitude
formation, and subsequent intentions to apply to the job, has previously been studied. However,
this focus is mainly on the positive aspects of the job advertisement that influence applicants to
pursue the job. For example, general inclusion of certain text descriptions of the expected worklife balance of the job increases applicants’ reported attraction to the job (Ehrhart et al., 2012).

Organizations that include statements demonstrating the organization’s values tend to attract
more applicants than organizations that do not (Highhouse et al., 2002). This allows job seekers
to see if they maintain values that match those of the organization and those individuals with
matched values are more attracted to the organization. Another positive aspect in job
advertisements that leads to an increase in an individual’s intention to apply to a job, is the
scarcity information provided for the position (Highhouse et al., 1998). Specifically,
organizations that state how many applicants they are hiring and how many positions are left for
a certain job posting, tend to be viewed as more reputable and prestigious by applicants.
Inclusion of human resource practices in a job ad also increases intent to apply in groups of
Black applicants (Highhouse et al., 1999).
These prior examples demonstrate the positive impact text can have on an applicant’s
attitude towards the job and organization and further impact their intention to apply (Allen et al.,
2007; Highhouse et al., 2003). However, there is limited research on the influence text has on
deception in a job advertisement context. Understanding the elements of a job advertisement that
impact applicants’ feelings of deception and lead them to avoid applying, may be more
influential than those positive text features that encourage applying. In much of the literature on
avoiding negative attitudes, individuals tend to weigh negative features more strongly than
positive features (Baumeister et al., 2001).

#### 2.6.3 Detection of Perceived Deception in Text

While deception within general text has been studied, this is not frequently translated to
the text in job advertisements. It can be assumed that text within job advertisements functions
similarly to deceptive text in prior research. Specifically, in terms of the variety in the structure

and features that can convey deception and elicit an overall negative attitude towards a job
posting.
Prior reports of deception detection by human raters are shown to hold in the detection of
entire false or deceptive statements. This is relevant in the detection of written legal statements
by lawyers or investigators, who tend to be more accurate at detecting deception via text opposed
to in facial expressions (Matsumoto et al., 2011). Additionally, deceptive or false statements are
able to be detected by individuals across languages (English, Spanish, and Chinese). This is
commonly referred to as statement analysis to examine written statements or interview
transcripts for verbal cues of deception, including linguistic markers such as, the statement
structure, grammatical techniques, and word usage (Matsumoto et al., 2015).
Previous usages of text to predict deception show that computer-based programing can
actually be trained on text in order to perform better than humans at detecting deception using
specific words (Newman et al., 2003). Additionally, categorizations of textual features can act as
indicators to deception. These features can be statements that are overgeneralized, selfreferences, lengthy text, or overly negative statements (Furnham & Taylor, 2004). Contextual
frameworks of deception detection also indicate that text can convey both cognitive and
emotional elements of deception depending on the context (Markowitz & Hancock, 2019). These
examples of prior research on detecting deception in text indicate that textual features can
convey perceptions of deception to individuals and computers can even be trained to replicate
and improve upon that detection.

#### 2.6.4 Potential Cues of Perceived Deception in Job Advertisement Text

While, deception research in the context of job advertisements is limited, an example of
the detection of deception in an online advertisement setting is prevalent in online dating

profiles. Through means of self-preservation, individuals tend to positively inflate their dating
profiles online. However, people can pick up on linguistic cues that indicate lies in their written
biographies (Toma & Hancock, 2012). In determining whether an individual’s online dating
profile contains some semblance of lies, people pick up on several different features. Similarly,
there are a wide range of job advertisement characteristics that can convey deception to
applicants and impact not only their perception, but also their attitude formed and intention to
apply for the job (Walker et al., 2008). It can be assumed that text can convey deception in many
ways. In order to direct that assumption, it is necessary to look at prior research on job
advertisements that indicates which features of text may be likely to make an applicant perceive
deception or feel mislead.
One text feature that may indicate deception is the repetition of statements in job
advertisements. Specifically, repetition may relate to processing fluency within a single job
advertisement viewed by an individual. That is, the more a statement of relevance is repeated
within a job advertisement, the easier it will be for an applicant to process it (Alter &
Oppenheimer, 2009). While this is found in a variety of contexts, semantic priming of a
statement creates an easier time for an individual in processing similar or repeated follow up
statements, later in a job advertisement. This fluency or ease of processing a specific statement
or information that is repeated in a job advertisement also facilitates positive judgements and
decisions (Morewedge & Kahneman, 2010). Research on fluency typically indicates that the
processing ease leads individuals to form a positive attitude towards the target (Storme et al.,
2015). However, this effect may only function within a single job advertisement. That is, if the
information that is repeated throughout the advertisement is consistent with the prior information
advertised, applicants will feel a more positive, and potentially authentic attitude towards the ad.

This is due to applicants being able to form attitudes towards a job advertisement based on their
cognitive information received from a job advertisement (Mitchell & Olson, 1977). In the case of
fluency between job advertisements, it could potentially have the opposite effect, because there
is time between viewing ads and there is not cognitive fluency. Additionally, seeing the same
information between multiple ads could signal to individuals that the advertisement is reusing
information from a standard job ad or from other job advertisements. Instead of having a positive
attitude due to fluency, this repetition in statements across job advertisements could lead to
deceptive feelings and a negative attitude formed towards the ad. A similar effect could create a
lack of fluency for information that is inconsistent within a single job advertisement. That is, if
an applicant reading a job ad finds conflicting information, it could lead to feelings of deception
as well.
Another feature depicted in job advertisement text that could lead to perceptions of
deception is a lack of information surrounding the pay depicted in the advertisement. When
investigating the factors of job advertisements that influence job-seekers to pursue the job in the
advertisement, pay and salary information tend to be the most influential in motivating applicants
to apply to a job (Khan et al., 2013). Thus, text features surrounding the description of pay for a
job in an advertisement is relevant in the attitude formed towards the ad. If an individual finds
the pay information deceptive, then the overall attitude towards the job advertisement may be
negative. Specifically, pay information that is ambiguous can feel misleading to individuals
viewing the job posting (Yüce & Highhouse, 1998). This could also translate into large ranges of
pay that are provided appearing ambiguous and deceptive to individuals. Cognitive components
of attitudes towards pay could also lead to deception. If an individual has prior knowledge of
what a typical salary or pay range for a job type would be, and an advertisement depicts the job

as earning much more than that range, it could lead to cognitive information that feels deceptive
or misleading based on feelings of skepticism.
This cognitive information leading to attitude formation could also apply to individuals’
prior experiences with qualifications for similar jobs or job duties. Therefore, if a job ad depicts
unrealistic expectations for qualifications or duties that are above and beyond what is typically
expected for the job type, it could lead to applicants feeling misled by the information in the
advertisement. With a move towards more telework options as well, job advertisements could
mislead applicants by promising a work from home or telework option that seems positive but
unrealistic. Work-life balance promises could also function in a similar way. With many jobs
being depicted in the media, people have a general idea of the work-life balance for many job
types and can determine what is realistic to expect from a certain position of interest. For
example, if a job ad for a doctor promises flexibility in work hours, it could seem deceptive and
too good to be true.
Misleading features in a job advertisement could also be more generalized, such that job
advertisements which have a lack of information could elicit feelings of misleadingness. This
could be that the organization fails to provide detailed information or descriptions on a variety of
aspects about the job. This lack of information could also be due to the organization trying to
reach a larger audience and gain a larger applicant pool. However, a lack of specific information
about the job can actually lead applicants to have lower intentions to complete the job
application, which would actually lead to a smaller applicant pool (Feldman et al., 2006). Failure
to include a comprehensive description of any aspect of the job could lead applicants to have a
more negative attitude towards the organization as well (Lee et al., 2013). When organizations
fail to include specific details in their recruitment advertisements, applicants feel that the ad is

less truthful and will be less likely to continue the application process and view the organization
more negatively (Farida, 2010). More specificity in the rewards and benefits information
included in the job advertisement can lead to job advertisements being viewed more positively
(Verwaeren et al., 2017). Specifically, providing actual and realistic pay ranges can lead to more
positive attitudes and intentions to apply to the job.
In addition to a lack of information or information specificity, ambiguous information
can lead to applicants developing a deceptive attitude towards the job advertisement (Mitra et al.,
2008). Even if information is actually included in features of the job advertisement, applicants
may still feel that it is misleading if that information is ambiguous, such as a wide range
provided in the pay for a job. Additionally, applicants tend to prefer seeing action statements in
job postings that provide information to the specific job duties employees will do on the job
(White et al., 2019). This emphasizes that ambiguous, non-action oriented information fails to
provide enough detail for applicants to view the advertisement as authentic and accurate. It can
also be relevant that unnecessary information included may be perceived as deceptive, as it
provides no details and may cause ambiguity. As an extension of the text that applicants view as
deceptive, it is possible that features of the text like question marks, statements posed as
questions, unnecessary exclamation points, or odd text spacing may lead to ambiguity and
further the feelings of deceptiveness.
To date, only one study has examined deception perceptions via a rhetorical analysis of
job ads (Engstrom et al., 2017). The analyses suggest that job advertisements may oversell
positions and certain rhetoric may seem inauthentic. The authors suggest to include less clichés
and metaphors, as well as included fewer creative statements. While this provides more
evidence-based suggestions, the provided suggestions are simply words or phrases to avoid

using, and only a few are given. It also assumes homogeneity among these perceptions, whereas
people may differ quite dramatically in how they perceive the same ad.

### 2.7 Methods to Detect Deception in Job Advertisements

To detect deceptiveness systematically, researchers in computer science have started to
incorporate computational approaches. For example, researchers used a computer program to
scan behavioral features listed as skill requirements in job advertisements and compared them to
attributes mined from similar jobs on other recruiting sites. Disparities between stated and
required job skills were operationalized as “scams” and the researchers discovered patterns in the
ad content (e.g, words, syntax) and context (e.g., visuals) in scam versus non-scam ads (Nindyati
et al., 2019). In another study using a machine learning model trained on a dataset of fraudulent
and real job ads, researchers developed a way to detect fraudulent ads (Vidros et al., 2017).
These studies, however, emphasize objective deception rather than perceptions of deception by
the labor market. They also take an engineering/optimization approach to studying deception,
relegating the features inherent in those predictive models as undescribed components of a black
box.
Understanding the text of a job advertisement that seems deceptive can help provide
further insight into the specific wording or semantics of what applicants may perceive as
deceptive. Recently, researchers have used word frequencies to look at the difference between
actual job ads and scam advertisements (Amaar et al., 2022). Although not emphasizing
perceptions, this study found that many fake advertisements show differences to real ads in their
wording of the job title. In addition to ignoring perceptions, word frequencies are also limited in
that they lose the context of the surrounding words, which could interact with each other to make
the ad more or less deceptive. A more advanced text model, GPT-3, which can generate/edit text

along a specified criterion, was employed to create diversity statements in job advertisements
that were indistinguishable from human-generated statements (Borchers et al., 2022). This
research highlights the importance of human perceptions of job advertisements, but unfortunately
did not measure actual human perceptions, nor did it provide an explanation for why certain ads
were perceived as more realistic in terms of their diversity statements.
To date, there has not been a study that covers the full spectrum of linguistic and text
components of job advertisements and what individuals may perceive as deceptive. Using
modern language analytic techniques or natural language processing (NLP), this study aims to
empirically understand the nature of individuals’ perceived deception of job advertisement text
and provide theory as to why those perceptions are formed from specific text.

## 3 Method

While prior research in advertising covers linguistic cues to deceptive or misleading text
(Gaeth & Heath, 1987; Toma & Hancock, 2012), it is not fully applied in the domain of job
advertisements. There are several studies that indicate job advertisement features that attract
employees (Allen et al., 2007; Ehrhart et al., 2012; Highhouse et al., 2002) but these studies
focus only on features that promote application and attraction to the job posting. With the
salience of negative information over positive (Baumeister et al., 2001), and the potential ability
for individuals to detect misleading or deceptive cues in advertising, there is a gap in the
literature as to what features discourage applicants from applying for jobs. Additionally, those
features that promote application are assumed to be generalizable across individuals, without
empirical support.
The following studies aim to better understand the frequency and distribution of
perceived deception in job advertisements. Then subsequently utilize that information to assess if

text cues influencing perceived deception are generalizable across individuals and there exists a
concept of a shared deceptive perception for a job advertisement. In other words, do all
individuals perceive deception or misleadingness in job advertisement text the same? Finally,
with the generalizability information of perceived deception indicating that individuals do not
share a single perception, a person-centered approach will be taken for subsequent analyses.
Once the types of individuals and their corresponding patterns of perceived deception are
assessed, text responses of the reasoning or formation of those perceptions will be condensed for
better understanding using a natural language processing topic modeling approach. This novel
and thorough method to studying deception or misleading text in job advertisements introduces
an empirically supported, person-centered approach to explore perceptions of deception.

### 3.1 Study 1: Perceived Deception Distinction

Study 1 was conducted to provide a better understanding of applicants’ attitudes of
deception towards text in job advertisements in a realistic context of job seeker’s job search
behaviors. This study provides evidence that perceptions informing misleading or deceptive
attitudes are more specific and distinct from generalized negative attitudes. That is, deceptive
attitudes are a component of an overall negative attitude (Held & Germelmann, 2018;
Stepchenkova & Park, 2021). The following study also acted as a means of collecting job
advertisement images for subsequent studies using a realistic job search.

#### 3.1.1 Study 1 Sample

Study 1 focused on collecting job advertisements searched for by undergraduate
psychology students, as a representative sample for the population of active and potential job
seekers. Specifically, 96 undergrad social psychology students completed the job search survey
and found links to 10 jobs each. With some missing data and incorrect links removed, this

resulted in a total of 628 job advertisement pictures. These images were cleaned to maintain
consistency with the headers of the website pages and remove any ads or additional features that
distracted from the text as the focal point of the study. The final used ads are available at the
following Open Science Framework (OSF) link under “Indeed Job Ads used in Study 1”:
https://osf.io/xf9e6/files/osfstorage
Part of an example job advertisement collected and used in the study is shown in Figure 4 below.
Figure 4
Example Job Advertisement

Note. This screenshot provides an example of the job advertisements collected and used in the
survey to assess perceived deception. The above job advertisement has been cleaned to remove
additional images or ratings.

Undergraduate student populations are commonly used in peer-reviewed research on job
seeking behaviors and recruitment as a means to access populations typically engaging or
preparing to engage in frequent or active job seeking behaviors (Walker et al., 2008; Yüce &
Highhouse, 1998; Zusman & Landis, 2002). Additionally, undergraduate students are those most
likely to apply to a large number of jobs and at a high rate in their job search efforts. This makes
the population especially desirable for recruitment due to the potential for a large applicant pool
for entry-level positions (Campbell & Sumners, 1995). Many recruiters and organizations also
tend to target undergraduates in career fairs and job search efforts, making it a representative
population for the target audience of many job advertisement efforts. Our undergraduate
population used to select job advertisements also provides access to a sample that represents the
majority of 65% of the population who are employed full time but do not have a college degree,
this includes those who have some college education or an associate’s degree (U.S. Bureau of
Labor Statistics, 2022).
Additionally, online job advertisements were chosen due to the accessibility and ease for
both organizations and individuals that comes with using websites for recruitment, the past ten
years have seen an increase in online recruiting activities. About 90% of large organizations use
online recruiting (Chapman et al., 2005). Overall, online recruitment websites now hold about
110 million job postings (Maurer & Liu, 2007). The widespread nature of job advertisements,
especially on web platforms such as Monster, Indeed, Glassdoor, and LinkedIn, makes a large
impact on impressions of the organization as a whole, due to the sheer amount of postings
viewed.

#### 3.1.2 Study 1 Procedure

Online job advertisements were sampled by providing undergraduate psychology
students with a survey on Qualtrics.com to complete a job search specifically on Indeed.com as
part of a course activity on attitudes. Participants were directed through the job search and asked
to provide links to ten different jobs. After completing the survey with ten job postings,
applicants were shown a debriefing page and thanked for completing the survey.
As of January 2022, Indeed.com contained 11.3 million job postings, as well as being
responsible for 65% of all hires made online (Indeed Hiring Lab, 2022). By having students
complete the job search on Indeed.com, I aim to provide a similar sample of job advertisements
to what most applicants will see in their job search. Participants were also asked to search for
only full-time positions. This is similar to the U.S. population of approximately 120 million fulltime employees out of the approximately 165 million employed individuals in the U.S. (U.S.
Bureau of Labor Statistics, 2022). Additionally, Indeed.com provides organizations with a
templated layout to input their job advertisements. This template includes several relevant
sections, such as pay, location, benefits, job duties and responsibilities, requirements, etc. This is
a conservative source of job advertisements, as they should be up to some standard of accuracy
and consistency due to the template provided. That is, if a job ad is constructed using less
structure, it may be more likely to be viewed as misleading. Therefore, ads found on Indeed.com
that are rated as deceptive provides a more generalizable source of data.

#### 3.1.3 Study 1 Measures

In the Qualtrics survey, students were asked to follow a link to Indeed.com where they
completed a realistic job search as if they were looking for a “job position they would currently
consider applying to”. They were asked to keep a specific job position in mind when doing this

job search and to input it in a text entry box. Additionally, students were asked to report what
industry the job position was in, based on the U.S. Bureau of Labor Statistics list (2022) (see
Appendix A1).
The next section of the survey asked students to find ten job advertisements based on
their chosen position and to keep Indeed.com’s search features at default. The students could
choose any location they would like to work for the job search. To get a random sample of 10 job
advertisements, students were asked to choose the first job ad on every page.
Once the students obtained ten different job postings, they were asked to include the link
in a text box and answer three follow up questions. These follow up questions included singleitem scales for attitudes, deception, and intent to apply. Specifically, a single item to assess
attitude was included. The attitude item asked participants to indicate the level to which they
agreed with the following statement: “I like the job advertisement/posting in the link I provided
above.” Participants responded on a 7-point Likert-type scale from “strongly agree” to “strongly
disagree” (see Appendix A2). Participants were asked to respond on the same scale to an item
measuring deception in advertising based on the item used in Haefner (1972), where the
definition of deception is provided as a perception of inaccuracy or feeling of being misled. The
deception item specifically asked participants to respond to the statement: “I feel the job
advertisement/posting in the link I provided above is deceiving” (see Appendix A3). Finally,
participants’ intent to apply to the job was measured using an item from Staw et al. (1986) on job
attitudes (see Appendix A4).

#### 3.1.4 Study 1 Analytic Approach

To provide evidence for the distinction between deception or misleading perceptions and
negative attitudes, a Pearson correlation coefficient was calculated between the attitude and

deception items. This correlation acts as a means of convergent validity evidence, in that
deception is not the same as a negative attitude towards a specific job advertisement, but instead
is a related construct (Campbell & Fisk, 1959).

#### 3.1.5 Study 1 Results

Convergent Validity Evidence. In order to provide support for convergent validity when
measuring deception and negative attitudes towards the job advertisements, a Pearson correlation
was run on the two items. In doing so, I aim to show that feelings of deception towards an ad are
related to a negative attitude towards the job advertisement, but only a piece of a potential
overall negative feeling. While these deceptive feelings can lead to negative attitudes, they are
novel and more specified. The results from the Pearson correlation indicated that there is a
significant, but small negative relationship, between a positive attitude towards the job ad and a
feeling of deception from the job ad (r (678) = -0.378, p < .001). In providing evidence for
convergent validity between the constructs of deception and negative attitudes should be related
but not too strongly related (Campbell & Fisk, 1959). This can be quantified as a correlation
around an absolute value of 0.7, however, this may be an overly optimistic estimate in the case of
attitudes and deception, because deception is only a piece of a negative attitude and may not be
as similar as a construct that fully captures a similar spectrum of dimensions as the negative
attitude construct.

#### 3.1.6 Study 1 Discussion

Comparing the resulting correlation coefficient of -0.378 to the standard of 0.7 for
concepts that are related but not too strongly related, there seems to be sufficient support for the
convergence of concepts. Additionally, because the absolute value of -0.378 is less than the 0.7,
it may be assumed that it reflects the nature of deception as a component of a negative attitude.

That is, the negative correlation reflects that as participants perceived job advertisements overall,
as deceptive their overall attitude decreased or was more negatively valanced. This would be
expected based on the negative nature of deception or misleading perceptions. The following
results provide support for the directed study of perceived deception as a unique contribution to
the recruiting and advertising literature.

### 3.2 Study 2: Perceived Deception Distribution and Homogeneity

After establishing the distinct nature of deception, Study 2 lends a better insight into the
base rate of perceived deception and the nature of the homogeneity of job advertisement
perceptions across several job dimensions. Combined, this information facilitates a more
informed design process in the subsequent Study 3.

#### 3.2.1 Study 2 Research Questions & Hypothesis

Research Question 1. What does the distribution of deceptiveness look like for entry
level jobs?
Hypothesis 1. The distribution will be representative of a Gaussian distribution in that
there will be just as many job advertisements rated as highly deceptive or misleading as there are
those rated as highly authentic. But most of the job advertisements will be neutral in authenticity.
This is based on the recent trend in social media bringing awareness to misleading job
advertisements (Powell, 2021; Ryan, 2017; Wong, 2022). This trend may lead more individuals
to think critically and question job advertisements in terms of their authenticity.
Research Question 2. Do ratings of perceptions across different job advertisement
dimensions demonstrate homogeneity?

#### 3.2.2 Study 2 Sample

After the survey for collecting job advertisement images, a SONA study was conducted
to assess the perceived deception of each job advertisement to new raters. This study was
constructed on Qualtrics.com and participants signed up on SONA for 1 credit hour. There was a
total of 389 undergraduate psychology students as participants. The sample of 389 participants
was composed of 33% male and 67% females, the distribution of ethnicities is: 68% white, 5%
Black or African American, 7% Hispanic/Latin-American, 16% Asian, 4% other, and the mean
age was 19.71 years (SD= 1.27).

#### 3.2.3 Study 2 Procedure

After providing consent to take the survey, participants were directed to a timed section
where they completed a series of questions on a single job advertisement that was repeated at
random for the other job advertisements until 55 minutes had passed. Participants only saw as
many job advertisements as they could complete questions for in the 55 minutes. The first part of
the timed question block for a single job advertisement showed a randomly selected image of a
job advertisement collected from the prior survey, followed by questions about the job
advertisement. Then another block with the ad was shown again with follow up questions about
feelings of overall deceit towards the advertisement. The next block repeated the same
advertisement and had participants copy text that they found deceptive and write it as they would
ideally want to see it in a job advertisement or as more authentic. Finally, participants moved on
to complete demographic questions and were debriefed before exiting the survey.

#### 3.2.4 Study 2 Measures

Participants were asked to type the title of the job and select the industry of the job from a
list from the U.S. Bureau of Labor Statistics (2022) (see Appendix A1). The participants were

then asked to rate how deceiving the job advertisement seems overall from the same scale
(Haefner, 1972) and with the same response options (7-point Likert type scale from “strongly
agree” to “strongly disagree”) as in the survey used for job advertisement data collection (see
Appendix A3).
For the same job advertisement, participants were directed to move to another page and
shown the job advertisement again. They were then asked to rate the extent that they felt
deceived or mislead by the job ad on several different job dimensions. These dimensions were
taken from the different sections that Indeed.com provides employers with to fill in. Applicants
can also see each section in the job advertisement indicated by a heading. These 11 sections
include: job description, overview of the company, salary/pay, benefits, responsibilities/duties,
skills, qualifications, schedule, education, work location, and participants were provided another
option to input any additional information they found deceptive. These dimensions were rated on
a sliding scale question type in Qualtrics, indicating how deceptive the statement from that
specific dimension is (see Appendix A5). The participants also had an option to check if the
dimension was not applicable. Participants were also asked a one-item intent to apply question
“regardless of qualifications” from the same scale as in the data collection survey (Staw et al.,
1986) (see Appendix A4).
In the last section for the same job advertisement, the job ad was shown again and asked
participants to type text from the job advertisement they found deceptive into a text entry box.
Below the text box, participants were asked to rewrite the deceptive text to appear more
authentic to job applicants. Five text boxes were provided for 5 different pairs of deceptive and
authentic text inputs. Finally, participants were asked in an open-ended question if there were
any additional features other than the text that they found deceptive.

Once the 55 minutes of job advertisement questions had elapsed, the participants moved
on to completing demographic information. This included the mini-IPIP personality measure on
a Likert type scale (Donnellan et al., 2006) (see Appendix A6). The final three demographic
questions were, ethnicity, gender, and age.

#### 3.2.5 Study 2 Analytic Approach

As a means of analyzing the distribution of deception ratings on job advertisements
(Research Question 1, Hypothesis 1), the data from study 2 were restructured to reflect the
number of job advertisements corresponding to each response option on the 7-point Likert type
scale measuring perceived deception. The distribution of deception was constructed to show
perceived authenticity corresponding to “Strongly Disagree-Neither Agree nor Disagree” on the
left of the distribution and perceived deception corresponding to “Neither Agree nor DisagreeStrongly Agree” on the right of the distribution. Then the resulting distribution was visually
compared to a Gaussian distribution.
In order to provide support for a higher-level construct of organizational impression
management and aggregate individual perceived deception scores (Research Question 2),
interrater reliability (IRR) was additionally calculated. A measure of interrater reliability was
chosen over an interrater agreement measure because of the study’s emphasis on a higher-level
construct from consistency in ratings, opposed to the ability to interchange individual ratings.
Specifically, I want to be able to aggregate the individual scores and not simply interchange
them, based on a compositional theoretical approach (Kozlowski & Klein, 2000; LeBreton &
Senter, 2008).
Interrater reliability was measured by looking at each participants’ rating of overall
deceptiveness for a job ad, per job ad. However, in the design of the study, participants only saw

a selection of job advertisements and did not rate every ad. This ultimately led to an ill-structured
matrix of the data. In the case of an ill-structured measurement design (ISMD) certain guidelines
are provided to assess interrater reliability. Putka et al. (2008) suggest an alternative to traditional
generalizability measures (G) when using ISMD by calculating G(q,k). This method aims to
adapt the ISMD to a form that can be used to assess interrater reliability and avoids the bias in
more traditional methods caused by scale length or number of raters. This method first suggests
restructuring the data so that there are 3 columns: the rater, the target of the rating, and the rating
score (Figure 5); allowing a comparison of rater scores for each job advertisement.
Figure 5
Example of Data Restructuring for Computing G(q,k) in ISMD

Note. This figure demonstrates how ill-structured measurements designs should be restructured
when utilizing the method proposed by Putka et al. (2008).
Once the data is restructured, the variance components can be estimated using standard
statistical packages (SAS, SPSS, and R) with code provided in the manuscript. In this study, SAS
was utilized to analyze IRR by generating a G(q,k) coefficient. The method of computing the

interrater reliability with an ISMD utilizes the harmonic mean number of raters per target being
rated. This allows for situations where there may be an unequal number of raters rating each
target (Putka et al., 2008). In doing so, the harmonic mean gives equal weight to each average,
regardless of the number of ratings a target receives. Additionally, this harmonic mean is
multiplied by a “q multiplier” in order to remove error and analyze the main effect of raters for
each target being rated (Putka et al., 2008). The q multiplier functions by analyzing the overlap
in the sets of raters rating each target. In the end, this method produces a value (G(q,k)) that
reflects the reliability of the mean rating for each job advertisement, or the proportion of
expected observed score variance that is attributed to true score variance.

#### 3.2.6 Study 2 Results

Distribution of Deceptive Job Advertisements. As a means of providing support for the
proposed phenomenon that job advertisements may be perceived as deceptive via specific text,
an initial distribution of ratings was produced. The single-item deception measure used to assess
perceived deception is shown in Appendix A3. This definition of deception and the way it is
measured is based on a single-item measure used in advertising (Armstrong et al., 1980;
Gardner, 1975). Participants answered this question after viewing a randomly selected job
advertisement from a sample of 628 entry level jobs.
Based on Research Question 1, the distribution of job advertisements was assessed to
determine the frequency of perceived deception in the chosen sample of job advertisements for
entry level jobs. The distribution includes all 611 out of the 628 ads that received ratings on
perceived deceptiveness. Due to the large number of ads, some were not seen and did not receive
ratings. The distribution depicted in Figure 6 is representative of a Gaussian distribution, with
many ads being perceived as neutral and less ads perceived as either extremely authentic or

extremely deceptive. Specifically, a one sample confidence interval for proportion was
calculated using an exact binomial method, with a sample size of 611 participants. Out of these,
179 indicated that they felt some aspect of the job ad was deceptive, resulting in a proportion of
29.30%, 95% CI [25.71%, 33.08%]. Therefore, Hypothesis 1 is supported by the distribution in
Figure 6. This provides support for the proposed phenomenon of job advertisement text being
perceived as deceptive. Ideally, there would be almost no job advertisements perceived as
deceptive.
Figure 6
Distribution of Job Ads Rated on Overall Perceived Deception

Note. This figure shows the distribution of participant ratings after viewing a job advertisement
and answering a single-item measure of perceived deception with a 7-point Likert-type scale.
Additionally, Table 1 breaks down the specific percentage of advertisements viewed as
deceptive, neutral, or authentic. There were about 30% of job advertisements viewed as
deceptive, which is a large percentage compared to the about 45% of job advertisements
perceived as authentic. This comparison demonstrates that while many job advertisements may

be only slightly authentic or deceptive, there are still quite a few advertisements that participants
feel are inauthentic or misleading in their text.
Table 1
Percentage of Job Advertisement Ratings
Perceived Deception Rating

Calculated Percentage of Ratings
\# of Job Ads
Rated

Total Job Ads
Rated

% of Job Ads

Deceptive
(Slightly Agree, Agree, Strongly
Agree)

29.3%

Neutral
(Neither Agree nor Disagree)

25.9%

Authentic
(Strongly Disagree, Disagree,
Slightly Disagree)

44.8%

Note. This table is constructed based on the distribution from Figure 6. Below each job
advertisement rating is the specific associated Likert-type scale responses in parentheses.
Interrater Reliability. In the current study, IRR was estimated via G(q,k) for several
different job advertisement dimensions. In addition to computing the IRR for the overall
perceived deception rating for the job advertisements viewed by more than one participant, the
specific job features were also rated and the corresponding IRRs were calculated. Specifically,
11 dimensions were used based on the sections built into the template of each Indeed.com job
advertisement. Participants rated each job advertisement on its perceived deception for each of
these 11 dimensions. Participants had the option to choose “not applicable” for a job
advertisement that did not have a listed dimension included. By calculating the IRR for overall
deception and deception for each dimension, it can provide evidence that an overall higher level
of perceived deception exists and can generalize across participants viewing the job

advertisements, for multiple job dimensions. When assessing the IRR metric, a standard of a
score greater than 0.7 is typically used as evidence that a target is perceived similarly by
individuals (Cronbach et al., 1972; Putka et al., 2008). An IRR metric can range from 0 (no
agreement) to 1 (complete agreement). Specifically, a reliability coefficient of 0.7 means that
70% of the variance in the observed score is systematic and can be attributed to participants’
ratings of deceptiveness. That is, the additional 30% of variance partitioned out is attributed to
random error. After using SAS to compute the estimate for interrater reliability using the method
for ISMD data, the reported IRR metric for overall deception and deception rating for job
dimensions did not meet the 0.7 standard (Table 2). This indicates that there is insufficient
evidence to aggregate scores across individuals for a higher level of perceived deception. This
means that individuals may not view the same text in a job advertisement as deceptive. As a
follow up exploratory analysis, the IRR was broken down by gender (Table 2) to see if gender
differences accounted for the low IRR scores. While some dimensions showed an increase in the
gender breakdown, there is still a lack of support for an overall gendered perception of deceiving
job ad text. Therefore, to address Research Question 2, there was no support that ratings of
perceptions across different job advertisement dimensions demonstrate homogeneity from the
IRR metrics computed.
Table 2
Interrater Reliability for Participants’ Deception Ratings on Job Dimensions
Rated Job Advertisements
Job Dimension

n

G(q,k)

Overall Deception

1,444

0.125

Female

1,344

0.056

Male

0.000

Benefits

1,149

0.268

Female

0.253

Male

0.242

Description

1,288

0.261

Female

0.147

Male

0.072

1,267

0.203

Female

0.097

Male

0.095

Education

1,215

0.211

Female

0.104

Male

0.095

Experience

1,210

0.211

Female

0.189

Male

0.000

Location

1,247

0.119

Female

0.060

Male

0.000

Overview

1,180

0.206

Female

0.145

Male

0.101

1,191

0.228

Female

0.286

Male

0.070

Qualifications

1,261

0.188

Female

0.085

Male

0.059

Schedule

1,182

0.162

Duties

Pay

Female

0.118

Male

0.151

1,237

0.209

Female

0.056

Male

0.129

Skills

Note. This table shows the interrater reliability (IRR) metric of G(q,k) when using ill-structured
measurement designs (ISMD). The metric for overall deception and the additional 11 dimensions
did not meet the 0.7 standard for agreement and aggregation of the individual scores. The n
column shows the number of advertisements that had more than one rater in common and an IRR
metric was able to be calculated. Additionally, the breakdown into separate genders did not meet
the 0.7 standard for IRR metrics.

#### 3.2.7 Study 2 Discussion

Due to the lack of agreement amongst raters across multiple dimensions of job
advertisements and within genders, Study 2 is followed up with an approach that addresses these
limitations. Therefore, the reasons for the lack of agreement must be better understood.
Specifically, the seen lack of agreement could be caused by an actual lack of shared perceptions
as to what is deceptive in the text of a job advertisement. However, there are many job
advertisements rated as deceptive based on the distribution in Figure 6, so it is likely that another
factor in the study design is causing the low interrater reliability scores.
Specifically, there may not be much overlap in the advertisements viewed by participants.
With the large amount of job advertisements and the small amount of job advertisements rated
per participant, there may not be enough ratings per advertisement to reflect shared perceptions.
The survey had a total of 611 job advertisements rated by 389 participants. When the participants
were arranged by which ads they had viewed, a total of 1,971 ratings of advertisements were
provided by all participants. The ratings able to be used in calculating IRR were 1,444 out of the
1,971, because they corresponded with a job advertisement that had more than one rater. The

computed overlap in job advertisements seen by participants (Mean overlap = 0.082, Max
overlap = 4) was too low to provide evidence for a shared perception. Additionally, participants
only rated about 7 ads on average, which was not enough to create a higher overlap in job
advertisements seen. The calculations for these numbers are found in the following Open Science
Framework (OSF) link under “Check_Overlap_in_IDs.iypnb”:
https://osf.io/xf9e6/files/osfstorage
In addition to the lack of overlap in job advertisements rated, there was a small increase
in interrater reliability when breaking down the overall deception into dimensions. This may
indicate that a more nuanced view of perceived deception is needed to capture the full picture of
how job advertisement text is perceived. Specifically, a more person-centered approach may be
appropriate. Support for this approach is based on prior literature as well. In assessing job
preferences amongst individuals, a person-centered approach is often used to examine different
groups of individuals that value different organizational features (Turban et al., 1993). The
person-organization fit perspective demonstrates that individuals typically seek values in their
future organization that match their own (Cable & Judge, 1994). For example, a woman that has
a young child may value spending time with that child and value an organization that presents
authentically in their work schedule section in a job advertisement. To address these elements of
study design and understand perceived deception from a more person-centered perspective,
Study 3 was conducted.

### 3.3 Study 3: A Person-Centered Approach to Perceived Deception

In response to both a push in organizational research for more person-centered
approaches and a low interrater reliability metric, an additional study was conducted (Morin et

al., 2018). Study 3 aims to address the evident issues in survey design in order to be more
directed and informed in data collection.
Specifically, after computing the interrater reliability from ill-structured measurement
designs following Putka et al. (2008), insufficient evidence for an overall shared perception of
deception was found. However, it was also evident that due to the missingness, not many
individuals were actually seeing the same job advertisements. To address this, Study 3 used a
shortened survey with fewer job advertisements and fewer questions, in addition to more time
allocated to complete the job advertisement survey.
Study 3 included only 10 job advertisements (based on the 7-job ad per hour average
rating computed for Study 2). These job advertisements were selected from the original sample
of 628 by choosing the 5 most deceptive and 5 least deceptive/authentic ads based on
participants’ average ratings to be able to capture variation within and between groups. The 5 job
advertisements found to be the most deceptive (see Appendix B1) and most authentic (see
Appendix B2) based on participants’ average ratings can be found at the following OSF link
under “Indeed Job Ads used in Study 3”: https://osf.io/xf9e6/files/osfstorage
Additionally, due to the subjective or artificial nature of these ratings, and the lack of shared
perceptions of what is deceptive in a job advertisement, choosing the most deceptive and
authentic advertisements is simply a proxy for the ads with the most salient features to rate. That
is, they may not be truly the most deceptive or authentic due to the varied nature of perceptions,
but they are the job advertisements that individuals felt the most strongly about specific text,
which produced a sample of representative job advertisements with text cues for rating.
Study 3 also provided participants with 1.5 SONA credits to complete and described to
participants that it should take about 1.5 hours. This adjusts participants' expectations of how

long the survey takes and does not time them. While the survey from Study 2 restricted
participants to rate within the timed 55 minutes, participants can realistically take as long as they
want to rate all 10 job advertisements in Study 3.
In providing participants with more time and realistic expectations all participants can
rate all the provided job advertisements. This smaller sample of job advertisements ensured that
everyone is able to rate the same job advertisements, creating a non-sparse N people x K jobs
predictor matrix, and avoids the prior missingness problem in Study 2.
To further prevent missingness, the survey is reduced to only the essential items.
Specifically, all participants saw the same job advertisements and simply rated them on overall
deceptiveness, and deceptiveness of each job dimension. If a participant rated a job
advertisement or dimension as deceptive (greater than 4 on the Likert-type scale), they were
asked to input text into a response box to provide their reasoning as to their rating of deception
This shorter survey also avoids survey fatigue effects and elicit more thoughtful responses.
The final adjustment to the survey for Study 3 was the addition of two types of checks to
ensure that participants were in fact reading the job advertisements and answering thoughtfully.
The first type of check was done using 4 synonymous questions that should have the same
answer if a participant is answering attentively (Curran, 2016; DeSimone et al., 2015; Meade &
Craig, 2012). The second type of check simply asks participants if they responded seriously at
the end of the survey (Aust et al., 2013; Verbree et al., 2020). These adjustments based on the
prior studies allow for less missing data and more thoughtful responses in order to assess
perceptions of deception from a person-centered perspective.

#### 3.3.1 Study 3 Research Questions

Research Question 2a: How many latent profiles best explain perceptions of deception
within the various job dimensions (e.g., do people view pay statements as similarly deceptive
and non-deceptive)?
Research Question 2b: What is the proportion of respondents belonging to each profile?
Research Question 2c: What is the nature of the profiles’ response patterns?
Research Question 3: Within different groupings of deceptiveness perceptions (i.e.,
latent profiles) for each dimension, what are the common reasons people give for why they found
the dimensions misleading or deceptive?
Research Question 3a. What are the commonalities within those perceptions across all
dimensions?

#### 3.3.2 Study 3 Sample

A single round of data collection was conducted for Study 3. In order to maintain a
consistent and representative sample of job seekers, Study 3 utilized SONA study systems. The
survey was constructed and taken on Qualtrics.com and participants from a South Eastern
University signed up on SONA for 1.5 credit hours equal to 1.5 hours of time spent completing
the survey. There was a total of 302 participants that responded to the survey. However, with the
removal of inattentive respondents, the final sample size for analysis was 114. The sample of 114
participants was composed of 28.07% male and 71.93% female, the distribution of ethnicities is:
64.04% white, 20.18% black, 7.02% Hispanic/Latin-American, 5.26% Asian, 3.51% other, and
the mean age was 19.56 years (SD = 1.41).

#### 3.3.3 Study 3 Procedure

Participants who signed up for the study on SONA, were provided with a weblink to
access the study located on Qualtircs.com. They were sent to a consent form, in which they were
prompted to check a box if they agreed to continue the study based on the provided information.
After providing consent, participants were told they would complete a survey that would take
about 1.5 hours. This section also detailed to participants that they would view 10 job
advertisements and be asked some follow up questions on those job advertisements.
For each of the 10 job advertisements, participants would see the job advertisement and
then be asked to rate the 11 job dimensions on how misleading the provided information seems.
After each dimension that asked about how deceptive the job advertisement seemed, the
participants were then asked to input text to provide their reasoning for their selection responses
in the deceptive question. The entire survey consisted of 10 job advertisements, where each had
11 job dimensions participants were asked to rate, with a text box for each dimension’s rating
that asked participants about their reasons for their chosen rating. This part of the survey was
expected to take about 1.5 hours to complete. The participants then moved to complete the
demographic questions and were debriefed before exiting the survey.

#### 3.3.4 Study 3 Measures

The measures included in Study 3 were derived from the Study 2 measures. Participants
rated the job dimensions per job advertisement using the same single-item deception scale as in
Study 2. After viewing a job advertisement, participants were prompted to identify a specific
dimension in the job advertisement and rate it on a 7-point scale from “Strongly Disagree” to
“Strongly Agree” as to how deceptive/misleading that portion of the job advertisement seemed
(Appendix A7). The same 11 dimensions were used as were used in Study 2, including: job

description, overview of the company, salary/pay, benefits, responsibilities/duties, skills,
qualifications, schedule, education, and work location. Once a dimension was rated, the
participants were asked to provided their reasoning, which is also depicted in Appendix A7.
A main change to this study was the concise nature of the ratings, Study 2 had
unnecessary items to the main research questions that were removed to avoid survey fatigue.
Another change was the addition of attention check items throughout the survey based on asking
participants simple questions that mean the same thing or are synonymous. This is based on the
expectation that if participants are paying attention, they should respond the same to these four
questions (Curran, 2016; DeSimone et al., 2015; Meade & Craig, 2012). To keep the questions
on theme with the survey, these questions simply asked if the participants were currently
employed, along with synonymous questions (Appendix A8). A final seriousness check item was
included at the end of the survey that asked participants if they were responding in a thoughtful
and serious manner (Aust et al., 2013; Verbree et al., 2020). This provided participants with a
chance to have their answers removed from data analysts if they were not paying attention
(Appendix A9).
The end of the survey included the mini-IPIP personality measure on a Likert type scale
(Donnellan et al., 2006) (see Appendix A6). The final three demographic questions were,
ethnicity, gender, and age.

#### 3.3.5 Study 3 Analytical Approach

Latent Profile Analysis Overview. As a follow up to address the limitations of
insufficient agreement found in the computed IRR metric (G(q,k)), a latent profile analysis
(LPA) method was used to take a more person-centered approach to the shared perceptions of
deception (Research Question 2, Research Questions 2a-2c). Due to the lack of homogeneity

amongst ratings for a specific job advertisement from the low agreement, there is not sufficient
justification to aggregate across ratings for a single job advertisement.
As a person-centered approach, LPA treats respondents as discrete groups, with
homogeneous individuals within those groups, but heterogeneous between groups. These
approaches identify unobservable subgroups within a population when the observed measures
(indicator variables) are all continuous. Examples of person-centered approaches include cluster
analysis and latent profile analysis (LPA). Different names for latent profile analysis include
gaussian (finite) mixture models or simply mixture modeling. Conceptually, Mixture Modeling
is a more flexible tool than non-parameter clustering approaches (e.g., agglomerative clustering).
These models allow people to probabilistically belong to a cluster (soft clustering), and allow for
more confirmatory methods to be used (p-values, fit indices, model comparison) making the
optimal model choice less subjective (Peugh & Fan, 2013). These features make such methods
exploratory in nature but confirmatory in validation.
The primary goal of conducting a latent profile analysis is to identify a set of multivariate
normal distributions, each with their distinctive means, variances, and covariances that can
recreate the complete distributions of responses of members. Therefore, when measuring people
on K grouping variables (e.g., ratings along different relevant dimensions), if a researcher
estimates P latent profiles, then the method will provide a variance-covariance matrix for each
profile describing the interrelationship between the K variables for that profile, as well as their
means. These can potentially be informative for assigning a qualitative label to the nature of that
profile. Simultaneously, via the Expectation-Maximization algorithm, latent profile analysis
estimates the probabilities that each person originated from each of the produced latent profiles.

Therefore, if estimating P profiles for N cases, the method creates an N x P matrix containing the
probabilities that each of the N people is a member of each of the P profiles.
Using a person-centered approach allows for a better understanding of what types of
deception individuals may perceive from a job advertisement. Job advertisements have many
distinct components such as the ones classified in the current sample of Indeed.com job
advertisements. These 11 different dimensions or categories of job features can elicit differing
perceptions of deception in individuals. By finding distinct profiles using similar patterns of
participant responses, it provides insight into what different subpopulations or profiles find
deceptive within that specific dimension of a job advertisement.
The latent profile analysis approach differs from prior approaches used to study
deception, because it emphasizes the potential for individual differences within people’s
perceptions. Research that attempts to predict what advertisements are deceptive or authentic
may find that there is not enough homogeneity amongst ratings for the same advertisement to
justify aggregating across raters. That is, it is theoretically incongruous to describe a job
advertisement as being moderately deceptive (e.g., a “4” on perceived deceptiveness), a
uniformly perceived construct, and referring to an ad as being universally deceptive, when really
it is a mixture of 1s and 7s, representing very different perceptions across individuals. Claiming
that an organization has a common climate or that a job advertisement has a shared perception of
deceptiveness necessitates support for isomorphism, or that the concept means the same thing
when translating it to a higher level of analysis (Kozlowski & Klein, 2000). While, often,
agreement indices are used to justify existence of a construct at a higher-level, for the purpose of
prediction, only interrater reliability is needed, as deceptiveness is considered in a relative sense–
why are some ads perceived as more deceptive than others. To that extent, Generalizability

theory approaches, which partition the inconsistency attributable to rater differences and to
item/ad differences, and to unsystematic error, can describe how uniformly perceptions exist
across advertisements. Low consistency within advertisements suggests that latent profile
approaches are needed to understand the heterogeneity within the responses.
The relevance of LPA in this specific use case, is its ability to capture differences in how
individuals may view the same text within a section of a job advertisement and then group them
based on a shared common pattern of responding (Spurk et al., 2020). So, those individuals with
similar perspectives as to what is deceptive will be classified together based on their similar
regression slopes. In LPA, these profile grouping predictions are viewed as stemming from a
single distribution, with each subpopulation having a distinct distribution (Woo et al., 2018).
For example, in the overview section, some individuals may find the statement, “we treat our
employees like a family” misleading and feel that it is a red flag, while others may feel that it is
authentic. This difference may come from individuals valuing job dimensions differently while
job searching, thus influencing their perceptions of the text. To capture the nuances in
perceptions, multiple LPAs were performed using the deceptiveness ratings on each of the 11 job
ad dimensions to examine the different profiles of perceptions.
Latent Profile Analysis Data Preparation. Before performing the 11 separate latent
profile analyses on each job dimension, several steps were taken; including: a power analysis, the
removal of inattentive responders, data restructuring, imputations to address any missingness,
and generalizability analysis to inform the context of the LPA results.
Power Analysis. To assess feasibility generalizability of a latent profile analysis, a power
analysis was done to address concerns about sample size suitability. Methodologists highlight the
Monte Carlo simulation method as a promising approach for estimating detection power based

on a given sample size in the context of mixture modeling (Muthén & Muthén, 1998–2010;
Muthén & Muthén, 2002; Wolf et al., 2013). This approach simulates how well the specified
analysis can recover a known profile solution (i.e., the correct number of profiles) under specific
sample size conditions. Using the “make blobs” function provided by the sci-kit learn library in
Python programming language, I simulated known cluster solutions that had unconstrained
covariance, randomly dispersed means with a variance equal to 1. These assumptions are
conservative as they simulate profiles that can occur anywhere in space for Z-scored variables.
Under these conditions and using the collected sample size of 114 participants, there is 56%
power at detecting 3 profiles (which is just one below the median number of latent profiles in IO; Spurk et al., 2020), using the Bayesian Information Criterion (BIC) as the selection metric.
The power of detection increases to 96% when looking at detecting 2 profiles. The full code for
the simulation can be at the following Open Science Framework (OSF) in the “Power Analysis”
folder in the file labeled “Actual_Sample_Size_Power_Analysis.ipynb”:
https://osf.io/xf9e6/files/osfstorage
Attention Check. The original collected sample of 302 participants who signed up for the
study consisted of 136 participants who completed the entire survey study. Within those 136
participants, 126 confirmed that they responded thoughtfully and seriously to the survey. This
was asked as a single item at the end of the survey (Appendix A9). Then final sample size used
for analysis was 114, which consisted of the remaining participants from the 126 serious
responders that also passed the attention check consisting of 4 synonymous items (Appendix
A8). That is, any participant with a variance score greater than 0 to the synonymous attention
check question, was dropped due to an indication that those questions were not answered in the
same manner and is indicative of inattentive responding.

Data Restructuring. To set up the collected data to run the 11 LPAs for each job
dimension, participant ratings of each of the 10 job advertisements were separated by dimension.
In doing so, a smaller dataset of participant deceptive ratings for a single job dimension was
created. This was repeated for each of the 11 dimensions, resulting in 11 different smaller
datasets. Once the ratings were separated by dimension, it displays the data to show how
individuals rated each of the 10 job advertisements in terms of deceptiveness for a specific
dimension. Table 3 shows an example of how these dimensions were represented in a smaller
dataset of participants' deception ratings per job advertisement.
Table 3
Example Deception Ratings for a Job Dimension
Participant ID

Benefits
Job Ad 1

Benefits
Job Ad 2

Benefits
Job Ad 3

Benefits
Job Ad 4

A

B

Note. This table shows an example of how profiles were generated using LPA for each job
dimension and participants' deception ratings on those dimensions for each of the 10 job
advertisements. In this example, participants rated the deception of the benefits section and the
similarity in patterns of responding between participant A and B as well as, participant C and D
demonstrate that they will likely be in the same profile.
Imputation. To address any missingness in the resulting datasets for each dimension, an
imputation was run. Specifically, imputations per dimension were run in R programming
language using the mice package (Multivariate Imputation by Chained Equations) (van Buuren
& Groothuis-Oudshoorn, 2011). The “mean” option was used as a conservative imputation
option to avoid artificial inflation of intercorrelations for the 10 job advertisements. Because the

Chronbach’s alpha is a function of how correlated the different jobs are, using alternative
methods such as predictive mean matching could potentially lead to an increase in the
generalizability coefficient of the job advertisement dimension. Results, however, did not
qualitatively differ from different model choices.
Mean imputation was done for the dataset with the job advertisement ratings for each of
the 11 dimensions. Mean imputation imputes missing values by calculating the mean of the
observed non-missing ratings for a single job advertisement and replaces the missing values for
that job advertisement with the calculated mean; this is done for each of the 10 job
advertisements (Schafer, 1997). Which, due to the low amount of missing data after removal of
inattentive participants (< 0.0001%), may have been due to computer issues due to the forced
response nature of the survey answer set up.
Generalizability Coefficient. As a means of reassessing the Generalizability coefficient
with the redesign of the survey used in Study 3, G-theory was used to calculate the
Generalizability coefficient as a measurement of reliability. Specifically, G was computed using
the “gtheory” package (Moore, 2016) in R per the guide by Huebner and Lucht (2019). Based on
Huebner & Lucht (2019) study 3 uses a crossed one-facet design in that, there is only one facet
of the job advertisements for items rated and every person rates each item. This measurement of
p persons on i items is defined as ܺ௣௜ . This can be expressed as:

ܺ௣௜ = ߤ + ‫ݒ‬௣ + ‫ݒ‬௜ + ‫ݒ‬௣௜

(1)

Where ߤ is the grand mean and the ‫ݒ‬Ԣ‫ ݏ‬are the variance components. In the above
formula, (Brennan, 2001) ‫ݒ‬௣ and ‫ݒ‬௜ are the main effects of the persons and items and ‫ݒ‬௣௜ is the
interaction effect. Once the main effects and interaction effects are computed to determine
different sources of variability that contribute to the total observed variance, the “gtheory”
package in R uses an ANOVA to estimate the variance components using the main effects

means, the deviation scores, and the sum of squares for each main effect and their interaction.
This provides insight into the variance that can be attributed to the items, to the raters, and that is
error or left unexplained.
It is also relevant to assess how much of the variance or fluctuation in ratings can be
attributed to the raters or participants themselves and not the job advertisements or items, to
further analyze the shared nature or lack of a perception of deception in job advertisements. To
do so, the variance attributable to the raters is divided by the total variance. The resulting number
is then subtracted from 1 to get the G-coefficient as a measure of rater consistency (Monterio et
al., 2019). This provides a measure of how much score fluctuation can be attributed to
participants rating in a consistent manner. That is, the closer to 1, to more consistent the
participants’ ratings are to each other.
This framework for reliability evaluation can further help understand the nature of
perceptions of job advertisement text in the context of both Study 2 and 3 and how the number or
nature of job advertisements, level of missingness, or study design. Additionally, looking at the
source of variance for each dimension can further inform subsequent research on job ad
perceptions.
Latent Profile Analysis Implementation. After initial cleaning and analyses were run,
11 latent profile analyses were performed on each of the job dimensions. By running an LPA on
each of the dimensions, a more holistic perspective can be taken as to whether profiles of
perceptions look similar or have distinctions across different dimensions. That is, dimensions
like salary may show more profiles in terms of similar response patterns than the company
overview, which may show less profiles, providing insight into the different perceptions or how
much variety there is in perceptions of job dimensions that make up a typical online job

advertisement. Additionally, in running all 11 LPAs, a supplemental overall deception dimension
was not included as in the prior Studies 1 and 2 due to the repetitive nature of the construct. It is
expected that the more detailed and informed nature of each dimension will provide more
theoretical insight than profiles of overall deception could.
The same approach was used to analyze the profile fit for each dimension. Specifically,
the “tidyLPA” package in R was utilized to assess profile fit (Rosenberg et al., 2018). “tidyLPA”
was chosen due to its ease in comprehensive comparisons between model fits. While some of the
options for model assumption are not relevant for the job ad rating data, the first three models’
assumptions in “tidyLPA” have more universal and conservative assumptions that generalize to
more data. Some of the additional models have assumptions that variables are uncorrelated with
each latent class, which is not the case in this situation, as the job ads are the only consideration
in distinguishing between latent classes. The specific models of comparison for profile fit are
model 1 (equal variances and covariances fixed to zero), model 2 (varying variance and
covariances fixed to zero), and model 3 (equal variances and equal covariances). Each of these
models’ assumptions are tested when assessing profile fit to determine the number of profiles
and model with the best fit for the specific job ad dimension in consideration (Pastor et al.,
2007). The variation in models allows for a mix of both parsimonious, flexible, and stable
solutions.
In analyzing the latent profiles, the “tidyLPA” package uses maximum likelihood
estimate (MLE) to estimate the means, variance, and covariances of the observed variables
within each latent profile, or in this case, each job advertisement. MLE then finds the parameter
values that maximize the likelihood of those data under that specific model. The goal being to

identify the model and number of profiles that best represents the underlying structure of the data
using those estimation parameters while still maintaining a level of interpretability.
The best fit was determined by comparing fit indices across the estimated models, where
the lower values indicated the best model fit and a good balance between complexity and
interpretability. To capture these considerations, the BLRT (Bootstrap Likelihood Ratio Test)
and corresponding significance values were considered, along with the BIC (Bayesian
Information Criterion). BIC was assessed first to find the smallest value, indicating the model
and profile number with the best fit. Then the BLRT was assessed to determine that the model,
compared to other models fits significantly better than the alternatives. Additionally, BLRT has
been shown in simulations to predict correct model and profile fit above what BIC was able to
achieve (Nylund et al., 2007). BIC was also considered in determining model fit and number of
profiles due to the common practice of utilizing it as a fit index in organizational science and the
emphasis on both model complexity and sample size (Nylund et al., 2007; Spurk et al., 2020).
Because of the good performance of BIC and default use, it was considered along with the BLRT
fit statistic (Jedidi et al., 1997; Magidson & Vermunt, 2004; Roeder & Wasserman, 1997). While
both AIC and BIC were reported and both represent how well the model fits the data and
penalizes by the number of parameters in the model to prevent overfitting, BIC has a stronger
penalty for overfitting and that can lend to better performance in model fitting than AIC (Jedidi
et al., 1997; Roeder & Wasserman, 1997).
Running an LPA can create profiles of deception per dimension to better understand the
nature of different groups of individuals who may view a certain section of a job advertisement
as deceptive, while some feel it is authentic. However, LPA cannot tell us why those perceptions
are formed from the present job advertisement text. In order to better understand the reasoning

individuals, have for rating job advertisements as deceptive, a natural language processing (NLP)
topic modeling method was used.
Natural Language Processing Topic Analysis Overview. Although person-centered
approaches, like latent profile analysis, can highlight common patterns of perceptions across job
ads, the reasons why may be unclear. In following up the LPA with a text analysis approach,
both a more descriptive nature and reasoning can be provided for the deception found in different
profiles per dimension and what reasons are shared across dimensions (Research Question 3
and Research Questions 3a). By analyzing text quantitatively, further subgroups based on
varied reasons for rating text as deceptive can be discovered. That is, there may be a group of
respondents who tend to provide high deceptiveness ratings across all advertisements.
Qualitatively, this profile is labeled as “skeptics.” Despite their common perceptions, they may
have different reasons for those patterns. Thus, if asked to indicate why they found the text
deceptive, members within that profile might provide different reasons (e.g., disillusionment
from decades of experience, anti-capitalist views). Therefore, further exploring verbal
justifications for choices at the individual level can be informative.
A modern way to quantify vast amounts of information in the form of text, beyond what a
human could interpret and find main ideas within, is by using state-of-the art models called
“transformer” models. Transformer models utilize neural networks to encode both structural and
semantic information, as a means of combining the power of both textual information sources.
While this is a lot of information for processing, transformer models are fairly effective in
handling this volume of parallel computations, with a vector representation for structural text
information and another for semantic information (Yu et al., 2021). Due to recent advances in
computational power, transformer models utilize deep neural networks to allow for

improvements in computational efficiency (Vaswani et al., 2017). Figure 7 below depicts the
general architecture of a transformer model that has already been pre-trained and fine-tuned and
is given input text to generate an output text embedding and subsequent decipherable text or
classification prediction. Pre-trained models are provided a comprehensive sample of text based
on what is readily available online. So, pre-trained refers to the fact that these models have a
head start and already know English (or whatever language the text of interest is in). This large
corpus of text is already embedded and contained in the model’s “knowledge base” in order to
effectively understand general English terms (Meng et al., 2022; Sia et al., 2020). However,
sometimes specific use cases are better understood by the model if they are used to fine-tune the
transformer models. This is when a specific large amount of text input is additionally embedded
and the model is then trained on these embeddings to better understand specific use cases and
make better predictions within those cases.

Figure 7
Transformer Text Model Architecture

Note. This figure demonstrates an overview of how transformer models work. These models take
the context of words into account and give attention to each word in that context within a
sentence. This means the same words in a different order would have a different output
embedding. Therefore, both word embeddings and their position are weighted and transformed
into a higher-level input. This process is repeated until a final output embedding is produced.
The output can then be used to make predictions or classify off of sentence meaning.
When words are used as data for prediction in transformer models, they must first be
embedded. This means that words are represented as numeric values. These numerical
representations are done so through tokenization (Devlin et al., 2018). These vector
representations of the text are the inputs transformer models use to fine-tune the pre-trained
model to adapt to new datasets. A visualization of this process is shown in Figure 8 below.

Figure 8
Visualization of Word Embeddings

Note. This figure depicts how words can be embedded and represented as numeric vectors. Each
word has a vector embedding and at the sentence level, the average of the embeddings represents
the general meaning of the words together. Therefore, similar sentences in terms of meaning or
syntax, will have similar overall embeddings.
In order to understand the features (both text-based and others) an unsupervised method
of text analysis is used, where latent themes are found from a large corpus of text from their
embeddings (Finkelstein-Landau & Morin, 1999). Unsupervised methods work particularly well
when the text is unstructured or unlabeled in nature. In a sense, this form of topic modeling is a
form of dimension reduction applied to text, similar to factor analysis or principal component
analysis (Bikienga, 2018). While methods of topic analysis have been around for a while, more
modern approaches enable technological advances in machine learning to provide researchers
with more options and information.
Specifically, one such model is topic modeling using an open-source library of
transformers. This study uses a specific transformer from the Hugging Face library called “AllminiLM-L6v2” (2021). This specific model utilizes deep learning models that are pre-trained

and simply must be fine-tuned on the text data of interest (Grootendorst, 2022). Transformer
models contain many connected layers of pre-trained data. This pre-trained data comes from a
dense library of text data that the model has already been trained on. In this process, the model
then encodes these text data as dense vector representations or embeddings (Wang et al., 2021).
In order to fine-tune the transformer model, one simply uses a dataset of their own text data to
find the latent topic representations.
The specific topic analytic approach utilizes the “All-miniLM-L6v2” model. It not only
extracts relevant words for clusters to represent topics in the given data, but it also is more
efficient than older, non-pre-trained models (Grootendorst, 2022). This means that in order to
apply this method of topic modeling to new data, it does not require extensive computing power
or time to train the model. Another advantage of this open-source model is that it allows for a
variety of different topic modeling features including: relevant word scoring, topic visualization
options, similarity topic searches for new words, and hierarchical clustering (Angelov, 2020).
These options make topic modeling using pre-trained embeddings via a transformer model more
robust and flexible than previous approaches to topic modeling (Sia et al., 2020). A simplified
visual example of how topic modeling via transformer models functions is depicted in Figure 9
below.

Figure 9
Overview of Transformer Model Topic Discovery Process

Note. This figure demonstrates a simplified overview of how topic modeling with transformer
models reduces a large corpus of unorganized text from many documents into topics and
corresponding keywords. First, the transformer model takes uncategorized text from the input
documents and converts them to vector embeddings. The embeddings are then dimensionally
reduced and clustered into semantically similar topics in the next phase using two separate
algorithms built into the code. Next, topic representations are created by extracting keywords for
each cluster. Keywords are chosen based on the frequency of a word in a cluster, the frequency
of the word across all clusters, and the average number of words per cluster. The end result is a
list of topics or text-based dimensions of the input documents (Mehdi, 2021).
Natural Language Processing Topic Analysis Implementation. To gain insight into
the reasons participants provided for their deceptive ratings, the data set was split into deceptive
and authentic. Where, any text responses corresponding to a score higher than the midpoint of 4
on the Likert-type scale (“Slightly Deceptive”, “Deceptive”, and “Very Deceptive”), were
considered deceptive. Because this remaining single column of deceptive reasoning text is
unstructured in nature, the pre-trained transformer approach is particularly apt. This text data was
also made up of between about 200 to 400 phrases for each dimension, which is comparatively
small for typical NLP tasks. However, using pre-trained transformer models is a good way to
derive meaning from what is a large amount for humans but a small amount for less advanced
language models. That is, pre-trained transformers have a head start and already have some
comprehensive English embeddings and can still make good predictions when fine-tuned with a
smaller dataset, opposed to being trained from scratch with that small dataset (Devlin et al.,

2018). Using a pre-trained transformer model, a topic analysis was done on each of the 11
dimensions to identify reasons for highly deceptive ratings within profiles displaying highly
deceptive ratings.
Before generating embeddings for the text inputs, the data was “cleaned” using ChatGPT
(OpenAI, 2022). While there is no standard for how to clean text data, there is a common issue
that participants may not convey full ideas or just write a few disjointed words which do not
assist in discovering latent topics. Therefore, a modern and replicable approach was taken by
utilizing ChatGPT to clean text inputs. ChatGPT is a generative language model that is based on
the transformer architecture, in that it has already been trained on large amounts of text
embeddings. However, ChatGPT is particularly powerful, replicable, and appropriate for human
text input cleaning because of its construction using reinforcement learning based on human
feedback (Stiennon et al., 2020). This means that human AI trainers were used to respond to
actual prompt entries into OpenAI and based on these appropriate human responses, ChatGPT
was fine-tuned on these data. That specific model is called GPT-3.5 and is the version I utilized
for cleaning the text input. ChatGPT is also what is considered a large language model, that is, it
can easily handle a large amount of input text, while there are limits on output length, the phrases
used were run through the model one at a time (Ouyang et al., 2022). To get the text inputs of
deceptive reasoning into an interpretable statement for topic analysis, the prompt “The following
is a reason why a person found the job description (job dimensions were changed for each of the
11 dimensions) in a job advertisement deceptive, rewrite the reason to make it more succinct and
clearer, while keeping the overall meaning the same:” This prompt iterated through the provided
list of reasons for deceptive perceptions per dimension. Using a descriptive prompt like the one
used in Study 3 is found to be more effective in producing results closer to the goal depicted in

the prompt (OpenAI, 2022). Additionally, ChatGPT’s API allows for a hyperparameter
adjustment to the temperature of the model, which can be adjusted from 0 to 1. In setting this
hyperparameter to ensure low randomness and that the original meaning of the phrases input was
mostly the same but more comprehensible, it was set to 0.00001. A final step in cleaning the text
data was to remove stop words and punctuation before generating embeddings from the input
text (Figure 8). Several examples of the phrases produced from ChatGPT and the corresponding
original phrases, as well as the final cleaned text after removing stop words can be found in the
table below.
Results ChatGPT Text Cleaning of Phrases
Job Ad
Dimension

Original Text

ChatGPT Text

Final Cleaned Text

Job Description

They do not explain all the
lingo that they use, so I was
still confused about what
the job really entails.

The job description uses
unclear language, leaving
me unsure about the job
responsibilities.

Uses unclear language
leaving unsure about
responsibilities.

Salary

There is a very big
difference in the lower
range vs. the upper range
for the salary.

The salary range in the
job advertisement varies
greatly.

Range varies greatly.

Skills

Some skills they require
seem a little extreme.

The required skills are
too demanding.

Skills demanding.

Education

It is “preferred” that you
have a high school diploma
or equivalent.

The job ad is misleading
because it uses
“preferred” instead of
“required” for the
education.

Misleading uses
preferred instead of
required.

Once the text is encoded into embeddings that represent the latent meaning of all the
deceptive reasoning input text, the number of clusters that best fit the text data was calculated.
Specifically, a probabilistic approach using a Gaussian Mixture Model (GMM) was used to
cluster similar embeddings together to create an overall topic embedding. In applying GMM, the
embeddings are generated from a mixture of several Gaussian distributions, each representing a
cluster. The goal is to estimate the parameters of these distributions in order to find the best fit in
terms of number of clusters. In this case, the code utilizes an Expectation-Maximization (EM)
algorithm to estimate the parameters and the BIC was used to predict clusters and choose the
number that best estimates the model parameters (Sia et al., 2020). This means, a different
number of clusters could be the best solution for each job ad dimension. In running the GMM, it
was set to literature through 1 to 10 clusters for the solution. This was chosen to maintain a level
of parsimony and interpretability of the clusters (Burnham & Anderson, 2004; Domingos, 1999).
After iterating through 1-10 cluster solutions, a BIC plot of solutions was produced. In deciding
the number of clusters for the best fit solution, both the BIC and a visual approach was taken. If
there were BIC scores close, those solutions were assessed in a visual scatter plot to determine
the most parsimonious, interpretable, and generalizable solution (Molnar, 2020). These cluster
solutions were then used to initialize a GMM with the appropriate cluster number and fit that
GMM to the text embeddings, post ChatGPT. Finally, cluster labels are able to be predicted for
each data point. The cluster assignments for each data point or phrase can then be assessed to
derive meaning from those clusters
To retrieve interpretable topics from each cluster, several different methods were used to
gain unique insight from each method. First, a principal component analysis (PCA) was used to
reduce the dimensionality of the topic embeddings in their latent space to produce an

interpretable visualization of the clusters in a 2D graph (Sia et al., 2020). Therefore, the final
plotted data frame contained 2D embeddings, the cluster assignments, and the corresponding
texts in an interactive plot. A second, non-interactive plot was produced using representative text
found by finding the location of the data point whose Euclidean distance to the cluster’s mean
coordinate is the smallest. Additionally, ChatGPT was utilized again to provide understandable
summaries of all the text classified into each cluster. Because there are so many phrases per
cluster, it is difficult for humans to generate a summary that accounts for repeated instances and
weights them effectively in a summarized main idea. In this instance, the prompt “Write a
condensed and succinct summary sentence of the following list. Make the summary into a
concise, clear, and straightforward main idea:” was used to iterate through each cluster. This
produced a phrase or main idea statement per cluster as a means of deriving meaning from the
classified phrases. The most common words are found based on their counts in the frequency
distribution of each cluster. Their corresponding percentages of occurrence in the distribution are
also included in the analysis. As a final means of understanding the clusters, a representative
index was found for each cluster by computing the closest data point to the mean of the
embeddings in each cluster using the Euclidean distance between the data points and the mean of
the embeddings. In addition to the representative text, the number of phrases included in each
cluster was computed. This detailed understanding of the topics and reasons behind ratings of
perceived deception acts as an empirical way to inform the practice of job ad writing.

#### 3.3.6 Study 3 Results

The results of this study are categorized by job advertisement dimension, where the
reported findings of the LPA and topic analysis for each dimension are described. While each of
the 11 dimensions is a complex approach. It is comprehensive due to the exploratory nature of

this study. These 11 dimensions may lend to unique features continuing to deceive that would
not be shown in a larger scale overall perspective of the job advertisement as a whole.
Additionally, while there may be consistency in the finding between dimensions, that could not
be empirically supported prior to this intensive exploratory study. Considering all 11 dimensions
in an entire job advertisement also helps to direct the attention of the participants ratings the
deception level. That is, they can take the time to notice individual components within each
dimension of text that they may not focus on or pay attention to, while being asked about the job
advertisement as a whole. This method was also taken to reduce cognitive load. While the survey
was longer, participants were asked to only assess a small portion of a large body of text at once.
In doing, so this can lead to more detailed responses informing specific text contributing to
perceptions of deception within each dimension or section of the advertisement (Sweller, 1998).
Job Dimension 1: Job Description. The job description dimension refers to the overall
statement provided by the company that outlines the job being advertised, Indeed.com typically
labels this section as such.
Descriptive Statistics for Job Description. Means, standard deviations, and
intercorrelations of the 10 job advertisements for the job description dimension are in Appendix
C1, Table 3. Some general observations can be made from this data. First, there is a fair amount
of variance, based on the standard deviations among deception ratings for all job advertisements.
Additionally, the mean ratings of only one job advertisement, job ad 3, is above the mid-point of
the 7-point Likert type scale, indicating a deceptive perception for the job description. All the
remaining job ads were rated as either neutral or slightly authentic. There are also several
significant correlations (32 out of 45 total) amongst the job advertisement ratings. This indicates
that while job advertisements may show similar ratings, there are distinct advertisements rated as

clearly deceptive. Moreover, it is possible that common textual elements in job descriptions,
found in both deceptive and authentically perceived advertisements, may elicit comparable
reactions when they appear in correlated job advertisements. These correlations support the idea
that if a particular text feature or phrase in a job ad is considered deceptive by a specific profile,
and the job ad was correlated with to another on deceptive ratings, it allows for a well-informed
prediction of what text is perceived as deception: the text similar across both advertisements.
Latent Profile Analysis for Job Description. One goal of study 3 was to discover
distinct profiles of deceptive perceptions within the job description dimension. This was
explored by running an LPA on the ratings of deceptive for the job description for each of the 10
job advertisements. The latent profile analysis fit statistics for this dimension are in Appendix
C1, Table 4. There were convergence issues for the model 2, a 3-profile solution, potentially due
to small sample size and overfitting, non-convergence after 1,000 iterations, or lack of variation
based on the assumptions of the model. These solutions are reported but were not considered in
the solution for best fit.
To address Research Question 2a, there was the best fit with a 2-profile solution using
model 2 (varying means and equal variances). The fit statistics chosen as discussed above were
considered based mainly on the BIC value (4,243) being the lowest value for the 2-profile
solution using model 2 reported statistics. This profile additionally had a p-value of 0.01,
indicating a good fit above other model alternatives.
The size of each profile and means on the 10 different job advertisements can be found in
Appendix C1, Table 6. In regard to Research Question 2b, about 84.2% of the respondents were
assigned to the Profile 1 or the “Mildly Skeptical with Heightened Awareness” profile, which is
the strong majority of individuals. The smaller Profile 2, or the “Overly Trusting” profile

contained 15.8% of the sample. Naming each profile was done on an observational basis, but the
reported means on each job advertisement demonstrate their perspective differences in
perception of deception as it relates to job description for each advertisement. A visual
representation of each profile is depicted below in Figure 10.
Figure 10

Assessing the two profiles for job description perceive deception, addresses Research
Question 2c, which concerns the nature of each profile. Looking at Figure 10 and the mean
ratings corresponding to each profile, it is clear that Profile 2 remains trusting of most
advertisements, rating on average that they are mildly authentic. In contrast, the majority of the
participants, belonging to Profile 1, were much more concerned with the job descriptions being
deceptive in general, or at least uncertain, and had a heightened sense of deception in response to

the job description in job advertisement #3, that was not shown in the Profile 2 responses. This
specific job advertisement is that for a registered dietician, found in Appendix B1, titled
“Deceptively Rated Job Advertisement 3” and is available on OSF at the following link under
“Indeed Job Ads used in Study 3”: https://osf.io/xf9e6/files/osfstorage. In looking at the job
description for the registered dietician, it conveys very little about the job or company and
contains several creative or persuasively worded statements, which may seem less enticing and
more like trying to oversell to some individuals. This except for job ad 3’s job description is
found in Figure 11, below.
Figure 11
Job Description for Job Advertisement 3

Generalizability for Job Description. As a means of reassessing the low generalizability
in Study 2, the generalizability coefficient was computed again with the changed study design
and approach in Study 3. In this study, the total generalizability of G-coefficient was 0.792,
which was above the >0.7 standard as used in Study 2. While this is counter to the initial
conclusion of distinct perceptions based on the results of the generalizability computations from
Study 2, there may be artificial inflation due to study design. Specifically, the lack of sparse
matrices or lack of missingness in Study 3, compared to Study 2 due to effective attention
checks, could have decreased Study 2’s G-coefficient. The summary of variance components

along with the G-coefficient can be found in Appendix C1, Table 5. Of note is the proportion of
person variance compared to the source of Item variance. About 20.9% of the variance can be
explained by individual differences in rating the deceptiveness of the job advertisements,
compared to the 10% of variance explained by the difference between the job advertisements,
meaning there may be individual differences influencing ratings were left unexplored that
contribute to profiles besides perceived deception. That is, deception could be of a more complex
nature than initially thought. Additionally, about 69.1% of the variance comes from error, this
may indicate that there are factors contributing to profile membership that are unmeasured or
unaddressed. In looking at the two profiles of job description deception, they are fairly similar
despite the ratings of job ad 3, which could indicate intensity differences of very similar
perceptions being accurately reflected in the G-coefficient.
NLP Topic Modeling for Job Description. The other goal of study 3 was to further
investigate the nature of the formation of deceptive perceptions found in each separate job
dimension. This was done utilizing NLP as discussed above to perform topic modeling with each
set of text inputs corresponding to deceptive ratings. There was a sample size of n = 225
statements, indicating that 225 participants rated the job descriptions across the 10
advertisements as some level of deceptive. The pre-trained transformer model works well with
larger amounts of text that cannot be analyzed by humans alone. This method aims to address
Research Question 3.
The job description dimension had a cluster solution of best fit at n = 10 clusters of topics
representing the reasons or further details for the deception perceptions. This is based on the BIC
plot of the GMM fit to the embeddings of the job description dimension text (Figure 12). This

plot shows a clear drop in BIC when moving towards the 10-cluster solution, with no other
cluster models being relatively close.
Figure 12
BIC Plot for Job Description Cluster Solutions

To answer Research Question 3, the reasons people gave for their ratings were
summarized into a main idea per cluster using ChatGPT, these, along with representative words
and number of statements in each cluster can be found in Appendix C2, Table 7. This table
demonstrates that about 71 statements (Cluster 9) were made (1 for each participant) about the
job description being misleading due to a lack of important details. With this being the largest
cluster, it included components of the job advertisements that put more than the job description
in that section. Therefore, statements regarding the lack of details for the pay and requirements
are leading to deceptive perceptions as well. Additionally, statements in those clusters indicated
that the job seems “too good to be true” based on the top words table found in Appendix C2,
Table 8. The second most populated cluster (Cluster 6) has 48 statements that feel the deceptive
nature of the ad comes from being unclear; again on several different components of the job that
seemed to be listed in the job description section as well as other parts of the job advertisement.

Utilizing the PCA done on the clusters, an interactive plot of the clusters can be found at
the following webpage:
https://computationalorganizationalresearch.com/software/jobaddeception/job_description_plot.h
tml. This plot enables you to scroll over data points in the clusters and find relevant text inputs
that contribute to the overall meaning of each cluster. A simplified static version of this plot can
be found in Figure 13 below. This shows main concepts from each cluster within the plot, as
opposed to the specific statements in the interactive plot. When looking at the two main clusters
(Cluster 6 and Cluster 9) and the dimension that splits them. It seems that there is a dimension
represented in the 2D space corresponding to a continuum of vague or unclear to misleading or
too good to be true based on the information that was included. This implies that there is a
middle ground where job descriptions contain enough information but do not try to over sell the
position.
Figure 13
Clusters for the Job Description Dimension

Job Dimension 2: Company Overview. The next dimension of interest is the company
overview, which refers to the section provided for companies to input information that represents
values or provides prospective employees with more information. While this section is not
present in all included job advertisements, it is labeled as such when companies fill it in for a job
posting. However, it is possible that the lack of information, based on what was discovered in the
job description dimension, could contribute to perceptions of deception.
Descriptive Statistics for Company Overview. Means, standard deviations, and
intercorrelations of the 10 job ads for the company overview dimension can be found in
Appendix D1, Table 9. A few aspects of note are present in this information. Again, there are a
large number of significant correlations, more than most dimensions measured (38 out of 45
total). This may be potentially due to the fact that not all the job ads had a company overview,
which could still be viewed as deceptive, but that lack of information would probably be viewed
similarly for all advertisements that also did not include that section, due to the lack of variability
possible in the text. There are again high standard deviations, that demonstrate a fair amount of
variance across all job advertisements’ company overviews being rated. Finally, there are means
that demonstrate instances of perceived deception for several job advertisements. That is, several
means are above the midpoint of 3 and indicate slight deceptive perceptions. The distribution
from Study 1, showed that deceptions of both authenticity and deception were distributed
normally, in that there were less extremes, it is still noteworthy however, that people are fairly
suspicious of deception for many of the advertisements included in the study.
Latent Profile Analysis for Company Overview. Study 3 aimed to identify unique
patterns of deception within the company overview dimension. This was achieved by conducting
a latent profile analysis on the deception ratings of the company overview for the same 10 job

advertisements. The fit statistics for the LPA can be found in Appendix D1, Table 10. There was
another convergence issue for the 3-profile solution in model 2, again from the same sample size
being used and introducing similar problems with the sample size and the model’s assumptions
potentially leading to lack of convergence after the set of 1,000 iterations. This solution was not
considered, but was reported.
Research Question 2a was addressed by finding an optimal solution of model and
profile fit with a 2-profile solution using model 2. With the same standards for fit indices, using
the BIC and BLRT significance, the BIC for the chosen solution was the lowest at 4,289 with a
significant BLRT value of p = 0.010.
The distribution of participants across the two profiles and their respective means for the
10 job advertisements are presented in Appendix D1, Table 12. Concerning Research Question
2b, approximately 58.8% of the respondents belonged to Profile 1, labeled “Neutral but Aware
of Deception”, which constituted a slight majority of the participants. The smaller Profile 2,
termed the “Trusting but Occasionally Suspicious” profile, accounted for the remaining 41.2% of
the sample. These profile names were determined by observations and the reported means for
each job advertisement. Figure 14 provides a visual representation of each profile.

Figure 14

Evaluating these two profiles related to company overview, pertains to Research
Question 2c. Upon examination of Figure 13 and the mean ratings associated with each profile,
it can be interpreted that both profiles share a similar pattern of perceptions, but differ slightly in
the intensity of that perception of deception. Both profiles have instances across the job
advertisements that demonstrate there are perceptions of deception, however Profile 1 displays
those instances more intensely via higher ratings on mostly the same job advertisements in
respect to company overview. These specific advertisements are job ad number 3 for the
registered dietician and job ad number 9 for a retail sales associate. These both can be viewed in
their entirety in Appendix B1 and can be accessed via the following OSF link:
https://osf.io/xf9e6/files/osfstorage.
In respect to the company overview in job ad number 3, there is no specific labeled
company overview section but there is a section that discusses why the company feels they are
worthwhile to work for. This is shown below in Figure 15. This overview contains very

descriptive and detailed information which may be viewed as a positive. However, both profiles
felt that the information was conveyed in a deceptive manner.
Figure 15
Company Overview for Job Advertisement 3

Additionally, job ad #9 was viewed as mildly deceptive in regards to the company
overview. There again is not a specific section labeled “company overview” but there is a brief
description of the company included and it says: “Our Growing Company is seeking experience,
results-driven retail sales associates to join our Virginia Furniture Market team at our
Christiansburg Showroom.” This potentially can be perceived as deceptive based on the way it is
conveyed or certain assumptions about the company’s employees that may not feel true from the
statement.

Generalizability for Company Overview. In Study 3, the generalizability coefficient was
recalculated to assess the low generalizability of Study 2, for every dimension. This resulted in a
G-coefficient of 0.734, which actually meets the > 0.7 standard. This finding again contradicts
the initial conclusion of distinct perceptions from Study 2, which may be due to the small sample
size and unmeasured variance.
The summary of variance components along with the G-coefficient can be found in
Appendix C1, Table 5. Of note is the proportion of Person variance compared to the source of
Item variance. About 20.9% of the variance can be explained by individual differences between
people, compared to the 10% of variance explained by the difference between job
advertisements, meaning there may be individual differences left unexplored that contribute to
profiles besides deception ratings. Additionally, about 69.1% of the variance comes from error,
this may indicate that there are factors contributing to profile membership that are unmeasured.
These profiles also mirror each other closely with slight intensity differences in deception
ratings, indicating that there may be consistency within perception based on the redesigned study
3’s G-coefficient.
NLP Topic Modeling for Company Overview. In further understanding the nature of the
deception ratings at an individual level, each person’s input text was analyzed and assigned to
representative clustered using a NLP topic modeling approach. This aims to address Research
Question 3.
For the company overview dimension, there was a sample size of n = 256 statements,
indicating that 256 participants rated the job descriptions across the 10 advertisements at some
level of deceptiveness. The company overview cluster solution had a best fit at n = 7 clusters.
This is based on the BIC plot shown in Figure 16. While there is a clear second drop in solution

fit for 10 clusters, a 7-cluster solution was chosen based on the minor contribution of 3 additional
clusters in lowering the BIC and minor contribution in interpretable additional clusters.
Figure 16
BIC Plot for Company Overview Cluster Solutions

In regards to Research Question 3, the reasons people gave for their ratings were
summarized into a main idea per cluster using ChatGPT, these, along with representative words
and number of statements in each cluster can be found in Appendix D2, Table 13. There are
some shared themes found in certain clusters, compared to all other dimensions (Clusters 1 and
2). These are themes of information being misleading or unclear, leading to confusion and
deception. However, there are many more statements in Cluster 7 (75) that have a unique
reasoning based on the use of biased language, overly positive statements, and the overuse of
exclamation points. While these techniques may be positive for marketing certain products, it
does not seem to be perceived well in the context of conveying information about the company
posting a job opening. It may seem like a conceited way to oversell something that is not as truly
positive as it is represented.

In assessing the top words for Cluster 7, the words “biased” and “suspicious” come up as
representing 8% and 6% of the frequency distribution of words (Appendix D2, Table 14). These
indicate that there may be words in the highly rated as deceptive job ad number 3 feel biased or
suspicious. Specifically, statements in that ad like: “translate extra time into money” and “the
busy profession”, make assumptions about those potentially interested in the position that may
not be true.
The interactive plot of statements in each cluster in a 2D space, can be found at the
following webpage:
https://computationalorganizationalresearch.com/software/jobaddeception/overview_plot.html.
This plot can assist in finding relevant dimensions that the PCA may have reduced the
embeddings into, demonstrating a core underlying feature that the clusters differ on. In this case,
it seems that spanning between Clusters 7 and 3, there is a latent space that represents the
continuum of the company description containing information that is overly positive, suspicious,
biased, or seemingly fake to no company details or information. Where either extreme seems
deceptive. A non-interactive plot is shown below in Figure 17.

Figure 17
Clusters for the Company Overview Dimension

Job Dimension 3: Salary. The dimension of salary is especially important as recently
and times post-COVID, companies frequently experience employees leaving due to low or noncompetitive pay (Cajner et al., 2020). It is especially important in today’s climate to present to
employees a salary that they feel is depicted truthfully and is fair in order for them to even apply
or respond to a job posting.
Descriptive Statistics for Salary. The descriptive statistics for the 10 job advertisements
and their ratings of deception for the salary dimensions are found in Appendix E1, Table 15. The
significant correlations between job advertisements represent those salary sections that were
rated similarly in terms of perceived deceptiveness or misleadingness. Many companies report
their salaries or pay provided to entire employees to apply so with a diverse sample of jobs, it

can be assumed that different salary amounts can be pierced deceptively for a potential additional
reason(s). There are two ads of note (Ad number 1 and Ad number 3) that have ratings higher
than the midpoint, indicating that they are perceived as somewhat deceptive. Again, there are
high standard deviations, depicting a fair amount of variation in those deceptive ratings, even
though participants are all directed to assess the same salary information per advertisement.
Latent Profile Analysis for Salary. In part, Study 3 aimed to uncover distinct deception
patterns within the salary dimension by conducting a latent profile analysis on the deception
ratings of the same 10 job advertisements. The LPA fit statistics are available in Appendix E1,
Table 16. Similar convergence issues arose from the 3-profile solution in model 2, this solution
was not considered, but is included in the fit statistics table. Research Question 2a was
addressed by selecting an optimal 2-profile solution using model 2, which demonstrated the best
fit indices, including the BIC (4,274) and a significant BLRT value of p = 0.010.
The distribution of participants across the two profiles and their respective means for the
10 job advertisements can be found in Appendix E1, Table 18. In relation to Research Question
2b, about 77.2% of the sample fall into profile 1 or the “Wary and Alert” profile and the smaller
profile of “Generally Trusting” contains 22.8% of the respondents. Based on the latent profile
plot in Figure 18, both profiles follow similar patterns of deception across the advertisements,
however, the generally more skeptical profile (1) with higher ratings of deception found
advertisements 1 and 3 fairly deceptive. Profile 2 only had similar heightened levels of deception
perceptions with the advertisement 1.

Figure 18

These advertisements can be found in Appendix B1 and are available on the OSF website listed
in prior sections of this paper. When looking at the pay or salary sections of these jobs, some
details can be noted. Specifically, for job advertisement number 1 (Mixologist) the listed salary
is $29,455 - $71,495 a year. The salary for the advertisement number 3 (Registered Dietician) is
$45 - $120 an hour. Both of these are large ranges and may lead to feelings of deception. These
both can be viewed in their entirety in Appendix B1 and can be accessed via the following OSF
link: https://osf.io/xf9e6/files/osfstorage.
Generalizability for Salary. To reassess the low generalizability found in Study 2, the
generalizability coefficient was recalculated for the modified study design and approach used in
Study 3. In this study, the total G-coefficient reached 0.838, surpassing the >0.7 standard applied
in Study 2. These results broken down by variance components can be found in Appendix E1,

Table 17. Contrary to the initial conclusion of unique perceptions based on Study 2’s
generalizability computations, this increase could be due to similar profiles as to how salary is
viewed. There are some differences in intensity and spikes of deception ratings for Profile 1,
while Profile 2 remains trusting or indecisive, that could be due to additional unmeasured factors
or irrelevant ads that do not capture profile differences appropriately. This assumption is based
on the high variance estimate attributable to the residual of 66.3%. This can also limit the
generalizability of the study to future job advertisements.
NLP Topic Modeling for Salary. Study 3 also aimed to assess the individual level
deception perceptions for each participant’s ratings in a way that derives meaning from the large
amount of text responses. Using NLP topic modeling via pre-trained transformers allows for this
deeper dive into the reasoning for participants’ ratings. This approach aims to address Research
Question 3.
For the salary information, there was a sample size of n = 259 statements, indicating that
259 participants rated the job descriptions across the 10 advertisements as some level of
deceptiveness. The salary dimension had an optimal cluster solution of n = 5, representing the
topics corresponding to the reasons or finer details of deception perceptions. This is based on the
BIC plot of the GMM fit to the embeddings of the salary dimension text (Figure 19). The plot
shows a drop in the BIC at a solution of 5, which a subsequent increase and drop again at a
solution of 8. While the 8-cluster solution has a slightly lower BIC compared to the 5-cluster
solution, the 8-cluster solution was not chosen due to the smaller cluster sizes not showing very
representative additional topics when assessed. Also 5-clusters is a more replicable and
interpretable solution for understanding how to avoid deceptive features eliciting the
corresponding ratings during job ad construction.

Figure 19
BIC Plot for Salary Cluster Solutions

To answer Research Question 3, the reasons participants provided for their ratings were
condensed into a primary idea for each cluster utilizing ChatGPT. These main ideas, along with
representative words and the number of statements in each cluster, can be found in Appendix E2,
Table 19. This table shows that 2 clusters share the bulk of the statements (Cluster 4 and 5).
Cluster 4 (containing 93 statements) is summarized to depict that the information included is
potentially fraudulent, with payment details remaining unclear due to unrealistic salary ranges or
deceptive statements about bonuses, leading to confusion. Cluster 5 (containing 60 statements) is
summarized by highlighting the broad range in salary being unclear and leading to deception or
disappointment. Additionally, there are unexplained factors as to why there is a range or if it
depends on experience or not, like may be typical in certain positions. Both the job
advertisements (1 and 3) rated as most deceptive in the LPA had broad salary ranges that were
left unaddressed in the subsequent job advertisement information. While one was for salary and
one was for hourly pay, the large range was viewed negatively regardless. The further
breakdown of top words per cluster can be found in Appendix E2, Table 20.

An interactive plot of the clusters was produced and can be accessed at the following
webpage:
https://computationalorganizationalresearch.com/software/jobaddeception/salary_plot.html. This
plot depicts the text and their corresponding clusters. A static version of the plot can be found
below in Figure 20, that shows the relevant text inputs that contribute to the overall meaning of
each cluster based on the closest Euclidean distance to the mean of the cluster. When viewing the
largest distances between clusters (from Cluster 1 to Cluster 5 and Cluster 3 to Cluster 4) you
can form an understanding of what dimensions may be represented in the 2D space, as relevant
for distinction between clusters. Specifically, the latent space from Cluster 1 to Cluster 5, there is
a continuum from Cluster 1, representing a lack of information or unclear information to Cluster
5, where the information included was a range that was too broad to be clear. From Cluster 3 to
Cluster 4, there is a dimension of the actual amount of pay seeming deceptive. The text in
Cluster 3, mentions instances of the pay seeming too high or the compensation structure
appearing unusual that leads to deception. Cluster 4, however, contains instances of participants
reporting that the pay included was too low and seemed suspicious or desperate and that felt
deceptive. For example, it may seem suspicious that even though the pay is stated for the HR
position in job advertisement 4, it contains a broad range as well as includes a competitive
performance-based incentive structure, which may be confusing or unclear in regards to that
specific position.

Figure 20
Clusters for the Salary Dimension

Job Dimension 4: Benefits. The dimension of benefits is typically stated on Indeed.com
job advertisements and a specific section is provided for it. This section is particularly important
because it may be used as a means for organizations to gain a competitive advantage (Bradley et
al., 2008). This could easily lead to slight inflations in the depiction of available benefits in a job
posting.
Descriptive Statistics for Benefits. The means, standard deviations, and intercorrelations
of the 10 job ads for the benefits dimension can be found in Appendix F1, Table 21. Several
notable aspects are evident in these data. Firstly, there is again, a high number of significant
correlations between job advertisements, which may indicate that there is not enough variety in

the benefits sections of job advertisements chosen. It could also be that many companies tend to
post similar benefits in job advertisements in terms of authenticity, regardless of the position
advertising for. While several means are around the midpoint, there are a few that indicate slight
deception or uncertainty that represents the Gasuain distribution of perceived deception from
Study 1. The also was high standard deviations across all job advertisements, indicating that
there was high variance from those reported means, indicating that individual participants could
be rating benefits as extremely authentic or extremely deceptive.
Latent Profile Analysis for Benefits. Study 3 aimed to uncover distinctive deception
patterns within the included benefits of the job advertisement. The LPA fit statistics can be found
in Appendix F1, Table 22. Once again, there was a convergence issue for the 3-profile solution
in model 2, stemming from a convergence issue in model fit. Therefore, this solution is reported
but not considered in the final best fit solution.
Research Question 2a was addressed by identifying an optimal model and profile fit
using a 2-profile solution with model 2. Maintaining the same standards for fit indices, such as
BIC and BLRT significance, the chosen solution has the lowest BIC at 4,319, with a significant
BLRT value of p = 0.01.
Appendix F1, Table 24 presents the distribution of participants across the two profiles
and their respective means for the 10 job advertisements. Regarding Research Question 2b,
approximately 43.0% of the participants belonged to Profile 1, labeled “Slightly Skeptical”.
While the slight majority of participants at 57.0% belonged to the “Fluctuating Deception”
profile (2). Figure 21 shows the latent profile plot for the salary dimension based on the mean
rating of each profile for each of the 10 job advertisements.

Figure 21

Examining the two profiles for salary addresses Research Question 2c, which focuses on
the nature of each profile. A review of Figure 21 and the mean ratings of each profile, reveals
that Profile 1 is much more consistent with their ratings of deception. Additionally, there are not
very consistent patterns shared between the two profiles, but there are shared high ratings of
deception for the same advertisements. The profiles just seem to fluctuate between those similar
ratings to different extents. That is, Profile 1 is much more consistent with their ratings compared
to Profile 2. The specific job advertisements that shared similar high deceptive ratings across
profiles were job advertisements 3, again, 6 and 8. These can be found in Appendix B1, or at the
same OSF link: https://osf.io/xf9e6/files/osfstorage.
The only benefit listed in the section for job advertisement 3 is a flexible schedule, while
the other two advertisements have no distinctive benefits section. This could indicate that not

including the information is seen as deceptive or misleading. Many companies may maintain the
practice of waiting until the selection or hiring process to describe the benefits, however, that
may not be best practice if applicants do not even apply due to feeling misled by the lack of
listed benefits in a job advertisement.
Generalizability for Benefits. In Study 3, the generalizability coefficient was recalculated
due to the low generalizability of Study 2. This resulted in a G-coefficient of 0.854, which is
above the >0.7 standard. This can be found in Appendix F1, Table 23. The plot for the benefits
dimension contains a fair amount of fluctuation for one dimension over the other. This may
suggest that there is a fair amount of consistent across profiles, as seen by the overlap in the
profiles for ads 6 and 8. Again, there is a large portion of residual variance contributing to the
overall G-coefficient.
NLP Topic Modeling for Benefits. To gain additional insight into the nature of deception
ratings at an individual level, each participant’s input text was analyzed and assigned to
representative clusters using the same topic modeling approach. This addresses Research
Question 3.
For the benefits section, there was a sample size of n = 205 statements, indicating that
205 participants rated the job descriptions across the 10 advertisements as a form of deception or
feeling misled. The benefits dimension had a cluster solution that demonstrated the best fit at n =
8. This selection is based on the BIC plot depicted in Figure 22. Although there is a clear
secondary drop in solution fit for 10 clusters, an 8-cluster solution was chosen due to the similar
BIC scores and the goal of optimizing the solution to be more generalizable and understandable.
Additionally, more clusters would lead to smaller counts of phrases per cluster. With the smaller

sample size of text, that may lead to a solution that is overfitting to the specific data for the
chosen advertisements in the study.
Figure 22
BIC Plot for Benefits Cluster Solutions

In order to address Research Question 3, the reasons participants provided for their
ratings were condensed into a primary idea for each cluster using ChatGPT. These main ideas,
along with representative words and the number of statements in each cluster, can be found in
Appendix F2, Table 25. The most amount of statements per cluster can be found in Cluster 2,
where 82 statements indicate that the company did offer good benefits such as flexible
scheduling and unlimited paid time off, but these benefits were lacking in important information,
making them seem deceptive. Of additional note, is that many of the 39 phrases in Cluster 1,
found the ratio of details on COVID policies to details on actual benefits deceiving or
misleading. That lack of clarity in benefits, but an over descriptive section of policies that maybe
are more relevant during the selection process, lends to misleading or unclear feelings.
Additionally, this demonstrates that it may matter what information is detailed and not just the

fact that there are details in the job description.
The top words per cluster table found in Appendix F2, Table 26, shows that there are
consistent themes shared with the other dimensions that inclined top contributing words such as:
“misleading”, “unclear”, and “vague”. This table also shows that in Cluster 5, while there were
only 15 phrases, many of them focused on the term “uniform allowance” (a total of 56.6%
contribution to the top 10 words). This term was not defined or specified in the job advertisement
and left participants feeling confused and like they may misinterpret the ad.
A plot of clusters with interactive labels can be accessed at the following link:
https://computationalorganizationalresearch.com/software/jobaddeception/benefits_plot.html.
This plot shows the text for each data point and what cluster it belongs to. A static version of this
plot is shown below in Figure 23. There is potentially an identifiable dimension that is
represented as a continuum between the space spanning several clusters. This dimension could
potentially be interpreted as unclear information to clear information. Specifically, this appears
between Clusters 1 and 2. An additional dimension condensed into the space between Clusters 4
and 7 covers benefits that are being oversold or inclusive of things that are not benefits to
including benefits that are mismatched with other information in the job advertisement. For
example, job advertisement 2 has benefits listed like: “free lunch Every Friday, Complimentary
DoorDash DashPass and Headspace subscription!, and Annual holiday parties, Teammate
Appreciation Week, team meetings and happy hours! While these are found explicitly under the
benefits section they are not what many people think of when they think of benefits and may
seem misleading or have an alternative motive. This theme is also depicted in Cluster 2’s
interactive plot, where individuals note that these things are listed instead of the usual insurance
details or it seems “too good to be true”.

Figure 23
Clusters for the Benefits Dimension

Job Dimension 5: Responsibilities. Job responsibilities depicted in a job advertisement
can be a big factor to an employee’s self-selection process (Saks et al., 2006). In other words, an
employee may decide they are under or over qualified for a position based on the listed
responsibilities and skip the application process. If responsibilities are not listed in a manner
where the employee feels that it is reliable or truthful information, they would probably decide to
not use that information and opt to apply for a position in another job posting.
Descriptive Statistics for Responsibilities. The means, standard deviations, and
intercorrelations of the 10 job ads for the responsibilities can be found in Appendix G1, Table
27. The means for the responsibilities dimension are lower than most of the other dimensions
with only job advertisement 3 having a mean rating above the uncertainty midpoint and has

ratings of slight deception. However, there are high standard deviations, meaning that the means
do not fully represent how everyone rated each advertisement. There are many high correlations
in the table, similar to the other dimensions. This consistency in correlated ratings across job
advertisements on many dimensions may mean that the job advertisements chosen did not have
enough different information or were too similar on some dimensions for participants to form
distinct attitudes.
Latent Profile Analysis for Responsibilities. Study 3 aimed to identify unique patterns
of deception within the company overview dimension. This goal was accomplished by
performing a latent profile analysis on the deception ratings of the company overview for the
same 10 job advertisements. The LPA fit statistics can be found in Appendix G1, Table 28. A
convergence issue occurred for the 3-profile and 2-profile solution in model 2, which was again
due to the same sample size being used, potentially leading to lack of convergence after the set of
1,000 iterations because of conflicts between the sample size and the model's assumptions. It
could also be due to the higher correlations in the responsibility section ratings between job
advertisements. These solutions were not considered, but were reported.
Research Question 2a was addressed by identifying the optimal model and profile fit
with a 2-profile solution using model 1. Following the same criteria for fit indices, such as the
BIC and BLRT significance, the chosen solution had the lowest BIC at 4,134 and a significant
BLRT value of p = 0.010.
Appendix G1, Table 30 displays the distribution of participants across the two profiles
and their respective means for the 10 job advertisements. In relation to Research Question 2b,
around only 13.2% of the participants were part of Profile 1, named "Wavering Deception".
Meanwhile, the large majority of participants, at 86.8%, belonged to Profile 2, the "Trusting but

Aware" profile. Figure 24 presents the latent profile plot for the benefits dimension based on the
mean rating of each profile for each of the 10 job advertisements.
Figure 24

Research Question 2c focuses on the nature of each profile. A closer examination of
Figure 24 and the mean ratings of each profile reveals that Profile 1 and Profile 2 share similar
patterns of ratings with different levels of intensity and slight variations in the amplitude of the
graphed line across advertisements, meaning there are is more variety in their ratings than those
in Profile 2. The job advertisement that received similar high deceptive ratings across profiles
was #3. Additionally, job ad number 4 was rated highly in only Profile 1. These job
advertisements are in Appendix B1 or at the OSF link: https://osf.io/xf9e6/files/osfstorage.
Job advertisement 3 for the Registered Dietician contains almost no description of
responsibilities besides stating a section called your role, which says: “As a member of our

counseling team, you will provide counseling services to users who need help or advice in your
area of expertise.” While there is a statement provided, it is vague and does not seem to match
the job title. As for job ad 4, for the HRIS Analyst, there is a thorough description of
responsibilities that shows a difference in perceptions, as only one profile rated that job ad as
deceptive. The responsibilities for job ad 4 can be found in Figure 25 below.
Figure 25
Responsibilities for Job Advertisement 4

Generalizability for Responsibilities. In Study 3, the generalizability coefficient was
recalculated due to Study 2's low generalizability. This yielded a G-coefficient of 0.803, which
falls above the >0.7 standard and can be found in Appendix G1, Table 29. This provides fair
generalizability evidence for shared perceptions of deception. This can be seen in the LPA plot
due to the similar trends in responses between the profiles with slight variations.

NLP Topic Modeling for Responsibilities. To gain further insight into deception ratings
at the individual level, participants' input text was analyzed and assigned to representative
clusters using the same topic modeling approach, addressing Research Question 3.
For the responsibilities dimension, there was a sample size of n = 205 statements,
indicating that 205 participants rated the job descriptions across the 10 advertisements as some
level of deceptiveness. The responsibility dimension had a cluster solution with the best fit at n =
4, based on the BIC plot shown in Figure 26. This solution was chosen due to the clear drop in
BIC from a cluster solution of 3 to a cluster solution of 4. Additionally, the subsequent cluster
solutions tested did not show improvement over 4, the closest solutions matched the 4-cluster
solution.
Figure 26
BIC Plot for Responsibilities Cluster Solutions

With respect to Research Question 3, participants’ reasons for their ratings were
summarized into a main idea for each cluster using ChatGPT. Appendix G2, Table 31 presents
the representative words and the number of statements in each cluster. Certain clusters, such as

Cluster 3 and Cluster 4 share the bulk of the phrases, with 83 and 63, respectively. Cluster 3
describes that there are responsibilities listed but they seem excessive for the position or
understated, causing a mismatch between what the applicant feels may be required for the
position and what is asked. Cluster 4 reflects the common theme of the information being lacking
or unclear. Additionally, Cluster 1 contains only 14 phrases but they all focus on the
misrepresentation of the dietician position that is actually described more as a counseling or
therapy position.
Upon examining the top words for Cluster 1 and Cluster 3 (Appendix G2, Table 32),
there are specific positions that people found misleading. Specifically, Cluster 1 mentioned
“therapy” and “counselor” both over 10% of the time compared to overall word count. Cluster 3,
mentioned the mixologist position 4.7% of the time within that cluster.
An interactive plot of the statements in each cluster within a 2D space can be found at the
following webpage:
https://computationalorganizationalresearch.com/software/jobaddeception/responsibilities_plot.h
tml.
This plot can help identify relevant dimensions that the PCA might have reduced the embeddings
into, revealing a core underlying feature that distinguishes the clusters. In this case, it appears
that a latent space between Cluster 4 and Cluster 3 that shows a continuum from the listed
responsibilities being too expensive for the position or lacking for the position. Both of these
situations require some prior knowledge of the position to recognize, so for higher-level
positions where applicants are experienced, this could be an issue when responsibilities are
misrepresented. Additionally, these jobs may have more at stake in getting applicants or have

more to lose if the applicant realizes the job is not what they thought. A static plot is shown
below in Figure 27.
Figure 27
Clusters for the Responsibilities Dimension

Job Dimension 6: Skills. The skills dimension is separately listed on many Indeed.com
ads and is provided as an input for the company to list skills they expect the applicant to possess
when applying. This is important for employees to be able to know if they are able to do the job
advertised.
Descriptive Statistics for Skills. The descriptive statistics for the 10 job advertisements
and their ratings of deception for the salary dimensions are found in Appendix H1, Table 33. The
significant correlations between job advertisements are higher than many of the other

dimensions, ranging mostly within 0.3 and 0.4. This may mean that many job ads have similarly
viewed skills sections in terms of their levels of deceptiveness. Probably, these job
advertisements could lack variability in their skills sections leading to similar perceptions. This is
potentially the case due to the means ranging mostly around the midpoint of an uncertain rating.
There is a fair amount of standard deviation amongst the deception ratings for the skills
dimension.
Latent Profile Analysis for Skills. Study 3 partially aimed to uncover unique deception
patterns within the skills dimension by conducting a latent profile analysis on the deception
ratings of the same 10 job advertisements. LPA fit statistics can be found in Appendix H1, Table
34. Research Question 2a was addressed by choosing an optimal 3-profile solution using model
2, which showed the best fit indices, including the BIC (4,241) and a significant BLRT value of
p = 0.010.
Appendix HI, Table 36 presents the distribution of participants across the three profiles
and their respective means for the 10 job advertisements. Regarding Research Question 2b, the
profiles were fairly evenly representative of the sample. Profile 1, named “Mostly Trusting” had
about 26.3% of the sample. Profile 2, named “Generally Trusting but Slightly Uncertain” had
about 30.7% of the sample. Profile 3, named “Trusting but Slightly Skeptical” had 43.0% of the
sample. These profiles share very similar trends in their means for each job advertisement rating,
in that they are consistent in what they rate as deceptive, but there are not very high ratings of
deception.

Figure 28

Job advertisements 2, 3, 7, 8, and 9 are all rated at near 4, indicating that they are viewed
as slightly deceptive in how the skills are depicted in the job advertisement. Job advertisement 2
for an Early Intervention Specialist (Figure 29) prioritizes passion over skills and focuses a lot on
a valid driver's license, as well as creatively names the section as, “what you will bring:” all of
this combined may be confusing to applicants. Job advertisement 3, seems to lack mentioning
any skills for a registered dietician, which seems like it should require some level of skills.
Additionally, job ads 7, 8, and 9 vary in their required skills for the different positions but seem
to fail to list skills for any of them. Therefore, the failure to list skills could be viewed as
deceptive, especially for those within the Profile 2.
These ads can be viewed in their entirety in Appendix B1 and can be accessed via the following
OSF link: https://osf.io/xf9e6/files/osfstorage.

Figure 29
Skills for Job Advertisement 2

Generalizability for Skills. In Study 3, the generalizability coefficient was recalculated
for every dimension to address the low generalizability found in Study 2. This resulted in a Gcoefficient of 0.813, which meets the > 0.7 standard. This finding contradicts the initial
conclusion of distinct perceptions from Study 2, which may be due to the small sample size and
unmeasured variance.
The summary of variance components, along with the G-coefficient, can be found in
Appendix H1, Table 35. Notably, about 68.1% of the variance comes from error, indicating that
unmeasured factors may be contributing to profile membership. These profiles closely mirror
each other with minor intensity differences in deception ratings, suggesting that there may be
consistency within perception based on Study 3's redesigned G-coefficient. There is also a
limited range of fluctuation within the profiles, due to the fairly low means of deception ratings
for each job advertisement in the skills dimension.
NLP Topic Modeling for Skills. To further understand the nature of deception ratings at
an individual level, each person's input text was analyzed and assigned to representative clusters
using an NLP topic modeling approach. This addresses Research Question 3.
For the skills dimension, there was a sample size of n = 266 statements, indicating that
266 participants rated the job descriptions across the 10 advertisements as deceptive. The
company skills cluster solution demonstrated the best fit at n = 7 clusters. This choice is based on

the BIC plot shown in Figure 30. Although there are slightly worse solutions around the 7-cluster
solution. There is convergence and a relatively large drop in the BIC for the 7 clusters.
Figure 30
BIC Plot for Skills Cluster Solutions

Addressing Research Question 3, the reasons people provided for their deception ratings
were summarized into a main idea per cluster using ChatGPT. Details about these clusters,
including representative words and the number of statements in each cluster, can be found in
Appendix H2, Table 37. Cluster 4 has the most phrases at 89, which is 36 more than the second
largest cluster of Cluster 1. Cluster 1 depicts similar themes found throughout the other
dimensions of unclear information on the certain dimension, leading to confusion or misleading
perception. However, Cluster 4 includes phrases that lend to the summary picking up on themes
of unnecessary qualifications seeming misleading, as well as indicating that what is listed is
unclear or infers that the applicant understands the skills, this could even be for some of the entry
level positions such as the retail sales associate in job advertisement 9, where some individuals
who have not worked in retail, may not know the skills but still be qualified.

Examining the top words for each cluster, mirrors the themes found from ChatGPT in
running through each of the phrases per cluster. However, Table 38 in Appendix H2, shows that
there are some prominent words of note in Cluster 6. Specifically, the top word count is
“registered” at 16.7% of the total words for that cluster. This may mean that positions that are
listed as needing a registered person, are not depicting that in a clear manner. Cluster 6 again has
lots of instances of the word dietician including, potentially meaning that the position is not
depicting the skills required for that position adequately. Job advertisement 3 is listed as a
“registered dietician” but fails to mention any skills besides being registered.
The interactive plot of clusters with corresponding text per data point is at the following
website:
https://computationalorganizationalresearch.com/software/jobaddeception/skills_plot.html.

This plot enables for the interpretation of relevant dimensions from the PCA. In the skills
dimension, the space between Clusters 1 and 5 may represent a dimension of ambiguity.
Whereas, the space between Clusters 4 and 6 add a dimension of relevance of those skills
listed in relation to the job expectations. Therefore, there can be job advertisements that
list too many skills and they are ambiguous or job advertisements that fail to list skills for
jobs that may need them and it is clear that they are lacking. In which, both situations
would lead to deceptive ratings. A static version of the plot can be found in Figure 31
below.

Figure 31
Clusters for the Skills Dimension

Job Dimension 7: Qualifications. While the qualifications section typically appears
after the skills section. Many job advertisements may only choose to include one or those posting
them may combine those two sections. However, skills and qualifications are distinct. In that,
skills are more specific abilities or more than enable individuals to perform tasks, like being
proficient in a coding language or a certain software. Whereas, qualifications are like credentials
earned or physical awards for a commitment to a goal, such as a degree or certification. This
distinction is important because qualifications can be more difficult, time consuming, or
expensive to obtain and jobs may have less flexibility on that dimension than on the skills
needed, where alternative skills could suffice.

Descriptive Statistics for Qualifications. The descriptive statistics for the 10 job
advertisements and their ratings of deception for the Qualifications dimension can be found in
Appendix I1, Table 39. Significant correlations between job advertisements and their
corresponding deception ratings indicate that certain qualifications sections received similar
ratings. Given the diverse range of jobs and equally diverse qualifications for each job, this is
unexpected. However, this could mean that if there are no qualifications listed, the participants
only have a single stimulus to look at to rate deception, as opposed to the presence of varied text.
This could lead to more similar ratings between different ads. Additionally, many of the means
are around the midpoint of the deception ratings scale, where the participants indicated that they
felt the ad was neither authentic nor deceptive. There are also high standard deviations,
indicating high variability around those means per job advertisement.
Latent Profile Analysis for Qualifications. Study 3 partly aimed to identify unique
deception patterns within the qualifications dimension by conducting a latent profile analysis on
the deception ratings of the 10 job advertisements. Appendix I1, Table 40, presents the LPA fit
statics. Convergence issues similar to those encountered in the 3-profile solution of model 2 led
to the exclusion of this solution, although it is still included in the fit statistics table. Addressing
Research Question 2a, an optimal 2-profile solution was chosen using model 2’s assumptions,
as it exhibited the best fit indices, including a BIC of 4,412 and a significant BLRT value of p =
0.010.
Appendix I1, Table 42, displays the distribution of participants across the two profiles
and their corresponding means for the 10 job advertisements. In relation to Research Question
2b, approximately 78.1% of the sample belongs to Profile 1, the "Overall Uncertain" profile,
while the "Overly Trusting" profile encompasses the remaining 21.9% of respondents. As shown

in Figure 32's latent profile plot, both profiles exhibit very similar deception patterns across the
advertisements. Even though Profile 1 viewed job advertisements as more uncertain that the
more trusting nature of those in Profile 2, both profiles tend to find the job advertisements 2 and
8 more deceptive than the rest, although not quite to the slightly deceptive level.
Figure 32

Job advertisement 8 lists the qualifications for the Health Resource Analyst I position as:
“Driver’s License (Preferred), US work authorization (Preferred)”. Which seems unrelated to the
position without much explanation or any additional information in other parts of the
advertisement. Job advertisement 2 for an Early Intervention Specialist, does not have a section
specifically titled qualifications, but mentioned that the applicant needs, “a deep commitment to
show up everyday (which includes reliable transportation and a valid driver’s license). Again this
is a reasonable qualification but may not equate to the employee’s commitment to showing up on

time and may exclude those that rely on public transportation.
These both can be viewed in their entirety in Appendix B1 and can be accessed via the following
OSF link: https://osf.io/xf9e6/files/osfstorage.
Generalizability for Qualifications. In Study 3, the generalizability coefficient was
recalculated to address the low generalizability identified in Study 2. With the modified study
design and methodology, the total G-coefficient reached 0.816, exceeding the >0.7 standard used
in Study 2. The detailed breakdown of variance components can be found in Appendix I1, Table
41. Contrary to the initial conclusion of unique perceptions based on Study 2’s generalizability
calculations, this increase may be attributable to the similar patterns of responding even across
different groups. There is only a slight difference in how strongly they feel something in a job
advertisement’s text is deceptive, in terms of the qualification’s secession. Additionally, many
companies did not differentiate between skills and qualifications, or even include qualifications
which would limit the rating to remain around the midpoint of “neither deceptive nor authentic”.
The qualifications dimension also has the largest source of variance attributed to the residual
component or the interaction between the person and item sources, at 73.9%. This indicates that
there are unexplained sources of variability contributing to the G-coefficient, potentially meaning
that the G-coefficient could be higher in including other factors in the study to account for that
unexplained variance. It could also indicate that deception is accurately measured via a singleitem and the perceptions are generalizable across individuals for a group level shared perception.
NLP Topic Modeling for Qualifications. Study 3 also aimed to evaluate the deception
perceptions at the individual level for each participant’s ratings by extracting meaning from the
large volume of text responses. Utilizing NLP topic modeling with pre-trained transformers

enables a deeper examination of the reasons behind the ratings participants provided for each
qualifications section. This covers Research Question 3.
Within the qualifications dimension there was a sample size of n = 269 statements,
indicating that 269 participants rated the job descriptions across the 10 advertisements as some
level of deceptiveness. The qualifications dimension had an optimal cluster solution of 6 clusters,
representing the reasons or more nuanced details of deception perceptions. This selection is
based on the BIC plot of the GMM fit to the embeddings of the qualifications dimension (Figure
33). The plot reveals an initial drop in BIC at a solution of 6, which a later drop at 8. For more
representative clusters, a smaller number is preferred due to the relatively small number of
phrases, as thus a smaller number of assigned phrases for the additional clusters.
Figure 33
BIC Plot for Qualifications Cluster Solutions

To answer Research Question 3, ChatGPT was used to summarize the reasons
participants provided for their ratings into a primary idea for each cluster. The main ideas, along
with representative words and the number of statements in each cluster can be found in
Appendix I2, Table 43. The table reveals that due to the mixing of qualifications and skills

section in many of the job advertisements, there are similarities between the themes. For
example, Cluster 2, with 61 reasons, indicates that some positions seem to be asking for
excessive qualifications for the position of interest. These listed qualifications may also lack
specificity, as additionally supported by Cluster 3 (21 reasons) that mentions how applicants may
not apply to a job if the qualifications seem excessive and are not explained. Indicating that it is
potentially okay to mention things such as having a driver’s license as long as it is explained.
Cluster 4, with the most phrases at 62, mentions that it is unclear in many positions as to what
the qualifications are, as they are simply not listed, leading to deception if the position seems like
it may necessitate certain qualifications.
The further breakdown of top words in Appendix I2, Table 44, indicates that some
qualifications specifically mention education, although there is a separate section indicated for
this. The overlap in information can be confusing, unclear, or misleading, based on the top words
for Cluster 1, if it is inconsistent or provided without reason. This idea is more specifically
conveyed by Cluster 6, which seems to include the lack of a qualification section or information
that is interpretable.
An interactive plot of the clusters is available at the following website:
https://computationalorganizationalresearch.com/software/jobaddeception/qualifications_plot.ht
ml. This plot illustrates the text and their corresponding clusters. A static version of the plot,
shown in Figure 34, displays the relevant text inputs that contribute to the overall meaning of
each cluster based on the closest Euclidean distance to the cluster’s mean. By examining the
largest distances between Clusters 2 and 5 as well as Clusters 4 and 6, dimensions potential
represented in the 2D space can be inferred. Specifically, the latent space from Cluster 2 to 5
forms a continuum of the qualifications being mentioned to the qualifications missing. Then

from Clusters 4 to 6, there is a spectrum of excessive requirements for the position to lacking
expected requirements for the positioning. This could indicate that a combination at either end of
the spectrum is deceptive to applicants, including excessive requirements that do not have
justification. This could seem deceptive or even unfair if it disproportionately impacts certain
groups based on the qualifications without reasoning.
Figure 34
Clusters for the Qualifications Dimension

Job Dimension 8: Schedule. The dimension of schedule is important to assist applicants
in envisioning themselves in that advertised position. It provides tangible information about what
the work week would look like for an employee and if not truly reflective of the expected
schedule, it could lead applicants to start a job and quickly have to quit due to a schedule that

they did not expect and does not work for them. Additionally, flexible schedules and work-life
balance are important factors for job applicants when searching for new opportunities and is
probably a factor that is focused on when job searching (Kossek et al., 2011).
Descriptive Statistics for Schedule. Appendix J1, Table 45 contains the means, standard
deviations, and intercorrelations of the 10 job ads for the schedule dimension. Several notable
aspects can be observed in this table. First, there are less significant correlations between job
advertisement deception rating than many of the other dimensions (22/45) at just about half. This
could indicate a lot more variability in the options for schedules as well as the different schedules
for the different kinds of jobs. Also, due to the relevance of the schedule dimension, there are
hardly any job advertisements that fail to mention the schedule details. While several means are
around the uncertainty midpoint, there are quite a few at or near 4, indicating that there is a slight
level of deception for the salary information in those job advertisements. Additionally, there are
high standard deviations across all job advertisements indicating substantial variance in the
reported means.
Latent Profile Analysis for Schedule. Study 3 aimed to uncover distinctive deception
patterns within the schedule dimension of the job advertisement. The LPA fit statistics can be
found in Appendix J1, Table 46. Again, there was a convergence issue for the 3-profile solution
in model 2, stemming from a convergence issue in model fit. Consequently, this solution is
reported but not considered in the final best fit solution.
Research Question 2a was addressed by identifying an optimal model and profile fit
using a 2-profile solution with model 2. Adhering to the same standards for fit indices, such as
BIC and BLRT significance, the chosen solution had the lowest BIC at 4,448, with a significant
BLRT value of p = 0.01.

Appendix J1, Table 48 presents the distribution of participants across the two profiles and
their respective means for the 10 job advertisements. With regard to Research Question 2b,
approximately 54.4% of the participants belonged to Profile 1, labeled “Moderate Skepticism”,
while 45.6% of participants belonged to the “Mixed Suspicious” Profile 2. Figure 35 displays the
latent profile plot for the schedule dimension based on the mean ratings of each job
advertisement.
Figure 35

Each profile contains about half of the participants, meaning there is a fairly even split
between profile membership. Further assessing the nature of the profiles, visually based on the
plot, addresses Research Question 2c. Both profiles have strong fluctuations across job
advertisements, but trend in a very similar manner. Again, the main difference is the level of
intensity in deception deceptions. There are high ratings of deception for both profiles for job

advertisements 2 and 4. Additionally Profile 2 shows a heightened level of deception for job ad
3, compared to ads 2 and 4, while Profile 1, shows a slight leniency in skepticism for job ad 3.
Finally, both profiles were at least skeptical of job advertisement 10. These can be found in
Appendix B1, or at the same OSF link: https://osf.io/xf9e6/files/osfstorage.
Job advertisement 3 for the registered dietitian indicates that the position can be full-time,
part-time, or temporary with a flexible schedule. Job advertisement 3 also advertises being able
to set your own schedule, which could appear deceptive for a health position. Job advertisement
4 for the HRIS analyst, says the job is full-time but includes a statement saying “scheduled ‘off
business hours’ during periods of system outages”. This is a vague statement and may not
directly relate to applicants better understanding their schedule. Job advertisement 2 for the early
intervention specialist says the position is full-time without much elaboration. Job advertisement
10 for the online marketing manager mentions that the position is full-time again, without
additional details.
Generalizability for Schedule. In Study 3, the generalizability coefficient was
recalculated due to Study 2's low generalizability. This resulted in a G-coefficient of 0.847,
which is above the >0.7 standard and can be found in Appendix J1, Table 47. This is supported
by the almost equal person and item sources of variance with 15.30% and 14.1% of the variance,
respectively. That is, the variability is almost equally attributable to differences in deception
perception rating patterns of individuals as well as the specific features of the items. There is also
the remaining 70.6% of the variance attributed to the residual which could mean that perceptions
of deception and the corresponding rating patterns of a person may be influenced by study design
or something unmeasured.

NLP Topic Modeling for Schedule. The pre-trained transformer model for topic
discovery is the second part of Study 3 and assists in finding individual-level reasons as to why
deception perceptions were formed or can provide more detail to the numeric rating. This aims to
answer Research Question 3.
Within the schedule dimension there was a sample size of n = 372 statements, indicating
that 372 participants rated the job descriptions across the 10 advertisements as some level of
deceptiveness. The schedule dimension had a cluster solution with the best fit at n = 6, based on
the BIC plot shown in Figure 36. This solution was decided upon due to the drop in BIC from the
5-cluster solution to the 6–cluster solution. Further support for the 6-cluster solution comes from
the leveling off and slight increase in BIC until the 10-cluster solution.
Figure 36
BIC Plot for Schedule Cluster Solutions

In relation to Research Question 3, participants’ justification for their individual ratings
were condensed into a central theme for each cluster using ChatGPT. Table 49, in Appendix J2
displays the representative words and the quantity of statements for each cluster. Some clusters,
like Clusters 3 and 5 had the majority of the statements at 96 and 85, respectively. However, the

ideas behind these clusters are quite opposing. Cluster 3 has a main idea of there being
information about the schedule that conveys information about flexibility, work hours,
availability and compensation for those hours. Cluster 5’s main idea focuses on a lack of
information about work hours, shift availability, and scheduling factors, causing uncertainty. In
either situation it appears that applicants could find very important schedule information
misleading or even deceptive.
Upon reviewing the top words by cluster in Appendix J2, Table 50, a large portion of
many of the clusters contain the word “misleading”. Clusters 1, 2, and 3 all have misleading as
the top word. However, like the difference between Cluster 3 and 5, it looks like there are
differing reasons as to why the scheduled portion of the job advertisement is found to be
misleading. This can be further explored by looking at the specific phrases in each cluster and
getting an idea of the dimensions in the 2D space that separates the clusters.
The plot of phrases by cluster based on their embeddings reduced into a 2D space with
meaningful dimensions can be found at the following web page:
https://computationalorganizationalresearch.com/software/jobaddeception/schedule_plot.html.

Additionally, a static version of the plot can be found in Figure 37, below. Some
observations from these plots are that the continuum of no information to too much
information between Clusters 3 and 5 is depicted.

Figure 37
Clusters for the Schedule Dimension

Job Dimension 9: Education. The education dimension is used interchangeably
sometimes in Indeed.com advertisements. However, a separate input section is provided for the
skills, qualifications, education, and experience needed. All which are distinct. Not all
qualifications include education, that is education is a more specific type of qualification. There
also may be industry standards as to the appropriate level of education to request of applicants
for certain positions within different industries. Additionally, education is a very long term
qualification that immediately invalidates someone from a position if they do not meet the
educational requirements.

Descriptive Statistics for Education. Appendix K1, Table 51 presents the means,
standard deviations, and intercorrelations of the 10 job ads cornering the education dimension.
This table illustrates a few key points. First, there are several significant correlations between
deception ratings of different job advertisements. This could indicate that different positions are
asking for applicants with different educational backgrounds or levels but it is viewed
deceptively. This could also mean that the same educational background is applied to different
positions and that is equally deceptive. There are means along the higher side of the midpoint of
the 7-point scale. This demonstrates that there are slight deceptive perceptions across
advertisements. Finally, there are high standard deviations for all means, showing variability
from those means of each job advertisement
Latent Profile Analysis for Education. Study 3 aimed to identify different distributions
of response patterns within the participants’ ratings of deception. That is, grouping individuals
based on similar ways of viewing deception within the education section for the sample of job
advertisements. The LPA fit statistics are presented in Appendix K1, Table 52. There were no
convergence issues with the 3-profile solution in model 2, like several other dimensions. This
could be attributed to the differing standard deviations and intercorrelations for different
dimensions, causing convergence issues for different dimensions in the same sample.
Research Question 2a is assessed by identifying the optimal model and profile fit using
a 3-profile solution with model 2. Following the same criteria for fit indices, such as BIC and
BLRT significance, the selected solution had the lowest BIC at 4,405, with a significant BLRT
value of p = 0.01.
The spread of participants across the 3 profiles and their corresponding profile means for
each job advertisement are presented in Appendix K1, Table 54. Addressing Research Question

2b, approximately 14.9% of the participants belonged to Profile 1, named the “Generally
Trusting” group. Profile 2 contained the majority of the sample with 46.5% of the participants
who tended to respond in a “Slightly Skeptical” manner. Finally, Profile 3 has 38.6% of the
sample and is named “Trusting with Heightened Awareness”. Figure 38 displays the latent
profile plot for the education dimension based on the estimated means of the profile with the best
fit’s responses.
Figure 38

Visually and based on the means, Research Question 2c was addressed to understand the
nature of each of the 3 profiles. Looking at the distribution of participants per profile, there are
many more participants in Profiles 2 and 3 than in Profile 1, which indicates that less people are
in the more consistent group in terms of perceptions of deception across job advertisements. The
other two groups fluctuate more as to what advertisements are viewed as deceptive. However, all
of the profiles are barely above the “slightly deceptive” level, with Profile 1 actually being more

trusting than suspicious of the advertisements. The only two advertisements that are even
considered deceptive in terms of education are job advertisements 4 and 8. These can be found in
Appendix B1, or at the same OSF link: https://osf.io/xf9e6/files/osfstorage. Job advertisement 4
for the HRIS analyst does not mention any education necessary for the position. Job
advertisement 8 for the health resource analyst also has no educational information.
Generalizability for Education. In Study 3, the generalizability coefficient was
recalculated due to Study 2's low general the partitioned variance and the sources of that
variances along with the G-coefficient are shown in Appendix J1, Table 53. The G-coefficient
for the education dimension is above the >0.7 standard at 0.823. Additionally, there are almost
equal person and item sources of variance with 17.7% and 17.2%, respectively. There is also the
most variance from the residual interaction at 65.1%, indicating that it could be due to
measurement error or something unaccounted for in the study.
NLP Topic Modeling for Education. The second component of Study 3 involves a pretrained transformer model for topic discovery, which aids in identifying the specific reasons
behind the formation of deception perceptions at an individual level. It also offers further
insights into the numeric ratings. This component is designed to address Research Question 3.
Within the education dimension there was a sample size of n = 331 statements, indicating
that 331 participants rated the job descriptions across the 10 advertisements as some level of
deceptiveness. The education dimension had a cluster solution with the best fit at n = 7. This
solution is based on a visual assessment of the BIC plot. From the solution of 6 to 7 clusters,
there is a clear decrease in the BIC, indicating a better fit at a 7-cluster solution. Additional
support for this solution comes from the leveling off after the 7-cluster solution, indicating that
there are only slight incremental improvements in the 8-10 clusters solution.

Figure 39
BIC Plot for Education Cluster Solutions

ChatGPT was run on the phrases in each cluster to find tangible themes and to address
Research Question 3. Table 55 in Appendix K2 shows the number of statements per cluster out
of the total 1,140 statements analyzed, as well as the representative words and summaries. The
table demonstrates that a clear majority of the phrases are found in Cluster 4 at 134. The main
idea of Cluster 4 included the broad concepts of the information included being misleading,
lacking of necessary information, and thus causing confusion and uncertainty. Additionally,
Cluster 5 with 26, phrases is dedicated to education requirements indicating a high school or
college diploma without specifying why or that it is for a job where that requirement may not be
the norm.
Appendix K2, Table 56 shows the top words of each cluster based on frequency. Of note,
in Cluster 2, there are words such as: “degree”, “associate”, and “college” which indicate that
participants are thinking and assessing the education information in the job advertisements.
However, they may be deceptive because of the other words in the cluster such as: “required”
and “preferred” indicating that there are some education requirements that are not necessary for

certain positions, but there is a preference towards applicants that meet those requirements
whether it is stated or not.
To understand the full phrases in each cluster and the space between each cluster as
relevant dimensions, an interactive plot was produced. This can be found at the following link:
https://computationalorganizationalresearch.com/software/jobaddeception/education_plot.html.
A static version of this plot can be found below in Figure 40 with the phrases reported that are
the closest in Euclidian distance to the mean of the cluster. The plot depicts a large space
between Cluster 2 and Cluster 4, which may represent a dimension of lacking education
information to existent information. Additionally, the space between Clusters 5 and 6 represents
a dimension of too high of degree requirements to too low of degree requirements compared to
the industry standard.

Figure 40
Clusters for the Education Dimension

Job Dimension 10: Experience. The dimension of experience is related to qualifications,
skills, and education, but technically refers to more similar or same job experience. Jobs that
state experience requirements typically are not entry level. Therefore, employees looking for a
specific job level may interpret the experience section according to the position title.
Descriptive Statistics for Experience. The means, standard deviations, and
intercorrelations of the 10 job ads for the experience section is in Appendix L1, Table 57. Of
note are the large number of significant correlations. This is found across many dimensions and
shows that the sections in different ads are viewed similarly in terms of deception. This could
indicate that those sections have similar text or that the job advertisements have different text
eliciting similar levels of deception. There are also many means at the uncertainty level with only

a few running into the slightly deceptive ratings. Additionally, there are high standard deviations
for all job advertisements, indicating that there is variance around those reported means, and they
may not be representative of every individual that viewed that job advertisement.
Latent Profile Analysis for Experience. Study 3 aimed to uncover distinctive deception
patterns within the experience portion of the job advertisement. The LPA fit statistics can be
found in Appendix L1, Table 58. There were no convergence issues and the profile and model of
best fit was a 3-profile solution under the assumptions of model 2. This addresses Research
Question 2a. Maintaining the same standards for fit indices, such as BIC and BLRT
significance, the selected solution had the lowest BIC at 4,360 with a significant BLRT value of
p = 0.01.
In regards to Research Question 2b, Appendix L1, Table 60 presents the distribution of
participants across the 3 profiles. Specifically, Profile 1, which was named “Generally Trusting”
contained 15.8% of the participants. Profile 2 contained the majority of participants at 45.6% and
was named the “Generally Skeptical” group. Finally, Profile 3 contained 38.6% of the sample
and were named the “Wavering Skepticism” group. Figure 41 shows the latent profile plot for
the experience dimension based on the mean rating of each profile for each of the 10 job
advertisements.

Figure 41

The latent profile plot for experience shows that perceptions of deception are less profile
dependent and potentially more job advertisement dependent, as there is not much difference
between profiles in terms of intensity of ratings or how those ratings fluctuate. There is a slight
difference in consistency of ratings across job advertisements for each group, in that Profile 3
wildly varies, while Profile 1 and 2 have more consistent rating styles in terms of deception.
The job advertisements that did show similar ratings, regardless of profile were job
advertisements 3 and 8. These can be found in Appendix B1, or at the same OSF link:
https://osf.io/xf9e6/files/osfstorage. Job advertisement 3 seems to depict inconsistent information
in that they mention looking for someone who “displays a high degree of professionalism,
experience, and desire to help people.” That is the only mention of experience besides the
qualification of being a registered dietician. It seems inconsistent to have mention of a high
degree of experience and not mention any of the specifics past being a registered dietician. Job

advertisement 8 for a health resource analyst does not mention any prior experience needs
despite having intensive job responsibilities listed that may not be depicting an entry level
position.
Generalizability for Experience. In Study 3, the generalizability coefficient was
recalculated due to the low generalizability of Study 2. This resulted in a G-coefficient of 0.848,
which is above the >0.7 standard. The table reporting the G-study statistics can be found in
Appendix L1, Table 59. This may be considered fair generalizability evidence for shared
perceptions of deception. This can be seen in the similarity between the profiles in the LPA plot,
they tend to rate very similarly despite having some differences in consistency. This may suggest
that the profile is part of a larger profile which is not captured due to measurement error or
unmeasured influences of perception, or even low sample size.
NLP Topic Modeling for Experience. To gain additional insight into the nature of
deception ratings, the input text provided by each participant was analyzed and assigned to a
cluster using the analytic topic modeling approach discussed. This process aims to address
Research Question 3.
The total experience dimension there was a sample size of n = 295 statements, indicating
that 295 participants rated the job descriptions across the 10 advertisements as some level of
deceptiveness. The experience dimension had a cluster solution that demonstrated the best fit at n
= 9 clusters. This is decided from the BIC plot and visually assessing the lowest BIC with the
corresponding cluster fit. The BIC plot is shown below in Figure 41. There is a clear lowest BIC
at the 9-cluster solution, even with the BIC accounting for complexity and penalizing more
dimensions to avoid overfitting.

Figure 41
BIC plot for Experience Cluster Solutions

Research Question 3 also concerns the nature of the clusters. An interpretable summary
from the many phrases per cluster was produced utilizing ChatGPT. The details of the clusters
statement distribution and the summaries of the clusters are found in Appendix L2, Table 61.
The two most populated clusters were Cluster 3 and 4. Cluster 3 with 58 phrases had themes
around experience requirements that are misleading or lacking specific details to make it
understandable or clear. Cluster 4 had 56 phrases and had a main idea of the experience
requirements lacking or not enough information to even determine the requirements.
Additionally, Cluster 8 with 44 phrases has the theme of either excessive or insufficient
requirements for what job would be expected to require. While, Cluster 9 with 25 statements
focused on themes of the difference between optional or preferred and required not being clear.
The top words per cluster are found in Appendix L2, Table 62. Of note in this table is the
way Cluster 2 seems to quantify experience. Specifically, the word “year” and “years” are at a
combined 40.6% of the total words. This is across all job advertisements, so if entry level

positions mention prior years of experience, they may be inaccessible to many individuals. This
is also in contrast to job ads that simply state “prior” experience, which may not provide enough
specification based on the top words from Cluster 1.
A plot of clusters with interactive labels for the experience dimension can be accessed at
the following link:
https://computationalorganizationalresearch.com/software/jobaddeception/experience_plot.html.

This plot is also depicted as an image in Figure 42, below. Some dimensions can be
identified from the plot. The space from Cluster 2 to Cluster 8, may depict a dimension of
excessive experience to insufficient experience for the position. Additionally, the latent
space from Cluster 5 to Cluster 7 may demonstrate a relevant dimension of niche to
general experience listed, or the specificity of the listed experience.
Figure 42
Clusters for the Experience Dimension

Job Dimension 11: Work Location. The work location is an essential part of the job
advertisement. However, this can include more than just the physical location in the section on
Indeed.com. Location can include the available telework options, whether there are multiple
locations that the employees commute between, if there are high travel requirements and the
physical location may not be as relevant. All of these considerations are especially important as
telework and remote work options are more prevalent or expected in certain industries.
Descriptive Statistics for Work Location. The means, standard deviations, and
intercorrelations of the 10 job ads for the responsibilities can be found in Appendix M1, Table
63. There are the least number of significant correlations out of any of the dimensions at 19/45.
This indicates that the deception perceptions of the work location in different ads are not related.
Potentially indicating that the work location is a fairly distinctive feature. The means for work
location are low compared to the midpoint, where there is barely slight deception indicated by
the means of the different job advertisements. Additionally, the standard deviations are high
potentially reflecting true variability around the mean as to how the job advertisements are
perceived. However, based on the high G-coefficient, these high standard deviations are more
likely from measurement error or ineffective means of capturing the ratings of deception for the
work location dimension. This could even represent that many companies are back to in person
and do not have additional considerations associated with the work location.
Latent Profile Analysis for Work Location. Study 3 aimed to identify unique patterns of
deception within the work location dimension. This goal was accomplished by performing a
latent profile analysis on the corresponding ratings for each of the work locations in the 10 job
advertisements. The LPA fit statistics can be found in Appendix M1, Table 64. A convergence
issue emerged for the 3-profile solution in model 2, which might be due to the sample size used.

The sample size could potentially cause non-convergence after 1,000 iterations as a result of
conflicts between the sample size and the assumptions of the model. Although these solutions
were not considered, they have been reported.
Research Question 2a, addressed the optimal model and profile fit which was a 2-profile
solution with model 2 assumptions. Adhering to the same standards for fit indices, such as BIC
and BLRT significance, the selected solution has the lowest BIC at 4,192 and a significant BLRT
at value of p = 0.01.
Appendix M1, Table 66 showcases the distribution of participants across the two profiles
and their respective means for the 10 job advertisements. In terms of Research Question 2b, the
profile maintained a fairly even split. There were 41.2% of the participants in Profile 1, named
“Uncertain but Trusting” and the remaining 58.8% of participants were in Profile 2, named
“Generally Trusting but Aware of Deception”. Figure 43 illustrates the latent profile plot for the
work location dimension based on the average rating of each profile for each of the 10 job
advertisements.

Figure 43

Research Question 2c delves into the characteristics of each profile. A more detailed
analysis of Figure 43 and the average ratings of each profile indicates that Profile 1 and 2 show
fairly similar ratings with none depicting too highly deceptive rating, besides Profile 2, seems to
differ in feeling that job advertisement 8 has a deceptive work location. These can be found in
Appendix B1, or at the same OSF link: https://osf.io/xf9e6/files/osfstorage. Job advertisement 3
for a registered dietician mentions that you can work in person or remote, but does not actually
mention where the in person location is. Job advertisement 8 for the Health Resource Analyst
says that you need the ability to commute or relocate. It also specifically mentioned that the job
is in Carson City, NV, but you need to reliably commute or plan to relocate before starting work,
which is preferred. Job advertisement 10, for the online marketing manager but does not state
that it is remote, it may need to be assumed by the applicant.

Generalizability for Work Location. In Study 3, the generalizability coefficient was
recalculated due to Study 2's low generalizability. This resulted in a G-coefficient of 0.861,
which fall above the >0.7 standard and can be found in Appendix M1, Table 65. Additionally,
there is a large amount of residual variance at 73.2% indicating that there is either measurement
error in that something else may be influencing the deception perceptions of work location.
NLP Topic Modeling for Work Location. The pre-trained transformer model for topic
discovery is the second part of Study 3 and assists in finding individual-level reasons as to why
deception perceptions were formed or can provide more detail to the numeric rating. This aims to
answer Research Question 3.
Within the work location dimensions there was a sample size of n = 214 statements,
indicating that 214 participants rated the job descriptions across the 10 advertisements as some
level of deceptiveness. The work location dimension had a cluster solution with the best fit at n =
6, based on the BIC plot shown in Figure 36. This solution was determined by looking at the BIC
score of each cluster solution and choosing the solution with the lowest BIC. While a cluster
solution of 6 and 10 are potentially comparable, the 6 cluster solution is more interpretable based
on the resulting plot of clusters and corresponding data points.

Figure 44
BIC Plot for Work Location Cluster Solutions

In relation to Research Question 3, participants’ explanations for their individual ratings
were synthesized into a core theme for each group using ChatGPT. Appendix M2, Table 67
demonstrates the characteristic words and the number of statements for each group. Of note is
Group 5 with the strong majority of statements at 129. The themes depicted for Cluster 5 from
ChatGPT center around the information being unclear or deceptive about remote work,
potentially applicable to the assumed remote position from Job ad 8. Additionally, the theme of
Cluster 5 mentions multiple locations being unclear. Indeed.com default to put the work location
as multiple locations if it is not specified, which further leads to confusion if there are inferences
the company is expecting the applicants to make about the remote nature of work.
Further understanding can be added to the cluster in analyzing the top words based on the
frequency distribution of words. For the work location dimension, this can be found in Appendix
M2, Table 68. The top words for many of the clusters stop at one or two words. This is due to the
limited words in the included statements and many of those simplifying being the same word.
This could be attributed to survey fatigue or inattentive or effortless responding. However,

Cluster 5 has instances of words such as “remote” (10.4%), “office” (5.5%), and “address”
(5.5%). These could indicate misleading feelings coming from the lack of specification on where
the job is or if there are inconsistencies in remote and physical locations advertised in the job
posting.
A visualization of phrases by group, based on their reduced embeddings in a 2D space
with meaningful dimensions, can be accessed at the following webpage:
https://computationalorganizationalresearch.com/software/jobaddeception/worklocation_plot.ht
ml. The plot shows that there are some clusters with repeated instances of a single word.
However, the space surrounding Cluster 5 represents a variety of things applicants may find
misleading. As the space approaches Cluster 1, there are more instances of phrases that lack
specificity altogether, and that lack is what is found to be deceptive.
Figure 45
Clusters for the Work Location Dimension

Shared Topics Across Dimensions. The final Research Question 3a concerns the
shared topics found across all 11 dimensions researched in Study 3. To assess this research
question empirically, as opposed to looking at all of the topic plots and cluster themes per
dimension one at a time, a final topic analysis was conducted on the combined text inputs. This
results in a dataset of deceptive reasoning phrases of n = 12,540. This is a more substantial
amount of text data and is closer to text sample sizes that function particularly well with pretrained transformers.
The same analytic approach was taken in discovering topics within the entire dataset.
These reasons for deception perceptions across all job advertisement dimensions can show the
most relevant theme based on cluster size and relevant emergent themes. This can also
demonstrate the portion of statements per dimension that are relevant amongst all other
dimensions. The representative words across multiple clusters can also show the topics or words
that are relevant in comparison to the total amount of phrases across all dimensions.
The was a sample size of n = 2,994 phrases depicting deceptive or misleading perception
explanations included across all dimensions. The overall topic solution for the combined
dimension topic analysis was a 10-cluster solution. This was determined using the BIC and
finding the cluster solution with the lowest BIC. This plot is shown in Figure 46 below. The 10cluster solution shows a clear drop in BIC from the 9-cluster solution, with no other cluster
solutions with a comparable BIC score. This seems to make theoretical sense as well, due to the
combined nature of all 11 dimensions, and there could be approximately 1 cluster per dimension
with the key concerns or reasons for deception included.

Figure 46
BIC Plot for all 11 Dimensions

The interpretation of the produced 10-cluster solution was done by asking ChatGPT to
create a main idea statement for each cluster. Without using ChatGPT, it would be much more
difficult for a human to interpret all of the data points or statements and condense them into a
few main points. These summaries per cluster and the statements per cluster are in Table 69, in
Appendix N. Cluster 4 stands out as containing a large number of phrases at 1,120, which is
almost the entire data set for a single dimension topic analysis. Cluster 4 conveys main ideas that
focus on the work location being unclear and confusing, as well as lacking specificity
surrounding the in-person and remote positions. This could be representing the entire work
location dimension as a main idea about how the lack of specificity and clarity about remote and
in-person work is deceptive. Cluster 2 also contains 395 phrases about misleading education
requirements that are unclear or have unrealistic qualifications. Cluster 3 demonstrates a strong
theme around the lack of information appearing misleading. Additionally, Cluster 6 focuses on
how salary information presented in ranges are unclear or misleading when it includes flexible

hours as well. Finally, of note, Cluster 10 has a focal topic about the lack of explanation behind
the benefits listed.
The top words table for all 11 dimensions can be found in Appendix N, Table 70. While
there are clear clusters for certain dimensions, there are also clusters that focus on themes in
deception perception. Specifically, Cluster 3 has top words of “information” (13.4%), “provided”
(12.8%), “lacks” (9.9%), indicating a cluster formed around statements describing that the lack
of information or insufficient information was misleading. Additionally, Cluster 7 has 39.9% of
the words being confusing. This could mean that the information is not well organized or
conflicts within the job advertisement.
A visualization of phrases that belong to each cluster in a reduced 2D space can be found
at the following webpage:
https://computationalorganizationalresearch.com/software/jobaddeception/totaldimensions_plot.
html. The sample size of phrases across all dimensions is a larger and more suitable sample size
to discover clear dimensions in the 2D space represented in the plot. The resulting cluster plot
shows the clear clusters but they centralize around similar unclear concepts.The space between
clusters can also be referred to as the reduced dimensions of relevance. In looking at Cluster 4,
while it focused on work location, it overlaps with other statements and clusters that contain
unclear terms. As the space in the 2D plot moves closer to Cluster 2, there are more statements
that cover the lack of specific details all together. Additionally, near the top of the plot, Clusters
6 and 9 cover benefits and pay about a job that seem overly positive, where there are a few
statements in Cluster 1 at the opposite end of the space, that may define the other end of the
spectrum of a lack of information that should be required for the specific positions, such as
experience or certain requirements. Although some clusters form based on dimension, there are

overlapping ideas among clusters that mention deception may stem from too much information
or too little information. These misleading feelings during the application process can also be
from the existent information appearing unclear, vague, or conflicting with information in other
sections of the advertisement. There are also job advertisements that may just be confusing to
those trying to apply, which would certainly discourage applicants from trying to understand the
job position on their own with lacking information. The static version of the plot can be found
below in Figure 47.
Figure 47
Clusters for all 11 Dimensions

Summary of Results for Study 3. Overall, there are similar themes across dimensions of
unclear and confusing or conflicting information being rated as deceptive. In contrast, aspects
that can also lead to feelings of confusion or feelings of deception are job advertisements that

contain vague information. That is job advertisements that include information but it may seem
atypical for the job position and is thus viewed deceptive or misleading. Additionally,
participants felt that if there were aspects of the job ad specified that did not match the typical or
standard for that position, there should be an explanation or reasoning.
In looking at the profiles per job advertisement dimension, many profiles reflect each
other, but with varying degrees of intensity to their deception perceptions. However, many
profiles across all dimensions were around the mid-point of the 7-point scale, and job
advertisements were typically rated as slightly deceptive within each profile. The specific job
advertisements of note based on the profiles, as a whole, rating them as either consistently
deceptive or consistently authentic across dimensions were job advertisements 3 and 5. Job
advertisement 3, for the Registered Dietician contained many inconsistencies and read much like
a persuasive marketing scam to apply for a job that seemed too good to be true, with
inconsistencies, and unrealistic promises. Which was reported in text across many dimensions
and could potentially apply to this job advertisement, due to its consistent deceptive ratings,
regardless of dimension or profile. Job advertisement 5, on the other hand, was almost never
rated above deceptive across all profiles and all dimensions. Job advertisement 5, is for a legal
administrative assistant. The features of note that seem distinctly different from job
advertisement 3 are the clear noting of what qualifications are preferred or required, the
organization of the job advertisement, and through reasoning behind all sections. Additionally,
there is creative wording similar to job ad 3, but it is still viewed as more authentic than job ad 3
across many dimensions.
The table below titled, “Summary of Results by Research Question” reports a summary of
the expansive results of the 12 topic analyses and 11 latent profile analyses. While this table is

only a portion of the results, it aims to condense the main ideas into a single table for
interpretability. This table does not include research question 3a, which assesses all dimensions
of deception reasons in a topic analysis, this is reported above.
Summary of Results by Research Question
Job Ad
Dimension

RQ 2a

RQ 2b

RQ 2c

RQ 3

1. Job
Description

Most Deceptive
Job ads by Profile

2 profiles
(model 2)

Profile 1: 84.2%
Profile 2: 15.8%

1: “Mildly Skeptical
with Heightened
Awareness”
2: “Overly Trusting”

10 clustersunclear, vague,
misleading,
conflicting,
unprofessional
vocabulary, seems
too good to be true

1: Job ad # 3
2: None above
midpoint

2. Company
Overview

2 profiles
(model 2)

Profile 1: 58.8%
Profile 2: 41.2%

1: “Neutral but
Aware of
Deception”
2: “Trusting but
Occasionally
Suspicious”

7 clusterslacks sufficient
information on goal,
values, and
background; scam,
biased language

1: Job ad # 3 & 8
2: Job ad # 3 & 8

3. Salary

2 profiles
(model 2)

Profile 1: 77.2%
Profile 2: 22.8%

1: “Wary but Alert”
2: “Generally
Trusting”

5 clustersbroad range,
unrealistic salary
range, bonuses and
raises seem
deceptive

1: Job ad # 1 & 3
2: Job ad # 1

4. Benefits

2 profiles
(model 2)

Profile 1: 43.0%
Profile 2: 57.0%

1: “Slightly
Skeptical”
2: “Fluctuating
Deception”

8-clustersundefined terms,
free lunch and
appreciation week
non-traditional
benefits, flexible
schedule lack
information

1: Job ad # 3 & 8
2: Job ad # 3, 6, &

5.
Responsibiliti
es

2 profiles
(model 1)

Profile 1: 13.2%
Profile 2: 86.6%

1. “Wavering
Deception”
2. “Trusting but
Aware”

4-clustersunrealistic
expectations for the
position, overstated
or understated, lacks
specifics

1. Job ad # 3 & 4.
2. Job ad # 3

6. Skills

3 profiles
(model 2)

Profiles 1: 26.3% 1. “Mostly Trusting”
Profile 2: 30.7% 2. “Generally
Profile 3: 43.0% Trusting but Slightly
Uncertain”
3. “Trusting but
Slightly Skeptical”

7-clustersirrelevant skills, no
skills listed, implied
skills but not
explicitly stated

1. Job ad # 3
2. Job ad # 2, 3, 7,
8, & 9
3. Job ad # 2, 3, 8

7.
2 profiles
Qualifications (model 2)

Profile 1: 78.1%
Profile 2: 21.9%

1. “Overall
Uncertain”
2. “Overly Trusting”

6-clusters1. Job ad # 2 & 8
excessive experience 2. Job ad # 2, 8, &
needed, lacks details 9
and vague

8. Schedule

Profile 1: 54.4%
Profile 2: 45.6%

1. “Moderate
Skepticism”
2. “Mixed
Suspicious”

6-clustersunrealistic offer for
making your own
schedule, flexible
work arrangement,
doesn’t specify
hours or days

2 profiles
(model 2)

1. Job ad # 3 & 10
2. Job ad # 2, 4, &

9. Education

3 profiles
(model 2)

Profile 1: 14.9%
Profile 2: 46.5%
Profile 3: 38.6%

1. “Generally
Trusting”
2. “Slightly
Skeptical”
3. “Trusting with
Heightened
Awareness”

7-clustersHigh school or
college diploma
needed without
reasoning, vague or
not mentioned,
unclear requirements

1. Job ad # 2 & 8
2. Job ad # 4, 8, &
3. Job ad # 4, 8, &

10.
Experience

3 profiles
(model 1)

Profile 1: 15.8%
Profile 2: 45.6%
Profile 3: 38.6%

1. “Generally
Trusting”
2. “Generally
Skeptical”
3. “Wavering
Skepticism”

9-clustersExcessive years
experience required,
niche qualifications,
complex skills for
entry positions

1. Job ad # 2 & 8
2. Job ad # 3 & 8
3. Job ad # 3 & 8

11. Work
Location

2 profiles
(model 2)

Profile 1: 41.2%
Profile 2: 58.8%

1. “Uncertain but
Trusting”
2. “Generally
Trusting but Aware
of Deception”

6-clusterslack of information,
conflicting
information about
remote work,
multiple locations
term is unclear

1. Job ad # 3 & 10
2. Job ad # 3, 8, &

Note. Research question 2a (RQ 2a): How many latent profiles best explain perceptions of deception within the
various job dimensions? Research question 2b (RQ 2b): What is the proportion of respondents belonging to each
profile? Research question 2c (RQ 2c): What is the nature of profiles’ response patterns? Research Question 3 (RQ
3): Within different groupings of deceptiveness perceptions (latent profiles) for each dimension, what are common
reasons people give for why they found the dimensions misleading?

#### 3.3.7 Study 3 Discussion

The aim of Study 3 was to take a more person-centered approach to understanding
perceived deception in job advertisements. This is due to the low generalizability found in Study
2. In running the latent profile analyses on each of the 11 dimensions, 2 to 3 profiles were found
amongst different dimensions. However, these profiles fluctuated around the midpoint of mildly
deceptive to mildly authentic. Many dimensions were displaying profiles that looked similar with
different levels of intensity or variability across job advertisements. In finding latent profiles of

deception perceptions for job advertisement dimensions, the results are bounded by sample size.
With a sample size of n =114, there was only enough power to detect 3 profiles at a reasonable
detection rate (56%). However, the median number of latent profiles in organizational research is
4. Using a larger sample size, such as n = 200, there would be more power to potentially detect
more nuanced profiles that cannot be found with 114 ratings. Specifically, in simulating known
cluster solutions with unconstrained covariance, randomly dispersed means with a variance equal
to 1, n = 200 has the power to detect closer to the median of 4 profiles with 78.9% power. The
full code of this simulation can be found at the following OSF in the “Power Analysis” in the file
labeled “Proposed_Study_3_Power_Analysis.ipynb”.
Additionally, Study 3 reanalyzed the G-coefficient computed for each dimension in Study
2, however, in Study 3, most dimensions had an acceptable G-coefficient at >0.7 or just near it
(Cronbach et al., 1972; Putka et al., 2008). There was a study redesign to avoid missingness and
the sparse matrix found in Study 2, this lack of missingness, effective attention checks and less
advertisements viewed per participant, Study 3 could be depicting more realistic coefficients.
This is supported by the similarity between several of the latent profiles discovered, which trend
in similar ways to which advertisements were most deceptive. Along with sufficient
generalizability support for shared perceptions between individuals from Study 3, there were
consistent high standard deviations for many job advertisements. This indicates that the ratings
are fairly spread out from the means of each job dimension or vary greatly, but the relative
differences or spread between the data points remain consistent across the job advertisements
rated, or raters rate similarly regardless of job advertisement. This situation of high standard
deviations and high generalizability coefficients could reflect real individual differences around
the mean of the job advertisements’ ratings or there could be measurement errors. The latter is

supported by the high residual validity in the G-study, potentially reflecting that there is not
necessarily true variability. Instead, there may be sample size issues reflected in these findings as
well.
I conducted the topic analysis for every dimension, which depicted several common
themes across job advertisements that ranged from unclear or incongruent information to a
scarcity or lack of information leading to deception. Additionally, there are unique cluster
solutions of topics per dimension not found in the overall topic modeling approach that
contribute a unique perspective within each dimension or section of the job advertisement. In
understanding the individual statements and their classification in clusters, it can help to fully
understand a spectrum of reasons deceptive perceptions are formed during a job search. That is,
without assessing all 11 dimensions, even the similarities for deception perceptions could not be
known in an empirical manner. It adds to the exploratory study that unique topics per cluster
were found to further contribute to empirically supporting job advertisement writing.

## 4 Overall Discussion

The goal of this study was mainly exploratory in nature to better understand how the text
in job advertisements is perceived. Specifically, if that text is perceived as deceptive and the
nature and reasoning behind those perceptions. In addressing this, I conducted 11 latent profile
analyses and 11 subsequent topic analyses. Each of the 11 analyses corresponded to a specific
dimension. In including all 11 dimensions and completing these analyses, a specific and direct
understanding of what leads to perceptions of job advertisements to be deceptive or misleading
can be empirically understood.
The latent profile analyses demonstrated solutions of 2 to 3 profiles amongst the different
dimensions. While these profiles did demonstrate similar patterns within dimensions with slight

fluctuations, these analyses and subsequent conclusions may be bounded by sample size. These
profiles did however, indicate specific advertisements that individuals in some of the profiles
indicated as more deceptive than others to get a better understanding of what text in the
dimension made individuals feel misled.
High G-coefficients with the improved study design from Study 2 to Study 3, showed
that the attention checks and lower ad count may have been an effectively designed study.
However, the high residual variance components for all dimensions indicates that there may be
unmeasured factors contributing to the ratings or additional issues in the study design. This is
supported though, that there are some similar patterns of responding and perceptions of
advertisements even between profiles. While this conclusion may not be generalizable without
testing with a larger sample size or a designed study, it can provide tangible evidence used to
contextualize the topic clusters of individual level statements of text.
The topic analysis demonstrated that several dimensions shared similar themes of
information provided without further detail creating confusion, vague information in the job
advertisements, as well as information that is so detailed it seems too good to be true. Within
each dimension, there are further topics related to the relevant dimension that can further provide
details as to the specific types of text in this sample of job advertisements that may be perceived
as deceptive. Additionally, Study 1 showed that among a larger number of advertisements
sampled, there are moderate levels of deception. These studies provide more direct empirical
support for what text may be negatively or deceptively perceived in job advertisements, and that
there are a fair number of advertisements where this is prevalent, which can inform the job
advertisement writing process.

### 4.1 Theoretical Implications

The major theoretical implications of this dissertation include: providing initial theory for
job advertisement features related to deception, analyzing perceptions of job advertisements from
a person-centered approach, and aiming to better understand the prevalence of perceptions of
deception in job advertisements. I conducted a thorough topic analysis for all of the 11 job
dimensions found in Indeed.com advertisements. Using a natural language processing topic
modeling approach and finding a cluster solution of best fit for each dimension, I was able to
identify major themes in each dimension. These themes indicate the reasons or explanations
participants provide as to their ratings of deception. This expands on prior research that typically
focuses on a single dimension. While some topics, such as lack of specificity or ambiguity are
consistent with prior research, those studies limited the context of those topics to the rewards and
benefits information in job advertisements (Verwaeren et al., 2017). These themes provide a
theoretical framework for further research within each dimension of the job advertisements.
In taking a person-centered approach to understanding the text features that influence
perceptions of deception or misleading feelings towards job advertisements, I conducted 11
latent profile analyses along with computing the generalizability coefficient of ratings with each
dimension. While profiles did show some similar patterns of responding, it could demonstrate
that there are more shared perceptions of deception. Regardless of the further exploration this
study may necessitate, it sets precedent for future research assessing perceptions during the
recruiting process. Much of the prior literature on attitudes and perceptions during the job search
automatically generalizes findings to all individuals, without appropriately assessing if
perceptions can be aggregated to a shared perception that may generalize outside of the study.

Utilizing an informed latent profiles analysis can set precedent for better understanding that there
may be groups of individuals that differ on their perceptions.
Finally, the initial portion of this study aimed to gather a representative sample of those
entering the workforce and better understand the nature of perceptions in job advertisements.
Without assessing the frequency of feelings of deceit or being misled by job advertisements, it
cannot be assumed that it happens for all job searchers without empirical evidence. This
provided theoretical evidence that job searchers entering the job market do find almost as many
job advertisements slightly deceptive as slightly authentic. These theoretical contributions can
help inform further research on recruitment and attitudes formed during that process.

### 4.2 Practical Implications

The major practical implication of this study includes a more empirically informed way
to write job advertisements. There are many ways a person can interpret the information in a job
advertisement but trying to better understand salient factors that could lead to negative attitudes
such as deception or feeling misled, can potentially impact the amount of applicants a job posting
receives, or even the quality of applicants. In finding unique topics per cluster such, broad pay
ranges, specific information about qualifications without reasoning, or assuming the applicant
will infer information about the work location from the title name, are all some salient dimension
specific items findings. These previously were unidentified in the relevant literature that focused
very generally on the negative effects on applicants’ intent to apply based on general information
scarcity (Feldman et al., 2006; Lee et al., 2013). In better understanding that these features may
impact at least a large portion of the applicant, job advertisement writing can be more intentional
based on avoiding eliciting feelings of being misled by the organization.

I also propose that not all perceptions of job advertisements are similar, which is a
previously unaccounted for perspective in the practice of job advertisement writing. This can
bound prior suggestions or practices that generalize job advertisement writing. In better
understanding the type of applicants the job advertisement is aimed at, certain features may elicit
a stronger feeling of deception and would have empirical support to be avoided. While there is
more research to be conducted on the nature of the profiles, it is a strong first step in the potential
of catering job ads to create realistic job previews for profiles of people that may maintain
different perceptions of what is stated in the job advertisement. Overall, this research provides
more empirical evidence that job advertisement writing should be done in a thoughtful manner to
avoid features of text that could discourage large groups of applicants from applying.

### 4.3 Limitations and Future Directions

One main limitation of the study is the conflicting evidence between Studies 2 and 3 as to
the generalizability of perceptions across individuals, that is, do all job seekers view job
advertisements the same? While the initial G-coefficient of Study 2 suggested that there was no
evidence to support a shared perception of deception in job advertisements, the follow-up Study
3 provided support for more consistent ratings of deception across individuals. There is reason to
believe that the redesign in Study 3 lends more support to the shared nature of perceptions.
Additionally Study 3 demonstrated several consistent profiles, with only slight differences in
intensity of ratings that further supports a more shared perception. However, despite this
evidence all G-studies across dimensions had high proportions of residual variance, indicating a
potential unmeasured factor, issues in measuring deception, or an insufficient sample size.
Another limitation is the significant correlations between job advertisements in each
dimension. This could mean that participants are not able to differentiate between sections in

advertisements, or that some advertisements are poorly organized and exclude sections of
interest. Therefore, it is possible that the job advertisements included in the study were too
similar in certain dimensions or lacked important information that was only on occasion found
deceptive. This issue could potentially be resolved with more job advertisements or an
alternative means of selecting relevant but distinctive job advertisements.
Another limitation is that, while the study aimed to direct participants as to what section
to focus on for each question, it may not be effective in drawing participant’s attention. That is,
participants could be considering the job advertisements as a whole; as seen in statements that
mentioned how information conflicted between sections. While this could contribute to the
theoretical background of perceptions formed during the job search, a more effective means of
isolating the dimensions of interest should be utilized.
Finally, in many of the latent profile analyses run, there were only slight variations in
intensity of responses. Many of the profiles only had a few advertisements rated as deception,
and those were only in the slightly deceptive range. While the distribution of deception from
Study 1 demonstrated that most perceptions of deception are slight or mildly, those may not be
fully captured in the LPA results. This may be an issue of acquiescence in responding potentially
due to survey fatigue. Even though Study 3 aimed to reduce survey fatigue, there were still 10
job ads rated for 11 dimensions with corresponding text that could have potentially led to
participants ratings “Neither Agree nor Disagree” almost all of the time. A solution to this could
be to focus only on a single dimension or two or even create specific examples taken from the
job advertisement for those dimensions. Additionally, changing the rating style to a rank
ordering style and having participants rank statements taken from job advertisements on their

level of deception could avoid acquiescence, get more information on a single dimension, and
further illustrate the nuances of potential profiles within dimensions.
An immediate future direction for this study is to collect a larger sample size and re-run
the latent profile and topic modeling analyses for each dimension. In comparing these results, a
larger sample size may power additional profiles to be found or more variation between profiles.
The current sample size bounds the results of the latent profiles analysis to be less generalizable.
Additionally, the topic analysis would benefit from a large sample in that there would be more
defined dimensions in the cluster plots after performing the PCA. From there, follow up research
can be more informed and directed.
A more long-term future direction would be to conduct follow up research as to the
perceptions of deception or misleadingness of job advertisements statements and text constructed
via different methods. This could include an empirically based job advertisement writing method
where profiles of potential applicants are considered to adjust information or present information
based on that profiles themes of perceived deception. In addition, another method would be to
write job advertisements for scratch, on the spot without any references to empirical guidelines
or findings. A final method would be to utilize generative text models like ChatGPT to construct
job advertisements. In presenting applicants with these different advertisements from different
sources, it can inform what method is best or at least deceptive in terms of applicant perceptions.

## 5 Conclusion

The presented research adds a theoretical and methodological perspective to studying job
advertisements perceptions that could lead to applicant behaviors that were not previously
considered. The study found that there may be a more nuanced, person-centered approach to
studying job advertisements that was not previously utilized, based on an assumption that these

perceptions were generalizable without evidence. The current study demonstrates that many
dimensions have distinct profiles, that while trending in a similar fashion, may need more power
or study design changes to detect additional profiles. This study also provides a theoretical
background that encompasses the information included in an entire job advertisement, that
extends past what many prior studies have assessed. In finding common topics across
dimensions, and also unique topics per dimension, it contributes a strong base to further inform
the job ad writing process in a more empirically supported manner.

## References

All-miniLM-L6v2. (2021, August 30). Hugging Face. Retrieved March 18, 2023, from
https://huggingface.co/sentence-transformers/all-MiniLM-L6v2/commit/acbb28c8aa70f5503c85d6b90e8cd65606993a20
Allen, D. G., Mahto, R. V., & Otondo, R. F. (2007). Web-based recruitment: Effects of
information, organizational brand, and attitudes toward a web site on applicant attraction.
Journal of Applied Psychology, 92(6), 1696. https://doi.org/10.1037/0021-9010.92.6.1696
Alter, A. L., & Oppenheimer, D. M. (2009). Uniting the tribes of fluency to form a
metacognitive nation. Personality and Social Psychology Review, 13(3), 219-235.
https://doi.org/10.1177/1088868309341564
Amaar, A., Aljedaani, W., Rustam, F., Ullah, S., Rupapara, V., & Ludi, S. (2022). Detection of
fake job postings by utilizing machine learning and natural language processing approaches.
Neural Processing Letters, 54(3), 2219-2247. https://doi.org/10.1007/s11063-021-10727-z
Angelov, D. (2020). Top2vec: Distributed representations of topics. arXiv preprint.
https://doi.org/10.48550/arXiv.2008.09470
Armstrong, G. M., Gurol, M. N., & Russ, F. A. (1980). Defining and measuring deception in
advertising: A review and evaluation. Current Issues and Research in Advertising, 3(1), 1739. https://doi.org/10.1080/01633392.1980.10505292
Aust, F., Diedenhofen, B., Ullrich, S., & Musch, J. (2013). Seriousness checks are useful to
improve data validity in online research. Behavior Research Methods, 45, 527-535.
https://doi.org/10.3758/s13428-012-0265-2

Baum, M., & Kabst, R. (2014). The effectiveness of recruitment advertisements and recruitment
websites: Indirect and interactive effects on applicant attraction. Human Resource
Management, 53(3), 353-378. https://doi.org/10.1002/hrm.21571
Baumeister, R. F., Bratslavsky, E., Finkenauer, C., & Vohs, K. D. (2001). Bad is stronger than
good. Review of General Psychology, 5(4), 323-370. https://doi.org/10.1037/10892680.5.4.323
Beal, D. J., Weiss, H. M., Barros, E., & MacDermid, S. M. (2005). An episodic process model of
affective influences on performance. Journal of Applied psychology, 90(6), 1054.
https://doi.org/10.1037/0021-9010.90.6.1054
Becker, M., Wiegand, N., & Reinartz, W. J. (2019). Does it pay to be real? Understanding
authenticity in TV advertising. Journal of Marketing, 83(1), 24-50.
https://doi.org/10.1177/0022242918815880
Bikienga, S. (2018). Understanding topic models from multivariate OLS perspective. A Gentle
Technical Survey. http://www.salfobikienga.rbind.io/papers/intro_to_topic_models.pdf
Bodur, H. O., Brinberg, D., & Coupey, E. (2000). Belief, affect, and attitude: Alternative models
of the determinants of attitude. Journal of Consumer Psychology, 9(1), 17-28.
https://doi.org/10.1207/s15327663jcp0901_2
Borchers, C., Gala, D. S., Gilburt, B., Oravkin, E., Bounsi, W., Asano, Y. M., & Kirk, H. R.
(2022). Looking for a handsome carpenter! Debiasing GPT-3 job advertisements. arXiv
preprint. https://doi.org/10.48550/arXiv.2205.11374
Borstorff, P. C., Marker, M. B., & Bennett, D. S. (2007). Online recruitment: Attitudes and
behaviors of job seekers. Journal of Strategic E-commerce, 5(1/2), 1.

https://www.proquest.com/citedby/MSTAR_192410623/9CFFE8777C884F69PQ/1?account
id=14826
Bradley, L., Royer, S., & Eckardt, F. (2008). There is a link between work life balance culture
and strategic competitive advantage. In Proceedings of the 22nd ANZAM Conference 2008:
Managing in the Pacific Century (pp. 1-21). Promaco Conventions Pty Ltd.
Breaugh, J. A., & Starke, M. (2000). Research on employee recruitment: So many studies, so
many remaining questions. Journal of Management, 26(3), 405-434.
https://doi.org/10.1177/014920630002600303
Brennan, R. L. (2001). Generalizability theory. Springer-Verlag Publishing.
https://doi.org/10.1007/978-1-4757-3456-0
Burnham, K. P., & Anderson, D. R. (2004). Multimodel inference: understanding AIC and BIC
in model selection. Sociological Methods & Research, 33(2), 261-304. https://doi.org/
10.1177/0049124104268644
Cable, D. M., & Graham, M. E. (2000). The determinants of job seekers' reputation perceptions.
Journal of Organizational Behavior, 21(8), 929-947. https://doi.org/10.1002/10991379(200012)21:8<929::AID-JOB63>3.0.CO;2-O
&DEOH'0 -XGJH7$  3D\SUHIHUHQFHVDQGMREVHDUFKGHFLVLRQV$SHUVRQဨ
organization fit perspective. Personnel Psychology, 47(2), 317-348.
https://doi.org/10.1111/j.1744-6570.1994.tb01727.x
Cajner, T., Crane, L. D., Decker, R. A., Grigsby, J., Hamins-Puertolas, A., Hurst, E., ... &
Yildirmaz, A. (2020). The US labor market during the beginning of the pandemic recession
(No. w27159). National Bureau of Economic Research. https://doi.org/10.3386/w27159

Campbell, D. T., & Fiske, D. W. (1959). Convergent and discriminant validation by the
multitrait-multimethod matrix. Psychological Bulletin, 56(2), 81.
&DPSEHOO-( 6XPQHUV*(  5HFUXLWLQJFROOHJHVWXGHQWVIRUHQWU\ဨOHYHOSRVLWLRQV
Managerial Auditing Journal, 10(3), 8-14. https://doi.org/10.1108/02686909510079684
Chaouachi, S. G., & Rached, K. S. B. (2012). Perceived deception in advertising: Proposition of
a measurement scale. Journal of Marketing Research & Case Studies, 1.
https://doi.org/10.5171/2012.712622
Chapman, D. S., Uggerslev, K. L., Carroll, S. A., Piasentin, K. A., & Jones, D. A. (2005).
Applicant attraction to organizations and job choice: A meta-analytic review of the
correlates of recruiting outcomes. Journal of Applied Psychology, 90(5), 928.
https://doi.org/10.1037/0021-9010.90.5.928
ChatGPT. (2022, November 30). OpenAI. Retrieved March 20, 2023, from
https://openai.com/blog/chatgpt#OpenAI
Chawla, N., Gabriel, A. S., Rosen, C. C., Evans, J. B., Koopman, J., Hochwarter, W. A., ... &
-RUGDQ6/  $SHUVRQဨFHQWHUHGYLHZ of impression management, inauthenticity, and
employee behavior. Personnel Psychology, 74(4), 657-691.
https://doi.org/10.1111/peps.12437
Cronbach, L. J., Gleser, G. C., Nanda, H., & Rajaratnam, N. (1972). The dependability of
behavioral measurements: Theory of generalizability for scores and profiles (pp. 1-33).
New York: Wiley.
Collins, C. J., & Han, J. (2004). Exploring applicant pool quantity and quality: The effects of
early recruitment practice strategies, corporate advertising, and firm reputation.
Personnel Psychology, 57(3), 685-717. https://doi.org/10.1111/j.1744-6570.2004.00004.x

Curran, P. G. (2016). Methods for the detection of carelessly invalid responses in survey data.
Journal of Experimental Social Psychology, 66, 4-19.
https://doi.org/10.1016/j.jesp.2015.07.006
Darke, P. R., & Ritchie, R. J. (2007). The defensive consumer: Advertising deception, defensive
processing, and distrust. Journal of Marketing Research, 44(1), 114-127.
https://doi.org/10.1509/jmkr.44.1.114
DeSimone, J. A., Harms, P. D., & DeSimone, A. J. (2015). Best practice recommendations for
data screening. Journal of Organizational Behavior, 36(2), 171-181.
https://doi.org/10.1002/job.1962
Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). Bert: Pre-training of deep
bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805.
https://doi.org/10.48550/arXiv.1810.04805
Domingos, P. (1999). The role of Occam's razor in knowledge discovery. Data Mining and
Knowledge Discovery, 3, 409-425. https://doi.org/10.1023/A:1009868929893
Donnellan, M. B., Oswald, F. L., Baird, B. M., & Lucas, R. E. (2006). The mini-IPIP scales:
Tiny-yet-effective measures of the Big Five factors of personality. Psychological
Assessment, 18(2), 192. https://doi.org/10.1037/1040-3590.18.2.192
Eagly, A. H., & Chaiken, S. (2007). The advantages of an inclusive definition of attitude. Social
Cognition, 25(5), 582. https://doi.org/10.1521/soco.2007.25.5.582
Eagly, A. H., Chaiken, S., Gilbert, D. T., Fiske, S. T., & Lindzey, G. (1998). Attitude structure
and function. In Gilbert, D. T., Fiske, S. T., & Lindzey, G. (Eds.), The handbook of social
psychology (Vol.1). (pp. 269-322). Oxford University Press.

Ehrhart, K. H., Mayer, D. M., & Ziegert, J. C. (2012). Web-based recruitment in the Millennial
generation: Work–life balance, website usability, and organizational attraction. European
Journal of Work and Organizational Psychology, 21(6), 850-874.
https://doi.org/10.1080/1359432X.2011.598652
Engstrom, C. L., Petre, J. T., & Petre, E. A. (2017). Rhetorical analysis of fast-growth
businesses’ job advertisements: Implications for job search. Business and Professional
Communication Quarterly, 80(3), 336-364. https://doi.org/10.1177/2329490617723117
Faliagka, E., Ramantas, K., Tsakalidis, A., & Tzimas, G. (2012, May). Application of machine
learning algorithms to an online recruitment system. In Proc. International Conference
on Internet and Web Applications and Services (pp. 215-220).
Farida, S. (2010). The impact of information specificity in recruitment advertisements on the
application pursuit process in pakistan. African Journal of Business Management, 4(15),
3315-3320.
Feldman, D. C., Bearden, W. O., & Hardesty, D. M. (2006). Varying the content of job
advertisements: The effects of message specificity. Journal of Advertising, 35(1), 123141. https://doi.org/10.2753/JOA0091-3367350108
Finkelstein-Landau, M., & Morin, E. (1999, May). Extracting semantic relationships between
terms: Supervised vs. unsupervised methods. In International Workshop on Ontological
Engineering on the Global Information Infrastructure (pp. 71-80).
Fishbein, M., & Ajzen, I. (1974). Attitudes towards objects as predictors of single and multiple
behavioral criteria. Psychological Review, 81(1), 59. https://doi.org/10.1037/h0035872

Fisher, G. G., Matthews, R. A., & Gibbons, A. M. (2016). Developing and investigating the use
of single-item measures in organizational research. Journal of Occupational Health
Psychology, 21(1), 3. https://doi.org/10.1037/a0039139
Furnham, A., & Taylor, J. (2004). The dark side of behaviour at work: Understanding and
avoiding employees leaving, thieving and deceiving. Springer.
Gaeth, G. J., & Heath, T. B. (1987). The cognitive processing of misleading advertising in young
and old adults: Assessment and training. Journal of Consumer Research, 14(1), 43-54.
https://doi.org/10.1086/209091
Gardner, D. M. (1975). Deception in Advertising: A Conceptual Approach. Journal of
Marketing, 39(1), 40-46. https://doi.org/10.1177/002224297503900107
Gardner, D. M. (1976). Deception in advertising: a receiver oriented approach to understanding.
Journal of Advertising, 5(4), 5-19. https://doi.org/10.1080/00913367.1976.10672657
Gatewood, R. D., Gowan, M. A., & Lautenschlager, G. J. (1993). Corporate image, recruitment
image and initial job choice decisions. Academy of Management Journal, 36(2), 414-427.
https://doi.org/10.5465/256530
Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF
procedure. arXiv preprint. https://doi.org/10.48550/arXiv.2203.05794
Haefner, J. E. (1972). The legal versus the behavioral meaning of deception. Proceedings of the
Third Annual Conference of the Association for Consumer Research, Chicago, IL, 356360.
Harris, R. J. (1977). Comprehension of pragmatic implications in advertising. Journal of Applied
Psychology, 62(5), 603. https://doi.org/10.1037/0021-9010.62.5.603

Held, J., & Germelmann, C. C. (2018). Deception in consumer behavior research: A literature
review on objective and perceived deception. Projectics/Proyéctica/Projectique, 21(3),
119-145. https://www.doi.org/10.3917/proj.021.0119
Highhouse, S., Beadle, D., Gallo, A., & Miller, L. (1998). Get'em while they last! Effects of
scarcity information in job advertisements. Journal of Applied Social Psychology, 28(9),
779-795. https://doi.org/10.1111/j.1559-1816.1998.tb01731.x
Highhouse, S., Hoffman, J. R., Greve, E. M., & Collins, A. E. (2002). Persuasive impact of
organizational value statements in a recruitment context. Journal of Applied Social
Psychology, 32(8), 1737-1755. https://doi.org/10.1111/j.1559-1816.2002.tb02773.
Highhouse, S., Lievens, F., & Sinar, E. F. (2003). Measuring attraction to organizations.
Educational and Psychological Measurement, 63(6), 986-1001.
https://doi.org/10.1177/0013164403258403
Highhouse, S., Stierwalt, S. L., Bachiochi, P., Elder, A. E., & Fisher, G. (1999). Effects of
advertised human resource management practices on attraction of african american
applicants. Personnel Psychology, 52(2), 425-442. https://doi.org/10.1111/j.17446570.1999.tb00167.x
Huebner, A., & Lucht, M. (2019). Generalizability theory in R. Practical Assessment, Research,
and Evaluation, 24(1), 5. https://doi.org/10.7275/5065-gc10
Indeed Hiring Lab. (2022). State of the labor market. Indeed.com.
https://www.hiringlab.org/2022/03/09/january-2022-jolts-report/
Jansen, B. J., Jansen, K. J., & Spink, A. (2005). Using the web to look for work: Implications
for online job seeking and recruiting. Internet Research.
https://doi.org/10.1108/10662240510577068

Jedidi, K., Jagpal, H. S., & DeSarbo, W. S. (1997). Finite-mixture structural equation models
for response-based segmentation and unobserved heterogeneity. Marketing Science,
16(1), 39-59. https://doi.org/10.1287/mksc.16.1.39
Johar, J. S., & Sirgy, M. J. (1991). Value-expressive versus utilitarian advertising appeals: When
and why to use which appeal. Journal of Advertising, 20(3), 23-33.
https://doi.org/10.1080/00913367.1991.10673345
Karim, M. M., Bhuiyan, M. Y. A., Nath, S. K. D., & Latif, W. B. (2021). Conceptual Framework
of Recruitment and Selection Process. International Journal of Business and Social
Research, 11(02), 18-25. https://doi.org/10.18533/ijbsr.v11i02.1415
Khan, N. R., Awang, M., & Ghouri, A. M. (2013). Impact of e-recruitment and job-seekers
perception on intention to pursue the jobs. Management & Marketing, 11(1), 47-57.
Kim, J., & Angnakoon, P. (2016). Research using job advertisements: A methodological
assessment. Library & Information Science Research, 38(4), 327-335.
https://doi.org/10.1016/j.lisr.2016.11.006
Kim, M. S., & Hunter, J. E. (1993). Relationships among attitudes, behavioral intentions, and
behavior: A meta-analysis of past research, part 2. Communication Research, 20(3),
331-364. https://doi.org/10.1177/009365093020003001
Kossek, E. E., Baltes, B. B., & Matthews, R. A. (2011). Focal article. How work–family research
can finally have an impact in the workplace. Industrial and Organizational Psychology:
Perspectives on Science and Practice, 4, 352-369. https://doi.org/10.1111/j.17549434.2011.01353.x
Kozlowski, S. W. J., & Klein, K. J. (2000). A multilevel approach to theory and research in
organizations: Contextual, temporal, and emergent processes. In K. J. Klein & S. W. J.

Kozlowski (Eds.), Multilevel Theory, Research and Methods in Organizations:
Foundations, Extensions, and New Directions. 3-90. San Francisco, CA: Jossey-Bass.
LeBreton, J. M., & Senter, J. L. (2008). Answers to 20 questions about interrater reliability and
interrater agreement. Organizational Research Methods, 11(4), 815-852.
https://doi.org/10.1177/1094428106296642
Lee, C. H., Hwang, F. M., & Yeh, Y. C. (2013). The impact of publicity and subsequent
intervention in recruitment advertising on job searching freshmen's attraction to an
organization and job pursuit intention. Journal of Applied Social Psychology, 43(1), 113. https://doi.org/10.1111/j.1559-1816.2012.00975.x
Magidson, J., & Vermunt, J. K. (2004). Latent class models. The Sage Handbook of Quantitative
Methodology for the Social Sciences, 175-198.
Marks, L. J., & Kamins, M. A. (1988). The use of product sampling and advertising: Effects of
sequence of exposure and degree of advertising claim exaggeration on consumers’ belief
strength, belief confidence, and attitudes. Journal of Marketing Research, 25(3), 266281. https://doi.org/10.1177/002224378802500304
Markowitz, D. M., & Hancock, J. T. (2019). Deception and language: The contextual
organization of language and deception (COLD) framework. In The Palgrave handbook
of deceptive communication (pp. 193-212). Palgrave Macmillan, Cham.
Matsumoto, D., Hwang, H. C., & Sandoval, V. A. (2015). Cross-language applicability of
linguistic features associated with veracity and deception. Journal of Police and
Criminal Psychology, 30(4), 229-241. https://doi.org/10.1007/s11896-014-9155-0
Matsumoto, D., Hwang, H. S., Skinner, L., & Frank, M. (2011). Evaluating truthfulness and
detecting deception. FBI Law Enforcement Bulletin, 80, 1.

Matthews, R. A., Pineault, L., & Hong, Y. H. (2022). Normalizing the use of single-item
measures: Validation of the single-item compendium for organizational psychology.
Journal of Business and Psychology, 37(4), 639-673. https://doi.org/10.1007/s10869022-09813-3
Maurer, S. D., & Liu, Y. (2007). Developing effective e-recruiting websites: Insights for
managers from marketers. Business Horizons, 50(4), 305-314.
https://doi.org/10.1016/j.bushor.2007.01.002
Meade, A. W., & Craig, S. B. (2012). Identifying careless responses in survey data. Psychological
Methods, 17(3), 437. https://doi.org/10.1037/a0028085
Mehdi, C. (2021, December 5). LDA, NMF, Top2Vec, and BERTopic. How do they work?.
Medium.com. https://medium.com/@mehdi_chebbah/lda-nmf-top2vec-and-bertopichow-do-they-work-d71b6365a3d7
Meng, Y., Zhang, Y., Huang, J., Zhang, Y., & Han, J. (2022, April). Topic discovery via latent
space clustering of pretrained language model representations. In Proceedings of the
ACM Web Conference 2022 (pp. 3143-3152). https://doi.org/10.1145/3485447.3512034
Mitchell, A. A., & Olson, J. C. (1977). Cognitive effects of advertising repetition. Advances in
Consumer Research, 4(1), 213-220.
Mitra, A., Raymond, M. A., & Hopkins, C. D. (2008). Can consumers recognize misleading
advertising content in a media rich online environment?. Psychology & Marketing, 25(7),
655-674. https://doi.org/10.1002/mar.20230
Molnar, C. (2020). Interpretable machine learning. Lulu.com. chromeextension://efaidnbmnnnibpcajpcglclefindmkaj/https://originalstatic.aminer.cn/misc/pdf/
Molnar-interpretable-machine-learning_compressed.pdf

Monteiro, S., Sullivan, G. M., & Chan, T. M. (2019). Generalizability theory made simple (r): an
introductory primer to G-studies. Journal of Graduate Medical Education, 11(4), 365370. https://doi.org/10.4300/JGME-D-19-00464.1
Moore, C. T. (2016). gtheory: Apply Generalizability Theory with R. R package version 0.1.2.
Retrieved 3/10/2023 from https://cran.r-project.org/web/packages/gtheory/index.html
Morewedge, C. K., & Kahneman, D. (2010). Associative processes in intuitive judgment. Trends
in Cognitive Sciences, 14(10), 435-440. https://doi.org/10.1016/j.tics.2010.07.004
Morin, A. J., Bujacz, A., & Gagné, M. (2018). Person-centered methodologies in the
organizational sciences: Introduction to the feature topic. Organizational Research
Methods, 21(4), 803-813. https://doi.org/10.1177/1094428118773856
Muthén, L. K., & Muthén, B. O. (1998-2010). Growth modeling with latent variables using
Mplus: Advanced growth models, survival analysis and missing data. Mplus short
courses.
Muthén, L. K., & Muthén, B. O. (2002). How to use a Monte Carlo study to decide on sample
size and determine power. Structural Equation Modeling, 9(4), 599-620.
https://doi.org/10.1207/S15328007SEM0904_8
1DJ\06  8VLQJDVLQJOHဨLWHPDSSURDFKWRPHDVXUHIDFHWMREVDWLVIDFWLRQJournal of
Occupational and Organizational Psychology, 75(1), 77-86.
https://doi.org/10.1348/096317902167658
Nath, D., & Gardner, D. M. (1986). Is there a theory of deception in advertising?. BEBR Faculty
Working Paper; 1296.

Newman, M. L., Pennebaker, J. W., Berry, D. S., & Richards, J. M. (2003). Lying words:
Predicting deception from linguistic styles. Personality and Social Psychology Bulletin,
29(5), 665-675. https://doi.org/10.1177/0146167203029005010
Nindyati, O., & Nugraha, I. G. B. B. (2019, November). Detecting scam in online job vacancy
using behavioral features extraction. In 2019 International Conference on ICT for Smart
Society (ICISS) (Vol. 7, pp. 1-4). IEEE.
https://doi.org/10.1109/ICISS48059.2019.8969842
Nylund, K. L., Asparouhov, T., & Muthén, B. O. (2007). Deciding on the number of classes in
latent class analysis and growth mixture modeling: A Monte Carlo simulation study.
Structural Equation Modeling: A Multidisciplinary Journal, 14(4), 535-569.
https://doi.org/10.1080/10705510701575396
Oliver, R. L. (1979). An interpretation of the attitudinal and behavioral effects of puffery.
Journal of Consumer Affairs, 13(1), 8-27. https://doi.org/10.1111/j.17456606.1979.tb00124.x
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., ... & Lowe, R. (2022).
Training language models to follow instructions with human feedback. Advances in
Neural Information Processing Systems, 35, 27730-27744.
https://doi.org/10.48550/arXiv.2203.02155
Pastor, D. A., Barron, K. E., Miller, B. J., & Davis, S. L. (2007). A latent profile analysis of
college students’ achievement goal orientation. Contemporary Educational Psychology,
32(1), 8-47. https://doi.org/10.1016/j.cedpsych.2006.10.003

Peugh, J., & Fan, X. (2013). Modeling unobserved heterogeneity using latent profile analysis: A
Monte Carlo simulation. Structural Equation Modeling: A Multidisciplinary Journal,
20(4), 616-639. https://doi.org/10.1080/10705511.2013.824780
Powell, C. A. (2021, November 11). Internet full backs redditor who called out companies that
false advertise pay rates. Newsweek: Culture. https://www.newsweek.com/internet-fullybacks-redditor-who-called-out-companies-that-false-advertise-pay-rates-1653154
Putka, D. J., Le, H., McCloy, R. A., & Diaz, T. (2008). Ill-structured measurement designs in
organizational research: Implications for estimating interrater reliability. Journal of
Applied Psychology, 93(5), 959. https://doi.org/10.1037/0021-9010.93.5.959
Reddy, D. J. M., Regella, S., & Seelam, S. R. (2020, October). Recruitment prediction using
machine learning. In 2020 5th International Conference on Computing, Communication
and Security (ICCCS), (pp. 1-4). IEEE.
https://doi.org/10.1109/ICCCS49678.2020.9276955.
Rindova, V. P., & Fombrun, C. J. (1999). Constructing competitive advantage: The role of firm–
constituent interactions. Strategic Management Journal, 20(8), 691-710.
https://doi.org/10.1002/(SICI)1097-0266(199908)20:8<691::AID-SMJ48>3.0.CO;2-1
Roberson, Q. M., Collins, C. J., & Oreg, S. (2005). The effects of recruitment message
specificity on applicant attraction to organizations. Journal of Business and Psychology,
19(3), 319-339. https://doi.org/10.1007/s10869-004-2231-1
Roeder, K., & Wasserman, L. (1997). Practical Bayesian density estimation using mixtures of
normals. Journal of the American Statistical Association, 92(439), 894-902.
https://doi.org/10.1080/01621459.1997.10474044

Román, S. (2010). Relational consequences of perceived deception in online shopping: The
moderating roles of type of product, consumer’s attitude toward the internet and
consumer’s demographics. Journal of Business Ethics, 95(3), 373-391.
https://doi.org/10.1007/s10551-010-0365-9
Rosenberg, J. M., Beymer, P. N., Anderson, D. J., Van Lissa, C. J., & Schmidt, J. A. (2018).
tidyLPA: An R package to easily carry out latent profile analysis (LPA) using opensource or commercial software. Journal of Open Source Software, 3(30), 978,
https://doi.org/10.21105/joss.00978
Rozario, S. D., Venkatraman, S., & Abbas, A. (2019). Challenges in recruitment and selection
process: An empirical study. Challenges, 10(2), 35.
https://doi.org/10.3390/challe10020035
Ryan, L. (2017, June 10). Five sneaky ways employers mislead job seekers. Forbes.
https://www.forbes.com/sites/lizryan/2017/06/10/five-sneaky-ways-employers-misleadjob-seekers/?sh=1646552a3590
Rynes, S. L., & Cable, D. M. (2003). Recruitment research in the twenty-first century. In
Borman, W. C., Ilgen D. R., Klimoski, R. J. (Eds.), Handbook of Psychology: Industrial
and Organizational Psychology, 12, (pp. 55-76). John Wiley & Sons, Inc.
Saks, A. M.(2006). Antecedents and Consequences of Employee Engagement. Journal of
Managerial Psychology, 21(7), (pp. 600-619).
https://doi.org/10.1108/02683940610690169
Schafer, J. L. (1997). Analysis of incomplete multivariate data. CRC press.
Schweyer, A. (2004). Talent management systems: Best practices in technology solutions for
recruitment, retention and workforce planning. John Wiley & Sons.

Sia, S., Dalmia, A., & Mielke, S. J. (2020). Tired of topic models? clusters of pretrained word
embeddings make for fast and good topics too!. arXiv preprint arXiv:2004.14914.
https://doi.org/10.48550/arXiv.2004.14914
Sivertzen, A. M., Nilsen, E. R., & Olafsen, A. H. (2013). Employer branding: employer
attractiveness and the use of social media. Journal of Product & Brand Management.
https://doi.org/10.1108/JPBM-09-2013-0393
Spurk, D., Hirschi, A., Wang, M., Valero, D., & Kauffeld, S. (2020). Latent profile analysis: A
review and “how to” guide of its application within vocational behavior research. Journal
of Vocational Behavior, 120, 103445. https://doi.org/10.1016/j.jvb.2020.103445
Stafford, M. R. (2005). International services advertising (ISA): Defining the domain and
reviewing the literature. Journal of Advertising, 34(1), 65-86.
https://doi.org/10.1080/00913367.2005.10639184
Staw, B. M., Bell, N. E., & Clausen, J. A. (1986). The dispositional approach to job attitudes: A
lifetime longitudinal test. Administrative Science Quarterly, 56-77.
https://doi.org/10.2307/2392766
Stepchenkova, S., & Park, H. (2021). Authenticity orientation as an attitude: Scale construction
and validation. Tourism Management, 83, 104249.
https://doi.org/10.1016/j.tourman.2020.104249
Stiennon, N., Ouyang, L., Wu, J., Ziegler, D. M., Lowe, R., Voss, C., ... & Christiano, P. (2020).
Learning to summarize from human feedback. arXiv preprint arXiv:2009.01325.
https://dl.acm.org/doi/abs/10.5555/3495724.3495977

Storme, M., Myszkowski, N., Davila, A., & Bournois, F. (2015). How subjective processing
fluency predicts attitudes toward visual advertisements and purchase intention. Journal of
Consumer Marketing. https://doi.org/10.1108/JCM-10-2014-1187
Sweller, J., Van Merrienboer, J. J., & Paas, F. G. (1998). Cognitive architecture and instructional
design. Educational psychology review, 251-296.
https://doi.org/10.1023/A:1022193728205
Taylor, H. C., & Russell, J. T. (1939). The relationship of validity coefficients to the practical
effectiveness of tests in selection: Discussion and tables. Journal of Applied Psychology,
23(5), 565. https://doi.org/10.1037/h0057079
Toma, C. L., & Hancock, J. T. (2012). What lies beneath: The linguistic traces of deception in
online dating profiles. Journal of Communication, 62(1), 78-97.
https://doi.org/10.1111/j.1460-2466.2011.01619.x
Turban, D. B., Eyring, A. R., & Campion, J. E. (1993). Job attributes: Preferences compared
with reasons given for accepting and rejecting job offers. Journal of Occupational and
Organizational Psychology, 66(1), 71-81. https://doi.org/10.1111/j.20448325.1993.tb00517.x
U.S. Bureau of Labor Statistics. (2022). Labor force statistics from the current population
survey. https://www.bls.gov/cps/cpsaat08.htm
van Buuren, S., & Groothuis-Oudshoorn, K. (2011). mice: Multivariate imputation by chained
equations in R. Journal of Statistical Software, 45(3), 1-67.
https://doi.org/10.18637/jss.v045.i03

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I.
(2017). Attention is all you need. Advances in Neural Information Processing Systems,
30. https://doi.org/10.48550/arXiv.1706.03762
Verbree, A. R., Toepoel, V., & Perada, D. (2020). The effect of seriousness and device use on
data quality. Social Science Computer Review, 38(6), 720-738.
https://doi.org/10.1177/0894439319841027
Verwaeren, B., Van Hoye, G., & Baeten, X. (2017). Getting bang for your buck: The specificity
of compensation and benefits information in job advertisements. The International
Journal of Human Resource Management, 28(19), 2811-2830.
https://doi.org/10.1080/09585192.2016.1138989
Vidros, S., Kolias, C., Kambourakis, G., & Akoglu, L. (2017). Automatic detection of online
recruitment frauds: Characteristics, methods, and a public dataset. Future Internet, 9(1),
6. https://doi.org/10.3390/fi9010006
Walker, H. J., Feild, H. S., Giles, W. F., & Bernerth, J. B. (2008). The interactive effects of job
advertisement characteristics and applicant experience on reactions to recruitment
messages. Journal of Occupational and Organizational Psychology, 81(4), 619-638.
https://doi.org/10.1348/096317907X252487
Wang, K., Reimers, N., & Gurevych, I. (2021). Tsdae: Using transformer-based sequential
denoising auto-encoder for unsupervised sentence embedding learning. arXiv preprint.
https://doi.org/10.48550/arXiv.2104.06979
Wanous, J. P., Reichers, A. E., & Hudy, M. J. (1997). Overall job satisfaction: How good are
single-item measures?. Journal of Applied Psychology, 82(2), 247.
https://doi.org/10.1037/0021-9010.82.2.247

White, J., Stafford, J., & Beaver, J. (2019). Toward more effective recruitment of millennials
according to job interest: a comparison of job titles versus job action statements.
International Journal of the Academic Business World, 13(1), 1.
Wolf, E. J., Harrington, K. M., Clark, S. L., & Miller, M. W. (2013). Sample size requirements
for structural equation models: An evaluation of power, bias, and solution propriety.
Educational and psychological measurement, 73(6), 913-934.
https://doi.org/10.1177/0013164413495237
Wong, K. (2022, May 5). Tiktoker calls out ‘misleading’ job listing for advertising $13 an hour–
When they pay barely minimum wage. Daily Dot.
https://www.dailydot.com/irl/minimum-wage-misleading-barista/
Woo, S. E., Jebb, A. T., Tay, L., & Parrigon, S. (2018). Putting the “person” in the center:
Review and synthesis of person-centered approaches and methods in organizational
science. Organizational Research Methods, 21(4), 814-845.
https://doi.org/10.1177/1094428117752467
Yu, W., Jiang, Z., Chen, F., Hou, Q., & Feng, J. (2021). LV-BERT: Exploiting layer variety for
BERT. arXiv preprint. https://doi.org/10.48550/arXiv.2106.11740
Yüce, P., & Highhouse, S. (1998). Effects of attribute set size and pay ambiguity on reactions to
‘help wanted’ advertisements. Journal of Organizational Behavior, 19(4), 337-352.
https://doi.org/10.1002/(SICI)1099-1379(199807)19:4<337::AID-JOB848>3.0.CO;2-V
Zottoli, M. A., & Wanous, J. P. (2000). Recruitment source research: Current status and future
directions. Human Resource Management Review, 10(4), 353-382.
https://doi.org/10.1016/S1053-4822(00)00032-2

Zusman, R. R., & Landis, R. S. (2002). Applicant preferences for web-based versus traditional
job postings. Computers in Human behavior, 18(3), 285-296.
https://doi.org/10.1016/S0747-5632(01)00046-2

## Appendix A - Survey Measures

### Appendix A1: Selection of U.S. Bureau of Labor Statistics Industry (2022)

What industry is your job position in?
[ ] Natural Resources and Mining
[ ] Construction
[ ] Manufacturing
[ ] Trade, Transportation, and Utilities
[ ] Information
[ ] Finance
[ ] Business Services
[ ] Education
[ ] Healthcare
[ ] Hospitality and Food Service
[ ] Other ________________

### Appendix A2: Attitude Scale based on Eagly et al., (1998)

Indicate the level to which you agree with the following statement:
I like the job advertisement/posting in the link I provided above.
Strongly
disagree

Disagree

Slightly
Disagree

Neither
Agree
nor
Disagree

Slightly
Agree

Agree

Strongly
Agree

[]

[]

[]

[]

[]

[]

[]

### Appendix A3: Job Advertisement Deception Scale based on Haefner (1972)

Indicate the level to which you agree with the following statement:
I feel the job advertisement/posting in the link I provided above is deceiving.
By deceiving we mean:
Ɣ The job advertisement/posting describes the job or organization/company in a
way that seems too good to be true.
Ɣ The job advertisement/posting seems misleading or makes claims about the job
that are unbelievable.
Ɣ The job advertisement/posting seems to be offering a job that will look different
while actually working the job than how the job is described in the
advertisement/posting.
Ɣ The job advertisement/posting includes unrealistic expectations for the
applicant.
Strongly
Disagree

Disagree

Slightly
Disagree

Neither
Agree nor
Disagree

Slightly
Agree

Agree

Strongly
Agree

[]

[]

[]

[]

[]

[]

[]

### Appendix A4: Intent to Apply Scale (Straw et al., 1986)

Indicate the level to which you agree with the following statement:
I would apply to the job advertisement/posting in the link I provided above.
Strongly
Disagree

Disagree

Slightly
Disagree

Neither
Agree nor
Disagree

Slightly
Agree

Agree

Strongly
Agree

[]

[]

[]

[]

[]

[]

[]

### Appendix A5: Job Advertisement Deception Scale for Dimensions based on Haefner (1972)

Rate the extent to which each of the following job dimensions found in the above job advertisement/posting seems to
provide information about the job or company in a deceptive way.
Provide a rating from “Strongly Disagree” to “Strongly Agree” for each section of the job advertisement/posting.
With “Strongly Disagree” being that the information seems very accurate and “Strongly Agree” being that the
information seems very deceptive.
If any of the following job dimensions are not included in the job advertisement/posting, please select “Not
Applicable”.
Job Dimension

Strongly
Disagree

Disagree

Slightly
Disagree

Neither
Agree nor
Disagree

Slightly
Agree

Agree

Strongly
Agree

Not
Applicable

Job Description

[]

[]

[]

[]

[]

[]

[]

[]

Overview of the
Company

[]

[]

[]

[]

[]

[]

[]

[]

Salary/Pay

[]

[]

[]

[]

[]

[]

[]

[]

Benefits

[]

[]

[]

[]

[]

[]

[]

[]

Responsibilities/
Duties

[]

[]

[]

[]

[]

[]

[]

[]

Skills

[]

[]

[]

[]

[]

[]

[]

[]

Qualifications

[]

[]

[]

[]

[]

[]

[]

[]

Schedule

[]

[]

[]

[]

[]

[]

[]

[]

Education

[]

[]

[]

[]

[]

[]

[]

[]

Experience

[]

[]

[]

[]

[]

[]

[]

[]

Work Location

[]

[]

[]

[]

[]

[]

[]

[]

Other:
__________

[]

[]

[]

[]

[]

[]

[]

[]

### Appendix A6: Mini-IPIP Scale for Personality (Donnellan et al., 2006)

Describe yourself as you generally are now, not as you wish to be in the future. Describe
yourself as you honestly see yourself, in relation to other people you know of the same sex as
you, and roughly your same age.
Indicate for each statement, whether it is: “Very Inaccurate”, “Moderately Inaccurate”, “Neither
Accurate Nor Inaccurate”, “Moderately Accurate”, or “Very Accurate” as a description of you.
Very
Inaccurate

Moderately
Inaccurate

Neither
Accurate
nor
Inaccurate

Moderately
Accurate

Very
Accurate

I am the life of the party.

[]

[]

[]

[]

[]

I sympathize with others’
feelings.

[]

[]

[]

[]

[]

I get chores done right
away.

[]

[]

[]

[]

[]

I have frequent mood
swings.

[]

[]

[]

[]

[]

I have a vivid
imagination.

[]

[]

[]

[]

[]

I don’t talk a lot.

[]

[]

[]

[]

[]

I am not interested in
other people’s problems.

[]

[]

[]

[]

[]

I often forget to put
things back in their
proper place.

[]

[]

[]

[]

[]

I am relaxed most of the
time.

[]

[]

[]

[]

[]

I am not interested in
abstract ideas.

[]

[]

[]

[]

[]

I talk to a lot of different
people at parties.

[]

[]

[]

[]

[]

I feel others’ emotions.

[]

[]

[]

[]

[]

I like order.

[]

[]

[]

[]

[]

I get upset easily.

[]

[]

[]

[]

[]

I have difficulty
understanding abstract
ideas.

[]

[]

[]

[]

[]

I keep in the background.

[]

[]

[]

[]

[]

I am not really interested
in others.

[]

[]

[]

[]

[]

I make a mess of things.

[]

[]

[]

[]

[]

I seldom feel blue.

[]

[]

[]

[]

[]

I do not have a good
imagination.

[]

[]

[]

[]

[]

### Appendix A7: Job Advertisement Deception Rating per Dimension

Job Description:
Indicate the level to which you agree with the statement in bold below. With
“Strongly Agree” meaning it seems deceptive or misleading and “Strongly Disagree”
meaning it seems authentic.
“I feel the information provided about the job description in the job
advertisement is deceptive or misleading.”
Strongly
Disagree

Disagree

Slightly
Disagree

Neither
Agree nor
Disagree

Slightly
Agree

Agree

Strongly
Agree

[]

[]

[]

[]

[]

[]

[]

Please provide your reasoning for your selected response in the box below.

Note. This item shows the single item deception scale used for the job advertisement dimension
of “job description”. This item was repeated for each job advertisement and changed to inquire
about each job dimensions. The other 10 job dimensions (a total of 11) that were asked about
(replacing the job description text in the item above) were: Overview of company, Salary,
Benefits, Responsibilities/Duties, Skills, Qualifications, Schedule, Education, Experience, and
Work location.

### Appendix A8: Attention Check Items based on Synonymous Questions (Curran, 2016;

DeSimone et al., 2015; Meade & Craig, 2012)
Please select an answer to the following statement:
I am currently employed (not including school).
[ ] Yes

[ ] No

Please select an answer to the following statement:
I have a job right now (not including school).
[ ] Yes

[ ] No

Please select an answer to the following statement:
I currently work a job (not including school).
[ ] Yes

[ ] No

Please select an answer to the following statement:
At this time, I am employed (not including school).
[ ] Yes

[ ] No

### Appendix A9: Seriousness Check Item (Aust et al., 2013; Verbree et al., 2020)

It would be very helpful if you could tell us at this point whether you have taken part in
this survey seriously, so that we can use your answers for our scientific analyses, or
whether you were not providing a serious attempt at responding
[ ] Yes, I was responding seriously

[ ] No, I was not responding seriously

## Appendix B - Indeed Job Advertisements used in Study 3

### Appendix B1: Top 5 Deceptively Rated Job Advertisements from Study 2 used in Study 3

Deceptively Rated Job Advertisement 1 (Job advertisement #1)

Deceptively Rated Job Advertisement 2 (Job advertisement #2)

Deceptively Rated Job Advertisement 3 (Job advertisement #3)

Deceptively Rated Job Advertisement 4 (Job advertisement #4)

Deceptively Rated Job Advertisement 5 (Job advertisement #5)

### Appendix B2: Top 5 Authentically Rated Job Advertisements from Study 2 used in Study 3

Authenticity Rated Job Advertisement 1 (Job advertisement #6)

Authenticity Rated Job Advertisement 2 (Job advertisement #7)

Authenticity Rated Job Advertisement 3 (Job advertisement #8)

Authenticity Rated Job Advertisement 4 (Job advertisement #9)

Authenticity Rated Job Advertisement 5 (Job advertisement #10)

## Appendix C - Job Description Dimension Results

### Appendix C1: Latent Profile Analysis Results for Job Description Dimension

Table 3
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Job Description Dimension
Job Ad
\#

SD

3.0

1.8

3.0

1.8

0.254**

3.8

2.0

0.160

0.297**

2.4

1.7

0.280**

0.293**

0.273**

1.9

1.3

0.219*

0.247**

0.217*

0.569***

2.3

1.7

0.136

0.091

0.156

0.451*** 0.440***

2.4

1.4

0.243**

0.160

0.096

0.214*

0.221*

0.150

2.3

1.5

0.076

0.185*

0.181

0.262**

0.129

0.285**

0.240*

2.5

1.5

0.288**

0.097

0.245**

0.274**

0.162

0.198*

0.413***

0.278**

2.1

1.4

0.211*

0.286**

0.109

0.268**

0.238*

0.339***

0.260**

0.268**

0.285**

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 4
Latent Profile Enumeration Fit Statistics for Job Description Dimension
Model #

\# of
Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,146

4,332

4,386

4,323

0.00

NA

-2,058

4,179

4,263

4,165

175.00

0.010

-2,036

4,156

4,271

4,138

44.50

0.010

-2,146

4,332

4,386

4,323

0.00

NA

2*

-2,025

4,131

4,243

4,114

243.00

0.010

NA

NA

NA

NA

NA

NA

-2,035

4,199

4,377

4,172

0.00

NA

-1,998

4,148

4,356

4,116

73.30

0.010

-1,954

4,082

4,320

4,045

88.30

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying
mean. Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances
fixed to 0. Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information
criteria; BIC = Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped
log-likelihood ratio test. NA = indicates convergence issues during model estimation potentially due to model
misspecification for the data structure. Best fit model chosen from BIC due to balance of model fit and model
complexity.

Table 5
Summary of Variance Components and Generalizability Coefficients in G Study for Job Description
Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.610

20.9

–

Item (I)
(Job advertisement)

0.292

10.0

–

P X I (Residual)

2.030

69.1

–

Total

2.932

100.0

–
0.792

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 6
Percent of Sample by Profile and Means of Job Advertisements by Profile for Job Description Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Mildly Skeptical w/
Heightened
Awareness

84.2%

3.218

3.270

4.207

2.625

2.000

2.458

2.458

2.416

2.677

2.239

2. Overly Trusting

15.8%

1.555

1.556

1.724

1.441

1.332

1.276

1.780

1.668

1.555

1.388

Note. N = 114. Means are on a 1-7 scale.

### Appendix C2: Natural Language Processing Topic Analysis Results for Job Description Dimension

Table 7
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Job Description Dimension
Cluster #

Number of
Statements
per Clusters

Representative
Words

Summary

Cluster 1

deceptive

The job description is generally deceptive as a whole.

Cluster 2

lacks,
sufficient,
information

The job description information is inadequate, lacking sufficient details and
specific requirements, resulting in unclear and insufficient expectations and
responsibilities.

Cluster 3

good, true

The job description seems too good to be true.

Cluster 4

misleading

The job description is misleading.

Cluster 5

vague

The job description is vague.

Cluster 6

unclear,
responsibilities

The job description includes instances of unclear and misleading job
responsibilities, duties, and requirements, that require revision and clarification.

Cluster 7

unclear

The job description is unclear.

Cluster 8

confusing,
mentions,
fulltime,
parttime,
positions,
hours, listed,
indicate,
parttime

The job description is confusing and misleading, with contradictory information
about flexibility, scheduling, and required experience.

Cluster 9

job, misleading

The description is deceptive, misleading, and lacks important details such as pay
range and specific requirements, making them appear too good to be true.

Cluster 10

advertised,
The job titles and descriptions are misleading and lack clarity, causing confusion
counselors,
about the actual responsibilities and requirements of the positions.
actual, position,
dietitians

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the
following list that conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the
“list” referenced in the prompt.

Table 8
Top Words by Cluster Based on Word Count for Job Description Dimension
Cluster #

Top Word 1 Top Word 2 Top Word 3 Top Word 4 Top Word 5 Top Word 6 Top Word 7 Top Word 8 Top Word 9

Top Word

Cluster 1

deceptive
(100%)

–

–

–

–

–

–

–

–

–

Cluster 2

information
(17.8%)

details
(13.3%)

lacks
(11.1%)

brief
(11.1%)

sufficient
(11.1%)

lacked
(8.9%)

insufficient
(8.9%)

lack (8.9%)

unclear
(4.4%)

inadequate
(4.4%)

Cluster 3

good
(45.0%)

true
(45.0%)

appears
(10.0%)

–

–

–

–

–

–

–

Cluster 4

misleading
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 5

vague
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 6

unclear
(28.6%)

responsibilities (17.9%)

confusing
(12.5%)

misleading
(8.9%)

lacks
(7.1%)

duties
(7.1%)

mixologist
(5.4%)

requirement
s (5.4%)

clarity
(3.6%)

therapy
(3.6%)

Cluster 7

unclear
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 8

schedule
(14.3%)

flexible
(14.3%)

parttime
(14.3%)

work
(10.7%)

fulltime
(10.7%)

hours
(7.1%)

set (7.1%)

misleading
(7.1%)

confusing
(7.1%)

unclear
(7.1%)

Cluster 9

job (16.4%)

deceptive
(13.4%)

misleading
(13.4%)

good
(10.4%)

appears
(10.4%)

vague
(9.0%)

positive
(7.5%)

true (7.5%)

misleadingly (6.0%)

pay (6.0%)

Cluster 10

misleading
(16.0%)

counseling
(12.0%)

title
(12.0%)

food
(12.0%)

dietician
(8.0%)

position
(8.0%)

service
(8.0%)

responsibilit
ies (8.0%)

focuses
(8.0%)

baristas
(8.0%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix D - Company Overview Dimension Results

### Appendix D1: Latent Profile Analysis Results for Company Overview Dimension

Table 9
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Company Overview Dimension
Job Ad
\#

SD

2.7

1.6

3.4

1.8

0.254**

3.8

1.9

0.185*

0.118

2.8

1.8

0.364***

0.276**

0.340***

2.6

1.5

0.209*

0.276**

0.194*

0.181

2.8

1,8

0.315*** 0.328***

0.254**

0.387***

0.293**

2.9

1.7

0.317*** 0.483*** 0.324*** 0.423***

0.267*

0.365***

2.3

1.4

3.3

2.2

0.147

-0.012

0.158

0.224*

0.113

0.218*

1.8

0.310*** 0.374***

0.259**

0.254**

0.257**

0.495*** 0.458***

0.303**

1.5

0.222*

0.215*

0.417***

0.173

0.245**

0.323***

0.237*

0.265**

0.297**

0.253**

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 10
Latent Profile Enumeration Fit Statistics for Company Overview Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,198

4,435

4,490

4,427

0.00

NA

-2,105

4,271

4,356

4,258

186.00

0.010

-2,081

4,245

4,360

4,228

47.8

0.010

-2,198

4,435

4,490

4,427

0.00

NA

2*

-2,048

4,177

4,289

4,160

300.00

0.010

NA

NA

NA

NA

NA

NA

-2,071

4,272

4,450

4,245

0.00

NA

-2,035

4,222

4,430

4,190

72.0

0.010

-2,028

4,230

4,468

4,193

14.50

0.079

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying
mean. Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed
to 0. Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria;
BIC = Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood
ratio test. NA = indicates convergence issues during model estimation potentially due to model misspecification
for the data structure. Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 11
Summary of Variance Components and Generalizability Coefficients in G Study for Company Overview
Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.785

25.6

–

Item (I)
(Job advertisement)

0.227

7.4

–

P X I (Residual)

2.952

67.0

–

Total

3.964

100.0

–
0.734

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 12
Percent of Sample by Profile and Means of Job Advertisements by Profile for Company Overview Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Neutral but Aware
of Deception

58.8%

3.037

4.016

4.132

3.403

2.986

3.635

3.590

2.768

4.072

2.832

2. Trusting but
Occasionally
Suspicious

41.2%

2.216

2.388

3.248

1.926

1.984

1.465

1.841

1.520

2.215

1.269

Note. N = 114. Means are on a 1-7 scale.

### Appendix D2: Natural Language Processing Topic Analysis Results for Company Overview Dimension

Table 13
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Company Overview Dimension
Cluster #

Number of
Statements
per Clusters

Representative
Words

Summary

Cluster 1

misleading

The company overview contains misleading and deceptive information.

Cluster 2

unclear

The company overview has unclear information.

Cluster 3

lacking

The company overview lacks clear and sufficient information regarding its mission, goals,
values, and background, leading to inadequate beliefs and a lack of professionalism.

Cluster 4

did, provide,
information

The company information provided was not as informative and seems like a scam, with the
lack of a clear mission statement and confusing contact information.

Cluster 5

misleading, lacks, The provided information feels misleading and deceptive by the company, including a lack of
details, provide,
details, unclear information, and misrepresentation of responsibilities and requirements.
assistance

Cluster 6

lacks, information The provided information is insufficient and lacks relevant details.

Cluster 7

misleadingly,
positive

The information appears misleading, unclear, and unrealistic, with excessive use of
exclamation points and biased language, making it difficult to determine the true nature of the
positions offered.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the prompt.

Table 14
Top Words by Cluster Based on Word Count for Company Overview Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Cluster 1

misleading
(61.8%)

Cluster 2

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

deceptive
(38.2%)

–

–

–

–

–

–

–

–

unclear
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 3

lacks
(21.9%)

information
(20.3%)

lacked
(14.1%)

background
(9.4%)

lacking
(9.4%)

mission
(6.2%)

clear (4.7%)

inadequate
(4.7%)

sufficient
(4.7%)

goals
(4.7%)

Cluster 4

information
(20.0%)

provide
(20.0%)

provided
(10.0%)

like (10.0%)

scam
(10.0%)

informative
(10.0%)

strange
(5.0%)

foundation
(5.0%)

acronym
(5.0%)

doesn’t
(5.0%)

Cluster 5

information
(21.4%)

lacks
(17.1%)

misleading
(15.7%)

details
(8.6%)

lacked
(8.6%)

unclear
(7.1%)

deceptive
(5.7%)

given
(5.7%)

reason
(5.7%)

cdc (4.3%)

Cluster 6

information
(36.5%)

insufficient
(14.4%)

lacks
(13.5%)

provided
(12.5%)

lack (7.7%)

sufficient
(5.8%)

lacked
(4.8%)

details
(3.8%)

relevant
(1.0%)

–

Cluster 7

appears
(18.0%)

misleading
(12.0%)

unclear
(12.0%)

vague
(10.0%)

deceptive
(10.0%)

misleadingly (8.0%)

good (8.0%)

true (8.0%)

biased
(8.0%)

suspicious
(6.0%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix E - Salary Dimension Results

### Appendix E1: Latent Profile Analysis Results for Salary Dimension

Table 15
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Salary Dimension
Job Ad
\#

SD

4.1

1.8

2.8

1.7

0.345***

4.1

2.1

0.323***

0.196*

2.9

1.9

0.165

0.172

0.111

2.6

1.6

0.254**

0.281**

0.100

0.130

1.9

1.3

-0.054

0.214*

0.042

0.271*

0.216*

1.9

1.2

0.100

0.205*

0.137

0.340***

0.265**

0.400***

2.3

1.6

0.050

0.077

0.172

0.144

0.190*

0.187*

2.3

1.5

0.016

0.365***

0.163

0.203*

0.350*** 0.342*** 0.375***

0.266**

2.6

1.7

0.243**

0.305***

0.280**

0.130

0.259**

0.126

0.139

0.209*

0.278**

0.244**

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 16
Latent Profile Enumeration Fit Statistics for Salary Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,156

4,351

4,406

4,343

0.00

NA

-2,058

4,250

4,335

4,237

123.00

0.010

-2,057

4,197

4,312

4,180

74.70

0.010

-2,156

4,351

4,406

4,343

0.00

NA

2*

-2,040

4,161

4,274

4,144

232.00

0.010

NA

NA

NA

NA

NA

NA

-2,063

4,257

4,435

4,229

0.00

NA

-2,041

4,235

4,443

4,203

43.90

0.020

-2,032

4,239

4,477

4,202

18.2

0.495

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying mean.
Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed to 0.
Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria; BIC =
Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood ratio
test. NA = indicates convergence issues during model estimation potentially due to model misspecification for the
data structure. Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 17
Summary of Variance Components and Generalizability Coefficients in G Study for Salary Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.536

16.2

–

Item (I)
(Job advertisement)

0.577

17.5

–

P X I (Residual)

2.190

66.3

–

Total

3.303

100.0

–
0.838

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 18
Percent of Sample by Profile and Means of Job Advertisements by Profile for Salary Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Wary and Alert

77.2%

4.380

3.037

4.800

3.234

2.711

2.068

2.043

2.596

2.486

3.003

2. Generally Trusting

22.8%

3.031

1.927

1.529

1.713

2.041

1.371

1.416

1.338

1.762

1.416

Note. N = 114. Means are on a 1-7 scale.

### Appendix E2: Natural Language Processing Topic Analysis Results for Salary Dimension

Table 19
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Salary Dimension
Cluster #

Number of
Statements per
Clusters

Representative Words

Summary

Cluster 1

unclear, information

The salary information provided is unclear, misleading, and lacks specificity,
causing confusion and suspicion regarding accuracy and truthfulness.

Cluster 2

misleading

The salary information is misleading.

Cluster 3

salary, range, misleading

The salary information is broad, unclear, misleading, and incomplete, making it
difficult to accurately determine potential earnings and causing suspicion about the
accuracy and adequacy of the salaries listed.

Cluster 4

advertised, hour,
suspicious, potentially,
misleading

The salary information is misleading and potentially fraudulent, with unclear
payment timing and criteria, unrealistic salary ranges, and deceptive statements
about bonuses and raises, leading to suspicion and confusion among applicants.

Cluster 5

range, unclear,
unexplained

The salary information has a broad range that is unclear, leading to deception and
disappointment for potential employees, with significant variations and
inconsistencies depending on experience and other factors.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the prompt.

Table 20
Top Words by Cluster Based on Word Count for Salary Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

Cluster 1

unclear
(25.0%)

information
(21.2%)

misleading
(17.3%)

good (7.7%)

true (7.7%)

mention
(5.8%)

actual
(3.8%)

doesn’t
(3.8%)

accurate
(3.8%)

high (3.8%)

Cluster 2

misleading
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 3

salary
(39.6%)

range
(19.8%)

misleading
(10.9%)

broad
(7.9%)

appears
(5.9%)

disclosed
(4.0%)

unclear
(3.0%)

difficult
(3.0%)

determine
(3.0%)

potential
(3.0%)

Cluster 4

advertised
(17.2%)

range
(14.9%)

misleading
(14.9%)

deceptive
(9.7%)

hourly
(9.0%)

unclear
(9.0%)

hour (8.2%)

low (6.7%)

potential
(6.0%)

lower
(4.5%)

Cluster 5

range
(47.7%)

unclear
(18.0%)

broad
(10.9%)

misleading
(6.2%)

wide (4.7%)

deceptive
(3.9%)

inconsistent
(2.3%)

provided
(2.3%)

vague
(2.3%)

hour (1.6%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix F - Benefits Dimension Results

### Appendix F1: Latent Profile Analysis Results for Benefits Dimension

Table 21
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Benefits Dimension
Job Ad
\#

SD

2.9

1.7

2.6

1.8

0.169

3.9

1.9

0.027

0.236*

2.2

1.6

0.236*

0.426***

2.1

1.5

0.189*

0.403*** 0.309*** 0.394***

3.8

1.9

0.317***

-0.197*

-0.015

0.008

-0.093

3.1

1.8

0.145

0.119

0.288**

0.311***

0.107

0.149

4.3

1.6

0.072

-0.146

0.169

-0.073

-0.037

0.345***

0.177

2.5

1.5

0.230*

0.228*

0.249**

0.229*

0.344***

0.143

0.328***

0.127

3.3

1.8

0.204*

0.045

0.261**

0.193*

0.084

0.261**

0.256**

0.276**

0.270**

0.122

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 22
Latent Profile Enumeration Fit Statistics for Benefits Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,219

4,478

4,532

4,469

0.00

NA

-2,139

4,340

4,435

4,327

159.00

0.010

-2,123

4,330

4,445

4,312

32.30

0.010

-2,219

4,478

4,532

4,469

0.00

NA

2*

-2,062

4,207

4,319

4,189

313.0

0.010

NA

NA

NA

NA

NA

NA

-2,119

4,367

4,545

4,340

0.00

NA

-2,110

4,372

4,580

4,340

17.40

0.772

-2,098

4,371

4,609

4,334

23.40

0.446

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying
mean. Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed
to 0. Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria;
BIC = Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood
ratio test. NA = indicates convergence issues during model estimation potentially due to model misspecification
for the data structure. Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 23
Summary of Variance Components and Generalizability Coefficients in G Study for Benefits Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.506

14.6

–

Item (I)
(Job advertisement)

0.533

15.3

–

P X I (Residual)

2.432

70.1

–

Total

3.471

100.0

–
0.854

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 24
Percent of Sample by Profile and Means of Job Advertisements by Profile for Benefits Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Slightly Skeptical

43.0%

3.442

4.059

4.770

3.198

3.053

3.725

3.592

4.284

3.156

3.579

2. Fluctuating
Deception

57.0%

2.480

1.541

3.191

1.450

1.375

3.809

2.753

4.372

1.953

3.031

Note. N = 114. Means are on a 1-7 scale.

### Appendix F2: Natural Language Processing Topic Analysis Results for Benefits Dimension

Table 25
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Benefits Dimension
Cluster #

Number of
Statements
per Clusters

Representative
Words

Summary

Cluster 1

unclear, misleading

The company uses misleading and unclear language, lack of specific details, and focus on
COVID protocols instead of other important job details may cause confusion and deception
for employees, requiring changes to be made for transparency and accuracy.

Cluster 2

listed, flexible,
schedule, benefit,
deceptive

The company offers good benefits such as flexible scheduling and unlimited paid time off,
but many of the listed benefits are misleading or lack important information.

Cluster 3

deceptive,
advertised

The advertised benefits were often deceptive, misleading, and lacked important details,
causing doubts about the credibility of the company and leading to disappointment for many
applicants.

Cluster 4

listed

The benefits were not included or mentioned, some of those that were seemed odd.

Cluster 5

uniform, allowance

The benefit of “uniform allowance” is unclear and confusing, with some potentially
perceiving it as a deceptive benefit while others see it as a real and appealing standard
requirement, but there is a lack of clarity as to what it means.

Cluster 6

misleading

The job ad contains misleading information.

Cluster 7

lacked, information

There are various instances where information is lacking or insufficient, leading to
skepticism and a lack of clarity.

Cluster 8

unclear

The information provided is often unclear, vague, and lacking in specificity, with promised
details frequently undisclosed or missed, requiring revision or clarification.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the prompt.

Table 26
Top Words by Cluster Based on Word Count for Benefits Dimension
Cluster #

Top Word

Top Word

Top Word

Top Word

Top Word

Top Word

Top Word

Top Word

Top Word

Top Word

Cluster 1

misleading
(37.7%)

unclear
(17.4%)

person
(10.1%)

reason
(7.2%)

clear
(5.8%)

information time (4.3%)
(4.3%)

instead
(4.3%)

deceptive
(4.3%)

needed
(4.3%)

Cluster 2

flexible
(16.8%)

schedule
(13.7%)

time
(11.5%)

misleading
(9.9%)

insurance
(9.2%)

advertised
(8.4%)

benefit
(8.4%)

paid (8.4%)

good
(6.9%)

unlimited
(6.9%)

Cluster 3

advertised
(29.5%)

deceptive
(19.3%)

unrealistic
(11.4%)

misleading
(8.0%)

appear
(6.8%)

offered
(5.7%)

good
(5.7%)

person
(4.5%)

appeared
(4.5%)

true (4.5%)

Cluster 4

mentioned
(40.0%)

listed
(36.0%)

offered
(8.0%)

list (4.0%)

included
(4.0%)

considering
(4.0%)

odd (4.0%)

–

–

–

Cluster 5

uniform
(28.3%)

allowance
(28.3%)

benefit
(13.2%)

unclear
(5.7%)

don’t
(5.7%)

understand
(5.7%)

deceptive
(3.8%)

term (3.8%)

mentioned
(3.8%)

meaning
(1.9%)

Cluster 6

misleading
(66.7%)

agree
(33.3%)

–

–

–

–

–

–

–

–

Cluster 7

information
(28.3%)

lacked
(23.9%)

lacks
(13.0%)

lack (8.7%)

provided
(4.3%)

clarity
(4.3%)

details
(4.3%)

sufficient
(4.3%)

specific
(4.3%)

appear
(4.3%)

Cluster 8

unclear
(35.5%)

vague
(12.9%)

disclosed
(12.9%)

specified
(9.7%)

section
(6.5%)

provided
(6.5%)

promised
(6.5%)

insufficient
(3.2%)

offered
(3.2%)

minimal
(3.2%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix G - Responsibilities Dimension Results

### Appendix G1: Latent Profile Analysis Results for Responsibilities Dimension

Table 27
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Responsibilities Dimension
Job Ad
\#

SD

2.8

1.7

3.1

1.7

0.201*

4.0

1.8

-0.002

0.198*

2.3

1.6

0.314***

0.125

0.300**

2.1

1.4

0.145

0.323***

0.193*

0.458***

2.3

1.8

0.140

-0.031

0.036

0.121

2.2

1.4

0.140

0.244**

0.158

0.470*** 0.355***

0.072

2.5

1.5

0.198*

0.272**

0.140

0.330*** 0.376***

0.198*

0.154

2.1

1.3

0.178

0.237*

0.237*

0.428*** 0.325***

0.144

0.459***

1.9

1.1

0.264**

0.227*

0.271**

0.488*** 0.431*** 0.323*** 0.343*** 0.411*** 0.445***

0.162

0.271**

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 28
Latent Profile Enumeration Fit Statistics for Responsibilities Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,084

4,208

4,262

4,199

0.00

NA

2*

-1,994

4,050

4,134

4,036

180.00

0.010

-1,976

4,036

4,151

4,018

35.90

0.010

-2,084

4,208

4,262

4,199

0.00

NA

NA

NA

NA

NA

NA

NA

NA

NA

NA

NA

NA

NA

-1,959

4,047

4,225

4,020

0.00

NA

-1,924

4,001

4,209

3,969

68.50

0.010

-1,886

3,945

4,183

3,908

77.70

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying mean.
Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed to 0. Model 3
= equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria; BIC = Bayesian
information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood ratio test. NA =
indicates convergence issues during model estimation potentially due to model misspecification for the data structure.
Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 29
Summary of Variance Components and Generalizability Coefficients in G Study for Responsibilities
Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.542

19.6

–

Item (I)
(Job advertisement)

0.374

13.6

–

P X I (Residual)

1.841

66.8

–

Total

2.757

100.0

–
0.803

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 30
Percent of Sample by Profile and Means of Job Advertisements by Profile for Responsibilities Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Wavering
Deception

13.2%

4.289

4.011

5.261

5.327

3.653

3.018

4.030

4.003

3.566

3.152

2. Trusting but Aware

86.8%

2.575

2.994

3.762

1.784

1.802

2.186

1.946

2.275

1.877

1.708

Note. N = 114. Means are on a 1-7 scale.

### Appendix G2: Natural Language Processing Topic Analysis Results for Responsibilities Dimension

Table 31
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Responsibilities Dimension
Cluster #

Number of
Statements per
Clusters

Representative
Words

Summary

Cluster 1

unclear, provide,
The counselor position was misrepresented as primarily dealing with mental health,
information, tasks, but it actually focuses on dieticians and includes separate roles for counseling and
involved, early,
using ABA therapy for autistic children, with specific areas of counseling mentioned.
intervention,
therapy,
education,
leaving, applicant,
unsure, entails

Cluster 2

unclear,
misleading

The responsibilities contain unclear and misleading information.

Cluster 3

deceptive, unclear

The responsibilities listed contain misleading and unclear job descriptions with
unrealistic expectations, deceptive duties, and excessive or understated requirements,
making it difficult for applicants to understand the actual job and discouraging them
from applying.

Cluster 4

lacks, clear,
information

The information listed is unclear, misleading, and lacks specific details regarding
required duties and responsibilities.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list
that conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in
the prompt.

Table 32
Top Words by Cluster Based on Word Count for Responsibilities Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

Cluster 1

unclear
(15.4%)

counseling
(15.4%)

therapy
(11.5%)

counselor
(11.5%)

lacks (7.7%)

details
(7.7%)

use (7.7%)

autistic
(7.7%)

children
(7.7%)

position
(7.7%)

Cluster 2

misleading
(54.0%)

unclear
(46.0%)

–

–

–

–

–

–

–

–

Cluster 3

deceptive
(22.4%)

advertised
(16.5%)

listed
(12.9%)

misleading
(11.8%)

unclear
(9.4%)

vague
(7.1%)

list (5.9%)

unrealistic
(4.7%)

excessive
(4.7%)

mixologist
(4.7%)

Cluster 4

unclear
(22.2%)

lacks
(14.8%)

information
(12.3%)

lacked
(11.1%)

duties
(7.4%)

clear (7.4%)

misleading
(6.2%)

job (6.2%)

listed
(6.2%)

requirement
s (6.2%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix H - Skills Dimension Results

### Appendix H1: Latent Profile Analysis Results for Skills Dimension

Table 33
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Skills Dimension
Job Ad
\#

SD

2.9

1.6

3.6

1.8

0.221*

3.7

1.9

0.044

0.178

2.2

1.3

0.205*

0.205*

0.190*

2.2

1.5

0.045

0.259**

0.313*** 0.406***

2.1

1.4

0.048

0.117

2.9

1.7

0.424*** 0.356***

3.7

1.8

0.246**

3.3

1.7

0.273**

0.153

0.275**

2.2

1.7

0.033

0.137

0.133

0.060

0.224*

0.361***

0.184*

0.303**

0.262**

0.069

0.343*** 0.308***

0.146

0.279**

0.178

0.315***

0.054

0.203*

0.091

0.411*** 0.320***

0.375*** 0.315*** 0.343***

0.099

0.275**

0.006

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 34
Latent Profile Enumeration Fit Statistics for Skills Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,172

4,385

4,440

4,376

0.00

NA

-2,111

4,283

4,368

4,270

123.00

0.010

-2,052

4,187

4,302

4,169

118.00

0.010

-2,172

4,385

4,440

4,376

0.00

NA

-2,029

4,140

4,252

4,123

287.00

0.010

3*

-1,974

4,071

4,241

4,045

111.00

0.010

-2,065

4,259

4,437

4,232

0.00

NA

-2,045

4,242

4,450

4,210

39.6

0.030

-1,987

4,148

4,386

4,111

116.00

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying
mean. Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed
to 0. Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria;
BIC = Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood
ratio test. NA = indicates convergence issues during model estimation potentially due to model misspecification
for the data structure. Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 35
Summary of Variance Components and Generalizability Coefficients in G Study for Skills Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.592

18.7

–

Item (I)
(Job advertisement)

0.415

13.1

–

P X I (Residual)

2.154

68.1

–

Total

3.161

100.0

–
0.813

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 36
Percent of Sample by Profile and Means of Job Advertisements by Profile for Skills Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Mostly Trusting

26.3%

1.702

2.525

3.120

1.526

1.473

1.420

1.408

2.155

2.020

1.363

2. Generally Trusting
but Slightly Uncertain

30.7%

3.839

4.078

3.366

1.688

1.530

1.609

3.906

4.168

3.974

1.365

3. Trusting but
Slightly Skeptical

43.0%

2.935

3.999

4.290

2.945

3.143

2.923

3.162

4.214

3.591

3.339

Note. N = 114. Means are on a 1-7 scale.

### Appendix H2: Natural Language Processing Topic Analysis Results for Skills Dimension

Table 37
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Skills Dimension
Cluster #

Number of
Statements per
Clusters

Representative
Words

Summary

Cluster 1

unclear,
requirements

The skills required lack clarity and specificity, with excessive and insufficient
information provided, making it unclear and misleading.

Cluster 2

requirements,
misleading

The skills required are confusing and misleading.

Cluster 3

deceptive, did,
list, necessary

The list of skills is insufficient and deceptive and lacks clear and specific mention of
required skills information, causing the person to feel deceived or that the information
is being misrepresented.

Cluster 4

lacks, clear,
inferred,
qualifications,
responsibilities,
listed

The listed skills lack clarity and specificity, with some requiring unnecessary
qualification and other misleading listing requirements or responsibilities.

Cluster 5

skills, required,
clearly, stated

The skills listed are vague, where some skills required are specific and some are
implied, while others lack clear skill requirements and other explicitly state necessary
skills.

Cluster 6

requires,
registered,
dietitian, lacks,
information,

The list of skills required for becoming a registered dietitian are unclear and
misleading, lacking sufficient information and specific skill requirements.

necessary, like,
communication,
experience
Cluster 7

unclear, listed

The skills required are unclear, misleading, and have vaguely stated reasoning.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the
prompt.

Table 38
Top Words by Cluster Based on Word Count for Skills Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

Cluster 1

required
(29.8%)

requirements (19.1%)

lacks
(13.8%)

information
(8.5%)

list (5.3%)

unclear
(5.3%)

clear (5.3%)

listed
(5.3%)

insufficient
(4.3%)

specific
(3.2%)

Cluster 2

requirements (42.4%)

misleading
(42.4%)

confusing
(10.6%)

unclear
(4.5%)

–

–

–

–

–

–

Cluster 3

deceptive
(31.1%)

required
(15.6%)

necessary
(13.3%)

list (11.1%)

lacked
(6.7%)

insufficient
(4.4%)

information
(4.4%)

provided
(4.4%)

person
(4.4%)

include
(4.4%)

Cluster 4

lacks
(18.1%)

requirements (16.2%)

required
(14.3%)

skill
(14.3%)

clear (9.5%)

experience
(6.7%)

requires
(5.7%)

necessary
(5.7%)

require
(4.8%)

qualifications (4.8%)

Cluster 5

skills
(26.0%)

skill
(12.0%)

requirements (10.0%)

required
(9.0%)

clearly
(8.0%)

stated
(8.0%)

mentioned
(8.0%)

lacks (8.0%) clear (6.0%)

specified
(5.0%)

Cluster 6

registered
(16.7%)

requires
(16.7%)

dietitian
(16.7%)

misleading
(10.0%)

dietician
(10.0%)

lacks
(10.0%)

required
(6.7%)

requirements (6.7%)

organizational (3.3%)

using
(3.3%)

Cluster 7

unclear
(26.2%)

misleading
(18.0%)

listed
(16.4%)

required
(14.8%)

mentioned
(9.8%)

reason
(3.3%)

provided
(3.3%)

specific
(3.3%)

vague
(3.3%)

unclearly
(1.6%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix I - Qualifications Dimension Results

### Appendix I1: Latent Profile Analysis Results for Qualifications Dimension

Table 39
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Qualifications Dimension
Job Ad
\#

SD

3.1

1.8

3.7

1.9

0.271**

3.0

1.9

0.046

0.166

2.7

1.7

0.360***

0.231*

0.109

2.1

1.4

0.179

0.284**

0.199*

0.294**

2.3

1.6

0.172

0.119

0.143

0.335***

0.206*

2.8

1.7

0.241**

0.189*

0.124

0.385***

0.125

0.306***

3.6

2.0

0.098

0.110

0.309***

0.154

0.103

0.207*

0.191*

2.9

1.7

0.152

0.183

0.161

0.104

0.071

0.012

0.202*

2.6

1.7

0.233*

0.311***

0.081

0.431***

0.248**

0.128

0.414*** 0.368*** 0.323***

0.080

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 40
Latent Profile Enumeration Fit Statistics for Qualifications Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,232

4,504

4,559

4,496

0.00

NA

-2,166

4,395

4,480

4,382

131.00

0.010

-2,141

4,365

4,480

4,347

51.70

0.010

-2,232

4,504

4,559

4,496

0.00

NA

2*

-2,109

4,300

4,412

4,283

246.00

0.010

NA

NA

NA

NA

NA

NA

-2,145

4,420

4,598

4,392

0.00

NA

-2,140

4,432

4,640

4,400

9.40

0.970

-2,090

4,355

4,593

4,318

99.30

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying mean.
Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed to 0.
Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria; BIC =
Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood ratio
test. NA = indicates convergence issues during model estimation potentially due to model misspecification for the
data structure. Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 41
Summary of Variance Components and Generalizability Coefficients in G Study for Qualifications
Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.606

18.4

–

Item (I)
(Job advertisement)

0.253

7.7

–

P X I (Residual)

2.426

73.9

–

Total

3.285

100.0

–
0.816

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 42
Percent of Sample by Profile and Means of Job Advertisements by Profile for Qualifications Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Overall Uncertain

78.1%

3.397

4.006

3.438

3.047

2.251

2.519

3.138

3.903

2.958

2.891

2. Overly Trusting

21.9%

1.925

2.596

1.464

1.412

1.355

1.406

1.527

2.637

2.477

1.366

Note. N = 114. Means are on a 1-7 scale.

### Appendix I2: Natural Language Processing Topic Analysis Results for Qualifications Dimension

Table 43
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Qualifications Dimension
Cluster #

Number of Representative Words
Statements
per Clusters

Summary

Cluster 1

misleading

The qualifications are a mix of unclear, misleading, and confusing.

Cluster 2

qualifications,
specified

The job qualifications listed are often misleading and unclear, with some requiring excessive
education or experience, while others lack clarity and specificity.

Cluster 3

requires, registered,
dietician, doesn’t,
mention, preferred,
required, work,
experience

The job qualifications are unclear and misleading, often requiring registered dietitians status
or previous barista experience without specifying relevance, and some even require
registration as a therapist or nutrition specialist, making it difficult to assess qualifications.

Cluster 4

unclear, requirements

The qualifications lack necessary and clear requirements, with some being misleading and
excessive, and important information regarding qualifications and responsibilities
insufficiently provided.

Cluster 5

deceptive

The qualifications were deceptive and misleading, lacking accurate information and leading
to false beliefs about qualifications, salary, and job requirements.

Cluster 6

lacks, clear

The list of qualifications lacks clarity, specificity, and important details, leading to confusion
and inconsistency.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the prompt.

Table 44
Top Words by Cluster Based on Word Count for Qualifications Dimension
Cluster #

Top Word 1

Top Word 2

Top Word 3

Top Word 4

Top Word 5

Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

Cluster 1

misleading
(76.1%)

confusing
(13.0%)

unclear
(10.9%)

–

–

–

–

–

–

–

Cluster 2

qualifications (18.4%)

degree
(13.6%)

experience
(12.6%)

college
(10.7%)

required
(10.7%)

requires
(7.8%)

high (6.8%)

listed
(6.8%)

requirements (6.8%)

school
(5.8%)

Cluster 3

dietician
(14.0%)

requires
(12.0%)

registered
(12.0%)

experience
(12.0%)

barista
(10.0%)

required
(10.0%)

unclear
(10.0%)

misleading
(8.0%)

doesn’t
(6.0%)

mention
(6.0%)

Cluster 4

misleading
(13.2%)

requirements (13.2%)

license
(12.3%)

drivers
(11.3%)

insufficient
(10.4%)

lacks (9.4%)

required
(9.4%)

requires
(7.5%)

necessary
(7,5%)

information
(5.7%)

Cluster 5

deceptive
(31.1%)

reason
(11.5%)

provided
(11.5%)

misleading
(11.5%)

information
(8.2%)

preferred
(6.6%)

listed
(6.6%)

believe
(4.9%)

accurately
(4.9%)

sorry (3.3%)

Cluster 6

lacks
(24.1%)

unclear
(20.7%)

clear
(15.5%)

lacked
(8.6%)

clarity
(6.9%)

listed
(6.9%)

vague
(6.9%)

required
(5.2%)

specific
(3.4%)

list (1.7%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix J - Schedule Dimension Results

### Appendix J1: Latent Profile Analysis Results for Schedule Dimension

Table 45
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Schedule Dimension
Job Ad
\#

SD

2.8

1.8

4.0

1.7

0.156

4.1

2.1

-0.015

0.108

4.1

1.9

0.190*

0.475***

0.185*

2.2

1.5

0.296**

0.278**

0.106

0.253**

3.1

1.7

0.174

0.115

-0.032

0.142

0.200*

2.4

1.6

0.166

-0.003

0.047

0.139

0.280**

0.019

3.3

1.9

0.130

0.231*

0.100

0.315***

0.144

0.202*

0.092

2.9

1.7

0.281**

0.232*

0.280**

0.238*

0.339***

0.213*

0.206*

0.372***

3.9

1.8

0.123

0.263**

0.233*

0.355***

0.136

0.082

0.119

0.129

0.170

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 46
Latent Profile Enumeration Fit Statistics for Schedule Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,255

4,550

4,604

4,541

0.00

NA

-2,200

4,462

4,547

4,449

109.00

0.010

-2,175

4,434

4,549

4,416

50.40

0.010

-2,255

4,550

4,604

4,541

0.00

NA

2*

-2,127

4,336

4,448

4,319

255.00

0.010

NA

NA

NA

NA

NA

NA

-2,173

4,476

4,654

4,448

0.00

NA

-2,160

4,472

4,680

4,440

26.00

0.228

-2,135

4,443

4,681

4,406

50.90

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying mean.
Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed to 0.
Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria; BIC =
Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood ratio test.
NA = indicates convergence issues during model estimation potentially due to model misspecification for the data
structure. Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 47
Summary of Variance Components and Generalizability Coefficients in G Study for Schedule Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.557

15.30

–

Item (I)
(Job advertisement)

0.515

14.1

–

P X I (Residual)

2.576

70.6

–

Total

3.648

100.0

–
0.847

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 48
Percent of Sample by Profile and Means of Job Advertisements by Profile for Schedule Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Moderate
Skepticism

54.4%

1.729

3.549

3.922

3.542

1.512

2.638

1.686

2.845

2.113

3.552

2. Mixed Suspicious

45.6%

3.890

4.592

4.290

4.711

2.910

3.549

3.180

3.819

3.742

4.385

Note. N = 114. Means are on a 1-7 scale.

### Appendix J2: Natural Language Processing Topic Analysis Results for Schedule Dimension

Table 49
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Schedule Dimension
Cluster #

Number of
Statements per
Clusters

Representative
Words

Summary

Cluster 1

misleading

The schedule contains a mix of unclear and misleading information.

Cluster 2

stated, full, time,
misleading

The schedule includes various instances of misleading and unclear descriptions, with
deceptive claims of flexibility, unrealistic expectations, and lack of clear information
regarding work hours, availability, and compensation.

Cluster 3

specified,
misleading

The schedule contains instances of deceptive and misleading information provided
about flexible work arrangements, leading to confusion and suspicion among job
seekers.

Cluster 4

unclear, lacks,
specific, details

The schedule lacks clarity, specificity, and transparency, with potentially misleading
descriptions and unclear timeframes, and involves online and in-office work with
varying contexts for flexibility needs.

Cluster 5

unclear,
required, work
hours,
mentioning,
hour, shifts,
weekend,
availability

The schedule information is misleading and lacks clear information about required
work hours, shift availability, and scheduling factors, causing confusion and
uncertainty for potential employees.

Cluster 6

lacks,
information,
work

The work schedule lacks accurate, detailed, and sufficient information, including
required skills and the possibility of afterhours work, and is often misleading and
vague with some information missing.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the
prompt.

Table 50
Top Words by Cluster Based on Word Count for Schedule Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Cluster 1

misleading
(58.7%)

Cluster 2

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

unclear
(41.3%)

–

–

–

–

–

–

–

–

misleading
(17.4%)

fulltime
(16.5%)

time
(13.2%)

hours
(10.7%)

unclear
(8.3%)

deceptive
(8.3%)

work
(7.4%)

parttime
(6.6%)

stated
(5.8%)

advertised
(5.8%)

Cluster 3

misleading
(15.8%)

deceptive
(14.5%)

flexible
(14.5%)

provided
(9.2%)

advertised
(18.4%)

specific
(9.2%)

disclosed
(7.9%)

specified
(6.6%)

good (6.6%)

true (6.6%)

Cluster 4

unclear
(31.2%)

lacks
(12.5%)

clear
(12.5%)

work
(11.2%)

lacked
(7.5%)

vague
(7.5%)

misleading
(6.2%)

time (3.8%)

provide
(3.8%)

specific
(3.8%)

Cluster 5

hours
(21.4%)

work
(15.6%)

hour
(11.6%)

misleading
(11.2%)

unclear
(10.7%)

shifts
(7.6%)

days (6.7%)

information
(5.8%)

shift (4.9%)

specific
(4.5%)

Cluster 6

information
(37.5%)

work
(16.2%)

lacks
(11.2%)

provide
(7.5%)

insufficient
(7.5%)

provided
(5.0%)

sufficient
(3.8%)

missing
(3.8%)

lacked
(3.8%)

clear (3.8%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix K - Education Dimension Results

### Appendix K1: Latent Profile Analysis Results for Education Dimension

Table 51
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Education Dimension
Job Ad
\#

SD

3.8

1.6

3.6

2.0

0.143

3.6

1.9

0.275**

0.288**

3.9

1.9

0.453***

0.167

0.328***

2.4

1.5

0.137

0.284**

0.292**

0.182

2.2

1.4

0.109

0.029

0.109

0.220*

-0.017

2.7

1.7

0.262**

0.100

0.258**

0.199*

0.221*

0.145

4.5

1.9

0.311***

0.142

0.354*** 0.384***

0.021

0.089

0.171

2.3

1.5

0.055

0.184*

0.211*

0.074

0.192*

0.149

0.241**

0.182

3.6

1.7

0.442***

0.194*

0.298**

0.492***

0.050

0.166

0.249**

0.443***

0.122

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 52
Latent Profile Enumeration Fit Statistics for Education Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,221

4,482

4,537

4,473

0.00

NA

-2,160

4,382

4,466

4,368

122.00

0.010

-2,129

4,341

4,456

4,324

62.20

0.010

-2,221

4,482

4,537

4,473

0.00

NA

-2,123

4,328

4,441

4,311

196.00

0.010

3*

-2,056

4,235

4,405

4,209

135.00

0.010

-2,123

4,377

4,555

4,349

0.00

NA

-2,109

4,371

4,579

4,338

28.10

0.198

-2,080

4,333

4,571

4,296

59.30

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying mean.
Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed to 0.
Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria; BIC =
Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood ratio test.
NA = indicates convergence issues during model estimation potentially due to model misspecification for the data
structure. Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 53
Summary of Variance Components and Generalizability Coefficients in G Study for Education Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.637

17.7

–

Item (I)
(Job advertisement)

0.617

17.2

–

P X I (Residual)

2.340

65.1

–

Total

3.593

100.0

–
0.823

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 54
Percent of Sample by Profile and Means of Job Advertisements by Profile for Education Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Generally Trusting

14.9%

2.236

2.692

1.399

1.459

1.575

1.519

1.580

2.814

1.520

1.853

2. Slightly Skeptical

46.5%

4.040

3.830

4.164

4.333

2.582

2.766

3.766

4.874

3.019

4.098

3. Trusting with
Heighten Awareness

38.6%

3.974

3.665

3.584

4.225

2.492

1.587

1.609

4.666

1.607

3.685

Note. N = 114. Means are on a 1-7 scale.

### Appendix K2: Natural Language Processing Topic Analysis Results for Education Dimension

Table 55
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Education Dimension
Cluster #

Number of
Statements per
Clusters

Representative
Words

Summary

Cluster 1

requirements
misleading

The education section lists misleading requirements.

Cluster 2

misleading
requirements,
mention degree
necessary

The requirements contain various instances of misleading or unclear requirements for
education and degree qualifications in job postings.

Cluster 3

lacks
information,
requirements

The requirements section lacks clarity and specific information, including clear
qualifications and educational requirements.

Cluster 4

misleading,
requirements,
mentioned

The requirements listed were often unclear, misleading, and lacked necessary
information, causing confusion and uncertainty for potential applicants.

Cluster 5

misleading,
required, high
school, diploma

The job education requirements listed were misleading and unclear, suggesting that a
high school or college diploma is necessary or preferred when it may not be, leading
to confusion and potentially deceiving applicants.

Cluster 6

education,
requirements,
specified

The education requirements for a particular position were either not clearly stated,
specified, or unclear, leading to confusion and the need for clarification.

Cluster 7

unclear,
requirements

The listed requirements are unclear and confusing.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the
prompt.

Table 56
Top Words by Cluster Based on Word Count for Education Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Cluster 1

misleading
(50.0%)

Cluster 2

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

requirements (50.0%)

–

–

–

–

–

–

–

–

degree
(30.0%)

required
(12.5%)

misleading
(10.8%)

requirements (10.0%)

preferred
(8.3%)

necessary
(8.3%)

college
(7.5%)

associates
(4.2%)

unclear
(4.2%)

experience
(4.2%)

Cluster 3

requirements (32.6%)

lacks
(17.4%)

information
(12.8%)

lacked
(10.5%)

clear (8.1%)

specific
(4.7%)

insufficient
(4.7%)

required
(3.5%)

section
(3.5%)

lack (2.3%)

Cluster 4

requirements (35.1%)

misleading
(14.5%)

required
(13.0%)

unclear
(9.9%)

deceptive
(6.9%)

specify
(6.1%)

provide
(3.8%)

necessary
(3.8%)

listed
(3.4%)

information
(3.4%)

Cluster 5

high
(16.3%)

misleading
(15.2%)

school
(15.2%)

diploma
(13.0%)

requirements (9.8%)

college
(9.8%)

degree
(6.5%)

stating
(5.4%)

unclear
(4.3%)

required
(4.3%)

Cluster 6

education
(32.1%)

requirements (29.5%)

specified
(14.1%)

stated
(6.4%)

mentioned
(3.8%)

clearly
(3.8%)

unclear
(3.8%)

necessary
(2.6%)

level (2.6%)

requirement
(1,3%)

Cluster 7

requirements (50.0%)

unclear
(42.3%)

confusing
(7.7%)

–

–

–

–

–

–

–

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix L - Experience Dimension Results

### Appendix L1: Latent Profile Analysis Results for Experience Dimension

Table 57
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Experience Dimension
Job Ad
\#

SD

3.3

1.8

3.8

1.9

0.290**

4.0

1.9

0.111

0.247**

2.4

1.6

0.195*

0.075

0.151

2.1

1.5

0.312***

0.268**

-0.006

0.336***

2.6

1.6

0.104

-0.036

0.220*

0.295**

2.5

1.6

0.235*

0.132

0.292**

0.353*** 0.309***

4.2

1.8

0.308***

0.200*

0.341***

0.169

-0.107

0.142

0.164

2.6

1.6

0.332***

0.163

0.121

0.200*

0.171

0.108

0.265**

0.178

2.7

1.9

0.129

0.161

0.043

0.236*

0.141

0.294**

0.167

0.146

-0.007
0.145

0.105

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 58
Latent Profile Enumeration Fit Statistics for Experience Dimension
Model #

\# of
Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,215

4,471

4,525

4,462

0.00

NA

-2,171

4,406

4,491

4,393

86.30

0.010

-2,130

4,343

4,458

4,325

85.30

0.010

-2,215

4,471

4,525

4,462

0.00

NA

-2,092

4,266

4,379

4,249

246.00

0.010

3*

-2,033

4,191

4,360

4,165

117.00

0.010

-2,128

4,385

4,563

4,358

0.00

NA

-2,113

4,377

4,585

4,345

29.90

0.178

-2,089

4,351

4,589

4,314

48.40

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying
mean. Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances
fixed to 0. Model 3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information
criteria; BIC = Bayesian information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped loglikelihood ratio test. NA = indicates convergence issues during model estimation potentially due to model
misspecification for the data structure. Best fit model chosen from BIC due to balance of model fit and model
complexity.

Table 59
Summary of Variance Components and Generalizability Coefficients in G Study for Experience
Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.527

15.2

–

Item (I)
(Job advertisement)

0.535

15.5

–

P X I (Residual)

2.396

69.3

–

Total

3.458

100.0

–
0.848

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 60
Percent of Sample by Profile and Means of Job Advertisements by Profile for Experience Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Generally Trusting

15.8%

1.872

2.415

1.482

1.366

1.483

1.361

1.422

2.860

1.549

1.192

2. Generally Skeptical

45.6%

4.098

4.452

4.402

3.394

2.883

2.780

3.113

4.705

3.463

3.028

3. Wavering
Skepticism

38.6%

2.824

3.582

4.501

1.654

1.502

2.813

2.120

4.155

1.842

2.873

Note. N = 114. Means are on a 1-7 scale.

### Appendix L2: Natural Language Processing Topic Analysis Results for Experience Dimension

Table 61
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Experience Dimension
Cluster #

Number of
Statements
per Clusters

Representative
Words

Summary

Cluster 1

prior, required

The job posting lacked clarity and did not clearly state all necessary prior
requirements, including mental health services and hands-on experience, which may
favor inexperienced candidates but also raises concerns about credibility.

Cluster 2

requiring,
excessive, years

The job experience requirements for certain positions are unrealistic, requiring
excessive years of experience, complex skills, and niche qualifications.

Cluster 3

deceptive,
misrepresented,
required

The job experience requirements were misleading and lack necessary specificity,
leading to confusion and disappointment for candidates.

Cluster 4

fails, specify,
necessary,
qualifications

The job experience requirements listed are often unclear, misleading, and lack
necessary details, making it difficult for applicants to determine the necessary
qualifications and experience needed for the role.

Cluster 5

unclear, necessary The experience required is unclear and necessary information is missing, making it
seem misleading.

Cluster 6

agreed

There is agreement to the deceptive nature of the experience listed.

Cluster 7

experience,
requirements,
stated

The job requires specific and clearly stated experience requirements.

Cluster 8

unclear,
requirements

The requirements stated are insufficient, unclear, excessive, or lack necessary
information, leading to confusion and suspicion.

Cluster 9

did, specify,
required

The experience requirements had certain items required or specified, while others
were optional or preferred, and some appeared excessive or odd, with reasons only
sometimes provided.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the
prompt.

Table 62
Top Words by Cluster Based on Word Count for Experience Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

Cluster 1

prior
(28.1%)

necessary
(19.3%)

required
(12.3%)

indication
(8.8%)

provide
(7.0%)

listed
(7.0%)

previous
(5.3%)

list (5.3%)

mention
(3.5%)

mentioned
(3.5%)

Cluster 2

years
(34.4%)

excessive
(15.6%)

required
(9.4%)

requiring
(6.2%)

unrealistic
(6.2%)

requirements (6.2%)

year (6.2%)

customer
(6.2%)

service
(6.2%)

requires
(3.1%)

Cluster 3

misleading
(20.8%)

required
(19.8%)

deceptive
(16.7%)

necessary
(12.5%)

requires
(6.2%)

person
(6.2%)

mention
(5.2%)

specify
(4.2%)

Cluster 4

required
(16.9%)

requires
(14.3%)

misleading
(11.7%)

necessary
(10.4%)

lacks (9.1%)

experience
(9.1%)

unclear
(7.8%)

requirements (7.8%)

skills
(6.5%)

education
(6.5%)

Cluster 5

misleading
(29.8%)

unclear
(29.8%)

necessary
(23.4%)

required
(17.0%)

–

–

–

–

–

–

Cluster 6

agreed
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 7

experience
(41.3%)

specified
(14.7%)

requirement
s (14.7%)

required
(6.7%)

requirement
(6.7%)

necessary
(4.0%)

stated
(4.0%)

listed
(2.7%)

disclosed
(2.7%)

unclear
(2.7%)

Cluster 8

required
(18.3%)

requirements (18.3%)

information
(13.5%)

unclear
(11.5%)

lacks
(11.5%)

insufficient
(10.6%)

provided
(5.8%)

regarding
(4.8%)

clear (2.9%)

lack (2.9%)

Cluster 9

required
(48.5%)

specify
(12.2%)

necessary
(9.1%)

mention
(9.1%)

excessive
(6.1%)

appears
(3.0%)

listed
(3.0%)

hope (3.0%)

optional
(3.0%)

stated
(3.0%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

lacks (4.2%) requirements (4.2%)

## Appendix M - Work Location Dimension Results

### Appendix M1: Latent Profile Analysis Results for Work Location Dimension

Table 63
Means, Standard Deviations, and Intercorrelations of Job Advertisements for Work Location Dimension
Job Ad
\#

SD

1.9

1.3

3.2

1.7

0.319***

3.6

2.1

0.119

0.029

2.4

1.6

0.203*

0.182

0.180

2.2

1.5

0.291**

-0.022

0.152

0.082

1.9

1.2

0.256**

0.252**

0.193*

0.389***

0.109

2.4

1.7

0.308***

0.131

0.183

0.065

0.411***

0.099

2.6

1.7

0.280**

0.232*

0.124

0.101

0.186*

0.192*

0.286**

2.1

1.4

0.340***

0.257**

0.225*

0.135

0.212*

0.267**

0.322***

0.284**

3.7

2.0

0.045

0.181

0.082

0.022

0.035

0.053

-0.030

0.102

0.026

Note. N = 114. *p < .05, ** p < .01, *** p < .001. Deception ratings of job advertisement’s job descriptions are on a 1-7 Likert-type scale.
Images of job advertisements and corresponding numbers can be found in Appendix B and at https://osf.io/xf9e6/files/osfstorage under
“Indeed Job Ads used in Study 3”.

Table 64
Latent Profile Enumeration Fit Statistics for Work Location Dimension
Model #

\# of Profiles

AIC

BIC

SSA-BIC

BLRT

BLRT pvalue

-2,161

4,362

4,417

4,354

0.00

NA

-2,088

4,238

4,323

4,225

146.00

0.010

-2,074

4,232

4,347

4,214

28.10

0.050

-2,161

4,362

4,417

4,354

0.00

NA

2*

-1,999

4,080

4,192

4,062

324.00

0.010

NA

NA

NA

NA

NA

NA

-2,085

4,300

4,478

4,272

0.00

NA

-2,060

4,271

4,479

4,239

50.70

0.010

-2,032

4,238

4,476

4,201

55.00

0.010

Note. N = 114. * = best fit. Model # refers to the models in the tidyLPA packages. All models allow varying mean.
Model 1 = equal variances, and covariances fixed to 0. Model 2 = varying variances, and covariances fixed to 0. Model
3 = equal variances and equal covariances. LL = log likelihood; AIC = Alaike information criteria; BIC = Bayesian
information criteria; SSA-BIC = sample-size-adjusted BIC; BLRT = bootstrapped log-likelihood ratio test. NA =
indicates convergence issues during model estimation potentially due to model misspecification for the data structure.
Best fit model chosen from BIC due to balance of model fit and model complexity.

Table 65
Summary of Variance Components and Generalizability Coefficients in G Study for Work Location
Dimension
Source

Variance Estimate

Percentage (%)

G Coefficient

Person (P)
(Participant)

0.440

13.9

–

Item (I)
(Job advertisement)

0.406

12.8

–

P X I (Residual)

2.314

73.2

–

Total

3.160

100.0

–
0.861

Note. N = 114. Based on Generalizability Theory in R code from Huebner & Lucht (2019). p X i study
design code was used in R to compute G coefficient. G coefficient standard based on > 0.7 (Cronbach et
al., 1972; Putka et al., 2008).

Table 66
Percent of Sample by Profile and Means of Job Advertisements by Profile for Work Location Dimension
Mean of Job Advertisement #
Profile # and Names

Percent
of
Sample

1. Uncertain but
Trusting

41.2%

1.510

2.898

3.317

1.618

1.691

1.520

1.559

1.454

1.523

3.622

2. Generally Trusting
but Aware of
Deception

58.8%

2.229

3.452

3.757

2.937

2.519

2.223

2.918

3.313

2.544

3.682

Note. N = 114. Means are on a 1-7 scale.

### Appendix M2: Natural Language Processing Topic Analysis Results for Work Location Dimension

Table 67
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings in the Work Location Dimension
Cluster #

Number of
Statements
per Clusters

Representative
Words

Summary

Cluster 1

lacks, specific
information

The main issue is a lack of information, including insufficient details, omissions, and
unclear addresses, making it difficult to understand and potentially misleading.

Cluster 2

specified

The work location information was not provided or specified.

Cluster 3

misleading

The work location information has misleading information.

Cluster 4

unclear

The work location information consists of unclear information.

Cluster 5

unclear, misleading

The location information contains various instances of unclear, misleading, and deceptive
information about remote work, multiple locations, making it difficult for job seekers to
determine the actual job location.

Cluster 6

confusing

The work location information is confusing and ambiguous.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the prompt.

Table 68
Top Words by Cluster Based on Word Count for Work Location Dimension
Cluster #

Top Word 1 Top Word 2

Top Word 3

Top Word 4

Top Word 5 Top Word 6

Top Word 7

Top Word 8

Top Word 9

Top Word

Cluster 1

information
(32.6%)

lacks
(15.2%)

insufficient
(13.0%)

provided
(6.5%)

difficult
(6.5%0

person
(6.5%)

locate
(6.5%)

lacked
(4.3%)

address
(4.3%)

actual
(4.3%)

Cluster 2

specified
(77.8%)

provided
(22.2%)

–

–

–

–

–

–

–

–

Cluster 3

misleading
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 4

unclear
(100.0%)

–

–

–

–

–

–

–

–

–

Cluster 5

misleading
(22.0%)

unclear
(20.7%)

remote
(10.4%)

listed
(9.1%)

provided
(7.9%)

locations
(7.3%)

specific
(6.1%)

information
(5.5%)

office
(5.5%)

address
(5.5%)

Cluster 6

confusing
(75.0%)

ambiguous
(25.0%)

–

–

–

–

–

–

–

–

Note. Percentages in parentheses represent word count percentage based on overall word count.

## Appendix N - Total Job Dimension Topic Analysis

Table 69
ChatGPT-3.5 Generated Summary for Topic Clusters from Word Embeddings for all 11 Dimensions
Cluster #

Number of
Statements
per
Clusters

Representative
Words

Summary

Cluster 1

deceptive

The job ads contained false information, lacked important qualifications and information, and
provided insufficient and unclear reasons, making them deceptive.

Cluster 2

education,
requirements,
mentioned

The education requirements for various positions are unclear, misleading, and lack clarity, with
some positions requiring excessive or unrealistic qualifications, while others do not specify
necessary education levels or provide confusing information.

Cluster 3

lacks, information

The provided information lacks important details, specificity, clarity, and sufficient details, and
omits crucial information such as location, duties, responsibilities, and benefits, making it
misleading.

Cluster 4

1120

unclear,
potentially,
misleading

The work location is unclear and confusing and lacks specificity about various remote and inperson positions, which lacks specificity and clarity, leading to potential deception and
uncertainty for job seekers.

Cluster 5

changes, needed,
vague, unclearly

The information needs changes to be more clear, it is vague and does not clearly convey the
information about the job.

Cluster 6

unclear, pay,
range

The job listings are found to often be deceptive from unclear salary information, broad pay
ranges, and misleading promises of high salaries and flexible hours.

Cluster 7

unclear

There are multiple instances of unclear or confusing statements in the job advertisements.

Cluster 8

unclear,
experience,
requirements

The job requirements are often misleading and lack clear specificity for necessary experience,
certifications, and skills, leading to confusion and disappointment among potential candidates.

Cluster 9

unclear, work,
schedule

The company’s work schedule and availability policies are unclear and misleading, with
promises of flexibility and weekend availability that contradicts actual requirements and lacks
specific details.

Cluster 10

benefits, listed,
description

The job posting lacks clear and specific information about the benefits offered, with many
benefits mentioned but not adequately explained, leading to doubts about the credibility and the
actual benefits available.

Note. OpenAI ChatGPT API used in Python with the prompt “Write a condensed and succinct summary sentence for the following list that
conveys the main ideas of the list.” The code iterated through the text input for each cluster which made up the “list” referenced in the prompt.

Table 70
Top Words by Cluster Based on Word Count for all 11 Dimensions
Cluster #

Top Word

Top Word 2 Top Word 3 Top Word 4 Top Word 5 Top Word 6 Top Word 7 Top Word 8 Top Word 9

Top Word

Cluster 1

deceptive
(35.7%)

information
(15.4%)

person
(10.2%)

qualifications (7.6%)

Cluster 2

education
(16.8%)

required
(14.8%)

skills
(14.2%)

qualificati - requiremenons (13.4%) ts (11.0%)

Cluster 3

information
(13.4%)

provided
(12.8%)

company
(11.6%)

lacks
(9.9%)

Cluster 4

unclear
(18.1%)

misleading
(14.6%)

location
(10.4%)

Cluster 5

changes
(15.1%)

needed
(15.1%)

Cluster 6

salary
(26.7%)

Cluster 7

false (7.3%)

responsibilities (7.3%)

insufficient
(4.4%)

reason
(4.2%)

finding
(4.2%)

required
(3.9%)

listed
(9.2%)

lacks
(5.4%)

degree
(5.2%)

specified
(5.1%)

unclear
(4.9%)

insufficient
(8.0%)

lack (7.1%)

details
(5.4%)

lacked
(5.1%)

sufficient
(3.4%)

responsibilities (2.4%)

description
(10.3%)

deceptive
(9.1%)

provided
(8.9%)

responsibilities (7.2%)

vague
(7.2%)

work
(6.9%)

reason
(6.4%)

vague
(15.1%)

conveys
(15.1%)

meaning
(15.1%)

unclear
(15.1%)

unclearly
(9.3%)

–

–

–

range
(19.3%)

pay (18.7%)

unclear
(9.3%)

deceptive
(6.2%)

misleading
(4.9%)

high (3.9%)

broad
(3.9%)

flexible
(3.7%)

hours
(3.3%)

unclear
(60.1%)

confusing
(39.9%)

–

–

–

–

–

–

–

–

Cluster 8

experience
(37.1%)

requirement
s (19.6%)

required
(12.7%)

prior (6.7%)

listed
(4.8%)

lacks
(4.6%)

unclear
(3.9%)

mentioned
(3.7%)

misleading
(3.5%)

doesn’t
(3.5%)

Cluster 9

schedule
(25.6%)

work
(14.8%)

hours
(12.5%)

flexible
(8.8%)

information
(8.3%)

unclear
(7.7%)

lacks
(6.7%)

fulltime
(6.5%)

misleading
(4.8%)

provided
(4.3%)

Cluster 10

benefits
(58.0%)

listed
(8.8%)

benefit
(4.4%)

information
(4.4%)

mentioned
(4.4%)

appear
(4.4%)

mention
(4.0%)

unrealistic
(4.0%)

offered
(4.0%)

uniform
(3.5%)

Note. Percentages in parentheses represent word count percentage based on overall word count.

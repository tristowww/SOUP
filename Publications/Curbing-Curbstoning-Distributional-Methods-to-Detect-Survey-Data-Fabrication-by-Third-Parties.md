# Curbing Curbstoning: Distributional Methods to Detect Survey Data Fabrication by Third-Parties

Ivan Hernandez, Teresa Ristow, and Matthew Hauenstein

Psychological Methods, 2022, Vol. 27, No. 1, 99-120
DOI: https://doi.org/10.1037/met0000403

Keywords: survey methods, research design, ethics, fraud, curbstoning
Supplemental materials: https://doi.org/10.1037/met0000403.supp

Published Online First: August 26, 2021
Ivan Hernandez https://orcid.org/0000-0002-3141-7525
Matthew Hauenstein https://orcid.org/0000-0002-1812-7953

1 Department of Psychology, Virginia Polytechnic Institute and State University
2 Kroc Institute for International Peace Studies, University of Notre Dame

Some of these results were presented during the 2020 35th Society of Industrial/Organizational Psychology conference in Austin, Texas, United States during a poster presentation session.

Correspondence concerning this article should be addressed to Ivan Hernandez, Department of Psychology, Virginia Polytechnic Institute and State University, 890 Drillfield Drive, Blacksburg, VA 24060, United States. Email: ivanhernandez@vt.edu

Received October 4, 2019
Revision received February 26, 2021
Accepted March 5, 2021

## Abstract

Curbstoning, the willful fabrication of survey responses by outside data collectors, threatens the integrity of the inferences drawn from data. Researchers who outsource data collection to survey collection panels, field interviewers, or research assistants should validate whether each collection agent actually collected the data. Our review of the survey auditing literature demonstrates a consistent presence of curbstoning, even at professional levels. This study proposes several general simple survey questions that have statistical distributions known a priori, as a method to detect curbstoning. By exploiting common deficiencies in statistical understanding, survey collectors imputing data to these questions can leverage empirically known distributions to determine deviation from the expected distribution of responses. We examined both authentic and fabricated surveys that included these questions and we compared the observed distributions with the expected distributions. The majority of the proposed methods had Type I error rates near or below the specified alpha level (.05). The methods demonstrated the ability to detect false responses correctly 48%-90% of the time across two samples when surveying at least 50 participants. While the methods varied in effectiveness, combining these methods demonstrated the highest statistical power, with Type I error rates lower than 1%. Additionally, even in situations with smaller sample sizes (e.g., N = 30), combining these methods allows them to be effective in detecting curbstoning. These methods provide a simple and generalizable way for researchers not present during data collection to possess accurate data.

### Translational Abstract

Researchers often have their surveys collected by third-parties, including research assistants, collaborators, or online panels. While outsourcing collection offers a scalable way for researchers to conduct more research and access more populations, there are also limitations. Methodologists have highlighted that outsourced data collection is at risk of "curbstoning," where an interviewer manually fabricates data instead of collecting it. Most audits of large survey organizations find that curbstoning is present at some level. This article proposes several general simple survey questions that can detect interviewers curbstoning. These questions ask for the respondent to provide innocuous biographical information, with known statistical distributions. By exploiting common deficiencies in people's statistical understanding, survey collectors fabricating data to these questions will create response patterns that deviate from the expected distribution of responses. Comparing the distribution of responses in the data to the distribution expected provides a way to probabilistically determine if a collection of data is unusual. When predicting the fabrication status of a sample of real and fabricated data hey demonstrated the ability to detect false responses correctly 48%-90% of the time across two samples, when surveying at least 50 participants. Combining these methods demonstrated the highest effectiveness, with more than 90% of its fabrication predictions being correct, and a false positive rate lower than 1%. These methods provide a simple and generalizable way for researchers to further validate their data.

## What Is "Curbstoning"

Researchers often delegate survey collection to third-parties, including panel services, academic collaborators, or research assistants (Bentley et al., 2017; Boas et al., 2020). Hiring others to collect data has the potential to reach broader demographics and obtain larger samples. However, researchers outsourcing collection have no first-hand assurance that the data were authentically collected (Schoenherr et al., 2015). Even professional survey panel companies see fabricated collection as a major concern (Biemer & Lyberg, 2003; Li et al., 2009). Therefore, academic researchers enlisting their services or using their own assistants, should similarly share this concern. Although several methods exist for verifying data integrity, each has its own limitations including: intrusiveness, time intensiveness, hardware requirements, inflexibility across research designs, requiring calibration samples, dependence on survey-length, and unknown Type I error rates. The current project addresses the limitations by proposing several methods based on common cognitive errors when judging statistical processes.

"Curbstoning" describes the act of interviewers purposely falsifying survey data (Koczela et al., 2015). Examples of curbstoning are: an interviewer not being able to meet a quota and completing the surveys alone; an unmotivated research assistant only asking the respondents to complete a basic part of the survey while she/he completes the rest; or, an unchecked, entry-level survey employee imputing results to minimize effort or receive a higher payment. As with fraud, it leaves room for the public to question the credibility of scientific results. A recent Pew survey finds that between 25% to 50% of Americans consider misconduct a "very big" or "moderately big" problem (Funk et al., 2019). A review of public skepticism of psychology identified the failure to self-police as a major detriment to the public's image of psychology (Lilienfeld, 2012). Providing quality assurance methods can both enhance the validity of research and also the public's perception of the field.

## Frequency of Curbstoning

Curbstoning is an issue found consistently, even in professional survey collection companies. A report from the United States Census Bureau reinterviewed a collection of suspicious interviews across three different surveys -- the Current Population Survey (CPS), the National Crime Survey (NCS), and the New York City Housing Vacancy Survey (NYC-HVS). By dividing the number of confirmed interviewers caught fabricating by the total number of interviewers, they found that .4%, .4%, and 6.5% of the CPS, NCS, and NYC-HVS interviewers, respectively, were falsifying their data completely (Schreiner et al., 1988). Using data from the National Health Interview Survey, from 1983 through 1996, Hood and Bushery (1997) randomly selected interviewers or used suspicious demographics to flag interviewers for reinterviewing. They found that between .2% and 3.5% of 7,500 interviewers had fabricated data. Koch (1995) conducted a large-scale survey on the German population and found that between .4% and 2.3% of randomly selected interviews consisted of fabricated data. Kiecker and Nelson (1996) conducted a survey of 316 U.S. firms that supply "interview services." Directors at the firms reported that 6.3% of their interviewers were caught fabricating entire interviews, despite supervision in a telephone call center.

In addition to large-scale audits of survey collection panels, there are also individual reports of studies validating their interviewers (Bredl et al., 2013). Krejsa et al. (1999) describes a quality assurance (QA) analysis where a QA agent visits a home that was presumably interviewed by a hired interviewer and verifies participation. Curbstoning rates ranged from 0% to 1.2% across three different survey cities. Turner et al. (2002), conducted a study on sexually transmitted infection prevalence, in Baltimore. Using respondent telephone verification, they found that six of the 36 recruited interviewers (16%) submitted fabricated responses. Schaefer et al. (2005) examined 6 years of data collected from 16,000 households as part of the German Socio-Economic Panel Study. Across those six waves, the analysis found that nine out of approximately 1,600 household interviewers (.5%) completely faked their data. The rates were similar (.6%) for personal interviews. Harrison and Krauss' (2002) report on a survey conducted in Zimbabwe revealed that three of the five interviewers (60%) delivered untrustworthy data, based on examining tape-recordings. Sharma and Elliott (2019) describe an Indian TV viewership study where two out of 19 interviewers (10.5%) were found fabricating data. Bredl et al. (2012) mention a case in which the first round of a survey conducted by 13 interviewers had 30% of the interviewers entirely falsify interviews.

From the above research, we draw three conclusions regarding the frequency of curbstoning. First, curbstoning differs by context, especially by region. The base rate of curbstoning depends on where researchers collect data, which has implications for international collaboration. Second, the base rate in the United States is fairly consistent, where it is seldom observed at 0%, with most survey panel audits finding the base rate between 1%-2% on average, and rarely above 6%. Therefore, the true frequency of curbstoning is likely rare, but can also be reliably expected in a large sample. This base rate implies that for every 25 researchers who dispatch four research assistants to collect data from the public, an average one to two of those studies (4%-8%) would be affected by curbstoning (assuming interviewers were randomly selected from the population). Demonstrating the cumulative impact of curbstoning, Kuriakose and Robbins (2016) analyzed 1,000 public data sets from international surveys and found that approximately 20% of the data sets show fabrication at the study-level, and of the suspected data sets, approximately 5% of the data were fabricated.

Many of the auditing studies focused on organizations that specialize in interviewing, which should be less susceptible than nonspecialists to survey validity issues. Perceptually, survey organizations see fabrication as a major concern (Biemer & Lyberg, 2003; Li et al., 2009). Given these estimates and professional concerns, just like scientific fraud, which is also a rare event, curbstoning should be considered important by scientists, because of the compounding effects in aggregate. Whereas one person is unlikely to experience curbstoning, the consistent presence and combination of interviewers to create study data, means that curbstoning will be present within a large enough sample.

### Susceptibility of Academic Research to Curbstoning

Although psychological research is most commonly conducted using laboratory samples and online crowdsourcing platforms, such as MTurk or Prolific, researchers also occasionally use methods that are susceptible to curbstoning, such as panel services and in-person field studies. To illustrate how prevalent panel services and field surveyors are in published research, we examined every article published in the previous year (September 2019-September 2020), 5 years ago (September 2014-September 2015), and 10 years ago (September 2009-September 2010) from three journals that study socially relevant questions: the Journal of Personality and Social Psychology (JPSP), the Journal of Applied Psychology (JAP), and the Journal of Consumer Psychology (JCP). In total we coded 389 JPSP articles, 296 JAP articles, and 134 JCP articles. We coded each study within an article for whether it (a) used a panel service or (b) used field interviewers in a nonlaboratory setting. This analysis coded a total number of 2,242 studies (NJPSP = 1,441, NJAP = 422, NJCP = 379). We summarize the results of this review in Table 1. Based on these analyses, we find no indication that panel services and in-person field studies consistently decreased over time. Thus, while panel services and in-person field studies are less common than lab and crowdsourced methodologies, they remain a persistent part of socially-related research.

In the three journals examined, no clear increasing or decreasing trend in frequency emerged for panel services or in-person field interviews. In JPSP, there was a statistically significant increase in the use of panel services from 2010 (.62%, 95% CI [.08, 1.33]), to 2015 (3.04%, 95% CI [1.41, 4.67)]), and from 2015 to 2020 (6.94%, 95% CI [4.78, 9.1]), based on examining the overlap of the 95% confidence intervals of each proportion (see Table 1). The rate has increased linearly by 3% every 5 years. However, the use of field studies remained statistically indistinguishable between 2010 (3.95%, 95% CI [2.21, 5.69]), 2015 (2.81%, 95% CI [1.24, 4.38]), and 2020 (2.25%, 95% CI [.99, 3.51]). Therefore, it is possible that field studies in social and personality psychology are used to address questions that are not yet easily addressed with the advances in technology during this time. In JAP, panel service usage has remained near 3.5% across 2010 (3.23%, 95% CI [.12, 6.34]), 2015 (3.98%, 95% CI [1.09, 6.86]), and 2020 (3.28%, 95% CI [.12, 6.44]), with no statistically significant differences between those proportions. We also find no statistically significant differences between in-person field interviews in 2010 (6.45%, 95% CI [2.13, 10.78]) and 2015 (7.95%, 95% CI [3.96, 11.95]), though the proportion from 2015 to 2020 (1.63%, 95% CI [.61, 3.89]) did decrease significantly. Similarly, in JCP, there is no clear linear trend in how frequently panel services are used, though 2015 had an extremely high rate of using panel services (14.57%, 95% CI [8.94, 20.2]), which was a statistically significant increase relative to 2010 (4.12% 95% CI [.17, 8.08]) and statistically larger than 2020 (0%, 95% CI [.58, 3.42]), with no detectable difference between 2010 and 2020. In JCP, we find a statistically similar rate of in-person field interviews across 2010 (5.15, 95% CI [.75, 9.55]), 2015 (1.99, 95% CI [.24, 4.21]), and 2020 (2.29, 95% CI [.27, 4.85]). Therefore, there seems to be no strong or consistent evidence that the usage of curbstoning-susceptible methods has decreased compared with 10 years ago, and in some areas, panel service usage appears to be increasing.

Based on the prior review, we conclude that even with wide accessibility of services such as MTurk or Prolific, researchers will still require examining people within their social context via field interviews, or prioritize the ostensible demographic representation and ease offered by panel services. In JPSP, panel services were most often used to obtain demographically representative individuals, and in JCP, JAP, JPSP, field interviews were used to reach either difficult-to-sample populations or keep people within the social environment. These motivations are not so easily addressed by online studies done by gig-economy workers. Therefore, the benefits offered by using curbstoning-susceptible methods are likely to remain, indicating that curbstoning detection has modern relevance. Although vulnerable to fabrication, researchers using these collection strategies can easily minimize skepticism of their findings by providing verification. This verification is crucial because, otherwise, auditing is left to the party providing the data. Stacey (2016) suggests that the one receiving the data should be verifying to separate conflicts of interest from the verification process.

### Table 1: Prevalence Estimates of Curbstoning-Susceptible Methods Among Popular Social and Applied Journals

| Journal | Year | % using panel collection | % using field studies | Overall % |
|---------|------|--------------------------|----------------------|-----------|
| JPSP | 2019-2020 | 6.94 [4.78, 9.1] | 2.25 [0.99, 3.51] | 9.19 [6.74, 11.65] |
| JPSP | 2014-2015 | 3.04 [1.41, 4.67] | 2.81 [1.24, 4.38] | 5.85 [3.63, 8.08] |
| JPSP | 2009-2010 | 0.62 [0.08, 1.33] | 3.95 [2.21, 5.69] | 4.57 [2.71, 6.44] |
| JAP | 2019-2020 | 3.28 [0.12, 6.44] | 1.64 [0.61, 3.89] | 4.92 [1.08, 8.76] |
| JAP | 2014-2015 | 3.98 [1.09, 6.86] | 7.95 [3.96, 11.95] | 11.93 [7.14, 16.72] |
| JAP | 2009-2010 | 3.23 [0.12, 6.34] | 6.45 [2.13, 10.78] | 9.68 [4.47, 14.88] |
| JCP | 2019-2020 | 0 [0.58, 3.42] | 2.29 [0.27, 4.85] | 2.29 [0.27, 4.85] |
| JCP | 2014-2015 | 14.57 [8.94, 20.2] | 1.99 [0.24, 4.21] | 16.56 [10.63, 22.48] |
| JCP | 2009-2010 | 4.12 [0.17, 8.08] | 5.15 [0.75, 9.55] | 9.28 [3.5, 15.05] |

Note. Journals examined were the Journal of Personality and Social Psychology (JPSP; NArticles2019-2020 = 128, NStudies2019-2020 = 533, NArticles2014-2015 = 117, NStudies2014-2015 = 427, NArticles2009-2010 = 144, NStudies2009-2010 = 481), the Journal of Applied Psychology (JAP; NArticles2019-2020 = 76, NStudies2019-2020 = 122, NArticles2014-2010 = 123, NStudies2014-2015 = 176, NArticles2009-2010 = 97, NStudies2009-2010 = 124), and the Journal of Consumer Psychology (JCP; NArticles2019-2020 = 36, NStudies2019-2020 = 131, NArticles2014-2015 = 48, NStudies2014-2015 = 151, NArticles2009-2010 = 50, NStudies2009-2010 = 97). 95% Asymptotic confidence intervals indicated in parentheses.

## Preventing Curbstoning

Researchers use a variety of techniques to prevent curbstoning before it occurs (Harrison & Krauss, 2002; Kennickell, 2015; Stacey, 2016). These methods serve as a deterrent of curbstoning, and address some common factors that promote curbstoning, including: low interviewer motivation, low interviewer ability to complete the survey task, and low chance of being discovered. By implementing these methods, researchers put themselves in a better, though not guaranteed, position to decrease the overall base rate of curbstoning.

### Coaching Interviewers

Coaching interviewers emphasizes the importance of increasing motivation, group norms, and corporate cultures among interviewers (Kiecker & Nelson, 1996). Crespi (1945) recommends researchers keep close relationships with interviewers to increase cohesion and minimize apathy toward the findings.

### Providing Realistic Expectations for Interviewers

Kiecker and Nelson (1996) describe the importance of creating positive work conditions and avoiding unrealistic production quotas, time constraints, and/or work rules. Stacey (2016) warns against providing demographic quotas for interviewers. Rather researchers must know the results that are feasible to obtain.

### Educating Interviewers

Making the interviewers aware that the surveys are monitored for fabrication, may decrease curbstoning as well as emphasize the higher-level goals of the study.

### Incentivizing the Behavior of Interviewers

Harrison and Krauss (2002) recommend employing interviewers with a personal interest in the data quality. Because curbstoning is an act of deception, researchers suggest measuring interviewer characteristics such as morals, integrity, and morale as part of the selection process (Kiecker & Nelson, 1996).

Kennickell (2015) argues that sufficient compensation may create a social norm for what behavior is expected when interviewing. Additionally, researchers should incentivize following the survey's protocol, including behaviors indicative of conscientiousness. Winker (2016) highlights that external incentives can counteract curbstoning, when individual differences associated with curbstoning are unknown during hiring.

### Behaviorally Tracking Interviewers

Requiring indicators that are difficult to fake are suggested as another means to deter curbstoning. Kennickell (2015) suggests using GPS technology to ensure that interviewers are in the expected survey location. Harrison and Krauss (2002) and Gomila et al. (2017) advocate tape recording interviews and require receipts from participants with their signatures.

## Current Detection Methods

Realistic constraints might prohibit implementing curbstoning deterrents. Even if deterred, researchers should still validate the efficacy of prevention methods. In addition to the mitigation strategies offered, Stacey (2016) suggests including items that could signify fraud within the study, including survey questions and metadata. Including specific items offers an additional line of defense, verifying the efficacy of the mitigation strategies. In the following section, we have summarized common detection methods that provide further assurance of the data's integrity. We draw from the methodological groupings of Stacey (2016) and Bredl et al. (2013) as well as from the reviews by Birnbaum (2012), De Haas and Winker (2014), and Menold et al. (2013). Following each class of methods, we provide an overview of their benefits and limitations.

### Recontact Procedures

The most direct method of detecting fake survey data is the recontact method (Bredl et al., 2013; Lavrakas, 2008). Respondents list their phone number, home address, or email within the survey and the researcher then calls a random sample of participants, visits in person, or sends them a message to verify that they indeed took the survey.

**Benefits.** This method is simple to implement because it does not require a ground-truth sample of authentic data. The single-item request for contact information works even with studies with limited time and does require computerized administration. The American Association for Public Opinion Research (2003) suggests that face-to-face recontacting is the most effective method of detecting fraudulent data, with an ostensibly perfect statistical power and Type I error rate, if participants have perfect memory of the interview. The method's effectiveness does not appear to be affected by survey length.

**Limitations.** This method requires associating responses with highly identifying information, preventing usage in sensitive studies. The method's success also depends on participants responding to follow-ups. If nonanswered follow-ups are considered noninterviews, the Type I error rate is inflated. Additionally, this method requires participants to remember taking the original survey and has a limited time window. Hauck (1969) found that fourteen out of 100 noninterviewed persons actually stated that they had been interviewed.

### Completion Rates

Another method of verification examines the "completion rate," which is the total number of participants accepting the interview divided by the total number of requests. Turner et al. (2002) and Hood and Bushery (1997) detected a large number of fabricated interviews by focusing recontact efforts on interviewers who had shown a suspiciously high completion rate. Bredl et al. (2012) used the nonresponse ratio or the proportion of questions remaining unanswered of all questions. This ratio is expected to be lower for curbstoners than for honest interviewers.

**Benefits.** No specialized computers are needed, and no additional questions need to be added to the study, which means that it is one of the most generally applicable methods across different survey designs.

**Limitations.** A separate calibration sample or multiple interviewers is needed to determine the expected completion rate. The statistical power of the method is not invariant to the survey length because completion rates depend on the effort required. Precisely estimating the Type I error of this method would require a large sample of interviewers. Additionally, regional differences may moderate the completion rate (Hood & Bushery, 1997).

### Response Distribution Analysis

This methodology compares the distribution of Likert scale responses to a presumed authentic distribution. Stacey (2016) proposed that the aggregated responses recorded from a collection of surveys should follow a normal distribution. Stacey justified this assumption by positing that when a single outcome is dependent on a large number of independent stimuli, then the probability distribution of that outcome variable will be approximately normal. This method combines all of the responses to 7-point Likert scale questions from an interviewer, and performs a goodness of fit test comparing the collection of responses against a normal distribution. Response distribution methods are often similar to methods used to detect inauthentic responses of job applicants (Kemper & Menold, 2014). These methods focus on the frequency of certain response patterns that favor certain values on a Likert scale. Examples of response pattern analysis include: extreme responding style (Bredl et al., 2012; Porras & English, 2004), middle responding style (Storfinger & Opper, 2011), acquiescent responding style (Messick, 1966), and, preferences for the first or last options in a series of options (Krosnick & Alwin, 1987). Stacey (2016) proposed using a bivariate goodness of fit test to compare the joint distribution of responses from multiple variables from a calibration sample of valid data to the distribution of an interviewer.

**Benefits.** These methods all use Likert scales that already exist within the survey. Therefore, they require no special hardware or additional questions, and are generalizable across different survey designs. Because the methods often use a statistical test to compare distributions, they can potentially have a known Type I error rate, but only once authentic data are collected from a calibration sample.

**Limitations.** Often these methods require a calibration sample or a multitude of interviewers to provide the ground-truth distribution. It is unclear how generalizable the authentic-response distribution is to other populations or based on previous questions answered. Therefore, the Type I error is only an estimate, and may not be generalizable for different populations without collecting a separate calibration sample for the new population.

### Dispersion Analysis

Curbstoners may over- or underestimate how much responses vary. Researchers using this technique compare the variance of an interviewer's questions to the variance of the questions from the rest of the sample (Reuband, 1990). Some authors propose an absolute cutoff value based on the proportion of the variance from an interviewer to the variance of the other interviewers, while other authors use a bootstrap resampling approach to derive a test-statistic representing the unusualness of an interviewer's variance (Schaefer et al., 2005). Stacey (2016) proposed comparing the dispersion or variability of two groups of data, using the Siegel-Tukey test where the variance of a collection of interviewer's responses is compared to the variability of the remainder of the sample data.

**Benefits.** Dispersion analysis is applicable when Likert scales are included within the survey, highlighting their general applicability across social research. Because only self-reported responses are required, the study does not require computer administration.

**Limitations.** Dispersion analysis requires a calibration sample of data, and its Type I error is only known if the calibration sample can be verified as authentic. The statistical power of the method depends on the survey length, because the dispersion is calculated using the number of available items.

### Factor Outliers

Blasius and Thiessen (2012, 2013, 2015) find that interviewer factor mean values are located away from the other interviewers' mean scores. Furthermore, their stereotypical answers reduce the variation of their factor scores, meaning they can be detected by low standard deviations of factor scores. Scores that exceed a certain upper or lower bound of deviation are considered fabricated. Stacey (2016) used fifteen items to measure two factors. The researcher extracted factors from the participants for a given interview and a parallel analysis compares the number of factors extracted to that expected from a randomized dataset.

**Benefits.** These methods are generalizable across a variety of survey designs due to the common usage of multiitem multifactor scales. The method is invariant of survey length. Additionally, they do not require the respondent to use a computer, and could be used in any population demonstrating a similar factor structure.

**Limitations.** These methods require a training sample to determine the appropriate cutoff. Parallel analysis may be able to provide a distributional test, but the distribution of random responses may not correspond to the actual null distribution of a curbstoner. They require adding a multiitem scale, if not already included, marginally increasing the total question count.

### Open-Ended Response Analysis

This category of detection methods requires asking participants to complete an open-ended question with text-input instead of a Likert scale. Open-ended analysis examines the absence of data to detect curbstoning (Bredl et al., 2012). Respondents asked about their ethnicity or gender may often write-in their response if none of the listed options apply. Because curbstoning is motivated by the desire to save effort, curbstoners are less likely to engage in effortful behaviors such as write in text.

Bredl et al. (2012) used the "others-ratio" calculated as the proportion of 'others' answers in all answers where the item 'others' is selectable to detect curbstoning. Hood and Bushery (1997) used omitted open-ended data such as telephone numbers to detect curbstoning. Stacey (2016) proposed asking participants six open-ended questions that required a sentence of response. By comparing the median number of characters of each interviewer's responses to the rest of the interviewers, researchers could identify potentially curbstoned data. Bredl et al. (2012) examined how frequently participants rounded off their answers to questions that asked about precise numeric quantities. Presumably motivated to save time, curbstoners tend to round far more than authentic responders.

**Benefits.** Open-ended analysis methods are fairly generalizable across survey designs that have open-ended questions with an "other" option (e.g., gender, ethnicity) which are commonly asked in demographic sections. They also do not require computer administration; interviewees may type, write, or dictate their answers.

**Limitations.** This method requires a calibration or multiple raters to obtain a ground-truth estimate of the distribution. In studies comparing omissions of open-ended responses in authentic and fabricated data sets, the false alarm rate can be high (82.4%-93.9%), and the distribution of omission, rounding off, and character length are not known prior to the study.

### Duplicate Analysis

Kuriakose and Robbins (2016) proposed the "maximum percent match" (MPM) statistic, which measures the maximum percentage of questions on which each respondent matches any other respondent in the dataset. They argue that the presence of responses that match another respondent's responses for more than 85% of questions indicates likely falsification, due to simulations showing that there is a near-zero percent chance of this occurring through resampling.

**Benefits.** The method offers a potentially nonparametric method to detect fabrication, with ostensibly known Type I error rates, though this property is contentious. The method can be applied to any study with a large number of Likert scale responses.

**Limitations.** Simmons et al. (2016) demonstrated that duplication analysis using the proposed cutoffs overestimates the number of fabrications. The proposed match statistics are not invariant to survey design; the cutoffs for unusualness are extremely sensitive to the number of questions, the number of response options, the number of respondents, and homogeneity within the population. The statistical power of the method is not clear as it only captures a very restricted form of curbstoning, which is item similarity.

### Algorithmic Methods

Curbstoning researchers in recent years are using statistical learning techniques such as cluster analysis, discriminant analysis, and sophisticated predictive models (e.g., random forests). These methods calculate aggregated descriptive statistics from all of the available data to use as predictor variables to determine fabrication. Li et al. (2009) used a composite of variables including participant labor force status, region, urbanicity, experience/supervisory title, interview mode, length, timing, and completion of the interview as predictor variables in a linear model. Bredl et al. (2012) used a combination of indicators, including extreme response, nonresponse, and selection of the "other" category in a K-means cluster analysis and in a discriminant analysis. Birnbaum (2012) analyzed forms consisting of 12 questions, along with a completion time indicator. The author then used a cross-validation feature selection method to determine the optimal number of relevant predictor variables for the model, and then fit a random forest model to those features to predict the known fabrication status in the data. In a separate study, Birnbaum (2012) constructed 664 potential curbstoning detection features by quantifying and transforming the responses given and timing variables recorded, using various descriptive statistics. These predictors and their outcome ("real" or "fake") underwent a logistic regression and random forest to relate the outcome to the predictors.

Researchers have also used theoretically informed scales, rather than general items, to train supervised classification models. Drawing from research examining individual-level applicant faking, Kemper and Menold (2014) train a discriminant analysis classifier using an overclaiming scale (Burns & Christiansen, 2011; Ziegler et al., 2013), and a self-enhancement scale (Kemper et al., 2012). They found predictive utility in those measures with falsifiers attributing a stronger tendency for an overly positive self-description. In addition to using supervised methods, Birnbaum et al. (2012) demonstrated the efficacy of unsupervised methods (multinomial models, s-value technique) at detecting data. These methods perform robust outlier analysis using the item-level responses and completion times as features.

**Benefits.** Relative to all other categories of detection methods, algorithmic methods appear to have the highest statistical power. Bredl et al. (2013) found that the statistical power at detecting four curbstoners varied from 33% to 100% depending on the clustering method used. Birnbaum et al. (2012) attained statistical power between 80 and 90%.

**Limitations.** The algorithmic approach represents an analysis framework, and lacks a set of standard items. Without a theoretically justified set of predictors, the predictive ability is dependent on the survey-length to mine the items available. Also, without a standard set of items, the relevant predictors in one research study may not be relevant for other studies. To avoid overfitting the model, researchers need to use a separate hold-out sample to estimate the Type I error after the parameters have been tuned (Putka, 2018).

### Timing and Behavior Analysis

Because curbstoners are trying to save effort by fabricating data, they may allocate less time to completing each survey or a specific item, compared with a true respondent (Bushery et al., 1999). An interviewer who completes more questions on the same day, turns in surveys at unusual times, or whose average completion time is highly deviant may be fabricating. Birnbaum et al. (2013) also demonstrated that other behavioral indicators measured over a smartphone (e.g., editing times, times scrolled, times swiped) could detect fabrication using deviation and algorithmic analysis.

**Benefits.** This method does not rely on specific questions, and therefore adds no extra questions to the survey. Researchers can estimate the normative distribution from either a separate sample of data, or a collection of interviewers, which is then amenable to statistical testing.

**Limitations.** Examining reactions requires computerized testing to calculate accurately. Further, each new survey must have its own calibration sample to determine the appropriate bounds of deviation. A participant completing a survey in two minutes may be unusual for certain designs but not for others. Additionally, the method's power is tied to the number of items on a survey because each item provides an additional timestamp in the dataset.

### Summary of Different Limitations of Current Methods

Below we summarize the common major limitations discussed for the current detection methods, as well as their implications for accurately detecting curbstoning.

**Time Intensive to Researchers.** Methods such as recontacting participants, while effective, also requires finding and reinterviewing participants. This time intensiveness lowers the efficiency of the process. It also increases the cost to perform detection, and is therefore, less scalable.

**Intrusiveness.** Participants who need to provide highly identifying information, as with "recontacting," may experience discomfort from reduced privacy. This high intrusiveness may be difficult to justify to the participant or ethics review board. Enforcing this requirement may minimize the response rate or create a biased sample by including only participants that find the risk acceptable. Further, designs collecting identifying information could potentially alter the answers to any subsequent sensitive questions.

**Require Calibration Samples.** One of the key limitations shared by every method discussed, except for recontacting, is the need to determine a cutoff for accurately classifying fabrication. Researchers either use a training sample to learn the appropriate cutoffs, or gather data from many interviewers, treating the pooled data as a ground-truth distribution. The consequence of this limitation is an increase in the number of resources required. These types of analyses are especially problematic for collection designs where the indicators differ by context or population, whose thresholds may not generalize to other populations. Methods that use the pooled data for a ground truth cannot make predictions when only a single interviewer collected data.

**Survey Hardware Requirements.** Some methods measure timing with computerized devices. Recording via computers can present additional costs or prohibit studying certain populations.

**Generalizability Across Research Questions.** Fabrication detection methods sometimes only apply to certain collection contexts or survey purposes. Response-based detection methods work only on a collection of many Likert ratings, which may not suit the open-ended nature of a study. Open-ended designs that emphasize longer text responses do not apply to Likert-based questions. Algorithmic methods may discover variables that are relevant for one research question, but not others.

**Inconsistent Statistical Power Based on Survey Design.** Many methods, especially response, timing, algorithm, and duplication-based analysis methods rely on using the full spectrum of available items to determine fabrication. When studies use a greater number of items to detect fabrication, the methods can better estimate the individual's score on that metric. Therefore, the relationships are less attenuated via higher reliability, and the test's statistical power increases. This property indicates that the methods' detection ability is not invariant of the study's design. As a consequence, researchers will not experience uniform success with the methods, and curbstoning is less likely to be detected by studies with fewer items.

**Unclear Type I Error Rates.** The principal limitation found in all current curbstoning methods is the lack of an a priori or statistically justified Type I error rate -- the probability that a person who has not faked collecting data will be predicted to have faked. Many methods provide a simple cutoff value for what counts as fraudulent, based on deviation from a calibration distribution. While the researchers may report a false positive rate based on this distribution, it is not clear how the error rate holds across different samples. Further, many methods lack the ability to control the maximum desired Type I error in a statistically formal way. Because curbstoning is a low base rate event that is rarely observed in more than 6% of interviewers, the false positive rate must be tightly controlled. Even methods that had 100% statistical power, if they also had a false positive rate of 10%, would be more likely to be wrong than right when making predictions regarding a phenomenon with a true base rate less than 5% (Gigerenzer, 2009).

## Proposed Methods

The current article proposes a class of methods to detect survey data fabrication across a variety of contexts. These methods are similar to response distribution methods discussed earlier, but rather than using distributions estimated from the surveys, they use known distributions of biographical and psychological traits. First, we will discuss the methods, and then describe how those methods address the various common limitations of current detection methods.

### Method 1: Detection Via Logarithmic Distributions

**Intuition.** Benford (1938) originally noted that the first digit of many variables including street addresses, populations, death rates, cost data, and lengths of rivers consistently follow a logarithmic distribution (Equation 1) -- a phenomenon known as "Benford's law." The leading (nonzero) digits should be distributed such that the proportion of digits is equal to the log of 1 plus the reciprocal of the digit. Table 2 provides the expected proportions for each nonzero leading digit.

P(d) = log10(1 + 1/d)    (1)

Many statisticians have proposed it as a method to detect fraud (for a review see Nigrini, 2012 and Chi, 2020). It is sometimes used in forensic accounting and other financial domains because it applies to costs (Bredl et al., 2012), however, we seek to extend this method to social surveys.

**Application: Distribution of Leading Digit of Addresses.** Our method leverages the finding that home address numbers follow Benford's law. In cities, addresses tend to be centered around an initial starting point of 0, most addresses will begin with 1, then subsequently 2, and then 3, with increasingly less frequency. A variety of additional research has replicated this finding when collecting address data (Gelman, 2013; Gelman & Nolan, 2017). Asking for only a person's leading address digit provides a general-purpose question applicable to a wide range of surveys.

#### Table 2: Expected Proportion of Leading Digits Under Benford's Law

| Leading digit | Expected proportion |
|--------------|-------------------|
| 1 | 30.10% |
| 2 | 17.61% |
| 3 | 12.49% |
| 4 | 9.69% |
| 5 | 7.92% |
| 6 | 6.69% |
| 7 | 5.80% |
| 8 | 5.11% |
| 9 | 4.58% |

**Implementation.** Researchers should ask the for first digit of participants' home address. After receiving an interviewer's collected data, the researcher computes the observed frequency of each reported digit from 1 to 9. Researchers would then compare those observed counts to the number expected if the digits followed Benford's law. That is, for N collected surveys, each with the first digit of the participant's address, we would expect each digit to occur in the following proportions: "1" to occur N x .301 times; "2" to occur N x .176 times; "3" to occur N x .125 times; "4" to occur N x .097; "5" to occur N x .079 times; "6" to occur N x .067 times; "7" to occur N x .058; "8" to occur N x .051 times; and "9" to occur N x .046 times. Using the chi-square goodness of fit test, commonly used to evaluate deviations from Benford's law (Durtschi et al., 2004; Geyer & Williamson, 2004; Nigrini, 1996), we can obtain the probability of observing a chi-square statistic at least as large as the one we observed, if the data originated from the logarithmic distribution implied by Benford's law (for a visual explanation of the identification process, see Figure 1).

#### Figure 1: Applying Benford's Law to Detect Fabricated Leading Address Digits

Note. This figure shows how to use respondents' street addresses to detect if a dataset with 50 responses, that were collected by a single person, are fabricated. This process compares the frequency of the first digit of people's current street address (1-9) with the expected distribution implied by Benford's law. See the online article for the color version of this figure.

### Method 2: Detection Via Uniform Distributions

**Intuition.** People have difficulty producing uniformly distributed random processes. A pervasive cognitive bias is underestimating various aspects of randomness including, equiprobability, sequence independence, irregularity, and incompressibility (Nickerson, 2002). We emphasize equiprobability, the even sampling of numbers from a distribution, because compared with the other properties of randomness, it is order independent: That is, curbstoning detection is more applicable to studies if the surveys do not need to retain the order they were completed.

People display personal preferences for certain digits when generating random numbers (Mosimann et al., 1995; Preece, 1981; Yule, 1927). The Office of Research Integrity's Division of Research Investigations uses chi-square tests examining the distributions of ostensibly uniformly distributed digits within reports to detect scientific misconduct (ORI Case #93-02). We seek to extend these findings to detect curbstoning at the interviewer-level by asking people to self-report uniformly distributed sequences.

**Application: Distribution of Digits Within Phone Numbers.** We apply the literature on cognitive limitations of generating random uniform sequences to the context of phone numbers. The last four digits of a person's phone number are one example that follows this distribution. The proposed method asks participants to report the last four digits of their phone number. Data fabricators who come across this question should produce digits whose distribution deviates from the expected uniform distribution.

**Implementation.** Researchers would ask for the last four digits of participants' phone number. When all surveys have been delivered from a survey collector, the researcher combines all the four-digit strings into a list of N x 4 numbers. From this list of numbers, the researcher calculates the observed number of times each number (from 0 to 9) occurs. Researchers would then compare the frequency of each digit to the frequency expected in a uniform distribution of equal sample size. If the survey collector returned 50 surveys, then there are 50 x 4 = 200 total numbers reported. Therefore, each digit should occur 200/10 = 20 times, if drawn from a uniform distribution. The observed proportion of all numbers is compared with the expected proportion using a chi-square test goodness of fit test. Excessive deviations (with p-values below a specified Type I error threshold) from what would be expected under a uniform distribution suggest fraudulent data (see Figure 2).

#### Figure 2: Examining Uniform Distribution Frequencies to Detect Fabricated Phone Numbers

Note. This figure shows how to use the last four digits of respondents' phone numbers to detect if a dataset with 50 responses, that were collected by a single person, are fabricated. This process compares the frequency of each digit (0-9) across all numbers with the expected distribution implied by a uniform distribution of digits. See the online article for the color version of this figure.

### Method 3: Detection Via Over- and Under-Estimates of Co-Occurrences

**Intuition.** How large must a gathering of people be to make the probability of finding at least two people with the same birthday at least 50% of the time? This question is known as the "birthday problem," whose probability is calculated with the following formula (Equation 2; Von Mises, 1939):

p(n) = 1 - 365! / (365^n (365 - n)!)    (2)

The answer, n = 23, which produces a probability of 50.73%, surprises most people. In fact, only 41 people are needed to have a 95% chance of finding a least one shared birthday. More than 90% of people overestimate the number, with the modal response being n = 100 (Voracek et al., 2008). The birthday problem demonstrates people's difficulty producing random sequences by avoiding repeating values that just occurred (Reichenbach, 1971). This bias in recognizing and producing a random sample of birthdays offers a method to detect real versus fabricated data.

**Application: Proportion of Near-Birthdays to Non-Near Birthdays.** Our proposed method asks participants to report the date of an autobiographical event that is distributed fairly uniformly, such as their date of birth. Once a researcher has a collection of birth dates from a survey, he or she can compare the observed number of co-occurring, or nearly co-occurring events in the sample, to the expected amount.

Because, in a sample of 50 participants, there is only a high (95%) certainty for one set of birthdays overlapping, we propose making the method more robust by also examining the number of birthdays that miss by a single day. This modification retains the general principle of people incorrectly understanding the co-occurrence of similar events in random uniform distribution. Additionally, this proportion is consistent across all sample sizes. Regardless of the number of people compared, no fewer than .822% of the possible pairs will have birthdays within one day of each other.

**Implementation.** Consider a survey collected from 50 people. Each respondent provides their month and day of birth. There are (50 x 49)/2 = 1,225 possible pairwise comparisons. For each pairwise comparison, the researcher will compare the distance between days within the same 366 day calendar year. January 1st and January 2nd have an absolute difference of 1, January 1st and December 31st have a distance of 365 days. The researcher then calculates the number of times where the difference was 1 or fewer (j) and the number of times the difference was greater than 1 (k). The variables j and k should sum to total number of pairwise comparisons (e.g., 1,225 for 50 birthdays). The researcher compares, using a 2 x 2 chi-square goodness of fit test, the observed number of near birthdays and non-near birthdays to their expected value under a uniform distribution. The uniform distribution implies that (3/number of days in a year) should be the percentage of pairs that are non-near birthdays. These expected values are: expected near birthdays = (j + k) x .00822; expected non-near birthdays = (j + k) x .99178. Observed values that excessively deviate from the expected number of near birthdays versus non-near birthdays (p-value below a specified threshold) under a random uniform distribution suggest fraud (see Figure 3).

#### Figure 3: Examining Uniform Distribution Distances to Detect Fabricated Birthdays

Note. This figure shows how to use the month and day of respondents' birthdays to detect if a dataset with 50 responses, that were collected by a single person, are fabricated. This process compares the frequency of near and non-near birthdays across all birthdays with the expected distribution implied by a uniform distribution of birthdays in a year. The asterisks in the above figure represent the multiplication symbol. See the online article for the color version of this figure.

**Implementation Limitations.** The true underlying distribution of the birthday method does not actually reflect a uniform distribution. We thank an anonymous reviewer for highlighting that doctors in the U.S. work and deliver more babies during the work week than on Saturday or Sunday, this nonuniformity of delivery dates also extends to holidays. When there is a different underlying distribution than the proposed uniform one, we will see a difference in observed Type I error rate versus the one specified by the alpha level. We used data provided by the Social Security Administration and the Center for Disease Control over a span of 21 years (1994-2014) to quantify how much the Type I error rate deviates from the nominal Type I error rate (i.e., .05) when the actual birth rate distribution is not uniform, but a researcher uses the uniform distribution as the expected distribution in the chi-square goodness of fit test.

To examine the Type I error change when using a uniform distribution, we conducted a Monte Carlo simulation that simulated a set N (e.g., 25, 50, 75, 100) birth dates drawn from a given year, whose probability of being selected corresponds to the empirically observed frequency for that year (e.g., 2004). We then apply the birthday method to that collection of dates, to examine whether the number of near and non-near birthdays differs from what would be expected under a uniform distribution. If the chi-square goodness of fit test produces a p-value less than .05, then the collection is flagged as false (a Type I error), otherwise, it is considered genuine. We repeated this process 100,000 times for each year, and then calculated the proportion of times the N samples collected from that year would be flagged as false. This proportion is the Type I error rate of the birthday method for that year. This analysis illustrates how well the uniform distribution assumption performs when the actual rates are not available, and whether it is a sufficient approximation.

We find that the Type I error rate does not exceed the nominal alpha level (.05) when the test is applied to a collection of fewer than 100 surveys (see Table 3). Additionally, obtaining the specific year's birth rate distribution is not crucial. Across years, the error rate tends to be consistent. The range of error rates for any sample size was .007 or less, suggesting expected frequency of near birthdays in the U.S. has been stable year-to-year over this 21 year range. We did find that the average Type I error rate differed depending on the sample size, F(3, 80) = 221.81, p < .01. As the number of surveys examined increases, the Type I error rate deviates more from the nominal alpha level. This trend becomes problematic when examining an interviewer who collects 100 or more surveys. When the collection has more than 100 surveys, the Type I error rate of the test was higher than the desired alpha level in every year examined. Therefore the proportion of near birthdays implied by the uniform distribution (# of pairwise combinations x .00822) will provide a sufficient approximation of the expected number of near birthdays when examining fewer than 100 surveys or when historical information is not available. However, for a more stable Type I error rate, our empirical data suggests that the expected number of near miss birthdays in the U.S. is (# of pairwise combinations x .008356) and non near birthdays is (# of pairwise combinations x .991644). The empirically calculated proportion of near birthdays (.008356) is slightly larger than the value implied by the uniform distribution (.00822) because birthdays are naturally clustered, and using these empirical values produces the lowest deviation between expected and true frequencies of near and non-near birthdays, and shows stability across all years (SDnear birthday proportion = .000043), indicating its acceptability for general usage in the U.S.

#### Table 3: Type I Error Rates When Assuming Birthdays Follow a Uniform Distribution

| Year | N=25 | N=50 | N=75 | N=100 |
|------|------|------|------|-------|
| 1994 | 0.041 | 0.040 | 0.048 | 0.051 |
| 1995 | 0.043 | 0.041 | 0.046 | 0.053 |
| 1996 | 0.043 | 0.040 | 0.047 | 0.052 |
| 1997 | 0.043 | 0.041 | 0.048 | 0.052 |
| 1998 | 0.043 | 0.042 | 0.047 | 0.053 |
| 1999 | 0.044 | 0.042 | 0.048 | 0.053 |
| 2000 | 0.043 | 0.042 | 0.048 | 0.052 |
| 2001 | 0.044 | 0.042 | 0.049 | 0.054 |
| 2002 | 0.046 | 0.042 | 0.050 | 0.053 |
| 2003 | 0.044 | 0.044 | 0.050 | 0.055 |
| 2004 | 0.045 | 0.042 | 0.049 | 0.054 |
| 2005 | 0.045 | 0.044 | 0.051 | 0.057 |
| 2006 | 0.045 | 0.044 | 0.051 | 0.058 |
| 2007 | 0.045 | 0.044 | 0.052 | 0.056 |
| 2008 | 0.046 | 0.043 | 0.050 | 0.055 |
| 2009 | 0.045 | 0.044 | 0.051 | 0.056 |
| 2010 | 0.045 | 0.045 | 0.051 | 0.058 |
| 2011 | 0.047 | 0.044 | 0.051 | 0.057 |
| 2012 | 0.045 | 0.043 | 0.051 | 0.055 |
| 2013 | 0.043 | 0.042 | 0.050 | 0.055 |
| 2014 | 0.044 | 0.044 | 0.049 | 0.054 |

### Method 4: Detection Via Inaccurate Covariation

**Intuition.** Our final proposed method exploits people's lack of knowledge of exactly how multiple variables covary (Mirels, 1976). Social science researchers often measure latent constructs that have a population-level interrelation. Agreeableness tends to be positively related to extraversion, less so with conscientiousness, and negatively with neuroticism. For five latent constructs, there are 5!/(2!(5 - 2)!) = 10 possible construct-construct correlations to know. Correctly inputting scores to preserve those correlations requires both domain knowledge and the working memory or programming ability to have the final dataset demonstrate those correlations.

**Application: Deviation of the Population Mean Correlations From Personality.** We propose implementing the method using the Ten-Item Personality Inventory (Gosling et al., 2003).[1] This measure offers one of the briefest scales of the commonly measured five-factor model. Although researchers should use scales with better psychometric properties to measure personality, the Ten-Item Personality Inventory provides a conservative baseline for the applicability of using personality inventories as a measure of curbstoning detection.

[1] The use of two indicators to measure personality is not psychometrically recommended (Ziegler et al., 2014), and used in this article primarily to illustrate lower bounds when using condensed versions.

**Implementation.** To implement the covariation method, researchers would ask participants to complete the Ten-Item Personality Inventory (Gosling et al., 2003). After receiving an interviewer's surveys, the researcher reverse codes the negatively loading items. Then the researcher follows the scale's recommended procedure for calculating composite scores for each of the five factors by averaging the two items corresponding to that factor. Using the composite scores, the researcher computes the 5 x 5 correlation matrix from the total dataset. The researcher would then perform a covariance difference test by comparing the values of the sample correlation matrix to the population values reported in a large-scale validation article (see Table 4). The chi-square value of the test is compared to the largest chi-value that would be observed 95% of the time, if the sample data came from a distribution with correlations equal to the one expected (see Figure 4). Any nonsingular matrices should be flagged as fabricated.

#### Table 4: Assumed Population Correlation of Big Five Traits on the 10-Item Personality Inventory

| Trait | Extr. | Agree. | Cons. | Neur. | Open. |
|-------|-------|--------|-------|-------|-------|
| Extr. | -- | .05 | .04 | .15 | .35 |
| Agree. | | -- | .12 | .27 | .21 |
| Cons. | | | -- | .18 | .21 |
| Neur. | | | | -- | .22 |
| Open. | | | | | -- |

Note. N = 350; Data extracted from Ehrhart et al. (2009).

#### Figure 4: Examining Correlation Matrix Differences to Detect Fabricated Personality Scores

Note. This figure shows how to use the factor correlation matrix from a five dimension personality test to detect if a dataset with 50 responses, that were collected by a single person, are fabricated. This process compares the correlation coefficient of each pair of higher-order dimensions with the expected correlation implied by a large validation sample in a similar population. The asterisks in the above figure represent the multiplication symbol. See the online article for the color version of this figure.

## Benefits of Proposed Methods

### Controllable Type I Error Rates

The distributions for the authentic responses are well established. Therefore, researchers can examine the collected data's distribution with a chi-square test, which offers a known Type I error rate. This a priori Type I error rate is essential for knowing how likely a collection of data are to be fabricated -- the "positive predictive value."

### Bayesian Integration

The central question when using a detection method is answering the question, "What does it mean to have a positive prediction result when screening?" Most clinicians incorrectly interpret the statistical power of the test as the probability of the positive prediction being correct (Eddy, 1982; Hoffrage & Gigerenzer, 1998). However, the "positive predictive value" is the appropriate way to evaluate the diagnosticity of a "positive" (i.e., "fabricated") prediction (Altman & Bland, 1994). To obtain the correct answer to the question raised above, the statistical power needs to be considered in the context of the underlying base rate and the Type I error rate. Researchers use Bayes's theorem (Equation 3), to formally combine these pieces of information and know the positive predictive value of a "fabricated" prediction.

P(A|B) = P(B|A)P(A) / (P(B|A)P(A) + P(B|not A)P(not A))    (3)

The Bayes's theorem formula updates the statistical power estimate with the base rate probability of obtaining a positive result. This base rate probability, called the "prior," allows imputing subjective or evidence-based knowledge of how likely the data are to be fabricated. The Bayes's theorem formula normalizes the updated statistical power estimate using the sum of the updated power estimate and the probability of a false positive prediction (i.e., Type I error).

Translating Equation 3 to the context of curbstoning gives the following equation (Equation 4).

P(fabricated | positive result) = (statistical power x fabrication base rate) / (statistical power x fabrication base rate + Type I error rate x (1 - fabrication base rate))    (4)

If researchers want to know the probability that a person fabricated data, when the detection method gives a positive result, they would use the above formula using the power and Type I estimates of the detection method. For example, imagine a researcher is using a method with a Type I error of 10%, and statistical power of 100%. If the method predicted a survey collector to have "fabricated" and if the base rate of fabricating data is only 5%, then despite having such high power, there is only a 34.48% chance the survey collector actually fabricated their data, despite having perfect power. Therefore, if we assume a maximum base rate of 5%, then any prior published curbstoning method that has a Type I error rate above 5%, regardless of its statistical power, is uninformative (positive predictive value below 50%). The proposed methods deal with this limitation by allowing the Type I error to be adjusted, rather than have it be an unchangeable property of the method.

### Minimal Intrusiveness

The proposed methods do not require collecting identifying information like recontact methods or long open-ended text prompts. The proposed methods request only part of a person's address or phone number or birth date. This minimal information is less identifying than requesting a person's full address, email, or phone number.

### Does Not Require Calibration Samples

Unlike completion, response, reaction time (RT), dispersion, and algorithmic methods, these methods do not require collecting a sample of data from the same population to determine unusual responses. Also, they do not require collecting multiple interviewers to determine unusual responses. Rather, they measure a distribution whose unusual deviation cutoff is known prior to the analysis. This benefit allows the method to be applied more immediately and to data collected by a single interviewer.

### Applicable Across Administration Modalities

Unlike RT-based methods, the proposed methods can be implemented for surveys collected in any modality (e.g., paper and pencil, telephone, transcribed, computer). Therefore, these methods provide the same access to nontechnical populations that recontact, completion, response, dispersion, duplicate, and algorithmic methods provide.

### Applicable to Different Research Questions

Many of the variables measured by these methods are similar to commonly measured control variables across a variety of psychological research, including birthday ("age"), and personality. Therefore, these questions are either normatively expected, or minimally demanding of the participant, compared with other detection methods that require a large battery of items.

### Power Is Invariant to Survey Format

Many response-based, dispersion, duplication and reaction time, and algorithm-based methods recommend performing the analysis on a large number of items. The proposed methods have a fixed number of items (maximum of 13). Studies of any length that include an item are equally likely to detect fabrication.

## Evaluating the Proposed Methods

It is important to validate the effectiveness of the methods by calculating their Type I and Type II errors using authentic and fabricated responses. Participants' indicated responses may potentially differ from the hypothesized distributions for various reasons such as odd geographic locations, nonrandomly selected phone numbers, nonindependence of birthdays, or measurement variance.

## Method

### Sample

We sampled 326 participants from a population of students taking introductory psychology courses at a U.S. university in the Mid-Atlantic. Data collection was approved by the university's Institutional Review Board. Our sample of participants was 75% female, 77% White, with a mean age of 19.84 years (SD = 1.05). We sampled from this population as research assistants in psychology studies are most likely to be curbstoners, typically originating from this pool. Further, the age range and education level are similar to entry-level data employees, such as collectors at polling organizations.

### Procedure

Participants accessed the study via Qualtrics.com, which asked them to provide honest answers to a set of questions. The first 10 questions of the survey asked participants to describe their personality (used for Detection Method 4). The last set of questions asked participants to describe their personal characteristics (used for Detection Methods 1, 2, and 3). Participants were asked to provide the first digit of their address and the last four digits of their phone number and birthdate. The following questions were regarding participants' race and gender (and calculating participant demographics).

After completing the preliminary survey, participants were asked to recomplete the same survey 50 times, but from the perspective of 50 different participants. To increase participants' motivation to create believably fake responses, they were guaranteed that three participants who provided data whose statistical characteristics are closest to that of actual participants (those who faked the best) would win a $25 Visa gift card.

### Measures

The following measures were used during both the initial survey, and the fabrication response generation:

**Ten-Item Personality Inventory.** Participants completed the Ten-Item Personality Inventory (Gosling et al., 2003), which contains five pairs of items, each corresponding to a higher-order factor of the Big Five.

**First Digit of Their Address.** We asked participants to specify the first digit of their address. The survey validation feature only allowed responses that contained a single numeric value.

**Last Four Digits of Their Phone Number.** We asked participants to report the last four digits of their cell phone number. The survey validation feature required four digits to be entered.

**Date of Birth.** We asked participants their date of birth. This variable also provided demographic information.

**Effortful Responding Check.** We included a motivation check question at the end of the survey, which asked participants to verify that they were responding seriously and following the instructions. Research suggests that this check improves the quality of responses (Aust et al., 2013). A total of 166 participants admitted to not answering seriously, and were excluded from the analysis, leaving a final total of 160 participants used in the analysis. Including these participants who failed the effort check tended to increase the power estimates and the Type I error estimates by approximately 2%, with the exception of the birthday method, whose Type I error increased by 6%.

### Authentic Dataset

Participants' first set of responses to the survey (prior to being asked to fabricate data) were used to develop the authentic dataset. By combining a subset of these responses into a dataset of size n (i.e., 50), we can examine how often the methods incorrectly classify the collection as "fake." The proportion of authentic data sets classified as "fake" is the false-positive rate (Type I error) of the detection method. We used a resampling procedure that other fabrication researchers have used to generate smaller, varied samples of authentic data from a larger pool of authentic data to obtain distributional information (Gomila et al., 2017). Each participant created a collection of 50 fake responses. Therefore, we create authentic data sets of equal size to provide an estimate of the detection method's Type I error when examining data sets with 50 participants. Specifically, we drew a random sample of 50 participants, from the total sample of 160 participants. We repeated this process 1,000 times to generate 1,000 different combinations of 50 authentic responses (see Figure 5).

#### Figure 5: Process of Bootstrap Sampling All Authentic Data to Create Collections of N Authentic Data

Note. This figure shows how we evaluated a method's Type I error when classifying a collection of authentic data. We synthesized 1,000 datasets from a collection of N = 160 authentic responses by randomly sampling n < N (e.g., 50) points from the original N authentic responses.

### Calculating Observed and Expected Distributions

**First Address Digit.** The first address digit method is provided a sample of 50 responses, where each response is the first digit of the participant's address. We calculated the observed distribution by counting the number of times the following digits occurred: 1, 2, 3, 4, 5, 6, 7, 8, and 9 (zero is excluded in Benford's law). We also calculated the expected number of times each digit should occur if the data followed a Benford's law distribution (equation 1).

**Last Four Digits of a Phone Number.** The phone number method is provided a sample of 50 responses, where each response is the last 4 digits of a respondent's phone number. We counted the number of times each digit (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) occurred in all of the 50 phone numbers. This table of digit frequencies is the observed distribution. We compared that to the expected number of times that each digit should occur if the data followed a uniform distribution.

**Birthdays.** We created a distribution of near birthdays (birthdays within 1 day of each other) versus non-near birthdays among the 50 responses. The differences were calculated assuming the days fell on the same year. This expected distribution was therefore two numbers: the number of near birthdays in the sample, and the number of non-near misses. We calculated the expected number of birthdays that fall within 1 day of each other and those that do not, if the dates came from a uniform distribution.

**Personality.** We calculated the five higher-order factor scores on the Ten-Item Personality Inventory for each participant by performing the appropriate reverse coding, and averaging each related pair of items. We then calculated the correlation matrix between those variables for the 50 responses. We used the correlation matrix reported in a large-scale (N = 902) validation sample (Table 4; Ehrhart et al., 2009) as the expected matrix.

### Fabrication Detection and Evaluation

For the addresses, phone numbers, and birthdays with discrete distributions, we performed a chi-square test goodness of fit test comparing the observed and expected distribution for each collection of surveys. The critical chi-square value for the test was calculated via simulation, by randomly sampling 10,000 times from the expected distribution, and observing what chi-square value 95% of the cumulative density fell below. If the resulting chi-square value between the observed data and the expected counts was less than the critical chi-square value, then we failed to reject the null hypothesis, and concluded the data were authentic. If the chi-square value was greater than the critical chi-square value, then we predicted that the collection of data was fabricated. Alternatively, the researcher could use the standard, number of discrete categories minus 1 degrees of freedom for the chi-square goodness of fit test. For the personality data, we used a test which calculates a chi-square value corresponding to the difference between correlation matrix entries (Steiger, 1980). We evaluated each method in terms of its Type I error rate (the proportion of authentic collections of data predicted to be fabricated), and its statistical power (the proportion fabricated data sets predicted to be fabricated). Note that power is highly dependent on the motivation and skill of the sample and may vary between samples. These results only provide an estimate of power in a sample assumed to be similar to populations that often collect data (e.g., research assistants and entry-level employees). The different methods have also been written into the R-programming language that researchers can use to implement the methods, included in the online supplemental material (curbstoningdetection.R).

## Results

### Detection Via Non-Benford Distribution of First Address Digit

The address test correctly classified 80.6% of fabricated data sets as fraudulent, indicating high power when there are 50 people in a dataset (see Table 5). Additionally, for each bootstrapped dataset, which contained 50 authentic responses, we applied the same test and found that the test classified 12.6% of those responses as fraudulent.

The test demonstrated statistical power values of 73.13%, 63.13%, and 47.5% when examining a collection of 40, 30, and 20 responses, respectively; corresponding Type I error rates were 9%, 9%, and 10%, which indicate that Type I error is fairly constant across sample sizes, though 4% higher than expected (see Table 5). Confidence intervals around each error find that the error rates for 50 and 20 surveys were statistically significantly higher than the desired alpha level of .05. Therefore, the method is able to detect fraudulent responses, but the false positive error rate is consistently higher by approximately 4% of the desired rate, with additive increases in power for increasing sample sizes.

### Detection Via Nonproximate Birthdays

The birthday method correctly classified 48% of fabricated data sets as fraudulent, when there were 50 people in a dataset. For each bootstrapped dataset, which contained 50 authentic responses, we applied the same test and found that the test only classified 1.8% of those responses as fraudulent. The test demonstrated statistical power of 43.13%, 35.63%, and 25.63% when examining a collection of 40, 30, and 20 responses, respectively; corresponding Type I error rates were 4%, 1%, and 1%. None of the Type I error rates were significantly higher than .05, though the error rates for surveys with 30 and 20 responses were significantly lower. This lower error is not problematic for the viability of the test because it means that the test may make conservative assumptions about the underlying distribution. Therefore, the method does not exceed the controlled error rate, though none of the power rates surpass 50%.

### Detection Via Nonuniform Distribution of Phone Numbers

The phone number method correctly classified 80% of fabricated data sets as fraudulent when there are 50 people in a dataset. The test only classified 1.2% of authentic responses as fraudulent. When examining a collection of 40, 30, and 20 responses, the test demonstrated statistical powers of 73.13%, 60.63%, and 49.38%, respectively; the corresponding Type I error rates were 1.9%, 1.5%, and 1.4%. All confidence intervals included .05. Therefore, the methods attain a controlled error rate, and were likely to be right when there are at least 30 survey responses collected by a surveyor.

### Detection Via Inaccurate Correlation

The correlation matrix test correctly classified 90% of fabricated data sets as fraudulent, indicating high power when there are 50 people in a dataset. The test had a Type I error rate of 8.80%. The test demonstrated statistical powers of 77.5%, 51.88%, and 23.13% when examining a collection of 40, 30, and 20 responses, respectively; the corresponding Type I error rates were 8%, 8%, and 6%. None of the error rates were statistically different from the nominal Type I error rate. Therefore, the correlation method is able to detect fraudulent responses, with a controlled error rate, and likely to be right for our sample of at least 30 interviewed participants.

### Table 5: Power and Type I Error of the Proposed Methods of Various Survey Collection Sizes

| Method | Sample size | Power | Type I error |
|--------|------------|-------|-------------|
| Address | N = 50 | .81 [.74, .86] | .13 [.08, .19] |
| Address | N = 40 | .73 [.66, .80] | .09 [.05, .14] |
| Address | N = 30 | .63 [.55, .71] | .09 [.05, .14] |
| Address | N = 20 | .48 [.40, .56] | .10 [.06, .16] |
| Birthday | N = 50 | .48 [.40, .56] | .02 [.00, .05] |
| Birthday | N = 40 | .43 [.35, .51] | .04 [.01, .08] |
| Birthday | N = 30 | .36 [.29, .44] | .01 [.00, .04] |
| Birthday | N = 20 | .25 [.19, .32] | .01 [.00, .04] |
| Phone number | N = 50 | .80 [.73, .86] | .01 [.00, .04] |
| Phone number | N = 40 | .73 [.66, .80] | .02 [.00, .05] |
| Phone number | N = 30 | .61 [.53, .59] | .02 [.00, .05] |
| Phone number | N = 20 | .50 [.42, .88] | .01 [.00, .04] |
| Personality correlation | N = 50 | .90 [.84, .94] | .09 [.05, .14] |
| Personality correlation | N = 40 | .77 [.70, .83] | .08 [.04, .13] |
| Personality correlation | N = 30 | .51 [.43, .59] | .08 [.04, .13] |
| Personality correlation | N = 20 | .23 [.17, .30] | .06 [.03, .11] |

Note. If the collection of N surveys had a test statistic that exceeded the 95th percentile of test statistics under the null distribution, data was assumed to be fake. Values in parentheses represent 95% confidence intervals using the binomial exact calculation.

### Power Under Low Alpha Levels

We set the prior analyses' Type I error to be 5% from common statistical convention. However, because the prevalence of curbstoning is rather low, a researcher may want to set the Type I error rate to be at 1% or lower. We conducted additional analysis of N = 50 collected surveys. We set the alpha level to a maximum Type I error rate of 1%, and found that that statistical power was uniformly about 10% lower, but are still relatively higher or equal to other methods in extant literature (poweraddress = 74%; powerbirthday = 42%; powerphone number = 70%; powercorrelation = 78%). At an alpha level of .001, 3 of the 4 tests retain positive predictive values above 50% (poweraddress = 54%; powerbirthday = 31%; powerphone number = 57%; powercorrelation = 56%). The observed Type I errors for those were all at or below the nominal alpha levels of .01 and .001.

### Summary of Results for Individual Methods

Across all methods, we obtained the highest rate of power with at least 50 participants. Nearly all Type I error rates were statistically indistinguishable or slightly lower than the nominal alpha levels, with the exception of the address method, whose error rate was statistically different for two cases. Therefore, we believe the address method should be used with the most caution when controlled alpha levels are desired.

### Enhancing Predictions by Combining Approaches

We examined the effectiveness of combining the predictions into a single composite score. The composite score was simply the sum of the number of methods that predicted the dataset was fabricated (p < .05). If at least half of the scores indicate fabrication, then we hypothesize fabrication, otherwise, we establish that the data are authentic.

When the sample size of 50 was tested using the complete combination of metrics, the Type I error rate was 1.1% and the statistical power of 94.36%, meaning we were able to detect the fake responses nearly all the time. Using the sample of 40 responses, we found a Type I error rate of 1.5% and a power of 88.13%. In the sample of 30, we found a Type I error rate of 1.8% and were able to detect false responses 70% of the times. Our smallest sample size tested, N = 20, had a Type I error rate of .6% and we correctly detected fake responses 41.25% of the time. Overall, there was an increase in our ability to detect curbstoning correctly using a composite of all methods, which highlights the benefits researchers would experience by incorporating a variety of the proposed questions.

### Validation of the Methods With an Additional Sample

To provide supporting evidence of the method's estimated properties, and their reliability, we collected a separate sample of 63 participants who completed the same protocol as in the original study. Of those 63 participants, 52 passed the seriousness check. We found the greatest support for the methods when using a sample of 50 participants, therefore, we recalculated the power and Type I error of the method using that sample size examining for deflation of the original estimates. The Type I error rate of the address method was 0, and the statistical power was .73. The Type I error rate of the birthday method was 0, and the statistical power was .52. The Type I error rate of the phone number method was .01, and the statistical power was .77. The Type I error rate of the correlation method was 0, and the statistical power was .75. These cross-validated estimates demonstrate performance statistically indistinguishable from the nominal Type I error (the smallest p-value from a one-sample proportion test is .12). The estimates all display statistical power within the confidence intervals reported, with the exception of the correlation method, whose power is 15% lower than the original estimate.

### Integration With Machine Learning Algorithms

Prior research on curbstoning highlights the superiority of machine learning approaches to detect fabrication with high power and low error. The proposed methods can be integrated with machine learning to enhance their effectiveness, with the trade-off of losing an a priori Type I error rate and requiring a training/calibration sample. We trained a random forest classifier, used by Birnbaum (2012), on the original fabricated data of 160 participants, and on 160 bootstrapped samples of authentic data (see Figure 6 for an in-depth illustration). To find optimal hyperparameter settings, we used a threefold cross-validated 50-iteration randomized search through the maximal depth, percentage of predictors considered, number of samples in a split, and the number of trees. We conducted the analysis separately for each method's predictors which were based on distributional information similar to that used by the statistical methods:

- **Address method:** The proportion that each digit occurred, the mean, standard deviation, skew, and kurtosis of the addresses listed.
- **Birthday method:** The number of days that were within 1 day, 1 week, 2 weeks, 3 weeks, 4 weeks, 5 weeks, 6 weeks, and 7 weeks of each other, as well as the number of days that were 8 more weeks apart.
- **Phone number method:** The proportion that each digit from zero and nine occurred, the mean value, the standard deviation, skew, and kurtosis of all of the individual digits.
- **Correlation method:** The pairwise item correlations, means, and standard deviations of the five factors.

We trained four separate models to examine situations where each interviewer collected either 50, 40, 30, or 20 survey responses. When cross-validated on the separate set of 52 participants' fabricated data and 52 bootstrapped samples of authentic data, we found that our proposed methods' predictive ability was enhanced by using machine learning (see Table 6). Nearly all of the power estimates are all significantly greater than power from the hypothesis tests. The increase in power comes at the expense of sometimes greater Type I error rates. Interestingly, the correlation method makes perfect predictions for data sets even as small as 20. The address method likewise obtained extremely high power (.80%) with no Type I errors for data with as few as 30 collected interviews. Therefore, the proposed methods' achieve high precision efficiently when combined with the algorithmic approach. Additionally, integrating the methods with machine learning provides strong predictions for smaller data sets that were not predicted well with a significance testing framework.

#### Figure 6: Process of Applying Machine Learning to the Address Method and Its Validation

Note. A visual representation of the applied the algorithmic approach to detect curbstoning. The above figure illustrates training a random forest to predict if a collection of 30 responses were fabricated by a single individual or instead from a set of 30 authentic people, using the first digit of people's addresses from the 30 responses. AUC ROC = area under the receiver operating characteristic curve.

### Table 6: Power and Type I Error for the Proposed Methods for Various Sample Sizes When Implemented in a Machine Learning Model

| Method | Sample size | Power | Type I error |
|--------|------------|-------|-------------|
| Address | N = 50 | .96 [.87, .99] | .00 [.00, .07] |
| Address | N = 40 | .92 [.82, .98] | .00 [.00, .07] |
| Address | N = 30 | .83 [.70, .92] | .00 [.00, .07] |
| Address | N = 20 | .83 [.70, .92] | .13 [.06, .26] |
| Birthday | N = 50 | .79 [.65, .89] | .00 [.00, .07] |
| Birthday | N = 40 | .53 [.40, .58] | .02 [.00, .10] |
| Birthday | N = 30 | .63 [.49, .76] | .21 [.11, .35] |
| Birthday | N = 20 | .55 [.41, .70] | .26 [.16, .41] |
| Phone number | N = 50 | .86 [.74, .94] | .00 [.00, .07] |
| Phone number | N = 40 | .83 [.70, .92] | .02 [.00, .10] |
| Phone number | N = 30 | .85 [.72, .93] | .12 [.04, .23] |
| Phone number | N = 20 | .82 [.70, .92] | .19 [.10, .32] |
| Personality correlation | N = 50 | 1.00 [.93, 1.00] | .00 [.00, .07] |
| Personality correlation | N = 40 | 1.00 [.93, 1.00] | .00 [.00, .07] |
| Personality correlation | N = 30 | 1.00 [.93, 1.00] | .00 [.00, .07] |
| Personality correlation | N = 20 | 1.00 [.93, 1.00] | .00 [.00, .07] |

Note. Values in parentheses represent 95% confidence intervals using the binomial exact calculation.

## Discussion

Our study found that many of the methods proposed could obtain high levels of power (.80%) with at least 50 participants, even with the false positive rate set as low as 1%. When interviewers collect more data, the methods offer greater statistical power. Combining the methods provided even greater statistical power with similar error rates, and incorporating the questions into machine learning offered even greater predictive ability, at the expense of guaranteed error rates and requiring collecting a sample of training data.

### Limitations Presented by Partial Fabrication

The proposed technique is designed to detect instances where none of the data were collected, and all of the data have been imputed, which is the most common form of fabrication (reported rates between 72% and 100%: Hood & Bushery, 1997; Schaefer et al., 2005; Schreiner et al., 1988). We conducted analyses using the 50-participant sample of surveys to estimate the power to detect partial fabrication. For each collection of fake responses, we randomly removed a given percentage of cases and replaced them with an equal number of true responses from the actual data. We repeated the process 1,000 times to better estimate the true power of the method due to the randomness of sampling cases. We examined scenarios where 20%, 30%, 40%, 50%, 60%, 70%, and 80% of the data were fabricated. We found that each method's statistical power increased linearly as the percentage of data that was fabricated increased (see Table 7). When the data consisted of at least 60% fabricated data, then the address, personality, and aggregation of all methods had at least 50% power. Therefore, their guesses were more likely to be right than wrong. However, when only half or fewer are fabricated, the statistical power fell below 50%.

#### Table 7: Power of the Methods to Detect Fabrication, When a Percentage of the Data is Fabricated

| Method | 20% | 30% | 40% | 50% | 60% | 70% | 80% |
|--------|-----|-----|-----|-----|-----|-----|-----|
| Address | .20 | .28 | .36 | .47 | .54 | .62 | .71 |
| Birthday | .14 | .19 | .20 | .26 | .27 | .24 | .53 |
| Phone number | .08 | .15 | .23 | .38 | .46 | .54 | .69 |
| Personality correlation | .12 | .21 | .29 | .37 | .50 | .58 | .71 |
| Combined | .11 | .19 | .26 | .44 | .55 | .67 | .86 |

### Seven Guidelines for Detecting Fabrication

Based on the literature review and the analyses presented in this article, we suggest that identifying faked data is possible and enhanced under certain conditions. Given the potential threat of curbstoning, researchers using survey panels or field data collection should follow these specific steps to validate data against curbstoning:

1. Survey designs that incorporate panel services or field collection should incorporate at least one potential curbstoning detection method. International contexts had the highest rates of curbstoning (up to 20 times the base rate) in the literature review. Articles performing these checks should be treated by reviewers and readers similar to papers that preregister hypotheses or conduct a replication. They provide further evidence that the results are reliable, and reduce the concerns that authors need to address in the review process. The burden of proof must be on the researcher to demonstrate validity and not on the reviewer or editor to demonstrate the data aren't authentic.

2. For maximum predictive ability, we recommend using a form of the personality check, and use the phone question if strongly limited by time. Both have power near 80% and have Type I errors lower or equal to the nominal alpha level. They also show near perfect power and error when used with machine learning.

3. Researchers should treat the questions as a framework and use equivalent questions to counteract a curbstoner's knowledge of a specific detection technique. Although we tested the short-form Big Five, this test was intended as a conservative baseline. Study designs already incorporating scales with at least five-items, can implement the framework discussed, if large scale validation reports the interitem correlation matrix. Asking for the last four digits of the phone number can be replaced by asking about any uniformly distributed event from 0-9 including serial numbers, ID numbers, license numbers, and so forth.

4. All interviews should be labeled by the sole interviewer who collected it. This guideline facilitates uniquely identifying the source if a problem is found. Additionally, a dataset entirely fabricated by a single person is easier to detect than an dataset collected by multiple people where one person curbstones and the other does not (see section on partial fabrication).

5. Interviewers should be assigned to collect at least 50 responses each to provide adequate statistical power. At this sample size, most methods displayed statistical power at least 80%, and many combinations of methods displayed power above 90%. If collecting 50 responses is not possible, then using a machine learning approach with the questions improves power at the expense of not being able to control the Type I error rate and requiring a calibration sample.

6. Researchers should use different Type I error rates depending on whether testing an individual versus conducting an audit. Researchers may be interested in testing a single person due to a suspicion that data were collected inappropriately based on other factors. Although the base rate of curbstoning is between 1% and 2% across reported audits, this base rate was calculated across all interviewers. By isolating the test to cases of high suspicion, the base rate prior value increases, thereby increasing the positive predictive value of the test. We suggest using a 5% alpha level for testing highly suspect people (subjectively assigned a 10% probability of having fabricated data), which provides a positive predictive value of at least 66% for detection methods that have power near 90%. However, if using subjective priors is uncomfortable or if using the test to audit a large segment of people, where the base rate is closer to 1%, then we recommend setting the alpha level of a single test to .001. Based on the low alpha analysis described earlier, the positive predictive value (ppv) for the test with a .001 alpha level under a 1% base rate would be informative: ppvAddress = 85%, ppvBirthday = 76%, ppvPhone = 84%, ppvCorrelation = 85%, with statistical power is still above 50% for most tests. Therefore, the majority of fabrication will be detected, and a positive result is highly likely to be correct.

7. If an interviewer's collection is predicted to be fabricated, then researchers are encouraged to explore more time intensive procedures such as conducting follow-up calls with participants. If no means of investigating further are possible, researchers should conduct sensitivity analysis with and without the data to determine if the interpretation of the results changes when the results are included, similar to other scientific misconduct guidelines (Simonsohn et al., 2015; Steegen et al., 2016). If the qualitative interpretation is unaltered, then the choice of including or discarding the suspect data is less impactful. However, results should be reported with the caveat of unusual performance of any interviewers and the sample size affected. If including the suspect data alters the results, then the researcher has evidence that the data should be collected again. This data recollection is important to bring the study to the predetermined level of statistical power and to prevent discarding data solely to improve one's results.

### The Future of Faking Data

We anticipate that the future of curbstoning may be less of a lone endeavor because the purpose of curbstoning is to save time and effort. At some point, curbstoners working individually would not be able to save time by taking the complex steps required to subvert the method. Instead, professionally developed systems of answer generation may one day be commonly offered as a service. In computer science, generative adversarial networks (GANs) are already able create information used in many other curbstoning detection methods. GANs are artificial neural networks that can be given a training set, and learn how to generate new data with the same statistical properties (Goodfellow et al., 2014). GANs work by simultaneously training two parts of machine learning model in an adversarial relationship: a data generator that produces authentic-seeming content and a discriminator that tries to determine if the generated content is authentic using prior data and the newly generated content as training examples. By iterating between optimizing generation and discrimination, the produced content becomes increasingly authentic. GANs underly the hyperrealistic fabricated images/videos, called "deep fakes" that can be created freely online and have been used to automate developing false social media profiles (Satter, 2019). GANs have been used to impute item-level information (Yoon et al., 2018), forge signatures (Wang & Jia, 2019), respond to open-ended questions (Yang et al., 2017), and impersonate voices (Gao et al., 2018) -- outputs used by some existing curbstoning detection methods. It is plausible that, with enough demand, a curbstoning Artificial Intelligence would bridge the gap between entry-level interviewer and efficient data fabrication.

## Conclusion

The proposed data fabrication methods provide researchers simple ways to check if a third-party data collector, such as a research assistant or panel service, may have falsified the responses of a survey. These methods find a balance between many limitations common among curbstoning detection methods, and offer new benefits as well. By applying more statistical rigor to data verification, scientists can increase the validity and reproducibility of their findings.

## References

Altman, D. G., & Bland, J. M. (1994). Statistics notes: Diagnostic Tests 1: Sensitivity and specificity. BMJ, 308(6943), 1552. https://doi.org/10.1136/bmj.308.6943.1552

American Association for Public Opinion Research. (2003). Interviewer falsification in survey research: Current best methods for prevention, detection and repair of its effect. https://www.aapor.org/AAPOR_Main/media/MainSiteFiles/falsification.pdf

Aust, F., Diedenhofen, B., Ullrich, S., & Musch, J. (2013). Seriousness checks are useful to improve data validity in online research. Behavior Research Methods, 45(2), 527-535. https://doi.org/10.3758/s13428-012-0265-2

Benford, F. (1938). The law of anomalous numbers. Proceedings of the American Philosophical Society, 78(1938), 551-572.

Bentley, F. R., Daskalova, N., & White, B. (2017, May). Comparing the reliability of Amazon Mechanical Turk and Survey Monkey to traditional market research surveys. Proceedings of the 2017 CHI Conference Extended Abstracts on Human Factors in Computing Systems - CHI EA '17 (pp. 1092-1099). https://doi.org/10.1145/3027063.3053335

Biemer, P. P., & Lyberg, L. E. (2003). Introduction to survey quality. Wiley.

Birnbaum, P. P. (2012). Algorithmic approaches to detecting interviewer fabrication in surveys [Doctoral dissertation, Department of Computer Science and Engineering, University of Washington].

Birnbaum, B., Borriello, G., Flaxman, A. D., DeRenzi, B., & Karlin, A. R. (2013). Using behavioral data to identify interviewer fabrication in surveys. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems - CHI '13 (pp. 2911-2920). https://doi.org/10.1145/2470654.2481404

Birnbaum, B., DeRenzi, B., Flaxman, A. D., & Lesh, N. (2012, March). Automated quality control for mobile data collection. Proceedings of the 2nd ACM Symposium on Computing for Development - ACM DEV, Atlanta, GA (p. 1). https://doi.org/10.1145/2160601.2160603

Blasius, J., & Thiessen, V. (2012). Assessing the quality of survey data. Sage.

Blasius, J., & Thiessen, V. (2013). Detecting poorly conducted interviews. In P. Winker, N. Menold, & R. Porst (Eds.), Interviewers' deviations in surveys: Impact, reasons, detection and prevention (pp. 67-88). Peter Lang.

Blasius, J., & Thiessen, V. (2015). Should we trust survey data? Assessing response simplification and data fabrication. Social Science Research, 52, 479-493. https://doi.org/10.1016/j.ssresearch.2015.03.006

Boas, T. C., Christenson, D. P., & Glick, D. M. (2020). Recruiting large online samples in the United States and India: Facebook, Mechanical Turk, and Qualtrics. Political Science Research and Methods, 8(2), 232-250. https://doi.org/10.1017/psrm.2018.28

Bredl, S., Kotschau, K., & Winker, P. (2012). A statistical approach to detect interviewer falsification of survey data. Survey Methodology, 38, 1-10.

Bredl, S., Storfinger, N., & Menold, N. (2013). A literature review of methods to detect fabricated survey data. In P. Winker, N. Menold & R. Porst (Eds.), Interviewers' deviations in surveys (pp. 3-24). Peter Lang Academic Research.

Burns, G. N., & Christiansen, N. D. (2011). Methods of measuring faking behavior. Human Performance, 24(4), 358-372. https://doi.org/10.1080/08959285.2011.597473

Bushery, J. M., Reichert, J. W., Albright, K. A., & Rossiter, J. C. (1999). Using date and time stamps to detect interviewer falsification. Proceedings of the Section on Survey Research Methods (pp. 316-320). American Statistical Association.

Chi, D. (2020). First digit phenomenon in number generation under uncertainty: Through the lens of Benford's law [Unpublished master's thesis]. The University of Sydney, New South Wales, Australia.

Crespi, L. P. (1945). The cheater problem in polling. Public Opinion Quarterly, 9(4), 431. https://doi.org/10.1086/265760

De Haas, S., & Winker, P. (2014). Identification of partial falsifications in survey data. Statistical Journal of the IAOS, 30(3), 271-281. https://doi.org/10.3233/SJI-140834

Durtschi, C., Hillison, W., & Pacini, C. (2004). The effective use of Benford's law to assist in detecting fraud in accounting data. Journal of Forensic Accounting, 5(1), 17-34.

Eddy, D. M. (1982). Probabilistic reasoning in clinical medicine: Problems and opportunities. In D. Kahneman, P. Slovic, & A. Tversky (Eds.), Judgment under uncertainty (1st ed., pp. 249-267). Cambridge University Press. https://doi.org/10.1017/CBO9780511809477.019

Ehrhart, M. G., Ehrhart, K. H., Roesch, S. C., Chung-Herrera, B. G., Nadler, K., & Bradshaw, K. (2009). Testing the latent factor structure and construct validity of the Ten-Item Personality Inventory. Personality and Individual Differences, 47(8), 900-905. https://doi.org/10.1016/j.paid.2009.07.012

Funk, C., Hefferon, M., Kennedy, B., & Johnson, C. (2019). Trust and mistrust in Americans' views of scientific experts. Pew Research Center. https://www.pewresearch.org/Science/2019/08/02/Trust-and-Mistrust-Inamericans-Views-of-Scientific-Experts

Gao, Y., Singh, R., & Raj, B. (2018, April). Voice impersonation using generative adversarial networks. 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 2506-2510). https://doi.org/10.1109/ICASSP.2018.8462018

Gelman, A. (2013). Benford's law and addresses. https://statmodeling.stat.columbia.edu/2013/06/01/benfords-law-and-addresses/

Gelman, A., & Nolan, D. (2017). Teaching statistics: A bag of tricks. Oxford University Press.

Geyer, C. L., & Williamson, P. P. (2004). Detecting fraud in data sets using Benford's law. Communications in Statistics. Simulation and Computation, 33(1), 229-246. https://doi.org/10.1081/SAC-120028442

Gigerenzer, G. (2009). Making sense of health statistics. Bulletin of the World Health Organization, 87(8), 567-567. https://doi.org/10.2471/BLT.09.069872

Gomila, R., Littman, R., Blair, G., & Paluck, E. L. (2017). The audio check: A method for improving data quality and detecting data fabrication. Social Psychological & Personality Science, 8(4), 424-433. https://doi.org/10.1177/1948550617691101

Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A., & Bengio, Y. (2014). Generative adversarial nets. In Z. Ghahramani, M. Welling, C. Cortes, N. D. Lawrence, & K. Q. Weinberger (Eds.), Advances in neural information processing systems (Vol. 27, pp. 2672-2680). Curran Associates, Inc. http://papers.nips.cc/paper/5423-generative-adversarial-nets.pdf

Gosling, S. D., Rentfrow, P. J., & Swann, W. B. (2003). A very brief measure of the Big-Five personality domains. Journal of Research in Personality, 37(6), 504-528. https://doi.org/10.1016/S0092-6566(03)00046-1

Harrison, D. E., & Krauss, S. I. (2002). Interviewer cheating: Implications for research on entrepreneurship in Africa. Journal of Developmental Entrepreneurship, 7(3), 319-330.

Hauck, M. (1969). Is survey postcard verification effective? Public Opinion Quarterly, 33(1), 117-120. https://doi.org/10.1086/267675

Hoffrage, U., & Gigerenzer, G. (1998). Using natural frequencies to improve diagnostic inferences. Academic Medicine, 73(5), 538-540. https://doi.org/10.1097/00001888-199805000-00024

Hood, C. C., & Bushery, J. M. (1997). Getting more bang from the reinterviewer buck: Identifying "At Risk" interviewers. Proceedings of the Section on Survey Research Methods (pp. 820-824). American Statistical Association.

Kemper, C. J., & Menold, N. (2014). Nuisance or remedy? The utility of stylistic responding as an indicator of data fabrication in surveys. Methodology, 10(3), 92-99. https://doi.org/10.1027/1614-2241/a000078

Kemper, C. J., Beierlein, C., Bensch, D., Kovaleva, A., & Rammstedt, B. (2012). Eine Kurzskala zur Erfassung des Gamma-Faktors sozial erwunschten Antwortverhaltens: Die Kurzskala Soziale Erwunschtheit-Gamma [A short scale for recording the gamma factor socially desirable response behavior: The short scale Social Desirability-Gamma (KSE-G)]. KSE-G.

Kennickell, A. (2015). Curbstoning and culture. Statistical Journal of the IAOS, 31(2), 237-240. https://doi.org/10.3233/sji-150900

Kiecker, P., & Nelson, J. E. (1996). Do interviewers follow telephone survey instructions? Market Research Society Journal, 38(2), 1-14. https://doi.org/10.1177/147078539603800206

Koch, A. (1995). Gefalschte Interviews: Ergebnisse der Interviewerkontrolle beim ALLBUS 1994 [Fake interviews: Results of the interviewer control at ALLBUS 1994]. ZUMA-Nachrichten, 36, 89-105.

Koczela, S., Furlong, C., McCarthy, J., & Mushtaq, A. (2015). Curbstoning and beyond: Confronting data fabrication in survey research. Statistical Journal of the IAOS, 31(3), 413-422. https://doi.org/10.3233/SJI-150917

Krejsa, E., Davis, M., & Hill, J. (1999). Evaluation of the quality assurance falsification interview used in the census 2000 dress rehearsal. Proceedings of the Section on Survey Research Methods (pp. 635-640). American Statistical Association.

Krosnick, J. A., & Alwin, D. F. (1987). An evaluation of a cognitive theory of response-order effects in survey measurement. Public Opinion Quarterly, 51(2), 201-219. https://doi.org/10.1086/269029

Kuriakose, N., & Robbins, M. (2016). Don't get duped: Fraud through duplication in public opinion surveys. Statistical Journal of the IAOS, 32(3), 283-291. https://doi.org/10.3233/SJI-161019

Lavrakas, P. J. (2008). Encyclopedia of survey research methods. Sage.

Li, J., Brick, J. M., Tran, B., & Singer, P. (2009). Using statistical models for sample design of reinterview program. Proceedings of the Section on Survey Research Methods (pp. 4681-4695). American Statistical Association.

Lilienfeld, S. O. (2012). Public skepticism of psychology: Why many people perceive the study of human behavior as unscientific. American Psychologist, 67(2), 111-129. https://doi.org/10.1037/a0023963

Menold, N., Winker, P., Storfinger, N., & Kemper, C. (2013). A method for ex-post identification of falsifications in survey data. In N. Menold, P. Winker & R. Porst (Eds.), Survey standardization and interviewers' deviations-impact, reasons, detection and prevention (pp. 25-48). PL Academic Research.

Messick, S. (1966). The psychology of acquiescence: An interpretation of research evidence. ETS Research Bulletin Series, 1966(1), i-44. https://doi.org/10.1002/j.2333-8504.1966.tb00357.x

Mirels, H. L. (1976). Implicit personality theory and inferential illusions. Journal of Personality, 44(3), 467-487. https://doi.org/10.1111/j.1467-6494.1976.tb00133.x

Mosimann, J. E., Wiseman, C. V., & Edelman, R. E. (1995). Data fabrication: Can people generate random digits? Accountability in Research, 4(1), 31-55. https://doi.org/10.1080/08989629508573866

Nickerson, R. S. (2002). The production and perception of randomness. Psychological Review, 109(2), 330-357. https://doi.org/10.1037/0033-295X.109.2.330

Nigrini, M. J. (1996). A taxpayer compliance application of Benford's Law. The Journal of the American Taxation Association, 18(1), 72.

Nigrini, M. J. (2012). Benford's Law: Applications for forensic accounting, auditing, and fraud detection (Vol. 586). Wiley.

Porras, J., & English, N. (2004). Data-driven approaches to identifying interviewer data falsification: The case of health surveys. Proceedings of the Section on Survey Research Methods (pp. 4223-4228). American Statistical Association.

Preece, D. A. (1981). Distributions of final digits in data. The Statistician, 30(1), 31-60. https://doi.org/10.2307/2987702

Putka, D. J., Beatty, A. S., & Reeder, M. C. (2018). Modern prediction methods: New perspectives on a common problem. Organizational Research Methods, 21(3), 689-732. https://doi.org/10.1177/1094428117697041

Reichenbach, H. (1971). The theory of probability: An inquiry into the logical and mathematical foundations of the calculus of probability (E. H. Hutten & M. Reichenbach, Trans.). University of California Press.

Reuband, K.-H. (1990). Interviews, die keine sind -- "Erfolge" und "Misserfolge" beim Falschen von Interviews [Interviews that are not interviews: "Successes" and "failures" in cheating on interviews]. Kolner Zeitschrift Fur Soziologie Und Sozialpsychologie, 42(4), 706-733.

Satter, R. (2019). Experts: Spy used AI-generated face to connect with targets. AP News.

Schaefer, C., Schrapler, J. P., Muller, K. R., & Wagner, G. G. (2005). Automatic identification of faked and fraudulent interviews in the German SOEP. Schmollers Jahrbuch: Journal of Applied Social Science Studies. Zeitschrift Fur Wirtschafts- Und Sozialwissenschaften, 125(1), 183-193.

Schoenherr, T., Ellram, L. M., & Tate, W. L. (2015). A note on the use of survey research firms to enable empirical data collection. Journal of Business Logistics, 36(3), 288-300. https://doi.org/10.1111/jbl.12092

Schreiner, I., Pennie, K., & Newbrough, J. (1988). Interviewer falsification in census bureau surveys. Proceedings of the Section on Survey Research Methods (pp. 491-496). American Statistical Association.

Sharma, S., & Elliott, M. R. (2019). Detecting falsification in a television audience measurement panel survey. International Journal of Market Research. Advance online publication. https://doi.org/10.1177/1470785319874688

Simmons, K., Mercer, A., Schwarzer, S., & Kennedy, C. (2016). Evaluating a new proposal for detecting data falsification in surveys. Statistical Journal of the IAOS, 32(3), 327-338. https://doi.org/10.3233/SJI-161019

Simonsohn, U., Simmons, J. P., & Nelson, L. D. (2015). Better p-curves: Making p-curve analysis more robust to errors, fraud, and ambitious p-hacking, a Reply to Ulrich and Miller (2015). Journal of Experimental Psychology: General, 144(6), 1146-1152. https://doi.org/10.1037/xge0000104

Stacey, A. (2016). Detecting and mitigating "curbstoning" in business and management research. In V. Benson, & F. Filippaios (Eds.), Proceedings of the 15th European Conference on Research Methodology for Business and Management (pp. 265-274). Academic Conferences and Publishing International, Ltd.

Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). Increasing transparency through a multiverse analysis. Perspectives on Psychological Science, 11(5), 702-712. https://doi.org/10.1177/1745691616658637

Steiger, J. H. (1980). Tests for comparing elements of a correlation matrix. Psychological Bulletin, 87(2), 245-251. https://doi.org/10.1037/0033-2909.87.2.245

Storfinger, N., & Opper, M. (2011). Datenbasierte Indikatoren fur potenziell abweichendes Interviewerverhalten [Data-based indicators for potentially deviant interviewer behavior] (No. 58). Discussion Paper, Zentrum fur internationale Entwicklungs-und Umweltforschung.

Turner, C. F., Gribble, J. N., Al-Tayyib, A. A., & Chromy, J. R. (2002). Falsification in epidemiologic surveys: detection and remediation [Prepublication draft]. Technical Papers on Health and Behavior Measurement, Vol. 53, Research Triangle Institute.

Von Mises, R. (1939). Uber aufteilungs-und besetzungs-wahrscheinlichkeiten [About allocation and occupation probabilities]. Revue de la Faculte Des Sciences de L'Universite D'Istanbul, 4, 145-163.

Voracek, M., Tran, U. S., & Formann, A. K. (2008). Birthday and birthmate problems: Misconceptions of probability among psychology undergraduates and casino visitors and personnel. Perceptual and Motor Skills, 106(1), 91-103. https://doi.org/10.2466/pms.106.1.91-103

Wang, S., & Jia, S. (2019). Signature handwriting identification based on generative adversarial networks. Journal of Physics: Conference Series, 1187(4), 042047. https://doi.org/10.1088/1742-6596/1187/4/042047

Winker, P. (2016). Assuring the quality of survey data: Incentives, detection and documentation of deviant behavior. Statistical Journal of the IAOS, 32(3), 295-303. https://doi.org/10.3233/SJI-161012

Yang, Z., Hu, J., Salakhutdinov, R., & Cohen, W. (2017). Semi-supervised QA with generative domain-adaptive nets. Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (pp. 1040-1050). https://doi.org/10.18653/v1/P17-1096

Yoon, J., Jordon, J., & van der Schaar, M. (2018). GAIN: Missing data imputation using generative adversarial nets. In J. Dy & A. Krause (Eds.), Proceedings of the 35th International Conference on Machine Learning (Vol. 80, pp. 5689-5698). PMLR. http://proceedings.mlr.press/v80/yoon18a.html

Yule, G. U. (1927). VII. On a method of investigating periodicities disturbed series, with special reference to Wolfer's sunspot numbers. Philosophical Transactions of the Royal Society of London. Series A, Containing Papers of a Mathematical or Physical Character, 226(636-646), 267-298. https://doi.org/10.1098/rsta.1927.0007

Ziegler, M., Kemper, C. J., & Kruyen, P. (2014). Short scales -- Five misunderstandings and ways to overcome them. Journal of Individual Differences, 35(4), 185-189. https://doi.org/10.1027/1614-0001/a000148

Ziegler, M., Kemper, C., & Rammstedt, B. (2013). The Vocabulary and Overclaiming Test (VOC-T). Journal of Individual Differences, 34(1), 32-40. https://doi.org/10.1027/1614-0001/a000093

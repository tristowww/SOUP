Journal of Applied Psychology
© 2021 American Psychological Association
ISSN: 0021-9010

2022, Vol. 107, No. 11, 1995–2012
https://doi.org/10.1037/apl0000996

On the Assessment of Predictive Bias in Selection Systems
With Multiple Predictors
Jeffrey A. Dahlke1 and Paul R. Sackett2

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

1

Human Resources Research Organization, Alexandria, Virginia, United States
2
Department of Psychology, University of Minnesota

There is a long history of examining assessments used in college admissions or personnel selection for
predictive bias, also called differential prediction, to determine whether a selection system predicts
comparable levels of performance for individuals from different demographic groups who have the
same assessment scores. We expand on previous research that has considered predictive bias in individual
predictor variables to (a) examine magnitudes of differential prediction in multipredictor selection systems
and (b) explore how differences in prediction generalize across samples. We also share updated methods for
computing standardized effect sizes for categorically moderated regression models that facilitate the metaanalysis of differential prediction effects. Our ﬁndings highlight the importance of analyzing composite
predictors when testing for predictive bias in compensatory selection systems and demonstrate the
generalizability of long-observed differential prediction trends by race/ethnicity.
Keywords: differential prediction, predictive bias, selection, predictor weighting, meta-analysis
Supplemental materials: https://doi.org/10.1037/apl0000996.supp

minority group’s performance is underpredicted. Alternatively,
another possible ﬁnding is that minority group members perform
worse than an overall regression line would predict, a ﬁnding labeled
overprediction. There is extensive evidence regarding whether highstakes tests underpredict or overpredict minority groups’ performance. Examining race and ethnicity in the educational admissions
domain, Linn (1978) reviewed 22 studies and Young (2001)
reviewed 49 studies; both concluded that the consistent ﬁnding is
overprediction (i.e., the predicted grade point average [GPA] is
higher than the actual obtained GPA), rather than underprediction,
for Black and Hispanic students. Findings for Black and Hispanic
applicants in the employment domain parallel those in educational
admissions (Bartlett et al., 1978; Hartigan & Wigdor, 1989).
In contrast, underprediction of women’s performance is commonly found in the academic domain at the undergraduate level,
with meta-analytic evidence from 130 studies revealing that women
obtain GPAs about 0.24 points higher than would be predicted by
admissions tests alone (Fischer et al., 2013). Most of this sex
difference has been found to reﬂect differences in conscientiousness,
study habits, and course-taking patterns (Keiser et al., 2016; Kling
et al., 2013; Ramist et al., 1990; Stricker et al., 1993).
While some view any departure from a common regression line as a
reason to reject the use of a predictor, the Society for Industrial and
Organizational Psychology’s (SIOP; 2018) Principles for the Validation and Use of Personnel Selection Procedures (hereafter simply the
Principles) note that, in applied settings, organizations are primarily
concerned about the possibility of underpredicting performance of
members of historically disadvantaged groups. A ﬁnding of underprediction may be viewed by organizations as an impediment to the

There is a long history of examining assessments used in college
admissions or personnel selection for predictive bias, also called
differential prediction. Absent predictive bias, a given predictor
score would forecast the same level of subsequent criterion performance regardless of group membership (Cleary, 1968). To test this,
regression lines relating test scores to criterion performance are
examined to determine whether a given score predicts the same level
of criterion performance for each group. Regression lines for groups
of interest could differ in slopes, intercepts, or both.1 In this article,
we expand on previous research that has considered predictive bias
in individual predictor variables to (a) examine magnitudes of
differential prediction in multipredictor selection systems and (b)
explore how differences in prediction generalize across samples.
When testing for predictive bias, one possible ﬁnding is that
members of a minority group of interest perform better, on average,
than an overall regression line would predict. In other words, the

This article was published Online First December 30, 2021.
Jeffrey A. Dahlke
https://orcid.org/0000-0003-1024-4562
Jeffrey A. Dahlke completed a large part of this research while pursuing
his Ph.D. in industrial and organizational psychology at the University of
Minnesota; Studies 2 and 3 were adapted from his dissertation, as was this
article’s Online Supplement.
This research was supported by a grant from the College Board. Paul R.
Sackett has served as a consultant to the College Board. This relationship has
been reviewed and managed by the University of Minnesota in accordance
with its conﬂict of interest policies. This research is derived from data
provided by the College Board. Copyright © 2006–2013 The College Board
(www.collegeboard.com).
Correspondence concerning this article should be addressed to Jeffrey
A. Dahlke, Human Resources Research Organization, 66 Canal Center
Plaza, Suite 700, Alexandria, VA 22314, United States. Email: jdahlke@
humrro.org

1

When both slopes and intercepts differ between groups, the slope
difference is interpreted but the intercept difference is not, as it is a main
effect in the presence of an interaction effect.
1995

1996

DAHLKE AND SACKETT

use of a selection system as currently constituted, based on legal
concerns, fairness concerns, or both. A ﬁnding of overprediction may
not be seen as a barrier to selection system use, based on the logic that
the differential prediction does not harm the employment opportunities
of the protected group of interest. A ﬁnding of underprediction, as in
the above-discussed case of sex and admissions tests, prompts research
to guide decisions as to whether or not test use is warranted.

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Criticisms and Defenses of Historic Patterns
of Predictive Bias Findings
Despite the long history of predictive bias research and the
consistency of ﬁndings, in recent years, some researchers have
raised concerns about the accuracy with which differences in
prediction can be detected. Aguinis et al. (2010) designed a simulation study to examine the effects of measurement-error and direct
range-restriction artifacts on the Type I error rates and power of the
commonly used Cleary model of test bias (Appendix A presents an
overview of the Cleary model for interested readers). They concluded that, after artifacts are introduced, Cleary analyses generally
lack the necessary power to detect slope differences and intercept
differences are likely to be detected erroneously.
In response to these concerns, researchers used analysis methods not
affected by the Cleary model’s limitations to determine whether
Aguinis et al.’s (2010) conclusions were supported by real-world
data. Mattern and Patterson (2013) used a large database of postsecondary data from hundreds of thousands of college students from
hundreds of college cohorts to demonstrate that, after making corrections for range restriction and criterion measurement error, the historic
patterns of differences in prediction persisted. Berry and Zhao (2015)
used meta-analytic data to examine Black–White differences in prediction after making appropriate corrections for artifacts. Berry and
Zhao did not rely on moderated regression in their analyses; instead,
they used a new unbiased test of intercept differences and found that
Black applicants’ performance was still likely to be overpredicted.
The above-mentioned modern works supporting classic trends
prompted more concerns from critics of the predictive bias literature.
Aguinis et al. (2016) reanalyzed data used by Mattern and Patterson
(2013), focusing on regression analyses in which four predictors
(high school GPA [HSGPA], SAT Critical Reading, SAT Math, and
SAT Writing), group membership, and group-by-predictor interactions for the four predictors were all entered into a model together.
After applying this model to each college cohort, Aguinis et al.
tallied the percentage of cohorts in which each term in the model
reached statistical signiﬁcance, reporting that differential prediction
is common and that hundreds of thousands of students attend
schools where slope or intercept differences were found. On the
surface, this ﬁnding indicates a serious problem for test use.
However, we show that the ﬁndings are misleading and do not,
in fact, speak to predictive bias in operational test use. In the
following section, we articulate several general principles relevant
to predictive bias analyses that we believe are not well understood;
these principles form the basis of our analyses.

A Comparison of Possible Approaches for Assessing
Predictive Bias in Multipredictor Selection Settings
Predictive bias is, at its heart, an applied issue. When conducting
such an analysis, an organization is asking “if we use the proposed

selection system, will that system be biased against the group(s) of
interest?” Note that we used the phrase “selection system,” not
“predictor.” Consider the following scenario: An organization
proposes to use a regression-weighted composite of cognitive
ability, conscientiousness, and situational judgment scores for a
given job and conducts a high-quality validation study. They then
plan to examine potential predictive bias against subgroups for
which sample size is deemed large enough. Below, we outline three
possible approaches to this analysis.

Approach 1: Test Predictors One at a Time
Approach 1 is to conduct a separate analysis for each of the three
predictors: cognitive ability, conscientiousness, and situational
judgment. This would make sense if one were considering using
each as a stand-alone predictor (or using them sequentially as
multiple hurdles with reject vs. continue decisions made at each
step). A predictive bias analysis is a “what if?” analysis: If, say,
ability alone were used as the basis for selection, would there be bias
against a group of interest? However, as the three predictors are
being considered for joint use in a compensatory manner, this “one
at a time” analysis approach simply does not address the applied
question of whether a selection system that uses these three predictors as a set exhibits predictive bias (Sackett et al., 2003).

Approach 2: Test All Predictors and Their Interactions
in a Single Model
Approach 2 is to include each of the three predictors, as well as
their interactions, in a single regression analysis. This makes sense
on the surface because it is an expansion of single-predictor
predictive bias analysis to the multipredictor setting. This was
the approach taken by Aguinis et al. (2016). However, by including
multiple main effects and interactions in the same model, Aguinis
et al.’s (2016) conclusions about intercept and slope differences
drawn from signiﬁcance tests of individual coefﬁcients were not
based on operational predictor scores, but rather on the residuals of
predictor scores after controlling for the other predictors and
predictor-by-group interactions. Although this approach can support
meaningful comparisons of model ﬁt among properly speciﬁed
nested models, the signiﬁcance tests of individual coefﬁcients
can be misleading. As with Approach 1, this is effectively an
analysis of each predictor one at a time. The coefﬁcients for each
predictor and predictor-by-subgroup interaction address the question, “what would happen if the organization made selection
decisions on the residualized variance of a predictor, net of other
predictors included in the model?” This does not reﬂect our experience of how real-world selection decisions are made and, therefore,
does not provide a test of operational predictive bias.2 One cannot
justiﬁably conclude that a predictor–criterion relationship is biased
2
Note that this is only an issue when there are interactions included in the
model. In a main-effects-only model, the group membership coefﬁcient is the
same regardless of whether one enters a set of predictor variables individually
or enters a single-regression-weighted composite of the predictors. If interactions are included, Cleary-type contrasts among nested models featuring
these variables would still be informative (though the contrasts would be
based on different degrees of freedom than would be ideal); however, the
individual slope effects would not be indicative of slope bias in the system as
a whole.

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS

if what is really being analyzed is the leftover variance not shared
with other predictors, unless that leftover variance is, in fact, the
proposed selection system. Importantly, Aguinis et al. appear not to
have recognized the “what if” nature of their analyses. While they
were, in effect, reporting analyses of four different potential
selection systems (residualized HSGPA, residualized SAT Critical
Reading, residualized SAT Math, and residualized SAT Writing),
they reported for each system the number of students attending a
college at which predictive bias is found for that system and
discussed the ﬁndings as implying that large numbers of students
have been directly wronged by predictive bias in test use. As the
various SAT subtests and HSGPAs are used jointly in admissions
decision, the analyses reported by Aguinis et al. shed no light on
predictive bias in the tests as operationally used. This approach is
also problematic from a technical statistical perspective, which we
discuss later within the context of our third study.

Approach 3: Combine Predictors Into a Compensatory
Composite and Test the Composite
Approach 3 is to examine predictive bias in a multifaceted
selection system by forming a single composite predictor variable
and testing the composite for bias. This approach better approximates the way data from compensatory predictors are used in
operational settings (i.e., predictors are considered collectively
without controlling for each other’s inﬂuence) and avoids complications from multicollinearity issues. Sackett et al. (2003) developed
the argument for such an approach as a way to combat the issue of
omitted variables in regression analyses and, based on their work,
SIOP’s (2018) most recent version of the Principles calls for
predictive bias analyses to be conducted at the level of the operational composite.
The omitted variables problem is a standard issue in regression
analysis, and it is broadly recognized that regression coefﬁcients can
be biased unless they come from a fully speciﬁed model (i.e., one
including all determinants of the outcome of interest). The key
insight is that if an omitted variable is correlated with an included
variable, the shared variance is attributed to the included variable in
the regression model. This has long been recognized as a concern for
predictive bias analyses (Linn & Werts, 1971) but was brought to the
forefront by Sackett et al. (2003). They noted that, if an omitted
variable is correlated with group membership (e.g., race, gender),
the criterion variance that is in reality attributable to the omitted
variable(s) is attributed to group membership in a predictive bias
analysis.
Keiser et al. (2016) provided a useful illustration of this. In their
data, ACT scores underpredicted women’s college performance in
a large sample. They hypothesized that Big Five personality
traits—particularly conscientiousness—functioned as omitted
variables. Adding the Big Five to the regression model reduced
the gender coefﬁcient in a predictive bias analysis to a small and
nonsigniﬁcant value, thus eliminating the underprediction. There
are several important things to note about this analysis. First, the
common ﬁnding that admissions tests underpredict women’s
performance lends itself to an initial reaction that there must be
something wrong with the tests. Showing that the ﬁnding is
attributable to an omitted variable offers an alternate explanation.
Second, the ﬁnding that the underprediction is explainable by
personality factors has important implications for the argument we

1997

make in this article that predictive bias should be examined at the
level of a selection system. The ﬁnding that including personality
factors along with the ACT eliminates the underprediction
observed in an ACT-only analysis indicates that a selection
system that accounts for both Big Five scores and ACT scores
would not show predictive bias. A selection system that did not
include these personality factors and used only ACT scores
would, in fact, underpredict women’s performance. The remedy
upon discovering an omitted variable is the inclusion of that
omitted variable in the model. Either a direct measure of personality or other variables capturing this personality variance would
merit exploration. For example, a common argument for using
high school grades in addition to test scores in admissions systems
is that grades reﬂect both ability and motivation and may serve to
capture this personality variance. This foreshadows analyses we
report in this article in which we examine a composite of test score
and grades, in contrast to examining each separately.
Thus, there is a clear prescription to conduct analyses at the
composite level, rather than conducting separate analyses for each
individual predictor or including multiple predictors as separate
variables in a single regression model. However, the published work
on predictive bias has been primarily at the level of individual
predictors. An important question is, “what can be expected to
happen when we shift the focus of predictive bias from individual
predictors to predictor composites?” In this article, we present three
studies that shed light on this issue. In Study 1, we reanalyze Keiser
et al.’s (2016) data using effect-size metrics to demonstrate the
magnitude by which accounting for personality factors can reduce
the underprediction of female college students’ GPAs compared to
using ACT scores alone. In Study 2, we develop a conceptual and
analytic argument as to what can be expected when selection is
based on a multipredictor composite and offer an empirical demonstration based on meta-analytic estimates of predictor–criterion
relations. In Study 3, we revisit the database used as the basis
for Aguinis et al.’s (2016) conclusion that predictive bias ﬁndings
vary substantially from sample to sample. We examine what
happens when we study predictive bias at the level of predictor
composites, rather than testing multiple individual predictors in a
single regression analysis. In all our analyses, we make use of
recently developed standardized effect sizes for differential
prediction.

Effect Sizes for Differential Prediction
In our exploration of the issues introduced above, we express the
magnitudes of effects using a recently developed effect size for
categorical interaction effects called dMod_Signed. Nye and Sackett
(2017) developed dMod_Signed as standardized effect size to quantify
the difference between the two regression lines estimated in a
multiple regression model with a single binary moderator; this
makes it ideally suited for use as an effect-size complement to
the traditional signiﬁcance tests performed in the Cleary framework.
Conceptually, dMod_Signed represents the average difference between
a referent group’s regression line (e.g., the White line) and a focal
group’s regression line (e.g., the Black or Hispanic line), using the
focal group’s predictor distribution to generate predictions and
standardizing the result by dividing the raw average difference
by the referent group’s criterion standard deviation.

1998

DAHLKE AND SACKETT

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

When applied to a linear regression model, dMod_Signed can be
computed as
ð
1
dMod Signed =
f ðXÞ½Xðb11 − b12 Þ + b01 − b02 dX
(1)
SDY 1 2
where SDY 1 is the referent group’s observed criterion standard
deviation, f2 is the normal density function for the focal group’s
predictor distribution, b11 and b12 are the subgroup slopes for the
referent and focal groups, respectively, and b01 and b02 are the
subgroup intercepts for the referent and focal groups, respectively.
As dMod_Signed represents the standardized weighted mean difference between predicted scores from two regression models, the
interpretation of dMod_Signed is similar to the interpretation of any
other mean difference effect size (speciﬁcally Glass’ Δ, as that effect
size is standardized using only the control/referent group’s standard
deviation), except that dMod_Signed is framed in terms of predicted
criterion scores rather than observed scores. Positive and negative
dMod_Signed values indicate net effects of overprediction and underprediction, respectively, across the operational range of predictor
scores. Nye and Sackett (2017) also developed a related effect size to
capture the average absolute value difference in prediction (called
dMod_Unsigned) and Dahlke and Sackett (2018) subsequently showed
that dMod_Signed could be broken down into two effect sizes that
quantify overprediction (dMod_Over) and underprediction (dMod_Under)
separately. In this research, we use dMod_Signed in all analyses because
it represents the overall net effect of differential prediction.
In our usage of the dMod effect sizes, we discovered that integration was unnecessary for linear regression effects and we derived
algebraic formulas for the full set of dMod effect sizes (dMod_Signed,
dMod_Unsigned, dMod_Over, and dMod_Under). We present the equations
and rationales for these advancements in the Online Supplement.
The algebraic counterpart to Equation 1 is
SD

dMod Signed =

ðȲ 1 − Ȳ 2 Þ − r XY 1 SDXY 1 ðX̄ 1 –X̄ 2 Þ
1

SDY 1

(2)

where Ȳ 1 is the mean criterion score in the referent group, Ȳ 2 is the
mean criterion score in the focal group, r XY 1 is the correlation
between predictor and criterion scores in the referent group,
SDY 1 is the standard deviation of criterion scores in the referent
group, SDX 1 is the standard deviation of predictor scores in the
referent group, X̄ 1 is the mean predictor score in the referent group,
and X̄ 2 is the mean predictor score in the focal group. If one can
assume that the referent and focal groups have comparable variance
on both the predictor and criterion, dMod_Signed can be estimated
using standardized effects sizes as inputs,
dMod Signed ≅ dY − r XY 1 dX

(3)

where dX and dY are the standardized subgroup mean differences on
the predictor and criterion variables, respectively. Equation 3 is
virtually identical to Berry and Zhao’s test of intercept differences,
with the sole difference being that we specify using a validity
coefﬁcient from the referent-group rather than a combined-groups
validity estimate; even when groups have different slopes, dMod_Signed
accurately represents the net average difference in prediction. In
addition to making dMod effect sizes simpler to compute, our algebraic
formulas made it possible to analytically estimate the standard error of

dMod_Signed; the Online Supplement explains how to compute the
sampling variance estimators that correspond to Equations 2 and 3.3
The Online Supplement also describes how to estimate dMod_Signed
and its sampling variance when correcting for measurement error in
the criterion and/or predictor.4
Taken together, our algebraic effect-size formulas and our closedform estimators of dMod_Signed’s sampling error variance mean that
standardized effect sizes of differential prediction can be metaanalyzed. Prior to dMod_Signed and our simpliﬁed formulas, differential prediction effects could only be meta-analyzed if the predictor
and criterion measures were the same across studies, as the effects
were expressed as unstandardized regression coefﬁcients. Our new
formulas and error variance estimators for dMod_Signed will support
more comprehensive aggregation of differential prediction effects
by allowing researchers to meta-analyze effects from studies that
used different instrumentation to measure the same constructs
(e.g., studies using different measures of cognitive ability and
overall job performance). As we examine the effect of composite
predictors on predictive bias ﬁndings, we explain the insights that
can be gleaned from our dMod_Signed formulas, themselves, and from
their usage in primary studies and meta-analyses.

Study 1: Revisiting Keiser et al.’s (2016) Empirical
Example of Mitigating the Underprediction of Female
Students’ Cumulative GPAs
Earlier we summarized Keiser et al.’s (2016) ﬁnding that,
although ACT scores alone underpredict female students’ college
GPAs, underprediction was effectively nulliﬁed by analyzing ACT
scores along with scores on the Big Five personality factors. This is a
classic example of how omitted variables can cause a predictor to
appear predictively biased when, in fact, the underprediction only
occurred because other predictors that should be included in the
selection system were excluded from the analysis. In this study, we
reanalyze Keiser et al.’s data using the dMod_Signed effect size to (a)
demonstrate the magnitudes of the effects Keiser et al. identiﬁed in
their regression analyses and (b) offer a simple example of how
analyzing multiple predictors as a composite can help avoid ﬂawed
conclusions about differential prediction.

Method
We analyzed the correlation matrix reported by Keiser et al.
(2016; see their Table 1), which was based on data from 1,978
undergraduate students (40.7% male, 59.3% female) enrolled in an
introductory psychology course at a large Midwestern university.
The matrix included correlations among students’ ACT scores,
scores on the Big Five personality factors (conscientiousness,
agreeableness, neuroticism, openness, and extraversion), a dummy
variable representing sex, and a variety of academic performance
metrics (cumulative GPA, course grade, exam points, quiz points,
discussion points, and points earned by participating in research
studies). Of the available performance metrics, we chose to use
3
Error variance estimators are not available for the dMod_Unsigned, dMod_Over,
and dMod_Under effect sizes because they are unidirectional effects with highly
skewed, nonsymmetric sampling distributions.
4
However, operational estimates of dMod effects for predictive bias
analyses should never correct for predictor measurement error, as selection
decisions are based on observed predictor scores.

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS

cumulative GPA as the criterion variable in our analyses, as it is the
academic performance variable most commonly used in differential
prediction analyses due to its administrative importance.
Keiser et al.’s (2016) correlation matrix summarized the relations
among variables for males and females combined (i.e., the correlations represent within-group plus between-group covariance among
variables), with a dummy variable to indicate how mean scores
differed between males and females. We converted the correlations
between sex and continuous variables into d values for our analyses.
However, note that Equations 2 and 3 call for one to use referentgroup validity coefﬁcients to compute dMod_Signed. The combinedgroup correlations we obtained from Keiser et al.’s results are
therefore not ideal for use in the dMod_Signed formula; they overestimate within-group validity because they reﬂect a combination of
within- and between-group covariance rather than purely withingroup covariance. To account for this in our analyses, we removed
between-group variance from the combined-group validity estimates to obtain estimates of pooled within-group validity that could
be used to compute dMod_Signed. We note that our use of these pooled
within-group validity estimates assumes equal predictor-GPA correlations for men and women; this would not be ideal for operational
predictive bias analyses but will be sufﬁcient for achieving the
illustrative goals of the present study.
We quantiﬁed the standardized magnitudes of differential prediction for the same three nested models examined by Keiser et al.
(2016): ACT scores, a regression-weighted composite of ACT
scores and conscientiousness scores, and a regression-weighted
composite of ACT scores and scores on each of the Big Five
factors. We computed dMod_Signed using Equation 3 because our
input data consisted of standardized effect sizes.

Results
Consistent with Keiser et al.’s (2016) hierarchical regression
analyses, we found that using ACT as the sole predictor of
cumulative GPA produced underprediction (dMod_Signed =
−.170; ACT d value = .246; pooled within-group ACT validity =
.276) and using a composite of ACT scores and conscientious
scores as the predictor reduced the magnitude of underprediction to
a modest degree (dMod_Signed = −.145; composite d value = .127;
pooled within-group composite validity = .337). Predicting cumulative GPAs using a composite of ACT scores and scores on all of
the Big Five factors brought the magnitude of underprediction
down even further to a very small effect (dMod_Signed = −.058;
composite d value = −.119; pooled within-group composite
validity = .372).

Discussion
Keiser et al. (2016) showed that underprediction of women’s
cumulative GPAs by ACT scores diminished to a level that was not
statistically signiﬁcant once they accounted for personality factors.
We used their data to show the same phenomenon in the standardized effect-size metric of dMod_Signed. As we moved beyond analyzing ACT scores as the only predictor (dMod_Signed = −.170) and
added conscientiousness (dMod_Signed = −.145) followed by the rest
of the Big Five (dMod_Signed = −.058), underprediction decreased to
a very small magnitude. Accounting for personality variables helps
to avoid the omitted variables problem and prevents one from

1999

drawing ﬂawed conclusions about the extent to underprediction
poses an obstacle when forecasting women’s academic performance in college using standardized test scores.
The trends we observed in our analyses of composite predictors
are driven by very predictable statistical features of their component
predictors. By shifting from an ACT-only model to models that
included more personality variables, we increased levels of predictive validity and reversed the direction of mean differences on the
composite predictor. Whereas male students had a higher mean ACT
score (d = .246), female students had a higher mean on the
composite of ACT scores and Big Five factors (d = −.119). Recall
that dMod_Signed is the difference between dY and r XY 1 dX; thus, these
trends meant that dMod_Signed approached zero because, as we got
closer to a fully speciﬁed predictor set, the product of the validity
coefﬁcient and the predictor d value approached the d value for the
cumulative GPAs (−.102). In other words, analyzing a more
complete predictor set brought us closer to explaining why males
and females exhibited mean differences in cumulative GPAs, which
brought us closer to eliminating the underprediction produced when
the ACT was used as the only predictor.
In Study 2, we elaborate on the impact of forming predictors on
magnitudes of differential prediction by examining a wider variety
of predictor variables in the employment context and combining
them using several popular predictor weighting schemes. We also
dig deeper into the factors that affect magnitudes of dMod_Signed
results and demonstrate how using composite predictors affects
differential prediction in settings where overprediction is the prevailing ﬁnding.

Study 2: Effects of Forming Composite Predictors on
Magnitudes of Differential Prediction
Performance is determined by a multitude of factors (Campbell,
1990) and thoughtfully developed selection systems account for
this by gathering data on several predictor variables that each make
a unique contribution to forecasted levels of performance. Given
that multiple predictors are relevant to most, if not all, forms of
performance and that real-world selection systems seldom rely on a
single predictor, it is generally recommended that differential
prediction be evaluated at the level of the selection system rather
than at the level of individual predictors (Sackett et al., 2003; SIOP,
2018). As noted earlier, testing several predictors separately for
differential prediction when they are considered together to make
compensatory selection decisions fails to capture how data are
operationally used and can provide misleading indications of the
differential prediction associated with a composite of the predictors. As composite predictors are the recommended focus of
differential prediction analyses according to SIOP’s (2018) Principles and the effect of forming composites on dMod_Signed effect
sizes has not previously been explored, the present study ﬁlls this
gap by describing the implications of composites for dMod_Signed
effects.
The effect of forming composites on the magnitudes of differential prediction can be best understood by considering the formula for
computing dMod_Signed from correlations and d values. As we noted
in Study 1, Equation 3 makes it clear that the direction and
magnitude of differential prediction are determined by two key
things: The magnitude of subgroup mean differences on the criterion, as indexed by dY, and the magnitude of the product of r XY 1 and

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

2000

DAHLKE AND SACKETT

dX, which represents the magnitude of subgroup mean differences
on the predicted criterion scores when the referent group’s regression equation is used to make predictions. With all else being equal,
higher dY values increase the probability of observing overprediction or a lessened magnitude of underprediction, while higher r XY 1
and/or dX values increase the probability of observing underprediction or a lessened magnitude of overprediction.
Unless predictors are completely redundant with each other, their
intercorrelations will be less than 1.00 in absolute value, such that a
composite of predictors will have a validity coefﬁcient larger than
the average validity coefﬁcient of the individual predictors. Similarly, as was shown by Sackett and Ellingson (1997), a composite
predictor will also tend to have a d value larger in magnitude than the
average d value of its component predictors because of incomplete
overlap in the predictors’ variance.5 All else being equal, the smaller
the average intercorrelation among predictors, the greater will be
both the validity and the d value of the composite predictor. Given
that White-minority mean differences tend to be positive and that
predictors are generally analyzed in such a way that validity
coefﬁcients are positive, this means that predictor-combination
practices that increase the validity of a composite predictor will
also tend to increase mean differences on the composite, which
increases the r XY 1 × dX product. This implies that if one combines
two predictors, each of which exhibits overprediction of focal group
performance when analyzed separately, the composite of the two
will exhibit a smaller magnitude of overprediction than either of its
components because the r XY 1 × dX product increases in magnitude
while dY remains unchanged. In fact, depending on the magnitude of
mean differences on the criterion, it is theoretically possible that a
change in the r XY 1 × dX product from combining two predictors that
each individually overpredict (underpredict) performance could
even result in a composite predictor that underpredicts (overpredicts) performance.
In this study, we illustrate the effects of composites on dMod_Signed
using three popular methods for forming composites: unit weighting, regression weighting, and Pareto-optimal weighting. Unit
weighting and regression weighting are classic strategies for combining predictors. Pareto-optimal weighting, however, is a much
newer addition to the applied psychology toolkit that allows one to
select a weighting scheme from an inﬁnite number of solutions that
make conditionally optimal trade-offs between maximizing validity
and reducing adverse impact (see De Corte et al., 2007 for a detailed
explanation of this method). In short, Pareto optimization allows one
to simultaneously answer two important questions when forming
composite predictors: “for a given level of validity, what is the
lowest level of adverse impact possible?” and “for a given level of
adverse impact, what is the highest level of validity possible?”
Given that Pareto-optimal weighting explicitly optimizes the validity coefﬁcients and d values of composite predictors, one’s choice of
Pareto weights clearly affects dMod_Signed and it is therefore important that we explore Pareto optimization’s effects on differential
prediction.
Whereas use of unit weighting or regression weighting with a
given set of predictors produces a single dMod_Signed estimate (such
that, after choosing a weighting strategy, the degree of differential
prediction is dependent entirely upon which predictors are used), use
of Pareto weighting means that there are inﬁnitely many dMod_Signed
values that could result from a single set of predictors (such that the
degree of differential prediction is a function of one’s preferred

validity–diversity trade-off in addition to the set predictors one has
chosen to use). In the typical case of White-minority differences in
the United States, if one prefers a trade-off that favors minimizing
adverse impact over maximizing validity, the resulting dMod_Signed
value will be more likely to indicate a higher degree of overprediction, as both the validity estimate and the d value associated with the
composite predictor will be smaller than would have occurred had
one chosen a trade-off that placed greater importance on maximizing
validity. However, placing greater emphasis on validity will result in
a lower degree of overprediction because the r XY 1 × dX product will
be larger. The average amount of differential prediction in a selection system is a function of how the predictors are combined, and it
happens that Pareto weighting optimizes the same two predictor
attributes (i.e., validity and mean differences) that are most critical
for determining the magnitude of differential prediction.
We now demonstrate the principles described above by computing validity coefﬁcients, White–Black d values, and dMod_Signed
values for composite predictors using meta-analytic correlations and
d values. To convincingly demonstrate the effects of composite
formation methods on dMod_Signed estimates, the predictor variables
to be combined into composites represent varying degrees of
validity for predicting job performance and varying degrees of
adverse impact potential for Black job applicants. Note that the
value of dY will be unaffected by one’s choice of predictor(s) or how
one generates a composite, as this value can only be changed by
altering the criterion variable; thus, we focus on the implications of
r XY 1 and dX in our demonstrations.

Method
For our demonstrations, we used the meta-analytic correlation
matrix and vector of meta-analytic White–Black d values compiled
by Song et al. (2017) to compute validities, standardized mean
differences, and dMod_Signed effect sizes for composites consisting of
varying sets of ﬁve widely used predictors using three predictor
weighting methods. The artifact-corrected correlations and d values
from Song et al. (2017) are shown in Table 1 (note, however, that we
substituted Song et al.’s observed-metric criterion d value for the
corresponding unreliability corrected value reported by McKay &
McDaniel, 2006). Similar to the data we analyzed from Keiser et al.
(2016) in Study 1, note that Table 1’s meta-analytic validities
include between-group variance in addition to within-group variance, but we ideally need referent-group validity coefﬁcients to
compute dMod_Signed. We accounted for this in our analyses by
partialing between-group variance out of the combined-group validity estimates to obtain within-group validity estimates that are more
appropriate for computing dMod_Signed. As with Study 1, our goal in
these analyses is to demonstrate important concepts rather than draw
conclusions about differential prediction in a high-stakes operational context, and we believe the available data are acceptable for
this purpose. We computed unit-weighted and regression-weighted
composites for all possible combinations of the predictors shown in
Table 1, with predictor sets ranging in size from two to ﬁve
variables. We used the ParetoR package for R by Song (2018) to
compute Pareto-optimal solutions for the full ﬁve-predictor set.
5

Note, however, that the effects of forming a composite on the magnitude
of the d value do not necessarily hold if component predictors have mixed
directions of differences, particularly if they are differentially weighted.

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS

Table 1
Meta-Analytic Correlation Matrix and White–Black Mean Differences From Song et al. (2017) With Measurement-Error Corrected
Criterion d Value

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Correlation
Variable

White–Black d

1

2

3

4

5

1. Biodata
2. Conscientiousness
3. General mental ability
4. Integrity
5. Structured interview
6. Job performance

.39
−.09
.72
.04
.39
.46

—
.51
.37
.25
.16
.32

—
.03
.34
.13
.22

—
.02
.31
.52

—
−.02
.20

—
.48

Note. Roth et al. (2011) provided the predictor intercorrelations (corrected
for range restriction) and validities for biodata, cognitive ability,
conscientiousness, and structured interviews (corrected for both criterion
measurement error and range restriction). Van Iddekinge et al. (2012)
provided the integrity validity estimate, which Song et al. (2017)
corrected for direct range restriction. Bobko and Roth (2013) provided
predictor d value estimates for applicant populations. McKay and
McDaniel (2006) provided the measurement-error corrected d value for
job performance; this differs from Song et al. (2017) data, as they used the
uncorrected value of .38.

Results
Table 2 shows the effect sizes for composites consisting of different
sets of predictors. The results for both unit- and regression-weighted
composites indicate that composites consisting of more predictors, on
average, exhibited larger validities and larger d values, which gave
rise to larger products of those values and correspondingly smaller
dMod_Signed estimates. The mean dMod_Signed effect size for individual
predictors was .330 and smaller mean effect sizes were observed for
composites. The mean dMod_Signed effect sizes for unit-weighted
composites were .275 with two predictors (regression-weighted =
.227), .237 with three predictors (regression-weighted = .146), .211
with four predictors (regression-weighted = .084), and .193 with ﬁve
predictors (regression-weighted = .038). As the mean dMod_Signed
estimate for individual predictors was .330, these analyses reveal a
distinct trend that larger composites demonstrate less overprediction
of Black applicants’ performance. Not only did larger composites
tend to exhibit less overprediction, regression-weighted composites
exhibited less overprediction than their unit-weighted counterparts
because regression composites had larger validities and d values.
Table 3 shows the effect sizes and adverse impact ratios for 21
Pareto-optimal predictor composites. The Pareto solutions support
the trends observed in Table 2: Solutions that had larger d values
(i.e., greater adverse impact potential) and larger validities also had
smaller dMod_Signed effect sizes. The associations between dMod_Signed
effects and (a) validity coefﬁcients and (b) Black–White d values are
depicted in Figure 1. These solutions show that overprediction of
Black applicants’ performance is more likely when one uses Paretooptimal weights that give greater emphasis to minimizing adverse
impact potential and less emphasis to maximizing validity.

Discussion
This study was designed to investigate the effect of forming
composite predictors on dMod_Signed effect sizes. The results of our
illustrative analyses using meta-analytic data supported the

2001

anticipated trends: Compared to the average of its components
with positive d values, a composite has a larger validity coefﬁcient
and a larger d value, and both of these factors drive the dMod_Signed
estimate downward. Furthermore, when Pareto-optimal weights are
used, solutions that give greater emphasis to validity will produce
lower dMod_Signed estimates than will solutions that give greater
emphasis to adverse impact mitigation. These insights offer muchneeded insight into how dMod_Signed estimates are affected by
combining multiple predictors into a single composite. These ﬁndings also complement past work on the omitted variables problem
and support SIOP’s (2018) updated guidance in the Principles,
which advocates analyzing composites for differential prediction
rather than limiting one’s analyses to individual predictor variables.
This study demonstrated that a composite predictor tends to
exhibit a smaller magnitude of differential prediction than its
average component. In Study 3, we conceptually replicate the effects
of forming composites on differential prediction ﬁndings. We also
test whether differences in prediction generalize across settings by
meta-analyzing differential prediction effects computed from a large
postsecondary educational admissions database.

Study 3: Testing the Generalizability
of Differential Prediction in Postsecondary
Educational Admissions Settings
Study 2 showed that the magnitudes of differential prediction
observed for composite predictors can be quite different from the
magnitudes observed for the composites’ components. The present
study builds upon those ﬁndings by examining how statistical
artifacts impact differential prediction analyses performed on real
postsecondary educational admissions data using both individual
predictors (i.e., HSGPAs and SAT subtest scores for Critical
Reading, Mathematics, and Writing) and composite predictors
(i.e., SAT composite scores and a combination of SAT scores
and HSGPAs). In addition to replicating and expanding upon the
ﬁndings from Study 2, Study 3 also tests the generalizability of
differential prediction for White–Black and White–Hispanic contrasts, with differential prediction quantiﬁed using dMod_Signed.
By analyzing individual predictor variables along with composite
predictors, we aim to provide a clearer indication of the generalizability of differential prediction in operational selection systems
than has been available in the literature on postsecondary admissions to date. In previous research on the generalizability of
differential prediction, Aguinis et al. (2016) tested multiple predictors’ differential prediction simultaneously in regression models
heavily inﬂuenced by multicollinearity. Beyond the fact that Aguinis et al.’s strategy of including multiple predictors in a single model
did not answer the operational question of whether the predictors
produced biased predictions when used as a set, the multicollinearity
in Aguinis et al.’s models meant that their estimates of regression
coefﬁcients were not stable. Thus, their choice to tally the rates of
signiﬁcant coefﬁcients across small samples is misleading. Including highly correlated variables in a regression model means that the
unique contribution of each variable is difﬁcult to determine and
small ﬂuctuations in sample data can create large swings the
magnitudes of the predictors’ regression coefﬁcients due to multicollinearity (or “bouncing betas”). For example, in the Black–White
regression models analyzed by Aguinis et al. (2016), the Critical
Reading regression coefﬁcients correlated −.53 with the Writing

2002

DAHLKE AND SACKETT

Table 2
Unit- and Regression-Weighted Predictor Sets From Meta-Analytic Data in Table 1
Unit-weighted composites
Predictors

Regression-weighted composites

rXY

rXY_WG

dX

dMod_Signed

rXY

rXY_WG

dX

dMod_Signed

.320
.220
.520
.200
.480
.348

.305
.218
.502
.200
.468
.339

.390
−.090
.720
.040
.390
.290

.341
.480
.099
.452
.277
.330

.320
.220
.520
.200
.480
.348

.305
.218
.502
.200
.468
.339

.390
−.090
.720
.040
.390
.290

.341
.480
.099
.452
.277
.330

.311
.507
.329
.525
.516
.257
.466
.504
.618
.486
.452

.305
.489
.319
.511
.503
.258
.461
.489
.604
.477
.442

.171
.673
.271
.516
.428
−.031
.198
.525
.689
.306
.375

.408
.130
.374
.196
.244
.468
.369
.203
.043
.314
.275

.327
.538
.343
.540
.559
.257
.506
.554
.619
.524
.476

.315
.520
.330
.526
.544
.258
.497
.537
.605
.513
.465

.313
.733
.342
.502
.623
−.038
.324
.684
.704
.376
.456

.362
.078
.347
.196
.121
.470
.299
.093
.034
.267
.227

.483
.325
.476
.503
.610
.514
.483
.615
.456
.631
.509

.469
.321
.466
.487
.596
.502
.474
.603
.453
.618
.499

.459
.148
.320
.554
.700
.423
.335
.509
.171
.604
.422

.245
.413
.311
.190
.042
.248
.301
.153
.383
.086
.237

.560
.345
.541
.561
.630
.560
.573
.640
.532
.650
.559

.544
.334
.528
.545
.617
.548
.559
.628
.523
.638
.546

.637
.305
.472
.698
.718
.472
.623
.642
.341
.679
.559

.113
.358
.211
.080
.017
.201
.112
.057
.282
.027
.146

.475
.581
.470
.611
.599
.547

.463
.568
.462
.598
.589
.536

.393
.530
.280
.622
.441
.453

.278
.159
.331
.088
.200
.211

.574
.641
.560
.654
.658
.617

.559
.629
.548
.642
.646
.605

.631
.657
.470
.689
.645
.618

.107
.047
.202
.018
.043
.084

.574

.562

.475

.193

.658

.647

.653

.038

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

a

Individual predictors
Biodata (BD)
Conscientiousness (C)
General mental ability (GMA)
Integrity (I)
Structured interview (SI)
M
Two-predictor composites
BD + C
BD + GMA
BD + I
BD + SI
C + GMA
C+I
C + SI
GMA + I
GMA + SI
I + SI
M
Three-predictor composites
BD + C + GMA
BD + C + I
BD + C + SI
BD + GMA + I
BD + GMA + SI
BD + I + SI
C + GMA + I
C + GMA + SI
C + I + SI
GMA + I + SI
M
Four-predictor composites
BD + C + GMA + I
BD + C + GMA + SI
BD + C + I + SI
BD + GMA + I + SI
C + GMA + I + SI
M
Five-predictor composite
BD + C + GMA + I + SI

Note. rXY = overall validity for the combined population of Black and White applicants; rXY_WG = average within-group (i.e., pooled) validity across
subgroups computed by partialing between-group predictor and criterion variance out of the overall validity estimate; dX = standardized White–Black mean
difference on predictor; dMod_Signed = standardized mean difference in predicted performance between groups (dMod_Signed = dY − dX × rXY_WG). Estimates are
based on a population consisting of 85% White individuals and 15% Black individuals. In all analyses, the mean difference for performance was .46.
a
Results of individual predictors are shown in both unit- and regression-weighted solutions for ease of interpretation even though these are not truly composites.

coefﬁcients across samples and the Critical Reading-group interaction coefﬁcients correlated −.63 with the Writing-group interaction
coefﬁcients. This high level of dependency between the distributions of regression coefﬁcients means that multicollinearity created
the false appearance of variability in ﬁndings, particularly when
using a statistical signiﬁcance vote-counting method. We base our
analyses on composite predictors to avoid this problem.
The focus of this study is on differential prediction in operational
selection systems, which means that all artifacts except for predictor
measurement error should be accounted for. Operational estimates
of differential prediction indicate how subgroups’ regression equations differ when computed using applicant predictor data and
incumbent criterion data that have been properly corrected for range

restriction. Additionally, we correct for criterion measurement error
in effect sizes to obtain fully operational estimates of differential
prediction because, like other effect sizes, dMod_Signed is attenuated
by measurement error in the dependent variable.

Method
Participants
Participants were 1,104,003 students (880,159 White students
[79.72%], 100,394 Black students [9.09%], and 123,450 Hispanic
students [11.18%]) enrolled at 251 U.S. colleges and universities
that contributed to a data collection initiative led by the College

2003

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS

Table 3
Pareto-Optimal Composite Solutions From Data in Table 1

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Predictor weight
Pareto solution no.

Biodata

Conscientiousness

GMA

Integrity

Structured interview

rXY

rXY_WG

dX

dMod_Signed

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21

0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.030

1.000
0.842
0.796
0.751
0.709
0.668
0.627
0.587
0.546
0.505
0.461
0.415
0.383
0.362
0.339
0.315
0.289
0.261
0.227
0.183
0.091

0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.000
0.019
0.048
0.079
0.112
0.147
0.187
0.233
0.294
0.387

0.000
0.146
0.152
0.157
0.163
0.168
0.173
0.178
0.183
0.189
0.194
0.200
0.200
0.197
0.194
0.190
0.186
0.182
0.177
0.170
0.156

0.000
0.012
0.053
0.091
0.128
0.164
0.200
0.235
0.270
0.307
0.345
0.385
0.398
0.393
0.388
0.383
0.377
0.371
0.363
0.353
0.336

0.220
0.244
0.266
0.289
0.311
0.334
0.356
0.379
0.402
0.424
0.447
0.469
0.490
0.512
0.535
0.557
0.580
0.602
0.624
0.645
0.658

0.218
0.243
0.267
0.291
0.315
0.338
0.359
0.381
0.402
0.423
0.445
0.466
0.486
0.506
0.528
0.549
0.571
0.592
0.613
0.634
0.646

−0.090
−0.072
−0.052
−0.031
−0.010
0.013
0.037
0.062
0.088
0.116
0.146
0.177
0.213
0.248
0.287
0.330
0.375
0.425
0.481
0.549
0.653

0.480
0.478
0.474
0.469
0.463
0.456
0.447
0.437
0.425
0.411
0.395
0.377
0.357
0.334
0.308
0.279
0.246
0.208
0.165
0.112
0.038

Note. GMA = general mental ability; rXY = overall validity for the combined population of Black and White applicants; rXY_WG = average within-group
(i.e., pooled) validity across subgroups computed by partialling between-group predictor and criterion variance out of the overall validity estimate; dX =
standardized White–Black mean difference on predictor; dMod_Signed = standardized mean differences in predicted performance between groups (dMod_Signed =
dY − dX × rXY_WG). Estimates are based on a population consisting of 85% White individuals and 15% Black individuals. In all analyses, the mean difference for
performance was .46. Solution 21 is the regression-weighted solution and is identical to the ﬁve-predictor regression composite in Table 2.

Board. Consistent with Mattern and Patterson’s (2013) procedures,
we excluded subgroup samples with fewer than 15 observations. All
participants began college between 2006 and 2012. School-level
sample sizes ranged from 130 to 54,212 (Mdn = 1,866), schools
contributed between 1 and 7 cohorts of student data (Mdn = 3), and
cohort-level sample sizes ranged from 73 to 9,596 (Mdn = 667.5).
The College Board also provided covariance matrices and means for
the predictor scores of 7,159,809 applicants to our sample of
institutions. These data were nonrandomly sampled by virtue of
being collected from schools that used the SAT as a selection device
and that consented to provide students’ grade data to the College
Board for research purposes. The database we analyzed has been
used in other published research (e.g., Beatty et al., 2015; Dahlke
et al., 2018, 2019; Higdem et al., 2016; Kostal et al., 2015; Shewach
et al., 2017; Yu et al., 2016), but the present study reports unique
analyses of these data and draws novel insights.

Measures
The College Board provided students’ scores on each of the three
SAT subtests: Critical Reading, Mathematics, and Writing. Scores
on each subtest could range from 200 to 800 in 10-point increments.
Students provided their self-reported HSGPAs in a survey administered by the College Board, and schools reported students’ ﬁrst-year
college GPAs for inclusion in the College Board’s database.
HSGPAs and college GPAs could range from 0.0 to 4.3.

Procedure
Our analysis procedures consisted of several steps, including
computing observed subgroup descriptive statistics, correcting for

criterion measurement error, correcting for range restriction, computing composite predictors, computing dMod_signed effect sizes, and
meta-analyzing dMod_Signed effect sizes. Each of these steps is
detailed below.
Observed Subgroup Means and Covariances. We computed
covariance matrices and vectors of means for each subgroup’s ﬁrstyear GPAs, SAT scores, and self-reported HSGPAs at each school
in the database; note that we computed all analyses at the level of
schools, not cohorts. For each school, we organized subgroupspeciﬁc applicant distributional summaries provided by the College
Board; these summaries included the unrestricted means, variances,
and covariances of all predictor variables. The College Board
provided subgroup distributional summaries at the level of entering
cohorts but, as noted above, our interest was focused on institutionlevel differential prediction trends. Thus, for each subgroup at each
school, we merged the multivariate predictor distributions from all
cohorts into a single applicant mixture distribution that represented
the combined within-cohort and between-cohort variance in predictor scores. Having a single school-level applicant distribution for
each subgroup made the unrestricted predictor data compatible with
our goal of analyzing data at the school level rather than the cohort
level. We constructed mixture distributions using the “mix_matrix”
function from the psychmeta R package (Dahlke & Wiernik,
2019a, 2019b).
In addition to our analyses of subgroup-speciﬁc data, we also
performed the above operations on the complete data set from each
school that contained data from all subgroups. We then pooled the
school-wise distributions of overall predictor information to obtain a
distribution that represented the sample-size-weighted average
means, variances, and covariances of predictors across all schools

2004

DAHLKE AND SACKETT

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Figure 1
Association Between dMod_Signed Effect Sizes and Predictors’ Validity and Mean-Difference Effect Sizes for Pareto-Optimal Composites

Note. The numeric labels used as data points in the plot correspond to the “Pareto solution no.” identiﬁers assigned to the Pareto-optimal solutions in Table 3.

in our analysis. These overall estimates of range-restricted and
applicant data were necessary to support later steps in our procedure.
Corrections for Criterion Measurement Error. We corrected observed ﬁrst-year GPA criteria for measurement error
using subgroup-speciﬁc reliability estimates based on the internal
consistency of students’ ﬁrst-year grades at each school. We
performed reliability corrections separately on the data from
White, Black, and Hispanic samples. We estimated reliability
coefﬁcients by computing the intraclass correlation coefﬁcient
(ICC1) for ﬁrst-year course grades, which indicates the average
intercorrelation among individual students’ individual course
grades. After this, we used the Spearman–Brown formula to
step up each ICC1 estimate by the average number of courses
the students took to arrive at an estimate of the internal consistency of the grades that contributed to students’ ﬁrst-year GPAs.
The sample-size-weighted mean reliabilities were .85 for White
students (SD = .03) and .82 for both Black students (SD = .05)
and Hispanic students (SD = .05).
Range-Restriction Corrections. We used the Aitken–Lawley
multivariate range-correction procedure (Aitken, 1934; Lawley,
1943) to correct ﬁrst-year GPAs for range restriction using applicant
distributions from the College Board. Speciﬁcally, we used the
“correct_matrix_mvrr” function from the psychmeta R package
(Dahlke & Wiernik, 2019a, 2019b) to correct covariance matrices
for range restriction and we used psychmeta’s “correct_means_mvrr” function to correct the criterion means for range
restriction. When we corrected for artifacts, we made corrections
for criterion measurement error ﬁrst because the criterion reliability
coefﬁcients were based on range-restricted data; measurement error
of range-restricted criteria should always be corrected before making corrections for range restriction (Hunter et al., 2006).

Composites. To evaluate the differential prediction associated
with different methods of using predictor scores to make holistic
evaluations, we formed two composite predictors to include in our
analyses. We created (a) an SAT composite consisting of unitweighted Critical Reading, Mathematics, and Writing scores and
(b) a unit-weighted composite of the SAT composite and HSGPA.
We used unit weighting to approximate how admissions ofﬁcers may
treat indicators of academic aptitude from multiple sources as equally
important and give equal weight to each piece of information.
It was during this process of computing composite predictors that
it was necessary to use the estimates of overall predictor variances
pooled across schools mentioned earlier. When unit weights are used
to form a composite, each variable only gets equal weight if the
weights are proportional to the variables’ inverse standard deviations. Without either standardizing the variables or converting the
unit weights to an unstandardized metric, predictors given nominally
equal weight (e.g., if they are simply added or averaged) will end up
being weighted by their standard deviations and predictors with
greater variance will unintentionally receive more weight. Thus, we
used the pooled overall predictor variances to scale the weights used
in each sample to ensure that the variances of the resulting composites would be on the same metric across schools (i.e., the three SAT
subtests would get equal weight when forming the SAT composite,
and the SAT composite and HSGPA would receive equal weight
when forming the full predictor composite). If not for this rescaling
procedure, each school’s composite predictors would have had
idiosyncratic scales; applying consistent unstandardized metrics to
all weights supports meaningful cross-school comparisons.
dMod_Signed Analyses. We computed dMod_Signed using the
formula in Equation 2, which calls for correlations and unstandardized descriptive statistics. We estimated the sampling variance of

2005

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS

Table 4
Meta-Analyses of dMod_Signed Effect Sizes

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Observed

Corrected for range restriction and criterion unreliability

Referent

Focal

k

N

Predictor

d Mod Signed

d Mod Signed

SDdMod Signed

SDres

95% CI

80% CV

White

Black

236

975,966

White

Hispanic

240

999,018

HSGPA
SAT Mathematics
SAT Critical Reading
SAT Writing
SAT composite
HSGPA + SAT composite
HSGPA
SAT Mathematics
SAT Critical Reading
SAT Writing
SAT Composite
HSGPA + SAT composite

.44
.38
.40
.36
.28
.23
.30
.24
.23
.21
.15
.15

.45
.38
.42
.36
.26
.20
.34
.23
.23
.21
.14
.14

.18
.17
.17
.17
.16
.15
.19
.16
.14
.14
.12
.14

.17
.16
.16
.16
.15
.14
.18
.15
.13
.13
.11
.13

(.43, .48)
(.36, .40)
(.40, .44)
(.34, .38)
(.24, .28)
(.18, .22)
(.31, .36)
(.21, .25)
(.21, .25)
(.19, .22)
(.12, .16)
(.13, .16)

(.23, .67)
(.17, .59)
(.22, .62)
(.16, .56)
(.07, .45)
(.02, .38)
(.10, .57)
(.04, .42)
(.06, .40)
(.04, .37)
(−.00, .28)
(−.02, .31)

Note. k = number of studies contributing to meta-analysis; N = total sample size; d Mod Signed = weighted mean dMod_Signed effect size; SDdMod Signed = weighted
observed standard deviation of dMod_Signed; SDres = residual standard deviation of dMod_Signed; CI = conﬁdence interval around d Mod Signed ; CV = credibility
interval around d Mod Signed ; HSGPA = high school grade point average. White–Black subgroup contrasts were based on data from 875,572 White students and
100,394 Black students. White–Hispanic subgroup contrasts were based on data from 875,568 White students and 123,450 Hispanic students.

each dMod_Signed effect size using the procedure described in the
Online Supplement. We estimated the sampling variance of each
input statistic based on the sample-size-weighted mean statistic
across all samples, as the mean observed value of a statistic is
generally a better estimate of the parameter value than any sample
statistic considered in isolation and thus permits more reliable
estimates of sampling variance (Schmidt & Hunter, 2015).
Meta-Analyses. We used Schmidt and Hunter’s (2015)
random-effects meta-analytic methods to compute meta-analyses
of dMod_Signed effect sizes. We used the “ma_generic” function from
the psychmeta R package (Dahlke & Wiernik, 2019a, 2019b) to
compute meta-analyses with inverse sampling variance weights.6

Results
Table 4 shows the results for all meta-analyses of corrected
dMod_Signed effect sizes, along with the meta-analytic means of
observed effect sizes for reference. Figure 2 shows kernel density
plots of the dMod_Signed distributions summarized by our metaanalyses, along with meta-analytic means and 80% credibility
intervals. Consistent with our ﬁndings from Study 2, these results
show that dMod_Signed for composite predictors became smaller in
magnitude as more indicators were added. Individual predictors
reliably overpredicted the performance of Black and Hispanic
students relative to White students. However, the magnitudes of
overprediction shrank when HSGPA was added to the SAT composite and the predictor approached a fully speciﬁed model. In
general, corrections for statistical artifacts had rather small impacts
on the magnitudes of mean dMod_Signed estimates, but these corrections were still important to properly estimate credibility intervals
that account for artifactual variance. All of the 80% credibility
intervals indicated a generalizable trend in the direction of overprediction except for the analyses of composites in White–Hispanic
contrasts, where the lower credibility bounds dipped just
below zero.
To help explain the dMod_Signed trends depicted in Table 4, the
values arrayed in Table 5 provide a detailed look at other

standardized effect sizes implicated in the dMod_Signed calculations.
Examining patterns in validity coefﬁcients and standardized mean
differences can provide insights into the mechanisms driving the
magnitudes and directions of dMod_Signed. Table 5 shows metaanalytic means of all referent-group predictor validities, criterion
and predictor mean differences, and the products of predictor mean
differences and referent-group validities. The patterns of validity
coefﬁcients and d values resemble the ﬁndings from Study 2:
Composite predictors had larger validities and d values than would
be anticipated from the average effects of their component predictors. These effect-size trends mean that composite predictors
(particularly those with more components) tended to have d valuevalidity products that were larger than those associated with their
average components. For White–Black and White–Hispanic contrasts, these larger product terms had the effect of driving down not
only the mean dMod_Signed estimates, but also the residual dMod_Signed
parameter distributions. The negative effect of forming composites
on dMod_Signed estimates associated with overprediction can cause
the low end of the parameter distribution to drop slightly below zero.
However, although the White–Hispanic composite effects did not
strictly generalize, the residual underprediction effects were trivial
in magnitude (e.g., −.02).
6
Our weighting procedure was consistent with Schmidt and Hunter’s
methods because, as noted in the “dMod_Signed analyses” subsection, the
sampling variance of dMod_Signed is a function of the sampling variance of its
input statistics and we estimated all the inputs’ sampling variances using the
sample-size-weighted mean statistics. This approach holds the parameter
estimates of the input statistics constant across the sampling variance
computations, which was the strategy that allowed Schmidt and Hunter to
originally justify using sample-size weights in meta-analyses of correlations.
In a correlation meta-analysis, the proportional weights of sample sizes and
inverse variances (computed based one the sample-size-weighted mean
correlation) are trivially different, and inverse variance weights are directly
proportional to N − 1 weights because the latter is the denominator of the
sampling variance formula. A similar proportionality holds for dMod_Signed’s
other input statistics (i.e., means and SDs), which means that the linear
combination of those input statistics’ variances we used to quantify dMod_Signed’s
sampling error can be inverted to obtain Schmidt–Hunter-type weights.

2006

DAHLKE AND SACKETT

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Figure 2
Density Plots of Observed and Corrected dMod_Signed Distributions Used in Meta-Analyses

Note. Density plots represent distributions after weighting effect sizes by their meta-analytic weights. Solid vertical lines indicate metaanalytic means and dashed vertical lines indicate 80% credibility intervals. HSGPA = high school grade point average.

Our focus in this study, as in Studies 1 and 2, has been on the net
differences in predicted performance between subgroups across
entire distributions of predictor scores. As a measure of average
differences in prediction, dMod_Signed does not differentiate slope
differences from intercept differences, and researchers who use
dMod_Signed effect sizes must still be mindful of whether the net
differences indicated by the effect sizes arise from slope or intercept

differences. As a supplement to our meta-analyses of dMod_Signed
effects, we meta-analyzed conditional subgroup differences in
predicted college GPAs for each of our predictors to reveal the
origins of the overall differences. These analyses are described in
Appendix B. In short, we found that the self-report HSGPA
variable was a source of sizable slope differences, whether analyzed
alone or as part of a composite with SAT scores; however, it is unclear

2007

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS

Table 5
Meta-Analytic Means of Referent-Group Validities and Referent-Focal d Values Corresponding to dMod_Signed Computations

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Referent validity of
predictor

Referent-focal d value

Product of validity and d
value

Contrast

Variable

Observed

Corrected

Observed

Corrected

Observed

Corrected

W–B

First-year college GPA
HSGPA
SAT Mathematics
SAT Critical Reading
SAT Writing
SAT composite
HSGPA + SAT composite
First-year college GPA
HSGPA
SAT Mathematics
SAT Critical Reading
SAT Writing
SAT composite
HSGPA + SAT composite

—
.37
.24
.27
.32
.33
.44
—
.37
.24
.27
.32
.33
.44

—
.49
.36
.37
.43
.44
.55
—
.49
.36
.38
.43
.44
.56

0.62
0.42
0.98
0.79
0.82
1.03
0.87
0.39
0.18
0.60
0.56
0.57
0.69
0.53

0.78
0.65
1.15
1.00
1.01
1.20
1.08
0.39
0.29
0.73
0.70
0.69
0.81
0.64

—
.16
.24
.21
.26
.34
.38
—
.07
.14
.15
.18
.23
.23

—
.32
.41
.37
.43
.53
.59
—
.14
.26
.27
.30
.36
.36

W–H

Note. W–B = White–Black contrast in which Whites are the referent group; W–H = White–Hispanic contrast in which Whites are the referent group; observed =
observed effects in measured and range-restricted data; corrected = effects corrected for multivariate range restriction and, in the case of ﬁrst-year college GPA,
corrected for criterion measurement error; HSGPA = high school GPA; GPA = grade point average.

whether the ofﬁcial school-reported HSGPAs used for operational
decision-making would also exhibit this trend. Individual SAT subtest
scores did not produce pronounced slope differences, but we did
observe that SAT composite scores produced conditional differences
in prediction that were at least moderately related to the predictor
scores. These analyses revealed that underprediction of performance
can happen at the low ends of Black and Hispanic applicants’
predictor score distributions; this indicates that the overprediction
demonstrated in our meta-analyses of dMod_Signed effects is driven by
more reliable patterns of overprediction in the middle and upper
ranges of the predictor score distributions.

Discussion
Like Study 2, Study 3 showed that composite predictors, on
average, have smaller magnitudes of overall differences in prediction than their individual components, as indexed by dMod_Signed.
Study 3 also showed that White–Black and White–Hispanic differences in prediction exhibited a generalizable lack of underprediction
(except for White–Hispanic dMod_Signed signed estimates for
composites, which had credibility intervals that narrowly included
zero). Our meta-analyses of dMod_Signed effects showed that the
performance of Black and Hispanic samples is overwhelmingly
overpredicted relative to White samples. The lower bounds of
White–Hispanic credibility intervals that overlapped with zero
were of very small magnitudes (e.g., a lower credibility bound of
−.02), such that the lack of generalizable differential prediction
corresponded to magnitudes of underprediction so small that they
would not be considered practically meaningful by traditional
effect-size interpretation practices.
Contrary to Aguinis et al.’s (2016) claims that differential prediction does not generalize across settings, we found that differential
prediction does tend to generalize across samples in White–Black
and White–Hispanic comparisons. We acknowledge that there
remains a rather large amount of unexplained variance in effects,
but the credibility intervals from our meta-analyses indicate that the

heterogeneity primarily reﬂects varying degrees of overprediction
rather than large magnitudes of underprediction. It is important to
note that the method for determining generalizability differed
between Aguinis et al.’s study and ours: Aguinis et al. used Q tests
to determine whether signiﬁcant variance of effects remained after
accounting for artifactual variance, whereas we used credibility
intervals based on residual random-effects standard deviations.
Rather than conveying generalizability in the Hunter–Schmidt sense
(i.e., answering the question, “is zero outside the middle 80% of the
estimated parameter distribution?”), Aguinis et al.’s analysis addressed heterogeneity of effects (i.e., they answered the question “is
there a signiﬁcant amount of estimated parameter variance?”). The
Q test is affected by the number of samples in an analysis and can
signal signiﬁcant parameter variance in large meta-analyses, even
when the amount of parameter variance is not practically meaningful. Credibility intervals, however, avoid interpretation issues associated with signiﬁcance testing and provide a practical test of
generalizability by displaying ranges of effect sizes. Of course,
the heterogeneity of effects is important to characterize the consistency of results and the possibility of meaningful moderators;
however, in this case, most or all of the estimated parameter variance
represents net overprediction, which is generally not viewed as a
problematic ﬁnding. Thus, we argue that our results offer a clearer
indication about the generalizability of differential prediction effects
than did Aguinis et al.’s results.
This study is notable for being the ﬁrst meta-analysis of dMod_Signed
effect sizes and the ﬁrst application of our newly derived standard
error estimator for dMod_Signed effects. We recommend that future
meta-analyses of differential prediction effects examine dMod_Signed
estimates, as dMod_Signed can be meta-analyzed easily and permits the
examination of differences in prediction across studies that need not
use the same predictor and criterion measures. By allowing various
predictor and criterion measures to be meta-analyzed together,
dMod_Signed will be a particularly useful effect size for research on
personnel selection systems, as organizations vary widely in how
they operationalize criterion and predictor constructs. Future research

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

2008

DAHLKE AND SACKETT

that uses dMod_Signed and applies high ﬁdelity artifact corrections to
personnel selection data would be useful to empirically test whether
differences in prediction generalize in the work context.
Despite the large database used in this study and the care with
which statistical artifacts were corrected, several limitations must be
noted. First, the data analyzed in this study came from a nonrandom
sampling of both schools and students, which means that our results
may not generalize to all U.S. postsecondary institutions. Second, the
only predictor variables available for analysis in this study were SAT
scores and HSGPAs, but these are not the only predictors that colleges
consider when making admissions decisions. Predictors such as
admissions ofﬁcers’ ratings of applicants’ personal statements, letters
of recommendation, extracurricular activities, and rigor of high school
course choices would be necessary to establish a truly fully speciﬁed
prediction model. Many of the predictors that could not be included in
this study require more subjectivity than SAT score or HSGPAs,
which we view as a potential source of idiosyncrasy or biased
evaluation on the part of admissions ofﬁcers that could produce
undesirable patterns of differential prediction. We strongly encourage
more research on the predictive fairness of these other predictors,
particularly considering their heightened importance in test-optional
and test-free admissions settings. Third, given that differential prediction analyses require an unbiased criterion, it is possible that some
form of criterion bias could have inﬂuenced our results. However, this
is more a limitation of the GPA metric in general than of our study in
particular. Dahlke et al. (2019) recently investigated whether criterion
contamination in the form of individual differences in course-taking
choices could explain White-minority differential validity of the SAT.
They found that White–Black and White–Hispanic differential
validity disappeared after controlling for differences in students’
course-taking choices. This type of criterion contamination may
also inﬂuence estimates of dMod_Signed.

General Discussion
We presented three studies that demonstrated important issues
regarding differential prediction analyses. In these studies, we
illustrated the importance of analyzing fully speciﬁed composites
for drawing accurate conclusions about differential prediction and
demonstrated how the magnitudes of differential prediction produced by composite predictors change as a function of the number of
predictors included in the composites and how the predictors are
weighted. We also showed that historically documented patterns of
White–Black and White–Hispanic differential prediction on the
SAT tend to generalize across schools when properly corrected
effect sizes are meta-analyzed. Additionally, we derived simpliﬁed
formulas for differential prediction effect sizes to facilitate their
usage, particularly in meta-analysis (see the Online Supplement for
formulas and sampling variance estimators). Below, we review ﬁve
main contributions made in this article.

Contribution 1: New Readily Useable dMod
Effect-Size Formulas
Regarding our improvements to dMod effect-size formulas, our
algebraic formulas are much simpler to use than Nye and Sackett’s
(2017) and Dahlke and Sackett’s (2018) integration-based formulas
and our formulas require input values that are quite easy to obtain;
this ease of implementation supports broader usage of these effect

sizes. In fact, the simplest formula calls for only a validity estimate
and two d values, which would allow dMod_Signed to be closely
approximated from statistics commonly reported in the literature.

Contribution 2: Methods to Estimate the Standard
Error of dMod_Signed
Our analytically derived methods for estimating the standard error of
dMod_Signed mean that it is no longer necessary to rely on bootstrapping
procedures to quantify the statistical uncertainty of dMod_Signed
estimates, such that these effects can now be meta-analytically
aggregated like any other standardized effect size. Up to this point.
It has not been feasible to meta-analytically cumulate estimates of
differential prediction across studies.

Contribution 3: New Insights Into the Effects
of Forming Composites on Differential Prediction
Our algebraic dMod_Signed formulas also revealed an important
insight about directions and magnitudes of differences in prediction
observed for individual predictors as opposed to those observed for
composites of multiple predictors. Given that dMod_Signed is effectively
just the difference between (a) the referent-focal mean difference on
the criterion and (b) the product of the referent validity coefﬁcient with
the referent-focal mean difference on the predictor, the fact that
composite predictors tend to have larger validities and larger mean
differences than the average of their components means that composite
predictors will tend to exhibit differences in prediction that are less
extreme than the average difference in prediction of their components.
This is a critical observation, as it clearly indicates the inadequacy of
testing individual predictors for differential prediction when evaluating
predictive bias in selection systems that rely on multiple pieces of
information to make decisions. Testing for differential prediction in
compensatory selection systems is best done using composites that
support operational interpretations (Sackett et al., 2003; SIOP, 2018).
In addition to the fact that testing composites for predictive bias is
more statistically sound than including multiple predictor variables in a
single Cleary model analysis, composite predictors tend to exhibit
smaller standardized differences in prediction than their components
and may lead to different conclusions about differential prediction than
would separate analyses of their component predictors. In Study 1, we
reanalyzed data from Keiser et al. (2016) to show that combining ACT
scores with personality variables drastically reduced the magnitude by
which women’s college GPAs were underpredicted compared to using
ACT scores alone. These results provided an effect-size accompaniment
to Keiser et al.’s original regression-based inferences and emphasized
the importance of avoiding the omitted variables problem. Study 2
examined the implications of composite variables in more detail and
showed that one’s choices of predictors and predictor weighting
schemes have predictable impacts on magnitudes of differential prediction. In fact, one can reduce the risk of predictive bias against a minority
group by using Pareto-optimal weights that give greater emphasis to
adverse impact reduction than validity maximization; thus, one could
view Pareto-optimization as a method for balancing validity concerns
against both adverse impact potential and risk of underprediction
(assuming, of course, that mean differences on the criterion and
predictors favor the referent group and validity is positive).
Examining composite predictors for differential prediction in
compensatory multipredictor selection systems is critical for

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS

drawing accurate conclusions regarding operational trends, but the
most operationally sound analyses should also account for the
effects of range restriction and criterion measurement error. Range
restriction’s effects on differential prediction results can be confronted by implementing modern missing data approaches in one’s
analyses. Sophisticated procedures to account for the effects of
missing data on statistical results are becoming more accessible to
researchers and these procedures hold promise for supporting more
accurate conclusions about differential prediction. Methods such as
multiple imputation and full-information maximum likelihood
(FIML) estimation (see Newman, 2014 for an overview) can
help researchers to correct for range restriction in the form of
missing criterion observations and may therefore facilitate more
accurate regression model contrasts within the Cleary framework.
We encourage additional research on the application of missing data
methods to differential prediction analyses and the development of
best practice recommendations for such analyses.
As for criterion measurement error, we recommend that researchers correct for this artifact when computing dMod effect sizes (see the
Online Supplement for formulas that include measurement-error
corrections). Accounting for the effects of measurement error is
important for computing dMod effect sizes that accurately reﬂect the
operational impacts of differential prediction. However, as with any
analysis in the realm of personnel psychology, correcting for
measurement error is no replacement for researchers analyzing
the most relevant and most reliable criterion measurements available
to them; this will reduce reliance on statistical corrections when
computing dMod effect sizes and improve the statistical power of
differential prediction analyses.

Contribution 4: Revised Conclusions About the
Prevalence of Overprediction and Under prediction
We used the above ideas about applying dMod to composites to
revisit Aguinis et al.’s (2016) controversial ﬁnding that underprediction of racial/ethnic group performance is common. We
analyzed a more current version of the same large-scale college
admissions database and showed that, with appropriate analyses at
the level of composites, the classic ﬁnding that overprediction is
dominant is reconﬁrmed.

Contribution 5: Insights Into Relationships Among
Differential Prediction, Subgroup Differences, and
Criterion-Related Validity
Related to our contributions to the quantiﬁcation of differential
prediction, this research offers profound insights into prospects for
simultaneous achievement of three desirable objectives: high
criterion-related validity, small subgroup differences, and lack of
predictive bias. Consider the meta-analytic mean White–Black job
performance d value of .46 from Study 1. To eliminate differential
prediction, the product of dX and r XY 1 must equal .46. The smallest
dX that can achieve this is .46 if the predictor is perfectly valid.
However, predictive validity of 1.0 is never achievable in current
applied work. We offer an r XY 1 of .60 as a rough estimate of the
upper end of the attainable r XY 1 range. With r XY 1 = .60, dX must be
approximately .77 for the product of the two to equal .46. What this
analytic exercise shows is that it impossible to simultaneously attain
small (i.e., near-zero) subgroup differences and a net average effect

2009

of zero differential prediction. Efforts to reduce subgroup differences (e.g., by using equal weights rather than regression weights)
may achieve that goal but will also produce/increase overprediction.
This helps to understand the common organizational position that
the concern regarding predictive bias is the underprediction of
minority performance. Overprediction of minority performance
does not reﬂect bias against the minority group, and increased
overprediction is a common result of attempts to reduce subgroup
mean differences. We offer the proposition that, if told, “you have a
choice: reduce adverse impact, but with increased overprediction, or
reduce overprediction, but with increased adverse impact,” concerns
for increased diversity will likely take precedence. We suspect that
many advocates of an “any departure from a common regression line
is unacceptable” policy do not fully understand the implications of
their position.
Our algebraic approach to computing dMod_Signed provides selection researchers and practitioners with a simple heuristic for creating
strategies that will reduce differences in prediction. However, as
overprediction is not generally viewed as a problem, this is naturally
a bigger asset for settings in which underprediction occurs. Assuming that validity is positive, if one knows the direction and magnitude of dY and that d Mod Signed = dY − r XY 1 dX , the prescription for
mitigating differential prediction is clear: Seek out a set of predictors
that will help the product of r XY 1 and dX to balance out the value of
dY. Of course, one must keep in mind how criterion-related validity
and adverse-impact potential relate to organizational objectives; as
we described above, differential prediction, criterion-related validity, and adverse-impact potential are inextricably linked, and we
expect it is quite rare that one can simultaneously satisfy one’s goals
in all three areas.

Conclusion
The methodological advancements and research ﬁndings we have
reported here support the usage of operational analyses for differential prediction as recommended in SIOP’s (2018) Principles. We
derived updated dMod effect-size methods that will support the
quantiﬁcation of differential prediction in both primary research
and meta-analyses. We also demonstrated statistical principles
related to composites that inﬂuence how the magnitude and direction of dMod_Signed can be anticipated when designing selection
systems, with the fundamental concept being this: As a selection
system approaches a fully speciﬁed model of the criterion using
well-developed predictors, differential prediction will tend to
decrease in magnitude. Our large-scale analyses of postsecondary
admissions data support historic ﬁndings regarding overprediction
of minority performance, even after accounting for statistical artifacts. It is our hope that the tools, principles, and ﬁndings we have
presented here will contribute to the foundations underlying the next
generation of research on differential prediction.

References
Aguinis, H., Culpepper, S. A., & Pierce, C. A. (2010). Revival of test bias
research in preemployment testing. Journal of Applied Psychology, 95(4),
648–680. https://doi.org/10.1037/a0018714
Aguinis, H., Culpepper, S. A., & Pierce, C. A. (2016). Differential prediction
generalization in college admissions testing. Journal of Educational
Psychology, 108(7), 1045–1059. https://doi.org/10.1037/edu0000104

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

2010

DAHLKE AND SACKETT

Aitken, A. C. (1934). Note on selection from a multivariate normal population. Proceedings of the Edinburgh Mathematical Society (Series 2), 4(2),
106–110. https://doi.org/10.1017/S0013091500008063
Bartlett, C. J., Bobko, P., Mosier, S. B., & Hannan, R. (1978). Testing for
fairness with a moderated multiple regression strategy: An alternative to
differential analysis. Personnel Psychology, 31(2), 233–241. https://
doi.org/10.1111/j.1744-6570.1978.tb00442.x
Beatty, A. S., Walmsley, P. T., Sackett, P. R., Kuncel, N. R., & Koch, A. J.
(2015). The reliability of college grades. Educational Measurement:
Issues and Practice, 34(4), 31–40. https://doi.org/10.1111/emip.12096
Berry, C. M., & Zhao, P. (2015). Addressing criticisms of existing predictive
bias research: Cognitive ability test scores still overpredict African
Americans’ job performance. Journal of Applied Psychology, 100(1),
162–179. https://doi.org/10.1037/a0037615
Bobko, P., & Roth, P. L. (2013). Reviewing, categorizing, and analyzing the
literature on Black-White mean differences for predictors of job performance: Verifying some perceptions and updating/correcting others. Personnel Psychology, 66(1), 91–126. https://doi.org/10.1111/peps.12007
Campbell, J. P. (1990). Modeling the performance prediction problem in
industrial and organizational psychology. In M. D. Dunnette, & L. M.
Hough (Eds.), Handbook of industrial and organizational psychology
(2nd ed., Vol. 1). Consulting Psychologists Press, Inc.
Cheung, M. W.-L., & Chan, W. (2004). Testing dependent correlation
coefﬁcients via structural equation modeling. Organizational Research
Methods, 7(2), 206–223. https://doi.org/10.1177/1094428104264024
Cleary, T. A. (1968). Test bias: Prediction of grades of negro and white
students in integrated colleges. Journal of Educational Measurement,
5(2), 115–124. https://doi.org/10.1111/j.1745-3984.1968.tb00613.x
Dahlke, J. A., Kostal, J. W., Sackett, P. R., & Kuncel, N. R. (2018). Changing
abilities vs. changing tasks: Examining validity degradation with test scores
and college performance criteria both assessed longitudinally. Journal of
Applied Psychology, 103(9), 980–1000. https://doi.org/10.1037/apl0000316
Dahlke, J. A., & Sackett, P. R. (2018). Reﬁnements to effect sizes for tests of
categorical moderation and differential prediction. Organizational Research
Methods, 21(1), 226–234. https://doi.org/10.1177/1094428117736591
Dahlke, J. A., Sackett, P. R., & Kuncel, N. R. (2019). Effects of range
restriction and criterion contamination on differential validity of the SAT
by race/ethnicity and sex. Journal of Applied Psychology, 104(6), 814–
831. https://doi.org/10.1037/apl0000382
Dahlke, J. A., & Wiernik, B. M. (2019a). psychmeta: An R package for
psychometric meta-analysis. Applied Psychological Measurement, 43(5),
415–416. https://doi.org/10.1177/0146621618795933
Dahlke, J. A., & Wiernik, B. M. (2019b). psychmeta: Psychometric metaanalysis toolkit (2.3.2) [R; R Package]. https://CRAN.R-project.org/packa
ge=psychmeta (Original work published 2017).
De Corte, W., Lievens, F., & Sackett, P. R. (2007). Combining predictors to
achieve optimal trade-offs between selection quality and adverse impact.
Journal of Applied Psychology, 92(5), 1380–1393. https://doi.org/10
.1037/0021-9010.92.5.1380
Duhachek, A., & Iacobucci, D. (2004). Alpha’s standard error (ASE): An
accurate and precise conﬁdence interval estimate. Journal of Applied
Psychology, 89(5), 792–808. https://doi.org/10.1037/0021-9010.89.5.792
Fischer, F. T., Schult, J., & Hell, B. (2013). Sex-speciﬁc differential
prediction of college admission tests: A meta-analysis. Journal of Educational Psychology, 105(2), 478–488. https://doi.org/10.1037/a0031956
Hartigan, J., & Wigdor, A. (1989). Fairness in employment testing. Science,
245(4913), 14–14. https://doi.org/10.1126/science.2740906
Higdem, J. L., Kostal, J. W., Kuncel, N. R., Sackett, P. R., Shen, W., Beatty,
A. S., & Kiger, T. B. (2016). The role of socioeconomic status in SATfreshman grade relationships across gender and racial subgroups. Educational Measurement: Issues and Practice, 35(1), 21–28. https://doi.org/10
.1111/emip.12103
Hunter, J. E., Schmidt, F. L., & Le, H. (2006). Implications of direct and
indirect range restriction for meta-analysis methods and ﬁndings. Journal

of Applied Psychology, 91(3), 594–612. https://doi.org/10.1037/00219010.91.3.594
Keiser, H. N., Sackett, P. R., Kuncel, N. R., & Brothen, T. (2016). Why women
perform better in college than admission scores would predict: Exploring the
roles of conscientiousness and course-taking patterns. Journal of Applied
Psychology, 101(4), 569–581. https://doi.org/10.1037/apl0000069
Kling, K. C., Noftle, E. E., & Robins, R. W. (2013). Why do standardized
tests underpredict women’s academic performance? The role of conscientiousness. Social Psychological and Personality Science, 4(5), 600–
606. https://doi.org/10.1177/1948550612469038
Kostal, J. W., Kuncel, N. R., & Sackett, P. R. (2015). Grade inﬂation marches
on: Grade increases from the 1990s to 2000s. Educational Measurement:
Issues and Practice, 35(1) https://doi.org/10.1111/emip.12077
Lautenschlager, G. J., & Mendoza, J. L. (1986). A step-down hierarchical
multiple regression analysis for examining hypotheses about test bias in
prediction. Applied Psychological Measurement, 10(2), 133–139. https://
doi.org/10.1177/014662168601000202
Lawley, D. N. (1943). A note on Karl Pearson’s selection formulae.
Proceedings of the Royal Society of Edinburgh. Section A: Mathematical
and Physical Sciences, 62(1), 28–30. https://doi.org/10/ckc2
Linn, R. L. (1978). Single-group validity, differential validity, and differential prediction. Journal of Applied Psychology, 63(4), 507–512. https://
doi.org/10.1037/0021-9010.63.4.507
Linn, R. L., & Werts, C. E. (1971). Considerations for studies of test bias.
Journal of Educational Measurement, 8(1), 1–4. https://doi.org/10.1111/j
.1745-3984.1971.tb00898.x
Mattern, K. D., & Patterson, B. F. (2013). Test of slope and intercept bias in
college admissions: A response to Aguinis, Culpepper, and Pierce (2010).
Journal of Applied Psychology, 98(1), 134–147. https://doi.org/10.1037/
a0030610
McKay, P. F., & McDaniel, M. A. (2006). A reexamination of black-white
mean differences in work performance: More data, more moderators.
Journal of Applied Psychology, 91(3), 538–554. https://doi.org/10.1037/
0021-9010.91.3.538
Mulaik, S. A. (2010). Foundations of factor analysis. CRC Press.
Newman, D. A. (2014). Missing data: Five practical guidelines. Organizational Research Methods, 17(4), 372–411. https://doi.org/10.1177/
1094428114548590
Nye, C. D., & Sackett, P. R. (2017). New effect sizes for tests of categorical
moderation and differential prediction. Organizational Research Methods,
20(4), 639–664. https://doi.org/10.1177/1094428116644505
Ramist, L., Lewis, C., & McCamley, L. (1990). Implications of using
freshman GPA as the criterion for the predictive validity of the SAT. In
W. W. Willingham, W. H. Angoff, R. Morgan, & L. Ramist (Eds.),
Predicting college grades: An analysis of institutional trends over two
decades (pp. 253–288). Educational Testing Service.
Roth, P. L., Switzer, F. S., III, Van Iddekinge, C. H., & Oh, I.-S. (2011). Toward
better meta-analytic matrices: How input values can affect research conclusions in human resource management simulations. Personnel Psychology,
64(4), 899–935. https://doi.org/10.1111/j.1744-6570.2011.01231.x
Rotundo, M., & Sackett, P. R. (1999). Effect of rater race on conclusions
regarding differential prediction in cognitive ability tests. Journal of Applied
Psychology, 84(5), 815–822. https://doi.org/10.1037/0021-9010.84.5.815
Sackett, P. R., & Ellingson, J. E. (1997). The effects of forming multi-predictor
composites on group differences and adverse impact. Personnel Psychology,
50(3), 707–721. https://doi.org/10.1111/j.1744-6570.1997.tb00711.x
Sackett, P. R., Laczo, R. M., & Lippe, Z. P. (2003). Differential prediction and the
use of multiple predictors: The omitted variables problem. Journal of Applied
Psychology, 88(6), 1046–1056. https://doi.org/10.1037/0021-9010.88.6.1046
Schmidt, F. L., & Hunter, J. E. (2015). Methods of meta-analysis: Correcting
error and bias in research ﬁndings (3rd ed.). Sage Publications; https://
doi.org/10.4135/9781483398105
Shewach, O. R., Shen, W., Sackett, P. R., & Kuncel, N. R. (2017).
Differential prediction in the use of the SAT and high school grades in

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

ASSESSING PREDICTIVE BIAS WITH MULTIPLE PREDICTORS
predicting college performance: Joint effects of race and language.
Educational Measurement: Issues and Practice, 36(3), 46–57. https://
doi.org/10.1111/emip.12150
Society for Industrial and Organizational Psychology (SIOP). (2018). Principles for the validation and use of personnel selection procedures.
Industrial and Organizational Psychology: Perspectives on Science
and Practice, 11(S1), 1–97. https://doi.org/10.1017/iop.2018.195
Song, Q. C. (2018). Pareto-optimization via normal boundary intersection
method in diversity hiring [R]. https://github.com/Diversity-ParetoOptima
l/ParetoR (Original work published 2017).
Song, Q. C., Wee, S., & Newman, D. A. (2017). Diversity shrinkage: Crossvalidating pareto-optimal weights to enhance diversity via hiring practices.
Journal of Applied Psychology, 102(12), 1636–1657. https://doi.org/10
.1037/apl0000240

2011

Stricker, L. J., Rock, D. A., & Burton, N. W. (1993). Sex differences in
predictions of college grades from scholastic aptitude test scores. Journal
of Educational Psychology, 85(4), 710–718. https://doi.org/10.1037/
0022-0663.85.4.710
Van Iddekinge, C. H., Roth, P. L., Raymark, P. H., & Odle-Dusseau, H. N.
(2012). The criterion-related validity of integrity tests: An updated metaanalysis. Journal of Applied Psychology, 97(3), 499–530. https://doi.org/
10.1037/a0021196
Young, J. W. (2001). Differential validity, differential prediction, and
college admission testing: A comprehensive review and analysis (No.
2001-6). College Board.
Yu, M. C., Sackett, P. R., & Kuncel, N. R. (2016). Predicting college performance of homeschooled versus traditional students. Educational Measurement: Issues and Practice, 35(4), 31–39. https://doi.org/10.1111/emip.12133

Appendix A
Overview of the Cleary Model of Predictive Bias
The Cleary model (Cleary, 1968) relies on multiple moderated
linear regression to compare nested models and determine whether
including subgroup differences in slopes and/or intercepts improves
model ﬁt. Lautenschlager and Mendoza (1986) formulated a fourmodel step-down procedure that improved the power of this analysis, and modern implementations of the procedure (e.g., Aguinis et
al., 2010; Rotundo & Sackett, 1999) rely on comparisons among
three nested regression models (A1–A3):
Model 1∶Y i = b0 + b1 X i + ei

(A1)

Model 2∶Y i = b0 + b1 X i + b2 Gi + ei

(A2)

Model 3∶Y i = b0 + b1 X i + b2 Gi + b3 GX i + ei

(A3)

where i indexes observations, Y is the criterion variable, b0 is the model
intercept, b1 is the slope coefﬁcient for the predictor variable (X), b2 is
the intercept-difference coefﬁcient for the group-membership dummy
variable (G), b3 is the slope-difference coefﬁcient for the product of

predictor scores and group-membership codes (GX), and e represents
model residuals (i.e., error).
First, to test whether there are any differences in prediction
between the two groups, one must compare Models 1 and 3. If
these models are signiﬁcantly different, it means that the subgroups’
data cannot be adequately described using a single regression line.
Next, to determine whether the group-membership dummy variable
moderates the association between X and Y (i.e., the groups exhibit
slope differences) or it simply has a main effect on Y (i.e., the groups
exhibit intercept differences), one must compare Models 2 and 3. If
Model 3 ﬁts the data signiﬁcantly better than Model 2, one can
conclude that differential prediction has occurred in the form of
slope differences. If Model 3 does not demonstrate superior ﬁt,
one must compare Model 2 to Model 1 to determine whether there
are signiﬁcant differences in intercepts. Note that, even if Model 3
differs from Model 1, it is possible that one would fail to detect
differential prediction if Model 2 does not differ from Model 3 or
Model 1.

Appendix B
Supplemental Analyses of Conditional Differences in Prediction for Study 3
As a supplement to our summaries of differential prediction effect
sizes, we analyzed conditional subgroup differences in prediction
across Study 3’s predictor distributions to show the nature of the
differences (i.e., slope vs. intercept differences). In these analyses of
conditional differences, intercept differences can be inferred if the
mean differences across samples produce a ﬂat trend and slope
differences can be inferred if the mean differences are correlated
with predictor scores.
We used data corrected for criterion measurement error and range
restriction to ﬁt a separate regression model for each predictor and
each subgroup at each school. Then, for each referent-focal contrast
comparing the performance of a given predictor within a given
school, we generated predicted college GPAs for each subgroup
(with corresponding conditional error variances) based on 61
equally spaced predictor scores that ranged −3 to 3 SDs from the
focal group’s grand mean; these predictor scores represented the
distribution of focal group predictor scores across all schools
analyzed. After we generated predicted GPAs in all settings, we

computed the referent-focal differences in predictions at each
predictor score along with the error variances of the differences
in prediction, which are simply sums of the individual subgroups’
conditional regression error variances. We standardized the conditional differences in prediction and their standard errors by dividing
the values by the referent group’s criterion standard deviation, as is
done when computing dMod statistics.
We meta-analyzed the conditional differences in prediction for
each referent-focal contrast, each predictor variable, and each predictor score. Our meta-analyses of conditional differences used
restricted maximum likelihood (REML) estimation. Figure B1
summarizes the results of these meta-analyses, with 80% credibility
bands around the weighted average differences. Note that, with this
strategy, the aggregate trends need not be strictly linear because the
weights differed across meta-analyses.
The results in Figure B1 reveal that slope differences do occur,
but they are primarily associated with self-reported HSGPAs when
analyzed as a stand-alone predictor or as a component of an SAT

(Appendices continue)

2012

DAHLKE AND SACKETT

This document is copyrighted by the American Psychological Association or one of its allied publishers.
This article is intended solely for the personal use of the individual user and is not to be disseminated broadly.

Figure B1
Meta-Analytic Estimates of Standardized Conditional Differences in Prediction

Note. Positive differences in prediction indicate overprediction of Black or Hispanic students’ performance. Solid black lines represent REML-weighted
average standardized differences in predicted ﬁrst-year college GPAs and gray bands represent 80% credibility regions. The dashed black lines are reference
lines for differences of zero. REML = restricted maximum likelihood; GPA = grade point average.

and HSGPA composite. These slope differences were such that
overprediction was more pronounced for high predictor scores,
while low predictor scores were associated with average differences near zero or slightly below zero, which indicates small
magnitudes of underprediction. It is important to note that our
HSGPA data were self-reported, and it is not clear whether these
trends would generalize to ofﬁcial school-reported HSGPAs. It is
possible that the slope differences are, at least in part, an artifact of
the self-report nature of the data; additional research is needed to
explore this possibility.
Composite SAT scores (without HSGPAs) showed weaker slopedifference trends, but the SAT subtest score trends were quite ﬂat,
indicating that intercept differences dominate. Differences in

prediction at the low ends of the predictor score distributions
exhibited substantial heterogeneity across predictors, such that
widely varying differences are possible for low scorers. The 80%
credibility regions include negative values at the low ends of all
predictor score distributions, meaning that some degree of underprediction occurs for low scorers in a subset of settings. The middle
and high ranges of predictor score distributions were associated with
overprediction effects that tended to generalize across schools.

Received June 22, 2020
Revision received September 24, 2021
Accepted October 18, 2021 ▪


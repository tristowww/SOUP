Received: 24 July 2017

Revised: 24 January 2018

Accepted: 25 January 2018

DOI: 10.1111/peps.12263

ORIGINAL ARTICLE

Quantifying with words: An investigation of the
validity of narrative-derived performance scores
Andrew B. Speer
Wayne State University
Correspondence
Andrew B. Speer, Wayne State University, 5057
Woodward Ave, Room 8402.24, Detroit, MI
48202.
Email: speerworking@gmail.com

Abstract
Performance appraisal research has focused almost entirely on traditional numerical ratings despite narrative text comments regularly
being collected within appraisals. This study investigated the theory
and utility of leveraging narrative comments to better understand
employee performance. Narrative sentiment scores were derived
using text mining on a large sample of narrative comments. These
scores were then applied to an independent set of 2 years of performance data. It was assumed that narrative comments would reflect
true performance variance that overlaps with traditional ratings, but
also that they would capture incremental variance due to increases
in total information and a reduction in rater-motivated biases in contexts in which narrative data were not explicitly linked to administrative outcomes. The derived narrative scores were reliable across
years, converged with traditional numerical ratings and explained
incremental variance in future performance outcomes (performance
ratings, involuntary turnover, promotions, and pay increases). Collectively, this study highlights how narratives can enhance performance
measurement and demonstrates how these data can be economically
scored in applied settings.

The measurement of employee performance (DeNisi & Murphy, 2017) is one of the most important components of
human resource practices, and yet it is an area that has received considerable criticism in recent years. A quick review
of organizational research leads one to conclude that performance management systems are broken (e.g., Pulakos
& O'Leary, 2011; Pulakos, Hanson, Arad, & Moye, 2015). They suffer from low interrater reliability (Scullen, Mount,
& Goff, 2000; Viswesvaran, Ones, & Schmidt, 1996), a lack of discrimination among dimensions (e.g., Balzer & Sulsky, 1992), contamination and deficiency (Cascio & Aguinis, 2005), source effects (e.g., Hoffman & Woehr, 2009;
Lance, Hoffman, Gentry, & Baranik, 2008), rater biases (Landy & Farr, 1980), context effects (Harris, 1994; Jawahar
& Williams, 1997), and low user acceptability (Pulakos et al., 2015). These issues are concerning, and yet despite the
criticisms performance management systems are here to stay; they serve vital functions for organizations (e.g., pay
documentation, promotion decisions, data for employee development) that simply cannot be replaced by more subjective and undocumented means of decision making. Given this, it is vital to continue researching innovative approaches
to improve performance measurement.
Personnel Psychology. 2018;71:299–333.

wileyonlinelibrary.com/journal/peps

c 2018 Wiley Periodicals, Inc.


299

SPEER

One way to further this research is to unearth novel methods to systematically glean performance-related information from traditional performance data sources, and there is a data source that, although widely available, has
been severely underutilized: narrative performance comments. These qualitative text descriptions of employee performance frequently accompany traditional numerical ratings (Brutus, 2010) and offer rich contextual information about
employee performance, such as descriptions of competency behaviors, goal attainment, and general observations in
line with situational factors. In a recent survey of senior human resources leaders, Gorman, Meriac, Roch, Ray, and
Gamble (2017) found that 84% of companies use written summaries within performance appraisals, a proportion that
clearly warrants attention toward this topic.
Researchers have started investigating narrative comments with greater purpose, but, in general, this data source
has been ignored within the performance research literature (Brutus, 2010). This is not surprising. After all, until
recently most data were not electronically gathered, analyzing such data required laborious manual coding, and scoring of such text in a standardized fashion has been difficult. Basically, systematically taking and gleaning insights from
narrative data has been a challenge that up until recently required both a lot of time and a lot of resources. As such,
numerical ratings have ruled the day. This is unfortunate, as comments provide rich, contextual information about performance. Furthermore, because they are usually informal and not directly tied to administrative decisions (e.g., determining pay), they are less likely to be influenced by culturally and socially determined rating influences (Brutus, 2010).
This paper proposes that narrative comments contain true performance-related variance that is both reliable and
offers unique insights that are not captured by traditional numerical ratings. In examining this, advancements in text
mining (e.g., Ignatow & Mihalcea, 2017; Kobayashi, Mol, Berkers, Kismihók, & Den Hartog, 2017a, 2017b; Liu, 2012;
Pang & Lee, 2008) were applied to systematically score narrative performance data. Specifically, text mining was leveraged to build a custom dictionary to score performance narratives within a large organization. In doing this, 3 years of
over 15,000 performance ratings were analyzed and used to derive an algorithm from text provided during the performance appraisal. This model was then applied to predict performance ratings for subsequent years completely independent from the calibration sample. Construct validity and incremental prediction were evaluated in lieu with variables within the nomological network of performance. Furthermore, the derived narrative scores were used to investigate rater effects and whether specific segments of the traditional-numeric rating distribution could be improved by
leveraging the narrative data in combination.
This paper contributes to the performance management literature in several ways. First, systematic efforts to code
narrative comments have been underresearched (and therefore undeveloped), with only a handful of studies attempting this or similar work (Christianson DeMay, Chandonnet, Rasinowich, & Fenlason, 2006; Hedricks, Robie, Rupayana,
& Puchalski, 2017; Rupayana, Hedricks, Robie, & Puchalski, 2017). This study is the first to leverage the necessary
methodological design to test the efficacy of narrative sentiment scores, particularly by applying text mining within a
pure performance context, employing calibration and holdout samples, developing a custom-dictionary specific to a single organization, and developing models optimized to predict outcomes in independent samples. It therefore provides
a strong test of the efficacy of narrative comments, with applications for both academics and practitioners. Second,
narrative scores were tested using a range of performance-related outcomes, both concurrent and longitudinal, and
therefore establishes validity evidence of derived narrative scores. Third, this paper looks at when narratives might be
most informative and in what location of the traditional rating scale narrative scores would be most variable and explain
the most unique variance. Finally, like Campion, Campion, Campion, and Reider (2016), this paper demonstrates ways
to leverage recent enhancements in computer technology to better understand phenomena in the organizational sciences. Altogether, this paper investigates how comment data can be conceptualized and easily extracted to improve
performance measurement within organizations.

1

BRIEF OVERVIEW OF PERFORMANCE EVALUATION

Since the early 20th century, performance ratings have been frequently used and researched in organizations (Austin
& Villanova, 1992). In most performance management systems, employees are rated by their immediate supervisor on

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

300

301

a range of performance competencies or goals. The exact format of these ratings will vary (Landy & Farr, 1980), but in
most cases, the ratings will be made using closed-format scales (e.g., graphic rating scale) that are assigned numerical
values. For the sake of clarification within this manuscript, I will use the labels “traditional numerical ratings,” “traditional ratings,” or “numerical ratings” for all closed rating formats used in performance management. These include
ratings made using graphical rating scales, behavioral observation scales, or behaviorally anchored scales, among other
closed-end survey-based formats.
In addition to these traditional numerical ratings, it is also common for raters to provide qualitative text describing the employee's performance (Gorman et al., 2017). For instance, raters may be provided a comment box to give a
detailed description for the competencies that are rated, or for overall evaluations of an employee. Narratives contain
one to multiple sentences describing single performance topics (e.g., “Tonya consistently exhibits enthusiasm when
interacting with customers, greeting them as soon as they walk into the building”), multiple performance topics, or general performance descriptions (e.g., “Tonya is a star performer, and I couldn't ask for a better contributor on my team”).
They provide context around ratings and offer rich accounts of actual employee behaviors. I use the term “narrative
comments” or “qualitative ratings” for all text-based data received in open-format during the performance management process.
Although each of these types of ratings are common to the performance appraisal (PA) process, research on performance appraisals has focused almost entirely on traditional numerical ratings (Brutus, 2010; David, 2013; Smither &
Walker, 2004). There are many reasons for this. Traditional numerical ratings naturally provide a standardized scoring
format, thus allowing for ease of decision making. If an organization must assign pay or make some sort of administrative choice, it is much easier to do so when those decisions can be tied back to a quantified score. Measurement
involves quantification, and rating scales provide direct values that employees can be compared upon. This is particularly important to satisfy legal requirements for performance appraisals (Brutus, 2010). Because of their inherent
numerical properties, they are also easily analyzed by researchers to understand score distributions, factor structures
of performance, and relationships with other constructs. Rating scales are the predominant method to assess psychological phenomena in almost every other area of organizational research, making them a natural fit within performance
contexts. Finally, they are economical from an effort standpoint (Brutus, 2010; Murphy & Cleveland, 1995), a component that is important given the many competing responsibilities for managers.
Traditional numerical ratings are the core of performance appraisals, and yet they do suffer from measurement
issues. For one, the literature clearly demonstrates that there are issues with the reliability of such ratings (Scullen
et al., 2000; Viswesvaran et al., 1996). Although a thorough understanding of this and whether it is unique to just a
traditional rating format is beyond the scope of this paper, it is safe to say that the traditional numerical rating format
does not capture as much true score variance as we would like. There is room for improvement.
Second, the purpose and goals of the appraisal produce bias in traditional numerical performance ratings. Research
suggests that ratings are more lenient when administrative outcomes are tied to performance ratings than when conducted for developmental or feedback purposes (e.g., DeCotiis & Petit, 1978; Jawahar & Williams, 1997; Zedeck & Cascio, 1982). When base pay or annual bonuses are tied to the performance ratings, this is not surprising, and one can even
sympathize with the manager who elevates a poor performer's ratings to “acceptable” to ensure that employees are not
left in the cold when bonus paychecks come. Raters are also hesitant to make severe ratings for interpersonal reasons.
For instance, lower ratings could harm the subordinate–manager relationship (Harris, 1994), an effect that occurs due
to differences in raters’ motivations when completing ratings (Murphy, Cleveland, Skattebo, & Kinney, 2004). On the
other hand, raters who value development might provide lower ratings in some areas to highlight gaps upon which subordinates can develop. All told, it is false to assume that raters are always motivated to provide accurate ratings that
best represent true performance levels of rated targets (Murphy et al., 2004).
Third, unless ratings are made on an extremely precise scale covering a large number of performance-related behaviors, strictly quantitative ratings provide little context to understand why a particular rating was made. For example,
receiving a below average rating on the dimension of adaptability, although succinct, is not incredibly informative. On
the other hand, narrative comments allow one to comprehend the reasoning behind numerical ratings (Brutus, 2010;
Kabins, 2016), providing rich data regarding a person's behaviors within specific contexts and how others perceive

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

SPEER

SPEER

them. In this example, information such as “you failed to adopt usage of a new technology system and instead relied on
old methods to get work done” would provide much richer information. To exacerbate this issue, many organizations
are simplifying the rating process by limiting the number of numerical ratings within an appraisal, resulting in much
simpler and more generic surveys (Buckingham & Goodall, 2015).
Narratives are likely to suffer from similar issues. However, there is reason to believe that narrative comments represent true performance variance (Brutus, 2010) and that there may also be situations where narrative comments are
likely to improve total performance measurement. The problem is that with little empirical research on this topic, one
cannot confidently speak to aspects such as the reliability, validity, and moderators of performance narratives. As such,
the next section outlines similarities between traditional numerical ratings and narrative comments and then discusses
why narrative comments might be a useful source of data within the PA context.

2

MEASUREMENT USING NARRATIVE COMMENTS

Performance narratives act as free-form comments where raters can describe ratee goal obtainment, competencyrelated behaviors, and how ratee behavior impacted others. They are complex and often multithemed statements
about the valence of ratee behavior (Brutus, 2010) and given their free-form nature, offer raters chances to elaborate
upon their ratings regarding the context in which employee behavior occurred. This also affords raters the opportunity to provide formal development tips or future improvement suggestions, collectively making narratives a vehicle of
useful ratee information that should align with other measures of job performance.
Many appraisal processes incorporate both traditional and narrative components (Brutus, 2010; Gorman et al.,
2017), and when considering the relationship between these two forms of evaluation, it is helpful to consider how
each are formed. In this sense, DeNisi, Cafferty, and Meglino's (1984) Cognitive Model of the Performance Appraisal is
a useful framework to work within, which outlines six steps that occur during the rating process: (1) the rater observes
behavior(s) of the ratee, (2) that behavior is formed into some cognitive representation by the rater, (3) the representation is stored in memory, (4) the information is retrieved for formal evaluation, (5) retrieved information is reconsidered
and integrated with other units of information, and (6) evaluations are assigned. The model is sequential and the steps
interrelated, with improvements to each phase enhancing the overall quality of evaluation in step 6. In this final step,
DeNisi et al. indicate that the evaluations occur using some rating instrument. Here, narrative comments can be treated
as an instrument or device used to provide performance information.
Although detecting, interpreting, and mentally storing observed information is vital to judgments of others, steps
4–6 of the DeNisi et al. (1984) model are most proximal to similarities and differences between narrative comments
and traditional ratings (retrieving information from memory, synthesizing that information, and then making evaluations). Both traditional ratings and qualitative comments are based upon recollections of ratee behavior, which collectively are organized into general impressions of ratee performance regarding specific performance domains. Raters
will exert cognitive effort to recall ratee behavior and categorize that behavior into schemas that reflect the type and
valence of behavior. Because of this, each type of rating should be based off at least similar information. Indeed, empirical research shows that there is convergence between the two data sources (David, 2013; Smither & Walker, 2004),
and each method should be limited by similar types of judgment errors (e.g., Landy & Farr, 1980) and dependencies
on opportunities to observe ratee performance (e.g., Hoffman & Woehr, 2009; Lance et al., 2008). Basically, traditional
ratings and narrative scores should demonstrate a great deal of overlap and each reflect ratee behavior.
Of course, it should be made clear that much of the theoretical understanding of comments will be nuanced, as the
context in which narratives are developed in and the nature of comments themselves will vary. For example, Brutus
(2010) describes several characteristics that differentiate comments, such as the amount or length of text, the valence
(positive or negative), the amount of domain coverage (how much of the multidimensional construct space of performance is assessed), specificity (how detailed a comment describes a particular performance theme), and whether or not
comments offer suggestions for development. Further, differences in survey design (e.g., number and types of question
prompts), contextual factors (e.g., organizational feedback norms), rater factors (e.g., verbal ability), ratee factors (e.g.,

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

302

feedback seeking tendency), and rater-by-ratee factors (e.g., relationship quality) will likely impact the elicited comment data within a PA context. These factors make interpretation of narratives a challenging endeavor.
It should also be made clear that there are distinct differences between the two rating mediums that are likely to
produce differences in construct measurement, which will be addressed in upcoming sections. For now, we can assume
that narrative scores and traditional ratings should be based upon at least similar ratee information yet measured using
different mediums. Assuming this measurement method captures true performance variance about the person being
rated, one would then expect that narratives would correlate with other constructs within the nomological network of
job performance. Such correlations are key to establishing the construct validity of narrative comments and determining the utility of this measurement method in practice.

2.1

Nomological network of performance narratives

A nomological network illustrates a construct's relation to other constructs and measures that are aligned within a similar theoretical space, providing the basis for construct validity (Cronbach & Meehl, 1955). Measures of the same latent
construct should converge, as should variables that are conceptually linked by theory. The domain of job performance
itself is broad, encompassing a wide range of work-related behaviors and outcomes (Borman, Bryant, & Dorio, 2010;
Gatewood, Field, & Barrick, 2016; Pulakos & O'Leary, 2010). It entails not only performance-related behaviors (e.g.,
task performance, organizational citizenship behaviors, counterproductive work behaviors), but also outcomes associated with those behaviors. Within this study, traditional job performance ratings, involuntary turnover, promotions,
and pay increases were examined in efforts to establish the construct validity of narrative sentiment scores. In this
context, a narrative sentiment score is a numerical value that represents the favorability of a performance comment,
algorithmically derived based upon the content of that comment (discussed further in Section 3).
Both narrative comments and traditional ratings are operationalized to reflect how well an employee performed,
and as such each are measures of the latent job performance domain. If such is the case, beyond narrative scores
demonstrating measurement reliability, they would also be expected to be positively correlated with traditional performance ratings. This includes not only same-year performance ratings but also future job performance ratings, as
we know performance ratings are fairly stable across time (Viswesvaran et al., 1996). Although the reasoning behind
performance stability is complicated, and there is a growing literature describing the conditions and factors in which
performance will be less stable (e.g., Sturman, Cheramie, & Cashen, 2005; Zyphur, Chaturvedi, & Arvey, 2008), a simplistic explanation is that relative performance consistency is due to stability of adult cognitive abilities and personality traits that are related to performance (e.g., Roberts & DelVecchio, 2000; Schmidt & Hunter, 2004), consistency in
situational constraints in the work environment, and cumulating advantage effects for high performers (e.g., Aguinis,
O'Boyle, Gonzalez-Mule, & Joo, 2016; Van Der Vegt, Bunderson, & Oosterhof, 2006). Given all the above:
Hypothesis 1: Narrative sentiment scores will be positively correlated with traditional numerical performance ratings made the same year.
Hypothesis 2: Narrative sentiment scores will be reliable, correlating positively from one year to the next.
Hypothesis 3: Narrative sentiment scores will correlate positively with next year's traditional numerical performance ratings.
Narrative sentiment should also be related to involuntary turnover. Turnover has long been tied to job performance, with a particularly strong theoretical and empirical link with involuntary turnover (Barrick, Mount, & Strauss,
1994; Bycio, Hackett, & Alvares, 1990; Stumpf & Dawley, 1981; Wells & Muchinsky, 1985). The relationship between
turnover and performance has been outlined in theoretical models such as the push–pull model (Becker & Cropanzano, 2011); the unified criterion space by Harrison, Newman, and Roth (2006); and Hom, Mitchell, Lee, & Griffeth's
(2012) expanded criterion model. Employees who do not meet performance expectations will be “pushed out” of organizations (Becker & Cropanzano, 2011), more likely to become reluctant leavers (Hom et al., 2012), and are generally
subject to various forms of withdrawal (Harrison et al., 2006). Narrative comments, therefore assuming they capture

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

303

SPEER

SPEER

performance-related variance, should predict turnover. Comments low in valence (e.g., declarations that employees
“need improvement”) should be indicators that an employee is not meeting job demands or is exhibiting low fit, and
therefore employees with negative comments will be more likely to be pushed out of the organization. Narrative comments may also be used to elaborately document poor performance for later justification to fire employees.
Hypothesis 4: Narrative sentiment scores will correlate negatively with future involuntary turnover.
It is well established that job performance information guides administrative decisions such as pay allocation and
promotions (e.g., Cascio & Aguinis, 2005). Pay decisions and promotions act as distal outcomes stemming from job
performance behaviors, such that employees who add more value and perform better for an organization are rewarded
(Ng, Eby, Sorensen, & Feldman, 2005). Because they perform better, assumed to be due to superior human capital in
the form of increased knowledge, skills, abilities, experiences, and other favorable characteristics (e.g., Crook, Todd,
Combs, Woehr, & Ketchen, 2011; Kim & Ployhart, 2014), companies operating in a free-market economy will try to
retain top performers using rewards such as higher pay and promotions (Ng et al., 2005). On the other hand, there
is little incentive for organizations to give generous pay or promotions to underperforming individuals. As such, job
performance will be related to pay change and promotion likelihood.
Narrative comments are expected to overlap with traditional ratings and be reflective of job performance (Brutus,
2010). Under the logic that job performance will precede pay and promotions, narrative scores should therefore correlate with future pay changes and promotions. Building on this, narrative comments reflect information regarding a
ratee's individual characteristics and job-related behavior (Smither & Walker, 2004), which represent valued human
capital. Comments also contain suggestions for improvement (Brutus, 2010), which might initiate behavioral changes
that increase the likelihood of favorable career outcomes. Collectively, assuming that narrative scores capture true
performance-related variance, better performing employees should be more likely to receive higher future pay and be
more likely to receive future promotions.
Hypothesis 5: Narrative sentiment scores will correlate positively with future promotions.
Hypothesis 6: Narrative sentiment scores will correlate positively with future pay increases.
Although narrative comments and traditional ratings should each reflect the latent performance domain, there are
also differences in how each evaluation is made. The next section explores why performance narratives provide valid
but also different information about employee performance beyond traditional numerical ratings. In doing this, I want
to be clear that in no way am I reproachful of traditional numerical ratings, as traditional numerical ratings offer standardized and deliberate methods of measuring employee performance. Instead, I seek only to highlight the unique
aspects of utilizing narrative comments in the evaluation context. I believe that each can be integral parts of effective
performance management and when combined may result in an improved understanding of employee behavior.

2.2

Additional measurement benefits of performance narratives

Despite the obvious intricacies of narrative comments, there have only been a handful of studies that have systematically examined performance narratives (Christianson DeMay et al., 2006; David, 2013; Smither & Walker, 2004;
Wilson, 2010), and none have directly examined narratives with a focus on understanding the validity of this measurement method within a traditional PA system. I propose two primary reasons why narrative comments, when combined with traditional numerical ratings, can increase the quality of total performance measurement. Specifically, inclusion of narrative comments will result in (a) increases in total information and reliability, which is expected to occur
across appraisal settings. In addition, in contexts where narratives are not explicitly linked to distributive outcomes
(e.g., pay), narratives are likely to (b) exhibit a reduced amount of variance attributable to rater bias. These effects,
in turn, are assumed to impact the cognitive processes and information underlying the final performance evaluations
and result in unique, performance-related variance captured by narratives. Below each of these factors are elaborated
upon.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

304

2.2.1

Increases in total information

Numerical ratings and narrative comments are two mediums, with each containing similar but separate types of information. Narratives are likely to bolster the total amount of information measured with the appraisal in two ways: (1) by
enhancing reliability of the construct space already captured by the traditional ratings and (2) measuring performancerelated variance not already captured by traditional numerical ratings (i.e., increasing bandwidth).1 To the first of
these points, narrative comments contain information just like any other assessment, and some of this information will
converge with traditional numerical ratings, as raters often use the comments to justify their rating decisions (Brutus, 2010; David, 2013). Indeed, research has displayed convergence between the two data sources (David, 2013;
Smither & Walker, 2004). In such a case, the combination of both numerical ratings and narrative sentiment can serve
to increase measurement reliability, similar to how having more items in a self-report survey increases internal consistency (assuming narrative data can be reliably scored).
At the same time, narrative comments allow for the provision of additional construct-relevant information not
captured by traditional numerical ratings, thus also increasing the bandwidth of measurement. Given the free-form
nature of narratives, raters can elaborate more upon competencies, upon completion of goals, and how the behavior of
the employee impacted others (Kabins, 2016). This might be particularly salient if traditional performance scales are
overly broad, such as if managers only produce a single overall rating. In this case, the comment box allows for rich,
competency-related feedback, providing details the broader ratings cannot. Furthermore, if raters are using the comment box as an opportunity to not only comment on performance but also to provide development tips, this will cover
a broader spectrum of behavioral variance.
In addition, part of the reason why comments should enhance measurement bandwidth is because they offer contextual information regarding job-related behaviors. It is well established that behavior is a function of situational
demands and individual characteristics (e.g., Funder, 2006; Lewin, 1936). Traditional numerical ratings, with the possible exception of very nuanced and narrow behavioral competencies, describe people in general behavioral or competency terms without clear understanding of the contextual factors that may have impacted ratings. Although raters
may implicitly consider both situational and individual factors when forming a rating, separating the two sources of
variance is impossible by glancing at most simple numerical scores. On the other hand, a great benefit of narratives is
that they add rich context to ratings (Brutus, 2010; David, 2013), which is important because job performance is construed within specific work situations (Judge & Ferris, 1993). For instance, one could discern that a person received an
average score on customer service because they only met basic expectations, when in reality, they received an average
score because they performed well with most customers but struggled to console customers who were upset when
returning products. Narrative text allows understanding this contextual nuance. Of course, across formats and across
raters, specific narrative comments will differ in these respects. Generally though, and taken together, narrative comments are expected to increase the reliability of performance measurement and also the bandwidth of performancerelated variance.

2.2.2

Reduction in variance attributable to rater-motivation bias

Performance ratings are prone to numerous rating biases (Harris, 1994; Landy & Farr, 1980; Levy & Williams, 2004). Of
particular concern to this section are not biases pertaining to a judge's ability to accurately rate employees but rather
motivational factors that distort ratings when made (e.g., Spence & Keeping, 2011). Within organizational settings,
there are a number of variables that may motivate raters to distort ratings, and raters seek to avoid negative consequences and maximize rewards when making ratings, according to Harris's model of rater motivation. For instance,
a rater may want to avoid damaging the subordinate–manager relationship (avoid negative consequences) and, as a
result, give more lenient performance scores (Harris, 1994). These motivations help explain why ratings made in administrative settings, where ratings are more likely to affect employment decisions (e.g., promotions, pay), tend to be positively biased (e.g., DeNisi et al., 1984; Harris, 1994; Wherry & Bartlett, 1982). In this context, low ratings will result
in fewer distributive rewards, whereas high ratings will result in more rewards, causing potential aversive social outcomes (e.g., hostility) or favorable social outcomes (e.g., appreciation) with subordinates as a function of how lenient a

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

305

SPEER

SPEER

rater is. In line with this, Jawahar and Williams (1997) found that performance ratings made in administrative settings
produce inflated mean scores due to rater leniency.
So, performance appraisals are likely to be distorted due to contextual influences on rater motivation, especially
when they are tied to administrative decisions. Regarding performance narratives specifically, it is pertinent to note
that motivation to distort will also likely exist. For example, just as a lower traditional rating could lead to an unpleasant
confrontation with a subordinate, negative comments could also spur unpleasant interactions that promote avoidance
motivations (Wang, Wong, & Kwong, 2010; Wong & Kwong, 2007). However, whereas this may occur for both mediums
in likely equal probability, traditional narrative ratings are substantially more likely to be explicitly tied to distributive
outcomes than narrative comments are, and therefore more likely to be affected by leniency bias. The structured and
numeric format of traditional ratings makes them well-suited for making administrative decisions, whereas the freeform structure of narratives results in just the opposite (Brutus, 2010). In the case where traditional ratings are tied
to distributive outcomes but narrative comments are not,2 narrative comments will therefore be less affected by rater
motivated biases, which will improve measurement at the integration and evaluation phases of performance ratings.

2.2.3

Implications

The theory outlined thus far discusses not only why traditional ratings and narrative scores will converge but also why
narrative comments will explain incremental variance in performance outcomes above and beyond traditional ratings.
When combined with traditional ratings, narrative scores will increase total measurement information, broadening the
breadth of what is measured while simultaneously enhancing reliability due to increased amount of data. In addition,
in contexts in which narrative comments are not explicitly tied to administrative decisions but traditional ratings are,
narratives should contain less variance attributable to rater-motivated bias, therefore further enhancing the unique
value of this data source. Taken together, narrative scores should explain meaningful unique variance in prediction of
variables in the nomological network of job performance, above and beyond traditional numerical ratings.

Hypothesis 7: Narrative sentiment scores will explain unique variance in the prediction of future performancerelated outcomes (involuntary turnover, promotions, pay increases, and future traditional performance ratings) above and beyond traditional numerical performance ratings.

Finally, although we can expect increases in total performance information by using narrative comments, a logical
question becomes when this might be most informative. Given the prediction of incremental variance overall, narrative scores are expected to display meaningful variability within each level of the numerical distribution of traditional
ratings. Although this is equivalent to demonstrating unique variance (i.e., controlling for level of numerical rating), it
is also informative to narrow the focus specifically toward the parts of the numerical distribution where the largest
proportion of employees are rated. Within this study's setting, the majority of employees were rated into the midpoint
of the numerical performance scale. Only employees who were rated at or above this mark received annual bonuses,
and thus there was motivation for managers to inflate employee ratings, so subordinates received those bonuses even
if those employees truly were below average. In addition, with a limited pool of money to give raises, some managers
may have “suppressed” ratings more toward the middle for employees who truly deserved higher marks. Within that
middle scale point, for which there is no numerical rating variance, one is likely to still find a great deal of variability
in comment valence—some fairly neutral, some fairly favorable, and some more negative. Per the outlined theoretical
principles, in contexts where traditional ratings are more directly tied to distributive outcomes than narrative comments, it is then expected that narratives will be less susceptible to rating bias. Assuming the most bias exists at this
point in the rating scale and narrative comments are less susceptible to rater bias in the aforementioned context, the
following hypotheses are proposed:

Hypothesis 8: Narrative sentiment scores will display more variability at the midpoint of the traditional numerical
performance scale than at other parts of the distribution.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

306

Hypothesis 9: Narrative sentiment scores will be more strongly correlated with next-year performance ratings
when drawn from the midpoint of the traditional numerical performance scale than from other parts
of the distribution.
Several studies have examined the properties of narrative performance comments or comments from similar
domains (Christianson DeMay et al., 2006; David, 2013; Hedricks et al., 2017; Rupayana et al., 2017; Smither & Walker,
2004; Wilson, 2010), although none have explicitly tested their utility in providing unique information over and above
traditional numerical ratings. Furthermore, most investigations of narrative comments have leveraged manual, human
coding. This process is laborious and could potentially be improved by utilizing newer analytical methods of text mining
(e.g., Ignatow & Mihalcea, 2017; Liu, 2012; Pang & Lee, 2008). Thus, in this study, I explore whether narrative comments
can be automatically coded and whether the derived scores explain true score variance from the latent performance
domain. This was performed using refined analytical methods and by creating a localized performance dictionary within
a single organization. The next section reviews the process of text mining and how this can be applied to performance
data.

3

TEXT MINING IN A JOB PERFORMANCE CONTEXT

In organizational settings, qualitative text analysis has historically involved taking two or more experts (e.g., industrial
and organizational psychologists), have them review qualitative texts, and then rate or classify those texts according to some coding scheme. This process is quite time consuming and difficult to perform, and yet one that can
uncover important information. Given the challenges in manual, human coding and the number of text documents
that need to be coded to answer certain questions, automated forms of qualitative data analysis have increased
in use.
Natural language processing is a field of linguistic science that seeks to understand how computers can comprehend
and mimic human language (Landers, 2017; Manning & Schütze, 1999); this includes a series of methods to classify,
mine, and predict information from text data, otherwise known as text mining or text analytics. Text mining analyses
range from fully supervised (i.e., keyed upon some criterion, such as expert ratings) to fully unsupervised approaches
(Pang & Lee, 2008) and are used for a range of analytical tasks, including topical categorization, thematic analysis, sentiment analysis, author attribution, and personality measurement, among many others (e.g., Grimmer & Stewart, 2013;
Ignatow & Mihalcea, 2017; Kobayashi et al., 2017a, 2017b; Liu, 2012; Mairesse, Walker, Mehl, & Moore, 2007; Medhat, Hassan, & Korashy, 2014; Schwartz et al., 2013; Stamatatos, 2009). Text mining has increasingly been applied to the
social sciences (e.g., Ignatow & Mihalcea, 2017; McAbee, Landis, & Burke, 2017), although within this domain, the practice is still in its infancy. Applications have scored essays for college admissions (Attali, Lewis, & Steier, 2013), mined
text to derive personality scores and emotional states (Mairesse et al., 2007; Pang & Lee, 2008; Pennebaker & King,
1999), mined application blanks (Campion et al., 2016), predicted team processes and outcomes (Olenick et al., 2017),
derived estimates of company culture (Pandey & Pandey, 2017), and scored comments from applicant references to
predict job outcomes (Hedricks et al., 2017; Rupayana et al., 2017). In general, though, text mining has not thoroughly
infiltrated the organizational sciences.
The crux of text mining is the task of breaking text into smaller components. For instance, the commonly used
“bag of words” approach splits text into vectors of words or word phrases. This ignores portions of semantic information, such as grammar, word location, parts of speech, and so forth, instead focusing solely on the presence of
words or word phrases (e.g., “needs improvement”). Under this approach, analysis first requires processing text data
so the linguistic units can be analyzed. This involves applying algorithms to lower case words, removing punctuation, stemming or lemmatizing by translating words to their roots (e.g., “play,” “played,” and “playing” all become
“play,” which reduces complexity of the features), fixing spelling, and so forth. Then, a dataset is generated where
the cleaned text data are tokenized to a format that can be read by computers, where single text units are treated
as vectors. The vectors can represent single words such as “White” and “House” or word phrases (i.e., n-grams) such
as “White House,” which is qualitatively different from those two separate words. Note that the use of n-grams

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

307

SPEER

SPEER

in this way serves as a proxy of semantic representation of the original text when using bag of words (Grimmer
& Stewart, 2013). Finally, once all that is performed, the researcher conducts analyses to derive insights from the
data.
Supervised sentiment analysis was used within this study, which involves the computational treatment of opinion,
sentiment, and subjectivity in text (Ignatow & Mihalcea, 2017; Medhat et al., 2014; Pang & Lee, 2008; Wilson, Wiebe,
& Hwa, 2006). Sentiment analysis determines the valence or intensity of a text according to some defined construct or
criterion (e.g., how positive a review was) by applying classification or regression methods (Ignatow & Mihalcea, 2017;
Medhat et al., 2014; Pang & Lee, 2008; Wilson et al., 2006). Although historically this work has dealt with attitudes, its
application of machine learning principles allows one to key text to identify levels of many construct types (Pang & Lee,
2008) and, in the case of this paper, performance valence.
Sentiment analysis works by defining dictionaries that contain words and linguistic information indicative of a given
sentiment. For instance, if the words “eager,” “talks,” and “ecstatic” were defined in a dictionary to measure the construct of happiness, higher usage of these words would then indicate a text sentiment of happiness. Here, it is common
to use a priori dictionaries that define the construct or constructs of interest. These off-the-shelf dictionaries are relatively easy to obtain and require no data from the user to create. For instance, Linguistic Inquiry and Word Count
(LIWC, Tausczik & Pennebaker, 2010) is a commercially available set of dictionaries widely used by researchers, and
there are a number of free dictionaries available online as well (e.g., Grimmer & Stewart, 2013; Miller, 1995; Strapparava & Valitutti, 2004).
Although predefined dictionaries have their benefits, sentiment and what defines it are strongly influenced by the
domain in question (Liu, 2012; Pang & Lee, 2008). The type of language changes from situation to situation and over
time, and as such dictionaries may not generalize well to new contexts (Grimmer & Stewart, 2013; Liu, 2012). An alternative is to use supervised learning approaches to build localized dictionaries. This process leverages a training set
of data to build custom dictionaries and algorithms to predict an outcome of interest and then applies that to local
settings. For instance, in a study of Facebook posts, this sort of approach was found to outperform preestablished dictionaries (Schwartz et al., 2013). This is because the language used to define what words equate to positive or negative
sentiment are customized specifically to the context at hand.
Within the context of performance appraisals, a supervised learning approach can be performed by training narrative data to reproduce numerical performance ratings. In this case, the sentiment is the positivity of performance ratings. Performance narratives as a data source are quite ideal for text mining, as narratives are naturally accompanied by
numerical ratings needed for supervised learning (therefore forgoing additional need for judges to rate the sentiment
of comments), and they are less likely to contain sarcastic text, idioms, and hidden meanings, which can be difficult
for text analytics programs to accurately decipher (Ignatow & Mihalcea, 2017; Tausczik & Pennebaker, 2010). This last
point is a particularly important one. Text mining is difficult because text contains ambiguities and subtle meanings
that are difficult for computers to decipher (Kobayashi et al., 2017a, 2017b; Pang & Lee, 2008). However, performance
comments are written formally and are devoid of ambiguous language, and the topic is predetermined. This makes for
units of text that have clear-cut meaning and therefore are less ridden by error when keyed to an outcome.
Only a handful of studies have attempted text mining in performance-related contexts. In the only known efforts
to text mine actual performance data, Christianson DeMay et al. (2006) took 570 direct report comments and investigated the viability of gleaning topic themes. They compared text-mined themes to the topic themes derived using
manual, human coding. However, traditional statistics were not reported, a holdout sample was not used so to avoid
overfitting, and the derived scores were not correlated with performance outcomes to establish validity and utility
for the approach. In other efforts, both Hedricks et al. (2017) and Rupayana et al. (2017) created local text dictionaries using references made on the behalf of job applicants applying to various positions. Although this is not exactly
a performance-based context, it does involve others providing qualitative data about a person's work behaviors. The
Hedricks et al. study found narrative content did in fact correlate with numerical ratings from the same references, and
the Rupayana et al. study revealed that comment types were different when provided by supervisors or coworkers.
Although these three studies highlight the potential for performance narrative text mining, they did not fully address
this topic head on, which this study sought to do.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

308

4

METHODS

4.1

Participants

Archival performance data from a large U.S. financial services organization were used in the present study. For this
study, annual performance appraisals completed at the end of each calendar year were used, which were completed by
employees’ direct supervisors. All full-time individual contributors (i.e., nonmanagers) were included within this study,
and thus the jobs included were varied. A total of 5 years of performance data were utilized (2011–2015), although
to ensure employees had adequate time to ramp up to job responsibilities, only ratings where employees had been on
the job for at least 6 months were included. A total of 5,955 individual contributor ratings that met this guideline were
completed in 2011, 5,143 in 2012, 5,300 in 2013, 5,076 in 2014, and 5,286 in 2015. Note, however, that these sample
sizes were further reduced based on decision rules regarding comment length (see Section 4.3).
Data were then split to calibrate the model to score narrative text comments and then to test that model on an
independent holdout sample. Performance data from 2011, 2012, and 2013 were used as the calibration sample to
develop the model. This large sample helps meet the intensive requirements needed for the text mining calibration, and
the derived model was then used to score narrative comments from 2014 and 2015, treating these years as completely
independent sets of data. Data from 2014 to 2015 were used to test all study hypotheses, including investigations of
narrative score reliability and convergence with variables within the nomological network of job performance.

4.2

Measures

4.2.1

Annual performance ratings

As part of the organization's performance management process, all employees were rated by their immediate supervisor at the end of each calendar year. These traditional numerical ratings influenced a variety of administrative decisions
within the organization, including pay and promotions, and they were leveraged to conduct one-on-one development
sessions with subordinates following the ratings. Ratings were made using an online platform and included traditional
numerical ratings of job-specific competencies, goal expectations (i.e., goal attainment), and an overall performance
rating, which raters were instructed to base on the aforementioned ratings. These were accompanied by free-form
comment boxes that were voluntary for raters to complete.
All employees in the organization were rated using this system, although the competencies and expectations varied
considerably by job and by persons within jobs (i.e., managers and employees agreed upon the behaviors on which they
were to be evaluated upon each year). Because of this inconsistency, this study focused solely on the overall performance rating, which was made using a 7-point scale (ranging from 1 = “unacceptable” to 7 = “exceptional”). Although
performance is a multidimensional construct (Cascio & Aguinis, 2005), research supports the existence of a general
performance factor (e.g., Viswesvaran, Schmidt, & Ones, 2005), and as such this operationalization is appropriate given
the context. In line with this operationalization and with this study's bag-of-words treatment of text, narrative comments for each year were aggregated into single text files for each employee. This ensured that each employee had
a large amount of text data and parallels the comparison with overall performance ratings. The data were fed into all
text-based analyses.
Annual performance ratings for 2014 and 2015 formed the holdout, hypothesis-testing sample. Like the data from
the calibration sample (years 2011, 2012, and 2013), the overall performance rating (1–7) was used for each year. Average ratings were 4.95 (SD = .92) for 2014 and 4.86 (SD = 1.02) for 2015. 3.1% of the cases fell below the midpoint of
the scale, 32.9% fell at the midpoint (4), and 64.0% fell above 4 in 2014 (7.0%, 32.0%, and 61.0% for 2015).

4.2.2

Convergent performance measures

Beyond traditional performance ratings from the holdout sample (2014–2015), narrative sentiment scores were examined along with several other variables within the nomological net of job performance. Specifically, narrative sentiment
scores were also correlated with employee turnover, employee promotions, and yearly pay increases.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

309

SPEER

SPEER

Turnover
Involuntary terminations (i.e., employees who leave the company because employer chose to discharge employee from
company, and departure does not constitute as occurring due to retirement reasons) were examined for the duration
of the study period, ranging from when the 2014 performance ratings were made (just following the end of the 2014
calendar year) to 1 year after the final set of performance ratings in 2015 (so to the end of 2016). Thus, turnover data
were examined across a 2-year window. Turnover was coded dichotomously such that 1 = involuntarily termed. Of the
employees with either a 2014 or 2015 performance rating, 3.4% involuntarily terminated during the study period.

Promotions
A variable that indicated whether employees were promoted into a managerial role was included, spanning the duration of the study period. Like the turnover measure, this variable covered a 2-year window from when the 2014 performance rating was made and up until 1-year following the final rating of 2015. Promotions were coded such that
0 = not promoted and 1 = promoted. Over that period, 2.3% of employees were promoted from nonmanager positions
to managerial positions.

Pay increases
Percent pay increases from year-to-year were also included, once again spanning the duration of the study period. This
measure was operationalized as the percent increase in pay from 2014 to the end of 2015, and only included individuals
employed during that full span of time. Examination of this variable revealed strong positive skew and kurtosis, and so a
transformed version was created by square-rooting the original variable, resulting in adequate skew (.73) and kurtosis
(1.65). Both variables are presented for the results.

4.3

Text processing

4.3.1

Data overview

Examination of the narrative comments3 made by employees’ direct supervisors from 2011 to 2013 revealed that comments varied substantially in length. The average number of words per review was 831.8 (median = 635.5). Given the
large calibration and holdout samples, cases with extreme word counts were removed. All reviews with less than 150
words (∼5th percentile) or more than 2,500 words (∼97.5th percentile) were removed. This ensured that text documents contained enough text to achieve adequate estimates of sentiment. Upon removing cases with extreme word
counts, the data were then split into the calibration dataset (2011, 2012, and 2013) and the holdout dataset (2014
and 2015). The final analysis sample sizes for each set were 15,155 ratings for the calibration dataset (2011 = 5,474,
2012 = 4,761, 2013 = 4,920) and 9,536 ratings for the holdout dataset (2014 = 4,677, 2015 = 4,859).
Additional inspection also revealed that the number of words was positively associated with performance ratings
(r = .12, p < .01), and as such this term was included in all regression-based models examined within this study. A look
at a quadratic total words variable revealed that it explained minimal additional variance beyond the linear total words
variable and thus was not incorporated.

4.3.2

Preprocessing narrative comments

The first step of text mining involves breaking down text data into component parts that are manageable for statistical
programs, otherwise known as preprocessing. This is an iterative process and the approach varies by context. Here, the
raw text was converted to a preprocessed corpus using a bag-of-words approach, with all analyses being conducted in
R (R Core Development Team, 2007).
First, all text was lower cased, numbers were removed, and unexpected white space was stripped. Then, negation
was taken into account. Within a line of text, negation involves words that flip the polarity of the subsequent word (e.g.,
“not,” “never”). To deal with this, words that followed a negation term were appended with a prefix of “not_.” As an example, the phrase “He is not dependable” would become the series of words “he,” “is,” and “not_dependable.” Following

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

310

this, all punctuation was stripped4 and common English stop-words were removed (e.g., “the,” “a”). This helps eliminate
information that is unlikely to be informative when modeling, given the frequency and lack of meaning often associated with these words. Finally, words were “stemmed” by translating them to their root forms (e.g., “play,” “played,” and
“playing” all became “play”).

4.3.3

Formation of document term matrices

Upon cleaning the raw text, the newly created corpus was transformed into a document term matrix, where each row
represents a document and each column vector represents units of text. Column vectors included unigrams (i.e., all
single words), bigrams (i.e., all two-word combinations), and trigrams (i.e., all three-word combinations). Inclusion of
bigrams and trigrams helps capture, to a degree, the syntax and context of text that single words sometimes cannot
pick up (e.g., “subject matter expert”).5
The resulting column vector values can be represented several ways, such as treating the vectors as frequency
counts of a word within a document, simple binary indicators (0, 1) of whether a word occurred within a document, or as was performed here, by applying a term frequency-inverse document frequency (TF-IDF) correction to
each vector (Kobayashi et al., 2017b; Manning & Schütze, 1999; Paltoglou & Thelwall, 2010). This correction gives
more weight to terms that are infrequently found within the corpus and occurring often within the document being
scored and less weight to terms that are frequently found across many documents (and as such are less likely to be
informative).
The resulting document term matrix and its features were then reduced in two ways. First, any terms found in less
than 1% of the documents were removed (i.e., removing sparse terms), similar to the approach taken by Schwartz et al.
(2013) and recommended by Kobayashi et al. (2017a). Second, the number of vectors was further reduced by only
including terms that correlated significantly with job performance (i.e., univariate feature selection) using a conservative value of p < .001. This resulted in a final set of 833 column vectors. Although this number of variables is high
compared to most studies in the organizational sciences, it is perfectly reasonable within the text mining context (for
instance, Park et al., 2014 used 5,106 features) where the goal is to maximize prediction in a separate holdout sample and machine learning algorithms apply coefficient penalizing functions (e.g., Kuhn & Johnson, 2013; Putka, Beatty,
& Reeder, 2017) that maximize prediction in holdout samples by avoiding capitalization on chance due to the large
number of predictor variables. Further, the number of predictor variables to calibration sample size was a healthy 18.2
(15,155/833) n/k ratio.

4.4

Sentiment analysis

4.4.1

Ordinal narrative scores

Two separate models were developed using same-year performance ratings as the criteria, and each applied machine
learning principles to maximize prediction in new samples. The first model is treated as the primary and used to test
study hypotheses, and the second used to illustrate opportunities for prediction improvement depending on the prediction purpose (see Section 4.4.2). The first model was an elastic net linear regression model (Kuhn & Johnson, 2013;
Zou & Hastie, 2005), which produces a linear combination of regression weights fit to minimize model bias and variance in new samples. A regression model is well suited to predict sentiment of text documents (Pang & Lee, 2008), and
elastic net applies regression but with regularization and variable selection controls so to enhance prediction in new
samples. It combines ridge regression (Hoerl & Kennard, 1970; Zou & Hastie, 2005) with least absolute shrinkage and
selection operator regression (LASSO, Tibshirani, 1996). As such, it exhibits the benefits of multicollinearity correction
seen with ridge regression and the variable selection functioning of LASSO. The model was fit using the “glmnet” and
“caret” packages in R (Kuhn, 2014; Kuhn & Johnson, 2013), applying a three-repeated 10-fold cross-validation using
the full calibration sample (see Kuhn & Johnson, 2013, or Putka et al., 2017 for an overview of this approach). The
multiple cross-validations are used to determine optimal tuning parameters (whether the model is more a mix of ridge
regression or LASSO and the degree of regularization, each based upon minimizing error in the 30 cross-validations).

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

311

SPEER

SPEER

F I G U R E 1 Positive and negative word clouds of most discriminating word grams
Note: The graph on the left displays the 50 word phrases most associated with high performance, and the graph on
the right shows the 50 word phrases most associated with low performance. Scaling is based upon the correlation
between binary word variables and job performance ratings such that larger words are more strongly associated with
performance.

These tuning parameters are then used to fit the final model within the calibration sample, which can then be applied
in new contexts. The derived model output is labeled the ordinal narrative score within this study, as it keyed upon ordinal performance ratings. Once formed, the model can be applied to new samples, which for this study was the holdout
sample of 2014 and 2015 performance ratings. Further details on the contents of this model can be seen in Figure 1 of
Section 5.

4.4.2

Logistic narrative scores

The first model was fit using the ordinal performance ratings as the outcome. This was done because traditional ratings provide the most reliable and comprehensive criterion available. However, traditional numerical ratings can suffer
from measurement issues, and keying upon the ordinal ratings is fairly redundant, even if in a completely separate calibration sample (given the hypothesis that narrative comments will explain unique variance beyond traditional numerical ratings in predicting other performance-related outcomes). Another approach is to focus on extreme performance
scores (very low or very high, i.e., polarity classification, Pang & Lee, 2008), assuming that the narratives matched to
those ratings are best suited for identifying true sentiment of the comments. This aligns with the notion that administrative ratings may suffer from bias within the middle of the distribution, and as such narratives matched to moderate
numerical ratings may be less informative and contain more error when deriving a model. In a sense, this is analogous to
writing test items with extreme difficulty values that target specific segments of the latent trait or population. However,
instead of test items, the algorithms were explicitly trained to distinguish job performance at extreme levels where certain performance outcomes might be more likely to occur (e.g., turnover occurring with very poor performers). Based
on these principles, two separate logistic narrative scores were formed using logistic regression in the prediction of
artificially dichotomized performance ratings, via elastic net: a negative logistic narrative score and a positive logistic narrative score.
The positive and negative logistic narrative scores were also formed using elastic net regression, though using a
binomial distribution to produce logistic regression estimates (Kuhn & Johnson, 2013). The positive logistic narrative
model dichotomized ratings as 1 = ratings of “well above target” and “exceptional” from the 7-point distribution and 0
for all other ratings, resulting in 32.66% positive ratings. The negative logistic narrative model dichotomized ratings as
1 = ratings of “unacceptable”, “inconsistent” and “somewhat expected performance” from the 7-point distribution and

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

312

0 for all other ratings, resulting in 4.06% negative ratings. Once again, model tuning parameters were derived using a
k-folds approach, although here a 10-repeated threefold approach was used (as opposed to three-repeated 10-fold)
because of a low base rate of negative ratings.

5

RESULTS

5.1

Formation of narrative algorithms

The ordinal narrative scores and logistic narrative scores (both positive and negative) were formed within the calibration sample (years 2011, 2012, and 2013) using elastic net regression. Across the 30 replications of model fitting within the calibration sample, the mean cross-validated multiple R in predicting traditional performance ratings
was .64 (RMSE = .72) for the ordinal narrative score.6 Because the logistic narrative scores were fit to predict that
dichotomized ratings, accuracy, and kappa statics were examined. Across the 30 replications of model fitting the mean
cross-validated accuracy in predicting whether an employee was a low-performer was 96.4% (kappa = .41) for the negative logistic narrative score, and it was 76.6% (kappa = .42) for the positive logistic narrative score in identifying high
performers. Overall, the derived narrative scores were correlated with the traditional numerical ratings for the years
in which the model was fit.
To help understand the types of word phrases associated with high and low performance, word clouds were constructed that plot the top 50 positive word phrases and the top 50 negative word phrases, based upon the strongest
positive and negative correlations with performance ratings (out of 833 total phrases). Figure 1 displays these results.
Not surprisingly, many of the positive phrases include adjectives and adverbs such as “extremely,” “always,” “great,”
and “exceptional.” Those with higher ratings were also described as being “leaders,” and references were made to
“projects” with use of verbs such as “excels” and “manages.” On the other hand, those with lower ratings were frequently described as needing improvement or showing improvement. Words such as “inconsistent,” “struggles,” and
the conjunction “however” were indicators that an employee was performing poorly. In addition, note that many of
the most predictive terms were bigrams (“work with,” “not only,” “struggles with,” “needs improvement,” and “however
there”) or trigrams (“go to person,” “does great job,” “should have been,” and “will need continued”), and particularly
for the negatively valanced terms. This speaks to the importance of including phrases beyond just unigrams within the
model.

5.2

Do narrative sentiment scores correlate with performance outcomes?

With the models formed and a general understanding of what words are indicative of valence, the focus now turns to
applying estimations to the holdout sample (years 2014 and 2015) to test study hypotheses. Table 1 displays descriptive statistics and correlations among the primary study variables. Of immediate interest is whether the narrative comments correlate with same-year ratings. As seen, same-year numerical ratings and ordinal narrative scores correlated
on average .64 (2014 = .63, p < .01, 2015 = .65, p < .01). Because there was a correlation between performance and
word count, correlations were also calculated with word count partialled out, and the average correlation was .63.
Overall, the derived algorithm resulted in scores that overlap substantially with numerical ratings. This finding is particularly impressive given narrative scores did not require any work from coders but are automatically computed using
the derived algorithm. As a comparison, David's (2013) manual coding of comment favorability of manager narratives
correlated only .26 with same-year ratings. The observed correlation from this study is also considered to be large
according to conventional standards of effect size magnitude (Bosco, Aguinis, Singh, Field, & Pierce, 2015). Hypothesis
1 was fully supported.
Second, ordinal narrative scores were consistent from year to year, correlating .58 (p < .01) from 2014 to 2015
(r = .58 after controlling for word count). Research suggests that the rank order of employee performance is fairly
stable over time (Viswesvaran et al., 1996), and thus it is encouraging to find the same with narrative descriptions of
employees, supporting Hypothesis 2. In comparison, the traditional numerical ratings correlated .61 (p < .01) across

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

313

SPEER

4.86

.03

.02

.08

.26

13. 2015 Numerical rating

14. Involuntary turnover

15. Promotion

16. Pay change

17. Pay change (sqrt)

.11

.07

.15

.18

1.02

.92

3.9

10.5

.48

473.3

.23

.14

.60

513.0

.23

.11

.57

SD

.56

.28

.22

.10

.11
.21
.25

−.24

.25
−.04

.47
−.12

−.29

.49
−.18
−.15

.06
.61

.63

.06

−.01

.12
.14

−.01
−.07

.56
.10

−.39

.15

.11

.08

−.03

.35
−.24

.55
−.26

−.33

.58

.10

−.33

3.

.10

−.33

2.

−.04

.92

−.57

1.

.07

.06

.05

−.05

.07

.13

−.03

.04

.21

.64

.10

−.06

.09

4.

.27

.20

.08

−.15

.65

.49

.03

.10

.05

.07

.91

−.61

5.

−.25

−.17

−.03

.19

−.48

−.30

−.01

−.05

.05

−.04

−.36

6.

.23

.18

.08

−.10

.59

.47

.02

.08

.07

.08

7.

.05

.04

−.01

−.02

.08

.08

−.05

.05

.19

8.

−.04

−.03

.09

−.04

−.02

.08

−.14

.04

9.

−.24

−.24

−.07

−.13

.06

.11

.45

10.

−.17

−.20

−.07

−.05

.05

.08

11.

.38

.29

.12

−.18

.61

12.

.35

.25

.10

−.16

13.

−.17

−.11

−.02

14.

.17

.17

15.

.95

16.

17.

SPEER

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Note. Data from holdout sample of 2014–2015. There were 4,677 performance ratings for 2014 and 4,859 for 2015. All correlations equal to or greater than .03 are significant at the .05 level
(two-tailed). Exempt status, organizational tenure, and job tenure represent values from 2014.

4.2

4.95

12. 2014 Numerical rating

10. Org tenure

11. Job tenure

.63

13.1

9. Exempt status

.34

728.9

.05

6. 2015 Negative logistic score

8. 2015 Word count

4.91

5. 2015 Ordinal narrative score

7. 2015 Positive logistic score

.34

785.6

.04

2. 2014 Negative logistic score

4. 2014 Word count

4.92

1. 2014 Ordinal narrative score

3. 2014 Positive logistic score

Mn

Descriptive statistics and correlations

Variable

TA B L E 1

314

years. It is interesting to note that if performance composites are formed for each year by equally weighting the numerical rating and the narrative score, the year to year consistency between years increases to .67 (r = .66 after controlling
for word count). Thus, from a temporal consistency standpoint, the inclusion of both forms of data appears to increase
the reliability of measurement.
Hypotheses 3–6 tested whether narrative performance scores were significantly related to future performancerelated outcomes. First, ordinal narrative scores exhibited a strong correlation with next year's numerical performance
ratings (r = .49, p < .01), with identical results after controlling for word count. Given the convergence between narrative scores and traditional numerical ratings within years, this is expected, as each capture the latent performance
space (Hypothesis 3 supported).
Ordinal narrative scores also correlated −.18 (p < .01) with involuntary turnover (Hypothesis 4, r = −.18 after controlling for word count). Further exploring this outcome, the negative logistic narrative score was keyed to predict poor
performance, and scores from this measure correlated .25 (p < .01) with involuntary turnover. In comparison, the correlation between traditional numerical ratings and involuntary turnover was −.18. The positive logistic narrative score,
which was keyed to focus on the upper end of the performance distribution, exhibited a weaker though still significant
relationship with involuntary turnover (−.12, p < .01). These values are similar to those found in past research examining the relationship between numerical performance ratings and turnover (Griffeth, Hom, & Gaertner, 2000), though
slightly lower than past performance relationships with involuntary turnover (Bycio et al., 1990). The effect sizes can
be considered moderate according to conventional effect size benchmarks, which includes correlation distributions for
turnover-type variables (Bosco et al., 2015).
The ordinal narrative scores correlated .10 (p < .01) with promotions (Hypothesis 5, r = .10 after controlling for
word count). Although the positive logistic narrative score was keyed upon the upper end of the performance distribution and therefore where promotions are most likely to occur from, prediction was just marginally higher (.11, p < .01).
Although these correlations are not especially large, they are line with typical effect sizes when predicting promotions (Ng et al., 2005) and were expected to be lower in this study given the low variance for this dichotomous outcome. Finally, ordinal narrative scores correlated .22 (p < .01) with pay increases (r = .28 for the squared pay variable,
Hypothesis 6) and .22 after controlling for word count. All told, automatically derived narrative scores were related to
future performance outcomes in expected ways, providing additional construct validity evidence for narrative scores
as a measure of job performance.

5.3

Do narrative sentiment scores explain unique variance in future outcomes?

Although the narrative scores were significantly related to future performance outcomes, the real question is whether
they capture information that improves prediction of performance outcomes beyond traditional numerical ratings. To
this extent, a series of regression models were run to test whether narrative scores explain unique variance in the separate outcomes of next-year numerical performance ratings, future involuntary turnover, future promotions, and future
pay increases. In predicting each outcome, the first step involved entering control variables. Exempt-status, job tenure,
and organizational tenure were significantly related to all outcomes in the calibration dataset and were controlled for
in this step. Following the procedures from Bernerth and Aguinis (2016), these controls were included based upon theoretical concerns, have been used as controls in past performance studies, and are not latent constructs (and therefore
reliability is not of concern). Exempt status is defined 1 = exempt (i.e., salaried) and 0 = nonexempt (i.e., hourly). This
term is an important control because it distinguishes different types of jobs that have separate pay structures, managing structures, types of work, and ultimately levels of performance ratings. Likewise, it was desired to place everyone on
an equal playing-field regarding tenure, given its known relation to job performance (Schmidt & Hunter, 1998). Beyond
these three primary control variables, ratee word count was also controlled for in step 1 to isolate the effect of narrative sentiment in later steps, though results were same regardless of whether word count was treated as a control,
as a part of the narrative score, or not included at all. In step 2, the traditional numerical performance ratings from
2014 were entered, and in step 3, the narrative sentiment scores were entered to examine the incremental effect of
narrative comments. Tables 2–5 present these findings.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

315

SPEER

SPEER

TA B L E 2

Regression analyses predicting next-year's numerical performance ratings (2015)
Ordinal narrative

Neg logistic narrative

Step

Predictor

𝜷

R

1

Org tenure

−.03

.100**

.010**

Job tenure

.00

.00

.00
−.09

2
3

𝜷
−.02

Pos logistic narrative

𝚫R2

R

𝚫R2

𝜷

R

𝚫R2

.100**

.010**

−.03

.100**

.010**

.51

.615**

.368**

.18

.632**

.021**

Exempt status

−.09

−.07

2014 Word count

.02

.02

2014 Numerical rating

.49

.615**

.368**

.59

.615**

.368**

.20

.635**

.025**

−.09

.621**

.007**

2014 Narrative score

.01

Note. N = 3,582.
*p < .05, **p < .01. Separate regressions were run for each of the derived narrative scores (ordinal narrative scores, negative
logistic narrative scores, positive logistic narrative scores). For each regression, final standardized regression weights are presented.

Table 2 displays results predicting next-year performance ratings, with separate regression equations presented
for each of the three narrative scores (ordinal narrative, negative logistic, and positive logistic). Despite the strong
correlation between traditional numerical ratings across years, and despite a strong correlation between same-year
numerical ratings and narrative ratings, the 2014 ordinal narrative scores explained unique variance above and beyond
2014 traditional ratings in predicting 2015 numerical ratings (ΔR2 = .025, p < .01). The change in R2 was also significant
for the negative logistic narrative score (ΔR2 = .007, p < .01) and the positive logistic narrative score (ΔR2 = .021,
p < .01).
Table 3 displays logistic regression analyses in the prediction of involuntary turnover. Narrative scores explained
significant incremental variance in the prediction of involuntary turnover (Δ𝜒 2 df (1) = 13.0, ΔR2 = .011, p < .01)7 ,
though the magnitude of ΔR2 was not large. Interestingly, the negative logistic score was more influential than the
other narrative scores (Δ𝜒 2 df (1) = 33.3, ΔR2 = .023, p < .01), and the positive logistic score did not explain significant
incremental variance. This is expected, given the negative score was keyed upon the lower end of the performance
distribution.
Ordinal narrative scores also explained unique variance in promotions (Δ𝜒 2 df (1) = 7.6, ΔR2 = .007, p < .05),
although the incremental magnitude was lower than with previous outcomes and less than 1% of total variance
explained. Given promotions are a positive outcome, the positive logistic narrative also explained a small portion of
unique variance (Δ𝜒 2 df (1) = 8.6, ΔR2 = .008, p < .01), whereas the negative logistic score did not. Finally, narrative
scores explained unique variance in predicting future pay increases, as shown in Table 5. The ordinal narrative scores
(ΔR2 = .008, p < .01), negative logistic scores (ΔR2 = .011, p < .01), and the positive logistic scores (ΔR2 = .004, p < .01)
each added incremental variance, though once again the incremental change in variance explained was not large. Taken
together, Hypothesis 7 was fully supported.8

5.4

Does usefulness of narratives vary across the numerical rating distribution?

How informative narratives are may depend upon whether they accompany a negative, neutral, or positive traditional
numerical rating. It was predicted that narrative ratings would exhibit more variability and explain more unique variance within the middle of the numerical rating distribution. Table 6 provides 2014 narrative score means, 2014 narrative score standard deviations, and correlations between 2014 narrative scores with next-year's (2015) performance
ratings, bucketed by 2014 numerical ratings. Comparing the variance of narrative scores for those in the middle of the
distribution (SD = .48) versus the average variance within all other levels (SD = .41) reveals a significance difference in
variance, F (1,537, 3,138) = 1.38, p < .01, supporting Hypothesis 8.9 A post hoc comparison revealed that the difference in variance was nonsignificant when comparing narrative score variance from middle of the distribution to variance from the lower portion of the distribution (ratings 1–3, SD = .54), F (146, 1,537) = 1.23, p = ns. Instead, the major
difference occurred when compared against the high rating distribution (ratings 5–7, SD = .41), F (1,537, 2,991) = 1.41,

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

316

.55

.47

1.00

1,192.9

1,205.9

1,329.1

1,460.7

−2LL

.174**
.183**

13.0**

.090**

R2

123.2**

131.6**

𝚫−2LL

11.83

.49

1.00

.83

1.09

.88

1,172.6

1,205.9

1,329.1

1,460.7

−2LL

33.3**

123.2**

131.6**

𝚫−2LL

Negative logistic narrative
Exp(𝜷)

.197**

.174**

.090**

R2

.89

.37

1.00

.88

1.10

.88

1,205.8

1,205.9

1,329.1

1,460.7

−2LL

.1

123.2**

131.6**

𝚫−2LL

Positive logistic narrative
Exp(𝜷)

.175**

.174**

.090**

R2

317

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Note. N = 4,677.
*p < .05, **p < .01. Separate regressions were run for each of the derived narrative scores (ordinal narrative scores, negative logistic narrative scores, positive logistic narrative scores). Exp
(𝛽) = exponentiated 𝛽, otherwise known as an odds ratio. −2LL is model deviance. Note for all logistic regressions R2 is a logistic analog of R2 (i.e., pseudo-R2 ) and is formed by subtracting the
residual deviance from the null model deviance and then dividing by the null model deviance (Cohen, Cohen, West, & Aiken, 2003).

2014 Narrative score

3

2014 Word count

2014 Numerical rating

2

.90

1.10

Job tenure

1

Exempt status

.88

Null

Org tenure

0

Exp(𝜷)

Predictor

Ordinal narrative

Logistic regression analyses predicting involuntary turnover

Step

TA B L E 3

SPEER

1.89

904.8

912.4

987.0

1,072.0

−2LL

.149**
.156**

7.6*

.079**

R2

74.6**

85.0**

𝚫−2LL

.02

2.84

1.00

3.96

.86

.95

Exp(𝜷)

911.1

912.4

987.0

1,072.0

−2LL

1.2

74.6**

85.0**

𝚫−2LL

Negative logistic narrative

.150**

.149**

.079**

R2

4.11

2.35

1.00

3.74

.86

.95

Exp(𝜷)

903.7

912.4

987.0

1,072.0

−2LL

Positive logistic narrative

8.6*

74.6**

85.0**

𝚫−2LL

.157**

.149**

.079**

R2

SPEER

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Note. N = 4,677.
*p < .05, **p < .01. Separate regressions were run for each of the derived narrative scores (ordinal narrative scores, negative logistic narrative scores, positive logistic narrative scores).
Exp(𝛽) = exponentiated 𝛽, otherwise known as an odds ratio. −2LL is model deviance. Note that for all logistic regressions, R2 is a logistic analog of R2 (i.e., pseudo-R2 ) and is formed by subtracting
the residual deviance from the null model deviance and then dividing by the null model deviance (Cohen et al., 2003).

2014 Narrative score

3

2.36

1.00

2014 Numerical rating

2

2014 Word count

.86

3.78

Job tenure

1

Exempt status

.95

Null

Org tenure

0

Exp(𝜷)

Predictor

Ordinal narrative

Logistic regression analyses predicting promotions

Step

TA B L E 4

318

TA B L E 5

Regression analyses predicting percent pay increases
Ordinal narrative

Neg logistic narrative

Pos logistic narrative

Step

Predictor

𝜷

R

𝚫R

𝜷

R

𝚫R

𝜷

R

𝚫R2

1

Org tenure

−.24

.266**

.071**

−.24

.266**

.071**

−.23

.266**

.071**

.37

.484**

.164**

.07

.488**

.004**

2
3

2

2

Job tenure

−.11

−.10

−.11

Exempt status

−.09

−.08

−.09

2014 Word count

.04

2014 Numerical rating

.34

.484**

.164**

.37

.484**

.164**

.15

.493**

.008**

−.12

.496**

.011**

2014 Narrative score

.04

.04

Note. N = 4,328.
*p < .05,**p < .01. Separate regressions were run for each of the derived narrative scores (ordinal narrative scores, negative
logistic narrative scores, positive logistic narrative scores). Because of the skew and kurtosis of the original pay change variable, the square-root-transformed variable was used for regression analyses. For each regression, final standardized regression weights are presented.

TA B L E 6

Variance and correlations between 2014 narrative scores and 2015 numerical ratings by 2014 numerical

ratings
2014 Numerical
Rating

N

Mn narrative
score (2014)

SD narrative
score (2014)

R 2015 numerical
ratings

1–3

147

3.91

.54

.25*

4

1,538

4.55

.48

.24**

5–7

2,992

5.16

.41

.16**

Note. Sample sizes for the correlation between 2014 narrative ratings and 2015 traditional numerical ratings, by level of 2014
numerical rating, are N = 82 for ratings 1–3, N = 1,121 for ratings of 4, and N = 2,379 for ratings of 5–7.
*p < .05,**p < .01.

p < .01. Thus, narrative comments displayed more variability at low to moderate areas of the traditional performance
distribution, and less variance for higher ratings.
To examine whether narrative ratings were more informative (i.e., explain more unique variance) at certain parts
of the distribution, next-year performance ratings were used as the dependent variable. Comparing the correlation
between narrative scores and next-year numerical ratings for those in the middle of the distribution (r = .24) versus the
average correlation across all other levels (r = .17) reveals a significance difference in correlations (Z = 2.41, p < .05),
supporting Hypothesis 9. Once again, narratives from the middle of the distribution were not significantly more correlated with the dependent variable than narratives from the lower portion (r = .25) of the distribution (Z = −.16, p = ns),
but the correlation was significantly higher than that for narratives from the higher portion of the distribution (r = .16,
Z = 2.49, p < .05). Thus, narrative comments seem to be more informative and most helpful at lower to moderate areas
of the traditional performance distribution.

5.5

Multilevel analysis of rater effects

Large portions of performance rating variance are often attributable to rater effects (Scullen et al., 2000), and as such
follow-up analyses were conducted to investigate the relationship between narrative scores and traditional ratings
after controlling for rater-level factors. Using 2014 ratings, a multistep multilevel regression model was run using 2014
traditional numerical ratings as the dependent variable (Table 7). Note that analyses were also conducted for 2015
ratings, with similar findings. For simplicity, it was chosen to only interpret 2014 results here. Managers averaged 17.39
years of organizational tenure and 4.55 years of job tenure in role, and the average number of subordinates rated by
manager was eight.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

319

SPEER

.02

276.74

4.96

.10

Level 2 intercept variance .10

.02

.69

2

.06

.02

.00

50.65**

−10.34**

−6.98**

2.34*

1.67

2.46*

2.62**

−.05

12.91**

366.71**

t

SPEER

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Note. *p < .05, **p < .01. ƅ = unstandardized coefficient. Values presented under the likelihood ratio test are comparisons of model deviance in 𝜒 form.

.72

.74

.42

2,443.61**
(df = 5)

465.31**
(df = 4)

Level 1 residual variance

2,549.01**
(df = 9)

570.70**
(df = 8)

1,978.31**
(df = 1)

105.40**
(df = 4)

12

Model 2 to tested model

Model 1 to tested model

Null to tested model

Likelihood ratio test

11

11,768.29

9,789.99

12,233.60
7

12,339.00

3

.00

Model df

−12.21**

Deviance

.00

.04

−.29
22.16

.00

.01
**

.00

.00

.03

.00

.00

.00

.01

2.03*

.07

.01

.00

.00

4.95

SE

1.17

2.66**

2.78**

2.65**

14.12**

367.15

**

Model 3: L1 Narrative
ƅ

1.13

.00

Rater Mn word count

.04

.00

.00

.03

.00

.00

.00

.01

t

Ratee narrative score

.81

.08

3.57**

Rater Mn narrative score

.01

.01

.04

.00

3.01**

Rater job tenure

Ratee exempt status

.01
.00

.00

3.70**

4.95

9.04**

278.12

**

SE

Model 2: Rater variables
ƅ

.00

.13

Ratee job tenure

.00

.02

t

Rater org tenure

.01
.01

Ratee org tenure

.00

4.96

**

SE

Model 1: Controls
t

ƅ

SE

Null model

ƅ

Prediction of 2014 traditional numerical ratings using multilevel modeling

Ratee word count

Intercept

TA B L E 7

320

As seen in Table 7, 12.1% of the numerical rating variance was attributable to between-rater effects. After controlling for rate-level factors (org tenure, job tenure, and exempt status) and ratee word count, inclusion of rater level
variables of org tenure, job tenure, mean narrative performance scores, and average rater word count collectively
explained 81.1% of the available between rater variance, and collectively the variables explained 15.8% of total variance. In the next step, level-1 ordinal narrative scores were added, resulting in a significant improvement in model fit,
∆𝜒 2 (1) = 1,978.31 (p < .01). After accounting for level 1 controls and rater-level effects, the individual narrative scores
explained an additional 38.6% of remaining level-1 residual variance and an additional 32.5% of total rating variance.
Taken together, sentiment scores were highly related to numerical ratings after taking into account rater-level effects.
A potentially more interesting question is not whether narrative scores predict ratings after controlling for rater
effects, but whether there are large between-rater differences in narrative scores and whether the relationship
between numerical ratings and narrative scores varies across raters (i.e., significant slope variation). Research shows
that there are stylistic writing differences (e.g., Manning & Schütze, 1999; Pang & Lee, 2008); it is also likely that raters
vary in what types of information they rely upon when writing comments (Rotundo & Sackett, 2002) and that different
contextual, political, and personal factors motivate them. This question requires changing the dependent variable from
traditional numerical ratings to the narrative scores, with findings shown in Table 8.
First, narrative scores displayed larger amounts of between-rater variance (31.1%, from Table 8) than did the traditional numerical ratings (12.1%, from Table 7). A large portion of this variance was explained by level-1 control variables (org tenure, job tenure, and exempt status), ratee word count, and level-2 rater variables (rater org tenure, rater
job tenure, mean traditional numerical rating, and average rater word count), collectively explaining 62.3% of available
between-rater variance and 20.1% of total variance. When level-1 traditional numerical ratings were added in step 3,
an additional 39.5% of level-1 variance was explained and an additional 26.8% of total rating variance was explained.
Finally, a random slope term for level-1 numerical ratings was added to this model, resulting in a significant chi-square
change ∆𝜒 2 (2) = 115.66 (p < .01) and a variance of .018 (SD = .134). That results in a 90% unstandardized confidence interval of .13 to .57 for the slope of traditional numerical ratings, indicating that some raters very much align
comments with numerical ratings, others less so, and it is unlikely that traditional ratings will be negatively related to
narrative scores for a rater. Of course, the next step would usually be explaining this variance, and a number of ad hoc
interactions were examined in efforts to do so (e.g., manager tenure by numerical ratings). However, additional variance
explained in these efforts was inconsequential and therefore not reported.

6

DISCUSSION

This study theorized and presented initial data on a rich and yet underutilized data source within performance
appraisals. It was shown that narrative comments can be automatically scored and that those scores correlate with and
explain incremental variance in performance-related outcomes. This extends our understanding of performance measurement, highlights the utility in leveraging automatic text mining, and opens new research avenues to understand
employee performance. Below is a discussion of this paper's major theoretical contributions, practical contributions,
and areas for future work.

6.1

Theoretical considerations

This study was the first to use text mining to automatically score performance narratives and then evaluate the accuracy of the derived sentiment scores. Results were generally favorable. Narrative scores demonstrated strong sameyear convergence with numerical ratings, were reliable from year-to-year, and correlated with performance-related
outcomes such as turnover, promotions, and pay increases. These findings are noteworthy for several reasons.
First, narrative scores were clearly capturing performance-related variance. We know that narrative text aligns
with traditional ratings and that the narratives were calibrated upon them. Thus, finding that narrative scores converged with traditional ratings is not surprising, although still impressive given the magnitude of the correlations found,
and the prediction across the nomological network of job performance outcomes. In fact, the convergence between

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

321

SPEER

.08

.46
.00

Rater Mn num rating

Rater Mn word count

.10
.00

22.86**
**

2,070.88**
(df = 3)

2,336.95**
(df = 5)
1,955.21**
(df = 1)

381.74**
(df = 4)

.06

.05
.02

.01

.00

.02

.00

.00

.02

.00

38.44**

2.22*

4.55**

−3.61**

−1.26

.76

−.63

4.69**

−2.87**

469.41**

t

SPEER

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

Note. *p < .05, **p < .01. ƅ = unstandardized coefficient. Values presented under the likelihood ratio test are comparisons of model deviance in 𝜒 2 form.

.04

.10

Level 2 intercept variance .10

𝜎 2 Ratee num rating

.12

.13

.22

Level 1 residual variance .23

.22

2,452.62**
(df = 7)

2,387.45**
(df = 9)

2,503.12**
(df = 11)

14

4,755.83

.35

.00

432.24**
(df = 8)

50.54**

3.05

.10

−.01

.00

115.66**
(df = 2)

50.50**
(df = 4)

.01

.00

**

4.87**

−3.61**

−1.53

.01

.00

−.53
.80

.00

.00

.00

4.64**

.00

−3.40**

SE
.01

ƅ

466.36** 4.93

t

Model 4: Random slope

Model 3 to tested model

Model 2 to tested model

Model 1 to tested model

Null to tested model

Likelihood ratio test

12

4,871.49

11

Model df

7

7,258.95

3

Deviance

−4.71

.00

−.01
.02

.00

.00

−1.74

.02

.00

.00

.00

.01

SE

−3.63**

.02

.00

.00

.00

2.70**

.62

5.81**

6.14**

.36

.00

ƅ

474.33** 4.92

t

Model 3: L1 Narrative

Ratee numerical rating
6,826.70

.00
.02

.00

.00

.02

.00

−.01

.06

3.36**

Rater org tenure

.00

1.06

.00

5.79**
.00

.00

.00

5.25**

SE
.01

ƅ

360.37** 4.92

t

Model 2: Rater variables

Rater job tenure

7,208.45

.00

.00

Ratee job tenure

Ratee exempt status

.03

.00

.01

Ratee org tenure

.00

.01

SE

.00

353.55** 4.94

t

ƅ

.01

SE

ƅ

4.94

Model 1: Controls

Null model

Prediction of 2014 narrative scores using multilevel modeling

Ratee word count

Intercept

TA B L E 8

322

323

narrative scores and traditional ratings, as well as year-to-year consistency displayed, is stronger than studies that have
used manual human coding. For instance, David (2013) only found a correlation of .26 between manually coded narratives and same-year numerical ratings. On the other hand, Smither and Walker (2004) rated individual units within
comments and found strong interrater reliability, and with correlations of .67 with same-year numerical ratings and
.50 with next year's numerical ratings, which is more comparable with the results from this study. These are just a few
examples, and well-developed coding schemes with highly trained raters should result in accurate assessments of comment valence. However, people are also prone to decision errors and faulty synthesizing of information (e.g., Kuncel,
Klieger, Connelly & Ones, 2013; Meehl, 1954), which algorithms are not. At a minimum, it appears text mining and
machine learning algorithms can be trained to produce valid representations of comment sentiment, and that can be
applied within performance contexts.
Second, narratives were assumed to contain true performance variance, and a portion of that variance was assumed
to be incremental over traditional numerical ratings. In every test of this, narrative scores explained unique variance
in the prediction of performance-related outcomes within the nomological network, though it should be noted that
for some outcomes, the incremental change in variance explained was not large. Like Smither and Walker (2004) who
found that manually coded comments predict future performance improvement, this study's derived sentiment scores
explained unique variance in future performance ratings, involuntary turnover, promotions, and pay increases. These
incremental findings are particularly interesting given that the scores were calibrated upon numerical ratings themselves; words and word phrases indicative of negative or positive ratings were identified and these generalized to the
holdout sample, yielding something similar yet different from the numerical ratings themselves, and that difference
represented true-score variance (e.g., variance related to performance change).
Had a broader criterion composite been applied, such as a composite of both objective (e.g., customer satisfaction
ratings, objective sales data) and rating-based performance indicators, one might expect even greater measurement
bandwidth and therefore higher convergence with a broader range of performance variables. On the other hand, if
researchers are interested in predicting a narrow behavior or outcome, such as customer service, a narrow sampling
of the criterion domain for model calibration will perform better, per basic principles of the bandwidth-fidelity literature (e.g., Cronbach, 1960; Cronbach & Gleser, 1965; Hogan & Roberts, 1996; Ones & Viswesvaran, 1996; Schneider
et al., 1996). Thus, depending on what one hopes to accomplish when calibrating comment valence algorithms, narrative scores will measure different components of the performance space.
Third, a sizable proportion of narrative score variance was attributable to the rater. This is not surprising. After all,
people have distinct authoring styles (e.g., Manning & Schütze, 1999; Pang & Lee, 2008). Similarly, traditional numerical ratings also suffer from differing levels of elevation (e.g., Murphy & Cleveland, 1995), such that some raters are
more lenient and some are harsher. Thus, it was also not surprising that when rater effects from traditional ratings
were taken into account, total between-rater variance for narratives dropped. Additionally, when that rater variance
was controlled for, narrative scores still explained large proportions of individual variance in performance ratings. Like
traditional ratings, narratives are influenced by rater tendencies as well as variance directly attributable to individual
ratee variation.
Fourth, traditional ratings contain both bias and error (Wherry & Bartlett, 1982), and this was expected to occur
more in the middle of the traditional distribution. It was expected that narratives would be most variable and most
uniquely predictive within that middle region of the performance distribution, because this is the area where the most
traditional rating bias was assumed to exist. Some support was found for this assumption when comparing middle distribution narrative scores to higher distribution scores. This suggests that very favorable traditional ratings will align
well with narrative comments; if someone is a good performer they will be described as such. In this case, the narrative provides less unique information. On the other hand, average and below average ratings displayed more variation
in narrative sentiment, and that variation contained true score variance. This likely occurs when the numerical rating
contains bias due to social and contextual factors (e.g., DeNisi et al., 1984; Harris, 1994; Judge & Ferris, 1993; Levy &
Williams, 2004; Wherry & Bartlett, 1982), but the rater provides a more honest assessment of their employee within
the narrative review when those narratives are not linked to distributive outcomes. In addition, variance likely captured information pertaining to improvement, coaching, and developmental tips for those in the middle to lower end

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

SPEER

SPEER

of the distribution. Collectively, narrative scores should be particularly informative for employees rated as average or
below average.

6.2

Practical implications

This study showed that narrative comments are useful sources of data that can help predict future performance outcomes, and those narratives can be scored without manual, human efforts. Regarding the first point, performance
appraisals have suffered from relentless criticism over their reliability and accuracy (Scullen et al., 2000; Viswesvaran
et al., 1996), and thus even minor gains in psychometric properties will be welcomed. Inclusion of narrative data can
increase the reliability and bandwidth of measurement, and this can be done automatically via text mining. For example, the inclusion of narrative comment scores with traditional ratings increased year-to-year temporal consistency
from .61 to .67 (by 10%). The question is then how to apply these results and in what contexts. In this respect, there is
not an easy answer.
On the one hand, there are possible benefits to leveraging narrative data in the applied field. If, indeed, an organization has the resources to create sentiment scores using text algorithms, those scores could be combined with numerical ratings, resulting in enhanced accuracy of performance measurement. This could then be leveraged for determining
decisions such as involuntary terminations, promotions, and pay raises. These sentiment scores could provide “gentle”
suggestions for such decisions, such as synthesizing the numerical rating, sentiment score, and discretionary dollar pool
to recommend an employee's pay increase. This automation should hypothetically decrease the influence of biases and
faulty judgment when making these decisions. In a similar vein, the narrative scores could even be used to influence the
numerical rating itself and “course correct” when needed. As an example, a manager's comments could be automatically
scored and warnings given to the manager if the comments were drastically different from the numerical score entered
into the performance system. Such a system could have substantial positive benefit, resulting in qualitative data that
is well aligned with ratings and providing an additional prompt that forces raters to fully think through what they are
doing when conducting PAs.
On the other hand, there are many potential issues in applying this methodology for decision making, and potentially enough to suggest that it currently only be used for applied research (e.g., test validation) or non-decision-making
applications (e.g., the “course-correction” proposal outlined above). For one, if narratives were combined with ratings
to inform decisions, raters could still game the system by tweaking the narratives to align with their goals. One of the
motivating factors discussed in this paper dealt with the link between measurement and administrative decisions, and
using narratives to partially decide distributive outcomes would almost surely result in more lenient language. Narrative scores are no magic bullet. Organizations would need to provide clear instructions around expected length and
scope of comments, and user reactions would need to be well researched. Second, the rater effects found within this
study highlight concerns over variance attributable to the rater, as well as any potential rater biases. Well thought-out
protocols would need drafting to minimize distortion and to limit any bias. If leveraged to make decisions, one would
want to ensure that word phrases associated with protected classes are not used so to safeguard against legal risk. A
thorough review of word lists should be conducted, along with adverse impact analyses, and it would be wise to consider a more construct-oriented approach to algorithm building, either through formation of latent performance categories or by using single responses from construct-specific text boxes. More work in this area is highly recommended.
In general, narrative scores can be reliably developed and implemented with low setup costs. All that is needed
is a competent researcher, some programming or IT skills, and a little up-front time to set things up. From there, the
automation provides insights with little maintenance beyond periodic tests that the model is still performing adequately, and the challenge may be more the human element of how to leverage such data. Any implementation should
balance legal risk with reward. As standardized, job-related procedures are given credence in court settings, practitioners must ensure that raters are fully aware of how narrative data will be used, trained on how to write narratives,
and that data should be used consistently if it is leveraged for employment decisions. Either way, the application of
automated narrative scoring to guide decision making is a potentially fruitful area for researchers and practitioners in
the applied field.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

324

6.3

Limitations and areas for future research

This study was in part a proof-of-concept endeavor, mixing inductive and deductive methods to better understand a
high potential data source within the performance space. There are many questions still needing answers, and this will
hopefully spur future programs of research to answer such questions. This next section breaks down other areas for
future research.

6.4

Areas of future performance research

This study assumed that narrative comment data overlap with traditional numerical ratings and simultaneously captures unique performance variance. The incremental gains from narratives are hypothesized to occur as a function of
increases in total information and a reduction in rater-motivated bias (assuming traditional ratings are tied to administrative decisions and narrative comments are not). These assumptions are grounded in the extant performance literature. However, there was no direct test of these specific mechanisms, and future research should remedy this. For
instance, were the narrative improvements due to enhanced reliability when combining narratives with traditional ratings, or was it more a function of enhanced bandwidth due to contextualization of behavior and increased elaboration
(or some combination of both)? This study examined effects on temporal consistency but not interrater reliability; ideally, one would compare different forms of reliability, as well as the increased coverage of the performance domain.
Such a question is just one of many when considering the application of performance narratives. Here, groups of moderators are outlined that may impact comment data and the usefulness of such data. I address these briefly and urge
researchers to consider them in future research endeavors.

6.4.1

Design factors

Survey design features will moderate the quality of information provided from narrative comments. First, the bandwidth of the numerical performance scale will affect the amount of unique information gathered from narratives. Narrative comments, due to their increased contextualization, should be of most unique benefit when performance scales
are very broad and only measure a few competencies (such as just an overall rating). When the traditional numerical
ratings cover a varied set of narrow behaviors, the gains from narrative comments should be lessened. Second, the format of comment prompts is important. Are raters required (formally or informally) to provide responses, which will
increase the amount of text? Do specific text prompts exist for every corresponding numerical rating, or are there just
a few prompts (e.g., improvement suggestions, major strengths, overall comments)?
Third, it may be possible that the inclusion of comment prompts spurs more involved information processing when
making ratings (including traditional ratings). A requirement to provide rating justification may trigger cognitive elaboration, and research shows that the simple act of recalling critical performance incidents can improve rating accuracy
at the time of ratings (Williams, Cafferty, & DeNisi, 1990; Williams, DeNisi, Meglino, & Cafferty, 1986). This would be
important given the myriad of tasks managers must deal with beyond their performance rating responsibilities (Harris,
1994), forcing them to critically think through their ratings prior to making them. Finally, the methods used to score narratives (e.g., sentiment algorithm, manual coding) will affect the reliability and information obtained from text scores
and as such will moderate the quality of the derived narrative scores.

6.4.2

Contextual factors

Broader cultural and social organizational context factors (e.g., see Levy & Williams, 2004) will also moderate narrative
information quality. Probably, the most important contextual factor is the strength of contingency between traditional
numerical ratings and administrative decisions. In environments where there is pressure to align comments with organizational decisions, the correlations between ratings and narrative scores should be higher, limiting the amount of
unique information obtained from comments. When the two rating formats serve different purposes, raters will be
more likely to provide discrepant information within the narratives (Brutus, 2010).

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

325

SPEER

SPEER

Second, organizational feedback norms should affect the amount of text created (e.g., Fedor, Rensvold, & Adams,
1992). In departments or organizations where feedback is highly valued, or where accountability is high (Levy &
Williams, 2004), raters should be more inclined to provide rich narrative feedback. This extends to rater anticipation of upcoming performance discussions too. When manager–employee discussions are highly valued, raters
may put forth more effort to embed their feedback within the narrative comments. Finally, whether or not performance management is valued by leadership will impact narratives. When greater emphasis is placed on the quality of ratings by senior leadership, one's immediate supervisor, or one's group of manager peers, raters should be
more inclined to provide rich narrative comments. That, in turn, will lead to higher quality information. In cases
where feedback accountability is not high, when leadership does not espouse the values of ratings, and when ratings are not discussed in person, one might wonder whether narrative texts would provide consistently useful
information.

6.5

Rater and ratee factors

Rater and ratee factors should independently and in combination affect the quality of narrative comments. For one,
raters who are motivated to provide good feedback should write more and produce more insightful text (Brutus, 2010).
Although comments were assumed to result in increased information, there will be cases where raters will provide
minimal text about ratee performance (e.g., “the employee meets performance expectations”). In this case, no information gains would be expected from the comments. Two, because writing is a cognitively demanding task (Fitzer,
2003; Kellogg, 1994), raters with higher verbal ability and who can therefore more easily articulate their thoughts
will be more capable of producing informative narratives. These factors together could produce comments with low
interrater reliability, if two sources provided comments and those comments were used as stand-alone measures of
performance.
Another important area for future research is investigating how the type of rater affects the quality and content
of narrative information. This study only looked at manager-made comments, but research shows that different raters
focus more on certain aspects of performance and are exposed more frequently to certain types of behaviors (Hoffman
& Woehr, 2009; Lance et al., 2008). This has not been examined with narrative comments specifically. Are different
sources less likely to focus on developmental needs when writing narratives? Are certain sources capable of providing
rich feedback around specific types of performance behaviors? Rupayana et al. (2017) compared the content of references made from managers and coworkers and found noticeable differences. Additional systematic research is needed
to look at these differences for performance narrative comments specifically.
Other rater factors might also include job tenure and tenure as manager, as the former affects the opportunity to
observe a target, whereas the latter may lead to response sets. For example, it is possible that new managers might
not want to offend or might be adamant that their ratings are soundly based on behavioral data. In addition, demographic factors such as race, age, and gender might be relevant to narratives within a performance context, with the
interaction between rater and ratee being particularly interesting (making this a rater-by-ratee factor). Given existing
research on perceived gender differences (Eagly, 2007), one might expect different language to be used to describe
men and women. Furthermore, one could investigate how similarity between rater and ratee impacts the elevation
of comment sentiment, similar to work done with traditional ratings (e.g., Pulakos, Schmitt, & Chan, 1996; Sackett &
DuBois, 1991; Stauffer & Buckley, 2005) and started with narrative comments (Wilson, 2010). Finally, rater tendencies,
experiences, and traits are proposed to influence comment creation, including response tendencies (e.g., halo, Murphy,
Jako, & Anhalt, 1993), stereotypes (e.g., Murphy & Cleveland, 1995), training exposure (Woehr, 1994), traits related to
elevation (Harari, Rudolph, & Laginess, 2015), and individual moderators of judgment accuracy (e.g., Borman, 1979).
Given the degree of rater-specific variance found here, this is likely a prime area for future research.
Models of narratives also focus heavily on the reactions of the ratee and the motivating effects of certain types of
comments. These are certainly valid topics, though only likely to affect narrative information quality if the desire to
be procedurally fair influences what raters write, and it might. A strong focus on fairness might cause raters to align
ratings and comments. If ratees are particularly vocal about fairness or exhibit feedback seeking tendencies, this may

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

326

prompt raters to provide elaborate, longer, and better aligned narrative comments. In addition, the degree of liking
between manager and subordinate (Sutton, Baldwin, Wood, & Hoffman, 2013) could potentially impact the favorability
of comments, with the expectation that increased liking will be associated with increased comment favorability after
controlling for true performance levels.

6.6

Text mining and additional future areas of performance research

There are several additional directions for future research regarding the method of text mining specifically. For one,
this study took a generalized approach to performance measurement and the development of a localized dictionary. Analyses were conducted across jobs, years, and locations within one organization. As research in job analysis
clearly shows, jobs do differ, and one might wonder how generalizable locally created dictionaries might be across
organizations, jobs, and locations. Research in sentiment analysis shows that dictionaries are often context-specific,
although the contexts in that body of research are quite different from the performance context covered here. Are the
adjectives and words used to describe employee performance similar across companies? I would wager yes, but at the
same time, there will be within-job and within-culture variation. For instance, visual inspection of the developed dictionaries here revealed phrases that were specific to job families but would not apply to others. Future research should
investigate the generalizability of developed dictionaries and whether it is possible to create master dictionaries that
could be applied across organizations and just how narrow dictionaries might need to be at the job family level. As an
example, researchers could create specific dictionaries for broad job families like standard occupational classification
(SOC) codes, which have linkages via O*NET (National Center for O*NET Development, 2017). These are important
issues that need more research.
Two, this study focused on the holistic narrative score as opposed to any subfactors derived during the text mining. Although word clouds were used to understand what types of word phrases contributed to sentiment scores, the
latent structure of the word phrases was not investigated to understand exactly what the algorithm was measuring.
Smither and Walker (2004) and Brutus (2010) discussed the practice of assessing specific units of information (i.e.,
themes) from comments, and Kobayashi et al. (2017b) outline empirical methods for topic modeling and dimensionality reduction. Future research might consider factor analytical methods, clustering methods, or more advanced natural language processing methods to gain additional meaning from the data. As suggested by an anonymous reviewer,
these data might also lend themselves to a multitrait–multimethod analysis as a means to better establish construct
validity. For instance, if narrative text could be scored to capture various constructs (e.g., leadership), one could juxtapose the narrative method of measurement with manager ratings of the same dimensions, 360 observer ratings, and
with assessment data (e.g., personality testing). This would help understand what exactly can be assessed reliably with
performance narratives and is a recommended area for future work.
Finally, like Campion et al. (2016), this study highlights the utility of leveraging text mining within organizational
settings. Within this domain, there is room to investigate the many methods and approaches for scoring text data.
This includes investigating decision rules for cleaning data, whether there are gains to using more in-depth natural
language processing, different approaches to vectorizing text, uses of different types of algorithms (e.g., regressionbased, random forests), and rules regarding required sample sizes for calibration and holdout groups. For much of this,
the machine learning and natural language processing literatures can be referred to, but our field would also benefit
from context-specific investigations of these matters.

7

CONCLUSIONS

Narrative comments are a rich and interesting data source that should be leveraged more within the performance management domain. Whereas manual efforts to code comments have precluded large-scale systematic measurement,
recent improvements in the computer sciences make automatic coding in this context more feasible. Because comment
data offer potential gains in total performance measurement, future efforts should be made to continue investigating
their validity and utility in performance contexts.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

327

SPEER

SPEER

NOTES
1 Historically, focus on bandwidth and fidelity (Cronbach, 1960; Cronbach & Gleser, 1965; Ones & Viswesvaran, 1996; Schnei-

der, Hough, & Dunnette, 1996) has discussed the trade-off between the two. However, a trade-off only exists if the length of
the test, or in this case the amount of total performance information collected, is held constant.
2 This precondition is especially important, and it is one that the reviewers and editor made an emphasis to note. Some com-

panies may not have a strong contingency between traditional ratings and administrative outcomes, and in some cases,
outcomes may even be determined by narrative comments. The assumption that narratives will contain less bias is contingent upon the condition that traditional ratings are more directly tied to distributive outcomes within a given context. Likewise, if a company began utilizing narrative data to make decisions, it is expected that any gains in bias reduction would be
eliminated.
3 To maintain anonymity, all narrative comments were stripped of names, and all raters and ratees were identified via random

ID variable within the dataset.
4

Note that I did examine whether expressions such as exclamation marks were indicative of positive sentiment and did not find
there to be a strong positive effect.

5 Although Kobayahsi et al. (2017a) suggest that these features might not improve model performance, within this study, the

inclusion of bigrams and trigrams was found to improve model performance in cross-validated samples (R2 was 1.7% higher
than a model using just unigrams), thus justifying their use.
6

Elastic net parameters for the ordinal narrative score were alpha = .01 and lambda = .25, which means that the model
was prominently ridge regression. Elastic net parameters for the negative logistic narrative score were alpha = .05 and
lambda = .01, and for the positive logistic narrative score, they were alpha = .05 and lambda = 05.

7

Note for all logistic regressions, R2 is a logistic analog of R2 (i.e., pseudo-R2 ) and is formed by subtracting the residual deviance
from the null model deviance and then dividing by the null model deviance (Cohen, Cohen, West, & Aiken, 2003).

8 A separate set of regression analyses was also performed by adding all three narrative scores simultaneously (ordinal, nega-

tive logistic, positive logistic) in the final step of the regression for each outcome (next year performance, turnover, promotions, and pay). In each case, the best performing narrative score was near equivalent in total variance explained compared to
a weighted composite of all three. Therefore, these results are not shown.
9

Visual comparison of predicted values versus residuals was performed to examine heteroscedasticity. When regressing 2015
ratings on 2014 predictors (control variables, traditional ratings, and narrative text), there was consistency in residuals across
the span of predicted values, meaning the data were homoscedastic. Visual inspection of same year relationships (either 2014
or 2015) indicated residuals remained relatively consistent across predicted values, though there was some fluctuation. Thus,
there was some degree of heteroscedasticity for same-year comparisons. This is likely to occur when certain portions of a
distribution contain more error, which is assumed as part of these analyses. That said, heteroscedasticity is not “fatal to an
analysis” (Tabachnick & Fidell, 2001, p. 80), and comparisons of the ratios of conditional variances within each level of performance ratings were less than 2.0 for all comparisons, which is far less than the value of 10 recommended by Cohen et al.
(2003) as an indication of severe heteroscedasticity. Nevertheless, results should be interpreted with caution.

ORCID
Andrew B. Speer

http://orcid.org/0000-0002-3376-2103

REFERENCES
Aguinis, H., O'Boyle, E., Jr., Gonzalez-Mule, E., & Joo, H. (2016). Cumulative advantage: Conductors and insulators of heavytailed productivity distributions and productivity stars. Personnel Psychology, 69, 3–66.
Attali, Y., Lewis, W., & Steier, M. (2013). Scoring with the computer: Alternative procedures for improving the reliability of
holistic essay scoring. Language Testing, 30, 125–141.
Austin, J. T., & Villanova, P. (1992). The criterion problem: 1917–1992. Journal of Applied Psychology, 77, 836–874.
Balzer, W. K., & Sulsky, L. M. (1992). Halo and performance appraisal research: A critical examination. Journal of Applied Psychology, 77, 975–985.
Barrick, M. R., Mount, M. K., & Strauss, J. P. (1994). Antecedents of involuntary turnover due to a reduction in force. Personnel
Psychology, 47, 515–535.
Becker, W. J., & Cropanzano, R. (2011). Dynamic aspects of voluntary turnover: An integrated approach to curvilinearity in the
performance-turnover relationship. Journal of Applied Psychology, 96, 233–246.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

328

329

Bernerth, J. B., & Aguinis, H. (2016). A critical review and best-practice recommendations for control variable usage. Personnel
Psychology, 69, 229–283.
Borman, W. C. (1979). Individual differences correlates of accuracy in evaluating others' performance effectiveness. Applied
Psychological Measurement, 3, 103–115.
Borman, W. C., Bryant, R. H., & Dorio, J. (2010). The measurement of task performance as criteria in selection research. In J. L.
Farr & N. T. Tippins (Eds.), Handbook of employee selection (pp. 439–461). New York: Routledge.
Bosco, F. A., Aguinis, H., Singh, K., Field, J. G., & Pierce, C. A. (2015). Correlational effect size benchmarks. Journal of Applied
Psychology, 100, 431–449.
Brutus, S. (2010). Words versus numbers: A theoretical exploration of giving and receiving narrative comments in performance
appraisal. Human Resource Management Review, 20, 144–157.
Buckingham, M., & Goodall, A. (2015). Reinventing performance management. Harvard Business Review, 93, 40–50.
Bycio, P., Hackett, R. D., & Alvares, K. M. (1990). Job performance and turnover: A review and meta-analysis. Applied Psychology,
39, 47–76.
Cascio, W. F., & Aguinis, H. (2005). Applied psychology in human resource management (6th ed.). Upper Saddle River, NJ: PrenticeHall.
Campion, M. C., Campion, M. A., Campion, E. D., & Reider, M. H. (2016). Initial investigation into computer scoring of candidate
essays for personnel selection. Journal of Applied Psychology, 101, 958–975.
Christianson DeMay, C., Chandonnet, A., Rasinowich, C., & Fenlason, K. J. (2006, May). Application of an automated content
analysis process to multisource comments. Paper presented at the 21st Annual Conference of the Society for Industrial
and Organizational Psychology, Dallas, TX.
Cohen, J., Cohen, P., West, S. G., & Aiken, L. S. (2003). Applied multiple regression/correlation analysis for the behavioral sciences (3rd
ed.). Mahwah, NJ: Lawrence Erlbaum Associates.
Cronbach, L. J. (1960). Essentials of psychological testing (2nd ed.). New York, NY: Harper & Row.
Cronbach, L. J., & Gleser, G. C. (1965). Psychological tests and personnel decisions (2nd ed.). Urbana, IL: University of Illinois Press.
Cronbach, L. J., & Meehl, P. E. (1955). Construct validity in psychological tests. Psychological Bulletin, 52, 281–302.
Crook, T. R., Todd, S. Y., Combs, J. G., Woehr, D. J., & Ketchen, D. J., Jr. (2011). Does human capital matter? A meta-analysis of
the relationship between human capital and firm performance. Journal of Applied Psychology, 96, 443–456.
David, E. M. (2013). Examining the role of narrative performance appraisal comments on performance. Human Performance, 26,
430–450.
DeCotiis, T. A., & Petit, A. (1978). The performance appraisal process: A model and some testable hypotheses. Academy of Management Review, 21, 635–646.
DeNisi, A. S., Cafferty, T. P., & Meglino, B. M. (1984). A cognitive view of the performance appraisal process: A model and
research propositions. Organizational Behavior & Human Performance, 33, 360–396.
DeNisi, A. S., & Murphy, K. R. (2017). Performance appraisal and performance management: 100 years of progress? Journal of
Applied Psychology, 102, 421–433.
Eagly, A. H. (2007). Female leadership advantage & disadvantage: Resolving the contradictions. Psychology of Women Quarterly,
31, 1–12.
Fedor, D. B., Rensvold, R. B., & Adams, S. M. (1992). An investigation of factors expected to affect feedback seeking: A longitudinal field study. Personnel Psychology, 45, 779–805.
Fitzer, K. (2003). Review of theoretical and applied issues in written language expression. Canadian Journal of School Psychology,
18, 203−221.
Funder, D. C. (2006). Towards a resolution of the personality triad: Persons, situations, and behaviors. Journal of Research in
Personality, 40, 21–34.
Gatewood, R. D., Field, H. S., & Barrick, M. R. (2016). Human resource selection (8th ed.). New York: Cengage Learning.
Gorman, C. A., Meriac, J. P., Roch, S. G., Ray, J. L., & Gamble, J. S. (2017). An exploratory study of current performance management practices: Human resource executives’ perspectives. International Journal of Selection and Assessment, 25, 193–
202.
Griffeth, R. W., Hom, P. W., & Gaertner, S. (2000). A meta analysis of antecedents and correlates of employee turnover: Update,
moderator tests, and research implications for the next millennium. Journal of Management, 26, 463–488.
Grimmer, J., & Stewart, B. M. (2013). Text as data: The promise and pitfalls of automatic content analysis methods for political
texts. Political Analysis, 21, 1–31.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

SPEER

SPEER

Harari, M. B., Rudolph, C. W., & Laginess, A. J. (2015). Does rater personality matter? A meta-analysis of rater big fiveperformance rating relationships. Journal of Occupational and Organizational Psychology, 88, 387–414.
Harris, M. M. (1994). Rater motivation in the performance appraisal context: A theoretical framework. Journal of Management,
20, 737–756.
Harrison, D. A., Newman, D. A., & Roth, P. L. (2006). How important are job attitudes? Meta-analytic comparisons of integrative
behavioral outcomes and time sequences. Academy of Management Journal, 49, 305–325.
Hedricks, C. A., Robie, C., Rupayana, D., & Puchalski, L. (2017, April). Reference feedback on applicants: Do narrative comments
predict behavior ratings? Paper presented at the 32nd Annual Conference of the Society for Industrial and Organizational
Psychology, Orlando, FL.
Hoerl, A. E., & Kennard, R. W. (1970). Ridge regression: Biased estimation for nonorthogonal problems. Technometrics, 12, 55–
67.
Hoffman, B. J., & Woehr, D. J. (2009). Disentangling the meaning of multisource performance rating source and dimension
factors. Personnel Psychology, 62, 735–765.
Hogan, J., & Roberts, B. W. (1996). Issues and non-issues in the fidelity-bandwidth trade-off. Journal of Organizational Behavior,
17, 627–637.
Hom, P. W., Mitchell, T. R., Lee, T. W., & Griffeth, R. W. (2012). Reviewing employee turnover: Focusing on proximal withdrawal
states and an expanded criterion. Psychological Bulletin, 138, 831–858.
Ignatow, G., & Mihalcea, R. (2017). Text mining: A guidebook for the social sciences. Thousand Oaks, CA: Sage.
Jawahar, I. M., & Williams, C. R. (1997). Where all the children are above average: The performance appraisal purpose effect.
Personnel Psychology, 50, 905−925.
Judge, T. A., & Ferris, G. R. (1993). Social context of performance evaluation decisions. Academy of Management Journal, 36,
80–105.
Kabins, A. (2016). Why the qualms with qualitative? Utilizing qualitative methods in 360 degree feedback. Industrial and Organizational Psychology, 4, 806–810.
Kellogg, R. T. (1994). The psychology of writing. New York, NY: Oxford University Press.
Kim, Y., & Ployhart, R. E. (2014). The effects of staffing and training on firm productivity and profit growth before, during, and
after the great recession. Journal of Applied Psychology, 99, 361–389.
Kobayashi, V. B., Mol, S. T., Berkers, H. A., Kismihók, G., & Den Hartog, D. N. (2017a). Text classification for organizational researchers: A tutorial. Organizational Research Methods. Advanced online publication. http://journals.sagepub.
com/doi/abs/10.1177/1094428117719322
Kobayashi, V. B., Mol, S. T., Berkers, H. A., Kismihók, G., & Den Hartog, D. N. (2017b). Text mining in organizational research. Organizational Research Methods. Advanced online publication. http://journals.sagepub.com/doi/
abs/10.1177/1094428117722619
Kuhn, M. (2014). A short introduction to the caret package. Retrieved from https://cran.r-project.org/web/packages/caret/
vignettes/caret.pdf
Kuhn, M., & Johnson, K. (2013). Applied predictive modeling. New York, NY: Springer.
Kuncel, N. R., Klieger, D. M., Connelly, B. S., & Ones, D. S. (2013). Mechanical versus clinical data combination in selection and
admissions decisions: A meta-analysis. Journal of Applied Psychology, 98, 1060–1072.
Lance, C. E., Hoffman, B. J., Gentry, W. A., & Baranik, L. E. (2008). Rater source factors represent important subcomponents of
the criterion construct space, not rater bias. Human Resource Management Review, 18, 223–232.
Landers, F. N. (2017). A crash course in natural language processing. The Industrial-Organizational Psychologist, 54, 1–9.
Landy, F. J., & Farr, J. L. (1980). Performance rating. Psychological Bulletin, 87, 72–107.
Levy, P. E., & Williams, J. R. (2004). The social context of performance appraisal: A review and framework for the future. Journal
of Management, 30, 881–905.
Lewin, K. (1936). Principles of topological psychology. New York, NY: McGraw-Hill.
Liu, B. (2012). Sentiment analysis and opinion mining. San Rafael, CA: Morgan & Claypool Publishers.
Mairesse, F., Walker, M., Mehl, M., & Moore, R. (2007). Using linguistic cues for the automatic recognition of personality in
conversation and text. Journal of Artificial Intelligence Research, 30, 457–500.
Manning, C. D., & Schütze, H. (1999). Foundations of statistical natural language processing. Cambridge, MA: MIT Press.
McAbee, S. T., Landis, R. S., & Burke, M. I. (2017). Inductive reasoning: The promise of big data. Human Resource Management
Review, 27, 277–290.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

330

Medhat, W., Hassan, A., & Korashy, H. (2014). Sentiment analysis algorithms and applications: A survey. Ain Shams Engineering
Journal, 5, 1093–1113.
Meehl, P. E. (1954). Clinical versus statistical prediction: A theoretical analysis and a review of the evidence. Minneapolis, MN: University of Minnesota Press.
Miller, G. A. (1995). WordNet: A lexical database for English. Communications of the ACM, 38, 39–41.
Murphy, K. R., & Cleveland, J. N. (1995). Understanding performance appraisal: Social, organizational, and goal-based perspectives.
Thousand Oaks, CA: Sage.
Murphy, K. R., Jako, R. A., & Anhalt, R. L. (1993). Nature and consequences of halo error: A critical analysis. Journal of Applied
Psychology, 78, 218–225.
Murphy, K. R., Cleveland, J. N., Skattebo, A. L., & Kinney, T. B. (2004). Raters who pursue different goals give different ratings.
Journal of Applied Psychology, 89, 158–164.
National Center for O*NET Development.
onetcenter.org/taxonomy.html.

(2017).

O*NET-SOC

taxonomy.

Retrieved

from

https://www.

Ng, T. W. H., Eby, L. T., Sorensen, K. L., & Feldman, D. C. (2005). Predictors of objective and subjective career success. A metaanalysis. Personnel Psychology, 58, 367–408.
Olenick, J., Dixon, A., Dishop, C., Harvey, R., Karner, J., Change, D., & Kozlowski, S. (2017, April). Applying linguistic analysis to
isolated, and confined, extreme environmental teams. Paper presented at the 32nd Annual Conference of the Society of
Industrial and Organizational Psychology, Orlando, FL.
Ones, D. S., & Viswesvaran, C. (1996). Bandwidth-fidelity dilemma in personality measurement for personnel selection. Journal
of Organizational Behavior, 17, 609–626.
Paltoglou, G., & Thelwall, M. (2010). A study of information retrieval weighting schemes for sentiment analysis. Proceedings of
the 48th Annual Meeting of the Association for Computational Linguistics, pp. 1386–1395.
Pandey, S., & Pandey, S. K. (2017). Applying natural language processing capabilities in computerized textual
analysis to measure organizational culture. Organizational Research Methods. Advanced online publication.
http://journals.sagepub.com/doi/abs/10.1177/1094428117745648
Pang, B., & Lee, L. (2008). Opinion mining and sentiment analysis. Foundations and Trends in Information Retrieval, 2, 1–135.
Park, G., Schwartz, H. A., Eichstaedt, J. C., Kern, M. L., Kosinski, M., Stillwell, D. J., … Seligman, M. E. P. (2014). Automatic personality assessment through social media language. Journal of Personality and Social Psychology: Personality Processes and
Individual Differences, 108, 934–952.
Pennebaker, J. W., & King, L. A. (1999). Linguistic styles: Language use as an individual difference. Journal of Personality and
Social Psychology, 77, 1296–1312.
Pulakos, E. D., Hanson, R. M., Arad, S., & Moye, N. (2015). Performance management can be fixed: An on-the-job experiential
learning approach for complex behavior change. Industrial and Organizational Psychology: Perspectives on Science and Practice,
8, 51–76.
Pulakos, E. D., & O'Leary, R. S. (2010). Defining and measuring results of workplace behavior. In J. L. Farr & N. T. Tippins (Eds.),
Handbook of employee selection (pp. 513–528). New York, NY: Routledge.
Pulakos, E. D., & O'Leary, R. S. (2011). Why is performance management broken? Industrial and Organizational Psychology: Perspectives on Science and Practice, 4, 146–164.
Pulakos, E. D., Schmitt, N., & Chan, D. (1996). Models of job performance ratings: An examination of ratee race, ratee gender,
and rater level effects. Human Performance, 9, 103–119.
Putka, D. J., Beatty, A. S., & Reeder, M. C. (2017). Modern prediction methods: New perspectives on a common problem. Organizational Research Methods.
R Core Development Team. (2007). R: A language and environment for statistical computing. Vienna: Foundation for Statistical
Computing.
Roberts, B. W., & DelVecchio, W. F. (2000). The rank-order consistency of personality traits from childhood to old age: A quantitative review of longitudinal studies. Psychological Bulletin, 126, 3–25.
Rotundo, M., & Sackett, P. R. (2002). The relative importance of task, citizenship, and counterproductive performance to global
ratings of job performance: A policy- capturing approach. Journal of Applied Psychology, 87, 66–80.
Rupayana, D., Hedricks, C. A., Robie, C., & Puchalski, L. (2017, April). Who wrote that? Source effects in narrative feedback from
references. Paper presented at the 32nd Annual Conference of the Society for Industrial and Organizational Psychology,
Orlando, FL.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

331

SPEER

SPEER

Sackett, P. R., & DuBois, C. L. Z. (1991). Rater-ratee race effects on performance evaluation: Challenging meta-analytic conclusions. Journal of Applied Psychology, 76, 873–877.
Schmidt, F. L., & Hunter, J. E. (1998). The validity and utility of selection methods in personnel psychology: Practical and theoretical implications of 85 years of research findings. Psychological Bulletin, 124, 262–274.
Schmidt, F. L., & Hunter, J. (2004). General mental ability in the world of work: Occupational attainment and job performance.
Journal of Personality and Social Psychology, 86, 162–173.
Schneider, R. J., Hough, L. M., & Dunnette, M. D. (1996). Broadsided by broad traits: How to sink science in five dimensions or
less. Journal of Organizational Behavior, 17, 639–655.
Schwartz, H. A., Eichstaedt, J. C., Kern, M. L., Dziurzynski, L., Ramones, S. M., Agrawal, M., … Ungar, L. H. (2013). Personality,
gender, and age in the language of social media: The open vocabulary approach. PLoS One, 8, e73791.
Scullen, S. E., Mount, M. K., & Goff, M. (2000). Understanding the latent structure of job performance ratings. Journal of Applied
Psychology, 85, 956–970.
Smither, J. W., & Walker, A. G. (2004). Are the characteristics of narrative comments related to improvement in multirater
feedback ratings over time? Journal of Applied Psychology, 89, 575–581.
Spence, J. R., & Keeping, L. (2011). Conscious rating distortion in performance appraisal: A review, commentary, and proposed
framework for research. Human Resource Management Review, 21, 85–95.
Stamatatos, E. (2009). A survey of modern authorship attribution methods. Journal of the American Society for information Science
and Technology, 60, 538–556.
Stauffer, J. M., & Buckley, R. M. (2005). The existence and nature of racial bias in supervisory ratings. Journal of Applied Psychology, 90, 586–591.
Strapparava, C., & Valitutti, A. (2004). WordNet-affect: An affective extension of WordNet. In Proceedings of the Fourth International Conference on Language Resources and Evaluation, pp. 1083–1086.
Stumpf, S. A., & Dawley, P. K. (1981). Predicting voluntary and involuntary turnover using absenteeism and performance indices.
Academy of Management Journal, 24, 148–163.
Sturman, M. C., Cheramie, R. A., & Cashen, L. H. (2005). The impact of job complexity and performance measurement on the
temporal consistency, stability, and test-retest reliability of employee job performance ratings. Journal of Applied Psychology,
90, 269–283.
Sutton, A. W., Baldwin, S. P., Wood, L., & Hoffman, B. J. (2013). A meta-analysis of the relationship between rater liking and
performance ratings. Human Performance, 26, 409–429.
Tabachnick, B. G., & Fidell, L. S. (2001). Using multivariate statistics (4th ed.). Boston, MA: Allyn and Bacon.
Tausczik, Y. R., & Pennebaker, J. W. (2010). The psychological meaning of words: LIWC and computerized text analysis methods.
Journal of Language and Social Psychology, 29, 24–54.
Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. Journal of the Royal Statistical Society: Series B, 58, 267–
288.
Van Der Vegt, G., Bunderson, J., & Oosterhof, A. (2006). Expertness diversity and interpersonal helping in teams: Why those
who need the most help end up getting the least. Academy of Management Journal, 49, 877–893.
Viswesvaran, C., Ones, D. S., & Schmidt, F. L. (1996). Comparative analysis of the reliability of job performance ratings. Journal
of Applied Psychology, 81, 557–574.
Viswesvaran, C., Schmidt, F. L., & Ones, D. S. (2005). Is there a general factor in ratings of performance? A meta-analytic framework for disentangling substantive and error influences. Journal of Applied Psychology, 90, 108–131.
Wang, X. M., Wong, K. F. E., & Kwong, J. Y. Y. (2010). The roles of rater goals and ratee performance levels in the distortion of
performance ratings. Journal of Applied Psychology, 95, 546.
Wells, D. L., & Muchinsky, P. M. (1985). Performance antecedents of voluntary and involuntary managerial turnover. Journal of
Applied Psychology, 70, 329–336.
Wherry, R. J., & Bartlett, C. J. (1982). The control of bias in ratings: A theory of rating. Personnel Psychology, 35, 521.
Williams, K. J., Cafferty, T. P., & DeNisi, A. S. (1990). Effects of appraisal salience on recall and ratings. Organizational Behavior
and Human Decision Processes, 46, 217–239.
Williams, K. J., DeNisi, A. S., Meglino, B. M., & Cafferty, T. P. (1986). Initial judgments and subsequent appraisal decisions. Journal
of Applied Psychology, 71, 189–195.
Wilson, K. Y. (2010). An analysis of bias in supervisor narrative comments in performance appraisal. Human Relations, 63, 1903–
1933.

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

332

333

Wilson, T., Wiebe, J., & Hwa, R. (2006). Just how mad are you? Finding strong and weak opinion clauses. Computational Intelligence, 22, 73–99.
Woehr, D. J. (1994). Understanding frame-of-reference training: The impact of training on the recall of performance information. Journal of Applied Psychology, 79, 525–534.
Wong, K. F. E., & Kwong, J. Y. Y. (2007). Effects of rater goals on rating patterns: Evidence from an experimental field study.
Journal of Applied Psychology, 92, 577–585.
Zedeck, S., & Cascio, W. F. (1982). Performance appraisal decisions as a function of rater training and purpose of the appraisal.
Journal of Applied Psychology, 67, 752–758.
Zou, H., & Hastie, T. (2005). Regularization and variable selection via the elastic net. Journal of the Royal Statistical Society: Series
B, 67, 301–320.
Zyphur, M. J., Chaturvedi, S., & Arvey, R. D. (2008). Job performance over time is a function of latent trajectories and previous
performance. Journal of Applied Psychology, 93, 217–224.

How to cite this article: Speer AB. Quantifying with words: An investigation of the validity of narrative-derived
performance scores. Personnel Psychology. 2018;71:299–333. https://doi.org/10.1111/peps.12263

17446570, 2018, 3, Downloaded from https://onlinelibrary.wiley.com/doi/10.1111/peps.12263 by Virginia Tech, Wiley Online Library on [07/11/2023]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License

SPEER


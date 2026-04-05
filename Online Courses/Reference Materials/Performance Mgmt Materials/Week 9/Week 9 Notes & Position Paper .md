**[Performance Appraisal]{.underline}**

**[Week 9 (10/18): Multiple Metrics and Agreement in Performance Appraisals]{.underline}**

**Reliability Analysis:**

Explore the reliability of the ratings by computing the Cronbach\'s Alpha.

pythonCopy code

\# \... (Reliability Analysis code from the previous version)

**Interrater Correlation Analysis:**

Compute the interrater correlation using Pearson or Spearman\'s correlation coefficient to understand the degree to which the ratings from different raters are associated.

pythonCopy code

\# \... (Interrater Correlation Analysis code from the previous version)

**Discussion on Correlations Vs Reliability:**

Based on the interrater correlation analysis and the reliability analysis conducted earlier, discuss the difference between correlation and reliability in the context of performance appraisal. Reflect on the statement from Murphy & DeShon (2000) that correlations do not estimate the reliability of job performance ratings and discuss how this understanding impacts the interpretation of your analysis.

Here are the key points about ICC:

1.  **Measurement of Consistency or Agreement**:

    - ICC assesses the consistency or agreement of measurements, meaning it gauges how closely the data collected by different raters or instruments are aligned.

    - A high ICC indicates that the raters are providing consistent ratings across the subjects, while a low ICC suggests a lack of agreement among the raters.

2.  **Scale**:

    - The ICC values range between 0 and 1.

    - An ICC of 0 indicates no agreement among raters, and an ICC of 1 indicates perfect agreement.

3.  **Types of ICC**:

    - There are several forms of ICC depending on the study design and the specific assumptions being made.

    - For instance, ICC(1,1) assumes that both subjects and raters are randomly selected, while ICC(2,1) assumes that raters are fixed and subjects are random.

    - ICC(3,1) assumes that both raters and subjects are fixed, which means that the raters are the only raters of interest and the subjects are the only subjects of interest.

4.  **Calculation**:

    - ICC is calculated based on a ratio of variances.

    - The numerator represents the variance due to the subjects (the \"between\" variance), and the denominator represents the total variance, which includes both the \"between\" variance and the \"within\" variance (the variance due to the raters plus the residual variance).

The formula for ICC in a one-way random effects model, for instance, is:

ICC=Between-group varianceBetween-group variance+Within-group varianceICC=Between-group variance+Within-group varianceBetween-group variance​

5.  **Interpretation**:

    - The interpretation of ICC can be nuanced and should be done in the context of the specific study design and the particular form of ICC being used.

    - It\'s often interpreted as the proportion of the total variance that is due to the variance between subjects.

6.  **Applications**:

    - ICC is used in various fields for reliability analysis, particularly in settings where multiple raters or instruments are used to collect data on the same set of subjects.

    - It's often used in medical research, psychology, organizational studies, and other fields where inter-rater reliability is a concern.

The Intraclass Correlation Coefficient (ICC) is a measure of reliability or consistency of quantitative measurements made by different observers measuring the same quantity. It\'s often used in scenarios where you have multiple raters (also called judges or observers) evaluating the same set of subjects across different conditions or over time. Here's a more simplified breakdown of ICC:

1.  **What ICC Measures**:

    - ICC assesses how consistently different raters evaluate the same subjects.

    - It provides a score between 0 and 1 which measures the degree of agreement among raters.

**Example**:

- Suppose three doctors are rating the severity of illness of the same group of patients on a scale of 1 to 10. ICC can be used to determine how consistently these doctors are rating the severity of illness across patients. If the ICC is high (close to 1), it suggests that the doctors are largely in agreement on the severity ratings. If the ICC is low (close to 0), it suggests that there is little agreement among the doctors on the severity ratings.

For example, if one rater always rates 1 point higher than another rater, there is high reliability (they are consistently one point apart), but not perfect agreement (they don't give the exact same rating).

The articles for this week provide different perspectives on rater agreement in performance appraisal scores. While Facteau & Craig (2001) and Strauss (2005) find some evidence for agreement in various types of ratings, Murphy & DeShon (2000) provide a more nuanced approach that shows less support for agreement.

In your opinion, should raters be provided with other rater\'s ratings or know if the other raters have agreement or disagreement with them? What are the benefits or drawbacks to doing so, and how would this best be implemented in an organization?

1.  **Impact on Objectivity:**

    - How might knowing other raters' scores impact an individual rater's objectivity? Can this knowledge introduce bias, or can it lead to more calibrated and accurate assessments?

2.  **Feedback Quality:**

    - How can the quality and specificity of feedback be maintained if raters are aware of others' evaluations? Does it lead to richer insights or generic feedback?

3.  **Implementation Challenges:**

    - What are the potential challenges in implementing a system where raters are aware of each other's scores? How can these be mitigated to ensure fair and accurate appraisals?

4.  **Employee Perception:**

    - How might employees perceive the transparency of knowing that raters are aware of each other\'s ratings? Could this impact their trust in the appraisal process?

5.  **Training and Development:**

    - Would there be a need for additional training for raters to effectively utilize the information about other raters' scores? What might this training entail?

6.  **Ethical Considerations:**

    - Are there ethical considerations to weigh when sharing other raters' scores with evaluators? How can confidentiality and professionalism be maintained?

7.  **Organizational Culture:**

    - How does the organizational culture influence the decision to share or not share other raters' scores? Are certain cultures more conducive to this approach?

8.  **Technology's Role:**

    - How can technology facilitate or hinder the process of sharing other raters' evaluations? What features or safeguards should be in place?

9.  **Long-term Implications:**

    - What could be the long-term effects on employee performance and organizational health if raters are provided with insights into others' evaluations?

10. **Customization of the Approach:**

    - Should the decision to share other raters' ratings be customized based on the team, department, or individual being assessed? How can organizations make informed decisions on this?

**Hannah Ashby**

- Nope, drawbacks

- Conformity, groupthink, polarization, confidentiality

- Dominant personalities in person discussions

**Blair Butler**

- Examples of past raters responses to provide new raters context to increase agreement

- Increase rater understanding

- Do so but with anonymity

**Dan Caffery**

- Ratings should be provided to other raters

- However, with a coach or mediator

- Disagreements can provide information

**\
Charles Denman**

- Should share information based on benefits and drawbacks of the raters

- Confidentiality

- Different sources of information from different raters

**Mara Duckworth**

- Tell raters what others have rated after

- They probably already talk about it

- Promotions should be closed door

**Lauren Prata**

- Depends on some factors

- Only if taking into account the individuals complete performance

- Should know each other scores

- Avoid persuasion by submitting at the same time

- Eliminating biases and different perspectives

**Logan Robnett**

- Show ratings after submitting

- Control for biases

- Group dynamics could be negative

**Jack Wilkens**

- Share rater's ratings as a means to improve disagreement, but instead we could prioritize feedback

- Feedback should be prioritized

- More information leads to better ratings

**Tim Wu**

- Only when everyone has already turned in their ratings and there is a big discrepancy

- Peer pressure

- Group dynamics and different treatment

1.  **Definition**:

    - **Agreement**: Refers to the extent to which different raters provide identical ratings for the same subjects. It's about the concordance in the exact scores or ratings.

    - **Reliability**: Refers to the consistency of ratings across different raters. It's about whether the raters are systematically rating subjects in a similar manner, regardless of whether their ratings are identically the same.

2.  **Focus**:

    - **Agreement**: Focuses on the precision of ratings, examining how closely the ratings from different raters match each other.

    - **Reliability**: Focuses on the consistency or stability of ratings, examining whether the relative ranking of ratings remains the same across different raters.

3.  **Measurement**:

    - **Agreement**: Methods like Percent Agreement, Cohen's Kappa, and Bland-Altman Plot can be used to measure the level of agreement between raters.

    - **Reliability**: Methods like Intraclass Correlation Coefficient (ICC) and Cronbach\'s Alpha can be used to measure the reliability of ratings across different raters.

4.  **Interpretation**:

    - **Agreement**: High agreement indicates that raters are on the same page regarding their evaluations, providing similar scores for the same subjects.

    - **Reliability**: High reliability indicates that raters are consistent in their evaluations, even if they don't provide identical scores.

5.  **Importance in Performance Evaluations**:

    - **Agreement**: Essential for ensuring that different raters have a shared understanding and interpretation of the performance criteria. High agreement can lead to perceived fairness and acceptance of the evaluation process.

    - **Reliability**: Essential for ensuring that the evaluation process is stable and consistent over time or across different raters, which is crucial for the validity of the evaluation results.

6.  **Application**:

    - **Agreement**: More focused on the accuracy and unanimity in ratings which is often desired in performance evaluations to ensure fairness and clarity in assessments.

    - **Reliability**: More focused on the systematic approach of ratings which is crucial for establishing a dependable evaluation process.

7.  **Implication**:

    - **Agreement**: Lack of agreement may imply a need for rater training to calibrate their understanding and application of performance criteria.

    - **Reliability**: Lack of reliability may suggest a need for clearer guidelines or more objective criteria to reduce variability in ratings.

8.  **Reliability Assessment**:

    - You have multiple raters evaluating the performance of employees across different dimensions.

    - Reliability in this setting refers to the extent to which these raters are consistent in their evaluations.

9.  **Multiple Raters**:

    - Each dimension (e.g., Teamwork) is rated by multiple raters for each employee.

    - Cronbach\'s Alpha will help in understanding whether the raters are consistent with each other in their ratings for each dimension.

10. **Dimension-wise Assessment**:

    - By computing Cronbach\'s Alpha for each dimension separately, you\'re assessing the internal consistency of ratings within each dimension.

    - This provides insight into whether the raters\' evaluations are reliably consistent across different employees for each specific dimension.

11. **Interpretation**:

    - A high Cronbach\'s Alpha value (closer to 1.0) for a dimension would indicate that the raters are highly consistent in their ratings for that dimension across different employees.

    - Conversely, a low value (closer to 0.0) would suggest a lack of consistency among the raters for that dimension.

12. **Improvement and Feedback**:

    - Understanding the level of agreement among raters via Cronbach\'s Alpha can help identify dimensions where there might be ambiguity or differing interpretations among raters.

    - This, in turn, can be used to provide feedback to raters or to refine the rating process to achieve more reliable performance evaluations.

In summary, Cronbach's Alpha in this setting provides a measure of how well the set of raters are capturing a consistent evaluation across different employees for each performance dimension. It\'s a useful metric for understanding the reliability and consistency of the rating process in your performance appraisal assignment.

1.  **Purpose**:

    - **Cronbach\'s Alpha**: This is primarily used to assess the internal consistency or reliability of a set of test or scale items. It\'s often used in the context of questionnaires or scales where multiple items are intended to measure the same underlying construct.

    - **Intraclass Correlation Coefficient (ICC)**: ICC is used to assess the reliability of ratings or measurements made by different raters or instruments on the same subjects. It\'s often used in the context of reliability studies to assess the agreement among raters.

2.  **Assumptions**:

    - **Cronbach\'s Alpha**: Assumes that all items (or raters, in the context of your task) are interchangeable and measures the extent to which they all measure the same underlying construct.

    - **ICC**: Takes into account the structure of the data, considering both between-subject and within-subject variability. It\'s more suited for situations where the raters, items, or methods being compared are not interchangeable.

3.  **Calculation**:

    - **Cronbach\'s Alpha**: Calculated based on the average inter-item correlation.

    - **ICC**: Calculated based on a ratio of the between-group variance to the total variance (between-group plus within-group variance).

4.  **Output Interpretation**:

    - Both metrics produce a value between 0 and 1, where a higher value indicates better reliability or consistency.

    - However, the interpretation of these values is grounded in slightly different conceptual frameworks due to the differences in assumptions and calculation methods mentioned above.

5.  **Application in Your Setting**:

    - **Cronbach\'s Alpha**: Useful for checking the internal consistency among raters for each dimension separately, without considering the hierarchical or grouped structure of the data.

    - **ICC**: Might be more appropriate if you want to assess the reliability of ratings while accounting for the fact that the data has a hierarchical structure (e.g., ratings nested within dimensions nested within employees).

In summary, while both Cronbach\'s Alpha and ICC can provide insights into the reliability of your performance appraisal data, ICC might offer a more nuanced understanding of rater reliability by accounting for the structure of the data. On the other hand, Cronbach\'s Alpha provides a straightforward measure of internal consistency among raters for each dimension.

**Murphy, K. R., & DeShon, R. P. (2000). Interrater correlations do not estimate the reliability of job performance ratings. *Personnel Psychology, 53*, 873-900. <https://doi.org/10.1111/j.1744-6570.2000.tb02421.x>**

four sources of disagreement among raters were identified, including:

• Differences in observed behavior

• Differences in information available to the rater

• Differences in raters' experience levels

• Differences in how observed phenomena is evaluated

**Facteau, J. D., & Craig, S. B. (2001). Are performance appraisal ratings from different rating sources comparable? *Journal of Applied Psychology, 86*(2), 215- 227. [https://doi.org/10.1037/0021-9010.86.2.215](https://psycnet.apa.org/doi/10.1037/0021-9010.86.2.215)**

**Strauss, J. P. (2005). Multi‐source perspectives of self‐esteem, performance ratings, and source agreement. *Journal of Managerial Psychology*, *20*(6), 464-482. [https://doi.org/10.1108/02683940510615424](https://psycnet.apa.org/doi/10.1108/02683940510615424)**

\- Strauss found that different individuals' relationships

to an employee affect how they view that employee differently (2005).

1.  Murphy, K. R., & DeShon, R. P. (2000) critiqued the reliability of job performance ratings, challenging the conventional wisdom and methodologies underlying interrater correlations.

2.  Facteau, J. D., & Craig, S. B. (2001) delved into a comparative analysis of performance appraisal ratings from varied rating sources, exploring the nuances of comparability and consistency.

3.  Strauss, J. P. (2005) offered insights into the intricate dance between self-esteem, performance ratings, and source agreement, adding layers of psychological and relational dynamics into the mix.

The relationship between inter-rater correlations and reliability in the context of job performance ratings is a nuanced one. Here\'s a breakdown based on the referenced work by Murphy & DeShon (2000) and general principles in psychometrics:

1.  **Definition Divergence**:

    - **Interrater Correlation**: This metric assesses the degree of agreement or association between different raters. A high inter-rater correlation suggests that raters are consistent in their evaluations.

    - **Reliability**: This is a measure of the consistency or stability of a measurement over time or across different situations. It doesn\'t necessarily pertain to agreement between raters.

2.  **Different Foci**:

    - **Correlations** focus on the linear relationship between the ratings provided by different raters. They do not account for systemic biases or errors that might be present in the ratings.

    - **Reliability** focuses on the consistency and stability of measurements, which encompasses a broader set of considerations including the internal consistency of ratings, test-retest reliability, and other forms of measurement stability.

3.  **Bias and Error**:

    - Correlations can remain high even in the presence of systemic biases. For example, if one rater consistently rates higher than another, the ratings may still be highly correlated, but they are not reliable because of the bias.

    - Reliability metrics like Cronbach\'s Alpha or Intraclass Correlation Coefficient (ICC) can provide a more comprehensive understanding of the consistency and accuracy of ratings.

4.  **Scale of Measurement**:

    - Correlations are sensitive to the scale of measurement. A change in scale can alter the correlation coefficient significantly.

    - Reliability measures are less sensitive to the scale of measurement, making them more robust indicators of measurement consistency and accuracy.

5.  **Lack of Direct Estimation**:

    - Correlations do not provide a direct estimation of the proportion of variance in ratings that is attributable to true variance in the trait being measured (e.g., job performance).

    - Reliability metrics, on the other hand, are designed to estimate this proportion of variance, making them more suited for assessing the reliability of performance ratings.

6.  **Misinterpretation Risk**:

    - High inter-rater correlations can be misinterpreted as evidence of high reliability, which can lead to incorrect conclusions about the accuracy and usefulness of the ratings.

    - Reliability analysis provides a clearer picture of the potential errors and biases in the ratings, allowing for a more accurate interpretation of the data.

This exploration into the differences between inter-rater correlations and reliability highlights the importance of using appropriate statistical measures to accurately assess and interpret performance appraisal data.

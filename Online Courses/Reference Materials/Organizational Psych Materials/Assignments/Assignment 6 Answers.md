**Assignment 6**

**PSYC 650 --Organizational Psychology**

**Data Analysis & Hypothesis Testing on Burnout Among College Students**

Due to D2L on Wednesday December 4th @ 9 AM

**Objective:**

Apply regression and correlation analyses to explore the relationships between self-efficacy, social media usage, student employment, and burnout. Use statistical software (e.g., SPSS) to test hypotheses and interpret results. Utilize your chosen scales for the analysis.

**Instructions:**

Answer the questions below by working as a group on the analyses using the burnout study data. Make sure to turn in an assignment per individual for credit. Feel free to split up the work as a group if you want.

**Analysis Plan:**

Hypotheses:

- Hypothesis 1: Self-efficacy is negatively related to burnout among college students.

- Hypothesis 2: Social media usage is positively related to burnout among college students.

- Hypothesis 3: College student employment is positively related to burnout.

Variables:

- IVs: Self-efficacy (continuous), social media usage (continuous), and student employment (continuous)

- DV: Burnout (continuous)

Analyses to Perform:

1.  Initial tests of normality for parametric suitability.

2.  Simple regression analyses for each hypothesis.

3.  Multiple regression analysis to explore all IVs simultaneously.

4.  Mean difference testing for demographic group comparisons.

**Part 1: Preparing the Data**

1.  **Handling Missing Data**

- Identify and address missing data in the data set. For this study, missing data will be handled by dropping any cases (rows) with missing values. This is because we are focused on those students that are employed, and non-employed students would not have answered the employment hours question

- How many cases were removed due to missing data? 60 cases (114-60=54)

2.  **Reverse Scoring Items**

- Reverse score negatively worded items in the dataset (if applicable).

- Which items were reverse scored? \'MBI_15\', \'MBI_16\', \'MBI_17\', \'MBI_18\', \'MBI_19\', \'MBI_20\', \'MBI_21\', \'MBI_22\'

3.  **Compute Scale Scores**

- Compute scale scores for self-efficacy, social media usage, student employment, and burnout by calculating the average or sum of their respective items.

- List the label for each scale as it appears in Qualtrics:

  - Self-Efficacy Scale Score: GSE

  - Social Media Usage Scale Score: SMUS

  - Burnout Scale Score: MBI

> **Copy and paste SPSS output for computed scale scores below:**

**Relevant Results:**

- Self-Efficacy Scale Score (Mean, SD): (2.869, 0.574)

- Social Media Usage Scale Score (Mean, SD): (4.062, 1.879)

- Student Employment Scale Score (Mean, SD): (18.907, 8.742)

- Burnout Scale Score (Mean, SD): (3.817, 1.019)

- What is the reason to compute scale scores for each scale? Scale scores are computed to create a single measure that summarizes the response to multiple items, enhancing reliability and validity by reducing measurement error.

4.  **Test Scale Reliability**

- Assess the internal consistency of each scale using Cronbach's alpha. A Cronbach's alpha ≥ 0.70 is considered acceptable.

> **Copy and paste SPSS output for reliability testing here:**
>
> **Relevant Results:**

- Self-Efficacy Cronbach's Alpha: 0.915

- Social Media Usage Cronbach's Alpha: 0.936

- Burnout Cronbach's Alpha: 0.897

- Which scales have acceptable reliability? All of them

**Part 2: Initial Data Analysis**

5.  **Test of Normality**

- Use the scale scores computed in **Part 1** to test for normality (e.g., Shapiro-Wilk test, Kolmogorov-Smirnov test, or histogram visualization).

- Which test did you use and why?

> \- Test used: Shapiro-Wilk test
>
> \- Reason: The Shapiro-Wilk test is suitable for testing the normality of small to moderate sample sizes and provides reliable results for the dataset\'s size.
>
> **Copy and paste SPSS output for normality tests here:**

**Relevant Results:**

- Self-Efficacy Normality Test (test statistic, p-value): Test statistic = 0.973, p-value = 0.251

- Social Media Usage Normality Test (test statistic, p-value): Test statistic = 0.905, p-value = 0.000

- Student Employment Normality Test (test statistic, p-value): Test statistic = 0.960, p-value = 0.070

- Burnout Normality Test (test statistic, p-value): Test statistic = 0.979, p-value = 0.458

- Which scales are normally distributed? Self-Efficacy (GSE), Burnout (MBI), Hours

**Part 3: Correlation Analysis**

6.  **Create a Correlation Table**

- Generate a correlation matrix for self-efficacy, social media usage, student employment, and burnout.

> **Copy and paste SPSS output for the correlation matrix below:**
>
> **Relevant Results:**

- Self-Efficacy and Burnout (Hypothesis 1): Correlation (r = -0.619, p = 0.000)

- Social Media Usage and Burnout (Hypothesis 2): Correlation (r = 0.334, p = 0.014)

- Student Employment and Burnout (Hypothesis 3): Correlation (r = -0.159, p = 0.252)

<!-- -->

- Write a short interpretation of the correlations for each hypothesis.

- **Self-Efficacy**: There is a moderate negative correlation between self-efficacy and social media usage (r = -0.311, p = 0.022), suggesting that higher self-efficacy is associated with lower social media usage, and this relationship is statistically significant. There is a strong negative correlation between self-efficacy and burnout (r = -0.619, p \< 0.001), indicating that higher self-efficacy is strongly linked to lower burnout, and this relationship is statistically significant. The correlation between self-efficacy and hours worked is very weak and positive (r = 0.094, p = 0.498), suggesting almost no relationship and it is not statistically significant.

- **Social Media Usage**: Social media usage has a moderate positive correlation with burnout (r = 0.334, p = 0.014), implying that higher social media usage is linked to higher burnout, and this relationship is statistically significant. The correlation between social media usage and hours worked is weak and negative (r = -0.169, p = 0.221), indicating that higher social media usage may be associated with fewer hours worked, but this relationship is not statistically significant.

- **Burnout and Student Employment**: The correlation between burnout and hours worked is weak and negative (r = -0.159, p = 0.252), suggesting a slight tendency for more hours worked to be associated with lower burnout, though this correlation is not statistically significant.

**Part 4: Hypothesis Testing (Simple Regression)**

7.  **Testing Each Hypothesis in Isolation**

    - Conduct three simple regression analyses:

      - Hypothesis 1: Self-efficacy predicting burnout.

      - Hypothesis 2: Social media usage predicting burnout.

      - Hypothesis 3: Student employment predicting burnout.

> **Copy and paste SPSS output for each simple regression analysis below:**
>
> **Relevant Results for Simple Regression Analyses:**

- **Self-Efficacy → Burnout:**

  - Regression Coefficient (β): -0.619

  - Significance (p-value): 0.000

  - R²: 0.384

  - Interpretation: There is a strong negative relationship between self-efficacy and burnout (β = -0.619, p \< 0.001). The model explains 38.4% of the variance in burnout scores (R² = 0.384). For each one-unit increase in self-efficacy, burnout decreases by 1.099 units (B = -1.099, 95% CI \[-1.486, -0.711\]).

- **Social Media Usage → Burnout:**

  - Regression Coefficient (β): 0.334

  - Significance (p-value): 0.014

  - R²: 0.111

  - Interpretation: There is a moderate positive relationship between social media usage and burnout (β = 0.334, p = 0.014). The model explains 11.1% of the variance in burnout scores (R² = 0.111). For each one-unit increase in social media usage, burnout increases by 0.181 units (B = 0.181, 95% CI \[0.039, 0.323\]).

- **Student Employment → Burnout:**

  - Regression Coefficient (β): -0.159

  - Significance (p-value): 0.252

  - R²: 0.025

  - Interpretation: There is a very weak negative relationship between hours worked and burnout (β = -0.159, p = 0.252), and this relationship is not statistically significant. The model explains only 2.5% of the variance in burnout scores (R² = 0.025). For each additional hour worked, burnout decreases by 0.018 units (B = -0.018, 95% CI \[-0.050, 0.014\]), but this effect is not statistically significant.

- Write a short interpretation of the results for each hypothesis.

<!-- -->

- **Self-Efficacy and Burnout** Students with higher self-efficacy experience significantly lower burnout levels. This relationship is particularly robust, accounting for 38.4% of variance in burnout scores - making it the strongest predictor among variables studied.

- **Social Media and Burnout** Social media usage demonstrates a moderate positive correlation with burnout levels. While significant, it accounts for only 11.1% of variance in burnout scores, suggesting a less influential role than self-efficacy.

- **Employment and Burnout** Student employment hours show a negligible negative association with burnout. The relationship is not statistically significant and explains merely 2.5% of variance, indicating that employment hours are not a meaningful predictor of student burnout.

**Part 5: Multiple Regression Analysis**

8.  **Testing All Predictors Simultaneously**

    - Conduct a multiple regression analysis with self-efficacy, social media usage, and student employment predicting burnout.

> **Copy and paste SPSS output for the multiple regression analysis below:**
>
> **Relevant Results for Multiple Regression Analysis:**

- Model Summary (R²): 0.412

- **Predictor Coefficients (β) and Significance:**

  - Self-Efficacy: -0.567, p \< 0.001

  - Social Media Usage: 0.144, p = 0.219

  - Student Employment: -0.081, p = 0.466

- Write a short interpretation of the multiple regression results: The model significantly predicts burnout (F(3,50) = 11.683, p \< .001) and explains 41.2% of the variance in burnout scores (R² = 0.412).

> **Self-Efficacy:** Has a strong negative relationship with burnout (β = -0.567, p \< .001). For each one-unit increase in self-efficacy, burnout decreases by 1.006 units (B = -1.006).
>
> **Social Media Usage:** Shows a weak positive but non-significant relationship with burnout (β = 0.144, p = 0.219). For each one-unit increase in social media usage, burnout increases by 0.078 units (B = 0.078).
>
> **Student Employment:** Shows a very weak negative but non-significant relationship with burnout (β = -0.081, p = 0.466). For each additional hour worked, burnout decreases by 0.009 units (B = -0.009).
>
> These results indicate that self-efficacy is the strongest predictor of burnout among the variables studied.

**Part 6: Mean Difference Testing**

9.  **Bootstrap Resampling**

    - To ensure equivalence between sample sizes for each academic group, we will first bootstrap resample to create additional data points.

    - Number of bootstrap samples: 1000

10. **Examining Academic Year Differences** (I realize that I forgot to collect gender as a demographic-so that is one limitation...)

    - Conduct an ANOVA to compare mean scores on the variables of interest (self-efficacy, social media usage, student employment, and burnout) across the groups for different academic years.

> **Copy and paste SPSS output for mean difference testing below:**
>
> **Relevant Results:**
>
> **Self-Efficacy**:

- **Descriptive Statistics**:

  - Group 1 (Freshmen): M = 2.847, SD = 0.630

  - Group 2 (Sophomores): M = 2.762, SD = 0.448

  - Group 3 (Junior): M = 2.924, SD = 0.371

  - Group 4 (Senior): M = 3.032, SD = 0.639

  - Group 5 (Grad Student): M = N/A, SD = N/A

- **Test Results**:

  - ANOVA: F(3, 50) = 388.935, p \< 0.000

- **Effect Size**:

  - η² = 0.021

> **Social Media Usage**:

- **Descriptive Statistics:**

  - Group 1 (Freshmen): M = 4.517, SD = 2.218

  - Group 2 (Sophomores): M = 3.092, SD = 1.001

  - Group 3 (Junior): M = 4.321, SD = 1.317

  - Group 4 (Senior): M = 3.577, SD = 1.157

  - Group 5 (Grad Student): M = N/A, SD = N/A

- **Test Results**:

  - t-test/ANOVA: F(3, 50) = 1958.665, p \< 0.001

- **Effect Size**:

  - η² = 0.0981

> **Student Employment**:

- **Descriptive Statistics**:

  - Group 1 (Freshmen): M = 17.563, SD = 9.123

  - Group 2 (Sophomores): M = 21.597, SD = 6.092

  - Group 3 (Junior): M = 17.963, SD = 8.161

  - Group 4 (Senior): M = 20.682, SD = 9.676

  - Group 5 (Grad Student): M = N/A, SD = N/A

- **Test Results**:

  - ANOVA: F(3, 50) = 734.679, p \< 0.001

- **Effect Size**:

  - η² = 0.0392

> **Burnout**:

- **Descriptive Statistics**:

  - Group 1 (Freshmen): M = 3.946, SD = 1.073

  - Group 2 (Sophomores): M = 3.913, SD = 1.014

  - Group 3 (Junior): M = 3.258, SD = 0.640

  - Group 4 (Senior): M = 3.851, SD = 0.886

  - Group 5 (Grad Student): M = N/A, SD = N/A

- **Test Results**:

  - ANOVA: F(3, 50) = 1057.286, p \< 0.001

- **Effect Size**:

  - η² = 0.055

<!-- -->

- Write a short interpretation of the mean difference testing results:

> The results for the mean differences across the classification groups indicate that:
>
> **Self-Efficacy (GSE):** There are significant differences between groups (F = 388.94, p \< .001), with a small effect size (η² = 0.021). Seniors (M = 3.03) reported the highest self-efficacy, while sophomores (M = 2.76) reported the lowest. The largest difference was between sophomores and seniors (d = -0.49), indicating a moderate effect.
>
> **Social Media Usage (SMUS):** Significant differences exist between groups (F = 1958.67, p \< .001) with the largest effect size of all variables (η² = 0.098). Freshmen reported the highest usage (M = 4.52) and sophomores the lowest (M = 3.09). Large differences were found between sophomores and juniors (d = -1.05) and between freshmen and sophomores (d = 0.83).
>
> **Burnout (MBI):** Significant differences exist between groups (F = 1057.29, p \< .001) with a moderate effect size (η² = 0.055). Juniors reported the lowest burnout (M = 3.26) compared to freshmen (M = 3.95), with large differences between juniors and all other groups (d ranging from 0.77 to 0.78).
>
> **Student Employment (Hours):** Significant differences exist between groups (F = 734.68, p \< .001) with a small effect size (η² = 0.039). Sophomores worked the most hours (M = 21.60) and freshmen the least (M = 17.56). Moderate differences were found between sophomores and freshmen (d = -0.52) and between sophomores and juniors (d = 0.50).
>
> All group differences were statistically significant (p \< .001), with social media usage showing the largest overall effect size, followed by burnout, hours worked, and self-efficacy.
>
> **Part 7: Results Summary**
>
> **10. Summarizing Findings**

- Summarize results for each hypothesis. Indicate whether the data supported or rejected each hypothesis.

1.  Hypothesis 1 (Self-efficacy negatively relates to burnout): SUPPORTED

- Strong negative relationship (β = -0.619, p \< 0.001)

- Explains 38.4% of burnout variance

- For each unit increase in self-efficacy, burnout decreases by 1.099 units

- Remains strongest predictor in multiple regression (β = -0.567, p \< 0.001)

2.  Hypothesis 2 (Social media usage positively relates to burnout): SUPPORTED

- Moderate positive relationship (β = 0.334, p = 0.014)

- Explains 11.1% of burnout variance

- For each unit increase in social media use, burnout increases by 0.181 units

- Effect becomes non-significant in multiple regression (β = 0.144, p = 0.219)

3.  Hypothesis 3 (Student employment positively relates to burnout): NOT SUPPORTED

- Weak negative relationship (β = -0.159, p = 0.252)

- Only explains 2.5% of burnout variance

- For each hour worked, burnout decreases by 0.018 units

- Relationship remains non-significant in multiple regression (β = -0.081, p = 0.466)

  - Discuss the implications of the findings for understanding burnout among college students.

    - Self-efficacy emerges as the strongest predictor of student burnout.

    - Social media shows significant impact when examined alone, but less influence when considered alongside other factors

    - Student employment hours don\'t significantly affect burnout levels

    - The combined model (multiple regression) explains 41.2% of burnout variance

    - Academic differences exist, with juniors reporting lowest burnout levels (M = 3.258) compared to freshmen (M = 3.946), sophomores (M = 3.913), and seniors (M = 3.851)

  - Highlight any limitations in the analyses and suggest directions for future research.

> Limitations:

- Small sample of full-time employed students

- Gender was not collected as a demographic variable

- Sample size reduced to 54 after removing incomplete responses

- Study only included employed students

- Cross-sectional design

> Future Research Suggestions:

- Include gender demographics

- Examine both employed and non-employed students

- Investigate why juniors show lower burnout levels

- Consider longitudinal research design

- Study other potential factors affecting student burnout

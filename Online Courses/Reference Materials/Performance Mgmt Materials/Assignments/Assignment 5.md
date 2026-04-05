**Assignment 5**

**PSYC 654 -- Performance Management Systems**

**Using Python to Explore Interrater Reliability and Agreement**

Due to D2L on Wednesday, November 6 @ 9AM

**Objective:**

Explore how interrater reliability and agreement function in performance appraisals. You will calculate metrics like **Cohen's Kappa**, **Intraclass Correlation Coefficient (ICC), and Cronbach's Alpha** using Python and visualize the data to compare results. You will complete coding tasks where indicated and be asked to reflect on how reliability and agreement influence performance evaluations from the output.

**Instructions:**

You may work together for this assignment but need to turn in your own copy. Follow the steps below to calculate the metrics using Python. Make sure to **fill in the code where indicated**.

**[[Part 1: Employee Performance Data]{.underline}]{.mark}**

Below is the dataset for five employees who were rated by three different raters on their teamwork skills. Use this data to complete the Python code in Part 2.

  ---------------------------------------------------------------
  **Employee**    **Rater 1**     **Rater 2**     **Rater 3**
  --------------- --------------- --------------- ---------------
  **A**           5               5               4

  **B**           3               3               4

  **C**           2               2               1

  **D**           4               4               5

  **E**           5               5               5
  ---------------------------------------------------------------

**[Part 2: Calculating Interrater Agreement and Reliability in Python]{.underline}**

Follow the steps below to use Google Colab to calculate Cohen's Kappa, Intraclass Correlation Coefficient (ICC), and Cronbach's Alpha using Python to measure both agreement and reliability. **Make sure the fill in the code where indicated.**

**Step 1: Access Google Colab**

1.  Go to [Google Colab](https://colab.google/).

2.  Click **New Notebook** to create a new notebook.

OR

1.  Download the Assignment 5.ipynb from D2L

2.  Go to [Google Colab](https://colab.google/) and click new notebook like the steps above.

3.  Click File 🡪 upload notebook and browse your computer to upload the Assignment 5.ipynb file you downloaded to run the code included.

**Step 2: Installing and Importing Libraries**

1.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Importing installed packages

!pip install scikit-learn pandas matplotlib seaborn pingouin

import pandas as pd \# Import pandas for data manipulation

import seaborn as sns \# Import seaborn for advanced statistical plotting

import matplotlib.pyplot as plt \# Import matplotlib for general plotting

from sklearn.metrics import cohen_kappa_score \# Import cohen_kappa_score for inter-rater reliability

import pingouin as pg \# Import pingouin for advanced statistical tests 

2.  Press **Shift + Enter** to run the code.

**Step 3: Setting up the Data**

1.  Using the employee performance data provided in **Part 1**, complete the following code by **filling in the missing ratings for Rater 2 and Rater 3**:

\# Data setup: Fill in the ratings for Rater2 and Rater3

data = {

\'Employee\': \[\'A\', \'B\', \'C\', \'D\', \'E\'\],

\'Rater1\': \[5, 3, 2, 4, 5\],

\'Rater2\': \[\_\_, \_\_, \_\_, \_\_, \_\_\], \# \<- Fill in based on the table in Part 1

\'Rater3\': \[\_\_, \_\_, \_\_, \_\_, \_\_\] \# \<- Fill in based on the table in Part 1

}

 

\# Convert to DataFrame

df = pd.DataFrame(data)

df

2.  Run the code to view the data frame of ratings.

**Step 4: Calculate Cohen's Kappa (Interrater Agreement)**

1.  Add the following code to calculate Cohen's Kappa to measure the agreement between 2 raters. You will need to **complete the following code to calculate the agreement between Rater 1 and Rater 2.**

\# Cohen\'s Kappa for Rater1 and Rater2

kappa = cohen_kappa_score(df\[\'\_\_\_\_\'\], df\[\'\_\_\_\_\'\]) \# \<- Fill in the correct columns for Rater1 and Rater2

print(f\"Cohen's Kappa (Rater1 vs Rater2): {kappa}\")

 

2.  Run the code to view the results of the Cohen's Kappa calculation.

> **Interpreting Cohen's Kappa**:\
> Cohen's Kappa measures **interrater agreement** for categorical ratings between two raters, accounting for the agreement that could happen by chance.
>
> **Value Ranges**:

- **Above 0.80**: Almost perfect agreement.

- **0.60 -- 0.80**: Substantial agreement.

- **0.40 -- 0.60**: Moderate agreement.

- **0.20 -- 0.40**: Fair agreement.

- **Below 0.20**: Slight or poor agreement.

> **Key Points**:

- Higher Kappa values indicate that raters tend to assign similar ratings consistently.

- A low Kappa score can indicate poor agreement or that the raters interpret the rating criteria differently.

**Step 5: Visualize the Ratings for Agreement**

1.  Add the following code to create a bar plot to visualize the ratings for each employee by Rater 1, Rater 2, and Rater 3. Make sure to complete the code for the X and Y variables.

\# Bar plot to compare ratings by different raters

df.plot(kind=\'bar\', x=\'\_\_\_\_\', y=\[\'\_\_\_\_\', \'\_\_\_\_\', \'\_\_\_\_\'\], figsize=(8,6)) \# \<- Fill in the correct column names

plt.title(\'Comparison of Employee Ratings by Raters\')

plt.ylabel(\'Rating (1-5)\')

plt.show()

 

2.  Run the code to see the bar chart for interrater agreement.

**Step 6: Calculating Intraclass Correlation Coefficient (ICC)**

1.  Add this code to assess the consistency of ratings of ratings across all three raters, you will calculate **ICC**.

\# Prepare data for ICC calculation

df_melted = pd.melt(df, id_vars=\[\'\_\_\_\_\'\], value_vars=\[\'\_\_\_\_\', \'\_\_\_\_\', \'\_\_\_\_\'\], \# \<- Fill in the correct column names

var_name=\'Rater\', value_name=\'Rating\')

 

\# ICC calculation

icc = pg.intraclass_corr(data=df_melted, targets=\'Employee\', raters=\'Rater\', ratings=\'Rating\')

print(icc)

2.  Run the code to view the results of the ICC calculation.

> **Interpreting the ICC Results**
>
> Your output will show multiple types of ICC values. Here's a guide to what each ICC type means and how to interpret it.

1.  **ICC1 (Single Raters Absolute)**:

    - **Interpretation**: Measures reliability for a single rater. This shows how much of the variance in ratings is due to differences between employees versus random factors.

    - **When to Use**: Use ICC1 if you\'re interested in the reliability of individual raters.

2.  **ICC2 (Single Random Raters)**:

    - **Interpretation**: Assumes raters are randomly selected from a larger population. It evaluates how consistent individual raters are with the others.

    - **When to Use**: Use ICC2 if you want to generalize to a larger population of raters.

3.  **ICC3 (Single Fixed Raters)**:

    - **Interpretation**: Assesses reliability when the raters are fixed (i.e., the specific raters are of interest, not a larger population). It shows consistency within this specific set of raters.

    - **When to Use**: Use ICC3 when you\'re focusing on the specific raters involved, without intending to generalize beyond them.

4.  **ICC1k (Average Raters Absolute)**:

    - **Interpretation**: Similar to ICC1, but it calculates reliability based on the average of all raters\' scores, rather than a single rater.

    - **When to Use**: Use ICC1k if you want to assess how reliable the average of all raters' scores is.

5.  **ICC2k (Average Random Raters)**:

    - **Interpretation**: Measures the reliability of the average ratings from random raters. It assumes raters are randomly selected from a larger pool and calculates the reliability of their combined scores.

    - **When to Use**: Use ICC2k to generalize reliability across a random set of raters.

6.  **ICC3k (Average Fixed Raters)**:

    - **Interpretation**: Assesses the reliability of the average scores of a fixed group of raters. It assumes that the specific raters are of interest.

    - **When to Use**: Use ICC3k if you\'re focused on the combined reliability of these specific raters.

> **Guidelines for ICC Interpretation**

- **ICC Values**:

  - **Above 0.90**: Excellent reliability

  - **0.75 -- 0.90**: Good reliability

  - **0.50 -- 0.75**: Moderate reliability

  - **Below 0.50**: Poor reliability

- **Confidence Interval (CI95%)**: The 95% confidence interval shows the range within which the true ICC value is likely to fall. Narrow confidence intervals indicate more certainty about the ICC estimate, while wider intervals suggest more variability.

**Step 7: Visualizing ICC -- Heatmap of Ratings**

1.  Add this code to visualize the computed ICC to compare the consistency of ratings given by each rater for each employee.

\# Heatmap to visualize rater consistency

sns.heatmap(df\[\[\'\_\_\_\_\', \'\_\_\_\_\', \'\_\_\_\_\'\]\], annot=True, cmap=\"coolwarm\", cbar=True, \# \<- Fill in the correct column names for Rater1, Rater2, and Rater3

xticklabels=\[\'Rater1\', \'Rater2\', \'Rater3\'\], yticklabels=df\[\'Employee\'\])

plt.title(\'Heatmap of Ratings by Raters\')

plt.xlabel(\'Raters\')

plt.ylabel(\'Employees\')

plt.show()

2.  Run the code to see the heatmap for ICC.

**Step 8: Calculating Cronbach's Alpha (Internal Consistency)**

1.  Add this code to calculate Cronbach's Alpha to measure the internal consistency between the rating given by raters.

\# Calculate Cronbach\'s Alpha for the ratings given by Rater1, Rater2, and Rater3

df_ratings = df\[\[\'\_\_\_\_\', \'\_\_\_\_\', \'\_\_\_\_\'\]\] \# \<- Fill in the column names for Rater1, Rater2, and Rater3

cronbach_alpha = pg.cronbach_alpha(data=df_ratings)

print(f\"Cronbach\'s Alpha: {cronbach_alpha\[0\]}\") \# cronbach_alpha returns a tuple with (alpha, CI)

2.  Run the code to view the results of the Cronbach's Alpha calculation.

> **Interpreting Cronbach's Alpha**\
> Cronbach's Alpha measures **internal consistency**, indicating how closely related a set of items (or ratings from different raters) are in assessing the same construct.
>
> **Value Ranges**:

- **Above 0.90**: Excellent internal consistency (ideal for high-stakes assessments, e.g., psychological tests).

- **0.80 -- 0.90**: Good internal consistency (reliable for most purposes).

- **0.70 -- 0.80**: Acceptable internal consistency (suitable for exploratory research).

- **Below 0.70**: Low internal consistency (ratings may not be aligned well).

> **Key Points**:

- Higher values indicate that raters' scores are generally similar and consistently measure the same construct.

- However, very high Alpha scores (e.g., close to 1.0) may also suggest redundancy (items or raters that are too similar or repetitive).

**Step 9: Visualizing Cronbach\'s Alpha -- Box Plot of Rater Scores**

1.  Add this code to visualize the distribution of scores for each rater in a box plot to provide insights into the variability that impacts Cronbach's Alpha.

\# Box plot to visualize rater score distributions

df_ratings = pd.melt(df, id_vars=\[\'Employee\'\], value_vars=\[\'\_\_\_\_\', \'\_\_\_\_\', \'\_\_\_\_\'\], var_name=\'Rater\', value_name=\'Rating\') \# \<- Fill in the column names for Rater1, Rater2, and Rater3

 

sns.boxplot(x=\'Rater\', y=\'Rating\', data=df_ratings)

plt.title(\'Box Plot of Ratings by Each Rater\')

plt.ylabel(\'Rating (1-5)\')

plt.xlabel(\'Raters\')

plt.show()

2.  Run the code to see the box plot of rater scores.

**Step 10: Modifying Data to Observe Effects on Metrics**

1.  In this step, you will **modify Rater 3's ratings** to explore how changing the data affects the calculations of **Cohen's Kappa**, **ICC**, and **Cronbach's Alpha**.

2.  Add the code to modify Rater 3's ratings to all 5's:

\# Modify Rater3\'s ratings to all 5\'s

df\[\'Rater3\'\] = \[5, 5, 5, 5, 5\]

 

\# Re-run Cohen\'s Kappa for Rater1 and Rater3

kappa_13 = cohen_kappa_score(df\[\'Rater1\'\], df\[\'Rater3\'\])

print(f\"Cohen's Kappa (Rater1 vs Rater3): {kappa_13}\")

 

\# Re-run Cronbach\'s Alpha

cronbach_alpha = pg.cronbach_alpha(data=df\[\[\'Rater1\', \'Rater2\', \'Rater3\'\]\])

print(f\"Cronbach\'s Alpha after modification: {cronbach_alpha\[0\]}\")

3.  Reintroduce variability to Rater 3's ratings:

\# Modify Rater3\'s ratings to introduce variability

df\[\'Rater3\'\] = \[4, 5, 2, 5, 5\]

 

\# Re-run Cohen\'s Kappa and Cronbach\'s Alpha

kappa_13 = cohen_kappa_score(df\[\'Rater1\'\], df\[\'Rater3\'\])

print(f\"Cohen's Kappa (Rater1 vs Rater3): {kappa_13}\")

 

cronbach_alpha = pg.cronbach_alpha(data=df\[\[\'Rater1\', \'Rater2\', \'Rater3\'\]\])

print(f\"Cronbach\'s Alpha after introducing variability: {cronbach_alpha\[0\]}\")

**Interpreting the Combined Metrics (Cohen's Kappa, ICC, Cronbach's Alpha)**

- **Cohen's Kappa**: Measures **agreement** between two raters. Focuses on how much raters agree beyond chance.

- **ICC**: Measures **reliability** across multiple raters, looking at both absolute and relative consistency.

- **Cronbach's Alpha**: Measures **internal consistency**, showing how well raters' scores align as a group when measuring the same construct.

**Step 11: Save your Python notebook**

Save your Python notebook by converting it to a PDF with the following steps:

- Go to **File \> Print** in the Colab notebook.

- In the print dialog, select Landscape Layout, click **Save as PDF**

- Submit the **PDF to D2L.**

**[Part 3: Reflection on Results]{.underline}**

1.  What does the **Cohen's Kappa** score tell you about the agreement between Rater 1 and Rater 2? How important is agreement in performance-based decisions?

Write your answer here

2.  How consistent are the raters overall based on the **ICC** results? Would this level of reliability be acceptable in a high-stakes performance review?

Write your answer here

3.  How did changing **Rater 3's ratings** affect **Cronbach's Alpha**? What does this tell you about the internal consistency of the raters' evaluations?

Write your answer here

4.  In what situations would you prioritize **interrater agreement** (Cohen's Kappa) over **reliability** (ICC)? When would **internal consistency** (Cronbach's Alpha) be more important?

Write your answer here

5.  How could **rater training** (e.g., Frame of Reference training) improve interrater agreement and reliability? What impact might it have on the results you observed?

Write your answer here

**[Submission Instructions:]{.underline}**

- **Python Users**: Submit this word document along with the PDF version of your Python notebook.

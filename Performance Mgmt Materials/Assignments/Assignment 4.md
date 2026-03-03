**Assignment 4**

**PSYC 654 -- Performance Management Systems**

**Combining Performance Ratings from 360-Degree Feedback**

Due to D2L on Wednesday, October 22 @ 9AM

**Objective:**

Explore how different methods for combining performance ratings (averaging, summing, normalizing, and weighting) can influence performance evaluation. You will use either Python or Excel to analyze and visualize 360-degree feedback data.

**Instructions:**

You may work together for this assignment but need to turn in a copy each. Follow the steps below to work through the assignment calculations using either Python or Excel.

**[[Part 1: Example 360-Degree Feedback Data]{.underline}]{.mark}**

The employee, Sarah Lee, is a mid-level manager at XYZ Corporation that specializes in providing customer service solutions, who has received 360-degree feedback from her manager, peers, customers, and herself.

  ----------------------------------------------------------------------------------------------------------
  **Dimension**               **Manager Rating**   **Peer Rating**   **Customer Rating**   **Self-Rating**
  --------------------------- -------------------- ----------------- --------------------- -----------------
  **Communication**           4                    3                 5                     4

  **Problem-Solving**         5                    4                 4                     3

  **Teamwork**                3                    5                 N/A                   4

  **Customer Satisfaction**   5                    N/A               5                     4

  **Initiative**              4                    3                 N/A                   5
  ----------------------------------------------------------------------------------------------------------

**[Part 2: Combining Ratings Using Python or Excel Calculations]{.underline}**

You have the option to complete this assignment by coding in Python or performing manual calculations. Follow the steps below for your chosen method.

**[Option 1: Python Walkthrough in Google Colab]{.underline}**

Follow these steps to use Python to analyze the data and create the necessary charts.

**Step 1: Access Google Colab**

1.  Go to [Google Colab](https://colab.google/).

2.  Click **New Notebook** to create a new notebook.

**Step 2: Set Up the Data**

1.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Import necessary libraries

import pandas as pd

import matplotlib.pyplot as plt

 

\# Define the ratings

ratings = {

\'Dimension\': \[\'Communication\', \'Problem-Solving\', \'Teamwork\', \'Customer Satisfaction\', \'Initiative\'\],

\'Manager\': \[4, 5, 3, 5, 4\],

\'Peer\': \[3, 4, 5, None, 3\],

\'Customer\': \[5, 4, None, 5, None\],

\'Self\': \[4, 3, 4, 4, 5\]

}

 

\# Create a DataFrame

df = pd.DataFrame(ratings)

print(\"Original Ratings Data:\")

print(df)

2.  Press **Shift + Enter** to run the code and view the table of ratings.

**Step 3: Calculate Averages**

1.  Add the following code to calculate and display the average ratings:

\# Calculate averages

df\[\'Average\'\] = df\[\[\'Manager\', \'Peer\', \'Customer\', \'Self\'\]\].mean(axis=1)

 

\# Output the numeric average results

print(\"\\nAveraged Ratings:\")

print(df\[\[\'Dimension\', \'Average\'\]\])

 

\# Visualize the averages

plt.bar(df\[\'Dimension\'\], df\[\'Average\'\], color=\'skyblue\')

plt.title(\'Average Performance Ratings\')

plt.xlabel(\'Dimension\')

plt.ylabel(\'Average Rating\')

plt.xticks(rotation=45)

plt.show()

2.  Run the code to view the numeric results and the bar chart of the averages.

**Step 4: Calculate Sums**

1.  Add the following code to calculate and display the sums of the ratings:

\# Calculate sums

df\[\'Sum\'\] = df\[\[\'Manager\', \'Peer\', \'Customer\', \'Self\'\]\].sum(axis=1)

 

\# Output the numeric sum results

print(\"\\nSummed Ratings:\")

print(df\[\[\'Dimension\', \'Sum\'\]\])

 

\# Visualize the sums

plt.bar(df\[\'Dimension\'\], df\[\'Sum\'\], color=\'lightgreen\')

plt.title(\'Summed Performance Ratings\')

plt.xlabel(\'Dimension\')

plt.ylabel(\'Sum of Ratings\')

plt.xticks(rotation=45)

plt.show()

2.  Run the code to view the numeric results and the bar chart of the summed ratings.

**Step 5: Normalize the Scores**

1.  Add the following code to normalize the ratings (convert to percentages) and display the results:

\# Normalize the ratings (convert to percentages)

df_normalized = df\[\[\'Manager\', \'Peer\', \'Customer\', \'Self\'\]\].apply(lambda x: (x / 5) \* 100)

 

\# Calculate the average normalized score

df\[\'Normalized\'\] = df_normalized.mean(axis=1)

 

\# Output the numeric normalized results

print(\"\\nNormalized Ratings (in Percentage):\")

print(df\[\[\'Dimension\', \'Normalized\'\]\])

 

\# Visualize the normalized scores

plt.bar(df\[\'Dimension\'\], df\[\'Normalized\'\], color=\'salmon\')

plt.title(\'Normalized Performance Ratings (Percentage)\')

plt.xlabel(\'Dimension\')

plt.ylabel(\'Normalized Rating (%)\')

plt.xticks(rotation=45)

plt.show()

2.  Run the code to see the numeric results and the bar chart of the normalized ratings.

**Step 6: Weighted Ratings**

1.  Add this code to calculate the weighted average based on assigned weights:

\# Define weights for each dimension (must add up to 1)

weights = {

\'Communication\': 0.15,

\'Problem-Solving\': 0.25,

\'Teamwork\': 0.10,

\'Customer Satisfaction\': 0.35,

\'Initiative\': 0.15

}

 

\# Multiply the normalized ratings by the corresponding weight

df\[\'Weighted\'\] = df.apply(lambda row: row\[\'Normalized\'\] \* weights\[row\[\'Dimension\'\]\], axis=1)

 

\# Output the weighted ratings

print(\"\\nWeighted Ratings (Based on Assigned Weights):\")

print(df\[\[\'Dimension\', \'Weighted\'\]\])

 

\# Visualize the weighted ratings

plt.bar(df\[\'Dimension\'\], df\[\'Weighted\'\], color=\'purple\')

plt.title(\'Weighted Performance Ratings\')

plt.xlabel(\'Dimension\')

plt.ylabel(\'Weighted Rating\')

plt.xticks(rotation=45)

plt.show()

2.  Run the code to view the weighted results and chart.

**Step 6: Save your Python notebook**

Save your Python notebook by converting it to a PDF with the following steps:

- Go to **File \> Print** in the Colab notebook.

- In the print dialog, select Landscape Layout, click **Save as PDF**.

**Step 7: Insert Your Calculations and Graphs Below**

After running the code for each method (averaging, summing, normalizing, and weighting), input your results in the table provided and paste the bar charts directly into this document.

**[Option 2: Excel Walkthrough]{.underline}**

If you prefer manual calculations using **Excel**, follow these steps.

**Step 1: Input the Data into Excel**

1.  Open **Excel** or **Google Sheets**.

2.  Enter the employee ratings into a spreadsheet as shown in Part 1 of the assignment.

**Step 2: Calculate Averages, Sums, and Normalized Ratings**

1.  **Averages**:

    - In a new column, use the formula =AVERAGE(B2:E2) to calculate the average for each dimension.

    - Copy this formula down for all rows.

2.  **Sums**:

    - In another new column, use the formula =SUM(B2:E2) to calculate the sum for each dimension.

    - Copy this formula down for all rows.

3.  **Normalized Ratings**:

    - Convert each score to a percentage: =B2/5\*100 for each dimension.

    - Copy this formula down for all rows and across the columns for Manager, Peer, Customer, and Self ratings.

    - This will normalize scores for all sources. To get weighted ratings, for the final table, you will need to average across dimensions for a **single column of normalized scores.**

4.  **Averaging the Normalized Ratings**

    - In a new column, calculate the average of the normalized ratings across the row for every dimension. That is, you will average the ratings for each dimension for the Manager, Peer, Customer, and Self ratings. Use the formula Average (F2:I2) for communication, for example.

**Step 3: Weight the Ratings**

1.  Assign weights to each dimension, depending on its importance to the organization:

    - **Communication**: 15%

    - **Problem-Solving**: 25%

    - **Teamwork**: 10%

    - **Customer Satisfaction**: 35%

    - **Initiative**: 15%

2.  Multiply the **averaged scores** by the weights using the formula =F2\*0.15, adjusting weights for each dimension.

**Step 4: Create Bar Charts**

1.  Highlight the calculated averages, sums, normalized, or weighted ratings.

2.  Go to **Insert** \> **Bar Chart** to generate a chart.

3.  Customize the chart by adding titles and labeling the axes.

4.  Repeat for each type of rating.

**Step 5: Insert Your Calculations and Graphs Below**

After running the code for each method (averaging, summing, normalizing, and weighting), input your results in the table provided and paste the bar charts directly into this document.

**Step 6: Save your Excel notebook**

Save your Excel notebook file to submit to D2L

**[Part 3: Input Final Calculation Results]{.underline}**

Add your calculated results into the final calculations table below. Also, copy and paste your graphs below.

**Final Calculations Table**

  -----------------------------------------------------------------------------------------------------------------------
  **Dimension**               **Average Rating**   **Sum of Ratings**   **Normalized Rating (%)**   **Weighted Rating**
  --------------------------- -------------------- -------------------- --------------------------- ---------------------
  **Communication**                                                                                 

  **Problem-Solving**                                                                               

  **Teamwork**                                                                                      

  **Customer Satisfaction**                                                                         

  **Initiative**                                                                                    
  -----------------------------------------------------------------------------------------------------------------------

**Insert Graphs:**

**Graph for Average Ratings**:\
\[Insert your graph here\]

**Graph for Summed Ratings**:\
\[Insert your graph here\]

**Graph for Normalized Ratings**:\
\[Insert your graph here\]

**Graph for Weighted Ratings**:\
\[Insert your graph here\]

**[Part 4: Reflection on Results]{.underline}**

Reflect on your findings and answer the following questions. Your answers should be based on the analysis you completed in Part 2.

1.  **Comparison of Methods**:

    - How do the performance scores differ between averaging, summing, normalizing, and weighting?

> Write your answer here

- Which method provides the most accurate or fair representation of Sarah's performance, and why?

> Write your answer here

2.  **Practical Application**:

    - Consider XYZ Corporation's priority of customer satisfaction. How does weighting certain dimensions more heavily impact performance evaluations? Would weighting be beneficial to the organization?

> Write your answer here

3.  **Addressing Biases**:

    - How do differences in ratings from various sources (Manager, Peer, Customer, Self) impact the final results?

> Write your answer here

- How does combining these ratings reduce potential biases (e.g., self-rating inflation, peer leniency)?

> Write your answer here

**[Part 5: Recommendations]{.underline}**

Based on your analysis and reflection, provide a short recommendation on the best method for combining 360-degree feedback ratings for Sarah Lee. Consider whether weighing should be used and justify your recommendation by considering both fairness and alignment with XYZ Corporation's performance goals (e.g., employee development, customer satisfaction).

Write your answer here

**[Submission Instructions:]{.underline}**

- **Python Users**: Submit this word document with the table filled in and bar charts inserted, along with the PDF version of your Python notebook.

- **Excel Users**: Submit this document with the table filled in and bar charts inserted, along with the Excel file (or Google Sheets).

**Assignment 2**

**PSYC 650 -- Organizational Psychology**

**Intro to Python for Behavioral Data**

Due to D2L on Wednesday, September 24 @ 9AM

**Objective:**

You will practice Python coding and data analysis in a Jupyter notebook environment using **Google Colab**. This assignment covers: variables & lists, functions, creating and summarizing a dataset with 'pandas', and simple visualizations with 'matplotlib'.

You will download the provided **Intro_to_Python.ipynb** notebook and the dataset **IBM HR.csv**, open the notebook in Colab, and complete the marked **Task** cells. You will also answer short reflection questions at the end of this document.

**Instructions:**

You may work together for this assignment but need to turn in your own PDF as indicated at the end of the assignment.

**[Download the Files]{.underline}**

1.  Go to the course site on D2L.

2.  Download both files:

- **Intro_to_Python.ipynb**

- **IBM HR.csv**

**[Part 1: Open the Notebook in Google Colab]{.underline}**

1.  Go to <https://colab.research.google.com>.

2.  On the welcome screen, click the **Upload** tab.

3.  Upload **Intro_to_Python.ipynb**.

4.  Colab will open the notebook in your browser.

5.  Rename the notebook: **LastName_FirstName_Assignment2.ipynb**

**[Part 2: Loading Libraries and the Data]{.underline}**

**[2.1 Loading Libraries]{.underline}**

1\. Locate the code cell in the notebook marked for 2.2 loading libraries.

2\. Run the cell with code indicated below to load the required libraries:

import pandas as pd

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

**[2.2 Uploading and Loading the Dataset]{.underline}**

1.  In Colab, go to the left sidebar (**folder icon**).

2.  Click the **Upload** button and select **IBM HR.csv** from your computer.

- You should now see the file listed in your Colab environment under /content.

3.  In the notebook, find the cell marked:

data = pd.read_csv(\'/content/IBM HR.csv\')

4.  Press **Shift + Enter** to run the code.

**[Part 4: Working Through the Notebook]{.underline}**

1.  The notebook is divided into sections:

    - Basic Data Analysis

    - Creating a Correlation Table

    - Data Manipulation and New DataFrame Creation

    - Data Visualization

    - Saving your Notebook as a PDF

<!-- -->

1.  In each section, look for **Task** details to respond to questions marked **Answer** or to run the code and understand what the code does.

2.  Continue this process until you reach the end of the code and all tasks are completed.

3.  Make sure to follow the step to download your notebook as a PDF to submit to D2L along with this word document with your responses to the questions in the next part.

**ANSWERS:**

**Part 4: Basic Data Analysis**

**4.1 Displaying the First Few Rows**

- Code:

- data.head()

- Expected: First 5 rows of the IBM HR dataset (columns like *Age, Attrition, BusinessTravel, DailyRate, Department,* etc.).

**4.2 Looking at Data Details**

- Code:

- print(data.shape)

- Expected Output:

- (1470, 35)

- **Answer:** The dataset has **1470 rows** and **35 columns**.

**4.3 Summary Statistics**

- Code:

- data.describe()

- Expected: Descriptive statistics (count, mean, std, min, 25%, 50%, 75%, max) for numeric columns.

- **Answer (example):** *The average age of employees in the dataset is about 37 years.*

**4.4 Identify Missing Values**

- Code:

- data.isnull().sum()

- Expected Output: All columns show 0.

- **Answer:** The dataset contains **no missing values**.

**Part 5: Creating a Correlation Table**

**5.1 Correlation Table**

- Code:

- corr = data.corr(numeric_only=True)

- corr

- Expected: Correlation values between numeric variables.

- **Answer (example):** *MonthlyIncome and JobLevel have a notably high positive correlation (around 0.95).*

**5.2 Heatmap**

- Code:

- sns.heatmap(corr, annot=True, cmap=\'coolwarm\')

- plt.show()

- Expected: A heatmap showing strong positive correlations (e.g., JobLevel & MonthlyIncome) and weak ones elsewhere.

**Part 6: Data Manipulation**

**6.1 Selecting Specific Columns**

- Code:

- job_related_df = data\[\[\'EmployeeNumber\', \'JobSatisfaction\', \'PerformanceRating\'\]\]

- job_related_df.head()

- Expected: New DataFrame with 3 columns.

**6.2 Filtering Rows**

- Code:

- high_satisfaction_df = data\[data\[\'JobSatisfaction\'\] \> 3\]

- high_satisfaction_df.head()

- Expected: Subset of employees with JobSatisfaction = 4 (the highest rating).

**6.3 Merging DataFrames**

- Code:

- merged_df = pd.merge(job_related_df, high_satisfaction_df, on=\'EmployeeNumber\', how=\'inner\')

- merged_df.head()

- Expected: New DataFrame containing only employees with JobSatisfaction \> 3, keeping job satisfaction and performance columns.

**Part 7: Data Visualization**

**7.1 Scatter Plot**

- Code:

- sns.scatterplot(x=\'YearsAtCompany\', y=\'MonthlyIncome\', hue=\'Attrition\', data=data)

- plt.title(\'Monthly Income vs. Years at Company\')

- plt.show()

- Expected: Scatter plot with upward trend (income increases with years at company).

- **Answer:** *Employees with more years at the company tend to have higher monthly income. Attrition seems more common among those with lower income and fewer years of service.*

**7.2 Bar Plot of Attrition Rates**

- Code:

- sns.countplot(x=\'Attrition\', data=data)

- plt.title(\'Attrition Rates\')

- plt.show()

- Expected: Bar plot showing many more "No" than "Yes".

- **Answer:** *Attrition is relatively low --- most employees have not left the company.*

**7.3 Histogram of Monthly Income by Attrition**

- Code:

- sns.histplot(data=data, x=\'MonthlyIncome\', hue=\'Attrition\', element=\'step\', stat=\'probability\', common_norm=False)

- plt.title(\'Distribution of Monthly Income by Attrition\')

- plt.show()

- Expected: Histogram with overlapping distributions; employees who left ("Yes") skew toward lower monthly income ranges.

- **Answer:** *Employees who left the company tended to have lower monthly incomes compared to those who stayed.*

**[Part 5: Reflection Questions]{.underline}**

After completing the notebook tasks in Google Colab, answer these questions in this word document.

1.  What part of working in Colab felt easiest? What part was the most confusing?

    - Running code cells and immediately seeing the outputs was the easiest part. The most confusing part was uploading the dataset and making sure the file path matched correctly in the code.

2.  Did you encounter any errors while completing the notebook? If so, how did you solve them (or how could you solve them if you had more time)?

    - A common error was a FileNotFoundError when trying to load *IBM HR.csv*. This was solved by double-checking the filename and ensuring the file was uploaded into the Colab session. Another possible error was missing the seaborn package, which could be fixed with !pip install seaborn.

3.  Based on your descriptive statistics and plots, what is one interesting pattern you noticed in the IBM HR dataset?

    - Employees who left the company ("Attrition = Yes") tended to have lower monthly income and fewer years at the company compared to those who stayed. The attrition bar chart also showed that the majority of employees did not leave, but turnover was concentrated in certain groups.

4.  How could HR professionals use data like this (age, job role, attrition, etc.) to make organizational decisions? What ethical considerations should they keep in mind?

    - HR professionals could use this data to identify risk factors for attrition and improve retention strategies, such as adjusting pay or addressing job dissatisfaction. Ethically, they must ensure that data is not used to unfairly target or discriminate against specific groups, and they must protect employee privacy when analyzing and reporting results.

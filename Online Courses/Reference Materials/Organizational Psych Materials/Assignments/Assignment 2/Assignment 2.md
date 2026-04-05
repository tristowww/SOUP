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

**[Part 5: Reflection Questions]{.underline}**

After completing the notebook tasks in Google Colab, answer these questions in this word document.

1.  What part of working in Colab felt easiest? What part was the most confusing?

2.  Did you encounter any errors while completing the notebook? If so, how did you solve them (or how could you solve them if you had more time)?

3.  Based on your descriptive statistics and plots, what is one interesting pattern you noticed in the IBM HR dataset?

4.  How could HR professionals use data like this (age, job role, attrition, etc.) to make organizational decisions? What ethical considerations should they keep in mind?

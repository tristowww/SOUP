# **Assignment 2: Introduction to Data Analysis using Python in Google Colab**
###Objectives:

*   To familiarize yourself with Google Colab
*   Learn how to load Python libraries
*   Upload data
*   Perform basic data analysis

# **Part 1: Introduction**
##1.1 What is Google Colab?
Google Colab is a cloud-based platform that allows you to write and execute Python code through your browser. It offers free CPU and GPU resources. It acts as an environment to run Python code for data anylsis and many other uses.

##1.2 What is Python?
Python is a versatile programming language that is known for its popularity and readabiliy. With its ease of use, it is widely used for data analysis, web development, scientific computing, artificial intelligence, and more.

# **Part 2: Setting up the Google Colab Notebook**
##2.1 Open Google Colab
Navigate to Google Colab and start a new notebook.

From here you can upload a preexisting notebook or .ipynb file by clicking "File", "Open Notebook", "Upload", and "Choose File" to find a file on your computer if you already have code written or saved.

##2.2 Loading Libraries
In this sectiton, you will learn how to import necessary libraries to your Colab environmnet. Python libraries are a collection of functions and methods that are already written and allow you to perform many actions without writing your own code from scratch.


##**Task:**
Import the Pandas and NumPy libraries, as well as matplotlib and seaborn for data vizualization using the following code below. Execute each cell by pressing "Ctrl+Enter" or clicking the "play" button.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

# **Part 3: Loading the Data**

##3.1 Downloading and Loading Data

##**Task:**
Download and load the data from D2L labeled "IBM HR" and upload it to your Google Colab environment by clicking on the file icon on the left and then choosing "upload to session storage".

After uploading the dataset, read the data into a pandas DataFrame using the following code.

```python
data = pd.read_csv('/content/IBM HR.csv')
```

# **Part 4: Basic Data Analysis**

##4.1 Displaying the First Few Rows of the Data

##**Task:**
Use the **'head()'** function to display the first few rows of the data.

```python
data.head()
```

##4.2 Looking at Data Details

##**Task:**
Run the following code to check how many rows of data are in the IBM dataset.

##**Answer:**
Double click on this cell of text to input your answer to the following prompt below.

How many rows of data are there?:


```python
print(data.shape)
```

##4.3 Summary Statistics

##**Task:**
Use the **'describe()'** function to get the summary statsitcs of the data.

##**Answer:**
Double click on this cell of text to input your answer to the following prompt below.

Report one summary statistic from the data in a sentence:

```python
data.describe()
```

##4.4 Identify Missing Values

##**Task:**
Use the **'isnull().sum()'** function to identify missing values in each column.

##**Answer:**
Double click on this cell of text to input your answer to the following prompt below.

Does that dataset contain any missing values?:

```python
data.isnull().sum()
```

# **Part 5: Creating a Correlation Table**
##5.1 Create a Numeric Correlation Table
Now, you will create a correlation table to analze the relationships betweeen different variables in the dataset.

##**Task:**
Create a correlation table using the **'corr()'** method.

##**Answer:**
Double click on this cell of text to input your answer to the following prompt below.

What is a noteably high correlation?:

```python
corr = data.corr(numeric_only=True)
corr
```

##5.2 Display the Correlations as a Heatmap
We can download additional libraries to create a heatmap visualization of the correlattion table.

##**Task:**
Create a correlation heatmap using the seaborn library.

```python
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
```

# **Part 6: Data Manipulation and New DataFrame Creation**
##6.1 Selecting Specific Columns
We can also choose to select specific columns or variables out of the data to create a smaller DataFrame.

##**Task:**
Create a new DataFrame containing only the columns related to job satisfaction and performance.



```python
job_related_df = data[['EmployeeNumber', 'JobSatisfaction', 'PerformanceRating']]
job_related_df
```

##6.2 Filtering Rows Based on a Condition

##**Task:**
Create a new DataFrame containing only the rows where the job satisfaction rating is greater than 3. We will name this DataFrame high_satisfaction_df.



```python
high_satisfaction_df = data[data['JobSatisfaction'] > 3]
high_satisfaction_df.head()
```

##6.3 Merging DataFrames

##**Task:**
Create a new DataFrame by merging job_related_df and high_satisfaction_df based on a common column (EmployeeNumber). Use an inner join to merge the DataFrames.


```python
merged_df = pd.merge(job_related_df, high_satisfaction_df, on='EmployeeNumber', how='inner')
merged_df.head()
```

# **Part 7: Data Visualization**
##7.1 Scatter Plot of Monthly Income vs. Years at Company
Creating a visualization of the relationship between variables can help provide insights.

##**Task:**
Create a scatter plot to visualize the relationship between the variables'MonthlyIncome' and 'YearsAtCompany'.

##**Answer:**
Double click on this cell of text to input your answer to the following prompt below.

What is an observation you can make from the data visualizaiton?:

```python
sns.scatterplot(x='YearsAtCompany', y='MonthlyIncome', hue='Attrition', data=data)
plt.title('Monthly Income vs. Years at Company')
plt.xlabel('Years at Company')
plt.ylabel('Monthly Income')
plt.show()
```

##7.2 Bar Plot of Attrition Rates
Creating a visualization of the relationship between variables can help provide insights.

##**Task:**
Create a bar plot showing atttrition rates (Yes/No).

##**Answer:**
Double click on this cell of text to input your answer to the following prompt below.

What is an observation you can make from the data visualizaiton?:

```python
sns.countplot(x='Attrition', data=data)
plt.title('Attrition Rates')
plt.show()
```

##7.3 Histogram of Monthly Income and Attrition
Creating a visualization of the relationship between variables can help provide insights.

##**Task:**
Visualize the distribution of 'MonthlyIncome' using a histogram. Further, break it down based on 'Attrition' to see if there's any pattern.

##**Answer:**
Double click on this cell of text to input your answer to the following prompt below.

What is an observation you can make from the data visualizaiton?:

```python
sns.histplot(data=data, x='MonthlyIncome', hue='Attrition', element='step', stat='probability', common_norm=False)
plt.title('Distribution of Monthly Income by Attrition')
plt.show()
```

# **Part 8: Saving your Notebook as A PDF**
Save your notebook with your output.

##**Task:**
Before you submit your assignment, you need to save your notebook as a PDF document.

To do so, go to "file", click "print" and once a new window comes up, select the option to save as a pdf.

Upload this pdf to Assigment 1 in D2L.


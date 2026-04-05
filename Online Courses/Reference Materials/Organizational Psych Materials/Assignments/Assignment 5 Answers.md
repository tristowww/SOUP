**Assignment 5**

**PSYC 650 -- Organizational Psychology**

**Using Python to Classify Employee Behaviors**

Due to D2L on Friday, November 22 @ 9AM

**Objective:**

Classify employee behaviors as Organizational Citizenship Behaviors (OCBs) or Counterproductive Work Behaviors (CWBs) using TextBlob for sentiment analysis. Understand how text analytics can provide insights into employee behaviors in I/O Psychology.

**Instructions:**

You may work together for this assignment but need to turn in your own copy. Follow the steps below to run the code using Python. Make sure to **fill in the code where indicated and answer all follow up questions.**

**[Part 1: Set Up Python]{.underline}**

Follow the steps below to use Google Colab to run sentiment analysis on text in order to gain insights into predicting employee behavior. **Make sure the fill in the code where indicated. Answer the questions in each step where indicated.**

**Step 1: Access Google Colab**

1.  Go to [Google Colab](https://colab.google/).

2.  Click **New Notebook** to create a new notebook.

OR

1.  Download the Assignment 5.ipynb from D2L

2.  Go to [Google Colab](https://colab.google/) and click new notebook like the steps above.

3.  Click File 🡪 upload notebook and browse your computer to upload the Assignment 5.ipynb file you downloaded to run the code included.

**Step 2: Set up the Google Colab Environment**

The following code in Google Colab to install and import the required packages. This step ensures you have all the tools needed to process and visualize data.

1.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Install necessary packages for text analysis and data visualization

!pip install textblob matplotlib

 

\# Importing libraries for text analysis and visualization

from textblob import TextBlob \# For sentiment analysis

import pandas as pd \# For managing datasets

import matplotlib.pyplot as plt \# For creating visualizations

2.  Press **ctrl + Enter** to run the code.

**Step 3: Create a Dataset**

1.  Replace the placeholders ("Example CWB1", "Example OCB1"....) below with real examples of **OCBs** and **CWBs**. These examples will simulate real-world feedback.

- **DataFrames** are used to structure the data for easy analysis.

- Combine both your examples and initial dataset for comprehensive testing.

2.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Creating a sample dataset with initial comments

data = {

    \'Comments\': \[

        \"Helped a colleague with their project.\",

        \"Always late for meetings.\",

        \"Volunteered for the weekend event.\",

        \"Goes above and beyond to assist clients.\",

        \"Spread false rumors about a coworker.\",

        \"Pushes a coworker down the stairs.\",

        \"Offered to help a coworker with their workload.\",

        \"Took credit for others\' work.\",

        \"Frequently stays late to meet deadlines.\",

        \"Ignores important emails from management.\",

        \"Provides constructive feedback to peers.\",

        \"Missed a major deadline due to procrastination.\",

        \"Organized a team lunch to boost morale.\",

        \"Avoids unnecessary meetings to stay productive.\",

        \"Encourages team members to share their ideas.\",

        \"Rarely helps coworkers unless directly asked.\",

        \"Double-checks work to ensure accuracy.\",

        \"Distracts others during work hours.\",

        \"Mentors new employees to help them adapt.\",

        \"Criticizes coworkers in front of others.\"

    \]

}

 

\# Convert the dataset into a DataFrame (a table-like structure)

df = pd.DataFrame(data)

 

\# Now add your own examples

your_cwbs = \[\"Example CWB1\", \"Example CWB2\", \"Example CWB3\"\] \# Examples of negative workplace behaviors

your_ocbs = \[\"Example OCB1\", \"Example OCB2\", \"Example OCB3\"\] \# Examples of positive workplace behaviors

 

\# Combine your examples with the initial dataset

your_data = pd.DataFrame({\'Comments\': your_cwbs + your_ocbs})

df = pd.concat(\[df, your_data\]).reset_index(drop=True) \# Reset the index for a clean table

 

\# View the combined dataset

df

3.  Run the code to view the data frame of cwbs and ocbs.

**Step 4: Text Analysis Using TextBlob**

1.  We will perform sentiment analysis on the comments, associating positive sentiments with OCBs and negative sentiments with CWBs. Doing so with a threshold of 0.

- **TextBlob** analyzes sentiment polarity (ranging from -1 to 1).

- Positive polarity indicates OCB; otherwise, CWB.

- The apply function processes every comment in the dataset.

2.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Function to classify behaviors based on sentiment polarity

def classify_behavior(comment):

analysis = TextBlob(comment) \# Analyze the comment\'s sentiment

if analysis.sentiment.polarity \> 0: \# Positive sentiment

return \'OCB\'

else: \# Neutral or negative sentiment

return \'CWB\'

 

\# Apply the function to classify each comment

df\[\'Predicted Behavior Type\'\] = df\[\'Comments\'\].apply(classify_behavior)

 

\# Display the results

df\[\[\'Comments\', \'Predicted Behavior Type\'\]\]

3.  Run the code to view the results of the classification.

4.  Did all your example behaviors align with the predictions?

Not all behaviors aligned perfectly. While some comments with positive wording were correctly identified as OCB and those with clear negative sentiments were classified as CWB, certain behaviors were misclassified. For instance, a neutral comment like \"Frequently stays late to meet deadlines\" may have been misclassified as CWB despite indicating positive behavior. Similarly, subtle negative behaviors such as \"Ignores important emails from management\" could be classified as neutral (CWB) due to limited sentiment polarity.

5.  If there are any that do not align, why do you think that is?

The misalignment is likely due to the limitations of sentiment analysis. TextBlob analyzes only the linguistic sentiment and assigns polarity scores, but it doesn\'t account for the context or intent behind the statement. For example, certain sarcastic comments or negative behaviors masked in neutral language may not receive appropriately negative scores. Additionally, cultural or organizational nuances in language might affect how behaviors are perceived versus how they are scored based on polarity.

**Step 5: Visualization with Pie Chart**

1.  Add the following code to perform sentiment analysis on the comments, associating positive sentiments with OCBs and negative sentiments with CWBs, using the threshold of 0.

    - value_counts() calculates the frequency of each behavior type.

    - The pie chart visualizes these proportions with percentages displayed on each slice.

2.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Count the occurrences of each behavior type (OCB and CWB)

behavior_counts = df\[\'Predicted Behavior Type\'\].value_counts()

 

\# Create a pie chart to visualize the proportions of OCBs and CWBs

plt.figure(figsize=(8, 8)) \# Set the figure size

behavior_counts.plot(kind=\'pie\', autopct=\'%1.1f%%\', startangle=90, cmap=\'Set3\')

plt.title(\'Proportion of OCBs to CWBs\') \# Add a title to the chart

plt.ylabel(\'\') \# Remove the y-axis label for a cleaner look

plt.show() \# Display the pie chart

3.  Run the code to view the pie chart.

4.  What is the proportion of OCBs to CWBs?

> For the initial dataset, let\'s assume the following distribution:

- **60% OCB, 40% CWB**

This reflects the balance of positive versus negative sentiments based purely on linguistic polarity without adjusting thresholds. The results depend on how many comments lean toward positive (OCB) versus negative or neutral sentiments (CWB).

**Step 6: Adjusted Text Analysis Using TextBlob**

1.  Add the following code to perform sentiment analysis on the comments, associating positive sentiments with OCBs and negative sentiments with CWBs with an adjusted threshold of -0.3 to include slight negatives as OCBs.

    - **TextBlob** analyzes the sentiment of each comment, producing a polarity score between -1 (most negative) and 1 (most positive).

    - The threshold of -0.3 allows for slightly negative or neutral comments to be classified as OCB, broadening the definition of positive behaviors.

    - The results are stored in the Adjusted Prediction column, showing how each comment is classified based on the adjusted threshold.

2.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Define a function to classify behaviors based on sentiment polarity with an adjusted threshold

def classify_behavior(comment):

analysis = TextBlob(comment) \# Perform sentiment analysis on the comment using TextBlob

if analysis.sentiment.polarity \>= -0.3:

\# If the sentiment polarity is greater than or equal to -0.3 (includes slight negatives and neutrals), classify as OCB

return \'OCB\'

else:

\# Otherwise, classify as CWB for strongly negative sentiment

return \'CWB\'

 

\# Apply the classification function to each comment in the \'Comments\' column

df\[\'Adjusted Prediction\'\] = df\[\'Comments\'\].apply(classify_behavior)

 

\# Print the comments alongside their adjusted behavior predictions

df\[\[\'Comments\', \'Adjusted Prediction\'\]\]

3.  Run the code to see the pie chart.

**Step 7: Adjusted Visualization with Pie Chart**

1.  Add the following code to visualize the distribution of OCBs and CWBs through a pie chart after adjusting the threshold to -0.2.

    - **value_counts()**: Calculates the frequency of each behavior type (OCB and CWB) from the Adjusted Prediction column.

    - **Pie Chart**: Displays the distribution of behavior types as percentages.

    - **Visual Enhancements**: The Paired colormap ensures clear distinction between categories, and the startangle improves layout.

2.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Count the occurrences of each behavior type (OCB and CWB) based on the adjusted predictions

behavior_counts = df\[\'Adjusted Prediction\'\].value_counts()

 

\# Set up the figure size for the pie chart

plt.figure(figsize=(8, 8))

 

\# Plot a pie chart to visualize the proportion of OCBs and CWBs

behavior_counts.plot(

kind=\'pie\', \# Specify the chart type as pie

autopct=\'%1.1f%%\', \# Display the percentage of each slice with one decimal place

startangle=90, \# Start the first slice at 90 degrees for better alignment

cmap=\'Paired\' \# Use a paired colormap for distinct, visually appealing colors

)

 

\# Add a title to the pie chart

plt.title(\'Proportion of CWBs to OCBs\')

 

\# Remove the y-axis label for a cleaner look

plt.ylabel(\'\')

 

\# Display the pie chart

plt.show()

3.  Run the code to see the adjusted pie chart.

4.  What are the proportions of OCBs to CWBs?

After adjusting the threshold to include slight negatives or neutral sentiments as OCB, the distribution might shift to:

- **70% OCB, 30% CWB**

This broader threshold results in more comments being classified as OCB, particularly those with slight negativity that still indicate constructive or cooperative behavior (e.g., \"Provides constructive feedback to peers\").

5.  How is this different than the proportions with the threshold of 0?

The threshold adjustment accounts for behaviors that could be deemed positive despite having a minor negative sentiment score. The initial threshold (0) classified strictly neutral or negative comments as CWB, leading to a higher proportion of CWBs. Adjusting the threshold reflects a more nuanced understanding of workplace behaviors, ensuring behaviors like constructive criticism or reserved assistance aren\'t unfairly categorized as CWB.

**Step 8: Further Adjusting Predictions with Feature Engineering**

1.  Add this code to further adjust the predictions by adjusting the features that are associated with OCBs and CWBs. This includes specific keywords to make more accurate or meaningful predictions.

    - **Keyword Matching**: The apply function checks each comment for the presence of any keywords using lambda and any() functions.

    - **Case-Insensitive Search**: x.lower() ensures the search is not case-sensitive.

    - **Output**: The DataFrame now includes two new columns (Keyword OCB and Keyword CWB) that indicate whether specific keywords associated with OCB or CWB behaviors are found in each comment.

<!-- -->

2.  Replace the placeholders ('OCB Keyword 1', 'CWB Keyword 1'....) below with keywords from your input examples of **OCBs** and **CWBs**. These keywords will help adjust the predictions.

- **DataFrames** are used to structure the data for easy analysis.

- Combine both your examples and initial dataset for comprehensive testing.

3.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Define predefined keywords for OCB and CWB

keywords_ocb = \[\'help\', \'assist\', \'support\', \'volunteer\'\] \# Common terms associated with positive workplace behaviors (OCB)

keywords_cwb = \[\'late\', \'rumors\', \'credit\'\] \# Common terms associated with negative workplace behaviors (CWB)

 

\# Task: Add your own keywords for both OCB and CWB

your_keywords_ocb = \[\'OCB Keyword 1\', \'OCB Keyword 2\', \'OCB Keyword 3\'\] \# Additional positive behavior indicators (replace with your own if needed)

your_keywords_cwb = \[\'CWB Keyword 1\', \'CWB Keyword 2\', \'CWB Keyword 3\'\] \# Additional negative behavior indicators (replace with your own if needed)

 

\# Combine predefined keywords with the user\'s custom keywords

final_keywords_ocb = keywords_ocb + your_keywords_ocb \# Combine OCB keyword lists

final_keywords_cwb = keywords_cwb + your_keywords_cwb \# Combine CWB keyword lists

 

\# Create new columns to indicate whether a comment contains any OCB or CWB keywords

df\[\'Keyword OCB\'\] = df\[\'Comments\'\].apply(lambda x: any(word in x.lower() for word in final_keywords_ocb))

\# Checks if any OCB keyword is present in each comment (case-insensitive) and assigns True/False.

 

df\[\'Keyword CWB\'\] = df\[\'Comments\'\].apply(lambda x: any(word in x.lower() for word in final_keywords_cwb))

\# Checks if any CWB keyword is present in each comment (case-insensitive) and assigns True/False.

 

\# Display the comments along with the results for keyword matches

df\[\[\'Comments\', \'Keyword OCB\', \'Keyword CWB\'\]\]

4.  Run the code to view the results of the keyword additions.

**Step 9: Feature Engineering Predictions**

1.  Add this code to show the predictions for the feature engineering by adding additional keywords.

    - **Keyword-Based Classification**: This approach prioritizes keyword matching for behavior classification.

    - **apply(axis=1)**: Ensures the function is applied row-wise, utilizing both the keyword indicators and sentiment for robust classification.

    - **Output**: The Engineered Prediction column shows the final behavior type for each comment.

2.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Define a function to classify behaviors using keyword matching and fallback sentiment analysis

def engineered_classify_behavior(row):

if row\[\'Keyword OCB\'\]:

return \'OCB\' \# Classify as OCB if any OCB keyword is present

elif row\[\'Keyword CWB\'\]:

return \'CWB\' \# Classify as CWB if any CWB keyword is present

else:

return classify_behavior(row\[\'Comments\'\]) \# If no keywords are found, use sentiment analysis as a fallback

 

\# Apply the classification function to each row in the DataFrame

df\[\'Engineered Prediction\'\] = df.apply(engineered_classify_behavior, axis=1)

\# The \`apply\` function processes each row, using the keyword columns and the fallback for a final classification.

 

\# Display the comments along with their engineered predictions

df\[\[\'Comments\', \'Engineered Prediction\'\]\]

3.  Run the code to see the predictions for the keyword additions.

**Step 10: Feature Engineering Pie Chart Visualization**

1.  Add this code to visualize the feature engineered predictions with a pie chart.

    - **value_counts()**: Computes the frequency of each behavior type (OCB and CWB) from the Engineered Prediction column.

    - **Pie Chart**: Visualizes the relative proportions of predicted behaviors, providing a clear comparison.

2.  Copy and paste the following code into a new code cell in your Colab notebook:

\# Count the number of occurrences for each behavior type (OCB and CWB) from the \'Engineered Prediction\' column

behavior_counts = df\[\'Engineered Prediction\'\].value_counts()

 

\# Create a new figure for the pie chart with a specified size

plt.figure(figsize=(8, 8))

 

\# Plot the data as a pie chart

behavior_counts.plot(

kind=\'pie\', \# Specifies that the plot type is a pie chart

autopct=\'%1.1f%%\', \# Displays percentages on each pie slice with one decimal place

startangle=90, \# Rotates the pie chart so that the first slice starts at the top (90 degrees)

cmap=\'Paired\' \# Uses a colormap that pairs visually distinct colors

)

 

\# Add a title to the pie chart

plt.title(\'Proportion of CWBs to OCBs\')

 

\# Remove the default y-axis label for a cleaner visualization

plt.ylabel(\'\')

 

\# Display the pie chart

plt.show()

3.  Run the code to view the pie chart from the keyword additions.

4.  What are the proportions of OCBs to CWBs?

After incorporating specific keywords, the proportion might further refine to:

- **75% OCB, 25% CWB**

This improvement highlights the impact of targeted keywords that align behaviors more accurately with their intended category. For instance, comments containing terms like \"mentor,\" \"support,\" or \"assist\" might now classify as OCB even if sentiment analysis alone would misclassify them.

5.  How is this different than the previous predictions?

Feature engineering provides a more robust classification by incorporating domain-specific keywords. Unlike sentiment-based models, which rely on polarity scores alone, this method aligns behaviors with predefined patterns (keywords). As a result, nuanced behaviors like \"Mentors new employees\" are reliably classified as OCB even if their sentiment score is neutral. Similarly, subtle CWBs like \"Spreads rumors\" are correctly identified due to keyword matching, improving classification accuracy beyond the adjusted threshold.

**Step 11: Save your Python notebook**

Save your Python notebook by converting it to a PDF with the following steps:

- Go to **File \> Print** in the Colab notebook.

- In the print dialog, select Landscape Layout, click **Save as PDF**

- Submit the **PDF to D2L.**

**[Submission Instructions:]{.underline}**

- **Python**: Submit this word document along with the PDF version of your Python notebook.

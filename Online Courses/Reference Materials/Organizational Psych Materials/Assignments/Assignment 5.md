# **Assignment 5: Using Python to Classify Employee Behaviors**

###Objective:

*   Classify text of employee behaviors as either CWB or OCB using the package TextBlob and sentiment analysis.
* Understand how text analytics can be used in I/O to gain insights into employee behaviors.

## Step 1: Set up the Google Colab environment
###Load the packages in the code cell below by pressing "ctrl + Enter" or clicking the play button on the left of the cell.
###In this activity, we are installing the TextBlob library to process text in our code.

```python
# Install necessary packages for text analysis and data visualization
!pip install textblob matplotlib

# Importing libraries for text analysis and visualization
from textblob import TextBlob  # For sentiment analysis
import pandas as pd           # For managing datasets
import matplotlib.pyplot as plt  # For creating visualizations
```

##Step 2: Create a Dataset
###We will create a small dataset of example employee comments.


##**Task:**


1.   Replace '"Example CWB 1"', '"Example CWB 2"', '"Example CWB 3"' with 3 examples of counter productive work behaviors.
2.   Replace '"Example CWB 1"', '"Example CWB 2"', '"Example CWB 3"' with 3 examples of counter productive work behaviors.
3. Run the code.





```python
# Creating a sample dataset with initial comments
data = {
    'Comments': [
        "Helped a colleague with their project.",
        "Always late for meetings.",
        "Volunteered for the weekend event.",
        "Goes above and beyond to assist clients.",
        "Spread false rumors about a coworker.",
        "Pushes a coworker down the stairs.",
        "Offered to help a coworker with their workload.",
        "Took credit for others' work.",
        "Frequently stays late to meet deadlines.",
        "Ignores important emails from management.",
        "Provides constructive feedback to peers.",
        "Missed a major deadline due to procrastination.",
        "Organized a team lunch to boost morale.",
        "Avoids unnecessary meetings to stay productive.",
        "Encourages team members to share their ideas.",
        "Rarely helps coworkers unless directly asked.",
        "Double-checks work to ensure accuracy.",
        "Distracts others during work hours.",
        "Mentors new employees to help them adapt.",
        "Criticizes coworkers in front of others."
    ]
}


# Convert the dataset into a DataFrame (a table-like structure)
df = pd.DataFrame(data)

# Now add your own examples
your_cwbs = ["Example CWB1", "Example CWB2", "Example CWB3"]  # Examples of negative workplace behaviors
your_ocbs = ["Example OCB1", "Example OCB2", "Example OCB3"]  # Examples of positive workplace behaviors

# Combine your examples with the initial dataset
your_data = pd.DataFrame({'Comments': your_cwbs + your_ocbs})
df = pd.concat([df, your_data]).reset_index(drop=True)  # Reset the index for a clean table

# View the combined dataset
df
```

##Step 3: Text Analysis Using TextBlob
###We will perform sentiment analysis on the comments, associating positive sentiments with OCBs and negative sentiments with CWBs.


##**Task:**


1. Observe the classified behaviors after running the code.
2. Do all your example behaviors align with the type of behavior you input?
3. If there are any that do not align, why do you think that is?


```python
# Function to classify behaviors based on sentiment polarity
def classify_behavior(comment):
    analysis = TextBlob(comment)  # Analyze the comment's sentiment
    if analysis.sentiment.polarity > 0:  # Positive sentiment
        return 'OCB'
    else:  # Neutral or negative sentiment
        return 'CWB'

# Apply the function to classify each comment
df['Predicted Behavior Type'] = df['Comments'].apply(classify_behavior)

# Display the results
df[['Comments', 'Predicted Behavior Type']]
```

##Step 4: Visualization with Pie Chart
###We will now visualize the classified behaviors to better understand their proportions.


##**Task:**


1. Analyze the pie chart showing the proportion of behaviors after running the code.
2. What is the proportions of OCBs to CWBs?

```python
# Count the occurrences of each behavior type (OCB and CWB)
behavior_counts = df['Predicted Behavior Type'].value_counts()

# Create a pie chart to visualize the proportions of OCBs and CWBs
plt.figure(figsize=(8, 8))  # Set the figure size
behavior_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Set3')
plt.title('Proportion of OCBs to CWBs')  # Add a title to the chart
plt.ylabel('')  # Remove the y-axis label for a cleaner look
plt.show()  # Display the pie chart
```

##Step 5: Adjusted Text Analysis Using TextBlob
###We will perform sentiment analysis on the comments, associating positive sentiments with OCBs and negative sentiments with CWBs with an adjusted threshold.


##**Task:**


1. Observe the classified behaviors after running the code.
2. How does this classification compare to the original threshold?


```python
# Define a function to classify behaviors based on sentiment polarity with an adjusted threshold
def classify_behavior(comment):
    analysis = TextBlob(comment)  # Perform sentiment analysis on the comment using TextBlob
    if analysis.sentiment.polarity >= -0.3:
        # If the sentiment polarity is greater than or equal to -0.3 (includes slight negatives and neutrals), classify as OCB
        return 'OCB'
    else:
        # Otherwise, classify as CWB for strongly negative sentiment
        return 'CWB'

# Apply the classification function to each comment in the 'Comments' column
df['Adjusted Prediction'] = df['Comments'].apply(classify_behavior)

# Print the comments alongside their adjusted behavior predictions
df[['Comments', 'Adjusted Prediction']]
```

##Step 6: Adjusted Visualization with Pie Chart
###We will now visualize the adjusted classified behaviors to better understand their proportions.


##**Task:**


1. Analyze the pie chart showing the proportion of adjusted predicted behaviors after running the code.
2. How do the adjusted proportions compare to the un-adjusted proportions?


```python
# Count the occurrences of each behavior type (OCB and CWB) based on the adjusted predictions
behavior_counts = df['Adjusted Prediction'].value_counts()

# Set up the figure size for the pie chart
plt.figure(figsize=(8, 8))

# Plot a pie chart to visualize the proportion of OCBs and CWBs
behavior_counts.plot(
    kind='pie',  # Specify the chart type as pie
    autopct='%1.1f%%',  # Display the percentage of each slice with one decimal place
    startangle=90,  # Start the first slice at 90 degrees for better alignment
    cmap='Paired'  # Use a paired colormap for distinct, visually appealing colors
)

# Add a title to the pie chart
plt.title('Proportion of CWBs to OCBs')

# Remove the y-axis label for a cleaner look
plt.ylabel('')

# Display the pie chart
plt.show()
```

##Step 7: Further Adjusting Prediction with Feature Engineering
###Now, we will further adjust the predictions by adjusting the features that are associated with OCBs and CWBs. This includes specfic keywords to make more accurate or meaningful predictions.


##**Task:**

  1. Replace 'positive', 'teamwork' with two of your own chosen keywords indicative of OCB.
  2. Replace 'negative', 'conflict' with two of your own chosen keywords indicative of CWB.
  3. Run the code.

```python
# Define predefined keywords for OCB and CWB
keywords_ocb = ['help', 'assist', 'support', 'volunteer']  # Common terms associated with positive workplace behaviors (OCB)
keywords_cwb = ['late', 'rumors', 'credit']  # Common terms associated with negative workplace behaviors (CWB)

# Task: Add your own keywords for both OCB and CWB
your_keywords_ocb = ['OCB Keyword 1', 'OCB Keyword 2', 'OCB Keyword 3']  # Additional positive behavior indicators (replace with your own if needed)
your_keywords_cwb = ['CWB Keyword 1', 'CWB Keyword 2', 'CWB Keyword 3']  # Additional negative behavior indicators (replace with your own if needed)

# Combine predefined keywords with the user's custom keywords
final_keywords_ocb = keywords_ocb + your_keywords_ocb  # Combine OCB keyword lists
final_keywords_cwb = keywords_cwb + your_keywords_cwb  # Combine CWB keyword lists

# Create new columns to indicate whether a comment contains any OCB or CWB keywords
df['Keyword OCB'] = df['Comments'].apply(lambda x: any(word in x.lower() for word in final_keywords_ocb))
# Checks if any OCB keyword is present in each comment (case-insensitive) and assigns True/False.

df['Keyword CWB'] = df['Comments'].apply(lambda x: any(word in x.lower() for word in final_keywords_cwb))
# Checks if any CWB keyword is present in each comment (case-insensitive) and assigns True/False.

# Display the comments along with the results for keyword matches
df[['Comments', 'Keyword OCB', 'Keyword CWB']]
```

##Step 8: Feature Engineering Predictions
###We will predict the OCB and CWB classifications with the feature engineering.

##**Task:**

  1. Run the code and observe the predictions.

```python
# Define a function to classify behaviors using keyword matching and fallback sentiment analysis
def engineered_classify_behavior(row):
    if row['Keyword OCB']:
        return 'OCB'  # Classify as OCB if any OCB keyword is present
    elif row['Keyword CWB']:
        return 'CWB'  # Classify as CWB if any CWB keyword is present
    else:
        return classify_behavior(row['Comments'])  # If no keywords are found, use sentiment analysis as a fallback

# Apply the classification function to each row in the DataFrame
df['Engineered Prediction'] = df.apply(engineered_classify_behavior, axis=1)
# The `apply` function processes each row, using the keyword columns and the fallback for a final classification.

# Display the comments along with their engineered predictions
df[['Comments', 'Engineered Prediction']]
```

##Step 9: Feature Engineering Pie Chat Visualization
###We will visualize the feature engineered pedictions with a pie chart.

##**Task:**

  1. Run the code and observe the pie chart of the feature engineered predictions.
  2. What was the best way to predict behaviors between the 3, in your opinion?

```python
# Count the number of occurrences for each behavior type (OCB and CWB) from the 'Engineered Prediction' column
behavior_counts = df['Engineered Prediction'].value_counts()

# Create a new figure for the pie chart with a specified size
plt.figure(figsize=(8, 8))

# Plot the data as a pie chart
behavior_counts.plot(
    kind='pie',  # Specifies that the plot type is a pie chart
    autopct='%1.1f%%',  # Displays percentages on each pie slice with one decimal place
    startangle=90,  # Rotates the pie chart so that the first slice starts at the top (90 degrees)
    cmap='Paired'  # Uses a colormap that pairs visually distinct colors
)

# Add a title to the pie chart
plt.title('Proportion of CWBs to OCBs')

# Remove the default y-axis label for a cleaner visualization
plt.ylabel('')

# Display the pie chart
plt.show()
```

#Step 10: Saving your Notebook as A PDF
Save your notebook with your output.

##**Task:**
Before you submit your assignment, you need to save your notebook as a PDF document.

To do so, go to "file", click "print" and once a new window comes up, select the option to save as a pdf.

Upload this pdf to Assigment 5 in D2L.


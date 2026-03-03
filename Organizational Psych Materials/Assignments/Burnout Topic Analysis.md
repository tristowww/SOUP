co

{x}

<>

File

+ Code

& Burnout Topic Analysis.ipynb

Edit View Insert Runtime Tools Help All changes saved

+ Text

¥ Burnout Topic Analysis

Research Question:

How do students define burnout in their own words?

v Set up the Google Colab environment

=| fet 2, Share

RAM ——
Disk ——

Load the packages in the code cell below by pressing "ctrl + Enter" or clicking the play button on the left of the cell.

Y
~ (i)
=

# import necessary libaries and packages
!pip install bertopic

!pip install kneed

# Package Installation
!pip install bertopic transformers sentence-transformers wordcloud plotly kneed

# Data Manipulation and Analysis

import numpy as np

import pandas as pd

from collections import Counter, defaultdict
import re

import random

import os

from concurrent.futures import ThreadPoolExecutor

# Machine Learning and NLP

from bertopic import BERTopic

from sentence_transformers import SentenceTransformer

from sklearn.mixture import GaussianMixture

from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
from transformers import pipeline

# Text Processing

import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords as nltk_stopwords

from nltk.tokenize import word_tokenize

from wordcloud import WordCloud

# Visualization

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import textwrap

# Google Colab Specific
from google.colab import drive

Collecting bertopic
Downloading bertopic-0.16.4-py3-none-any.whl.metadata (23 kB)
Collecting hdbscan>=0.8.29 (from bertopic)

Downloading hdbscan-0.8.40-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_|

64.whl.metadata (15 kB)

Requirement already satisfied: numpy>=1.20.@ in /usr/local/lib/python3.10/dist-packages (from bertopic) (1.26.4)

Requirement already satisfied: pandas>=1.1.5 in /usr/local/lib/python3.10/dist-packages (from bertopic) (2.2.2)

Requirement already satisfied: plotly>=4.7.@ in /usr/local/lib/python3.10/dist-packages (from bertopic) (5.24.1)

Requirement already satisfied: scikit-learn>=0.22.2.post1 in /usr/local/lib/python3.10/dist-packages (from bertopic) (1.5.2)
Requirement already satisfied: sentence-transformers>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from bertopic) (3.2.1)
Requirement already satisfied: tqdm>=4.41.1 in /usr/local/lib/python3.10/dist-packages (from bertopic) (4.66.6)

Collecting umap-learn>=0.5.0 (from bertopic)
Downloading umap_learn-9.5.7-py3-none-any.whl.metadata (21 kB)

Requirement already satisfied: scipy>=1.0 in /usr/local/lib/python3.10/dist-packages (from hdbscan>=@.8.29->bertopic) (1.13.1)
Requirement already satisfied: joblib>=1.0 in /usr/local/lib/python3.10/dist-packages (from hdbscan>=0.8.29->bertopic) (1.4.2)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas>=1.1.5->bertopic) (2.8.2)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.1@/dist-packages (from pandas>=1.1.5->bertopic) (2024.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.1@/dist-packages (from pandas>=1.1.5->bertopic) (2024.2)

Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.10/dist-

packages (from plotly>=4.7.0->bertopic) (9.0.0)

Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from plotly>=4.7.0->bertopic) (24.2)

Requirement already satisfied: threadpoolct1l>=3.1.0 in /usr/local/lib/python3.10/dist-packages (from scikit-learn>=0.22.2.post1->bertopic) (3.5.0)
Requirement already satisfied: transformers<5.0.0,>=4.41.0 in /usr/local/lib/python3.10/dist-packages (from sentence-transformers>=0.4.1->bertopic) (4
Requirement already satisfied: torch>=1.11.0 in /usr/local/lib/python3.10/dist-packages (from sentence-transformers>=0.4.1->bertopic) (2.5.1+cu121)

Requirement already satisfied: huggingface-hub>=0@.20.@ in /usr/local/lib/python3
Requirement already satisfied: Pillow in /usr/local/lib/python3.10/dist-packages

.10/dist-packages (from sentence-transformers>=0.4.1->bertopic) (0.26.
(from sentence-transformers>=0.4.1->bertopic) (11.0.0)

Requirement already satisfied: numba>=@.51.2 in /usr/local/lib/python3.10/dist-packages (from umap-learn>=0.5.0->bertopic) (0.60.0)

Collecting pynndescent>=0.5 (from umap-learn>=0.5.@->bertopic)
Downloading pynndescent-9.5.13-py3-none-any.whl.metadata (6.8 kB)

Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers>=0.4.1->bertor
Requirement already satisfied: fsspec>=2023.5.@ in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers>=0.4.1
Requirement already satisfied: pyyaml>=5.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers>=0.4.1->ber
Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.20.0->sentence-transformers>=0.4.1->bertor
Requirement already satisfied: typing-extensions>=3.7.4.3 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.20.@->sentence-transforn

Dangiiiramant al ready satisfied: Tivml ite<a, 44, >=9 43  Gadeya in /usr/lecal /lib/python3. 19/dist- -packages ( (from num ba>=9.51.2->uman-learn>=-2.5 =-Shertonic

Hoyas Sei. aar cau SEs tee 2a Via ee

~~

be Nie bane FunaE” eoar is -Q- US eV Ppa

Requirement sireedly satisfied: six>=1.5 in /usr/local/1ib/python3.10/dist- packages (from python- -dateutil>= 2.8.2->pandas>=1.1.5->bertopic) (1.16.0)
Requirement already satisfied: networkx in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=0.4.1->bertopic) (3.4.2

Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages

(from torch>=1.11.0->sentence-transformers>=0.4.1->bertopic) (3.1.4)

Requirement already satisfied: sympy==1.13.1 in /usr/local/lib/python3.10/dist-packages (from torch>=1.11.0->sentence-transformers>=0.4.1->bertopic) (
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /usr/local/lib/python3.10/dist-packages (from sympy==1.13.1->torch>=1.11.0->sentence-transformers
Requirement already satisfied: regex!=2019.12.17 in /usr/local/lib/python3.10/dist-packages (from transformers<5.0.0, >=4.41.0->sentence-transformers>=
Requirement already satisfied: safetensors>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from transformers<5.0.0, >=4.41.0->sentence-transformers>
Requirement already satisfied: tokenizers<@.21,>=0.20 in /usr/local/lib/python3.10/dist-packages (from transformers<5.0.0, >=4.41.0->sentence-transforn

Requirement already satisfied: MarkupSafe>=2.@ in /usr/local/lib/python3.10/dist-

packages (from jinja2->torch>=1.11.0->sentence-transformers>=0.4.1->t

Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.20.0->sentence-t
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests ->huggingface-hub>=0.20.0->sentence-transformers>
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests ->huggingface-hub>=0.20.0->sentence-transfc
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests ->huggingface-hub>=0. 20.0->sentence-transfc

Downloading bertopic-0.16.4-py3-none-any.whl (143 kB)
—_—_— OO _ 143..7/143.7 kB 6.7 MB/S eta 0:00:00

Downloading hdbscan-0.8.40-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.2 MB)

4.2/4.2 MB 23.9 MB/s eta 9:00:00
Downloading umap_learn-0.5.7-py3-none-any.whl (88 kB)
—_—_— en 88.8/88.8 kB 4.4 MB/s eta 0:00:00
Downloading pynndescent-@.5.13-py3-none-any.whl (56 kB)
OO _ 56. 9/56.9 kB 3.3 MB/S eta 0:00:00
Installing collected packages: pynndescent, hdbscan, umap-learn, bertopic

Successfully installed bertopic-9.16.4 hdbscan-@.8.4@ pynndescent-@.5.13 umap-learn-@.5.7
Requirement already satisfied: transformers in /usr/local/lib/python3.10/dist-packages (4.46.2) S

4

¥ Data Loading and Inital Setup

- Import necessary libraries and packages for data manipulation, modeling, and visualization.

- Load datasets from local files, databases, or other sources.

[ ]

v

x, [2]
<>4

v

, [3]

# load the dataset by uploading the file
data = pd.read_csv('/content/Burnout_Data.csv' )

# Load a CSV file from Google Drive

drive.mount('/content/drive’ )

file_path = '/content/drive/My Drive/RU Org Psych/Fall 2024/Burnout_Data.csv'
data = pd.read_csv(file_path)

# Display the data
data

Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).

StartDate EndDate Status IPAddress Progress
9 Start Date End Date Response Tyne IP Address Progress Dura

1 = {"Importid":"startDate”,"timeZone":"America/De...  {"Importld":"endDate","timeZone":"America/Denv... {"Importld":"status"} {"Importld":"ipAddress"} {"Importid":"progress"} {"Imp

2 11/7/2024 12:17 11/7/2024 12:30 0 137.45.225.254 100
3 11/7/2024 12:51 11/7/2024 13:04 0 137.45.71.110 100
4 11/7/2024 17:43 11/7/2024 17:56 0 216.30.159.241 100
111 11/13/2024 14:56 11/13/2024 15:02 0 137.45.69.0 57
112 11/21/2024 8:37 11/21/2024 9:06 0 137.45.69.236 100
113 11/14/2024 10:15 11/14/2024 10:15 0 104.28.76.233 14
114 11/21/2024 12:46 11/21/2024 13:01 0 216.131.84.89 100
115 11/14/2024 13:08 11/14/2024 13:08 0 104.28.76.231 7

116 rows x 148 columns

# Remove the first two rows from the dataset
data = data.iloc[2:].reset_index(drop=True)

v Preparing the Data Structure

v

~ [4]
oy

v

% [5]

—_—
vw
—

# Prepare the text data for analysis by isolating the column of text data
df_burn = data[[ ‘burnopen']].copy()

df_burn.dropna(inplace=True)

df_burn = df_burn.astype(str)

df_burn_final = df_burn.values.flatten()

df_burn_final

array(['stress out and a lot of head aches’,
"I need a to reagather myself’,
"That one is lacking motivation to go throughout their duties. ',

‘When someone says they are burned out that means that they have no more energy left to pour into that specific thing. Typically occurring in

high demand jobs or task such as school',

"They are pretty much done with everything, they have been through a lot and can't give out any more than what they have already done.",
‘to me it means putting all your effort into something for so long and never seeing any progress/reward from the hard work and dedication,

inturn your brain feels like it just shuts off and suddenly you cant get anything at all done. ',

"That they are tired and just wanna rest. ', ‘tired or drained’,

'Tired',

"They are physically, mentally, spiritually are tired with everthing that
"just exhausted and giving up.',

is going on in their lives. ',

"Being out of energy and kind of dragging through the days until the weekend or a break ',

"They cant do what they love anymore’,

"That we are at our ends with the things that are piling up for us, and that it is all becoming too much. We are done.',

"Having no motivation for the things I once loved to do or the motivation

"Mind clouded and feel as if they can not handle whatever they are involved in anymore or need a mental break. ',

‘Tired or bored of life/work/school. Feeling empty of pointless',
‘They feel drained and emotionally exhausted.',

‘They just cant go anymore ',

to do the things I need to do. Physically and mentally.',

"When someone is burned out, I think of someone who is tired of doing something on repeat consistently. They have a workload that they can't

handle and are overwhelmed.",
‘That mean that you need to stop, and take time for yourself.',
‘I just want to give up because I have become so overwhelmed.',
‘tired of whats going on in my life’,
‘That they are tired and exhausted of putting in effort.',
"They need a break or they will break’,

"Reaching the end of their ability to effectively multitask multiple aspects of their life.',
"They're tired of the same thing happening over an over or have no energy ",

‘Something is wrong with them in a bad way',

"That I am exhausted and have very little energy to engage in any activity.',
‘When someone says they are “burned out," it typically means they are feeling physically, mentally, and emotionally exhausted to the point

where they can no longer function effectively. ',

‘That thew ere over. iorked and overwhelmed toa the n
cy Wenn Wossnee Lo eel pp

"Tired of doing things wanting a break.'

"they have reached their breaking sane,

"That you have been working very hard or doing something draining and you
"feeling drained and having no want to do the things they need to do',
"tired/exhausted',

"It means they are at their mental, emotional, and/or physical limits.',
‘mentally and physically drained’,

"I feel like I can't do anything and I'm exhausted", ‘tired’,

feel like you can't keep going or need a break. ",

"that there's no life left to lose, I've been drained so I've been running on empty for a while.",

"they are tired ',

"That they are tired and don't have any motivation left.",

"tired or exhausted or they are just going to things mentally',

"It means that they are reaching the end of their mental capacity and are

‘ready to break down', ‘They are just sick of what they do‘,
"physically and mentally exhausted ', ‘out of life’,

going to need a mental break before long. ',

"They are mentally and physically drained by the thigs going on around them.',

"They are tired of what they're doing.",
"That I have not energy or motivation. Just so done and tired. ',
‘just feeling emotionally drained and tired of everything’,

‘When I hear someone say they are “burned out," I think they in whatever they are referring it to, they are mentally and physically done and

over what it is and it no longer fulfills them in the way it did before.',
"It means mentally they are checked out and need a break.',
"Whenever I say it I feel like my social battery is about to die and that
"cant focus’,

# Output the number of text responses
print(f"Total number of responses for ‘burnopen': {data['burnopen'].dropna().sha

Total number of responses for 'burnopen': 109

Y Word Cloud Generation

~ Le]

(4)

# Combine the list into a singie string as word clouds take a string input
text = " ".join(review for review in df_burn_final)

# Create the word cloud object with specific parameters for clarity

wordcloud = WordCloud(
background_color="white",
colormap="viridis",

# Set background color to white
# Use the ‘viridis’ colormap for better contrast
width=800, # Set the width of the word cloud image
height=40ee, # Set the height of the word cloud image
max_words=200, # Set the maximum number of words in the cloud
# Set the maximum font size for words
# Increase the scale to improve image resolution
# Set a random seed for reproducibility

max_font_size=100,

scale=3,

random_state=42
).generate(text)

# Display the generated image:

plt.figure(figsize=(12, 6))  # Adjust the figure size for better visibility
plt.imshow(wordcloud, interpolation='bilinear' )

plt.axis ("off")

I don't have energy to do tasks, even ones I enjoy.",

pe[@]}")

plt.show()
ft
continue empty WY becomingability dedication consistent] hi checked _
SOMERS MEL oS. estar MUCH peer: ysome thing epee
pha mnie ver . put ting le ft.
wanna ove
ze Wabi overmaining days night StOP giving give
activity Ongoing rett attery
1Mme brain pretty whateverwil},,. referr Wi OF away
ready moons nr aspects
even Ye

specifi

c breaking g reagather worked @ StFeSSOF Sextrenely high ife
y ruining |
clouded
cya, L '€ physic
e
in ard

< erine led: Lacki

Exhaustion

n eo sie om get
p eG uae

spiritually

effort eFfeele@X

activitie re lose CY MALY 2
m e a Ne a niymor xhaus t hink _ "a
eebecome
Te readfB
lear

seeing lt =
mu Lp!

— E oo 7" er "a chore 20,
-~ Cc a +

£ 8 past 1! 6c “a

if u oO x

5 ee in ar o

3 $e ‘e

<£

v Sentiment Analysis using Dictionary Method

8‘ suas, Ol: a
aroun wv
goingnee di.

:
limits @

suddenly

ogr

incapable

ec

stres

a)

00

5

Tw fed
a y

nev J Wisi,
gole

someone

ne 4
shuts 4 es enjoy hobbies
duties © thing

2 bt U ir ne he

hear
Ng. Me A LNZ one POL int €
T ee] a yi ee Vel multitask emote piling Ln inturn§ involved

- Apply sentiment analysis models to understand emotional tone in text (e.g., positive, negative, neutral).

- Use pre-trained models such as VADER

a

(4)

Os

(4)

~

(4)

# Initialize VADER Sentiment Analysis
nltk.download('vader_lexicon') # Download required VADER lexicon
sia = SentimentIntensityAnalyzer() # Create VADER sentiment analyzer instance

# List to store sentiment classifications
sentiments = []

# Analyze sentiment for each response

for review in df_burn_final:
# Get polarity scores using VADER
# Returns dict with pos, neg, neu and compound scores
sentiment_scores = sia.polarity_scores (review)

# Classify sentiment based on compound score

# Using standard thresholds:

# >= 0.05 for positive

# <= -@.05 for negative

# Between -@.05 and 6.05 for neutral

if sentiment_scores['compound'] >= @.@5:
sentiment = ‘Positive'

elif sentiment_scores[ 'compound'] <= -@.0@5:
sentiment = ‘Negative’

else:
sentiment = ‘Neutral’

# Add classification to results list
sentiments. append(sentiment)

# Calculate sentiment distribution

# Count number of each sentiment using list comprehension

positive_reviews = sum(1 for sentiment in sentiments if sentiment == ‘Positive’ )
negative_reviews = sum(1 for sentiment in sentiments if sentiment == ‘Negative’ )
neutral_reviews = sum(1 for sentiment in sentiments if sentiment == 'Neutral')

# Print results

print(f"Number of Positive Reviews: {positive_reviews}")
print(f"Number of Negative Reviews: {negative_reviews}")
print(f"Number of Neutral Reviews: {neutral_reviews}")

Number of Positive Reviews: 23
Number of Negative Reviews: 67
Number of Neutral Reviews: 19
[nltk_data] Downloading package vader_lexicon to /root/nltk_data...

# Create a pie cnart to visualize the sentiment distribution
labels = ['Positive', ‘Negative’, ‘Neutral’ ]

sizes = [positive_reviews, negative_reviews, neutral_reviews ]
colors = ['green', ‘red', ‘gray']

plt.figure(figsize=(6, 6))

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1%%' )
plt.title('Sentiment Distribution’ )

plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

Sentiment Distribution

Negative

Neutral

etl

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Initialize lists to store the categorized reviews
positive reviews = []
neutral_reviews = []
negative_reviews = []

# Iterate over each review

for review in df_burn_final:
# Calculate sentiment scores for each review
sentiment_scores = sia.polarity_scores(review)

# Categorize the review based on the compound score

if sentiment_scores['compound'] >= 0.95:
positive_reviews.append(review)
neutral_reviews.append('')
negative_reviews.append('' )

elif sentiment_scores['compound'] <= -0.95:
positive_reviews.append('')
neutral_reviews.append('' )
negative_reviews.append(review)

else:
positive_reviews.append('' )
neutral_reviews.append(review)
negative_reviews.append('' )

# Create a new DataFrame with the categorized reviews
categorized_reviews_df = pd.DataFrame({

"Positive Reviews': positive_reviews,

"Neutral Reviews': neutral_reviews,

"Negative Reviews': negative_reviews

})

# Display the first few rows of the new DataFrame
categorized_reviews_df

Positive Reviews Neutral Reviews

1 | need a to reagather myself

2 That one is lacking motivation to go throughou...
3

>.

104
105
106 That they need a week to themselves
107
108

109 rows x 3 columns

Next steps: @) View recommended plots New interactive sheet

(4)

for review in df_burn_final:
# Calculate sentiment scores for each review
sentiment_scores = sia.polarity_scores(review)
compound_scores.append(sentiment_scores[ 'compound' ])

# Calculate the overall sentiment score based on an average
overall_sentiment_score = sum(compound_scores) / len(compound_scores)

# Determine the overall sentiment label based on the overall score
if overall_sentiment_score >= 9.95:
overall_sentiment_label = ‘Positive’
elif overall_sentiment_score <= -@.@5:
overall_sentiment_label = ‘Negative’
else:
overall _sentiment_label = ‘Neutral’
# Print the overall sentiment score and label
print(f"Overall Sentiment Score: {overall_sentiment_score}")
print(f"Overall Sentiment Label: {overall_sentiment_label}")

Overall Sentiment Score: -0.18259633027522937
Overall Sentiment Label: Negative

Negative Reviews FA

stress out and a lot of head aches il |

o

When someone says they are burned out that mea...

They are exhausted and running on fumes to get...

| think it means they are low on motivation, w...

They feel that they can not handle any more st...

i'm tired and need to take a break

v Accessing the Hugging Face.com API for Large Language Model Usage in Code

Hugging Face API Authentication & Setup Guide
For detailed API documentation, visit: https://huggingface.co/docs/hub/en/security-tokens

This section handles the authentication setup for accessing Hugging Face's models and services. You'll need an API key to access the models

used

in this analysis.

Quick Setup:

Create a free account at huggingface.co
Navigate to Settings > Access Tokens
Generate a new access token

Paste your token in the input below

Important Security Notes:

Never share or commit your API key
Regenerate immediately if exposed
Monitor for unauthorized usage

Usage in this Analysis:

Model access for text classification

© OCH allalysts
e Theme generation
e Text embedding creation

ad [11] # Hugging Face API Key Configuration
# Request API key from user
# This is needed to access Hugging Face's models and pipelines
# The API key is a personal access token that authenticates your requests

huggingface_api_key = input("Please enter your Hugging Face API key: ")

# Example API key format (commented out for security):
#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

=>4 Please enter your Hugging Face API key: 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

v Sentiment Analysis Using LLMs

- Apply sentiment analysis models to understand emotional tone in text (e.g., positive, negative, neutral).

- Use pre-trained models such as a deep learning-based transformer.

x [12] # Initialize Hugging Face Sentiment Analysis Pipeline
# Using multilingual BERT model trained for sentiment classification
# This model can handle text in multiple languages and returns ratings from 1-5
sentiment_analysis = pipeline(

task="text-classification", # Specify the NLP task
model="nlptown/bert-base-multilingual-uncased-sentiment", # Pre-trained model selection
token=huggingface_api_key # Authentication token

def get_sentiment_hf_api(text):

Analyze sentiment of input text using Hugging Face's BERT model.

Args:
text: Input text to analyze (can be any datatype, will be converted to string)

Returns:
str: Sentiment classification ('positive', 'negative', or ‘neutral')

The model uses a 5-point scale where:
- 1-2: Negative sentiment

- 3: Neutral sentiment

- 4-5: Positive sentiment

try:
# Input validation and preprocessing
text = str(text) # Convert input to string
if not text.strip(): # Handle empty/whitespace input

return ‘neutral’
# Get model prediction
response = sentiment_analysis(text)[@] | # Model returns list of predictions

score = int(response[ 'label'][@]) # Extract numerical rating (1-5)

# Convert 5-point scale to trinary classification

if score >= 4: # Ratings 4-5 are positive
return ‘positive’

elif score <= 2: # Ratings 1-2 are negative
return ‘negative’

else: # Rating 3 is neutral

return ‘neutral’

except Exception as e:
# Error handling: log error and return safe default
print(f"Error processing text: {e}")
return ‘neutral’

config.json: 100% (IS 953/953 [00:00<00:00, 50.7kB/s]
pytorch_model.bin: 100% [NS soso [00:06<00:00, 37.8MB/s]
tokenizer_config.json: 100% [TS 39.0/39.0 [00:00<00:00, 1.95kB/s]
vocab.txt: 100% [TS § 872k/872k [00:00<00:00, 6.77MB/s]
special_tokens_map.json: 100% SII «112/112 [00:00<00:00, 5.72kB/s]

(4)

< [13] # Create the sentiment DataFrame
sentiment_df = pd.DataFrame({
‘Document’: df_burn_final,
‘Sentiment’: [get_sentiment_hf_api(doc) for doc in df_burn_final]

})

Y [14] # Display sentiment distribution

sentiment_distribution = sentiment_df[ 'Sentiment'].value_counts()
print("\nSentiment Distribution:")

print(sentiment_distribution)

(4)

Sentiment Distribution:

Sentiment

negative 81
neutral 14
positive 14

Name: count, dtype: int64

Y [15] # Add percentage distribution

sentiment_percentages = sentiment_distribution / len(sentiment_df) * 100
print("\nSentiment Distribution (%):")
print(sentiment_percentages.round(2) )

(4)

Sentiment Distribution (%):

Sentiment
negative 74.31
neutral 12.84

positive 12.84
Name: count, dtype: float64

Y [16] # Plot sentiment distribution

plt.figure(figsize=(10, 6))

plt.bar(sentiment_distribution.index, sentiment_distribution.values, color=['red', ‘blue', ‘green'])
plt.xlabel( 'Sentiment' )

plt.ylabel('Number of Comments')

plt.title('Sentiment Distribution’ )

plt.show()

(4)

Sentiment Distribution

80

70

60

50

40

Number of Comments

30
20

10

negative neutral positive
Sentiment

vf [17] # Calculate overall sentiment score (including Neutral)
sentiment_score_mapping = {'positive': 1, ‘neutral’: @, ‘negative’: -1}
sentiment_df['Score'] = sentiment_df[ 'Sentiment' ].map(sentiment_score_mapping)
overall_sentiment_score = sentiment_df['Score' ].mean()
print(f"Overall Sentiment Score: {overall_sentiment_score}")

—_—

~ Overall Sentiment Score: -0.6146788990825688

——)

v Feature Extraction and Embedding Generation

2A [18] # Import and Initialize Sentence Transformer Model

# Import the SentenceTransformer class from sentence-transformers library

# This library provides easy access to various transformer models optimized for creating sentence embeddings
from sentence_transformers import SentenceTransformer

# Initialize the Language-agnostic BERT Sentence Embedding (LaBSE) model

# LaBSE is specifically designed to:

# - Create meaningful embeddings that work across 109 languages

# - Generate similar embeddings for semantically similar sentences, even in different languages
# - Produce fixed-size vector representations (768 dimensions)

embedding model = SentenceTransformer("LaBSE" )

modules.json: 100% (NS 461/461 [00:00<00:00, 24.5kB/s]

config sentence transformers.ison: 100, =A 991499 100-00<00-00
tence SON! (CC) i '</ 142 YUCUSILY

(4)

fal Tat
VV my vovil

README.md: 100% (IS 2.22k/2.22k [00:00<00:00, 128kB/s]
sentence_bert_config.json: 100% [TS = 53.0/53.0 [00:00<00:00, 3.10kB/s]
config.ison: 100% (IS 804/804 [00:00<00:00, 45.6kB/s]
model.safetensors: 100% [TS 1.88G/1.88G [00:22<00:00, 52.4MB/s]
tokenizer_config.json: 100% IS 397/397 [00:00<00:00, 8.95kB/s]
vocab.txt: 100% [iS § 5.221/5.22M [00:00<00:00, 14.7MB/s]
tokenizerjson: 100% [TS 9.6211/9.62M [00:00<00:00, 29.6MB/s]
special_tokens_map.json: 100% [IIS 112/112 [00:00<00:00, 1.46kB/s]
1_Pooling/config.json: 100% (TT 190/190 [00:00<00:00, 3.43kB/s]

2 Dense/config.json: 400% nn 4441414 [00:00<00:00, 1.72kB/s]
2_Dense/config.json: 100%, EEE eee §=114/114 [00:00<00:00 , 1.72kB/s

pytorch_model.bin: 100% [2 .3611/2.36M [00:00<00:00, 7.38MB/s]
model.safetensors: 100% [NS 2 .361/2.36M [00:00<00:00, 7.24MB/s]

. [21] # NLTK (Natural Language Toolkit) Data Setup

# Download required NLTK packages

nltk.download('vader_lexicon')  # For sentiment analysis with VADER
nltk.download('punkt_tab' ) # For sentence tokenization
nltk.download('stopwords' ) # For filtering common words

# Set data path for NLTK resources
nltk.data.path.append('/root/nitk_data') # Ensures NLTK can find downloaded resources

(4)

[nltk_data] Downloading package vader_lexicon to /root/nltk_data...
jnitk_dataj Package vader_iexicon is already up-to-date!
[nltk_data] Downloading package punkt_tab to /root/nltk_data...
[nltk_data] Unzipping tokenizers/punkt_tab.zip.

[nltk_data] Downloading package stopwords to /root/nltk_data...
[nltk_data] Package stopwords is already up-to-date!

v Text Preprocessing and Cleaning

- Remove punctuation, special characters, and extra whitespace.
- Tokenize the text data into individual words or phrases.

- Remove stopwords to focus on meaningful words.

- Store cleaned text for subsequent analysis.

dj Oo # Text Preprocessing for Topic Modeling

# Create comprehensive stopwords set by combining:

# 1. NLTK English stopwords (e.g., ‘the', ‘is', ‘at', ‘which')

# 2. Scikit-learn's stopwords (additional common English words)

stop_words = set(nltk_stopwords.words('english')).union(ENGLISH_STOP_WORDS)

def remove_stopwords(sentence):

Clean and preprocess text by removing unwanted characters and common words.

Args:
sentence (str): Raw text input

Returns:
str: Cleaned text with stopwords and special characters removed
# Step 1: Remove punctuation and special characters
# [4\w\s] matches any character that's not a word character (\w) or whitespace (\s)
sentence = re.sub(r'[*\w\s]', '', sentence)

# Step 2: Normalize whitespace
# Replace multiple spaces with single space and trim
sentence = re.sub(r'\s+', ' ', sentence).strip()

# Step 3: Tokenize into individual words
word_tokens = word_tokenize(sentence)

# Step 4: Remove stopwords
# List comprehension to keep only non-stopwords (converted to lowercase)
filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

# Step 5: Recombine words into cleaned sentence
return " ".join(filtered_sentence)

# Apply cleaning function to entire dataset
# List comprehension processes all texts in df_burn_final
df_burn_final_cleaned = [remove_stopwords(x) for x in df_burn_final]

# Display cleaned text list
df_burn_final_cleaned

‘energy motivation tired',

‘feeling emotionally drained tired’,

‘hear say burned think referring mentally physically longer fulfills way',
‘means mentally checked need break'

a
‘say feel like social battery die dont energy tasks ones enijoy',

(4)

"focus',

‘means life moment like past point tired tired existing’,

‘tired plate’,

‘Tired needs days relax gain motivation’,

‘means tired anymore given',

‘energy continue tasks',

"Physically mentally exhausted things work school’,

‘means point motivation continue’,

‘tired things constantly feeling drained like anymore’,

‘think clearly sleep night doesnt time themself’,

"Like tired fed',

‘overwhelmed activities happening life’,

‘overwhelmed going dont motivation continue pushing’,

‘need reset destress need time recoup’,

‘tired need break’,

"Exhausted need time away',

‘Exhaustion’,

"Theyve worked hard point energy effort left going rate’,

‘means stress giving’,

"stress',

‘says burned means feeling ongoing stress overwhelming sadness’,
‘Burned means incapable putting form effort life work’,

‘drained work motivation’,

‘feeling extremely tired passion school work personal hobbies',
‘tired maxed everyday life routine’,

‘need break new mentally taxing’,

‘kind feels like gole burned unrecognized effort trying hard thing things impossible’,
‘Exhausted feeling permanently drained matter able things physically mentally level usually',
‘Im tired motivation work’,

‘everythingto point need break’,

‘means need break time away stressors’,

‘Feeling mentally exhausted’,

‘Tired drained need break’,

‘lack motivation work accomplish’,

‘Tired need sleep’,

‘mentally physically exhausted need break’,

‘drained physically mentally lack goals’,

‘bother getting bed morning purposefully skipping class",

‘taken function anymore theyre’,

‘non stop needs time relax',

"nap time',

‘think spoon theory thats used discussing chronic illness burned feels like individual run spoons dont new spoons near future’,
‘feel mentally physcially tired’,

‘mentally emotionally physically drained long week autopilot long work consistently finally crashing’,
‘Drained dont want anymore continue push’,

"Tired enjoying anymore’,

‘point energy desire tasks",

‘unable focus gets distracted easily’,

‘exhausted running fumes little energy’,

‘think means low motivation separate fatigue exhaustion overlap’,
"need week’,

"feel handle stressors emotions feel unmotivated pick’,

"im tired need break‘ ]

¥ Embedding Generation

- Convert text into numerical representations (embeddings) for clustering and modeling.
- Use methods such as TF-IDF, Word2Vec, or transformer-based models like BERT.

- Generate vector representations for all text data, creating a basis for machine learning models and clustering.

7 [23] # Create numeric representations of text
embedding model = SentenceTransformer("LaBSE")
embeddings = embedding _model.encode(df_burn_final_cleaned)

- Perform clustering on text embeddings to identify distinct groups of similar responses.

- Interpret the clusters by analyzing common terms or characteristics shared by members of each cluster.

fl [24] # Gaussian Mixture Model (GMM) Cluster Analysis

# Initialize lists to store evaluation metrics
[] # Number of clusters tested
[] # BIC scores for each cluster count

x
y

# Test different numbers of clusters (k=1 to 19)

for k in range(1, 20):

Create GMM with:

- k components (clusters)

- spherical covariance (assumes circular clusters)

- fixed random state for reproducibility

gmm = GaussianMixture(n_componentssk,
covariance_type="spherical",
random_state=999 )

+ + H+ +

# Fit model to embeddings
gmm. fit (embeddings )

# Store results
x. append(k)
y.append(gmm.bic(embeddings)) # BIC: Lower score = better fit

# Visualize results

plt.plot(x, y, marker='o')

nlt.xlahel('Number of Clusters')

plt.ylabel('BIC Score’)

plt.title( ‘Elbow Plot for Optimal Number of Clusters')

plt.show()

(4)

Elbow Plot for Optimal Number of Clusters

—340000
—342500
—345000

—347500

BIC Score

—350000
—352500
—355000

—357500

2.5 5.0 7.5 10.0 12.5 15.0 17.5
Number of Clusters

nf [25] # Determine the optimal number of clusters based on the lowest BIC value
optimal_clusters = x[np.argmin(y) ]
print(f"Optimal number of clusters (based on lowest BIC value): {optimal_clusters}")

(4)

Optimal number of clusters (based on lowest BIC value): 5

Y [26] # Apply Gaussian Mixture Model Clustering

# Initialize GMM with optimal cluster count

gmm = GaussianMixture(n_components=optimal_clusters,
covariance_type="spherical", # Assumes circular clusters
random_state=999) # For reproducibility

# Fit model and get cluster assignments
clusters = gmm.fit_predict (embeddings)

# Create dictionaries to store:
reason_dictionary = defaultdict(list) # Cleaned text by cluster
original_reason_dictionary = defaultdict(list)  # Original text by cluster

a ~ = =

# Organize texts into clusters

for idx, cluster in enumerate(clusters):
reason_dictionary[cluster].append(df_burn_final_cleaned[ idx] ) # Store cleaned version
original_reason_dictionary[cluster].append(df_burn.iloc[idx, 9@]) # Store original version

# Display cluster assignments
reason_dictionary

Sy defaultdict(list,

{3: ['stress lot head aches',
‘lacking motivation duties’,
‘ends things piling',
‘tired exhausted putting effort’,
‘Theyre tired thing happening energy',
‘exhausted little energy engage activity’,
‘tired dont motivation left',
‘energy motivation tired’,
‘means tired anymore given',
‘energy continue tasks‘,
"means point motivation continue’,
‘overwhelmed going dont motivation continue pushing",
‘means stress giving’,
‘drained work motivation’,
‘Im tired motivation work',
‘lack motivation work accomplish',
"taken function anymore theyre’,
"‘Drained dont want anymore continue push’,
‘point energy desire tasks’,
‘unable focus gets distracted easily’,
‘exhausted running fumes little energy'],

1: ['need reagather',
"mean need stop time’,
"need break break’,
‘Tired things wanting break’,
‘feeling drained want things need’,
"means mentally checked need break’,
"Tired needs days relax gain motivation’,
‘need reset destress need time recoup’,
‘tired need break',
‘Exhausted need time away',
‘need break new mentally taxing’,
‘everythingto point need break’,
‘means need break time away stressors’,
‘Tired drained need break',
‘Tired need sleep',
‘non stop needs time relax’,
"need week’,
‘im tired need break'],

2: ['says burned means energy left pour specific thing Typically occurring high demand jobs task school’,
‘means putting effort long seeing progressreward hard work dedication inturn brain feels like shuts suddenly’,
‘energy kind dragging days weekend break’,

‘motivation things loved motivation things need Physically mentally’,
‘Mind clouded feel handle involved anymore need mental break’,

‘Tired bored lifeworkschool Feeling pointless’,

‘burned think tired repeat consistently workload handle overwhelmed’,
‘tired whats going life’,

"Reaching end ability effectively multitask multiple aspects life’,

“says burned typically means feeling physically mentally emotionally exhausted point longer function effectively’,
‘overworked overwhelmed point feels like chore stresses",

‘working hard draining feel like going need break',

"theres life left lose Ive drained Ive running’,

‘means reaching end mental capacity going need mental break long’,

‘hear say burned think referring mentally physically longer fulfills way',
"say feel like social battery die dont energy tasks ones enjoy’,

‘means life moment like past point tired tired existing’,

"Physically mentally exhausted things work school’,

4 rb) # Output cleaned and original text clusters for consistency check
print("\nCleaned Text Clusters:")
for cluster, texts in reason_dictionary.items():
print(#"Cluster {cluster}: {texts} (Total: {len(texts)} comments)")

(4)

print("\nOriginal Text Clusters:")
for cluster, texts in original_reason_dictionary.items():
print(f"Cluster {cluster}: {texts} (Total: {len(texts)} comments)")

Cleaned Text Clusters:

Cluster 3: ['stress lot head aches', ‘lacking motivation duties', ‘ends things piling', ‘tired exhausted putting effort', ‘Theyre tired thing happening
Cluster 1: ['need reagather', ‘mean need stop time', ‘need break break', ‘Tired things wanting break', ‘feeling drained want things need', ‘means mental
Cluster 2: ['says burned means energy left pour specific thing Typically occurring high demand jobs task school', ‘means putting effort long seeing prog
Cluster 4: ['pretty lot', ‘tired wan na rest', ‘tired drained', 'Tired', ‘exhausted giving', ‘love anymore’, ‘anymore’, ‘want overwhelmed', ‘wrong bad w
Cluster @: ['physically mentally spiritually tired everthing going lives', ‘feel drained emotionally exhausted', ‘means mental emotional andor physical

Original Text Clusters:

Cluster 3: ['stress out and a lot of head aches', ‘That one is lacking motivation to go throughout their duties. ', ‘That we are at our ends with the th
Cluster 1: ['I need a to reagather myself', 'That mean that you need to stop, and take time for yourself.', ‘They need a break or they will break', ‘Tir
Cluster 2: ['When someone says they are burned out that means that they have no more energy left to pour into that specific thing. Typically occurring i
Cluster 4: ["They are pretty much done with everything, they have been through a lot and can't give out any more than what they have already done.", ‘Th

Cluster @: ['They are physically, mentally, spiritually are tired with everthing that is going on in their lives.

4

v Theme Generation and Analysis Using LLMS

- Summarize key themes for each cluster to identify overarching topics or patterns using LLMS to capture all text

inputs.

- Use a text summarization model or manually review representative responses from each cluster.

- Provide detailed descriptions of the cluster themes to aid interpretation and support decision-making.

nf oO # Theme Analysis Pipeline Using Hugging Face's T5 Model

(4)

# Initialize text generation model for theme analysis
# Using Flan-T5-large (instead of base) for better quality and coherence in outputs
summarizer = pipeline("text2text-generation",

model="google/flan-t5-large",

token=huggingface_api_key)

def process_chunk(chunk):

Args:
chunk: List of related text responses
Returns:
str: 3-5 word theme capturing main concept
prompt = f"""Here are related survey responses:
{' | '.join(chunk) }
What single distinctive theme captures their shared meaning?

Y Os_ completed at 1:05AM
Be specific but brief, using about 3-5 words."""
try:
return summarizer(prompt, max_length=20, min_length=2)[@]['generated_text'].strip()
except Exception as e:
print(f"Error: {e}")
return ""

def expand_theme(texts):
Generate detailed analysis of theme with impact assessment.
Args:
texts: List of all responses in cluster
Returns:
str: Two-sentence analysis of theme and its implications
combined_texts = " | ".join(texts[:15]) # Use first 15 responses for context
prompt = f"""These survey responses share a common theme:
{combined_texts}
Write 2 brief sentences that:
1. Summarize the key theme's manifestation
2. Highlight its main impact
Be direct and specific."""
civ
return summarizer(prompt, max_length=100, min_length=20)[0]['generated_text'].strip()
except Exception as e:
print(f"Error generating expansion: {e}")
return "Expansion generation failed"

def get_cluster_theme(texts, chunk_size=12):
Process large text clusters in parallel chunks for efficiency.
Args:
texts: List of all texts in cluster
chunk_size: Number of texts per chunk
Returns:
str: Unified theme for entire cluster
chunks = [texts[i:i + chunk_size] for i in range(@, len(texts), chunk_size) ]
with ThreadPoolExecutor(max_workers=3) as executor:
themes = list(executor.map(process_chunk, chunks) )
return themes[@] if len(themes) == 1 else process_chunk(themes)

def process_cluster(cluster_data):
Generate comprehensive analysis for each cluster.
Args:
cluster_data: Tuple of (cluster_id, texts)
Returns:
dict: Complete analysis including theme, size, expansion, and examples
cluster, texts = cluster_data
return {
‘Cluster #': f"{cluster}",
"Theme': get_cluster_theme(texts),
"Size': len(texts),
‘Expansion’: expand_theme(texts),
‘Sample Responses': '\n'.join([f"* {text.strip()}" for text in texts[:3]])
}

# Process all clusters in parallel for efficiency
with ThreadPoolExecutor(max_workers=3) as executor:

cluster_info = list(executor.map(process_cluster, original_reason_dictionary.items()))
df_clusters = pd.DataFrame(cluster_info).sort_values('Cluster #')

# Create presentation-ready DataFrame with 1-based indexing
presentation_df = pd.DataFrame({
"Cluster': [f"Cluster {i+1}" for i in range(len(df_clusters) )],
‘Theme’: df_clusters['Theme'].values,
"Size': df_clusters['Size'].values,
"Expanded Analysis': df_clusters['Expansion'].values,
"Example Responses': df_clusters['Sample Responses‘ ].values

})

def style _df(df):
Apply professional styling to DataFrame for presentation.
Includes:
- Alternating row colors
- Professional fonts and spacing
- Clear headers and borders
return df.style\
.set_properties (**{
"text-align': ‘left',
‘white-space’: 'pre-wrap',
‘font-size’: ‘'1l1pt',
‘padding’: '1@px',
*max-width': '3@@px'
})\
.set_table_styles([
{'selector': ‘th’,
‘props': [('background-color', ‘#f2f2f2'),
('color', '‘black'),
('font-weight', 'bold')]},
{'selector': 'caption',
‘props': [('caption-side', ‘top'),
('font-size', '14pt')]},
{'selector': ‘tr:nth-child(even)',
‘props': [('background-color', '#f9f9f9')]},
])\
.set_caption("Theme Analysis of Survey Responses")\
-hide(axis='index' )

# Display final styled results
styled_df = style_df(presentation_df)
display(styled_df)

model.safetensors: 100% [i NE 3.13G/3.13G [00:39<00:00, 185MB/s]
generation_config.json: 100% [NS 147/147 [00:00<00:00, 7.74kB/s]
tokenizer_config.json: 100% (II 2.54K/2.54k [00:00<00:00, 160kB/s]
spiece.model: 100% (TIS = 792k/792k [00:00<00:00, 39.5MB/s]
tokenizerjson: 100% [IS 2.421/2.42M [00:00<00:00, 31.1MB/s]

special_tokens_map.json: 100% [INS 2.20k/2.20k [00:00<00:00, 116kB/s]

Theme Analysis of Survey Responses

Cluster Theme Size Expanded Analysis

The key theme is that people are physically,

Cluster 1 They are physically and mentally exhausted 12 mentary and emictionemy:- exhausted. It

and/or physical limits.

1. They are tired and need a break. 2. They
are drained and need some time away to just

Cluster 2 They need a reset or to destress. 18 ba. with theriselves snd fokhave ido

anything.

1. Burned out means they are physically,
mentally, and emotionally exhausted to the

Cluster 3 Burned out 33 point where they can no longer function

effectively. 2. It means that they are reaching
the end of their mental capacity and are going

to need a mental break before long.

The survey respondents are tired and
They are overwhelmed with everything going 4 exhausted. They are overwhelmed with
on everything going on, and don't have

motivation to continue pushing through.

Cluster 4

The survey respondents are tired and ready
Cluster5 exhausted 25 to give up. They have reached their breaking
point. They are tired and ready to give up.

Y Visualization of Theme Distribution

df oO # Prepare data for visualization from df_clusters DataFrame

(4)

cluster_counts = {row['Theme']: row['Size'] for _, row in df_clusters.iterrows()}

# Create the visualization
plt.figure(figsize=(14, 8)) # Larger figure for better readability

means they are at their mental, emotional,

Example Responses

* They are physically, mentally, spiritually are

tired with everthing t
lives.

hat is going on in their

* They feel drained and emotionally

exhausted.

* It means they are at their mental, emotional,
and/or physical limits.

* | need a to reagath

er myself

* That mean that you need to stop, and take

time for yourself.
* They need a break

or they will break

* When someone says they are burned out
that means that they have no more energy left
to pour into that specific thing. Typically
occurring in high demand jobs or task such as

school

* to me it means putting all your effort into

something for so lon

g and never seeing any

progress/reward from the hard work and

dedication, inturn yo

ur brain feels like it just

shuts off and suddenly you cant get anything

at all done.

¢ Being out of energy and kind of dragging
through the days until the weekend or a break

* stress out and a lot of head aches

* That one is lacking

motivation to go

throughout their duties.

* That we are at our

ends with the things that

are piling up for us, and that it is all becoming
too much. We are done.

ee hh ee

* They are pretty mu

a PTR eee
Ch QONe WIth CVeEryuiilg,

they have been through a lot and can't give
out any more than what they have already

done.
* That they are tired
* tired or drained

bars = plt.bar(cluster_counts.keys(), cluster_counts.values(), color='lightblue', edgecolor='black', linewidth=1)

# Update x-axis labels to be more readable

plt.xlabel('Cluster Themes', fontsize=14, labelpad=15)

plt.ylabel( ‘Number of Comments', fontsize=14)

plt.title('Distribution of Comments Across Themes', fontsize=16, pad=20)

# Rotate and align the tick labels, wrapping long labels for better appearance
wrapped_labels = [textwrap.fill(label, 2@) for label in cluster_counts.keys() ]
plt.xticks(range(len(wrapped_labels)), wrapped_labels, rotation=30, ha='right', fontsize=12)

# Add value labels on top of each bar with formatting
for bar in bars:
plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
str(int(bar.get_height())),
ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# Add a grid for easier comparison
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)

# Set y-axis limits to add more space at top
max_height = max(cluster_counts.values())
plt.ylim(@®, max_height * 1.2) # Add 20% padding at the top

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust layout to ensure labels are not cut off
plt.tight_layout()

# Show the plot
plt.show()

Distribution of Comments Across Themes

35

25

Number of Comments

Ciuster Themes

v Keyword Visualization

- Extract keywords from text data to identify important terms associated with clusters or sentiment.

- Visualize or list the keywords to provide insights into the core topics of the dataset.

- rb) # Keyword Analysis and Visualization

v
Os

(4)

(4)

def analyze_keywords(texts):

Extract and count keywords from pre-cleaned texts
Args:

texts: List of pre-cleaned text responses
Returns:

Counter object with word frequencies
# Combine all texts into single word list
all_words = []
for text in texts:

all_words.extend(text.split() )

return Counter(all_words) # Return word frequency counts

# Analyze keywords across all clusters

all_keywords = Counter() # Initialize counter

for texts in reason_dictionary.values():
cluster_keywords = analyze_keywords(texts)
all_keywords.update(cluster_keywords) # Combine frequencies

# Create and format DataFrame

keyword_df = pd.DataFrame.from_dict(all_keywords, orient='index', columns=['count' ])
keyword_df = keyword_df.sort_values('count', ascending=True)
keyword_df['percentage'] = (keyword_df['count'] / sum(keyword_df['count'])) * 100

# Visualize top 15 keywords
plt.figure(figsize=(12, 8))
top_keywords = keyword_df.tail(15) # Get top 15

# Create horizontal bar chart

bars = plt.barh(range(len(top_keywords)),
top_keywords['count'],
color='skyblue’ )

# Add labels and formatting

plt.yticks(range(len(top_keywords)), top_keyw

rds.index)
for i, bar in enumerate(bars):
count = top_keywords['count'].iloc[i]
percentage = top_keywords[ 'percentage'].iloc[i]
plt.text(bar.get_width(),
bar.get_y() + bar.get_height()/2,
f' {count} ({percentage: .1f}%)',
va='center' )

plt.title('Most Common Words Across All Clusters')
plt.xlabel('Frequency' )

plt.tight_layout()

plt.show()

# Display tabular results

print("\nKeyword Analysis Results:")

print("=" * 60)

print(top_keywords.sort_values('count', ascending=False).to_string())

Most Common Words Across All Clusters

tired
need

mentally

break 16 (2.9%)

means 14 (2.5%)
drained 13 (2.3%)
motivation 12 (2.2%)
exhausted 12 (2.2%)
physically 10 (1.8%)
energy 10 (1.8%)
things 10 (1.8%)
like 9 (1.6%)
life 8 (1.4%)
anymore 8 (1.4%)
feel 8 (1.4%)
0 5 10 15
Frequency

Keyword Analysis Results:

count percentage

tired 26 4.684685
need 21 3.783784
mentally 17 3.063063
break 16 2.882883
means 14 2.522523
drained 13 2.342342
exhausted 12 2.162162
motivation 12 2.162162
things 10 1.801802

Cluster Plot

e Visualizes text clusters with interactive hover details.

e Displays cluster sizes and top terms.

import plotly.express as px
from collections import Counter

# Define a custom color scheme
color_scheme = [

]

"#E63946', # Bright red
"#1D3557', # Deep navy blue
"#2A9D8F', # Teal
"#F4A261', # Orange
"#A8DADC' # Light cyan

# Ensure clusters are categorical to enforce correct color mapping
clusters = [str(cluster) for cluster in clusters] # Convert to strings for categorical mapping

# Create scatter plot with embeddings and hover text
fig = px.scatter(

)

x=embeddings[:, @],

y=embeddings[:, 1],

color=clusters, # Color by cluster assignments

title='Text Cluster Visualization by Category',

labels={'x': "Dimension 1", ‘'y': ‘Dimension 2', ‘color': 'Cluster'},
opacity=0.8, # Increased opacity for better visibility
color_discrete_sequence=color_scheme, # Apply custom colors
hover_data={'text': df_burn_final} # Add original text as hover data

# Update layout for better readability
fig.update_layout(

)

plot_bgcolor='rgba(240, 240, 250, @.5)', # Light blue-gray background
width=1000,
height=600,
title_x=0.5, # Center title
showlegend=True,
legend=dict(
bgcolor='rgba(255, 255, 255, @.8)', # Semi-transparent white background
bordercolor='rgba(@, @, 0, @.2)', # Light border
borderwidth=1
)s
hovermode='closest’,
hoverlabel=dict(
bgcolor="white",
font_size=12,
font_family="Arial"

# Add gridlines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128, 128, 128, @.2)')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128, 128, 128, @.2)')

# Get cluster statistics

cluster_counts = Counter(clusters)

print("\nCluster Distribution:")

for cluster, count in sorted(cluster_counts.items()):

print(#"Cluster {cluster}: {count} responses")

# Define the get_top_terms function
def get_top_terms(cleaned_texts, n=10):

Extract the top n most common terms from the cleaned text data.

all_words = * join(cleaned_texts).split()
common_terms = Counter(all_words) .most_common(n)
return [term for term, _ in common_terms ]

# Get top terms from the cleaned texts
top_terms = get_top_terms(df_burn_final_cleaned)

print("\nMost Common Terms:",

» |'.join(top_terms) )

# Calculate total points
total_points = len(clusters)
print(f"\nTotal Responses: {total_points}")

# Save to HTML for interactive viewing
fig.write_html("cluster_visualization.html")

# Show plot
fig.show()

Cluster Distribution:

Cluster @: 12 responses
Cluster 1: 18 responses
Cluster 2: 33 responses
Cluster 3: 21 responses

21

17 (3.1%)

20

and just wanna rest.

*v.o8 eda:

(3.8%)

25

» ‘They feel drained and emotionally

»

Cluster 4: 25 responses

Most Common Terms: tired, need, mentally, break, means, drained, motivation, exhausted, energy, physically

Total Responses: 169

Dimension 2

0.08

0.06

0.04

0.02

-0.02

—0.04

—0.06

Text Cluster Visualization by Category

e
e
e
e
e
e
ee
e e
e e
ee e
e
e
e
e
e
e e
e
e
e
—0.06 -—0.04 -—0.02

° o
e
® e
e e
° e 6
ee e
° ee
e °
°
e we ant e °
. @
° e
e
ee 6 e
°. e e °
e @
e
e e
e e. oe
s . C
°
e
o e
e
e
0 0.02 0.04

Dimension 1

Colab paid products - Cancel contracts here

Y Os

Y Os

completed at 1:05AM
completed at 1:05AM

0.06

Cluster
e 3
e 1
e 2
e 4
f°)

x


# **Burnout Topic Analysis**
###Research Question:

*   How do students define burnout in their own words?

## Set up the Google Colab environment
###Load the packages in the code cell below by pressing "ctrl + Enter" or clicking the play button on the left of the cell.


```python
# import necessary libaries and packages
!pip install bertopic
!pip install transformers
!pip install sentence-transformers --quiet
!pip install wordcloud
!pip install plotly
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
```

# Data Loading and Inital Setup
### - Import necessary libraries and packages for data manipulation, modeling, and visualization.
### - Load datasets from local files, databases, or other sources.

```python
# load the dataset by uploading the file
data = pd.read_csv('/content/Burnout_Data.csv')
```

```python
# Load a CSV file from Google Drive
drive.mount('/content/drive')
file_path = '/content/drive/My Drive/RU Org Psych/Fall 2024/Burnout_Data.csv'
data = pd.read_csv(file_path)

# Display the data
data
```

```python
# Remove the first two rows from the dataset
data = data.iloc[2:].reset_index(drop=True)
```

## Preparing the Data Structure


```python
# Prepare the text data for analysis by isolating the column of text data
df_burn = data[['burnopen']].copy()
df_burn.dropna(inplace=True)
df_burn = df_burn.astype(str)
df_burn_final = df_burn.values.flatten()
df_burn_final
```

```python
# Output the number of text responses
print(f"Total number of responses for 'burnopen': {data['burnopen'].dropna().shape[0]}")
```

# Word Cloud Generation

```python
# Combine the list into a single string as word clouds take a string input
text = " ".join(review for review in df_burn_final)

# Create the word cloud object with specific parameters for clarity
wordcloud = WordCloud(
    background_color="white",  # Set background color to white
    colormap="viridis",        # Use the 'viridis' colormap for better contrast
    width=800,                 # Set the width of the word cloud image
    height=400,                # Set the height of the word cloud image
    max_words=200,             # Set the maximum number of words in the cloud
    max_font_size=100,         # Set the maximum font size for words
    scale=3,                   # Increase the scale to improve image resolution
    random_state=42            # Set a random seed for reproducibility
).generate(text)

# Display the generated image:
plt.figure(figsize=(12, 6))   # Adjust the figure size for better visibility
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
```

# Sentiment Analysis using Dictionary Method
### - Apply sentiment analysis models to understand emotional tone in text (e.g., positive, negative, neutral).
### - Use pre-trained models such as VADER

```python
# Initialize VADER Sentiment Analysis
nltk.download('vader_lexicon')  # Download required VADER lexicon
sia = SentimentIntensityAnalyzer()  # Create VADER sentiment analyzer instance

# List to store sentiment classifications
sentiments = []

# Analyze sentiment for each response
for review in df_burn_final:
   # Get polarity scores using VADER
   # Returns dict with pos, neg, neu and compound scores
   sentiment_scores = sia.polarity_scores(review)

   # Classify sentiment based on compound score
   # Using standard thresholds:
   # >= 0.05 for positive
   # <= -0.05 for negative
   # Between -0.05 and 0.05 for neutral
   if sentiment_scores['compound'] >= 0.05:
       sentiment = 'Positive'
   elif sentiment_scores['compound'] <= -0.05:
       sentiment = 'Negative'
   else:
       sentiment = 'Neutral'

   # Add classification to results list
   sentiments.append(sentiment)

# Calculate sentiment distribution
# Count number of each sentiment using list comprehension
positive_reviews = sum(1 for sentiment in sentiments if sentiment == 'Positive')
negative_reviews = sum(1 for sentiment in sentiments if sentiment == 'Negative')
neutral_reviews = sum(1 for sentiment in sentiments if sentiment == 'Neutral')

# Print results
print(f"Number of Positive Reviews: {positive_reviews}")
print(f"Number of Negative Reviews: {negative_reviews}")
print(f"Number of Neutral Reviews: {neutral_reviews}")
```

```python
# Create a pie chart to visualize the sentiment distribution
labels = ['Positive', 'Negative', 'Neutral']
sizes = [positive_reviews, negative_reviews, neutral_reviews]
colors = ['green', 'red', 'gray']

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Sentiment Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
```

```python
# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Initialize lists to store the categorized reviews
positive_reviews = []
neutral_reviews = []
negative_reviews = []

# Iterate over each review
for review in df_burn_final:
    # Calculate sentiment scores for each review
    sentiment_scores = sia.polarity_scores(review)

    # Categorize the review based on the compound score
    if sentiment_scores['compound'] >= 0.05:
        positive_reviews.append(review)
        neutral_reviews.append('')
        negative_reviews.append('')
    elif sentiment_scores['compound'] <= -0.05:
        positive_reviews.append('')
        neutral_reviews.append('')
        negative_reviews.append(review)
    else:
        positive_reviews.append('')
        neutral_reviews.append(review)
        negative_reviews.append('')

# Create a new DataFrame with the categorized reviews
categorized_reviews_df = pd.DataFrame({
    'Positive Reviews': positive_reviews,
    'Neutral Reviews': neutral_reviews,
    'Negative Reviews': negative_reviews
})

# Display the first few rows of the new DataFrame
categorized_reviews_df
```

```python
# Create a dataframe for all sentiment scores added
compound_scores = []

for review in df_burn_final:
    # Calculate sentiment scores for each review
    sentiment_scores = sia.polarity_scores(review)
    compound_scores.append(sentiment_scores['compound'])

# Calculate the overall sentiment score based on an average
overall_sentiment_score = sum(compound_scores) / len(compound_scores)

# Determine the overall sentiment label based on the overall score
if overall_sentiment_score >= 0.05:
    overall_sentiment_label = 'Positive'
elif overall_sentiment_score <= -0.05:
    overall_sentiment_label = 'Negative'
else:
    overall_sentiment_label = 'Neutral'

# Print the overall sentiment score and label
print(f"Overall Sentiment Score: {overall_sentiment_score}")
print(f"Overall Sentiment Label: {overall_sentiment_label}")
```

# Accessing the Hugging Face.com API for Large Language Model Usage in Code

Hugging Face API Authentication & Setup Guide

For detailed API documentation, visit:
https://huggingface.co/docs/hub/en/security-tokens

This section handles the authentication setup for accessing Hugging Face's models and services.
You'll need an API key to access the models used in this analysis.

Quick Setup:
- Create a free account at huggingface.co
- Navigate to Settings > Access Tokens
- Generate a new access token
- Paste your token in the input below

Important Security Notes:
- Never share or commit your API key
- Regenerate immediately if exposed
- Monitor for unauthorized usage

Usage in this Analysis:
- Model access for text classification
- Sentiment analysis
- Theme generation
- Text embedding creation

```python
# Hugging Face API Key Configuration

# Request API key from user
# This is needed to access Hugging Face's models and pipelines
# The API key is a personal access token that authenticates your requests
huggingface_api_key = input("Please enter your Hugging Face API key: ")

# Example API key format (commented out for security):
#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
```

# Sentiment Analysis Using LLMs
### - Apply sentiment analysis models to understand emotional tone in text (e.g., positive, negative, neutral).
### - Use pre-trained models such as a deep learning-based transformer.

```python
# Initialize Hugging Face Sentiment Analysis Pipeline
# Using multilingual BERT model trained for sentiment classification
# This model can handle text in multiple languages and returns ratings from 1-5
sentiment_analysis = pipeline(
   task="text-classification",                                    # Specify the NLP task
   model="nlptown/bert-base-multilingual-uncased-sentiment",     # Pre-trained model selection
   token=huggingface_api_key                                     # Authentication token
)

def get_sentiment_hf_api(text):
   """
   Analyze sentiment of input text using Hugging Face's BERT model.

   Args:
       text: Input text to analyze (can be any datatype, will be converted to string)

   Returns:
       str: Sentiment classification ('positive', 'negative', or 'neutral')

   The model uses a 5-point scale where:
   - 1-2: Negative sentiment
   - 3: Neutral sentiment
   - 4-5: Positive sentiment
   """
   try:
       # Input validation and preprocessing
       text = str(text)                    # Convert input to string
       if not text.strip():                # Handle empty/whitespace input
           return 'neutral'

       # Get model prediction
       response = sentiment_analysis(text)[0]   # Model returns list of predictions
       score = int(response['label'][0])        # Extract numerical rating (1-5)

       # Convert 5-point scale to trinary classification
       if score >= 4:                          # Ratings 4-5 are positive
           return 'positive'
       elif score <= 2:                        # Ratings 1-2 are negative
           return 'negative'
       else:                                   # Rating 3 is neutral
           return 'neutral'

   except Exception as e:
       # Error handling: log error and return safe default
       print(f"Error processing text: {e}")
       return 'neutral'
```

```python
# Create the sentiment DataFrame
sentiment_df = pd.DataFrame({
    'Document': df_burn_final,
    'Sentiment': [get_sentiment_hf_api(doc) for doc in df_burn_final]
})
```

```python
# Display sentiment distribution
sentiment_distribution = sentiment_df['Sentiment'].value_counts()
print("\nSentiment Distribution:")
print(sentiment_distribution)
```

```python
# Add percentage distribution
sentiment_percentages = sentiment_distribution / len(sentiment_df) * 100
print("\nSentiment Distribution (%):")
print(sentiment_percentages.round(2))
```

```python
# Plot sentiment distribution
plt.figure(figsize=(10, 6))
plt.bar(sentiment_distribution.index, sentiment_distribution.values, color=['red', 'blue', 'green'])
plt.xlabel('Sentiment')
plt.ylabel('Number of Comments')
plt.title('Sentiment Distribution')
plt.show()
```

```python
# Calculate overall sentiment score (including Neutral)
sentiment_score_mapping = {'positive': 1, 'neutral': 0, 'negative': -1}
sentiment_df['Score'] = sentiment_df['Sentiment'].map(sentiment_score_mapping)
overall_sentiment_score = sentiment_df['Score'].mean()
print(f"Overall Sentiment Score: {overall_sentiment_score}")
```

#Feature Extraction and Embedding Generation

```python
# Import and Initialize Sentence Transformer Model

# Import the SentenceTransformer class from sentence-transformers library
# This library provides easy access to various transformer models optimized for creating sentence embeddings
from sentence_transformers import SentenceTransformer

# Initialize the Language-agnostic BERT Sentence Embedding (LaBSE) model
# LaBSE is specifically designed to:
# - Create meaningful embeddings that work across 109 languages
# - Generate similar embeddings for semantically similar sentences, even in different languages
# - Produce fixed-size vector representations (768 dimensions)
embedding_model = SentenceTransformer("LaBSE")
```

```python
# NLTK (Natural Language Toolkit) Data Setup

# Download required NLTK packages
nltk.download('vader_lexicon')   # For sentiment analysis with VADER
nltk.download('punkt_tab')           # For sentence tokenization
nltk.download('stopwords')       # For filtering common words

# Set data path for NLTK resources
nltk.data.path.append('/root/nltk_data')   # Ensures NLTK can find downloaded resources
```

#Text Preprocessing and Cleaning
### - Remove punctuation, special characters, and extra whitespace.
### - Tokenize the text data into individual words or phrases.
### - Remove stopwords to focus on meaningful words.
### - Apply additional techniques like stemming or lemmatization to standardize word forms.
### - Store cleaned text for subsequent analysis.

```python
# Text Preprocessing for Topic Modeling

# Create comprehensive stopwords set by combining:
# 1. NLTK English stopwords (e.g., 'the', 'is', 'at', 'which')
# 2. Scikit-learn's stopwords (additional common English words)
stop_words = set(nltk_stopwords.words('english')).union(ENGLISH_STOP_WORDS)

def remove_stopwords(sentence):
   """
   Clean and preprocess text by removing unwanted characters and common words.

   Args:
       sentence (str): Raw text input

   Returns:
       str: Cleaned text with stopwords and special characters removed
   """
   # Step 1: Remove punctuation and special characters
   # [^\w\s] matches any character that's not a word character (\w) or whitespace (\s)
   sentence = re.sub(r'[^\w\s]', '', sentence)

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
```

# Embedding Generation
### - Convert text into numerical representations (embeddings) for clustering and modeling.
### - Use methods such as TF-IDF, Word2Vec, or transformer-based models like BERT.
### - Generate vector representations for all text data, creating a basis for machine learning models and clustering.

```python
# Create numeric representations of text
embedding_model = SentenceTransformer("LaBSE")
embeddings = embedding_model.encode(df_burn_final_cleaned)
```

# Cluster Analysis
###- Perform clustering on text embeddings to identify distinct groups of similar responses.
### - Interpret the clusters by analyzing common terms or characteristics shared by members of each cluster.

```python
# Gaussian Mixture Model (GMM) Cluster Analysis

# Initialize lists to store evaluation metrics
x = []  # Number of clusters tested
y = []  # BIC scores for each cluster count

# Test different numbers of clusters (k=1 to 19)
for k in range(1, 20):
   # Create GMM with:
   # - k components (clusters)
   # - spherical covariance (assumes circular clusters)
   # - fixed random state for reproducibility
   gmm = GaussianMixture(n_components=k,
                        covariance_type="spherical",
                        random_state=999)

   # Fit model to embeddings
   gmm.fit(embeddings)

   # Store results
   x.append(k)
   y.append(gmm.bic(embeddings))  # BIC: Lower score = better fit

# Visualize results
plt.plot(x, y, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('BIC Score')
plt.title('Elbow Plot for Optimal Number of Clusters')
plt.show()
```

```python
# Determine the optimal number of clusters based on the lowest BIC value
optimal_clusters = x[np.argmin(y)]
print(f"Optimal number of clusters (based on lowest BIC value): {optimal_clusters}")
```

```python
# Apply Gaussian Mixture Model Clustering

# Initialize GMM with optimal cluster count
gmm = GaussianMixture(n_components=optimal_clusters,
                     covariance_type="spherical",  # Assumes circular clusters
                     random_state=999)             # For reproducibility

# Fit model and get cluster assignments
clusters = gmm.fit_predict(embeddings)

# Create dictionaries to store:
reason_dictionary = defaultdict(list)           # Cleaned text by cluster
original_reason_dictionary = defaultdict(list)   # Original text by cluster

# Organize texts into clusters
for idx, cluster in enumerate(clusters):
   reason_dictionary[cluster].append(df_burn_final_cleaned[idx])          # Store cleaned version
   original_reason_dictionary[cluster].append(df_burn.iloc[idx, 0])       # Store original version

# Display cluster assignments
reason_dictionary
```

```python
# Output cleaned and original text clusters for consistency check
print("\nCleaned Text Clusters:")
for cluster, texts in reason_dictionary.items():
    print(f"Cluster {cluster}: {texts} (Total: {len(texts)} comments)")

print("\nOriginal Text Clusters:")
for cluster, texts in original_reason_dictionary.items():
    print(f"Cluster {cluster}: {texts} (Total: {len(texts)} comments)")
```

#Theme Generation and Analysis Using LLMS
### - Summarize key themes for each cluster to identify overarching topics or patterns using LLMS to capture all text inputs.
### - Use a text summarization model or manually review representative responses from each cluster.
### - Provide detailed descriptions of the cluster themes to aid interpretation and support decision-making.

```python
# Theme Analysis Pipeline Using Hugging Face's T5 Model

# Initialize text generation model for theme analysis
# Using Flan-T5-large (instead of base) for better quality and coherence in outputs
summarizer = pipeline("text2text-generation",
                    model="google/flan-t5-large",
                    token=huggingface_api_key)

def process_chunk(chunk):
   """
   Generate a concise theme from a chunk of related texts.
   Args:
       chunk: List of related text responses
   Returns:
       str: 3-5 word theme capturing main concept
   """
   prompt = f"""Here are related survey responses:
   {' | '.join(chunk)}
   What single distinctive theme captures their shared meaning?
   Be specific but brief, using about 3-5 words."""
   try:
       return summarizer(prompt, max_length=20, min_length=2)[0]['generated_text'].strip()
   except Exception as e:
       print(f"Error: {e}")
       return ""

def expand_theme(texts):
   """
   Generate detailed analysis of theme with impact assessment.
   Args:
       texts: List of all responses in cluster
   Returns:
       str: Two-sentence analysis of theme and its implications
   """
   combined_texts = " | ".join(texts[:15])  # Use first 15 responses for context
   prompt = f"""These survey responses share a common theme:
   {combined_texts}
   Write 2 brief sentences that:
   1. Summarize the key theme's manifestation
   2. Highlight its main impact
   Be direct and specific."""
   try:
       return summarizer(prompt, max_length=100, min_length=20)[0]['generated_text'].strip()
   except Exception as e:
       print(f"Error generating expansion: {e}")
       return "Expansion generation failed"

def get_cluster_theme(texts, chunk_size=12):
   """
   Process large text clusters in parallel chunks for efficiency.
   Args:
       texts: List of all texts in cluster
       chunk_size: Number of texts per chunk
   Returns:
       str: Unified theme for entire cluster
   """
   chunks = [texts[i:i + chunk_size] for i in range(0, len(texts), chunk_size)]
   with ThreadPoolExecutor(max_workers=3) as executor:
       themes = list(executor.map(process_chunk, chunks))
   return themes[0] if len(themes) == 1 else process_chunk(themes)

def process_cluster(cluster_data):
   """
   Generate comprehensive analysis for each cluster.
   Args:
       cluster_data: Tuple of (cluster_id, texts)
   Returns:
       dict: Complete analysis including theme, size, expansion, and examples
   """
   cluster, texts = cluster_data
   return {
       'Cluster #': f"{cluster}",
       'Theme': get_cluster_theme(texts),
       'Size': len(texts),
       'Expansion': expand_theme(texts),
       'Sample Responses': '\n'.join([f"• {text.strip()}" for text in texts[:3]])
   }

# Process all clusters in parallel for efficiency
with ThreadPoolExecutor(max_workers=3) as executor:
   cluster_info = list(executor.map(process_cluster, original_reason_dictionary.items()))
df_clusters = pd.DataFrame(cluster_info).sort_values('Cluster #')

# Create presentation-ready DataFrame with 1-based indexing
presentation_df = pd.DataFrame({
   'Cluster': [f"Cluster {i+1}" for i in range(len(df_clusters))],
   'Theme': df_clusters['Theme'].values,
   'Size': df_clusters['Size'].values,
   'Expanded Analysis': df_clusters['Expansion'].values,
   'Example Responses': df_clusters['Sample Responses'].values
})

def style_df(df):
   """
   Apply professional styling to DataFrame for presentation.
   Includes:
   - Alternating row colors
   - Professional fonts and spacing
   - Clear headers and borders
   """
   return df.style\
       .set_properties(**{
           'text-align': 'left',
           'white-space': 'pre-wrap',
           'font-size': '11pt',
           'padding': '10px',
           'max-width': '300px'
       })\
       .set_table_styles([
           {'selector': 'th',
            'props': [('background-color', '#f2f2f2'),
                     ('color', 'black'),
                     ('font-weight', 'bold')]},
           {'selector': 'caption',
            'props': [('caption-side', 'top'),
                     ('font-size', '14pt')]},
           {'selector': 'tr:nth-child(even)',
            'props': [('background-color', '#f9f9f9')]},
       ])\
       .set_caption("Theme Analysis of Survey Responses")\
       .hide(axis='index')

# Display final styled results
styled_df = style_df(presentation_df)
display(styled_df)
```

#Visualization of Theme Distribution

```python
# Prepare data for visualization from df_clusters DataFrame
cluster_counts = {row['Theme']: row['Size'] for _, row in df_clusters.iterrows()}

# Create the visualization
plt.figure(figsize=(14, 8))  # Larger figure for better readability
bars = plt.bar(cluster_counts.keys(), cluster_counts.values(), color='lightblue', edgecolor='black', linewidth=1)

# Update x-axis labels to be more readable
plt.xlabel('Cluster Themes', fontsize=14, labelpad=15)
plt.ylabel('Number of Comments', fontsize=14)
plt.title('Distribution of Comments Across Themes', fontsize=16, pad=20)

# Rotate and align the tick labels, wrapping long labels for better appearance
wrapped_labels = [textwrap.fill(label, 20) for label in cluster_counts.keys()]
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
plt.ylim(0, max_height * 1.2)  # Add 20% padding at the top

# Remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Adjust layout to ensure labels are not cut off
plt.tight_layout()

# Show the plot
plt.show()
```

#Keyword Visualization
### - Extract keywords from text data to identify important terms associated with clusters or sentiment.
### - Visualize or list the keywords to provide insights into the core topics of the dataset.


```python
# Keyword Analysis and Visualization

def analyze_keywords(texts):
   """
   Extract and count keywords from pre-cleaned texts
   Args:
       texts: List of pre-cleaned text responses
   Returns:
       Counter object with word frequencies
   """
   # Combine all texts into single word list
   all_words = []
   for text in texts:
       all_words.extend(text.split())

   return Counter(all_words)  # Return word frequency counts

# Analyze keywords across all clusters
all_keywords = Counter()  # Initialize counter
for texts in reason_dictionary.values():
   cluster_keywords = analyze_keywords(texts)
   all_keywords.update(cluster_keywords)  # Combine frequencies

# Create and format DataFrame
keyword_df = pd.DataFrame.from_dict(all_keywords, orient='index', columns=['count'])
keyword_df = keyword_df.sort_values('count', ascending=True)
keyword_df['percentage'] = (keyword_df['count'] / sum(keyword_df['count'])) * 100

# Visualize top 15 keywords
plt.figure(figsize=(12, 8))
top_keywords = keyword_df.tail(15)  # Get top 15

# Create horizontal bar chart
bars = plt.barh(range(len(top_keywords)),
               top_keywords['count'],
               color='skyblue')

# Add labels and formatting
plt.yticks(range(len(top_keywords)), top_keywords.index)
for i, bar in enumerate(bars):
   count = top_keywords['count'].iloc[i]
   percentage = top_keywords['percentage'].iloc[i]
   plt.text(bar.get_width(),
            bar.get_y() + bar.get_height()/2,
            f' {count} ({percentage:.1f}%)',
            va='center')

plt.title('Most Common Words Across All Clusters')
plt.xlabel('Frequency')
plt.tight_layout()
plt.show()

# Display tabular results
print("\nKeyword Analysis Results:")
print("=" * 60)
print(top_keywords.sort_values('count', ascending=False).to_string())
```

#Cluster Plot
- Visualizes text clusters with interactive hover details.
- Displays cluster sizes and top terms.

```python
import plotly.express as px
from collections import Counter

# Define a custom color scheme
color_scheme = [
    '#E63946',  # Bright red
    '#1D3557',  # Deep navy blue
    '#2A9D8F',  # Teal
    '#F4A261',  # Orange
    '#A8DADC'   # Light cyan
]

# Ensure clusters are categorical to enforce correct color mapping
clusters = [str(cluster) for cluster in clusters]  # Convert to strings for categorical mapping

# Create scatter plot with embeddings and hover text
fig = px.scatter(
    x=embeddings[:, 0],
    y=embeddings[:, 1],
    color=clusters,  # Color by cluster assignments
    title='Text Cluster Visualization by Category',
    labels={'x': 'Dimension 1', 'y': 'Dimension 2', 'color': 'Cluster'},
    opacity=0.8,  # Increased opacity for better visibility
    color_discrete_sequence=color_scheme,  # Apply custom colors
    hover_data={'text': df_burn_final}  # Add original text as hover data
)

# Update layout for better readability
fig.update_layout(
    plot_bgcolor='rgba(240, 240, 250, 0.5)',  # Light blue-gray background
    width=1000,
    height=600,
    title_x=0.5,  # Center title
    showlegend=True,
    legend=dict(
        bgcolor='rgba(255, 255, 255, 0.8)',  # Semi-transparent white background
        bordercolor='rgba(0, 0, 0, 0.2)',    # Light border
        borderwidth=1
    ),
    hovermode='closest',
    hoverlabel=dict(
        bgcolor="white",
        font_size=12,
        font_family="Arial"
    )
)

# Add gridlines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128, 128, 128, 0.2)')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(128, 128, 128, 0.2)')

# Get cluster statistics
cluster_counts = Counter(clusters)
print("\nCluster Distribution:")
for cluster, count in sorted(cluster_counts.items()):
    print(f"Cluster {cluster}: {count} responses")

# Define the get_top_terms function
def get_top_terms(cleaned_texts, n=10):
    """
    Extract the top n most common terms from the cleaned text data.
    """
    all_words = ' '.join(cleaned_texts).split()
    common_terms = Counter(all_words).most_common(n)
    return [term for term, _ in common_terms]

# Get top terms from the cleaned texts
top_terms = get_top_terms(df_burn_final_cleaned)
print("\nMost Common Terms:", ', '.join(top_terms))

# Calculate total points
total_points = len(clusters)
print(f"\nTotal Responses: {total_points}")

# Save to HTML for interactive viewing
fig.write_html("cluster_visualization.html")

# Show plot
fig.show()
```


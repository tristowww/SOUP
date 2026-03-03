```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define the ratings
ratings = {
    'Dimension': ['Communication', 'Problem-Solving', 'Teamwork', 'Customer Satisfaction', 'Initiative'],
    'Manager': [4, 5, 3, 5, 4],
    'Peer': [3, 4, 5, None, 3],
    'Customer': [5, 4, None, 5, None],
    'Self': [4, 3, 4, 4, 5]
}

# Create a DataFrame
df = pd.DataFrame(ratings)
print("Original Ratings Data:")
print(df)
```

```python
# Calculate averages
df['Average'] = df[['Manager', 'Peer', 'Customer', 'Self']].mean(axis=1)

# Output the numeric average results
print("\nAveraged Ratings:")
print(df[['Dimension', 'Average']])

# Visualize the averages
plt.bar(df['Dimension'], df['Average'], color='skyblue')
plt.title('Average Performance Ratings')
plt.xlabel('Dimension')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.show()
```

```python
# Calculate sums
df['Sum'] = df[['Manager', 'Peer', 'Customer', 'Self']].sum(axis=1)

# Output the numeric sum results
print("\nSummed Ratings:")
print(df[['Dimension', 'Sum']])

# Visualize the sums
plt.bar(df['Dimension'], df['Sum'], color='lightgreen')
plt.title('Summed Performance Ratings')
plt.xlabel('Dimension')
plt.ylabel('Sum of Ratings')
plt.xticks(rotation=45)
plt.show()
```

```python
# Normalize the ratings (convert to percentages)
df_normalized = df[['Manager', 'Peer', 'Customer', 'Self']].apply(lambda x: (x / 5) * 100)

# Calculate the average normalized score
df['Normalized'] = df_normalized.mean(axis=1)

# Output the numeric normalized results
print("\nNormalized Ratings (in Percentage):")
print(df[['Dimension', 'Normalized']])

# Visualize the normalized scores
plt.bar(df['Dimension'], df['Normalized'], color='salmon')
plt.title('Normalized Performance Ratings (Percentage)')
plt.xlabel('Dimension')
plt.ylabel('Normalized Rating (%)')
plt.xticks(rotation=45)
plt.show()
```

```python
# Define weights for each dimension (must add up to 1)
weights = {
    'Communication': 0.15,
    'Problem-Solving': 0.25,
    'Teamwork': 0.10,
    'Customer Satisfaction': 0.35,
    'Initiative': 0.15
}

# Multiply the normalized ratings by the corresponding weight
df['Weighted'] = df.apply(lambda row: row['Normalized'] * weights[row['Dimension']], axis=1)

# Output the weighted ratings
print("\nWeighted Ratings (Based on Assigned Weights):")
print(df[['Dimension', 'Weighted']])

# Visualize the weighted ratings
plt.bar(df['Dimension'], df['Weighted'], color='purple')
plt.title('Weighted Performance Ratings')
plt.xlabel('Dimension')
plt.ylabel('Weighted Rating')
plt.xticks(rotation=45)
plt.show()
```


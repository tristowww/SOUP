```python
# Importing installed packages
!pip install scikit-learn pandas matplotlib seaborn pingouin
import pandas as pd             # Import pandas for data manipulation
import seaborn as sns           # Import seaborn for advanced statistical plotting
import matplotlib.pyplot as plt  # Import matplotlib for general plotting
from sklearn.metrics import cohen_kappa_score # Import cohen_kappa_score for inter-rater reliability
import pingouin as pg           # Import pingouin for advanced statistical tests
```

```python
# Data setup: Fill in the ratings for Rater2 and Rater3

data = {
    'Employee': ['A', 'B', 'C', 'D', 'E'],
    'Rater1': [5, 3, 2, 4, 5],
    'Rater2': [__, __, __, __, __],  # <- Fill in based on the table in Part 1
    'Rater3': [__, __, __, __, __]   # <- Fill in based on the table in Part 1
}

# Convert to DataFrame
df = pd.DataFrame(data)
df
```

```python
# Cohen's Kappa for Rater1 and Rater2

kappa = cohen_kappa_score(df['____'], df['____'])  # <- Fill in the correct columns for Rater1 and Rater2
print(f"Cohen’s Kappa (Rater1 vs Rater2): {kappa}")
```

```python
# Bar plot to compare ratings by different raters

df.plot(kind='bar', x='____', y=['____', '____', '____'], figsize=(8,6))  # <- Fill in the correct column names
plt.title('Comparison of Employee Ratings by Raters')
plt.ylabel('Rating (1-5)')
plt.show()
```

```python
# Prepare data for ICC calculation

df_melted = pd.melt(df, id_vars=['____'], value_vars=['____', '____', '____'],  # <- Fill in the correct column names
                    var_name='Rater', value_name='Rating')

# ICC calculation
icc = pg.intraclass_corr(data=df_melted, targets='Employee', raters='Rater', ratings='Rating')
print(icc)
```

```python
# Heatmap to visualize rater consistency

sns.heatmap(df[['____', '____', '____']], annot=True, cmap="coolwarm", cbar=True,  # <- Fill in the correct column names for Rater1, Rater2, and Rater3
            xticklabels=['Rater1', 'Rater2', 'Rater3'], yticklabels=df['Employee'])
plt.title('Heatmap of Ratings by Raters')
plt.xlabel('Raters')
plt.ylabel('Employees')
plt.show()
```

```python
# Calculate Cronbach's Alpha for the ratings given by Rater1, Rater2, and Rater3

df_ratings = df[['____', '____', '____']]  # <- Fill in the column names for Rater1, Rater2, and Rater3
cronbach_alpha = pg.cronbach_alpha(data=df_ratings)
print(f"Cronbach's Alpha: {cronbach_alpha[0]}")  # cronbach_alpha returns a tuple with (alpha, CI)
```

```python
# Box plot to visualize rater score distributions

df_ratings = pd.melt(df, id_vars=['Employee'], value_vars=['____', '____', '____'], var_name='Rater', value_name='Rating')  # <- Fill in the column names for Rater1, Rater2, and Rater3

sns.boxplot(x='Rater', y='Rating', data=df_ratings)
plt.title('Box Plot of Ratings by Each Rater')
plt.ylabel('Rating (1-5)')
plt.xlabel('Raters')
plt.show()
```

```python
# Modify Rater3's ratings to all 5's

df['Rater3'] = [5, 5, 5, 5, 5]

# Re-run Cohen's Kappa for Rater1 and Rater3
kappa_13 = cohen_kappa_score(df['Rater1'], df['Rater3'])
print(f"Cohen’s Kappa (Rater1 vs Rater3): {kappa_13}")

# Re-run Cronbach's Alpha
cronbach_alpha = pg.cronbach_alpha(data=df[['Rater1', 'Rater2', 'Rater3']])
print(f"Cronbach's Alpha after modification: {cronbach_alpha[0]}")
```

```python
# Modify Rater3's ratings to introduce variability

df['Rater3'] = [4, 5, 2, 5, 5]

# Re-run Cohen's Kappa and Cronbach's Alpha
kappa_13 = cohen_kappa_score(df['Rater1'], df['Rater3'])
print(f"Cohen’s Kappa (Rater1 vs Rater3): {kappa_13}")

cronbach_alpha = pg.cronbach_alpha(data=df[['Rater1', 'Rater2', 'Rater3']])
print(f"Cronbach's Alpha after introducing variability: {cronbach_alpha[0]}")
```


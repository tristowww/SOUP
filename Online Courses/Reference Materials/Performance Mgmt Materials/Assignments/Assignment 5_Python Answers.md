```python
!pip install scikit-learn pandas matplotlib seaborn pingouin
```

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import cohen_kappa_score
import pingouin as pg
```

```python
# Correctly filled data setup
data = {
    'Employee': ['A', 'B', 'C', 'D', 'E'],
    'Rater1': [5, 3, 2, 4, 5],
    'Rater2': [5, 3, 2, 4, 5],
    'Rater3': [4, 4, 1, 5, 5]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df
```

```python
# Cohen's Kappa for Rater1 and Rater2
kappa = cohen_kappa_score(df['Rater1'], df['Rater2'])  # <- Fill in the columns here (Hint: Use 'Rater1' and 'Rater2')
print(f"Cohen’s Kappa: {kappa}")

#Indicates perfect agreement between Rater 1 and Rater 2
```

```python
# Bar plot to compare ratings by different raters
df.plot(kind='bar', x='Employee', y=['Rater1', 'Rater2', 'Rater3'], figsize=(8,6))
plt.title('Comparison of Employee Ratings by Raters')
plt.ylabel('Rating (1-5)')
plt.show()
```

```python
# Prepare data for ICC calculation
df_melted = pd.melt(df, id_vars=['Employee'], value_vars=['Rater1', 'Rater2', 'Rater3'],
                    var_name='Rater', value_name='Rating')

# ICC calculation
icc = pg.intraclass_corr(data=df_melted, targets='Employee', raters='Rater', ratings='Rating')
print(icc)

# This suggests good reliability across raters
```

```python
# Heatmap to visualize rater consistency
sns.heatmap(df[['Rater1', 'Rater2', 'Rater3']], annot=True, cmap="coolwarm", cbar=True,
            xticklabels=['Rater1', 'Rater2', 'Rater3'], yticklabels=df['Employee'])
plt.title('Heatmap of Ratings by Raters')
plt.xlabel('Raters')
plt.ylabel('Employees')
plt.show()
```

```python
# Calculate Cronbach's Alpha for the ratings given by Rater1, Rater2, and Rater3
df_ratings = df[['Rater1', 'Rater2', 'Rater3']]
cronbach_alpha = pg.cronbach_alpha(data=df_ratings)
print(f"Cronbach's Alpha: {cronbach_alpha[0]}")

#This high value suggests excellent internal consistency, indicating that the raters’ scores are closely aligned when measuring the same construct.
```

```python
# Box plot to visualize rater score distributions
df_ratings = pd.melt(df, id_vars=['Employee'], value_vars=['Rater1', 'Rater2', 'Rater3'], var_name='Rater', value_name='Rating')

sns.boxplot(x='Rater', y='Rating', data=df_ratings)
plt.title('Box Plot of Ratings by Each Rater')
plt.ylabel('Rating (1-5)')
plt.xlabel('Raters')
plt.show()

#A box plot for each rater showing the distribution of their ratings. If each rater has a similar distribution, it suggests higher internal consistency.
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

Explanation:

Cohen’s Kappa drops to 0.0, indicating no agreement beyond chance due to
identical ratings from Rater 3.


Cronbach’s Alpha decreases to 0.75, showing a reduction in internal consistency as Rater 3’s ratings lack variability.

```python
# Modify Rater3's ratings to introduce variability
df['Rater3'] = [4, 5, 2, 5, 5]

# Re-run Cohen's Kappa and Cronbach's Alpha
kappa_13 = cohen_kappa_score(df['Rater1'], df['Rater3'])
print(f"Cohen’s Kappa (Rater1 vs Rater3): {kappa_13}")

cronbach_alpha = pg.cronbach_alpha(data=df[['Rater1', 'Rater2', 'Rater3']])
print(f"Cronbach's Alpha after introducing variability: {cronbach_alpha[0]}")
```

Explanation:

Cohen’s Kappa improves slightly to approximately 0.118, showing minimal agreement beyond chance once variability is reintroduced.

Cronbach’s Alpha increases to about 0.898, indicating good internal consistency as the ratings now have some variation.


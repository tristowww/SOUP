# **Assignment 6: Data Analysis & Hypothesis Testing on Burnout Among College Students**

###Objective:

Apply regression and correlation analyses to explore the relationships between self-efficacy, social media usage, student employment, and burnout. Use statistical software (e.g., SPSS) to test hypotheses and interpret results. Utilize your chosen scales for the analysis.

## Set up the Google Colab environment
###Load the packages in the code cell below by pressing "ctrl + Enter" or clicking the play button on the left of the cell.


```python
#Import Libraries with Descriptions

# For numerical computations and array operations
import numpy as np    # Handles mathematical operations on arrays, matrices

# For data manipulation and analysis
import pandas as pd   # Creates and manipulates data frames, reads/writes data files

# For data visualization
import matplotlib.pyplot as plt  # Base plotting library, creates static visualizations
import seaborn as sns           # Built on matplotlib, creates statistical visualizations

# For statistical modeling
from sklearn.linear_model import LinearRegression  # For regression analysis
import statsmodels.api as sm                      # For detailed statistical analysis, includes p-values
from scipy import stats                           # For statistical tests (e.g., t-tests, ANOVA)

# For data preprocessing
from sklearn.preprocessing import StandardScaler   # Standardizes variables (converts to z-scores)

# For specific statistical tests
from scipy.stats import pearsonr  # Specifically for Pearson correlations with p-values

# Google Colab Specific
from google.colab import drive
```

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
# Display all column names to verify their correctness
print("Column names in the dataset:")
print(data.columns.tolist())
```

```python
# Remove the first two rows from the dataset
data = data.iloc[2:].reset_index(drop=True)
```

## 1. Preparing the Data


### Create a new dataframe with just the variables of interest

```python
# Data Cleaning Steps

# Create a DataFrame with only the variables of interest, using appropriate labels from the CSV file
variables_of_interest = [
    # GSE items (Self-Efficacy Scale)
    *[f'GSE_{i}' for i in range(1, 11)],
    # SMUS items (Social Media Usage Scale)
    *[f'SMUS_{i}' for i in range(1, 18)],
    # Hours worked
    'Hours_1',
    # MBI items (Burnout Scale)
    *[f'MBI_{i}' for i in range(1, 23)],
    # Classification variable
    'Classification'
]
```

```python
# Check columns
existing_columns = [col for col in variables_of_interest if col in data.columns]
missing_columns = [col for col in variables_of_interest if col not in data.columns]
print(f"Existing columns: {existing_columns}")
print(f"Missing columns: {missing_columns}")
```

```python
# Create initial cleaned dataset
data_cleaned = data[existing_columns].copy()
data_cleaned
```

```python
# Convert Hours and rename
if 'Hours_1' in data_cleaned.columns:
    data_cleaned['Hours'] = pd.to_numeric(data_cleaned['Hours_1'], errors='coerce')
    hours_missing_count = data_cleaned['Hours'].isna().sum()
    print(f"Number of missing values in 'Hours' after conversion: {hours_missing_count}")
```

```python
# Convert string responses to numeric for scale items
def convert_response_to_numeric(series):
    return series.astype(str).str.strip().apply(lambda x: [int(d) for d in str(x)]).apply(pd.Series).mean(axis=1)
```

```python
# Convert GSE, SMUS, and MBI items
for col in existing_columns:
    if col.startswith(('GSE_', 'SMUS_', 'MBI_')):
        try:
            data_cleaned[col] = convert_response_to_numeric(data_cleaned[col])
        except:
            data_cleaned[col] = pd.to_numeric(data_cleaned[col], errors='coerce')

```

###2. Handling Missing Data


```python
# Check and handle missing data
print("\nInitial missing data count:")
print(data_cleaned.isnull().sum())
print(f"Initial number of rows: {data_cleaned.shape[0]}")
```

```python
# Remove rows with any missing values
initial_rows = data_cleaned.shape[0]
data_cleaned = data_cleaned.dropna().reset_index(drop=True)
final_rows = data_cleaned.shape[0]
cases_removed = initial_rows - final_rows
```

```python
print(f"\nCases removed due to missing data: {cases_removed}")
print(f"Final number of rows: {final_rows}")
```

####How many cases were removed due to missing data? 60

```python
# Verify no missing data remains
print("\nFinal missing data count:")
print(data_cleaned.isnull().sum())
```

###3. Reverse Score Items

```python
# Reverse score MBI items
reverse_mbi_items = ['MBI_15', 'MBI_16', 'MBI_17', 'MBI_18', 'MBI_19', 'MBI_20', 'MBI_21', 'MBI_22']
for item in reverse_mbi_items:
    if item in data_cleaned.columns:
        data_cleaned[item] = 8 - data_cleaned[item]  # On a 1-7 Likert scale
```

####Which items were reverse scored? 'MBI_15', 'MBI_16', 'MBI_17', 'MBI_18', 'MBI_19', 'MBI_20', 'MBI_21', 'MBI_22'

###4. Group Scale Items into Single Variable

```python
# Define scale items
gse_items = [f'GSE_{i}' for i in range(1, 11) if f'GSE_{i}' in data_cleaned.columns]
smus_items = [f'SMUS_{i}' for i in range(1, 18) if f'SMUS_{i}' in data_cleaned.columns]
mbi_items = [f'MBI_{i}' for i in range(1, 23) if f'MBI_{i}' in data_cleaned.columns]
```

```python
# Print the first few rows to verify data cleaning
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
print(data_cleaned)
```

###5. Descriptive Statistics


```python
# Function to safely convert string responses to numeric
def safe_convert_to_numeric(x):
    try:
        # First try simple numeric conversion
        return pd.to_numeric(x)
    except:
        # If that fails, try to clean the string and extract the first digit
        try:
            return int(str(x).strip()[0])
        except:
            return np.nan

# Convert items to numeric more safely
for col in gse_items + smus_items + mbi_items:
    data_cleaned[col] = data_cleaned[col].apply(safe_convert_to_numeric)

# Calculate scale scores
print("\nScale Statistics:")

# GSE scale scores
gse_scale_scores = data_cleaned[gse_items].mean(axis=1)
gse_mean = gse_scale_scores.mean()
gse_std = gse_scale_scores.std(ddof=1)
print(f"GSE Scale: Mean = {gse_mean:.3f}, Standard Deviation = {gse_std:.3f}")
print(f"GSE N = {gse_scale_scores.count()}")

# SMUS scale scores
smus_scale_scores = data_cleaned[smus_items].mean(axis=1)
smus_mean = smus_scale_scores.mean()
smus_std = smus_scale_scores.std(ddof=1)
print(f"\nSMUS Scale: Mean = {smus_mean:.3f}, Standard Deviation = {smus_std:.3f}")
print(f"SMUS N = {smus_scale_scores.count()}")

# MBI scale scores
mbi_scale_scores = data_cleaned[mbi_items].mean(axis=1)
mbi_mean = mbi_scale_scores.mean()
mbi_std = mbi_scale_scores.std(ddof=1)
print(f"\nMBI Scale: Mean = {mbi_mean:.3f}, Standard Deviation = {mbi_std:.3f}")
print(f"MBI N = {mbi_scale_scores.count()}")

# Hours variable
hours_mean = data_cleaned['Hours'].mean()
hours_std = data_cleaned['Hours'].std(ddof=1)
print(f"\nHours Worked: Mean = {hours_mean:.3f}, Standard Deviation = {hours_std:.3f}")
print(f"Hours N = {data_cleaned['Hours'].count()}")

# Store scale scores in the dataframe
data_cleaned['GSE_Score'] = gse_scale_scores
data_cleaned['SMUS_Score'] = smus_scale_scores
data_cleaned['MBI_Score'] = mbi_scale_scores

# Print summary of scale scores
print("\nScale Score Summary:")
print(data_cleaned[['GSE_Score', 'SMUS_Score', 'MBI_Score', 'Hours']].describe())

# Check for any remaining missing values
print("\nMissing values in scale scores:")
print(data_cleaned[['GSE_Score', 'SMUS_Score', 'MBI_Score', 'Hours']].isnull().sum())
```

###5. Test Scale Reliability via Cronbach's Alpha

```python
# Calculate Cronbach's alpha BEFORE scale scoring
def cronbach_alpha(items_df):
    # Convert to numeric and handle missing values
    df = items_df.apply(pd.to_numeric, errors='coerce')

    # Remove rows with any missing values for reliability analysis
    df = df.dropna()

    # Calculate number of items
    n_items = df.shape[1]

    # Calculate variance of the sum
    total_var = df.sum(axis=1).var(ddof=1)

    # Calculate sum of item variances
    item_vars = df.var(ddof=1).sum()

    # Calculate alpha
    alpha = (n_items / (n_items - 1)) * (1 - item_vars / total_var)

    return alpha

# Calculate reliability for each scale
print("\nReliability Analysis:")
print(f"GSE Scale (Self-Efficacy): α = {cronbach_alpha(data_cleaned[gse_items]):.3f}")
print(f"SMUS Scale (Social Media Usage): α = {cronbach_alpha(data_cleaned[smus_items]):.3f}")
print(f"MBI Scale (Burnout): α = {cronbach_alpha(data_cleaned[mbi_items]):.3f}")

```

####Which scales have acceptable reliability?
Self-Efficacy (GSE)

Social Media Usage (SMUS)

Burnout (MBI)



###6. Test of Normality

```python
def run_normality_test(data, name):
    # Remove missing values
    clean_data = data.dropna()
    n = len(clean_data)

    # Calculate statistics
    stat, p_value = stats.shapiro(clean_data)
    skewness = clean_data.skew()
    # Convert pandas kurtosis to SPSS kurtosis (excess kurtosis)
    kurtosis = clean_data.kurtosis() - 3

    # Calculate standard errors (SPSS formulas)
    se_skewness = np.sqrt(6 * n * (n - 1) / ((n - 2) * (n + 1) * (n + 3)))
    se_kurtosis = np.sqrt(24 * n * (n - 1) * (n - 1) / ((n - 3) * (n - 2) * (n + 3) * (n + 5)))

    print(f"\n{name}:")
    print(f"N = {n}")
    print(f"Shapiro-Wilk Statistic = {stat:.3f}")
    print(f"p-value = {p_value:.3f}")
    print(f"Skewness = {skewness:.3f}")
    print(f"SE of Skewness = {se_skewness:.3f}")
    print(f"Kurtosis = {kurtosis:.3f}")  # This is now excess kurtosis like SPSS
    print(f"SE of Kurtosis = {se_kurtosis:.3f}")

# Run normality tests on each variable
run_normality_test(gse_scale_scores, "GSE Scale")
run_normality_test(smus_scale_scores, "SMUS Scale")
run_normality_test(mbi_scale_scores, "MBI Scale")
run_normality_test(data_cleaned['Hours'], "Hours")
```

```python
# Create figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Histograms of Scale Scores and Hours')

# GSE Histogram
axs[0, 0].hist(gse_scale_scores.dropna(), bins=15, edgecolor='black')
axs[0, 0].set_title('GSE Scale Scores')
axs[0, 0].set_xlabel('Score')
axs[0, 0].set_ylabel('Frequency')

# SMUS Histogram
axs[0, 1].hist(smus_scale_scores.dropna(), bins=15, edgecolor='black')
axs[0, 1].set_title('SMUS Scale Scores')
axs[0, 1].set_xlabel('Score')
axs[0, 1].set_ylabel('Frequency')

# MBI Histogram
axs[1, 0].hist(mbi_scale_scores.dropna(), bins=15, edgecolor='black')
axs[1, 0].set_title('MBI Scale Scores')
axs[1, 0].set_xlabel('Score')
axs[1, 0].set_ylabel('Frequency')

# Hours Histogram
axs[1, 1].hist(data_cleaned['Hours'].dropna(), bins=15, edgecolor='black')
axs[1, 1].set_title('Hours')
axs[1, 1].set_xlabel('Hours')
axs[1, 1].set_ylabel('Frequency')

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()
```

####Which scales are normally distributed?

**GGSE (General Self-Efficacy Scale):**
Shapiro-Wilk: Statistic = 0.973, p = 0.251
Skewness = -0.454 (SE = 0.325)
Kurtosis = -1.888 (SE = 0.639)
Conclusion: The data is normally distributed (p > 0.05), with a slight negative skew and platykurtic distribution (flatter than normal).

**SMUS (Social Media Usage Scale):**

Shapiro-Wilk: Statistic = 0.905, p < 0.001
Skewness = 0.857 (SE = 0.325)
Kurtosis = -2.999 (SE = 0.639)
Conclusion: The data is not normally distributed (p < 0.05), showing positive skewness and a highly platykurtic distribution.

**MBI (Burnout Scale):**

Shapiro-Wilk: Statistic = 0.979, p = 0.458
Skewness = 0.273 (SE = 0.325)
Kurtosis = -2.890 (SE = 0.639)
Conclusion: The data is normally distributed (p > 0.05), with slight positive skewness and a platykurtic distribution.

**Hours:**

Shapiro-Wilk: Statistic = 0.960, p = 0.070
Skewness = 0.522 (SE = 0.325)
Kurtosis = -3.196 (SE = 0.639)
Conclusion: The data is normally distributed (p > 0.05), with moderate positive skewness and a highly platykurtic distribution.

**Summary: **Three scales (GSE, MBI, and Hours) show normal distributions based on Shapiro-Wilk tests, while SMUS significantly deviates from normality. All variables show notable platykurtic tendencies, indicating flatter distributions than normal.

####Which test did you use and why?
The Shapiro-Wilk test is suitable for testing the normality of small to moderate sample sizes and provides reliable results for the dataset's size.

### 7. Correlation Analysis


```python
from scipy.stats import pearsonr
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create a DataFrame with all the variables for correlation analysis
correlation_data = pd.DataFrame({
    'GSE': gse_scale_scores,
    'SMUS': smus_scale_scores,
    'MBI': mbi_scale_scores,
    'Hours': data_cleaned['Hours']
})

# Calculate correlations and p-values
correlation_matrix = np.zeros((4, 4))
p_values = np.zeros((4, 4))
variables = ['GSE', 'SMUS', 'MBI', 'Hours']

for i in range(len(variables)):
    for j in range(len(variables)):
        if i == j:
            correlation_matrix[i, j] = 1.0
            p_values[i, j] = 0.0
        else:
            valid_data = correlation_data[[variables[i], variables[j]]].dropna()
            if len(valid_data) > 1:
                r, p = pearsonr(valid_data[variables[i]], valid_data[variables[j]])
                correlation_matrix[i, j] = r
                p_values[i, j] = p
            else:
                correlation_matrix[i, j] = np.nan
                p_values[i, j] = np.nan

# Convert to DataFrames
correlation_matrix_df = pd.DataFrame(correlation_matrix,
                                   index=variables,
                                   columns=variables)
p_values_df = pd.DataFrame(p_values,
                          index=variables,
                          columns=variables)

# Print results
print("Correlation Matrix:")
print(correlation_matrix_df.round(3))
print("\nP-Values Matrix:")
print(p_values_df.round(3))

# Create heatmap
plt.figure(figsize=(10, 8))
mask = np.triu(np.ones_like(correlation_matrix), k=1)  # Create mask for upper triangle
sns.heatmap(correlation_matrix_df,
            annot=True,
            cmap='coolwarm',
            linewidths=0.5,
            fmt='.3f',
            square=True,
            mask=mask,
            vmin=-1,
            vmax=1,
            center=0)
plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.show()

# Print detailed correlation results
print("\nDetailed Correlation Results:")
for i in range(len(variables)):
    for j in range(i):
        var1, var2 = variables[i], variables[j]
        valid_data = correlation_data[[var1, var2]].dropna()
        if len(valid_data) > 1:
            r, p = pearsonr(valid_data[var1], valid_data[var2])
            n = len(valid_data)
            print(f"\n{var1} - {var2}:")
            print(f"r = {r:.3f}")
            print(f"p = {p:.3f}")
            print(f"n = {n}")
```

####Write a short interpertation of the correlations for each hypothesis.
- **Self-Efficacy**: There is a moderate negative correlation between self-efficacy and social media usage (r = -0.311, p = 0.022), suggesting that higher self-efficacy is associated with lower social media usage, and this relationship is statistically significant. There is a strong negative correlation between self-efficacy and burnout (r = -0.619, p < 0.001), indicating that higher self-efficacy is strongly linked to lower burnout, and this relationship is statistically significant. The correlation between self-efficacy and hours worked is very weak and positive (r = 0.094, p = 0.498), suggesting almost no relationship and it is not statistically significant.

- **Social Media Usage**: Social media usage has a moderate positive correlation with burnout (r = 0.334, p = 0.014), implying that higher social media usage is linked to higher burnout, and this relationship is statistically significant. The correlation between social media usage and hours worked is weak and negative (r = -0.169, p = 0.221), indicating that higher social media usage may be associated with fewer hours worked, but this relationship is not statistically significant.

- **Burnout and Student Employment**: The correlation between burnout and hours worked is weak and negative (r = -0.159, p = 0.252), suggesting a slight tendency for more hours worked to be associated with lower burnout, though this correlation is not statistically significant.

###8. Compute Standardized Scores

```python
# Get lists of item names
gse_items = [f'GSE_{i}' for i in range(1, 11) if f'GSE_{i}' in data_cleaned.columns]
smus_items = [f'SMUS_{i}' for i in range(1, 18) if f'SMUS_{i}' in data_cleaned.columns]
mbi_items = [f'MBI_{i}' for i in range(1, 23) if f'MBI_{i}' in data_cleaned.columns]

# Calculate raw scale scores (no standardization)
min_valid_items_mbi = 16
min_valid_items_gse = 7
min_valid_items_smus = 12

# Calculate raw mean scores
data_cleaned['MBI'] = data_cleaned[mbi_items].apply(
    lambda row: row.mean() if row.count() >= min_valid_items_mbi else np.nan, axis=1)

data_cleaned['GSE'] = data_cleaned[gse_items].apply(
    lambda row: row.mean() if row.count() >= min_valid_items_gse else np.nan, axis=1)

data_cleaned['SMUS'] = data_cleaned[smus_items].apply(
    lambda row: row.mean() if row.count() >= min_valid_items_smus else np.nan, axis=1)

# Print descriptives of raw scores
scale_scores = ['MBI', 'GSE', 'SMUS']
for scale in scale_scores:
    print(f"\n{scale} Scale Scores:")
    print(f"Mean = {data_cleaned[scale].mean():.3f}")
    print(f"SD = {data_cleaned[scale].std():.3f}")
    print(data_cleaned[[scale]].head())
```

####What is the reason to compute scale scores for each scale?
Scale scores are computed to create a single measure that summarizes the response to multiple items, enhancing reliability and validity by reducing measurement error.

### 9.Hypothesis Testing (Simple Regression)

```python
import statsmodels.api as sm
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def run_spss_style_regression(data, x_var, y_var):
    """Run regression with SPSS-style output tables"""
    # Get complete cases only
    complete_data = data[[x_var, y_var]].dropna()
    X = complete_data[x_var]
    y = complete_data[y_var]
    n = len(X)

    # Calculate correlation and R-squared
    correlation = np.corrcoef(X, y)[0, 1]
    r_squared = correlation ** 2
    adj_r_squared = 1 - ((1 - r_squared) * (n - 1)/(n - 2))

    # Fit model
    X_with_const = sm.add_constant(X)
    model = sm.OLS(y, X_with_const).fit()

    # Calculate standard error of the estimate
    std_error_est = np.sqrt(model.mse_resid)

    # Print SPSS-style output
    print("\nModel Summary")
    print("─" * 80)
    print("                                                   Change Statistics")
    print(f"Model    R       R Square  Adjusted R  Std Error of  R Square   F Change  df1  df2  Sig F Change")
    print(f"                           Square      Estimate      Change")
    print(f"1        {abs(correlation):.3f}    {r_squared:.3f}     {adj_r_squared:.3f}      {std_error_est:.5f}     {r_squared:.3f}    {model.fvalue:.3f}    1   {n-2}     {model.f_pvalue:.3f}")

    print("\nCoefficients")
    print("─" * 120)
    print("                           Standardized")
    print("        Unstandardized Coefficients    Coefficients            95% Confidence Interval for B")
    print("Model                B        Std Error   Beta         t     Sig.    Lower Bound  Upper Bound")

    # Calculate confidence intervals
    conf_int = model.conf_int()

    # Print coefficients
    print(f"1  (Constant)  {model.params['const']:>8.3f}    {model.bse['const']:.3f}                  {model.tvalues['const']:.3f}  {model.pvalues['const']:.3f}    {conf_int[0]['const']:.3f}       {conf_int[1]['const']:.3f}")
    print(f"   {x_var:<8}   {model.params[x_var]:>8.3f}    {model.bse[x_var]:.3f}     {correlation:.3f}      {model.tvalues[x_var]:.3f}  {model.pvalues[x_var]:.3f}    {conf_int[0][x_var]:.3f}       {conf_int[1][x_var]:.3f}")

    return model, correlation

# Run regressions with SPSS-style output
print("\n=== GSE → Burnout ===")
model_gse, corr_gse = run_spss_style_regression(data_cleaned, 'GSE', 'MBI')

print("\n=== SMUS → Burnout ===")
model_smus, corr_smus = run_spss_style_regression(data_cleaned, 'SMUS', 'MBI')

print("\n=== Hours → Burnout ===")
model_hours, corr_hours = run_spss_style_regression(data_cleaned, 'Hours', 'MBI')

# Create regression plots
plt.figure(figsize=(18, 5))

plt.subplot(1, 3, 1)
sns.regplot(x='GSE', y='MBI', data=data_cleaned)
plt.title(f'GSE vs Burnout\nβ = {corr_gse:.3f}, R² = {corr_gse**2:.3f}')

plt.subplot(1, 3, 2)
sns.regplot(x='SMUS', y='MBI', data=data_cleaned)
plt.title(f'SMUS vs Burnout\nβ = {corr_smus:.3f}, R² = {corr_smus**2:.3f}')

plt.subplot(1, 3, 3)
sns.regplot(x='Hours', y='MBI', data=data_cleaned)
plt.title(f'Hours vs Burnout\nβ = {corr_hours:.3f}, R² = {corr_hours**2:.3f}')

plt.tight_layout()
plt.show()

# Create diagnostic plots
def create_diagnostic_plots(model, X, y, title):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle(f'Diagnostic Plots - {title}')

    # Residuals vs Fitted
    fitted_vals = model.fittedvalues
    residuals = model.resid
    sns.scatterplot(x=fitted_vals, y=residuals, ax=axes[0,0])
    axes[0,0].axhline(y=0, color='r', linestyle='--')
    axes[0,0].set_title('Residuals vs Fitted')
    axes[0,0].set_xlabel('Fitted values')
    axes[0,0].set_ylabel('Residuals')

    # Q-Q plot
    stats.probplot(residuals, dist="norm", plot=axes[0,1])
    axes[0,1].set_title('Normal Q-Q Plot')

    # Scale-Location
    std_residuals = np.sqrt(np.abs(stats.zscore(residuals)))
    sns.scatterplot(x=fitted_vals, y=std_residuals, ax=axes[1,0])
    axes[1,0].set_title('Scale-Location')
    axes[1,0].set_xlabel('Fitted values')
    axes[1,0].set_ylabel('√|Standardized residuals|')

    # Original scatter with regression line
    sns.regplot(x=X, y=y, ax=axes[1,1])
    axes[1,1].set_title('Regression Line')

    plt.tight_layout()
    plt.show()

# Create diagnostic plots for each regression
create_diagnostic_plots(model_gse, data_cleaned['GSE'], data_cleaned['MBI'], 'GSE → Burnout')
create_diagnostic_plots(model_smus, data_cleaned['SMUS'], data_cleaned['MBI'], 'SMUS → Burnout')
create_diagnostic_plots(model_hours, data_cleaned['Hours'], data_cleaned['MBI'], 'Hours → Burnout')
```

####Write a short interpertation of the simple regression results for each hypothesis.
- **Self-Efficacy → Burnout:** There is a strong negative relationship between self-efficacy and burnout (β = -0.619, p < 0.001). The model explains 38.4% of the variance in burnout scores (R² = 0.384). For each one-unit increase in self-efficacy, burnout decreases by 1.099 units (B = -1.099, 95% CI [-1.486, -0.711]).

- **Social Media Usage → Burnout:** There is a moderate positive relationship between social media usage and burnout (β = 0.334, p = 0.014). The model explains 11.1% of the variance in burnout scores (R² = 0.111). For each one-unit increase in social media usage, burnout increases by 0.181 units (B = 0.181, 95% CI [0.039, 0.323]).

- **Student Employment → Burnout:** There is a very weak negative relationship between hours worked and burnout (β = -0.159, p = 0.252), and this relationship is not statistically significant. The model explains only 2.5% of the variance in burnout scores (R² = 0.025). For each additional hour worked, burnout decreases by 0.018 units (B = -0.018, 95% CI [-0.050, 0.014]), but this effect is not statistically significant.

### 10. Multiple Regression Analysis

```python
def run_spss_style_regression(data, dv, ivs):
    # Prepare data and fit model
    reg_data = data[ivs + [dv]].dropna()
    y = reg_data[dv]
    X = sm.add_constant(reg_data[ivs])
    model = sm.OLS(y, X).fit()

    # Calculate key statistics
    n = len(y)
    r2 = model.rsquared

    # Model Summary
    print("\nModel Summary")
    print("─" * 80)
    print("Model    R       R Square  Adjusted R  Std Error")
    print(f"1        {np.sqrt(r2):.3f}    {r2:.3f}     {model.rsquared_adj:.3f}      {np.sqrt(model.mse_resid):.3f}")

    # ANOVA
    print("\nANOVA")
    print("─" * 80)
    print("Model             SS          df    MS           F        Sig.")
    f_p = "<.001" if model.f_pvalue < 0.001 else f"{model.f_pvalue:.3f}"
    print(f"1  Regression   {model.ess:>10.3f}    {len(ivs):>2d}    {model.ess/len(ivs):>10.3f}   {model.fvalue:>7.3f}    {f_p}")
    print(f"   Residual     {model.ssr:>10.3f}    {n-len(ivs)-1:>2d}    {model.ssr/(n-len(ivs)-1):>10.3f}")
    print(f"   Total        {model.ess+model.ssr:>10.3f}    {n-1:>2d}")

    # Coefficients
    print("\nCoefficients")
    print("─" * 80)
    print("                 B        SE         Beta        t        Sig.")

    # Constant row
    const_p = "<.001" if model.pvalues.iloc[0] < 0.001 else f"{model.pvalues.iloc[0]:.3f}"
    print(f"(Constant)  {model.params.iloc[0]:>8.3f}    {model.bse.iloc[0]:.3f}                {model.tvalues.iloc[0]:>8.3f}    {const_p}")

    # Predictor rows
    for i, var in enumerate(ivs, 1):
        beta = model.params[var] * (reg_data[var].std() / y.std())
        p_val = "<.001" if model.pvalues[var] < 0.001 else f"{model.pvalues[var]:.3f}"
        print(f"{var:<10}  {model.params[var]:>8.3f}    {model.bse[var]:.3f}    {beta:>8.3f}    {model.tvalues[var]:>8.3f}    {p_val}")

    return model

# Run the regression
if {'GSE', 'SMUS', 'MBI', 'Hours'}.issubset(data_cleaned.columns):
    model = run_spss_style_regression(data_cleaned, 'MBI', ['GSE', 'SMUS', 'Hours'])

# Create diagnostic plots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Multiple Regression Diagnostic Plots')

# Residuals vs Fitted
sns.scatterplot(x=model.fittedvalues, y=model.resid, ax=axes[0,0])
axes[0,0].axhline(y=0, color='r', linestyle='--')
axes[0,0].set_title('Residuals vs Fitted')

# Q-Q plot
stats.probplot(model.resid, dist="norm", plot=axes[0,1])
axes[0,1].set_title('Normal Q-Q Plot')

# Scale-Location plot
std_resid = np.sqrt(np.abs(stats.zscore(model.resid)))
sns.scatterplot(x=model.fittedvalues, y=std_resid, ax=axes[1,0])
axes[1,0].set_title('Scale-Location')

# Residuals histogram
sns.histplot(model.resid, kde=True, ax=axes[1,1])
axes[1,1].set_title('Residuals Distribution')

plt.tight_layout()
plt.show()
```

####Write a short interpertation of the multiple regression results.

The model significantly predicts burnout (F(3,50) = 11.683, p < .001) and explains 41.2% of the variance in burnout scores (R² = 0.412).

**Individual predictors:**

**Self-Efficacy:** Has a strong negative relationship with burnout (β = -0.567, p < .001). For each one-unit increase in self-efficacy, burnout decreases by 1.006 units (B = -1.006).

**Social Media Usage:** Shows a weak positive but non-significant relationship with burnout (β = 0.144, p = 0.219). For each one-unit increase in social media usage, burnout increases by 0.078 units (B = 0.078).

**Student Employment:** Shows a very weak negative but non-significant relationship with burnout (β = -0.081, p = 0.466). For each additional hour worked, burnout decreases by 0.009 units (B = -0.009).

These results indicate that self-efficacy is the strongest predictor of burnout among the variables studied.

### 11. Mean Difference Testing

```python
# Bootstrap Resampling

# Perform bootstrap resampling to generate more data for each academic classification
if 'Classification' in data_cleaned.columns:
    n_bootstrap = 1000
    bootstrap_samples = []
    for i in range(n_bootstrap):
        resampled_data = data_cleaned.sample(n=len(data_cleaned), replace=True)
        bootstrap_samples.append(resampled_data)
    bootstrap_data = pd.concat(bootstrap_samples)

    # ANOVA with Bootstrap Data
    anova_results_bootstrap = {}
    descriptive_stats_bootstrap = {}
    effect_sizes_bootstrap = {}
    cohens_d_results = {}

    for var in ['GSE', 'SMUS', 'MBI', 'Hours']:
        if var in bootstrap_data.columns:
            # Compute descriptive statistics for each academic group
            descriptive_stats = bootstrap_data.groupby('Classification')[var].agg(['mean', 'std']).reset_index()
            descriptive_stats_bootstrap[var] = descriptive_stats
            print(f"Descriptive Statistics for {var} by Classification:")
            print(descriptive_stats)

            groups = [bootstrap_data[bootstrap_data['Classification'] == i][var] for i in bootstrap_data['Classification'].unique() if len(bootstrap_data[bootstrap_data['Classification'] == i][var]) > 0]
            if len(groups) > 1 and all(len(group) > 2 for group in groups):
                try:
                    anova_results_bootstrap[var] = stats.f_oneway(*groups)
                    # Calculate Effect Size (η²)
                    grand_mean = bootstrap_data[var].mean()
                    ss_between = sum([(len(group) * ((group.mean() - grand_mean) ** 2)) for group in groups])
                    ss_total = sum([(x - grand_mean) ** 2 for x in bootstrap_data[var]])
                    eta_squared = ss_between / ss_total
                    effect_sizes_bootstrap[var] = eta_squared

                    # Calculate Cohen's d for pairwise group comparisons
                    unique_classifications = bootstrap_data['Classification'].unique()
                    cohens_d_results[var] = {}
                    for i in range(len(unique_classifications)):
                        for j in range(i + 1, len(unique_classifications)):
                            group1 = bootstrap_data[bootstrap_data['Classification'] == unique_classifications[i]][var]
                            group2 = bootstrap_data[bootstrap_data['Classification'] == unique_classifications[j]][var]
                            if len(group1) > 2 and len(group2) > 2:
                                pooled_std = np.sqrt((np.var(group1, ddof=1) + np.var(group2, ddof=1)) / 2)
                                cohens_d = (group1.mean() - group2.mean()) / pooled_std
                                pair_label = f"{unique_classifications[i]} vs {unique_classifications[j]}"
                                cohens_d_results[var][pair_label] = cohens_d
                except ValueError:
                    anova_results_bootstrap[var] = 'Insufficient data for ANOVA'
                    effect_sizes_bootstrap[var] = 'Cannot calculate effect size'
                    cohens_d_results[var] = 'Cannot calculate Cohen\'s d'
            else:
                anova_results_bootstrap[var] = 'Insufficient data for ANOVA'
                effect_sizes_bootstrap[var] = 'Cannot calculate effect size'
                cohens_d_results[var] = 'Cannot calculate Cohen\'s d'

    print(f"ANOVA Results with Bootstrap Data: {anova_results_bootstrap}")
    print("Effect Sizes (η²) for Bootstrap Data:")
    for variable, effect_size in effect_sizes_bootstrap.items():
        print(f"{variable}: η² = {effect_size}")

    print("Cohen's d for Bootstrap Data (pairwise comparisons):")
    for variable, pairs in cohens_d_results.items():
        if isinstance(pairs, dict):
            for pair, d_value in pairs.items():
                print(f"{variable} ({pair}): Cohen's d = {d_value}")
        else:
            print(f"{variable}: {pairs}")

# Boxplot for Burnout (MBI) by Academic Classification
# -------------------------------
plt.figure(figsize=(10, 6))
sns.boxplot(x='Classification', y='MBI', data=bootstrap_data)
plt.title('Burnout (MBI) Scores by Academic Classification')
plt.xlabel('Academic Classification')
plt.ylabel('Burnout (MBI)')
plt.xticks(ticks=[0, 1, 2, 3, 4], labels=['Freshman', 'Sophomore', 'Junior', 'Senior', 'Graduate'])
plt.show()

```

####Write a short interpertation of the mean difference testing results.

Based on the ANOVA and effect size analyses across classification groups:

**Self-Efficacy (GSE):** There are significant differences between groups (F = 388.94, p < .001), with a small effect size (η² = 0.021). Seniors (M = 3.03) reported the highest self-efficacy, while sophomores (M = 2.76) reported the lowest. The largest difference was between sophomores and seniors (d = -0.49), indicating a moderate effect.

**Social Media Usage (SMUS):** Significant differences exist between groups (F = 1958.67, p < .001) with the largest effect size of all variables (η² = 0.098). Freshmen reported the highest usage (M = 4.52) and sophomores the lowest (M = 3.09). Large differences were found between sophomores and juniors (d = -1.05) and between freshmen and sophomores (d = 0.83).

**Burnout (MBI):** Significant differences exist between groups (F = 1057.29, p < .001) with a moderate effect size (η² = 0.055). Juniors reported the lowest burnout (M = 3.26) compared to freshmen (M = 3.95), with large differences between juniors and all other groups (d ranging from 0.77 to 0.78).

**Student Employment (Hours):** Significant differences exist between groups (F = 734.68, p < .001) with a small effect size (η² = 0.039). Sophomores worked the most hours (M = 21.60) and freshmen the least (M = 17.56). Moderate differences were found between sophomores and freshmen (d = -0.52) and between sophomores and juniors (d = 0.50).

All group differences were statistically significant (p < .001), with social media usage showing the largest overall effect size, followed by burnout, hours worked, and self-efficacy.


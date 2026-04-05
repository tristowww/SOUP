co

{x}

<>

& Assignment 4 Python Answers.ipynb +

File

+ Code

[ ]

(4)

[ ]

(4)

[ ]

(4)

oO

(4)

[ ]

(4)

Edit View Insert Runtime Tools Help Last edited on October 17

+ Text

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define the ratings
ratings = {

‘Dimension’: ['Communication', ‘Problem-Solving’, 'Teamwork', ‘Customer Satisfaction’, ‘Initiative'],

"Manager': [4, 5, 3, 5, 4],
"Peer': [3, 4, 5, None, 3],
"Customer': [5, 4, None, 5, None],
'Self': [4, 3, 4, 4, 5]

# Create a DataFrame

df = pd.DataFrame(ratings )
print("Original Ratings Data:")
print (df)

Original Ratings Data:
Dimension Manager Peer Customer Self

(2) Communication 4 3.0 5.0 4
1 Problem-Solving 5 4.0 4.0 3
2 Teamwork 3 5.9 NaN 4
3 Customer Satisfaction 5 NaN 5.0 4
4 Initiative 4 3.0 NaN 5

# Calculate averages
df['Average'] = df[['Manager', ‘Peer’, ‘Customer’, ‘Self']].mean(axis=1)

# Output the numeric average results
print("\nAveraged Ratings:")
print(df[['Dimension', ‘Average’ ]])

# Visualize the averages

plt.title('Average Performance Ratings’ )
plt.xlabel( 'Dimension' )

plt.ylabel( ‘Average Rating’ )
plt.xticks(rotation=45)

plt.show()

Averaged Ratings:
Dimension Average

(2) Communication 4.000000
1 Problem-Solving 4.000000
2 Teamwork 4.000000
3 Customer Satisfaction 4.666667
4 Initiative 4.9eee00
Average Performance Ratings
4
23
pe)
©
a
wv
aD
z

Dimension

# Calculate sums
df['Sum'] = df[['Manager', 'Peer', ‘Customer’, 'Self']].sum(axis=1)

# Output the numeric sum results
print("\nSummed Ratings:")
print(df[[ ‘Dimension’, 'Sum']])

# Visualize the sums

plt.bar(df['Dimension'], df['Sum'], color='lightgreen' )
plt.title('Summed Performance Ratings’ )

plt.xlabel( 'Dimension' )

plt.ylabel('Sum of Ratings')

plt.xticks(rotation=45)

plt.show()

Summed Ratings:
Dimension Sum

(2) Communication 16.0
1 Problem-Solving 16.9
2 Teamwork 12.0
3 Customer Satisfaction 14.0
4 Initiative 12.0
Summed Performance Ratings

Ww

Do

.—

+e

o

fa al

cS

°

&

a}

V7,

Dimension

# Normalize the ratings (convert to percentages)
df_normalized = df[['Manager', 'Peer', 'Customer', 'Self']].apply(lambda x: (x / 5) * 100)

# Calculate the average normalized score
df['Normalized'] = df_normalized.mean(axis=1)

# Output the numeric normalized results
print("\nNormalized Ratings (in Percentage):")
print(df[['Dimension', 'Normalized']])

# Visualize the normalized scores

plt.bar(df['Dimension'], df['Normalized'], color='salmon' )
plt.title( ‘Normalized Performance Ratings (Percentage) ')
plt.xlabel( 'Dimension' )

plt.ylabel('Normalized Rating (%)')
plt.xticks(rotation=45)

plt.show()

Normalized Ratings (in Percentage):
Dimension Normalized

2) Communication 80.000000
1 Problem-Solving 80.900000
2 Teamwork 80.800000
3 Customer Satisfaction 93.333333
4 Initiative  80.90000e0
Normalized Performance Ratings (Percentage)
80
£
2 60
+
©
fe a
bo]
w
N
: 40
o
=

20

Dimension

# Define weights for each dimension (must add up to 1)
weights = {

"Communication': 0.15,

"Problem-Solving': 9.25,

"Teamwork': 0.10,

"Customer Satisfaction': 90.35,

‘Initiative’: 0.15

# Multiply the normalized ratings by the corresponding weight
df['Weighted'] = df.apply(lambda row: row['Normalized'] * weights[row['Dimension']], axis=1)

# Output the weighted ratings
print("\nWeighted Ratings (Based on Assigned Weights):")
print(df[['Dimension', 'Weighted' ]])

# Visualize the weighted ratings

plt.bar(df[ 'Dimension'], df['Weighted'], color='purple' )
plt.title('Weighted Performance Ratings' )

plt.xlabel( ‘Dimension’ )

plt.ylabel( ‘Weighted Rating' )

plt.xticks(rotation=45)

plt.show()

Weighted Ratings (Based on Assigned Weights):
Dimension Weighted

(3) Communication 12.000000
1 Problem-Solving 20.900000
2 Teamwork 8.988000
3 Customer Satisfaction 32.666667
4 Initiative 12.9ee0e00
Weighted Performance Ratings
30
25
Da
=
% 20
a
oO
Vv
=
ob
wo
=

=
oO

ui

Dimension

Colab paid products - Cancel contracts here

El comment A Share @&

Connect v

‘*vVoeo8 eu:

w



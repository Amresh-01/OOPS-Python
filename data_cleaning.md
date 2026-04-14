## Methods to Handle Missing Metascore Values
### Method 1: Simple Removal (Drop rows with missing values)
-# Method 1: Drop rows with missing value(eg.Metascore)
df_dropped = df.dropna(subset=['missinf colomun'])

print("=== METHOD 1: DROP MISSING ROWS ===")
print(f"Original rows: {len(df)}")
print(f"Rows after dropping: {len(df_dropped)}")
print(f"Rows removed: {len(df) - len(df_dropped)} ({((len(df) - len(df_dropped))/len(df))*100:.1f}%)")

### Check if this affected the rating distribution
print(f"\nOriginal mean rating: {df['IMDB_Rating'].mean():.3f}")
print(f"After dropping mean rating: {df_dropped['IMDB_Rating'].mean():.3f}")

## when to use Method 1
    - When missing data is less than 5-10% of total (here it's 15.7% - borderline)
    - When the missing data is random (not biased)
    - When you have plenty of data

## Method 2: Fill with Median Value (Recommended for beginners)

    -# Method 2: Fill missing values with median
df_median = df.copy()
median_metascore = df['Metascore'].median()
df_median['Metascore'] = df_median['Metascore'].fillna(median_metascore)

print("=== METHOD 2: FILL WITH MEDIAN ===")
print(f"Median Metascore: {median_metascore}")
print(f"Missing values filled: {df['Metascore'].isnull().sum()}")
print(f"Remaining missing: {df_median['Metascore'].isnull().sum()}")

# Show examples of filled values
print("\nExample of filled values:")
missing_rows = df[df['Metascore'].isnull()].head(3)
for idx, row in missing_rows.iterrows():
    print(f"  {row['Series_Title']} (Rating: {row['IMDB_Rating']}) -> Metascore filled with {median_metascore}")

Why median is good:

Not affected by outliers

Preserves the central tendency of the data

Simple and fast

 Student scores: 85, 90, 88, 92, 87, [missing], 89, 91

 Median Fill (RECOMMENDED):
 Missing score = 89 (median of available scores)
 Result: Simple, fair, reasonable

 Drop Rows (NOT RECOMMENDED):
 Delete the missing student entirely
 Result: Lose data, incomplete analysis

 Mean Fill (NOT RECOMMENDED):
 Missing score = 88.9 (mean)
 Result: Fine, but median is better for test scores

 Your movie ratings are similar - median works best!
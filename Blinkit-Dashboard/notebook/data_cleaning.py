import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("BlinkIT Grocery Data.csv")

# Preview data
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Item Weight with average weight
df['Item Weight'].fillna(df['Item Weight'].mean(), inplace=True)

# Fill missing Rating with average rating
df['Rating'].fillna(df['Rating'].mean(), inplace=True)

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Sales to numeric if needed
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# Remove rows where Sales is missing
df = df.dropna(subset=['Sales'])

# Feature Engineering

# Sales Category
df['Sales Category'] = pd.qcut(
    df['Sales'],
    q=4,
    labels=['Low Sales', 'Medium Sales', 'High Sales', 'Top Seller']
)

# Visibility Category
df['Visibility Level'] = pd.cut(
    df['Item Visibility'],
    bins=[0, 0.05, 0.15, df['Item Visibility'].max()],
    labels=['Low Visibility', 'Medium Visibility', 'High Visibility']
)

# Rating Category
df['Rating Level'] = pd.cut(
    df['Rating'],
    bins=[0, 2.5, 3.5, 5],
    labels=['Low Rated', 'Average Rated', 'High Rated']
)

# Save cleaned dataset
df.to_csv("blinkit_cleaned_data.csv", index=False)

print("\nCleaning Completed!")
print("Clean dataset saved as blinkit_cleaned_data.csv")
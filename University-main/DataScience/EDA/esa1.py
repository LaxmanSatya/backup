import numpy as np
import pandas as pd  #type: ignore
import matplotlib.pyplot as plt #type: ignore
import seaborn as sns #type: ignore

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic housing data (5,000 rows)
n_samples = 5000
sq_ft = np.random.normal(2000, 500, n_samples).round()
prices = (sq_ft * 3000 + np.random.normal(500000, 200000, n_samples)).round()
bedrooms = np.random.choice([2, 3, 4, 5], size=n_samples, p=[0.2, 0.5, 0.2, 0.1])
neighborhoods = np.random.choice(['Downtown', 'Suburb A', 'Suburb B', 'Rural'], size=n_samples, p=[0.2, 0.4, 0.2, 0.2])

df = pd.DataFrame({
    'SquareFootage': sq_ft,
    'Bedrooms': bedrooms.astype(float),
    'Neighborhood': neighborhoods,
    'Price': prices
})

# Artificially inject messy data for the EDA demonstration
df.loc[df.sample(45).index, 'Bedrooms'] = np.nan  # 45 Missing values
df.loc[100, 'Bedrooms'] = 42.0                     # Outlier (42 bedrooms)
df = pd.concat([df, df.iloc[[10, 20, 30]]], ignore_index=True) # 3 Duplicate rows

# --- START EDA ---

# Step 1: Structural Assessment
print("Dataset Shape:", df.shape)
print("\nData Types and Info:")
df.info()

# Check for duplicates and drop them
print(f"\nDuplicate rows found: {df.duplicated().sum()}")
df = df.drop_duplicates().reset_index(drop=True)

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Handle missing data: Impute missing Bedrooms with the median
median_bedrooms = df['Bedrooms'].median()
df['Bedrooms'] = df['Bedrooms'].fillna(median_bedrooms)

# Identify Outliers using summary statistics
print("\nDescriptive Statistics (Notice the Max Bedrooms is 42):")
print(df.describe())

# Remove the extreme outlier (42 bedrooms)
df = df[df['Bedrooms'] < 10].reset_index(drop=True)
print(f"\nShape after removing outliers: {df.shape}")

# Set up plotting aesthetics
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# Convert price to millions for clearer visual interpretation
plot_df = df.copy()
plot_df['Price'] = plot_df['Price'] / 1_000_000

# 1. Distribution of House Prices (Univariate)
plt.subplot(2, 2, 1)
sns.histplot(data=plot_df, x='Price', kde=True, color='skyblue')
plt.title('Distribution of House Prices')
plt.xlabel('Price (in Millions)')

# 2. Square Footage vs Price (Bivariate Scatter Plot)
plt.subplot(2, 2, 2)
sns.scatterplot(data=plot_df.sample(500), x='SquareFootage', y='Price', alpha=0.6, color='coral')
plt.title('Price vs. Square Footage (Sample of 500)')

# 3. Prices by Neighborhood (Bivariate Box Plot)
plt.subplot(2, 2, 3)
sns.boxplot(data=df, x='Neighborhood', y='Price', palette='Set2')
plt.title('Price Distribution by Neighborhood')

# 4. Correlation Heatmap (Multivariate)
plt.subplot(2, 2, 4)
# Exclude categorical columns for numeric correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix Heatmap')

plt.tight_layout()
plt.show()

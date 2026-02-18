import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "survey_data.csv"  # Ensure the correct file path
df = pd.read_csv(file_path, encoding="latin1")

# Clean column names
df.columns = df.columns.str.strip()

# Convert 'Annual_Income' and 'Spending_Score' to numeric after removing symbols
df["Annual_Income"] = pd.to_numeric(df["Annual_Income"].replace('[^0-9.]', '', regex=True), errors='coerce')
df["Spending_Score"] = pd.to_numeric(df["Spending_Score"].replace('[^0-9.]', '', regex=True), errors='coerce')

# Handle missing values
df.dropna(inplace=True)

# Compute the correlation between Annual_Income and Spending_Score
correlation = df["Annual_Income"].corr(df["Spending_Score"])
print(f"\n📌 Correlation between Annual Income and Spending Score: {correlation:.2f}")

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["Annual_Income"], y=df["Spending_Score"], alpha=0.7, edgecolor='w')
plt.title(f'Annual Income vs. Spending Score (Correlation: {correlation:.2f})', fontsize=14)
plt.xlabel('Annual Income ($)', fontsize=12)
plt.ylabel('Spending Score', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Histogram of Annual Income and Spending Score
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df["Annual_Income"], bins=30, kde=True, color='blue')
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income')

plt.subplot(1, 2, 2)
sns.histplot(df["Spending_Score"], bins=30, kde=True, color='green')
plt.title('Distribution of Spending Score')
plt.xlabel('Spending Score')
plt.tight_layout()
plt.show()

# Boxplot to analyze spending habits by gender
plt.figure(figsize=(8, 6))
sns.boxplot(x=df["Gender"], y=df["Spending_Score"], palette='coolwarm')
plt.title('Spending Score Distribution by Gender')
plt.show()

# Pair plot for relationships among numeric variables
sns.pairplot(df, hue="Gender", diag_kind='kde')
plt.show()

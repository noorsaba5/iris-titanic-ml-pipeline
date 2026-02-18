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

# Compute correlation
correlation = df["Annual_Income"].corr(df["Spending_Score"])

# Create subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Scatter Plot
sns.scatterplot(x=df["Annual_Income"], y=df["Spending_Score"], alpha=0.7, edgecolor='w', ax=axes[0, 0])
axes[0, 0].set_title(f'Annual Income vs. Spending Score (Corr: {correlation:.2f})')

# Histogram of Annual Income
sns.histplot(df["Annual_Income"], bins=30, kde=True, color='blue', ax=axes[0, 1])
axes[0, 1].set_title('Distribution of Annual Income')

# Histogram of Spending Score
sns.histplot(df["Spending_Score"], bins=30, kde=True, color='green', ax=axes[1, 0])
axes[1, 0].set_title('Distribution of Spending Score')

# Boxplot for Spending Score by Gender
sns.boxplot(x=df["Gender"], y=df["Spending_Score"], palette='coolwarm', ax=axes[1, 1])
axes[1, 1].set_title('Spending Score Distribution by Gender')

# Adjust layout
plt.tight_layout()

# Show all plots together
plt.show()

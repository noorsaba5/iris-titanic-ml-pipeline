import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
file_path = "survey_data.csv"  # Ensure the correct file path
df = pd.read_csv(file_path)

# Step 2: Display basic information
print("🔹 Dataset Information:")
print(df.info())

# Step 3: Check and handle missing values
missing_values = df.isnull().sum()
print("\n🔹 Missing Values:\n", missing_values)

# Remove rows with missing values (if any)
df.dropna(inplace=True)

# Step 4: Compute the correlation between Annual_Income and Spending_Score
correlation = df["Annual_Income"].corr(df["Spending_Score"])
print(f"\n📌 Correlation between Annual Income and Spending Score: {correlation:.2f}")

# Step 5: Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df["Annual_Income"], df["Spending_Score"], alpha=0.7, edgecolors='w', label='Data Points')

# Add title and axis labels with the correlation coefficient
plt.title(f'Annual Income vs. Spending Score (Correlation: {correlation:.2f})', fontsize=14)
plt.xlabel('Annual Income ($)', fontsize=12)
plt.ylabel('Spending Score', fontsize=12)

# Add grid and legend for better readability
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# Step 6: Show the plot
plt.show()
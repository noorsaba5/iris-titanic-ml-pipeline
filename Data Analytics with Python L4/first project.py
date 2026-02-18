import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Argos_Best_Selling_Products.csv")

# Add Revenue Column
df["Revenue (£)"] = df["Price (£)"] * df["Units_Sold"]

# Summary Statistics
print("Summary Statistics:")
print(df.describe())

# Correlation Matrix
correlation_matrix = df[["Price (£)", "Units_Sold", "Avg_Rating", "Revenue (£)"]].corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

# Top 5 best-selling products by revenue
top_revenue_products = df.nlargest(5, "Revenue (£)")
print("\nTop 5 Best-Selling Products by Revenue:")
print(top_revenue_products[["Product_Name", "Category", "Revenue (£)"]])

# Top 5 best-selling products by units sold
top_units_sold_products = df.nlargest(5, "Units_Sold")
print("\nTop 5 Best-Selling Products by Units Sold:")
print(top_units_sold_products[["Product_Name", "Category", "Units_Sold"]])

# Visualization: Revenue by Category
plt.figure(figsize=(10, 5))
sns.barplot(x="Category", y="Revenue (£)", data=df.groupby("Category")["Revenue (£)"].sum().reset_index(), palette="viridis")
plt.title("Total Revenue by Category")
plt.xlabel("Product Category")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.show()

# Visualization: Price vs. Units Sold
plt.figure(figsize=(8, 5))
sns.scatterplot(x=df["Price (£)"], y=df["Units_Sold"], hue=df["Category"], palette="coolwarm")
plt.title("Price vs. Units Sold")
plt.xlabel("Price (£)")
plt.ylabel("Units Sold")
plt.show()

# Visualization: Rating Distribution
plt.figure(figsize=(8, 5))
sns.boxplot(x="Category", y="Avg_Rating", data=df, palette="Set2")
plt.title("Product Ratings Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Average Rating")
plt.xticks(rotation=45)
plt.show()

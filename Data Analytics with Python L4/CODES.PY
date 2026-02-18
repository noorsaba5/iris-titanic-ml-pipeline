import pandas as pd

# Sample Data
data = {
    'Study_Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Exam_Score': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Compute Correlation Matrix
correlation_matrix = df.corr()

print(correlation_matrix)
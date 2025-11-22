import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
# Step 1: Create two lists with random floats
list1 = np.random.uniform(0, 100, 100).tolist()  # Random floats between 0 and 100
list2 = np.random.uniform(50, 150, 100).tolist()  # Random floats between 50 and 150
 
# Step 2: Create a DataFrame to hold the lists
data = pd.DataFrame({
    'List1': list1,
    'List2': list2
})
 
# Step 3: Compute the correlation between List1 and List2
correlation = data['List1'].corr(data['List2'])
 
# Step 4: Create a scatter plot with the correlation coefficient
plt.figure(figsize=(10, 6))
plt.scatter(data['List1'], data['List2'], alpha=0.7, edgecolors='w', label='Data points')
 
# Add title and axis labels
plt.title(f'Scatter Plot of List1 vs List2 (Correlation Coefficient = {correlation:.2f})', fontsize=14)
plt.xlabel('List1 (Random Floats 0-100)', fontsize=12)
plt.ylabel('List2 (Random Floats 50-150)', fontsize=12)
 
# Add grid and legend for better readability
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
 
# Step 5: Display the plot
plt.show()
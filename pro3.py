import pandas as pd  # Import the pandas library

# Initialize an empty list to store user inputs
numbers = []

# Ask the user for 5 integer inputs
for i in range(5):
    num = int(input(f"Enter integer {i+1}: "))  # Get input and convert to int
    numbers.append(num)  # Append to list

# Convert the list into a Pandas Series
data = pd.Series(numbers)

# Calculate statistics
mean_value = data.mean()
median_value = data.median()
mode_value = data.mode().tolist()  # Convert mode to a list in case of multiple modes

# Display the results
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
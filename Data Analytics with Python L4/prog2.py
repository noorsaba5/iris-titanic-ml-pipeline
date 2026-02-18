import pandas as pd  # Import the pandas library
 
# Define a list of integers
numbers = [5, 12, 8, 12, 7, 10, 15, 8, 9, 6, 8, 5, 11, 9, 7, 10, 5,6,8,9,4,6,9,4,6,3,8,4,9,2,1,5,2,9,8,5,7,6,4,4]
 
# Convert the list into a Pandas Series (a one-dimensional labeled array)
data = pd.Series(numbers)
 
# Calculate the mean (average) of the numbers
mean_value = data.mean()
 
# Calculate the median (middle value when sorted)
median_value = data.median()
 
# Calculate the mode (most frequently occurring number(s))
mode_value = data.mode().tolist()  # Convert to a list in case there are multiple modes
 
# Display the results
print("Mean:", mean_value)    # Print the mean
print("Median", median_value)  # Print the median
print("Mode:", mode_value)    # Print the mode
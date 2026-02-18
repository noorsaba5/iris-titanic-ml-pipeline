# Static list of numbers to be used in the game
numbers = [10, 15, 8, 8, 20, 5]
 
# Welcome message and instructions
print("Welcome to Higher or Lower! (Enter 'H' for Higher, 'L' for Lower)")
 
# Loop through the numbers, except the last one (since we compare with the next)
for i in range(len(numbers) - 1):
    current = numbers[i]      # Get the current number
    next_num = numbers[i + 1] # Get the next number
    print("")  # Print a blank line for readability
    print("Current number:", current)  # Show the current number
 
    # Ask user for input and convert to uppercase for uniformity
    guess = input("Higher (H) or Lower (L)? ").strip().upper()
 
    # If the next number is the same as the current, user automatically moves on
    if next_num == current:
        print("Same number! Moving on...")
        continue  # Skip to the next iteration of the loop
 
    # Check if the user's guess is correct
    if (guess == "H" and next_num > current) or (guess == "L" and next_num < current):
        print("Correct!")  # Correct guess, move to the next number
    else:
        # Wrong guess, show the correct number and end the game
        print("Wrong! The next number was", next_num, ". Game over!")
        break  # Exit the loop since the game is over
 
# If the loop completes without a wrong answer, display the success message
else:
    print("")  # Blank line for spacing
    print("You completed the game! Well done!")  # Message for successful completion
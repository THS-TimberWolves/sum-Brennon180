# Get input from the user
try:
    user_number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

# Initialize variables
current_number = 1
total_sum = 0

# Use a while loop to sum numbers from 1 to user_number
while current_number <= user_number:
    total_sum += current_number
    current_number += 1

# Print the result
print(f"The sum of numbers from 1 to {user_number} is: {total_sum}")#for Summation code here


try:
    user_number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

total_sum = 0

for number in range(1, user_number + 1):
    total_sum += number


print(f"The sum of numbers from 1 to {user_number} is: {total_sum}")

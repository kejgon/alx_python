import random

# Generate a random number between -10000 and 10000 (inclusive)
number = random.randint(-10000, 10000)

# Extract the last digit with sign
if number >= 0:
    last_digit = number % 10
else:
    last_digit = -(-number % 10)
    
# Initialize an empty string to hold the output
output = ""

# Check conditions based on the value of the last digit
if last_digit > 5:
    output = "and is greater than 5"

if last_digit == 0:
    output = "and is 0"

if last_digit < 6 and last_digit != 0:
    output = "and is less than 6 and not 0"

# Print the result
print("Last digit of {} is {} {}".format(number, last_digit, output))

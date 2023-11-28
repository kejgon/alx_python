# import random

# # Generate a random number between -10000 and 10000 (inclusive)
# number = random.randint(-10000, 10000)

# # Extract the last digit with sign
# if number >= 0:
#     last_digit = number % 10
# else:
#     last_digit = -(-number % 10)
    
# # Initialize an empty string to hold the classification
# classification = ""

# # Check conditions based on the value of the last digit
# if last_digit > 5:
#     classification = "and is greater than 5"

# if last_digit == 0:
#     classification = "and is 0"

# if last_digit < 6 and last_digit != 0:
#     classification = "and is less than 6 and not 0"

# # Print the result
# print("Last digit of {} is {} {}".format(number, last_digit, classification))

import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
if number < 0:
    last_digit = last_digit * int(-1)

if last_digit > 5:
     output = "and is greater than 5"
elif last_digit == 0:
    output = "and is 0" 
else:
    output = "and is less than 6 and not 0"

print("Last digit of {} is {} {}".format(number, last_digit, output))

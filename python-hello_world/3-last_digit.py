import random

# Generate a random number
number = random.randint(-10000, 10000)

# Determine the sign of the number
if number < 0:
    sign_classification = "negative"
elif number == 0:
    sign_classification = "zero"
else:
    sign_classification = "positive"

# Extract the last digit
last_digit = abs(number) % 10

# Initialize the classification string for the last digit
classification = ""

# Classify the last digit
if last_digit > 5:
    classification = "and is greater than 5"
elif last_digit == 0:
    classification = "and is 0"
elif 0 < last_digit < 6:
    classification = "and is less than 6 and not 0"

# Print the result
print("Last digit of {} is {} {} and the number is {}".format(number, last_digit, classification, sign_classification))

import random
number = random.randint(-10000, 10000)
# Extract the last digit
last_digit = abs(number) % 10

# Extract the last digit
last_digit = abs(number) % 10



# Classify the last digit
classification = ""

if last_digit > 5:
    classification = "and is greater than 5"
elif last_digit == 0:
    classification = "and is 0"
else:
    classification = "and is less than 6 and not 0"

# Print the result
print("Last digit of {} is {} {}".format(number, last_digit, classification))
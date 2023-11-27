import random
number = random.randint(-10, 10)

# Classify the number
if number > 0:
    classification = "is positive"
elif number == 0:
    classification = "is zero"
else:
    classification = "is negative"

# Print the number and its classification
print("The number {} {}".format(number, classification))
import random
number = random.randint(-10, 10)

if number > 0:
    print("The number {} is positive.".format(number))
elif number == 0:
    print("The number {} is zero.".format(number))
else:
    print("The number {} is negative.".format(number))
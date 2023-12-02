# main_program.py

# Assign values to variables a and b
a = 1
b = 2

# Import and alias the add function from 0-add.py
from add_0 import add
if __name__ == "__main__":

    print("{} + {} = {}".format(a, b, add(a, b)))

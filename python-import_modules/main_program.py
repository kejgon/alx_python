# main_program.py

# Assign values to variables a and b
a = 1
b = 2

if __name__ == "__main__":
    # Import the add function from 0-add.py
    from 0-add import add

    # Print the result using string format
    print("{} + {} = {}".format(a, b, add(a, b)))

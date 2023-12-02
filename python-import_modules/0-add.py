

a = 1
b = 2

def add(a, b):
    return a + b

# This block ensures that the code below is only executed
# when the module is run as the main program, not when imported
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
 



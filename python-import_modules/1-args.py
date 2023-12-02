# argument_printer.py

import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1
    plural_s = 's' if num_arguments != 1 else ''

    if num_arguments > 0:
        print("{} argument{}:".format(num_arguments, plural_s))
    else:
        print("0 arguments.")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()

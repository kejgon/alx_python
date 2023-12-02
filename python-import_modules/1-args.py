# argument_printer.py

import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1
    plural_s = 's' if num_arguments != 1 else ''

    print("Number of argument{}: {}".format(plural_s, num_arguments), end='')
    print("{}".format('' if num_arguments == 0 else ':'))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))

if __name__ == "__main__":
    print_arguments()

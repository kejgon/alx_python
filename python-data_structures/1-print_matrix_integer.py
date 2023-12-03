def print_matrix_integer(matrix=[]):
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()

# Example usage
if __name__ == "__main__":

    print_matrix_integer()
  
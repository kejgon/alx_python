def print_matrix_integer(matrix=[]):
    for row in matrix:
        print(" ".join(map(str, row)))

# Example usage
if __name__ == "__main__":
    matrix = []

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()

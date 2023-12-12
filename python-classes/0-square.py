class Square:
    def __init__(self, size):
        self.__size = size

# Example usage
if __name__ == "__main__":
    my_square = Square(3)

    # Output: <class '__main__.Square'>
    print(type(my_square))

    # Output: {'_Square__size': 3}
    print(my_square.__dict__)

    # Output: 'Square' object has no attribute 'size'
    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    # Output: 'Square' object has no attribute '__size'
    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)

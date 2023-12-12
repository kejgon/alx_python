class Square:
    """A class representing a square.

    The Square class is designed to create square objects with a specified size.
    It initializes the size attribute during object creation.

    Attributes:
        __size (int): The size of the square.

    Methods:
        No additional methods are provided in this Class

    Example:
        >>> square = Square(5)
        >>> print(square.__size)
        5
    """

    def __init__(self, size=3):
        """Initialize a Square object with a specified size.

        Args:
            size (int): The size of the square. Defaults to 3.
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square()
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)
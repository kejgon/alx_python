"""
    A class representing a square.
"""
class Square:
    """
    The Square class is designed to create square objects with a specified size.
    It initializes the size attribute during object creation.

    Attributes:
        __size (int): The size of the square.

    Methods:
        area(): Returns the current square area.
    """

    def __init__(self, size=0):
        """Initialize a Square object with a specified size.

        Args:
            size (int): The size of the square. Defaults to 0.
                Raises:
                    TypeError: If size is not an integer.
                    ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return the current square area."""
        return self.__size ** 2



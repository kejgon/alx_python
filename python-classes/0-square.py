"""
    A class representing a square.
"""
class Square:
    """A class representing a square.

    The Square class is designed to create square objects with a specified size.
    It initializes the size attribute during object creation.

    Attributes:
        __size (int): The size of the square.

    Methods:
        No additional methods are provided in this Class

    """

    def __init__(self, size):
        """Initialize a Square object with a specified size.

        Args:
            size (int): The size of the square. Defaults to 3.
        """
        self.__size = size


# my_square = Square(3)
# print(my_square._Square__size)
# print(my_square.__dict__)










# class Square:
#     def __init__(self, size=3):
#         # Private attribute with a default value
#         self.__size = size

#     @property
#     def getSize(self):
#         # Getter method to access the private attribute
#         return self.__size



# # Creating an instance of the Square class
# my_square = Square()

# # Accessing the size attribute using the getter method
# print(f"Initial Size: {my_square.getSize}")

# # Attempting to change the size attribute (will not work)
# my_square._Square__size = 8
# print(f"Modified Size: {my_square.getSize}")

# Attempting to change the size attribute (will not work)
# try:
#     my_square.size = 5
# except AttributeError as e:
#     print(f"Error: {e}")

# class MyClass:
#     def __init__(self):
#         self.__private_method()

#     def __private_method(self):
#         print("This is a private method.")

# # Creating an instance of MyClass
# my_instance = MyClass()

# # Accessing the private method (not recommended)
# my_instance._MyClass__private_method()


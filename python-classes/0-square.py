class Square:

    def __init__(self, size=2):
        self.__size = size

    def my_square(self, x):
        return x ** 2  

# Create an instance of the Square class
square = Square()

# Access the private attribute using the correct syntax (no direct use of __size)
print('{}'.format(square._Square__size))  # Corrected attribute access

# Use the my_square method
print(square.my_square(2))
print(square.my_square.__dict__)


# class Square:
#     def __init__(self, size):
#         self.__size = size

# # Test the Square class
# if __name__ == "__main__":
#     my_square = Square(3)
#     print(type(my_square))
#     print(my_square.__dict__)

#     try:
#         print(my_square.size)
#     except AttributeError as e:
#         print(e)

#     try:
#         print(my_square.__size)
#     except AttributeError as e:
#         print(e)

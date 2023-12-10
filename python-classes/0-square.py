class Square:

    def __init__(self, size=2):
        self.__size = size

    def my_square(self, x):
        return x ** 2

# Create an instance of the Square class
mysquare = Square()

# Correct output - case: mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)
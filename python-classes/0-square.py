class Square:

    def __init__(self, size=2):
        self.__size = size

    def my_square(self, x):
        return x ** 2

# Create an instance of the Square class
mysquare = Square(3)

# Correct output - case: mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# Correct output - case: mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# mysquare = Square(89)
print(type(mysquare))
print(mysquare.__dict__)

# Correct output - case: mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# Try to access the non-existent attribute 'size'
try:
    print(mysquare.size)
except AttributeError as e:
    print(e)

# Try to access the non-mangled attribute '_size'
try:
    print(mysquare._size)
except AttributeError as e:
    print(e)

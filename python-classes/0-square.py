class Square:

    def __init__(self, size=2):
        self.__size = size

    def my_square(self, x):
        return x ** 2

# Create an instance of the Square class
mysquare1 = Square(3) # Correct output - case: mysquare = Square(3)
print(type(mysquare1))
print(mysquare1.__dict__)



mysquare2 = Square(89)
# mysquare = Square(89)
print(type(mysquare2))
print(mysquare2.__dict__)

mysquare3 = Square(3) # Correct output - case: mysquare = Square(3)

# Correct output - case: mysquare = Square(3)
print(type(mysquare3))
print(mysquare3.__dict__)

# Try to access the non-existent attribute 'size'
try:
    print(mysquare3.size)
except AttributeError as e:
    print(e)

# Try to access the non-mangled attribute '_size'
try:
    print(mysquare3._size)
except AttributeError as e:
    print(e)

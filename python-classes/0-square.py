class Square:
    def __init__(self, size):
        self.__size = size

# Correct output - case: mysquare = Square(3)
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# Correct output - case: mysquare = Square(3)
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# mysquare = Square(89)
mysquare = Square(89)
print(type(mysquare))
print(mysquare.__dict__)

# Correct output - case: mysquare = Square(3)
mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# Try to access the non-existent attribute 'size'
try:
    print(mysquare.size)
except AttributeError as e:
    print(e)

# Try to access the non-mangled attribute '_size'
try:
    print(mysquare._Square__size)
except AttributeError as e:
    print(e)

class Square:
    def __init__(self, size):
        self.__size = size

# Create an instance of the Square class
mysquare = Square(3)
print(type(mysquare))

# Access the __size attribute directly
print(mysquare._Square__size)

# Attempt to access the 'dict_' attribute (which doesn't exist)
try:
    print(mysquare.dict_)
except AttributeError as e:
    print(e)

# Attempt to access the 'size' attribute (which doesn't exist)
try:
    print(mysquare.size)
except AttributeError as e:
    print(e)

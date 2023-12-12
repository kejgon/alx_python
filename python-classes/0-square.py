class Square:
    def __init__(self, size):
        self.__size = size

    def dict_(self):
        return {'__size': self.__size}

# Case 1
mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict_)

# Case 2
mysquare = Square(89)
print(type(mysquare))
print(mysquare.dict_)

# Case 3
mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict_)

# Case 4
try:
    print(mysquare.size)
except AttributeError as e:
    print(e)

# Case 5
mysquare = Square(3)
print(type(mysquare))
print(mysquare.dict_)

# Case 6
try:
    print(mysquare._size)
except AttributeError as e:
    print(e)

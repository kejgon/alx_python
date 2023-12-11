class Square:
    def __init__(self, size):
        self.__size = size



mysquare = Square(3)
print(type(mysquare))
print(mysquare.__dict__)

# mysquare = Square(89)
mysquare = Square(89)
print(type(mysquare))
print(mysquare.__dict__)


# try:
#     print(mysquare.size)
# except AttributeError as e:
#     print(e)

# try:
#     print(mysquare._Square__size)
# except AttributeError as e:
#     print(e)

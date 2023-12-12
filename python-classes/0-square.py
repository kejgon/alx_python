class Square:
    def __init__(self, size=3):
        self.__size = size


my_square = Square()
print(type(my_square))
print(my_square.__dict__)

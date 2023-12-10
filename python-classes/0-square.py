class Square:
    def __init__(self, size):
        self.__size = size

# Test cases
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square._Square__size)
except AttributeError as e:
    print(e)

class Square:

    def __init__(self, size):
        self.__size = int(size)

    def my_square(self, x):
        return x ** 2

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except AttributeError as e:
    print(e)

try:
    print(my_square._Square__size)
except AttributeError as e:
    print(e)
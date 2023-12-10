class Square:

    def __init__(self, size=3):
        self.__size = size

    def my_square(self, x):
        return x ** 2

# Create an instance of the Square class
my_square = Square()

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

"""class Rectangle inheriting from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """principal function"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    """public method def area"""
    def area(self):
        return self.__width * self.__height

    """public method magic"""
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
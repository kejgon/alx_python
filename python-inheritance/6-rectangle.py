"""
    The BaseGeometry class is the base class for geometry-related classes.
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

        
class Rectangle(BaseGeometry):
    """
    The Rectangle class represents a rectangle and inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

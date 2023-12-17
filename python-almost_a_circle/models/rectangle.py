"""
        Rectangle class inherits from Base.
    """
from models.base import Base

class Rectangle(Base):
    """
        Rectangle class inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): X-coordinate of the rectangle (default is 0).
            y (int): Y-coordinate of the rectangle (default is 0).
            id (int): Identifier for the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def getWidth(self):
        """Getter for the width attribute."""
        return self.__width

    def setWidth(self, value):
        """Setter for the width attribute."""
        self.__width = value

    def getHeight(self):
        """Getter for the height attribute."""
        return self.__height

    def setHeight(self, value):
        """Setter for the height attribute."""
        self.__height = value

    def getX(self):
        """Getter for the x attribute."""
        return self.__x

    def setX(self, value):
        """Setter for the x attribute."""
        self.__x = value

    
    def getY(self):
        """Getter for the y attribute."""
        return self.__y

    def setY(self, value):
        """Setter for the y attribute."""
        self.__y = value

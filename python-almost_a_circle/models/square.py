"""
        Square class inherits from Rectangle.
    """
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): Size of the square (width and height).
            x (int): X-coordinate of the square (default is 0).
            y (int): Y-coordinate of the square (default is 0).
            id (int): Identifier for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"


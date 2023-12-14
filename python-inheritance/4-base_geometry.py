"""
This module defines the BaseGeometry class.

The BaseGeometry class is the base class for geometry-related classes.
"""

class BaseGeometry:
    """
    The BaseGeometry class is the base class for geometry-related classes.

    It currently does not have any attributes.
    """

    def area(self):
        """
        Public instance method to calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

# Filter out the automatically added methods in Python 3.6+
attributes = [attr for attr in dir(BaseGeometry) if not callable(getattr(BaseGeometry, attr))]

# print(attributes)

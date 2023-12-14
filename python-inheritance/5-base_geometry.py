"""
    The BaseGeometry class is the base class for geometry-related classes.
"""
class BaseGeometry:
    """
    The BaseGeometry class is the base class for geometry-related classes.

    It includes methods for calculating area and validating integer values.
    """

    def area(self):
        """
        Public instance method to calculate the area.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

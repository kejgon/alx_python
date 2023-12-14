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

    def __dir__(self):
        """
        Customize the dir() output to specify the order of attributes.

        Returns:
            list: A sorted list of attribute names.
        """
        return sorted(['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
                       '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
                       '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
                       '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
                       'area', 'integer_validator'])




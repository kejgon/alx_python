class Base:
    """Base class for managing id attribute in future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): If provided, assigns the id to the instance.
                      If not provided, increments __nb_objects and assigns the new value to the instance id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

# if __name__ == "__main__":
#     b1 = Base()
#     print(b1.id)

#     b2 = Base()
#     print(b2.id)

#     b3 = Base()
#     print(b3.id)

#     b4 = Base(12)
#     print(b4.id)

#     b5 = Base()
#     print(b5.id)

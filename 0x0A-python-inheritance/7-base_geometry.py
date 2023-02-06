#!/usr/bin/python3
"""[Write a class BaseGeometry (based on 6-base_geometry.py).]"""


class BaseGeometry:
    """[Base Geometry class]
    """
    def area(self):
        """[Public instance method: def area(self): that raises
     an Exception with the message area() is not implemented]
        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """[Public instance method: def integer_validator(self, name, value):
         that validates value]
        Arguments:
            name {[str]} -- [description]
            value {[int]} -- [description]
        Raises:
            TypeError: [name must be an integer]
            ValueError: [name must be greater than 0]
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

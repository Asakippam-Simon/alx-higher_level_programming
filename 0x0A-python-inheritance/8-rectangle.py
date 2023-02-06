#!/usr/bin/python3
"""[Write a class Rectangle that inherits from
 BaseGeometry (7-base_geometry.py).]"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """[class Rectangle that inherits from BaseGeometry]
    Arguments:
        BaseGeometry {[type]} -- [Base geometry super class]
    """
    def __init__(self, width, height):
        """[Instantiation with width and height]
        Arguments:
            width {[int]} -- [must beprivate and positve integer]
            height {[int]} -- [must beprivate and positve integer]
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

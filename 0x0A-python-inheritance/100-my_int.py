#!/usr/bin/python3
""" [Write a class MyInt that inherits from int] """


class MyInt(int):
    """[MyInt]
    Arguments:
        int {[class]} -- [superclass int]
    """
    def __init__(self, x):
        """[constructor]
        Arguments:
            x {[int]} -- [value]
        """
        self.x = x

    def __eq__(self, other):
        """[equality changed]
        Arguments:
            other {[type]} -- [description]
        Returns:
            [bool] -- [contrary boolean]
        """
        return (self.x != other)

    def __ne__(self, other):
        """[inequality changed]
        Arguments:
            other {[type]} -- [description]
        Returns:
            [bool] -- [contrary boolean]
        """
        return (self.x == other)

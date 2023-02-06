#!/usr/bin/python3
"""[Write a function that adds a new
 attribute to an object if it’s possible:]"""


def add_attribute(object, name, value):
    """[ adds a new attribute to an object]
    Args:
        object ([type]): [object of a determined class]
        name ([str]): [description]
        value ([str]): [description]
    Raises:
        TypeError: [description]
    """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(object, name, value)

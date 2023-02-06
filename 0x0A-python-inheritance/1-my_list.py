#!/usr/bin/python3
"""========================================================
 Write a class MyList that inherits from list
===========================================================
"""


class MyList(list):
    """[Public instance method that prints the list, but sorted (ascending sort)]
    Arguments:
        list {[Class]} -- [Class list]
    """
    def print_sorted(self):
        print(sorted(self))

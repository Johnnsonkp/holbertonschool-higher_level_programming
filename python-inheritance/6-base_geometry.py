#!/usr/bin/python3
"""
Write a class BaseGeometry with
a public instance method: def area(self):
that raises an Exception with the message
area() is not implemented
"""


class BaseGeometry:
    """
    a BaseGeometry class
    """

    def area(self):
        """
        raises an Exception with the message
        area() is not implemented
        """
        raise Exception("area() is not implemented")

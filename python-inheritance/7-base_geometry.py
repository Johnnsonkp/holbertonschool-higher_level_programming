#!/usr/bin/python3
"""
defines a class BaseGeometry with
the following methods:

def area(self): raises an Exception with 
  the message area() is not implemented
def integer_validator(self, name, value): that validates value:
  assumimg name is always a string
  if value is not an int: raise a TypeError exception, 
    with the message <name> must be an integer
  if value is less or equal to 0: 
    raise a ValueError exception with the 
    message <name> must be greater than 0
"""


class BaseGeometry:
    """defines a BaseGeometry class"""

    def area(self):
        "raises an Exception"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        "Validates value assuming name is a string"
        if not (isinstance(value, int) and type(value) == int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))

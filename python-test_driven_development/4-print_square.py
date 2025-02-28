#!/usr/bin/python3
"""
a function that prints a square with the character #
def print_square(size):
size is the size length of the square
if size is not an int raise TypeError
  size must be an integer
raise ValueError exception is size is less than 0
  size must be >= 0
raise TypeError is size is a float and less than 0
  size must be an integer
"""


def print_square(size):
    """a function that prints a square with the character #"""
    if (isinstance(size, int) is False):
        raise TypeError("size must be an integer")
    if (size < 0):
        raise TypeError("size must be >= 0")

    for i in range(size):
        print("#" * size)

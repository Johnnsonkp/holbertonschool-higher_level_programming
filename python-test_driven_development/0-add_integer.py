#!/usr/bin/python3
# function that adds 2 integers.
# def add_integer(a, b=98):
# Returns an integer: the addition of a and b
# a & b must be ints or floats, otherwise
#   raise a TypeError exception with the message
#   "a must be an integer" or b must be an integer
# a and b must be first casted to integers if they are float


def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

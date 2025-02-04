#!/usr/bin/python3
# def matrix_divided(matrix, div):
# matrix must be a list of lists of integers or floats,

"""
  Module Divide Matrix
  function that divides all elements of a matrix
  matrix must be a list of lists of integers or floats,
"""


def matrix_divided(matrix, div):
    """
    divides all elements of a matrix
    return a new matrix

    args:
      matrix: list of lists
      div: divisible number

    Raise:
      TypeError: div not int or float
      TypeError: matix is not a list of list of number
      ZeroDivisionError: Div is 0

    Return: a new matrix
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (
        type(matrix) is not list
        or not all((type(l) is list) for l in matrix)
        or not all((isinstance(n, (int, float)) for n in l) for l in matrix)
        or len(matrix[0]) == 0
    ):
        raise TypeError("matrix must be a matrix " "(list of lists) of integers/floats")
    l = len(matrix[0])
    if not all((len(x) == l) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [list(map(lambda x: round(x / div, 2), r)) for r in matrix]

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
    if div == float("inf"):
        return [[0.0 for _ in row] for row in matrix]
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (
        not isinstance(matrix, list)
        or matrix == []
        or not all(isinstance(row, list) for row in matrix)
        or not all(
            (isinstance(ele, int) or isinstance(ele, float))
            for ele in [num for row in matrix for num in row]
        )
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        l = len(matrix[0])
        if not all((len(x) == l) for x in matrix):
            raise TypeError("Each row of the matrix must have the same size")
        return [list(map(lambda x: round(x / div, 2), r)) for r in matrix]

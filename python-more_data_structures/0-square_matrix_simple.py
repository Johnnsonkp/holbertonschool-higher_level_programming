#!/usr/bin/python3
# def square_matrix_simple(matrix=[]):
# func computes the square value of all int of a matrix


def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x * x, row)) for row in matrix]

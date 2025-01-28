#!/usr/bin/python3
# def multiply_by_2(a_dictionary):
# You can assume that all values are only integers
# Returns a new dictionary


def multiply_by_2(a_dictionary):
    return {k: a_dictionary[k] * 2 for k in a_dictionary}

#!/usr/bin/python3
# def print_sorted_dictionary(a_dictionary):
# function that prints a dictionary by ordered keys
# Keys should be sorted by alphabetic order
# Remember: uppercase letters are order first
# ahead of lowercase letters


def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) > 0:
        sorted_dictionary = sorted(a_dictionary)

        for key in sorted_dictionary:
            print("{}: {}".format(key, a_dictionary[key]))

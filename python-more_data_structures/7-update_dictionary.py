#!/usr/bin/python3
# function that replaces or adds key/value in a dictionary
# def update_dictionary(a_dictionary, key, value):
# key argument will be always a string
# value argument will be any type
# If key exists in dictionary? the value will be replaced
# If key doesn’t exist in dictionary? it will be created


def update_dictionary(a_dictionary, key, value):
    if len(a_dictionary) > 0:
        a_dictionary[key] = value

    return a_dictionary

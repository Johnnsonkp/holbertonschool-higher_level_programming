#!/usr/bin/python3
# removes all characters c and C from a string
# def no_c(my_string):


def no_c(my_string):
    if my_string is None:
        return
    else:
        new_str = ""

        for char in my_string:
            if char != "c" and char != "C":
                new_str += char
        return new_str

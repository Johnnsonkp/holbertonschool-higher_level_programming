#!/usr/bin/python3
# prints all integers of a list, in reverse order.
# You have to use str.format() to print integers


def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        i = len(my_list) - 1
        while i >= 0:
            print("{}".format(my_list[i]))
            i -= 1
    else:
        return

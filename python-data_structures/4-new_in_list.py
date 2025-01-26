#!/usr/bin/python3
# replaces an element in a list at a specific position
# without modifying the original lis
# If idx is negative or out of range
# function returns a copy of the original list
# def new_in_list(my_list, idx, element):


def new_in_list(my_list, idx, element):
    if len(my_list) <= 0 or idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = [x for x in my_list]
        new_list[idx] = element
        return new_list

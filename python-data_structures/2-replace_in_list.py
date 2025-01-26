#!/usr/bin/python3
# replaces an element of a list at a specific position
# If idx is negative, the function should return the original list
# If idx is out of range the function should returns the original list

def replace_in_list(my_list, idx, element):
    if (idx < 0 or len(my_list) <= idx):
        return my_list
    else:
        my_list[idx] = element
    return my_list

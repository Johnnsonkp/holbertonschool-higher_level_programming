#!/usr/bin/python3
# adds all unique int in a list (once for each int)
# def uniq_add(my_list=[]):


def uniq_add(my_list=[]):
    new_list = 0
    for i in set(my_list):
        new_list += i

    return new_list

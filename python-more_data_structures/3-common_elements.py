#!/usr/bin/python3
# returns a set of common elements in two sets
# def common_elements(set_1, set_2):


def common_elements(set_1, set_2):
    new_set = set()

    for i in set_1:
        for x in set_2:
            if i == x:
                new_set.add(i)

    print("{}".format(new_set))

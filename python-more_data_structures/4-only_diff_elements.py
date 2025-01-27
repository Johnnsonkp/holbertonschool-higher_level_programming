#!/usr/bin/python3
# def only_diff_elements(set_1, set_2):
# returns a set of all elements present in only one set


def only_diff_elements(set_1, set_2):
    new_set = set()

    for i in set_1:
        for x in set_2:
            if i == x:
                new_set.remove(i)
                break
            else:
                new_set.add(i)
                new_set.add(x)

    return new_set

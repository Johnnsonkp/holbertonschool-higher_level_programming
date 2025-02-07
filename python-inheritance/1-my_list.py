#!/usr/bin/python3
# def print_sorted(self):

"""
class MyList(list):
def print_sorted(self):
"""


class MyList(list):
    """MyList Class that contains the print_sorted method"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        new_arr = self

        for i in range(len(new_arr)):
            for x in range(len(new_arr)):
                if not isinstance(new_arr[i], type(new_arr[x])):
                    raise TypeError(
                        "'<' not supported between "
                        "instances of '{}' and '{}'".format(
                            type(new_arr[i]).__name__, type(new_arr[x]).__name__
                        )
                    )

        print(sorted(self))

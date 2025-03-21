#!/usr/bin/python3
# def safe_print_integer(value):
# function that prints an integer with "{:d}".format()
# value can be any type (integer, string, etc.)
# The integer should be printed followed by a new line
# Returns True if value has been correctly printed
# Otherwise, returns False
# You have to use try: / except:
# You have to use "{:d}".format() to print as integer


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

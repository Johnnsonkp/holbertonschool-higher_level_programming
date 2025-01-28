#!/usr/bin/python3
# def safe_print_division(a, b):
# You can assume that a and b are integers
# Result of the division should print on the finally
# Returns the value of the division, otherwise: None
# You have to use try: / except: / finally:


def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div

#!/usr/bin/python3
"""
  function that prints My name is <first name> <last name>
  def say_my_name(first_name, last_name=""):
  first_name and last_name must be string
  or raise TypeError:
  first_name must be a string or
  last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """say_my_name func that prints My name is <first name> <last name>"""
    if (isinstance(first_name, str) == False):
        raise TypeError("first_name must be a string")
    if (isinstance(last_name, str) == False):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name.strip(), last_name.strip()))

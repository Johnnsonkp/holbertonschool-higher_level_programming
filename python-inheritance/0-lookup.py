#!/usr/bin/python3
# def lookup(obj):
""" 
  def lookup(obj):
  function that returns the list of available attributes 
  and methods of an object: 
  Returns a list object
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    if isinstance(obj, int) is not True:
        return dir(obj)

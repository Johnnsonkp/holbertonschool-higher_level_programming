#!/usr/bin/python3
# def lookup(obj):
""" 
  def lookup(obj):
  function that returns the list of available attributes and methods of an object: 
  Returns a list object
"""


def lookup(obj):
    if isinstance(obj, int) != True:
        return dir(obj)

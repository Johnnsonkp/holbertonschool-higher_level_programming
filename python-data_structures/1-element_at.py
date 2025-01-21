#!/usr/bin/python3 
# Write a function that retrieves an element from a list.
# element_at(my_list, idx) 

def element_at(my_list, idx):
  if idx < 0 or my_list[idx] == None:
    return None
  return (my_list[idx])
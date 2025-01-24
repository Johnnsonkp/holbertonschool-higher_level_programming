#!/usr/bin/python3
# 8-uppercase.py
# prints a string in uppercase followed by a new line
def uppercase(str):
    uppercase_str = ""
    for c in str:
        if 'a' <= c <= 'z':
            uppercase_str += chr(ord(c) - 32)
        else:
            uppercase_str += c
    print("{}".format(uppercase_str))


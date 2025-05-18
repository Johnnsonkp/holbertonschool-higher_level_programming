#!/usr/bin/python3
# 3-infinite_add.py
# prints result of the addition of all arguments

from sys import argv
if __name__ == "__main__":
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    print(sum)

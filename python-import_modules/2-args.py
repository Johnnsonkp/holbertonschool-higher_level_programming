#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    if count >= 0:
        print("{} arguments:".format(count))
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

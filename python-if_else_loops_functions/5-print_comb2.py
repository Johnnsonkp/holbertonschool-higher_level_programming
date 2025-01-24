#!/usr/bin/python3
# prints numbers from 0 to 99
for number in range(0, 100):
    if (number) < 99:
        print("{:02}".format(number), end=", ")

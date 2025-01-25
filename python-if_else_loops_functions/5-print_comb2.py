#!/usr/bin/python3
# writes the numbers from 0 to 99
# Numbers must be separated by ,, followed by a space
# Numbers should be printed in ascending order, with two digits
# The last number should be followed by a new line
# You can only use no more than 2 print functions with string format
# You can only use one loop in your code
# print(", ".join("{:02}".format(number) for number in range(100)))

for number in range(0, 100):
    if number < 99:
        print("{:02}, ".format(number), end="")
    else:
        print("{:02}".format(number))

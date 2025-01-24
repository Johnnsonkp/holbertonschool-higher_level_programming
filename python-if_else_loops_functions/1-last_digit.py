#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
str = "Last digit of"
greater_than = "and is greater than 5"
less_than = "and is less than 6 and not 0"

if number:
    if number >= 0:
        if (number % 10) == 0:
            print("Last digit of "f"{number} is "f"{number % 10} and is 0")
        elif (number % 10) < 6:
            print("Last digit of "f"{number} is "f"{number % 10} "f"{less_than}")
        else:
            print("Last digit of "f"{number} is "f"{number % 10} "f"{greater_than}")
    else:
        print("Last digit of "f"{number} is "f"-{(number * -1) % 10} "f"{less_than}")

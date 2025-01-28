#!/usr/bin/python3
# Technical interview preparation:

# You are not allowed to google anything
# Whiteboard first
# Create a function def roman_to_int(roman_string):
# that converts a Roman numeral to an integer.

# You can assume the number will be between 1 to 3999.
# def roman_to_int(roman_string) must return an integer
# If the roman_string is not a string or None, return 0


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0

    for i in range(len(roman_string)):
        if roman_dict.get(roman_string[i], 0) == 0:
            return 0

        if (
            i != (len(roman_string) - 1)
            and roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]
        ):
            num += roman_dict[roman_string[i]] * -1

        else:
            num += roman_dict[roman_string[i]]
    return num

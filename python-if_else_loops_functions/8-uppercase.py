#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line.

    Args:
        str: The input string.
    """
    result = ""
    for char in str:
        ascii_val = ord(char)
        if ord('a') <= ascii_val <= ord('z'):
            uppercase_val = ascii_val - 32
            result += chr(uppercase_val)
        else:
            result += char
    print(result)

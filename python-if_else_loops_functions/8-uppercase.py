#!/usr/bin/python3
def uppercase(str):
    """Prints a string in uppercase followed by a new line.

    Args:
        str: The input string.
    """
    for char in str:
        ascii_val = ord(char)
        if ord('a') <= ascii_val <= ord('z'):
            uppercase_val = ascii_val - 32
            print("{:c}".format(uppercase_val), end="")
        else:
            print(char, end="")
    print()  # Print a newline at the end

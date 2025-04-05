#!/usr/bin/python3
"""
0_add_integer.py

This module contains a function that adds two integers or floats.
The function ensures that the inputs are valid and raises TypeError
if they are not.
"""

def add_integer(a, b=98):
    """Adds two integers or floats and returns the result as an integer.

    Args:
        a (int, float): The first number to add.
        b (int, float, optional): The second number to add. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float, or if they are NaN or infinity.

    Returns:
        int: The sum of a and b, cast to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if a != a or b != b:  # Check for NaN
        raise TypeError("a must be an integer")
    
    if a == float('inf') or a == float('-inf') or b == float('inf') or b == float('-inf'):
        raise TypeError("a must be an integer")

    return int(a) + int(b)

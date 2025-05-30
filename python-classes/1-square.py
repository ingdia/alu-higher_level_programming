#!/usr/bin/python3
"""
This module defines a Square class.
The Square class represents a square with a size attribute.
"""


class Square:
    """
    A class that defines a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.__size = size  # Private attribute

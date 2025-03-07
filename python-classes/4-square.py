#!/usr/bin/python3
"""
4-square.py

This module defines a Square class that represents a square with a specific
size. The Square class includes:
- A private instance attribute `__size` that stores the size of the square.
- A property to retrieve and set the size, ensuring it is a non-negative
  integer.
- A constructor that initializes the size.
- A method to calculate the area of the square.
"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square, must be a non-negative integer.
    """

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the setter to initialize size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Update the private attribute

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Area calculation

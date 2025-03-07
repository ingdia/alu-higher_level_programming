#!/usr/bin/python3
"""
6-square.py

This module defines a Square class that represents a square with a specific
size and position. The Square class includes:
- A private instance attribute `__size` that stores the size of the square.
- A private instance attribute `__position` that stores the position of the
  square.
- Properties to retrieve and set the size and position, ensuring they are
  valid.
- A constructor that initializes the size and position.
- A method to calculate the area of the square.
- A method to print the square using the '#' character, considering the
  position.
"""


class Square:
    """A class that defines a square by its size and position.

    Attributes:
        __size (int): The size of the square, must be a non-negative integer.
        __position (tuple): The position of the square, must be a tuple of
        two positive integers.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer or if position is not a
            tuple of 2 positive integers.
            ValueError: If size is less than 0 or if position values are
            not positive integers.
        """
        self.size = size  # Use the setter to initialize size
        self.position = position  # Use the setter to initialize position

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

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If position values are not positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value  # Update the private attribute

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2  # Area calculation

    def my_print(self):
        """Prints the square using the '#' character, considering the
        position.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")  # Print an empty line
            return

        # Print the position (spaces)
        for _ in range(self.__position[1]):
            print("")  # Print empty lines for vertical position

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

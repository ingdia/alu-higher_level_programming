#!/usr/bin/python3
"""
2-matrix_divided.py

This module contains a function that divides all elements of a matrix
by a given divisor, with appropriate error handling.
"""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int, float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                    if each row of the matrix does not have the same size,
                    or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix with each element divided by div,
                       rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with the results
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix

#!/usr/bin/python3
"""
5-text_indentation.py

This module contains a function that prints text with two new lines
after each of the specified characters: ., ?, and :.
"""

def text_indentation(text):
    """Prints text with two new lines after each of the characters ., ?, and :.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to hold the modified text
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in '.?:':
            result += "\n\n"  # Add two new lines after the character
            # Skip any spaces after the punctuation
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1

    # Print the result without leading or trailing spaces
    print(result.strip())

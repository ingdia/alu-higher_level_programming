#!/usr/bin/python3
import sys


def infinite_add():
    # Initialize sum to 0
    total = 0
    
    # Get all arguments (excluding the script name)
    args = sys.argv[1:]
    
    # Add each argument to the total
    for arg in args:
        total += int(arg)
    
    # Print the result
    print(total)


if __name__ == "__main__":
    infinite_add()

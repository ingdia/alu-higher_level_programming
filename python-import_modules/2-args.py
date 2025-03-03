#!/usr/bin/python3
import sys


def print_arguments():
    # Get the arguments (excluding the script name)
    args = sys.argv[1:]
    num_args = len(args)
    
    # Print the number of arguments with proper grammar
    if num_args == 1:
        print(f"{num_args} argument:", end="")
    else:
        print(f"{num_args} arguments", end="")
    
    # Print : or . depending on if there are arguments
    if num_args == 0:
        print(".")
    else:
        print(":")
    
    # Print each argument with its position
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()

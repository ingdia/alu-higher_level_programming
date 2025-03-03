#!/usr/bin/python3
import hidden_4


def print_names():
    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter out names starting with '__' and sort alphabetically
    filtered_names = sorted([name for name in names if not name.startswith('__')])

    # Print each name
    for name in filtered_names:
        print(name)


if __name__ == "__main__":
    print_names()

#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


import sys


if __name__ == "__main__":
<<<<<<< Updated upstream
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
=======
  save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
  load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
>>>>>>> Stashed changes

  try:
        items = load_from_json_file("add_item.json")
  except FileNotFoundError:
        items = []
<<<<<<< Updated upstream
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
=======
  items.extend(sys.argv[1:])
  save_to_json_file(items, "add_item.json")
>>>>>>> Stashed changes

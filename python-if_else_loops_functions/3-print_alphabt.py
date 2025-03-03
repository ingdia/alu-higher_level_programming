#!/usr/bin/python3
print("".join(
    "{:c}".format(i) for i in range(ord('a'), ord('z'))
    if chr(i) != 'q' and chr(i) != 'e'
))

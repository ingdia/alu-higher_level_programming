#!/usr/bin/bash
impor random
number = random.randint(-10,10)
if number > 0:
    print(f"{number} is positive")
else number==0:
print(f"{number} is zero")
else: 
    print(f"{number} is negative")

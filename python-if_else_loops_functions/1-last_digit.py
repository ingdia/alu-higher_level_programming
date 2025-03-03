#!/usr/bin/python3
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit

# Determine the appropriate message
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# Print the formatted output
print("Last digit of {} is {} {}".format(number, last_digit, message))

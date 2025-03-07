#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = (str[39:66] + ' ' + str[-22:-18] + ' ' + str[:6])
print(str)
Tabitha Akimana
10:10 AM
#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allf = dir()
    for i in range(0, len(allf)):
        if allf[i][:2] != "__":
            print("{:s}".format(allf[i]))
Tabitha Akimana
10:20 AM
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
Tabitha Akimana
10:30 AM
#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        current_value = roman_numerals.get(char, 0)
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value


"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.
"""

def fake_bin(number):
    new_number = ""
    for n in number:
        if n < "5":
            new_number += "0"
        elif n >= "5":
            new_number += "1"
    return new_number

numero = "123456789"

print(fake_bin(numero))
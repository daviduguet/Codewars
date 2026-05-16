
"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    total = 0
    for n in sentence:
        if n in vowels:
            total += 1
        else:
            continue
    return total

text = "Natalia"

print(get_count(text))
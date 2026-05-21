
"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

EXAMPLE

high_and_low("1 2 3 4 5") # return "5 1"
"""

def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    highest = max(numbers)
    lowest = min(numbers)
    return f"{highest} {lowest}"

numeros = "1 2 3 4 9 -1 10"

print(high_and_low(numeros))
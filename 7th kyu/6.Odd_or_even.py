
"""
Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).
"""

def odd_or_even(lista):
    total = sum(lista)
    if total % 2 == 0:
        return "even"
    else:
        return "odd"
        
        
        
numeros = [0,1, 4, 1]

print(odd_or_even(numeros))
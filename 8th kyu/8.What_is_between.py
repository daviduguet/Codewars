
"""
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them
"""

def between(a,b):
    numbers = []
    for n in range(a, b+1):
        numbers.append(n)
    return numbers
        

n1 = 1
n2 = 4

print(between(n1, n2))
    

"""
Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer.

Square all numbers k (0 <= k <= n) between 0 and n.

Count the numbers of digits d used in the writing of all the k**2.

Implement the function taking n and d as parameters and returning this count.
"""

def nb_dig(n, d):
    squares = [i ** 2 for  i in range(0, n+1)]
    return sum(str(k).count(str(d)) for k in squares)

    
digits = nb_dig(10, 1)

print(digits)
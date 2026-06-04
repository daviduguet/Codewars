
"""
Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.
"""

def capitals(word):
    capitals = []
    for i, letter in enumerate(word):
        if letter.isupper():
            capitals.append(i)
        else:
            pass
    return capitals

word = "CodeWarS"

print(capitals(word))
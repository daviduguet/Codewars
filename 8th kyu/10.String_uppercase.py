
"""
Create a method to see whether the string is ALL CAPS.
"""

def is_uppercase(inp):
    for n in inp:
        if n.islower():
            return False
    return True
    
        
word = "HOLA"

print(is_uppercase(word))
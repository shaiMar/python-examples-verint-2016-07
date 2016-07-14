"""
Use range() and list comprehension to get
the list of all lowercase english letters
Hint: look for chr() and ord()
"""

oa = ord('a')
oz = ord('z')
list = [chr(X) for X in range(256) if X>=oa and X<=oz]
print list

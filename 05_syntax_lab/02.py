"""
Write a Python program that randomizes 7 numbers
and prints their sum total.
If the sum is divisable by 7, also print the word "Boom"
"""

from random import randint

sum = int(0)

for n in range(3):
    num = randint(1,100)
    sum = sum + num

print ('the sum of all numbers:'),sum

if sum % 7 == 0:
    print('Boom!')
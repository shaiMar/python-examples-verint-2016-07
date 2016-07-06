"""
Write a program that randomizes integers in a loop
until it finds a number that is divisable by: 7, 13 and 15
"""

from random import randint

numberToDiviseto = 7*13*15


while True:
    num = randint(1,10000000)
    if num % numberToDiviseto ==0:
        print('the number {} is devisable by {}').format(num,numberToDiviseto)
        break
    else:
        print('the number {} isnt devisable by {}').format(num,numberToDiviseto)

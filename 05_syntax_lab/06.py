"""
Write a program that randomizes 2 numbers
and calculates their least common multiplier,
that is the smallest number that is divisable
by both.
For example if the numbers were 4 and 6,
program should print 12
"""

from random import randint

a = randint(1,1000)
b = randint(1,1000)

for muliplier in range(a+b,a*b+1):
    if muliplier % a == 0 and muliplier % b ==0:
        print('the number {} is divisable by {} and {}').format(muliplier,a,b)
        break;



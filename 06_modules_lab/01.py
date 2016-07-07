""" Write a program that takes a count
from sys.argv import and prints "Hello Python"
count times
"""

import sys

times_to_print = 0

if len(sys.argv) > 1:
    times_to_print = int(sys.argv[1])


for n in range(times_to_print):
     print('Hello Python')


""" Write a program that reads 2 numbers from sys.argv
and prints their sum.
"""

import sys

if len(sys.argv) < 3:
    print ('not enough numbers')
else:
     a = int(sys.argv[1])
     b = int(sys.argv[2])

     print('the sum is: {}').format(a+b)


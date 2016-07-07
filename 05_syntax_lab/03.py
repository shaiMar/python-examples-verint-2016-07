"""
Write a program that randomizes a number
and prints the sum total of its digits.
For example if the number was: 2345
The result should be: 14
"""

from random import randint

num = randint(1,1000000)

numberString = str(num)

stringlen = len(numberString)

sum = 0
# go over all the chars in the string and summarize it value 
for index in range(0,stringlen):
    sum = sum + int(numberString[index])


print "the number is {} and the sum is {}".format(num,sum)


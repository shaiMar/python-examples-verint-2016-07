""" Write a program that selects a random number
and asks the user to guess it.

After each guess print a hint "too large" or "too small" to the user.

Bonus: To make things interesting, the program should cheat once in a white
"""

from random import randint

the_number = randint(0,1000)

input_number = 0

while the_number != input_number:
    print ('enter number:')
    input_number = int(raw_input())
    if input_number ==  the_number:
        print ("BOOOOOOOOOOOOOOOM!")
        break;
    if input_number >  the_number:
        print ("too large!")
    else:
        print ("too small!")
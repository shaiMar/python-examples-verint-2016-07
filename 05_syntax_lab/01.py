"""
Write a program that reads 10 numbers from
the user and prints the largest one
"""

largestNumber = int(0)

for n in range(10):
    print"please enter number(%d)" %(n+1)
    currentnumber=int(raw_input())
    if largestNumber < currentnumber:
        largestNumber = currentnumber



print('largest number is :'),largestNumber  
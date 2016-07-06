"""
Write a program that reads lines from the user
until an empty line is inserted.
After the user typed in an empty line,
print all previously inserted lines in reverse
order (from last to first)
"""

line = "ff"

totalstring = ""


while line:
    print('enter next line:')
    line = raw_input()
    totalstring = line + ';' + totalstring

stringsplits = totalstring.split(';')


print('here are the inputed lines in revers:')
for revline in stringsplits:
    if revline:
      print revline


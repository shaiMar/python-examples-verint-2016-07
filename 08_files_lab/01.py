"""
Write a program that takes 2 file names
and appends the second file's contents to
the end of the first one
"""
import sys

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]

with  open(file_name1,'a') as fin:
    with open(file_name2, 'r') as f:
     for line in f:
        fin.write(line)




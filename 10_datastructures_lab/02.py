"""
Write a program that finds anagrams in a words file
Program takes a path to a words file, 
reads the file and searches for words with the same letters.
All words with the same letters should be printed together
"""
import sys

words_sorted_letters_map = {}

with  open(sys.argv[1],'r') as ff:
    for line in ff:
        letter_sorted_string = ''.join(sorted(line.rstrip()))
        isFound = bool(0)
        for k in words_sorted_letters_map:
            if letter_sorted_string in k or k in letter_sorted_string:
                val=words_sorted_letters_map[letter_sorted_string]
                val= val +' ' + line.rstrip()
                words_sorted_letters_map[letter_sorted_string]=val
                isFound = 1
        if isFound == 0:
            words_sorted_letters_map[letter_sorted_string]=line.rstrip()

for j in words_sorted_letters_map:
    print words_sorted_letters_map[j]
           

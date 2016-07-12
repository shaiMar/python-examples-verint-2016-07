"""
Write a program that takes 3 names. The first two
are existing file names and the last is a new file name
Program should write the lines from the first two 
files interwinded into the output file
"""
import sys

file_name1 = sys.argv[1]
file_name2 = sys.argv[2]
output_filename = sys.argv[3]

with  open(file_name1,'r') as f1:
    with open(file_name2, 'r') as f2:
        with open(output_filename, 'w') as fout:
            l1 = f1.readline()
            l2 = f2.readline()
            while l1!='' or l2!='':
                if l1 != '':
                    fout.write(l1)
                    l1 = f1.readline()
                    #this part is for the last line 'OEL' char
                    if l1 == '':
                        fout.write('\n')
                if l2 != '':
                    fout.write(l2)
                    l2 = f2.readline()
                     #this part is for the last line 'OEL' char
                    if l2 == '':
                         fout.write('\n')





                       


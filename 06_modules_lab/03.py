""" Write a program that searches current working directory
for files larger than 1MB. Every time you find such a file print
its name to the user.

- When the program finds a large file. It should ask the user
  a message asking if she wants to delete it, and delete the
  file if requested

- Take threshold and path as command line arguments
"""


import os
import sys


if len(sys.argv) < 3:
    print('not enough arguments , 1st argument file size in KB , 2nd - directory path')
    sys.exit()

file_size_threshold = int(sys.argv[1])*1024
directory_path = sys.argv[2]

for name in os.listdir(directory_path):
    file_full_path=directory_path+"\\"+name
    current_file_size = os.path.getsize(file_full_path)
    if current_file_size > file_size_threshold:
        print(' file  {} the size of {} - press \'y\' in case you want to delete').format(file_full_path,current_file_size)
        is_to_delete = raw_input()
        if is_to_delete == 'y':
            print(' deleting file . . . ')
            os.remove(file_full_path)
            






#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:20:25 (UT+8) daisuke>
#

# importing os module
import os

# getting currently working directory
cwd = os.getcwd ()

# printing currently working directory
print (f'cwd = "{cwd}"')

# getting a list of files and directory
list_files1 = os.scandir ()

# printing list of files and directory
print (f'files and directories:')
for obj in list_files1:
    print (f'  {obj.name}')
    print (f'    is_dir = {obj.is_dir ()}')

# new directory name
dir_new = 'mynewdir'

# printing status
print (f'now, making a new directory...')

# making a new directory
os.mkdir (dir_new)

# printing status
print (f'finished making a new directory!')

# getting a list of files and directory
list_files2 = os.scandir ()

# printing list of files and directory
print (f'files and directories:')
for obj in list_files2:
    print (f'  {obj.name}')
    print (f'    is_dir = {obj.is_dir ()}')

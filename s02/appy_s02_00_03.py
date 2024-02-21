#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:19:44 (UT+8) daisuke>
#

# importing os module
import os

# target directory
dir_target = '/bin'

# obtaining a list of files and directories at the directory "dir_target"
list_files = os.listdir (path=dir_target)

# printing files and directories
print (f'list of files and directories at "{dir_target}":')
# for each file (or directory) in the list
for filename in list_files:
    # printing name of file (or directory)
    print (f'  {filename}')

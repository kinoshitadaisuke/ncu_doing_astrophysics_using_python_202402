#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:19:37 (UT+8) daisuke>
#

# importing os module
import os

# target directory
dir_target = '/bin'

# printing status
print (f'now, changing directory to "{dir_target}"...')

# changing directory
os.chdir (dir_target)

# printing status
print (f'finished changing directory to "{dir_target}"!')

# knowing where you are now
cwd = os.getcwd ()

# printing where you are now
print (f'currently working directory = "{cwd}"')

# obtaining a list of files and directories at currently working directory
list_files = os.listdir ()

# printing files and directories at "/bin"
print (f'list of files and directories at "{dir_target}":')
# for each file (or directory) in the list
for filename in list_files:
    # printing name of file (or directory)
    print (f'  {filename}')

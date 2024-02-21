#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:22:45 (UT+8) daisuke>
#

# importing pathlib module
import pathlib

# importing shutil module
import shutil

# file name of original file
file_original = 'pi_1000.txt'

# file name of new file
file_new = 'copy_of_pi_1000.txt'

# a function to carry out existence check for a file
def do_existence_check (filename):
    # making a pathlib object
    path_target = pathlib.Path (filename)
    # carrying out an existence check
    result = path_target.exists ()
    # returning result
    return result

# existence check for original file
exist_original = do_existence_check (file_original)
exist_new      = do_existence_check (file_new)

# printing results of existence checks
print (f'results of existence checks before copying file:')
print (f'  existence of file {file_original:24s} = {exist_original}')
print (f'  existence of file {file_new:24s} = {exist_new}')

# printing status
print (f'now, copying file from {file_original} to {file_new}...')

# copying file using shutil.copy2 ()
shutil.copy2 (file_original, file_new)

# printing status
print (f'finished copying file from {file_original} to {file_new}!')

# existence check for original file
exist_original = do_existence_check (file_original)
exist_new      = do_existence_check (file_new)

# printing results of existence checks
print (f'results of existence checks after copying file:')
print (f'  existence of file {file_original:24s} = {exist_original}')
print (f'  existence of file {file_new:24s} = {exist_new}')

#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/07 22:22:07 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# constructing a parser object
descr  = 'existence check of files'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-v', '--verbose', action='store_true', default=False, \
                     help='verbose mode (default: False)')
parser.add_argument ('files', nargs='+', \
                     help='files for existence check')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
verbose    = args.verbose
list_files = args.files

# making an empty dictionary to store results of existence check
dic_existence = {}

# processing files
for file_target in list_files:
    # printing status
    if (verbose):
        print (f'Now, checking file "{file_target}"...')
    # making pathlib object
    path_target = pathlib.Path (file_target)
    # existence check
    existence = path_target.exists ()
    # storing result of existence check into dictionary
    dic_existence[file_target] = existence
    # printing result of existence check
    if (existence):
        print (f'  File "{file_target}" exists.')
    else:
        print (f'  File "{file_target}" does not exist.')
    # printing status
    if (verbose):
        print (f'Finished checking file "{file_target}"!')

# printing summary
if (verbose):
    print (f'')
    print (f'Summary of existence check:')
    for file_target in list_files:
        if (dic_existence[file_target]):
            print (f'  {file_target:32s} : does exist')
        else:
            print (f'  {file_target:32s} : does NOT exist')

#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/02 08:20:05 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

#
# command-line argument analysis
#

# constructing parser object
descr  = f"existence check of files"
parser = argparse.ArgumentParser (description=descr)

# adding options
parser.add_argument ('files', type=str, nargs='+', \
                     help=f"files for existence check")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
list_files = args.files

#
# existence check of files
#

# processing each file
for filename in list_files:
    # making pathlib object
    path_file = pathlib.Path (filename)
    # existence check
    existence = path_file.exists ()
    # printing result
    if (existence):
        print (f"the file '{filename}' exists!")
    else:
        print (f"the file '{filename}' does not exist!")

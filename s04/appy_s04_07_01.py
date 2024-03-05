#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 08:20:12 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# constructing a parser object
descr  = 'Opening a file and reading data'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('file', default='', help='input data file name')

# parsing arguments
args = parser.parse_args ()

# parameters
file_input = args.file

# making a pathlib object for input file
path_input = pathlib.Path (file_input)

# check of existence of input file
if not (path_input.exists ()):
    # printing a message
    print (f'ERROR: input file "{file_input}" does not exist!')
    # stopping the script
    sys.exit (0)

# opening file
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # reading data
        data_str = line
        # conversion from string into float
        try:
            # conversion from string into float
            data = float (data_str)
        except:
            # printing a message
            print (f'ERROR: conversion from string into float failed!')
            # stopping this script
            sys.exit (0)
        # printing data
        print (f'{data:15.6f}')

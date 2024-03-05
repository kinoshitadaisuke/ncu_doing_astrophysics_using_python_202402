#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 09:21:11 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
parser = argparse.ArgumentParser (description='Making a histogram')

# adding arguments
parser.add_argument ('-a', '--binmin', type=float, default=0.0, \
                     help='minimum value for histogram (default: 0.0)')
parser.add_argument ('-b', '--binmax', type=float, default=1.0, \
                     help='maximum value for histogram (default: 1.0)')
parser.add_argument ('-w', '--binwidth', type=float, default=0.1, \
                     help='width of bins for histogram (default: 0.1)')
parser.add_argument ('file', default='', help='input data file name')

# parsing arguments
args = parser.parse_args ()

# parameters
file_input     = args.file
bin_min        = args.binmin
bin_max        = args.binmax
bin_width      = args.binwidth

# making a pathlib object for input file
path_input = pathlib.Path (file_input)

# check of existence of input file
if not (path_input.exists ()):
    # printing a message
    print (f'ERROR: input file "{file_input}" does not exist!')
    # stopping the script
    sys.exit (0)

# number of bins for histogram
bin_n     = int ((bin_max - bin_min) / bin_width) + 1

# making an empty list for storing data
list_data = []

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
        # appending data to list
        list_data.append (data)

# making a Numpy array
array_data = numpy.array (list_data)

# initialisation of numpy arrays for histogram
hist_x = numpy.linspace (bin_min, bin_max, bin_n)
hist_y = numpy.zeros (bin_n, dtype='int64')

# construction of a histogram
for i in range (len (array_data)):
    # if data is outside of [bin_min, bin_max], then skip
    if ( (array_data[i] < bin_min) or (array_data[i] > bin_max) ):
        continue
    # counting number of data in each bin
    hist_y[int ( (array_data[i] - bin_min) / bin_width)] += 1

# printing histogram
for i in range (bin_n - 1):
    bin_0 = bin_min + bin_width * i
    bin_1 = bin_min + bin_width * (i+1)
    print (f'{bin_0:6.1f} - {bin_1:6.1f}  {hist_y[i]:6d}')

#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 09:34:35 (CST) daisuke>
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
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
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
file_output    = args.output
resolution_dpi = args.resolution
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

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# check of extension of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing a message
    print (f'ERROR: output file must be either EPS or PDF or PNG or PS file.')
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
bins = numpy.linspace (bin_min, bin_max, bin_n)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# labels
ax.set_xlabel ('$x$')
ax.set_ylabel ('Number of data')

# axis settings
ax.set_xlim (bin_min, bin_max)

# plotting data
ax.hist (array_data, bins=bins, histtype='bar', \
         edgecolor='black', linewidth=0.3, align='mid', \
         label='Gaussian distribution')

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)

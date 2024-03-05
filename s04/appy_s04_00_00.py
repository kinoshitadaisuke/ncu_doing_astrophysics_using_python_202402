#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/27 15:09:52 (CST) daisuke>
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
import matplotlib.pyplot

# constructing a parser object
parser = argparse.ArgumentParser (description='A sample Matplotlib code')

# adding arguments
parser.add_argument ('-o', '--output', default='sample.png', \
                     help='output file name (default: sample.png)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output = args.output

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

# data to be plotted
data_x = numpy.linspace (0.0, +5.0, 10000)
data_y = numpy.sin (data_x**data_x) / (data_x**data_x)

#
# for making a plot using implicit pyplot interface, we call some functions
#

# plotting data using procedural pyplot interface
matplotlib.pyplot.plot (data_x, data_y, label="Sample data")

# adding legend to the plot
matplotlib.pyplot.legend ()

# saving a plot as a file
matplotlib.pyplot.savefig (file_output)

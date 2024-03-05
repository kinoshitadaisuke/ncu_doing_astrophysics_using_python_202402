#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/28 09:13:17 (CST) daisuke>
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
parser = argparse.ArgumentParser (description='A sample Matplotlib code')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output    = args.output
resolution_dpi = args.resolution

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
data_x  = numpy.linspace (-10.0, +10.0, 10**3)
data_l0 = 2.0 * data_x - 30.0
data_l1 = 2.0 * data_x - 20.0
data_l2 = 2.0 * data_x - 10.0
data_l3 = 2.0 * data_x - 0.0
data_l4 = 2.0 * data_x + 10.0
data_l5 = 2.0 * data_x + 20.0
data_l6 = 2.0 * data_x + 30.0

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_l0, color='red',     label='$f(x) = 2x - 30$')
ax.plot (data_x, data_l1, color='green',   label='$f(x) = 2x - 20$')
ax.plot (data_x, data_l2, color='blue',    label='$f(x) = 2x - 10$')
ax.plot (data_x, data_l3, color='cyan',    label='$f(x) = 2x$')
ax.plot (data_x, data_l4, color='magenta', label='$f(x) = 2x + 10$')
ax.plot (data_x, data_l5, color='yellow',  label='$f(x) = 2x + 20$')
ax.plot (data_x, data_l6, color='grey',    label='$f(x) = 2x + 30$')

# setting ranges of x-axis and y-axis
ax.set_xlim (-10.0, +10.0)
ax.set_ylim (-60.0, +100.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (-10.0, +10.0, 11))
ax.set_yticks (numpy.linspace (-60.0, +100.0, 17))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output, dpi=resolution_dpi)

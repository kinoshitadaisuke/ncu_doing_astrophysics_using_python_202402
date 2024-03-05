#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 14:12:27 (CST) daisuke>
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
parser = argparse.ArgumentParser (description='A plot of an ellipse')

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

# an ellipse
theta     = numpy.linspace (0.0, 2.0 * numpy.pi, 10**4)
ellipse_x = 5.0 * numpy.cos (theta)
ellipse_y = 3.0 * numpy.sin (theta)

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# range of plot
ax.set_xlim (-6.0, +6.0)
ax.set_ylim (-6.0, +6.0)

# plotting ellipse
ax.plot (ellipse_x, ellipse_y, linestyle='-', linewidth=3.0, color='black', \
         label='Ellipse')

# plotting a point on the ellipse
x = numpy.deg2rad (45.0)
ax.plot (5.0 * numpy.cos (x), 3.0 * numpy.sin (x), \
         linestyle='None', color='red', marker='o', markersize=15.0, \
         label='Point')

# aspect of plot
ax.set_aspect ('equal')

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

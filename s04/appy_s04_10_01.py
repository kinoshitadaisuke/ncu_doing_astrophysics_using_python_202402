#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 15:56:00 (CST) daisuke>
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
descr  = 'Making a 3D line plot'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.data)')
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

# data to be plotted
theta = numpy.linspace (0.0, 10.0 * numpy.pi, 1000)
x = numpy.cos (theta)
y = numpy.sin (theta)
z = theta * 0.2

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='3d')

# settings for plot
ax.set_xlim (-1.5, +1.5)
ax.set_ylim (-1.5, +1.5)
ax.set_zlim (-0.5, +5.5)
ax.set_box_aspect ( (3.0, 3.0, 6.0) )

# viewing angles of camera
el = 30.0
az = -60.0
ax.view_init (elev=el, azim=az)

# plotting data points
ax.plot (x, y, z, color='blue')

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

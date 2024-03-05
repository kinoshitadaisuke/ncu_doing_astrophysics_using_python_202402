#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 14:24:23 (CST) daisuke>
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
import matplotlib.animation

# constructing a parser object
parser = argparse.ArgumentParser (description='Making an simple animation')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('-a', '--semimajor', type=float, default=1.0, \
                     help='length of semimajor axis (defualt: 1.0)')
parser.add_argument ('-b', '--semiminor', type=float, default=1.0, \
                     help='length of semiminor axis (defualt: 1.0)')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output    = args.output
resolution_dpi = args.resolution
a              = args.semimajor
b              = args.semiminor

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# check of extension of output file
if not (path_output.suffix == '.mp4'):
    # printing a message
    print (f'ERROR: output file must be MP4 file.')
    # stopping the script
    sys.exit (0)

# an ellipse
theta     = numpy.linspace (0.0, 2.0 * numpy.pi, 10**4)
ellipse_x = a * numpy.cos (theta)
ellipse_y = b * numpy.sin (theta)

# number of frames for animation
n_frame = 600

# an empty list for storing frames for animation
list_frame = []

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

for i in range (n_frame):
    # initialisation of object list for plotting
    list_obj = []

    # range of plot
    ax.set_xlim (-1.2 * a, +1.2 * a)
    ax.set_ylim (-1.2 * b, +1.2 * b)

    # plotting ellipse
    ellipse, = ax.plot (ellipse_x, ellipse_y, \
                        linestyle='-', linewidth=3.0, color='black', \
                        label='Ellipse')
    list_obj.append (ellipse)

    # plotting a point
    x = numpy.deg2rad (i / n_frame * 720.0)
    point, = ax.plot (a * numpy.cos (x), b * numpy.sin (x), \
                      linestyle='None', color='red', marker='o', \
                      markersize=15.0, label='Point')
    list_obj.append (point)

    # aspect of plot
    ax.set_aspect ('equal')

    # appending frame
    list_frame.append (list_obj)

# making animation
anim = matplotlib.animation.ArtistAnimation (fig, list_frame, interval=50)

# saving file
anim.save (file_output, dpi=resolution_dpi)

#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 15:47:37 (CST) daisuke>
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
descr  = 'Making a 3D scatter plot'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-m', '--mean', type=float, default=0.0, \
                     help='mean of Gaussian distribution (default: 0.0)')
parser.add_argument ('-s', '--stddev', type=float, default=1.0, \
                     help='standard deviation of Gaussian dist. (default: 1.0)')
parser.add_argument ('-n', '--number', type=int, default=1000, \
                     help='number of random numbers (default: 1000)')
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.data)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# parameters
mean           = args.mean
stddev         = args.stddev
n              = args.number
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
rng = numpy.random.default_rng ()
x   = rng.normal (loc=mean, scale=stddev, size=n)
y   = rng.normal (loc=mean, scale=stddev, size=n)
z   = rng.normal (loc=mean, scale=stddev, size=n)

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='3d')

# settings for plot
ax.set_xlim (mean - 5.0 * stddev, mean + 5.0 * stddev)
ax.set_ylim (mean - 5.0 * stddev, mean + 5.0 * stddev)
ax.set_zlim (mean - 5.0 * stddev, mean + 5.0 * stddev)
ax.set_box_aspect ( (1.0, 1.0, 1.0) )

# viewing angles of camera
el = 45.0
az = 60.0
ax.view_init (elev=el, azim=az)

# plotting data points
ax.scatter (x, y, z, s=1.0, color='blue', alpha=0.1)

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

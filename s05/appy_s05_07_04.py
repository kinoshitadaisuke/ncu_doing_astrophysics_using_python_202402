#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/15 10:28:46 (CST) daisuke>
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
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing a parser object
descr  = 'Plotting a surface'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-a', type=float, default=1.0, \
                     help='a of a*exp[-(x-b)^2]*exp[-(x-c)^2]+d (default: 1)')
parser.add_argument ('-b', type=float, default=1.0, \
                     help='a of a*exp[-(x-b)^2]*exp[-(x-c)^2]+d (default: 1)')
parser.add_argument ('-c', type=float, default=1.0, \
                     help='a of a*exp[-(x-b)^2]*exp[-(x-c)^2]+d (default: 1)')
parser.add_argument ('-d', type=float, default=1.0, \
                     help='a of a*exp[-(x-b)^2]*exp[-(x-c)^2]+d (default: 1)')
parser.add_argument ('-min', type=float, default=0.0, \
                     help='minimum value of x for plotting (default: 0)')
parser.add_argument ('-max', type=float, default=1.0, \
                     help='maximum value of x for plotting (default: 1)')
parser.add_argument ('-n', type=int, default=1000, \
                     help='number of data points to produce (default: 1000)')
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
a              = args.a
b              = args.b
c              = args.c
d              = args.d
range_min      = args.min
range_max      = args.max
n              = args.n
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

# function of a surface
def surface (x, a, b, c, d):
    # curve
    z = a * numpy.exp (-(x[0] - b)**2) * numpy.exp (-(x[1] - c)**2) + d
    # returning y-value
    return z

# data to plot
data_x           = numpy.linspace (range_min, range_max, n)
data_y           = numpy.linspace (range_min, range_max, n)
data_xx, data_yy = numpy.meshgrid (data_x, data_y)
data_zz          = surface ( (data_xx, data_yy), a, b, c, d )

#
# making plot using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection='3d')

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')
ax.set_zlabel ('Z [arbitrary unit]')
ax.set_xlim (range_min, range_max)
ax.set_ylim (range_min, range_max)
ax.set_zlim (None, d * 1.5)

# plotting data
ax.plot_surface (data_xx, data_yy, data_zz)

# making a contour
ax.contour (data_xx, data_yy, data_zz, zdir='z', offset=0.0)

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

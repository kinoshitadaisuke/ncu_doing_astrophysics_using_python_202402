#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/14 09:44:25 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing a parser object
descr  = 'Finding minimum of a function'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-a', type=float, default=1.0, \
                     help='a of a*(x-b)**2+c (default: 1)')
parser.add_argument ('-b', type=float, default=1.0, \
                     help='b of a*(x-b)**2+c (default: 1)')
parser.add_argument ('-c', type=float, default=1.0, \
                     help='c of a*(x-b)**2+c (default: 1)')
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

# function of a curve
def curve (x, a, b, c):
    # curve
    y = a * (x - b)**2 + c
    # returning y-value
    return y

# finding minimum
minimum = scipy.optimize.minimize_scalar (curve, args=(a, b, c), method='brent')

# minimum value
min_x = minimum.x
min_y = minimum.fun

# printing minimum value
print (f'function: {a} * (x - {b})**2 + {c}')
print (f'minimum:  y = {min_y} at x = {min_x}')

# data to plot
data_x = numpy.linspace (range_min, range_max, n)
data_y = curve (data_x, a, b, c)

#
# making plot using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# plotting data
ax.plot (data_x, data_y, \
         linestyle='-', linewidth=3.0, color='blue', \
         label=f'$f(x)={a}(x-{b})^2+{c}$')

# plotting minimum value
ax.plot (min_x, min_y, \
         linestyle='None', marker='o', markersize=5.0, color='red', \
         label='minimum')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

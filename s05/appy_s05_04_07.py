#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/10 15:16:42 (CST) daisuke>
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
import scipy
import scipy.interpolate

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
descr  = 'cubic interpolation'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
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

# function for a curve
def curve (x):
    y = 10.0 * numpy.sin (x / 2.0) * numpy.cos (x / 3.0)**2 \
        * numpy.exp (-x / 10)
    return (y)

# generating data for interpolation
data_x = numpy.linspace (0.0, 10.0, 11)
data_y = curve (data_x)

# making a function for linear interpolation
spline1 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=1)

# making a function for quadratic interpolation
spline2 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=2)

# making a function for cubic interpolation
spline3 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=3)

# making a function for 4th-order spline interpolation
spline4 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=4)

#
# visualisation of result of interpolation using Matplotlib
#

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# plotting data points
ax.plot (data_x, data_y, \
         linestyle='None', marker='o', markersize=8.0, color='blue', \
         zorder=0.2, \
         label='raw data')

# plotting original curve
data_x0 = numpy.linspace (0.0, 10.0, 1001)
data_y0 = curve (data_x0)
ax.plot (data_x0, data_y0, \
         linestyle=':', linewidth=4.0, color='cyan', \
         zorder=0.0, \
         label='original curve')

# plotting result of interpolation
data_xi1 = numpy.linspace (0.0, 10.0, 1001)
data_yi1 = spline1 (data_xi1)
ax.plot (data_xi1, data_yi1, \
         linestyle='--', linewidth=2.0, color='magenta', \
         zorder=0.1, \
         label='linear')

# plotting result of interpolation
data_xi2 = numpy.linspace (0.0, 10.0, 1001)
data_yi2 = spline2 (data_xi2)
ax.plot (data_xi2, data_yi2, \
         linestyle='--', linewidth=3.0, color='yellow', \
         zorder=0.1, \
         label='quadratic')

# plotting result of interpolation
data_xi3 = numpy.linspace (0.0, 10.0, 1001)
data_yi3 = spline3 (data_xi3)
ax.plot (data_xi3, data_yi3, \
         linestyle='-.', linewidth=2.0, color='red', \
         zorder=0.1, \
         label='cubic')

# plotting result of interpolation
data_xi4 = numpy.linspace (0.0, 10.0, 1001)
data_yi4 = spline4 (data_xi4)
ax.plot (data_xi4, data_yi4, \
         linestyle='-', linewidth=1.0, color='green', \
         zorder=0.1, \
         label='4th-order spline')

# labels
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)

#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/15 18:34:52 (CST) daisuke>
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
import scipy.stats

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing a parser object
descr  = 'Least-squares method using SciPy'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-a', type=float, default=1.0, \
                     help='initial value of a for y=a(x-b)^2+c (default: 1)')
parser.add_argument ('-b', type=float, default=1.0, \
                     help='initial value of b for y=a(x-b)^2+c (default: 1)')
parser.add_argument ('-c', type=float, default=1.0, \
                     help='initial value of c for y=a(x-b)^2+c (default: 1)')
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('file', default='', help='input data file name')

# parsing arguments
args = parser.parse_args ()

# input parameters
a              = args.a
b              = args.b
c              = args.c
file_input     = args.file
file_output    = args.output
resolution_dpi = args.resolution

# making a pathlib object for input file
path_input = pathlib.Path (file_input)

# check of existence input file
if not (path_input.exists ()):
    # printing a message
    print (f'ERROR: input file "{file_input}" does not exist')
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

# making empty numpy arrays
data_x = numpy.array ([])
data_y = numpy.array ([])

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # splitting line into "x" and "y"
        (x_str, y_str) = line.split ()
        # converting string into float
        try:
            x = float (x_str)
        except:
            print (f'cannot convert "{x_str}" into float.')
            print (f'something is wrong.')
            print (f'exiting...')
            sys.exit (1)
        try:
            y = float (y_str)
        except:
            print (f'cannot convert "{y_str}" into float.')
            print (f'something is wrong.')
            print (f'exiting...')
            sys.exit (1)
        # appending data into numpy arrays
        data_x = numpy.append (data_x, x)
        data_y = numpy.append (data_y, y)

# printing data
for i in range (len (data_x)):
    print (f'(x_{i:02d}, y_{i:02d}) = ({data_x[i]:8.3f}, {data_y[i]:8.3f})')

# a function for curve
def curve (x, a, b, c):
    # curve
    y = a * (x - b)**2 + c
    # returning y
    return y

# initial guess of coefficients
param0 = [a, b, c]

# fitting
popt, pcov = scipy.optimize.curve_fit (curve, data_x, data_y, p0=param0)

# result of fitting
print (f'popt:\n{popt}')
print (f'pcov:\n{pcov}')

# fitted a and b
a_fitted, b_fitted, c_fitted = popt

# degree of freedom
dof = len (data_x) - len (popt)
print (f'dof = {dof}')

# reduced chi-squared
residual     = data_y - curve (data_x, a_fitted, b_fitted, c_fitted)
reduced_chi2 = (residual**2).sum () / dof
print (f'reduced chi-squared = {reduced_chi2}')

# fitted a and b
a_err, b_err, c_err = numpy.sqrt ( numpy.diagonal (pcov) )
print (f'a = {a_fitted:8.3f} +/- {a_err:8.3f} ({a_err/a_fitted*100.0:8.3f}%)')
print (f'b = {b_fitted:8.3f} +/- {b_err:8.3f} ({b_err/b_fitted*100.0:8.3f}%)')
print (f'c = {c_fitted:8.3f} +/- {c_err:8.3f} ({c_err/c_fitted*100.0:8.3f}%)')

# range of data
x_min = scipy.stats.tmin (data_x)
x_max = scipy.stats.tmax (data_x)

# fitted curve
fitted_x = numpy.linspace (x_min, x_max, 1000)
fitted_y = curve (fitted_x, a_fitted, b_fitted, c_fitted)

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
         linestyle='None', marker='o', markersize=5.0, color='blue', \
         zorder=0.2, \
         label='synthetic data for least-squares method')
ax.plot (fitted_x, fitted_y, \
         linestyle=':', linewidth=3.0, color='red', \
         zorder=0.1, \
         label='fitted curve by least-squares method')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

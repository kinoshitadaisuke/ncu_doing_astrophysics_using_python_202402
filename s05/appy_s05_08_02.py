#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/15 17:38:40 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

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
                     help='initial value of a for y=ax+b (default: 1)')
parser.add_argument ('-b', type=float, default=1.0, \
                     help='initial value of b for y=ax+b (default: 1)')
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
        # skipping line if line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line into "x" and "y"
        (x_str, y_str) = line.split ()
        # converting string into float
        try:
            x = float (x_str)
        except:
            print (f'ERROR: cannot convert "{x_str}" into float.')
            print (f'ERROR: something is wrong.')
            print (f'ERROR: exiting...')
            sys.exit (1)
        try:
            y = float (y_str)
        except:
            print (f'ERROR: cannot convert "{y_str}" into float.')
            print (f'ERROR: something is wrong.')
            print (f'ERROR: exiting...')
            sys.exit (1)
        # appending data into numpy arrays
        data_x = numpy.append (data_x, x)
        data_y = numpy.append (data_y, y)

# printing data
for i in range (len (data_x)):
    print (f'(x_{i:03d}, y_{i:03d}) = ({data_x[i]:15.6f}, {data_y[i]:15.6f})')

# a function for straight line
def line (x, a, b):
    # line
    y = a * x + b
    # returning y
    return y

# a function to calculate residuals
def residual (param, x, y):
    # calculation of residual
    residue = param[0] * x + param[1] - y
    # returning residual
    return residue

# initial guess of coefficients
param0 = [a, b]

# fitting
fit_lsq = scipy.optimize.least_squares (residual, param0, \
                                        args=(data_x, data_y) )

# printing result of fitting
print (f'{fit_lsq}')

# degree of freedom
dof = len (data_x) - len (fit_lsq.x)
print (f'dof = {dof}')

# reduced chi-squared
reduced_chi2 = (fit_lsq.fun**2).sum () / dof
print (f'reduced chi-squared = {reduced_chi2}')

# Jacobian
J = fit_lsq.jac
print (f'Jacobian:\n{J}')

# transpose matrix of Jacobian
Jt =J.T

# calculation of J^T J
Jt_J = numpy.matmul (Jt, J)

# covariance matrix
pcov = numpy.linalg.inv (Jt_J) * reduced_chi2
print (f'covariance matrix:\n{pcov}')

# fitted a and b
a_fitted, b_fitted = fit_lsq.x
a_err, b_err = numpy.sqrt ( numpy.diagonal (pcov) )
print (f'a = {a_fitted:8.3f} +/- {a_err:8.3f} ({a_err/a_fitted*100.0:8.3f}%)')
print (f'b = {b_fitted:8.3f} +/- {b_err:8.3f} ({b_err/b_fitted*100.0:8.3f}%)')

# range of data
x_min = scipy.stats.tmin (data_x)
x_max = scipy.stats.tmax (data_x)

# fitted line
fitted_x = numpy.linspace (x_min, x_max, 1000)
fitted_y = line (fitted_x, a_fitted, b_fitted)
    
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

# plotting fitted line
ax.plot (fitted_x, fitted_y, \
         linestyle=':', linewidth=3.0, color='red', \
         zorder=0.1, \
         label='fitted line by least-squares method')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

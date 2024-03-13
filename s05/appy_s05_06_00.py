#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/11 16:16:58 (CST) daisuke>
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
import scipy.integrate

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# constructing a parser object
descr  = 'solving a differential equation'
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

# coefficient
k = 0.1

# initial condition
y_0 = 100.0

# equation to solve
def dydx (t, y):
    # dy/dx = -ky
    dy = -k * y
    # returning value
    return dy

# x values
output_x = numpy.linspace (0.0, 50.0, 5001)

# solving differential equation using Runge-Kutta method
solution = scipy.integrate.solve_ivp (dydx, [0.0, 50.0], [y_0], \
                                      method='RK45', dense_output=True, \
                                      t_eval=output_x, \
                                      rtol=10**-6, atol=10**-9)

# x and y
numerical_x = solution.t
numerical_y = solution.y[0]

# printing solution
print (f'{solution}')

# analytical solution
analytical_x = output_x
analytical_y = y_0 * numpy.exp (-k * analytical_x)
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'$dy/dx = -ky$')
ax.set_xlabel (r'$x$')
ax.set_ylabel (r'$y$')

# plotting data
ax.plot (numerical_x, numerical_y, \
         linestyle='--', linewidth=3.0, color='blue', \
         zorder=0.2, \
         label='numerical solution')
ax.plot (analytical_x, analytical_y, \
         linestyle='-', linewidth=5.0, color='red', \
         zorder=0.1, \
         label='analytical solution')

# making legend
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=resolution_dpi)

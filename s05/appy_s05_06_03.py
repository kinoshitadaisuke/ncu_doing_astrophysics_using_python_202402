#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/13 12:02:35 (CST) daisuke>
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
descr  = 'Visualisation of planetary orbit'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-d', '--directory', default='data', \
                     help='directory for storing PNG files (default: data)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('file', default='input.data', \
                     help='input data file name (default: input.data)')

# parsing arguments
args = parser.parse_args ()

# input parameters
file_input     = args.file
dir_output     = args.directory
resolution_dpi = args.resolution

# making a pathlib object for input file
path_input = pathlib.Path (file_input)

# check of existence of output file
if not (path_input.exists ()):
    # printing a message
    print (f'ERROR: input file "{file_input}" does not exist!')
    # stopping the script
    sys.exit (0)

# making a pathlib object for output directory
path_output = pathlib.Path (dir_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output directory "{dir_output}" exists!')
    # stopping the script
    sys.exit (0)

# making a directory for storing PNG files
path_output.mkdir ()

# making empty lists for storing data
list_t = []
list_x = []
list_y = []
    
# opening input data file
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', find some parameters and then skip
        if (line[0] == '#'):
            fields = line.split ()
            if (len (fields) > 6):
                if (fields[1] == 'mass'):
                    Mstar = float (fields[6])
            if (len (fields) > 10):
                if (fields[7] == 'x0'):
                    x0 = float (fields[9])
                if (fields[7] == 'y0'):
                    y0 = float (fields[9])
                if (fields[7] == 'vx0'):
                    vx0 = float (fields[9])
                if (fields[7] == 'vy0'):
                    vy0 = float (fields[9])
            # skipping line
            continue
        # splitting line (time, X-coordinate, Y-coordinate)
        (t_str, x_str, y_str) = line.split ()
        # converting string into float
        t = float (t_str)
        x = float (x_str)
        y = float (y_str)
        # appending data to lists
        list_t.append (t)
        list_x.append (x)
        list_y.append (y)

# creating Numpy arrays
array_t = numpy.array (list_t)
array_x = numpy.array (list_x)
array_y = numpy.array (list_y)

# finding minimum and maximum values of x and y values
x_min = numpy.min (array_x)
x_max = numpy.max (array_x)
y_min = numpy.min (array_y)
y_max = numpy.max (array_y)

# determining range to plot
list_minmax = [abs (x_min), abs (x_max), abs (y_min), abs (y_max)]
coord_max = sorted (list_minmax)[-1] * 1.5

#
# making a plot using Matplotlib
#

# making plots
for i in range ( len (array_t) ):
    # output file name
    file_output = f'{dir_output}/{dir_output}_{i:08d}.png'

    # making objects "fig" and "ax"
    fig    = matplotlib.figure.Figure ()
    canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
    ax     = fig.add_subplot (111)

    # axes
    ax.set_title ('Planetary Motion')
    ax.set_xlabel ('X [au]')
    ax.set_ylabel ('Y [au]')
    ax.set_xlim (coord_max * -1, coord_max)
    ax.set_ylim (coord_max * -1, coord_max)
    ax.set_aspect ('equal')

    # plotting a star
    ax.plot (0.0, 0.0, \
             linestyle='None', marker='o', markersize=10, color='orange', \
             label='star')

    # plotting a planet
    ax.plot (array_x[i], array_y[i], \
             linestyle='None', marker='o', markersize=5, color='blue', \
             label='planet')

    # labels
    text_time = f"Time: %8.2f year" % (array_t[i])
    text_init = f"Initial conditions"
    text_mass = f"mass of star = {Mstar:5.2f} solar mass"
    text_iq   = f"(qx0, qy0) = ({x0:+5.2f} au, {y0:+5.2f} au)"
    text_iv   = f"(vx0, vy0) = ({vx0:+5.2f} x2pi au/yr, {vy0:+5.2f} x2pi au/yr)"
    ax.text (0.03, 0.95, text_time, transform=ax.transAxes)
    ax.text (0.03, 0.18, text_init, transform=ax.transAxes)
    ax.text (0.05, 0.13, text_mass, transform=ax.transAxes)
    ax.text (0.05, 0.08, text_iq, transform=ax.transAxes)
    ax.text (0.05, 0.03, text_iv, transform=ax.transAxes)

    # showing grid
    ax.grid ()

    # making legend
    ax.legend ()

    # saving the figure to a file
    fig.savefig (file_output, dpi=resolution_dpi)

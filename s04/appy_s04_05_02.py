#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/09/30 20:44:46 (CST) daisuke>
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
parser = argparse.ArgumentParser (description='Plot of logarithmic scale')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
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

# check of extension of output file
if not ( (path_output.suffix == '.eps') \
         or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') \
         or (path_output.suffix == '.ps') ):
    # printing a message
    print (f'ERROR: output file must be either EPS or PDF or PNG or PS file.')
    # stopping the script
    sys.exit (0)

# semimajor axis and orbital period of planets
dic_planets = {
    'Mercury': {'a':  0.3871, 'P':    88.0, 'marker': 's', 'colour': 'b'},
    'Venus':   {'a':  0.7233, 'P':   224.7, 'marker': '^', 'colour': 'y'}, 
    'Earth':   {'a':  1.0000, 'P':   365.2, 'marker': 'o', 'colour': 'g'},
    'Mars':    {'a':  1.5237, 'P':   687.0, 'marker': 'v', 'colour': 'r'},
    'Jupiter': {'a':  5.2034, 'P':  4331.0, 'marker': 's', 'colour': 'm'},
    'Saturn':  {'a':  9.5371, 'P': 10747.0, 'marker': '^', 'colour': 'g'},
    'Uranus':  {'a': 19.1913, 'P': 30589.0, 'marker': 'o', 'colour': 'c'},
    'Neptune': {'a': 30.0690, 'P': 59800.0, 'marker': 'v', 'colour': 'b'},
}

# line to be plotted
line_x = numpy.linspace (0.1, 100.0, 10**3)
line_y = 365.256363004 * line_x**1.5

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (line_x, line_y, linestyle='--', linewidth=3, color='coral')
for planet in dic_planets.keys ():
    ax.plot (dic_planets[planet]['a'], dic_planets[planet]['P'], \
             linestyle='None', \
             marker=dic_planets[planet]['marker'], markersize=10, \
             color=dic_planets[planet]['colour'], label=planet)

# setting log-scale
ax.set_xscale ('log')
ax.set_yscale ('log')

# setting labels for x-axis and y-axis
ax.set_xlabel ('Semimajor Axis [au]')
ax.set_ylabel ('Orbital Period [day]')

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output, dpi=resolution_dpi)

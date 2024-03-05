#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/01 13:36:57 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing gzip module
import gzip

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure
import matplotlib.dates

# constructing a parser object
parser = argparse.ArgumentParser (description='Making HR diagram')

# adding arguments
parser.add_argument ('-o', '--output', default='output.png', \
                     help='output file name (default: output.png)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution of plot in DPI (default: 225.0)')
parser.add_argument ('-m', '--mag', type=float, default=6.0, \
                     help='magnitude limit (default: 6.0)')
parser.add_argument ('file', default='', help='catalogue data file name')

# parsing arguments
args = parser.parse_args ()

# parameters
file_output    = args.output
resolution_dpi = args.resolution
mag_limit      = args.mag
file_catalogue = args.file

# making a pathlib object for catalogue file
path_catalogue = pathlib.Path (file_catalogue)

# check of existence of catalogue file
if not (path_catalogue.exists ()):
    # printing a message
    print (f'ERROR: catalogue file "{file_catalogue}" does not exist!')
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

# dictionary for storing data
stars = {}

# making empty numpy arrays for plotting
array_colour = numpy.array ([])
array_absmag = numpy.array ([])

# opening catalogue file
with gzip.open (file_catalogue, 'rb') as fh:
    # reading catalogue line-by-line
    for line in fh:
        # Harvard Revised Number of star
        HR = line[0:4].strip ()
        # name
        name = line[4:14].strip ()
        # Vmag
        mag_V = line[102:107].strip ()
        # B-V colour
        colour_BV = line[109:114].strip ()
        # spectral type
        sptype = line[127:147].strip ()
        # dynamical parallax flag
        dynamical_parallax = line[160]
        # parallax
        parallax = line[161:166]

        # skip, if any of mag_V, colour_BV, parallax is missing
        if ( (mag_V == '') or (colour_BV == '') or (parallax == '') ):
            continue
        # skip, if parallax is dynamical parallax
        if (dynamical_parallax == 'D'):
            continue
        # reformat parallax
        if (parallax[:2] == '+.'):
            parallax = '+0.' + parallax[2:]

        # conversion from string to float
        try:
            mag_V     = float (mag_V)
        except:
            continue
        try:
            colour_BV = float (colour_BV)
        except:
            continue
        try:
            parallax  = float (parallax)
        except:
            continue

        # skip, if parallax is negative
        if (parallax < 0.0):
            continue

        # skip, if parallax is zero
        if (parallax < 10**-4):
            continue
    
        # distance in parsec
        dist_pc = 1.0 / parallax

        # absolute magnitude
        absmag_V = mag_V - 5.0 * numpy.log10 (dist_pc) + 5.0

        # constructing the dictionary
        stars[HR] = {}
        stars[HR]["mag_V"]     = mag_V
        stars[HR]["colour_BV"] = colour_BV
        stars[HR]["parallax"]  = parallax
        stars[HR]["dist_pc"]   = dist_pc
        stars[HR]["absmag_V"]  = absmag_V
        stars[HR]["sptype"]    = sptype
        stars[HR]["name"]      = name

# printing header
print ("# Vmag, (B-V), parallax, distance, absmag_V, HR number, name")

# printing information of stars
for key, value in sorted (stars.items (), key=lambda x: x[1]['mag_V']):
    # skip if star's magnitude is fainter than magnitude limit
    if (stars[key]['mag_V'] > mag_limit):
        continue
    # printing information of a star
    print (f'{stars[key]["mag_V"]:+6.3f} ', \
           f'{stars[key]["colour_BV"]:+6.3f} ', \
           f'{stars[key]["parallax"]:+6.3f} ', \
           f'{stars[key]["dist_pc"]:+9.3f} ', \
           f'{stars[key]["absmag_V"]:+6.3f} ', \
           f'{int (key.decode ("utf-8")):4d} ', \
           f'{stars[key]["name"].decode ("utf-8")}')
    # appending data into numpy arrays
    array_colour = numpy.append (array_colour, stars[key]['colour_BV'])
    array_absmag = numpy.append (array_absmag, stars[key]['absmag_V'])

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# labels
ax.set_xlabel ('$(B-V)$ Colour Index')
ax.set_ylabel ('Absolute Magnitude')

# flipping direction of Y-axis
ax.invert_yaxis ()

# plotting data
ax.plot (array_colour, array_absmag, \
         linestyle='None', marker='o', color='red', \
         label='Nearby bright stars from BSC5')

# grid
ax.grid ()

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=resolution_dpi)

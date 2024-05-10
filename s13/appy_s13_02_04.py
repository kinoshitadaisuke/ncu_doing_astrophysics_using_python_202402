#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/10 13:30:36 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing astropy module
import astropy.table
import astropy.visualization

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing parser object
descr  = 'reading source catalogue file and showing locations of sources'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-c', '--catalogue-file', default='', \
                     help='input catalogue file name')
parser.add_argument ('-i', '--input-file', default='', \
                     help='input FITS file name')
parser.add_argument ('-o', '--output-file', default='', \
                     help='output file name')
parser.add_argument ('-r', '--radius', type=float, default=10.0, \
                     help='radius of aperture in pixel (default: 10)')
parser.add_argument ('-d', '--resolution', type=float, default=150.0, \
                     help='resolution of output image in DPI (default: 150)')

# command-line argument analysis
args = parser.parse_args ()

# catalogue file name
file_catalogue = args.catalogue_file
file_input     = args.input_file
file_output    = args.output_file
radius         = args.radius
resolution     = args.resolution

# making pathlib objects
path_input     = pathlib.Path (file_input)
path_catalogue = pathlib.Path (file_catalogue)
path_output    = pathlib.Path (file_output)

# check of input file name
if not (path_input.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file must be a FITS file.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# check of catalogue file name
if (file_catalogue == ''):
    # printing message
    print (f'ERROR:')
    print (f'Catalogue file name must be specified.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# check of output file name
if not ( (path_output.suffix == '.eps') or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') or (path_output.suffix == '.ps')):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file must be either EPS, PDF, PNG, or PS.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# existence check of input file
if not (path_input.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file "{file_input}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# existence check of catalogue file
if not (path_catalogue.exists () ):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Catalogue file "{file_catalogue}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file "{file_output}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# reading catalogue from a file
table_source = astropy.table.Table.read (file_catalogue, \
                                         format='ascii.commented_header')

# positions of detected sources
list_x = list (table_source['xcentroid'])
list_y = list (table_source['ycentroid'])

# opening FITS file
with astropy.io.fits.open (file_input) as hdu:
    # reading header and image
    header = hdu[0].header
    image  = hdu[0].data
    # if no image in PrimaryHDU, then read next HDU
    if (header['NAXIS'] == 0):
        header = hdu[1].header
        image  = hdu[1].data


# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('X [pixel]')
ax.set_ylabel ('Y [pixel]')

# normalisation
norm \
    = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (image) )

# plotting image
im = ax.imshow (image, origin='lower', cmap='viridis', norm=norm)

# plotting marks
for i in range ( len (list_x) ):
    # making a circle to indicate location of detected source
    source = matplotlib.patches.Circle (xy=(list_x[i], list_y[i]), \
                                        radius=radius, \
                                        fill=False, color="red", \
                                        linewidth=1)
    # plotting location of detected source
    ax.add_patch (source)

# saving file
fig.savefig (file_output, dpi=resolution)

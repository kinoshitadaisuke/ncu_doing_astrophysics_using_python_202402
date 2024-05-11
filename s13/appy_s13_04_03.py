#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/11 19:34:15 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# import sys module
import sys

# importing astropy module
import astropy.io.fits
import astropy.wcs
import astropy.visualization

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing parser object
descr  = 'reading two FITS files and visualising them'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', '--file-output', default='', \
                     help='output file name')
parser.add_argument ('-t', '--title1', \
                     help='title of first image')
parser.add_argument ('-u', '--title2', \
                     help='title of second image')
parser.add_argument ('-c', '--cmap', default='gray', \
                     help='colour map (default: gray)')
parser.add_argument ('-r', '--resolution', type=float, default=150.0, \
                     help='resolution of output image in DPI (default: 150)')
parser.add_argument ('-w', '--wcs', action='store_true', default=False, \
                     help='use WCS (default: False)')
parser.add_argument ('file1', default='', nargs=1, \
                     help='FITS file #1')
parser.add_argument ('file2', default='', nargs=1, \
                     help='FITS file #2')

# command-line argument analysis
args = parser.parse_args ()

# parameters
file_output    = args.file_output
file_fits1     = args.file1[0]
file_fits2     = args.file2[0]
title1         = args.title1
title2         = args.title2
colourmap      = args.cmap
resolution_dpi = args.resolution
use_wcs        = args.wcs

# making pathlib objects
path_fits1 = pathlib.Path (file_fits1)
path_fits2 = pathlib.Path (file_fits2)

# check of extension of input file 1
if not (path_fits1.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file "{file_fits1}" is not a FITS file!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# check of extension of input file 2
if not (path_fits2.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file "{file_fits2}" is not a FITS file!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# existence check of input file 1
if not (path_fits1.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file "{file_fits1}" does not exist!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)
    
# existence check of input file 2
if not (path_fits2.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file "{file_fits2}" does not exist!')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)
    

# function to read a FITS file
def read_fits (file_fits):
    # opening FITS file
    with astropy.io.fits.open (file_fits) as hdu_list:
        # reading FITS header, WCS information, and image data
        header = hdu_list[0].header
        wcs    = astropy.wcs.WCS (header)
        image  = hdu_list[0].data
    # returning header, wcs, and image
    return (header, wcs, image)

# reading first FITS file
(header1, wcs1, image1) = read_fits (file_fits1)

# reading second FITS file
(header2, wcs2, image2) = read_fits (file_fits2)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
if (use_wcs):
    ax1 = fig.add_subplot (121, projection=wcs)
    ax2 = fig.add_subplot (122, projection=wcs)
else:
    ax1 = fig.add_subplot (121)
    ax2 = fig.add_subplot (122)

# axes
ax1.set_title (title1)
ax2.set_title (title2)
if (use_wcs):
    ax1.set_xlabel ('Right Ascension')
    ax1.set_ylabel ('Declination')
    ax2.set_xlabel ('Right Ascension')
    ax2.set_ylabel ('Declination')
else:
    ax1.set_xlabel ('X [pixel]')
    ax1.set_ylabel ('Y [pixel]')
    ax2.set_xlabel ('X [pixel]')
    ax2.set_ylabel ('Y [pixel]')

# plotting images
norm1 = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (image1) )
im1 = ax1.imshow (image1, origin='lower', cmap=colourmap, norm=norm1)
norm2 = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (image2) )
im2 = ax2.imshow (image2, origin='lower', cmap=colourmap, norm=norm2)

# saving file
fig.tight_layout ()
fig.savefig (file_output, dpi=resolution_dpi)

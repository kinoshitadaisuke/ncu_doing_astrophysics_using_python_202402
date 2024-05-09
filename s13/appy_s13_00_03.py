#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 09:41:14 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.io.fits
import astropy.wcs
import astropy.visualization

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# construction pf parser object
descr  = 'Making a PNG file from a FITS file'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', \
                     help='input FITS file')
parser.add_argument ('-o', '--output', \
                     help='output PNG file')
parser.add_argument ('-t', '--title', \
                     help='title of output image')
parser.add_argument ('-c', '--cmap', default='gray', \
                     help='colour map (default: gray)')
parser.add_argument ('-r', '--resolution', type=float, default=150.0, \
                     help='resolution of output image in DPI (default: 150)')
parser.add_argument ('-w', '--wcs', action='store_true', default=False, \
                     help='use WCS (default: False)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_input     = args.input
file_output    = args.output
title          = args.title
colourmap      = args.cmap
resolution_dpi = args.resolution
use_wcs        = args.wcs

# opening FITS file
with astropy.io.fits.open (file_input) as hdu_list:
    # printing HDU information
    print (f'{hdu_list.info ()}')
    
    # reading FITS header, WCS information, and image data
    header = hdu_list[0].header
    wcs    = astropy.wcs.WCS (header)
    image  = hdu_list[0].data

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
if (use_wcs):
    ax = fig.add_subplot (111, projection=wcs)
else:
    ax = fig.add_subplot (111)

# axes
ax.set_title (title)
if (use_wcs):
    ax.set_xlabel ('Right Ascension')
    ax.set_ylabel ('Declination')
else:
    ax.set_xlabel ('X [pixel]')
    ax.set_ylabel ('Y [pixel]')

# plotting image
norm = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (image) )
im = ax.imshow (image, origin='lower', cmap=colourmap, norm=norm)
fig.colorbar (im)

# printing a message
print (f'{file_input} ==> {file_output}')

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

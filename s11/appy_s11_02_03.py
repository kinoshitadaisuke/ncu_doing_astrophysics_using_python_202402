#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/11/22 15:27:03 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# cmap
list_cmap = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'gray', \
    'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', \
    'cool', 'hot', 'copper', 'hsv', 'ocean', 'terrain', 'gnuplot', \
    'rainbow', 'turbo'
]

# construction of parser object for argparse
descr  = 'conversion from FITS to PNG'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='name of input file')
parser.add_argument ('-o', '--output', help='name of output file')
parser.add_argument ('-n', '--name', help='name of the object')
parser.add_argument ('-c', '--cmap', choices=list_cmap, default='gray', \
                     help='choice of cmap (default: gray)')
parser.add_argument ('-r', '--resolution', type=float, default=225.0, \
                     help='resolution in DPI (default: 225)')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
name           = args.name
cmap           = args.cmap
resolution_dpi = args.resolution
file_input     = args.input
file_output    = args.output

# reading FITS file
with astropy.io.fits.open (file_input) as hdu:
    # reading header
    header = hdu[0].header
    # WCS information
    wcs = astropy.wcs.WCS (header)
    # reading image
    image  = hdu[0].data

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection=wcs)

# axes
ax.set_title (name)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting image
norm = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.AsinhStretch () )
im = ax.imshow (image, origin='lower', cmap=cmap, norm=norm)
fig.colorbar (im)

# saving file
fig.savefig (file_output, dpi=resolution_dpi)

#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/11 20:06:36 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing astropy module
import astropy.table
import astropy.visualization

# importing scikit-image module
import skimage.transform

# importing astroalign module
import astroalign

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# date/time
now = datetime.datetime.now ()

# constructing parser object
descr  = 'aligning image'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-o', '--file-output', default='', \
                     help='output figure file')
parser.add_argument ('-r', '--resolution', type=float, default=150.0, \
                     help='resolution of output image in DPI (default: 150)')
parser.add_argument ('catalogue1', nargs=1, help='catalogue file 1')
parser.add_argument ('catalogue2', nargs=1, help='catalogue file 2')
parser.add_argument ('fits1', nargs=1, help='FITS file 1')
parser.add_argument ('fits2', nargs=1, help='FITS file 2')

# command-line argument analysis
args = parser.parse_args ()

# file names
file_cat1  = args.catalogue1[0]
file_cat2  = args.catalogue2[0]
file_fits1 = args.fits1[0]
file_fits2 = args.fits2[0]
file_fig   = args.file_output
resolution = args.resolution

# making pathlib objects
path_cat1  = pathlib.Path (file_cat1)
path_cat2  = pathlib.Path (file_cat2)
path_fits1 = pathlib.Path (file_fits1)
path_fits2 = pathlib.Path (file_fits2)
path_fig   = pathlib.Path (file_fig)

# check of output file name
if not ( (path_fig.suffix == '.eps') or (path_fig.suffix == '.pdf') \
         or (path_fig.suffix == '.png') or (path_fig.suffix == '.ps') ):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Figure file name must be either EPS, PDF, PNG, or PS.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# check of catalogue file name
if not ( (path_cat1.suffix == '.cat') and (path_cat2.suffix == '.cat') ):
    # printing message
    print (f'ERROR: Input file must be a catalogue file (*.cat).')
    print (f'ERROR: catalogue file 1 = "{file_cat1}"')
    print (f'ERROR: catalogue file 2 = "{file_cat2}"')
    # exit
    sys.exit ()

# check of FITS file name
if not ( (path_fits1.suffix == '.fits') and (path_fits2.suffix == '.fits') ):
    # printing message
    print (f'ERROR: Input file must be a FITS file (*.fits).')
    print (f'ERROR: FITS file 1 = "{file_fits1}"')
    print (f'ERROR: FITS file 2 = "{file_fits2}"')
    # exit
    sys.exit ()

# existence checks
if not (path_cat1.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_cat1}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()
if not (path_cat2.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_cat2}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()
if not (path_fits1.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_fits1}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()
if not (path_fits2.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_fits2}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()
if (path_fig.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_fig}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# function to read a FITS file
def read_fits (file_fits):
    # reading FITS file
    with astropy.io.fits.open (file_fits) as hdu:
        # reading header and image
        header = hdu[0].header
        image  = hdu[0].data
        # if no image in PrimaryHDU, then read next HDU
        if (header['NAXIS'] == 0):
            header = hdu[1].header
            image  = hdu[1].data
    # returning header and image
    return (header, image)

# reading catalogue from a file
table_source1 = astropy.table.Table.read (file_cat1, \
                                          format='ascii.commented_header')
table_source2 = astropy.table.Table.read (file_cat2, \
                                          format='ascii.commented_header')

# (x, y) coordinates of sources
list_source1_x = list (table_source1['xcentroid'])
list_source1_y = list (table_source1['ycentroid'])
list_source2_x = list (table_source2['xcentroid'])
list_source2_y = list (table_source2['ycentroid'])
position_1     = numpy.transpose ( (list_source1_x, list_source1_y) )
position_2     = numpy.transpose ( (list_source2_x, list_source2_y) )

# finding star-to-star matching
transf, (list_matched_2, list_matched_1) \
    = astroalign.find_transform (position_2, position_1)

# transformation
list_matched_2_aligned \
    = astroalign.matrix_transform (list_matched_2, transf.params)

# printing results
print (f'#')
print (f'# result of image alignment')
print (f'#')
print (f'#   date/time = {now}')
print (f'#')
print (f'# input files')
print (f'#')
print (f'#   catalogue file 1 = {file_cat1}')
print (f'#   catalogue file 2 = {file_cat2}')
print (f'#')
print (f'# transformation matrix')
print (f'#')
print (f'# [')
print (f'#  [{transf.params[0][0]:11.6f}, {transf.params[0][1]:11.6f}, {transf.params[0][2]:11.6f}],')
print (f'#  [{transf.params[1][0]:11.6f}, {transf.params[1][1]:11.6f}, {transf.params[1][2]:11.6f}],')
print (f'#  [{transf.params[2][0]:11.6f}, {transf.params[2][1]:11.6f}, {transf.params[2][2]:11.6f}]')
print (f'# ]')
print (f'#')
print (f'#')
print (f'# list of matched stars')
print (f'#')
for i in range ( len (list_matched_1) ):
    print (f'({list_matched_1[i][0]:8.3f}, {list_matched_1[i][1]:8.3f})', \
           f'on 1st image', \
           f'==> ({list_matched_2[i][0]:8.3f}, {list_matched_2[i][1]:8.3f})', \
           f'on 2nd image')

# reading FITS files
(header1, image1) = read_fits (file_fits1)
(header2, image2) = read_fits (file_fits2)

# byte swap
# data stored in FITS file is network byte-order (big endian).
# Intel/AMD CPUs use little endian.
image1 = image1.byteswap ().newbyteorder ()
image2 = image2.byteswap ().newbyteorder ()

# aligning 2nd image to 1st image
st = skimage.transform.SimilarityTransform (scale=transf.scale, \
                                            rotation=transf.rotation, \
                                            translation=transf.translation)
image2_aligned = skimage.transform.warp (image2, st.inverse)

# marker and colour names for matplotlib
markers = ['o', 'v', '^', 's', 'p', 'h', '8']
colours = ['maroon', 'red', 'coral', 'bisque', 'orange', \
           'wheat', 'yellow', 'green', 'lime', 'aqua', \
           'skyblue', 'blue', 'indigo', 'violet', 'pink']

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax1    = fig.add_subplot (121)
ax2    = fig.add_subplot (122)

# plotting first image
norm1 \
    = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (image1) )
im1 = ax1.imshow (image1, origin='lower', cmap='bone', norm=norm1)
for i in range ( len (list_matched_1) ):
    i_marker = i % len (markers)
    i_colour = i % len (colours)
    ax1.plot (list_matched_1[i][0], list_matched_1[i][1], \
              marker=markers[i_marker], color=colours[i_colour], \
              markersize=8, fillstyle='none')
ax1.set_title ('First Image')

# plotting second image
norm2 \
    = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (image2_aligned) )
im2 = ax2.imshow (image2_aligned, origin='lower', cmap='bone', norm=norm2)
for i in range ( len (list_matched_2_aligned) ):
    i_marker = i % len (markers)
    i_colour = i % len (colours)
    ax2.plot (list_matched_2_aligned[i][0], list_matched_2_aligned[i][1], \
              marker=markers[i_marker], color=colours[i_colour], \
              markersize=8, fillstyle='none')
ax2.set_title ('Second Image')

# writing to a file
fig.tight_layout ()
fig.savefig (file_fig, dpi=resolution)

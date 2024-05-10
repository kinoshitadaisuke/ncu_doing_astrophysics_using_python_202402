#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/10 12:32:16 (UT+8) daisuke>
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
import numpy.ma

# importing astropy module
import astropy.io.fits
import astropy.stats

# importing photutils module
import photutils.segmentation

# date/time
now = datetime.datetime.now ()

# constructing parser object
descr  = 'Estimating 1D sky background value for astronomical image'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input-file', default='', \
                     help='input file name')
parser.add_argument ('-s', '--sigma', type=float, default=3.0, \
                     help='threshold for sky estimate (default: 3 [sigma])')
parser.add_argument ('-t', '--threshold', type=float, default=2.0, \
                     help='threshold for source detection (default: 2 [sigma])')
parser.add_argument ('-n', '--npixels', type=int, default=5, \
                     help='minimum number of pixels for detection (default: 5)')
parser.add_argument ('-d', '--dilate-size', type=int, default=21, \
                     help='dilate footprint size (default: 21)')
parser.add_argument ('-m', '--maxiters', type=int, default=10, \
                     help='maximum number of iterations (default: 10)')

# command-line argument analysis
args = parser.parse_args ()

# file names
file_input  = args.input_file

# input parameters
sigma_sky   = args.sigma
sigma_det   = args.threshold
npixels     = args.npixels
dilate_size = args.dilate_size
maxiters    = args.maxiters

# making pathlib objects
path_input  = pathlib.Path (file_input)

# check of output file name
if not (path_input.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file must be a FITS file.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# existence check of output file
if not (path_input.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file "{file_input}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# opening FITS file
with astropy.io.fits.open (file_input) as hdu:
    # reading header and image
    header = hdu[0].header
    image  = hdu[0].data
    # if no image in PrimaryHDU, then read next HDU
    if (header['NAXIS'] == 0):
        header = hdu[1].header
        image  = hdu[1].data

# sigma-clipping algorithm for removing stars
sigma_clip = astropy.stats.SigmaClip (sigma=sigma_sky, maxiters=maxiters)

# finding threshold value for detecting local peaks
threshold_adu = photutils.segmentation.detect_threshold (image, \
                                                         nsigma=sigma_det, \
                                                         sigma_clip=sigma_clip)

# making segmentation image
image_segmentation = photutils.segmentation.detect_sources (image, \
                                                            threshold_adu, \
                                                            npixels=npixels)

# size of dilation footprint
footprint = photutils.utils.circular_footprint (radius=dilate_size)

# making source mask
source_mask = image_segmentation.make_source_mask (footprint=footprint)
        
# making masked array
image_masked = numpy.ma.array (image, mask=source_mask)

# finding mean, median, and standard deviation of masked image
mean, median, stddev = astropy.stats.sigma_clipped_stats (image_masked, \
                                                          sigma=sigma_sky, \
                                                          mask=source_mask)

# printing results
print (f'Input image: "{file_input}"')
print (f'Results of sky background level estimate:')
print (f'  mean                      = {mean:9.3f} ADU')
print (f'  median                    = {median:9.3f} ADU')
print (f'  3.0 x median - 2.0 x mean = {3.0 * median - 2.0 * mean:9.3f} ADU')
print (f'  2.5 x median - 1.5 x mean = {2.5 * median - 1.5 * mean:9.3f} ADU')

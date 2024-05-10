#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/10 13:13:23 (UT+8) daisuke>
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
import astropy.convolution

# importing photutils module
import photutils.background
import photutils.segmentation

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constructing parser object
descr  = 'Source extraction and de-blending using image segmentation'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input-file', default='', \
                     help='input file name')
parser.add_argument ('-o', '--output-file', default='', \
                     help='output file name')
parser.add_argument ('-s', '--sigma', type=float, default=3.0, \
                     help='threshold for sky estimate (default: 3 [sigma])')
parser.add_argument ('-m', '--maxiters', type=int, default=10, \
                     help='maximum number of iterations (default: 10)')
parser.add_argument ('-b', '--box-size', type=int, default=50, \
                     help='box size for sky background estimate (default: 50)')
parser.add_argument ('-f', '--filter-size', type=int, default=3, \
                     help='filter size (default: 3)')
parser.add_argument ('-t', '--threshold', type=float, default=2.0, \
                     help='threshold for source detection (default: 2 [RMS])')
parser.add_argument ('-k', '--kernel', type=float, default=3.0, \
                     help='FWHM of Gaussian convolution kernel (default: 3)')
parser.add_argument ('-a', '--kernel-array-size', type=int, default=5, \
                     help='Gaussian kernel array size (default: 5)')
parser.add_argument ('-n', '--npixels', type=int, default=10, \
                     help='number of connected pixels (default: 10)')
parser.add_argument ('-l', '--level', type=int, default=32, \
                     help='multi-thresholding levels (default: 32)')
parser.add_argument ('-c', '--contrast', type=float, default=0.001, \
                     help='minimum ratio of secondary peak (default=0.001)')
parser.add_argument ('-r', '--resolution', type=float, default=150.0, \
                     help='resolution of output image in DPI (default: 150)')

# command-line argument analysis
args = parser.parse_args ()

# file names
file_input  = args.input_file
file_output = args.output_file

# input parameters
sigma_sky     = args.sigma
maxiters      = args.maxiters
box_size      = args.box_size
filter_size   = args.filter_size
threshold_rms = args.threshold
fwhm_kernel   = args.kernel
array_size    = args.kernel_array_size
npixels       = args.npixels
nlevels       = args.level
contrast      = args.contrast
resolution    = args.resolution

# making pathlib objects
path_input  = pathlib.Path (file_input)
path_output = pathlib.Path (file_output)

# check of input file name
if not (path_input.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file must be a FITS file.')
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

# check of output file name
if not ( (path_output.suffix == '.eps') or (path_output.suffix == '.pdf') \
         or (path_output.suffix == '.png') or (path_output.suffix == '.ps') ):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file must be either EPS or PDF or PNG or PS file.')
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

# sky background estimator
skybg_estimator = photutils.background.SExtractorBackground ()

# making 2-D sky background map for a given image
image_skybg = photutils.background.Background2D \
    (image, box_size=(box_size, box_size), \
     filter_size=(filter_size, filter_size), \
     sigma_clip=sigma_clip, bkg_estimator=skybg_estimator)

# sky background subtraction
image_skysub = image - image_skybg.background

# detection threshold
detection_threshold = threshold_rms * image_skybg.background_rms

# 2-D Gaussian convolution kernel
convolution_kernel = photutils.segmentation.make_2dgaussian_kernel \
    (fwhm=fwhm_kernel, size=array_size)

# convolution
image_convolved = astropy.convolution.convolve (image_skysub, \
                                                convolution_kernel)

# detecting sources
image_segmented = photutils.segmentation.detect_sources \
    (image_convolved, detection_threshold, npixels=npixels)

# de-blending
image_deblended = photutils.segmentation.deblend_sources \
    (image_convolved, image_segmented, npixels=npixels, \
     nlevels=nlevels, contrast=contrast, progress_bar=False)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax1    = fig.add_subplot (121)
ax2    = fig.add_subplot (122)

# normalisation
norm \
    = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.HistEqStretch (image) )

# plotting segmentation image
im1 = ax1.imshow (image_segmented, origin='lower', \
                  cmap=image_segmented.make_cmap (), interpolation='nearest')
ax1.set_title ('Segmentation Image')

# plotting de-blended image
im2 = ax2.imshow (image_deblended, origin='lower', \
                  cmap=image_deblended.make_cmap (), interpolation='nearest')
ax2.set_title ('De-blended Image')

# writing to a file
fig.savefig (file_output, dpi=resolution)

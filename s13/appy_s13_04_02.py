#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/10 13:51:58 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing numpy module
import numpy

# importing astropy module
import astropy.io
import astropy.table

# importing photutils module
import photutils.datasets

# constructing parser object
descr  = 'reading star list file and generating FITS image'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--file-input', default='', \
                     help='input file name')
parser.add_argument ('-o', '--file-output', default='', \
                     help='output file name')
parser.add_argument ('-f', '--fwhm', type=float, default=4.0, \
                     help='FWHM of PSF in pixel (default: 4)')
parser.add_argument ('-g', '--fwhm-stddev', type=float, default=0.1, \
                     help='stddev of FWHM of PSF in pixel (default: 0.1)')
parser.add_argument ('-s', '--sky', type=float, default=1000.0, \
                     help='sky background level in ADU (default: 1000)')
parser.add_argument ('-e', '--sky-stddev', type=float, default=30.0, \
                     help='stddev of sky background in ADU (default: 30)')
parser.add_argument ('-x', '--size-x', type=int, default=2048, \
                     help='image size on x-axis (default: 2048)')
parser.add_argument ('-y', '--size-y', type=int, default=2048, \
                     help='image size on y-axis (default: 2048)')

# command-line argument analysis
args = parser.parse_args ()

# parameters
file_input  = args.file_input
file_output = args.file_output
fwhm        = args.fwhm
fwhm_stddev = args.fwhm_stddev
sky         = args.sky
sky_stddev  = args.sky_stddev
size_x      = args.size_x
size_y      = args.size_y

# image shape
image_shape = (size_x, size_y)

# check of input file name
if (file_input == ''):
    print ("Input file name must be specified.")
    sys.exit ()

# check of output file name
if not (file_output[-5:] == '.fits'):
    print ("Output file name must be a FITS file.")
    sys.exit ()

# making pathlib objects
path_input  = pathlib.Path (file_input)
path_output = pathlib.Path (file_output)
    
# existence check of input file
if not (path_input.exists ()):
    # printing message
    print ("ERROR: Input file '%s' does not exist." % (file_input) )
    # exit
    sys.exit ()

# existence check of output file
if (path_output.exists ()):
    # printing message
    print ("ERROR: Output file '%s' exists." % (file_output) )
    # exit
    sys.exit ()

# generating a new astropy table
table_stars = astropy.table.Table ()

# making empty lists for data
list_x     = []
list_y     = []
list_flux  = []
list_psf_x = []
list_psf_y = []
list_theta = []

# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping line, if line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (x_str, y_str, flux_str) = line.split ()
        # x, y, and flux
        x    = float (x_str)
        y    = float (y_str)
        flux = float (flux_str)
        # random number generation for PSF
        rng       = numpy.random.default_rng ()
        psf_x     = rng.normal (loc=fwhm, scale=fwhm_stddev, size=1)
        psf_y     = rng.normal (loc=fwhm, scale=fwhm_stddev, size=1)
        theta_deg = rng.uniform (0.0, 360.0, 1)
        theta_rad = numpy.deg2rad (theta_deg)
        # adding data to lists
        list_flux.append (flux)
        list_x.append (x)
        list_y.append (y)
        list_psf_x.append (psf_x)
        list_psf_y.append (psf_y)
        list_theta.append (theta_rad)

# adding data to astropy table
table_stars['amplitude'] = list_flux
table_stars['x_mean']    = list_x
table_stars['y_mean']    = list_y
table_stars['x_stddev']  = list_psf_x
table_stars['y_stddev']  = list_psf_y
table_stars['theta']     = list_theta

# generating stars
image_stars = photutils.datasets.make_gaussian_sources_image (image_shape, \
                                                              table_stars)
# generating sky background
image_sky = photutils.datasets.make_noise_image (image_shape, \
                                                 distribution='gaussian', \
                                                 mean=sky, \
                                                 stddev=sky_stddev)
# generating synthetic image
image = image_stars + image_sky

# preparing a FITS header
header = astropy.io.fits.PrimaryHDU ().header

# writing a FITS file
astropy.io.fits.writeto (file_output, image, header=header)

#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 09:55:08 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing numpy module
import numpy
import numpy.random

# importing astropy module
import astropy.io
import astropy.table

# importing photutils module
import photutils.datasets

# constructing parser object
descr  = 'generating a synthetic image with artificial stars and galaxies'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-x', '--size-x', type=int, default=2048, \
                     help='image size in X-axis (default: 2048)')
parser.add_argument ('-y', '--size-y', type=int, default=2048, \
                     help='image size in Y-axis (default: 2048)')
parser.add_argument ('-n', '--nstars', type=int, default=100, \
                     help='number of stars to generate (default: 100)')
parser.add_argument ('-g', '--ngalaxies', type=int, default=10, \
                     help='number of galaxies to generate (default: 10)')
parser.add_argument ('-f', '--flux-min', type=float, default=1000.0, \
                     help='minimum flux of stars (default: 1000)')
parser.add_argument ('-p', '--fwhm-psf', type=float, default=3.5, \
                     help='FWHM of PSF in pixel (default: 3.5)')
parser.add_argument ('-d', '--fwhm-stddev', type=float, default=0.1, \
                     help='stddev of FWHM distribution in pixel (default: 0.1)')
parser.add_argument ('-q', '--fwhm-psf-gal', type=float, default=8.0, \
                     help='FWHM of galaxy PSF in pixel (default: 8)')
parser.add_argument ('-r', '--fwhm-psf-gal-stddev', type=float, default=4.0, \
                     help='stddev of FWHM of galaxy PSF in pixel (default: 4)')
parser.add_argument ('-s', '--sky', type=float, default=1000.0, \
                     help='sky background level in ADU (default: 1000)')
parser.add_argument ('-e', '--sky-stddev', type=float, default=30.0, \
                     help='stddev of sky background in ADU (default: 30)')
parser.add_argument ('-o', '--output-file', default='', \
                     help='output file name')
parser.add_argument ('-l', '--log-file', default='', \
                     help='log file name')

# command-line argument analysis
args = parser.parse_args ()

# image size
image_size_x = args.size_x
image_size_y = args.size_y
image_shape  = (image_size_x, image_size_y)

# number of stars and galaxies to generate
nstars = args.nstars
ngals  = args.ngalaxies

# flux of faintest stars
flux_min = args.flux_min

# FWHM of PSF
fwhm_x            = args.fwhm_psf
fwhm_y            = args.fwhm_psf
fwhm_stddev_x     = args.fwhm_stddev
fwhm_stddev_y     = args.fwhm_stddev
fwhm_gal_x        = args.fwhm_psf_gal
fwhm_gal_y        = args.fwhm_psf_gal
fwhm_gal_stddev_x = args.fwhm_psf_gal_stddev
fwhm_gal_stddev_y = args.fwhm_psf_gal_stddev

# sky background level and stddev
sky_mean   = args.sky
sky_stddev = args.sky_stddev

# output file name and log file name
file_output = args.output_file
file_log    = args.log_file

# making pathlib objects
path_output = pathlib.Path (file_output)
path_log    = pathlib.Path (file_log)

# check of output file name
if not (path_output.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file must be a FITS file.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# check of log file name
if (file_log == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: You need to specify log file name.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# existence check for output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: output file "{file_output}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# existence check for log file
if (path_log.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: log file "{file_log}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit (0)

# printing status
print (f'Now, generating source table for stars and galaxies...')
    
# generating a new astropy table
table_stars = astropy.table.Table ()
table_gals  = astropy.table.Table ()

# random number generator
rng = numpy.random.default_rng ()

# generating random numbers for stars
position_x = rng.uniform (0, image_size_x, nstars)
position_y = rng.uniform (0, image_size_y, nstars)
theta_deg  = rng.uniform (0, 360, nstars)
psf_x      = rng.normal (loc=fwhm_x, scale=fwhm_stddev_x, size=nstars)
psf_y      = rng.normal (loc=fwhm_y, scale=fwhm_stddev_y, size=nstars)
powerlaw   = rng.power (1.5, size=nstars)
flux       = flux_min / powerlaw

# generating random numbers for galaxies
centre_gal_x   = rng.uniform (image_size_x * 0.3, image_size_x * 0.7)
centre_gal_y   = rng.uniform (image_size_y * 0.3, image_size_y * 0.7)
position_gal_x = rng.normal (loc=centre_gal_x, scale=300, size=ngals)
position_gal_y = rng.normal (loc=centre_gal_y, scale=300, size=ngals)
theta_gal_deg  = rng.uniform (0, 360, ngals)
psf_gal_x      = rng.normal (loc=fwhm_gal_x, scale=fwhm_gal_stddev_x, \
                             size=ngals)
psf_gal_y      = rng.normal (loc=fwhm_gal_y, scale=fwhm_gal_stddev_y, \
                             size=ngals)
powerlaw_gal   = rng.power (2.0, size=ngals)
flux_gal       = flux_min * 3 / powerlaw_gal

# conversion from degree to radian
theta_rad     = numpy.radians (theta_deg)
theta_gal_rad = numpy.radians (theta_gal_deg)

# adding data to the table of stars
table_stars['amplitude'] = flux
table_stars['x_mean']    = position_x
table_stars['y_mean']    = position_y
table_stars['x_stddev']  = psf_x
table_stars['y_stddev']  = psf_y
table_stars['theta']     = theta_rad

# adding data to the table of galaxies
table_gals['amplitude'] = flux_gal
table_gals['x_mean']    = position_gal_x
table_gals['y_mean']    = position_gal_y
table_gals['x_stddev']  = psf_gal_x
table_gals['y_stddev']  = psf_gal_y
table_gals['theta']     = theta_gal_rad

# printing status
print (f'Finished generating source table for stars and galaxies!')

# printing status
print (f'Now, writing source table into log file...')

# writing positions of stars and galaxies to log file
with open (file_log, 'w') as fh_log:
    # information of stars
    fh_log.write (f'#\n')
    fh_log.write (f'# input parameters for producing synthetic image\n')
    fh_log.write (f'#\n')
    fh_log.write (f'#   image_size_x      = {image_size_x}\n')
    fh_log.write (f'#   image_size_y      = {image_size_y}\n')
    fh_log.write (f'#   nstars            = {nstars}\n')
    fh_log.write (f'#   ngals             = {ngals}\n')
    fh_log.write (f'#   flux_min          = {flux_min}\n')
    fh_log.write (f'#   fwhm_x            = {fwhm_x}\n')
    fh_log.write (f'#   fwhm_y            = {fwhm_y}\n')
    fh_log.write (f'#   fwhm_stddev_x     = {fwhm_stddev_x}\n')
    fh_log.write (f'#   fwhm_stddev_y     = {fwhm_stddev_y}\n')
    fh_log.write (f'#   fwhm_gal_x        = {fwhm_gal_x}\n')
    fh_log.write (f'#   fwhm_gal_y        = {fwhm_gal_y}\n')
    fh_log.write (f'#   fwhm_gal_stddev_x = {fwhm_gal_stddev_x}\n')
    fh_log.write (f'#   fwhm_gal_stddev_y = {fwhm_gal_stddev_y}\n')
    fh_log.write (f'#   sky_mean          = {sky_mean}\n')
    fh_log.write (f'#   sky_stddev        = {sky_stddev}\n')
    fh_log.write (f'#   file_output       = {file_output}\n')
    fh_log.write (f'#   file_log          = {file_log}\n')
    fh_log.write (f'#\n')
    fh_log.write (f'# information of stars\n')
    fh_log.write (f'#\n')
    astropy.io.ascii.write (table_stars, fh_log, format='commented_header')
    # information of galaxies
    fh_log.write (f'#\n')
    fh_log.write (f'# information of galaxies\n')
    fh_log.write (f'#\n')
    astropy.io.ascii.write (table_gals, fh_log, format='commented_header')

# printing status
print (f'Finished writing source table into log file!')
    
# printing status
print (f'Now, generating synthetic stars...')
    
# generating stars
image_stars = photutils.datasets.make_gaussian_sources_image (image_shape, \
                                                              table_stars)

# printing status
print (f'Finished generating synthetic stars!')

# printing status
print (f'Now, generating synthetic galaxies...')

# generating galaxies
image_gals = photutils.datasets.make_gaussian_sources_image (image_shape, \
                                                             table_gals)

# printing status
print (f'Finished generating synthetic galaxies!')

# printing status
print (f'Now, creating synthetic image...')

# generating sky background
image_sky = photutils.datasets.make_noise_image (image_shape, \
                                                 distribution='gaussian', \
                                                 mean=sky_mean, \
                                                 stddev=sky_stddev)
# generating synthetic image
image = image_stars + image_gals + image_sky

# printing status
print (f'Finished creating synthetic image!')

# printing status
print (f'Now, writing FITS file...')

# preparing a FITS header
header = astropy.io.fits.PrimaryHDU ().header

# writing a FITS file
astropy.io.fits.writeto (file_output, image, header=header)

# printing status
print (f'Finished writing FITS file!')

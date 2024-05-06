#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/06 15:15:20 (Taiwan_Standard_Time_UT+8) daisuke>
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
import astropy.io.fits
import astropy.table

# importing photutils module
import photutils.datasets

# constructing parser object
descr  = 'generating a synthetic image of sky background + stars'
parser = argparse.ArgumentParser (description=descr)

# adding command-line arguments
parser.add_argument ('-b', '--background', type=float, default=1000.0, \
                     help='background level (default: 1000)')
parser.add_argument ('-s', '--sigma', type=float, default=10.0, \
                     help='noise level (default: 10)')
parser.add_argument ('-n', '--nstar', type=int, default=10, \
                     help='number of stars to add (default: 10)')
parser.add_argument ('-f', '--flux', type=float, default=10000.0, \
                     help='maximum total flux of star (default: 10000)')
parser.add_argument ('-p', '--psf', type=float, default=5.0, \
                     help='FWHM of stellar radial profile (default: 5)')
parser.add_argument ('-x', '--xsize', type=int, default=512, \
                     help='image size in x-axis (default: 512)')
parser.add_argument ('-y', '--ysize', type=int, default=512, \
                     help='image size in y-axis (default: 512)')
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
sky_background_level = args.background
noise_level          = args.sigma
nstar                = args.nstar
flux_max             = args.flux
psf_fwhm             = args.psf
image_size_x         = args.xsize
image_size_y         = args.ysize
file_output          = args.output

# making pathlib object
path_output = pathlib.Path (file_output)

# checking output file name
if (file_output == ''):
    # printing message
    print ("You need to specify output file name.")
    # exit
    sys.exit ()
# output file must be a FITS file
if not (path_output.suffix == '.fits'):
    # printing message
    print ("Output file must be a FITS file.")
    # exit
    sys.exit ()
# existence check of output file
if (path_output.exists ()):
    # printing message
    print ("Output file exists. Exiting...")
    # exit
    sys.exit ()

# image size
image_size = (image_size_x, image_size_y)

# date/time
now = datetime.datetime.now ().isoformat ()

# command name
command = sys.argv[0]

# printing message
print ("#")
print ("# input parameters")
print ("#")
print ("#  image size                = %d x %d" \
       % (image_size[0], image_size[1]) )
print ("#  mean sky background level = %f ADU" % sky_background_level)
print ("#  noise level (stddev)      = %f ADU" % noise_level)
print ("#  number of stars to add    = %d" % nstar)
print ("#  FWHM of stellar PSF       = %f pixel" % psf_fwhm)
print ("#  max total flux of stars   = %f ADU" % flux_max)
print ("#")

# printing status
print ("# now, generating background image...")

# generating sky background
image_background \
    = photutils.datasets.make_noise_image (image_size, \
                                           distribution='gaussian', \
                                           mean=sky_background_level, \
                                           stddev=noise_level)

# printing status
print ("# finished generating background image!")

# printing status
print ("# now, generating source table...")

# making a source table
fwhm_sigma            = 2.0 * numpy.sqrt (2.0 * numpy.log (2.0) )
source_table          = astropy.table.Table ()
source_table['x_0']   = numpy.random.normal (image_size_x * 0.5, \
                                             image_size_x * 0.1, nstar)
source_table['y_0']   = numpy.random.normal (image_size_y * 0.5, \
                                             image_size_y * 0.1, nstar)
source_table['sigma'] = numpy.array ([psf_fwhm] * nstar) / fwhm_sigma
source_table['flux']  = numpy.random.uniform (flux_max * 0.1, flux_max, nstar)

# printing status
print ("# finished generating source table!")

# printing source table
print ("# source_table:")
for i in range (nstar):
    print ("#   a star of flux %8.1f ADU at (x,y)=(%7.1f,%7.1f)" \
           % (source_table['flux'][i], source_table['x_0'][i], \
              source_table['y_0'][i]) )
print ("# total number of stars in source table = %d" % len (source_table))

# printing status
print ("# now, generating stars...")

# generating stars
image_star \
    = photutils.datasets.make_gaussian_prf_sources_image (image_size, \
                                                          source_table)

# printing status
print ("# finished generating stars!")

# printing status
print ("# now generating stars + background image...")

# making synthetic image
image = image_background + image_star

# printing status
print ("# now, generating FITS header...")

# preparing a FITS header
header = astropy.io.fits.PrimaryHDU ().header

# adding comments to the header
header['history'] = "FITS file created by the command \"%s\"" % (command)
header['history'] = "Updated on %s" % (now)
header['comment'] = "synthetic astronomical image simulating sky background"
header['comment'] = "Options given:"
header['comment'] = "  image size = %d x %d" % (image_size_x, image_size_y)
header['comment'] = "  mean sky background level = %f ADU" \
    % (sky_background_level)
header['comment'] = "  noise level  = %f ADU" % (noise_level)
header['comment'] = "  number of stars  = %d" % (nstar)
header['comment'] = "  FWHM of stellar PSF = %f pix" % (psf_fwhm)
header['comment'] = "  max total flux of stars  = %f ADU" % (flux_max)

# printing status
print ("# finished generating FITS header!")

# printing status
print ("# finished generating stars + background image!")

# printing status
print ("# now, writing output FITS file...")

# writing a FITS file
astropy.io.fits.writeto (file_output, image, header=header)

# printing status
print ("# finished writing output FITS file!")

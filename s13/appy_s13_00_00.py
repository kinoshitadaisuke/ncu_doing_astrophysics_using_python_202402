#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/06 14:27:17 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing datetime module
import datetime

# importing astropy module
import astropy.io.fits

# importing photutils module
import photutils.datasets

# constructing parser object
descr  = 'generating a synthetic image of sky background'
parser = argparse.ArgumentParser (description=descr)

# adding command-line arguments
parser.add_argument ('-b', '--background', type=float, default=1000.0, \
                     help='background level (default: 1000)')
parser.add_argument ('-s', '--sigma', type=float, default=10.0, \
                     help='noise level (default: 10)')
parser.add_argument ('-x', '--xsize', type=int, default=512, \
                     help='image size in x-axis (default: 512 pixel)')
parser.add_argument ('-y', '--ysize', type=int, default=512, \
                     help='image size in y-axis (default: 512 pixel)')
parser.add_argument ('-o', '--output', default='', \
                     help='output file name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
sky_background_level = args.background
noise_level          = args.sigma
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
print ("#  image size                = %d x %d" % (image_size_x, image_size_y) )
print ("#  mean sky background level = %f ADU" % sky_background_level)
print ("#  noise level (stddev)      = %f ADU" % noise_level)
print ("#")

# printing status
print ("# now, generating image...")

# generating sky background
image_background \
    = photutils.datasets.make_noise_image (image_size, \
                                           distribution='gaussian', \
                                           mean=sky_background_level, \
                                           stddev=noise_level)

# printing status
print ("# finished generating image!")

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

# printing status
print ("# finished generating FITS header!")

# printing status
print ("# now, writing output FITS file...")

# writing a FITS file
astropy.io.fits.writeto (file_output, image_background, header=header)

# printing status
print ("# finished writing output FITS file!")

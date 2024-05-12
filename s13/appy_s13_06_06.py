#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 19:20:59 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

# importing pathlib module
import pathlib

# importing astropy module
import astropy.io.fits

# constructing parser object
descr  = 'extracting science data from JWST FITS file'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--input', help='input file')
parser.add_argument ('-o', '--output', help='output file')

# command-line argument analysis
args = parser.parse_args ()

# file names
file_input  = args.input
file_output = args.output

# making pathlib objects
path_input  = pathlib.Path (file_input)
path_output = pathlib.Path (file_output)

# if file is not a FITS file, then skip
if not (path_input.suffix == '.fits'):
    # printing message
    print (f'WARNING:')
    print (f'WARNING: file "{file_input}" is not a FITS file!')
    print (f'WARNING: skipping')
    print (f'WARNING:')
    # exiting
    sys.exit (0)

# if file is not a FITS file, then skip
if not (path_output.suffix == '.fits'):
    # printing message
    print (f'WARNING:')
    print (f'WARNING: file "{file_output}" is not a FITS file!')
    print (f'WARNING: skipping')
    print (f'WARNING:')
    # exiting
    sys.exit (0)

# if file does not exist, then skip
if not (path_input.exists ()):
    # printing message
    print (f'WARNING:')
    print (f'WARNING: file "{file_input}" does not exist!')
    print (f'WARNING: skipping')
    print (f'WARNING:')
    # exiting
    sys.exit (0)

# if file exists, then skip
if (path_output.exists ()):
    # printing message
    print (f'WARNING:')
    print (f'WARNING: file "{file_output}" exists!')
    print (f'WARNING: skipping')
    print (f'WARNING:')
    # exiting
    sys.exit (0)

# opening FITS file
with astropy.io.fits.open (file_input) as hdu:
    # image of science data
    image = hdu[1].data
    # header of science data
    header = hdu[1].header
    # writing image and header into new file
    astropy.io.fits.writeto (file_output, image, header=header)

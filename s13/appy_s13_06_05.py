#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 19:10:44 (UT+8) daisuke>
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
descr  = 'showing structure of FITS files'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('files', nargs='+', help='FITS files')

# command-line argument analysis
args = parser.parse_args ()

# file names
list_files = args.files

# processing files one-by-one
for file_fits in list_files:
    # making pathlib object
    path_fits = pathlib.Path (file_fits)

    # if file is not a FITS file, then skip
    if not (path_fits.suffix == '.fits'):
        # printing message
        print (f'WARNING:')
        print (f'WARNING: file "{file_fits}" is not a FITS file!')
        print (f'WARNING: skipping')
        print (f'WARNING:')
        # skipping
        continue

    # if file does not exist, then skip
    if not (path_fits.exists ()):
        # printing message
        print (f'WARNING:')
        print (f'WARNING: file "{file_fits}" does not exist!')
        print (f'WARNING: skipping')
        print (f'WARNING:')
        # skipping
        continue

    # opening FITS file
    with astropy.io.fits.open (file_fits) as hdu:
        # printing HDU
        print (hdu.info ())

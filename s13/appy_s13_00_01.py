#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/09 09:32:17 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing astropy module
import astropy
import astropy.io.fits

# construction pf parser object
descr  = 'printing header of a FITS file'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('fits', help='FITS file name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_fits = args.fits

# making pathlib object
path_fits = pathlib.Path (file_fits)

# if the file does not exist, then stop
if not (path_fits.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_fits}" does not exist!')
    print (f'ERROR: stopping the script...')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# if the file is not a FITS file, then stop
if not (path_fits.suffix == '.fits'):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_fits}" is not a FITS file!')
    print (f'ERROR: stopping the script...')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# opening FITS file
with astropy.io.fits.open (file_fits) as hdu_list:
    # reading header of primary HDU
    header = hdu_list[0].header

    # printing formatted header
    print (f'{repr (header)}')

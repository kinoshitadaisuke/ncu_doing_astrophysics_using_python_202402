#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/12 17:59:18 (UT+8) daisuke>
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
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.esa.jwst

# date/time
now = datetime.datetime.now ().isoformat ()

# command name
command = sys.argv[0]

# constructing parser object
descr  = "downloading JWST image"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('files', nargs='+', default='', \
                     help='file names of JWST data')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
list_files = args.files

# downloading data products
for file_input in list_files:
    # downloading JWST image
    file_output = astroquery.esa.jwst.Jwst.get_product (file_name=file_input)

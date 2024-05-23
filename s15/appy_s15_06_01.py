#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/12/23 19:24:12 (Taiwan_Standard_Time_UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing zipfile module
import zipfile

# constructing parser object
descr  = "listing files in a zip file"
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('zipfile', nargs=1, default='', \
                     help='ZIP file name')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
file_zip = args.zipfile[0]

# making a pathlib object
path_zip = pathlib.Path (file_zip)

# existence check of ZIP file
if not (path_zip.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: file "{file_zip}" does not exist.')
    print (f'ERROR:')
    # stopping the script
    sys.exit (0)

# opening ZIP file
with zipfile.ZipFile (file_zip) as fh:
    # list of files in ZIP file
    list_files = fh.namelist ()
    # printing file names in ZIP file
    print (f'List of files in file "{file_zip}":')
    for filename in list_files:
        print (f'  {filename}')

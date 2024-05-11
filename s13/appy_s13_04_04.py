#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/11 19:51:12 (UT+8) daisuke>
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
import astropy.table

# importing astroalign module
import astroalign

# date/time
now = datetime.datetime.now ()

# constructing parser object
descr  = 'finding star-to-star correspondence'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('catalogue1', nargs=1, help='catalogue file 1')
parser.add_argument ('catalogue2', nargs=1, help='catalogue file 2')

# command-line argument analysis
args = parser.parse_args ()

# file names
file_cat1 = args.catalogue1[0]
file_cat2 = args.catalogue2[0]

# making pathlib objects
path_cat1 = pathlib.Path (file_cat1)
path_cat2 = pathlib.Path (file_cat2)

# check of catalogue file name
if not ( (path_cat1.suffix == '.cat') and (path_cat2.suffix == '.cat') ):
    # printing message
    print (f'ERROR: Input file must be a catalogue file (*.cat).')
    print (f'ERROR: catalogue file 1 = "{file_cat1}"')
    print (f'ERROR: catalogue file 2 = "{file_cat2}"')
    # exit
    sys.exit ()

# existence check of cat1 file
if not (path_cat1.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: catalogue file 1 "{file_cat1}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# existence check of cat2 file
if not (path_cat2.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: catalogue file 2 "{file_cat2}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# reading catalogue from a file
table_source1 = astropy.table.Table.read (file_cat1, \
                                          format='ascii.commented_header')
table_source2 = astropy.table.Table.read (file_cat2, \
                                          format='ascii.commented_header')

# (x, y) coordinates of sources
list_source1_x = list (table_source1['xcentroid'])
list_source1_y = list (table_source1['ycentroid'])
list_source2_x = list (table_source2['xcentroid'])
list_source2_y = list (table_source2['ycentroid'])
position_1     = numpy.transpose ( (list_source1_x, list_source1_y) )
position_2     = numpy.transpose ( (list_source2_x, list_source2_y) )

# finding star-to-star matching
transf, (list_matched_2, list_matched_1) \
    = astroalign.find_transform (position_2, position_1)

# transformation
list_matched_2_aligned \
    = astroalign.matrix_transform (list_matched_2, transf.params)

# printing results
print (f'#')
print (f'# result of image alignment')
print (f'#')
print (f'#   date/time = {now}')
print (f'#')
print (f'# input files')
print (f'#')
print (f'#   catalogue file 1 = {file_cat1}')
print (f'#   catalogue file 2 = {file_cat2}')
print (f'#')
print (f'# transformation matrix')
print (f'#')
print (f'# [')
print (f'#  [{transf.params[0][0]:11.6f}, {transf.params[0][1]:11.6f}, {transf.params[0][2]:11.6f}],')
print (f'#  [{transf.params[1][0]:11.6f}, {transf.params[1][1]:11.6f}, {transf.params[1][2]:11.6f}],')
print (f'#  [{transf.params[2][0]:11.6f}, {transf.params[2][1]:11.6f}, {transf.params[2][2]:11.6f}]')
print (f'# ]')
print (f'#')
print (f'#')
print (f'# list of matched stars')
print (f'#')
for i in range ( len (list_matched_1) ):
    print (f'({list_matched_1[i][0]:8.3f}, {list_matched_1[i][1]:8.3f})', \
           f'on 1st image', \
           f'==> ({list_matched_2[i][0]:8.3f}, {list_matched_2[i][1]:8.3f})', \
           f'on 2nd image')

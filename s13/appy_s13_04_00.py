#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/11 19:04:28 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy.random

# constructing parser object
descr  = 'generating random (x, y) positions of artificial stars'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-n', '--number', type=int, default=10, \
                     help='number of stars (default: 10)')
parser.add_argument ('-x', '--size-x', type=int, default=1024, \
                     help='image size on x-axis (default: 2048)')
parser.add_argument ('-y', '--size-y', type=int, default=1024, \
                     help='image size on y-axis (default: 2048)')
parser.add_argument ('-a', '--flux-min', type=float, default=100.0, \
                     help='minimum flux of stars (default: 100)')
parser.add_argument ('-b', '--flux-max', type=float, default=100000.0, \
                     help='maximum flux of stars (default: 100000)')
parser.add_argument ('-o', '--file-output', default='', \
                     help='output file name')

# command-line argument analysis
args = parser.parse_args ()

# parameters
nstars      = args.number
size_x      = args.size_x
size_y      = args.size_y
flux_min    = args.flux_min
flux_max    = args.flux_max
file_output = args.file_output

# check of output file name
if (file_output == ''):
    # printing message
    print ("ERROR: Output file name must be specified.")
    # exit
    sys.exit ()

# making pathlib object
path_output = pathlib.Path (file_output)

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file "{file_output}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# generating random numbers
rng = numpy.random.default_rng ()
position_x = rng.uniform (0, size_x, nstars)
position_y = rng.uniform (0, size_y, nstars)
flux       = rng.uniform (flux_min, flux_max, nstars)

# writing data to file
with open (file_output, 'w') as fh_out:
    # for each object
    for i in range ( len (position_x) ):
        # writing x, y, flux to file
        record = f'{position_x[i]:8.3f} {position_y[i]:8.3f} {flux[i]:10.3f}\n'
        fh_out.write (record)

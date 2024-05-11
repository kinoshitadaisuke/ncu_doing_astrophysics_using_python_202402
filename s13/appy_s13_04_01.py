#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/11 19:10:05 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# constructing parser object
descr  = 'rotation and translation of (x, y) coordinates'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-i', '--file-input', default='', \
                     help='input file name')
parser.add_argument ('-o', '--file-output', default='', \
                     help='output file name')
parser.add_argument ('-c', '--centre-x', type=float, default=1024.0, \
                     help='x-coordinate of centre of rotation (default: 1024)')
parser.add_argument ('-d', '--centre-y', type=float, default=1024.0, \
                     help='y-coordinate of centre of rotation (default: 1024)')
parser.add_argument ('-r', '--rotate', type=float, default=45.0, \
                     help='rotation angle in degree (default: 45)')
parser.add_argument ('-s', '--shift-x', type=float, default=10.0, \
                     help='amount of shift on x-axis (default:10)')
parser.add_argument ('-t', '--shift-y', type=float, default=10.0, \
                     help='amount of shift on y-axis (default:10)')

# command-line argument analysis
args = parser.parse_args ()

# parameters
file_input  = args.file_input
file_output = args.file_output
centre_x    = args.centre_x
centre_y    = args.centre_y
rotate_deg  = args.rotate
shift_x     = args.shift_x
shift_y     = args.shift_y

# conversion from deg to rad
rotate_rad = numpy.deg2rad (rotate_deg)

# check of input file name
if (file_input == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file name must be specified.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# check of output file name
if (file_output == ''):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file name must be specified.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# making pathlib objects
path_input  = pathlib.Path (file_input)
path_output = pathlib.Path (file_output)
    
# existence check of input file
if not (path_input.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Input file "{file_input}" does not exist.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# existence check of output file
if (path_output.exists ()):
    # printing message
    print (f'ERROR:')
    print (f'ERROR: Output file "{file_output}" exists.')
    print (f'ERROR:')
    # exit
    sys.exit ()

# list for new coordinates
list_new = []
    
# opening file for reading
with open (file_input, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping line, if line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (x_str, y_str, flux_str) = line.split ()
        # x, y, and flux
        x    = float (x_str)
        y    = float (y_str)
        flux = float (flux_str)
        # coordinate conversion (rotation and translation)
        x_0   = x - centre_x
        y_0   = y - centre_y
        x_1   = numpy.cos (rotate_rad) * x_0 - numpy.sin (rotate_rad) * y_0
        y_1   = numpy.sin (rotate_rad) * x_0 + numpy.cos (rotate_rad) * y_0
        x_2   = x_1 + shift_x
        y_2   = y_1 + shift_y
        x_new = x_2 + centre_x
        y_new = y_2 + centre_y
        # appending new positions to the list
        list_new.append ( (x_new, y_new, flux) )

# writing data to file
with open (file_output, 'w') as fh_out:
    # for each object
    for (position_x, position_y, flux) in list_new:
        # writing data
        record = f'{position_x:8.3f} {position_y:8.3f} {flux:10.3f}\n'
        fh_out.write (record)

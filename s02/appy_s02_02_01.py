#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:21:17 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing math module
import math

# making a parser object for command-line argument analysis
parser = argparse.ArgumentParser (description='trigonometric functions')

# choices of trigonometric functions
list_func = ['sin', 'cos', 'tan']

# adding arguments
parser.add_argument ('angle', type=float, default=0.0, help='angle in degree')
parser.add_argument ('-f', default='sin', choices=list_func, \
                     help='choice of trigonometric functions')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
angle_deg = args.angle
func      = args.f

# conversion of angle in degree into radian
angle_rad = math.radians (angle_deg)

# calculation
if (func == 'sin'):
    result = math.sin (angle_rad)
elif (func == 'cos'):
    result = math.cos (angle_rad)
elif (func == 'tan'):
    result = math.tan (angle_rad)

# printing result
if (func == 'sin'):
    print (f'sin ({angle_deg} deg) = {result}')
elif (func == 'cos'):
    print (f'cos ({angle_deg} deg) = {result}')
elif (func == 'tan'):
    print (f'tan ({angle_deg} deg) = {result}')

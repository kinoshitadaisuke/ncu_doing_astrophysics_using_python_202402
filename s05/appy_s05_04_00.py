#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/10 14:00:33 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.interpolate

# constructing a parser object
descr  = 'linear interpolation'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-a', '--gradient', type=float, default=1.0, \
                     help='gradient of a line (default: 1.0)')
parser.add_argument ('-b', '--yintercept', type=float, default=0.0, \
                     help='Y-axis intercept of a line (default: 0.0)')
parser.add_argument ('-x', '--xvalue', type=float, default=0.0, \
                     help='X-value of interpolation (default: 0.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
a              = args.gradient
b              = args.yintercept
xi             = args.xvalue

# generating data for interpolation
data_x = numpy.linspace (-10.0, 10.0, 11)
data_y = a * data_x + b

# printing data_x and data_y
print (f'line: y = {a} x + {b}')
print (f'  data_x = {data_x}')
print (f'  data_y = {data_y}')

# making a function for linear interpolation
func_interp = scipy.interpolate.interp1d (data_x, data_y, kind='linear')

# getting Y-value for X-value at X-value of "xi"
yi = func_interp (xi)

# printing result
print (f'result of interpolation:')
print (f'  func_interp ({xi}) = {yi}')
print (f'what we expect:')
print (f'  x={xi} --> y = {a} * {xi} + {b} = {a*xi+b}')

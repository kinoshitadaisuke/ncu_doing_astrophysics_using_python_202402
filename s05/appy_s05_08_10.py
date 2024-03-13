#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/15 18:44:43 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'Synthetic data generation'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-a', type=float, default=1.0, \
                     help='a of y=a(x-b)+c (default: 1.0)')
parser.add_argument ('-b', type=float, default=0.0, \
                     help='b of y=a(x-b)+c (default: 1.0)')
parser.add_argument ('-c', type=float, default=0.0, \
                     help='c of y=a(x-b)+c (default: 1.0)')
parser.add_argument ('-e', type=float, default=1.0, \
                     help='std. dev. of error (default: 1)')
parser.add_argument ('-n', type=int, default=1, \
                     help='number of data to generate (default: 1)')
parser.add_argument ('-min', type=float, default=0.0, \
                     help='minimum value of x for data generation (default: 0)')
parser.add_argument ('-max', type=float, default=1.0, \
                     help='maximum value of x for data generation (default: 1)')
parser.add_argument ('-o', default='output.data', \
                     help='output data file (default: output.data)')

# parsing arguments
args = parser.parse_args ()

# input parameters
a           = args.a
b           = args.b
c           = args.c
stddev      = args.e
n           = args.n
range_min   = args.min
range_max   = args.max
file_output = args.o

# making a pathlib object for output file
path_output = pathlib.Path (file_output)

# check of existence of output file
if (path_output.exists ()):
    # printing a message
    print (f'ERROR: output file "{file_output}" exists!')
    # stopping the script
    sys.exit (0)

# generating random numbers
err = scipy.stats.norm.rvs (loc=0.0, scale=stddev, size=n)

# function for a line
def curve (x):
    # line
    y = a * (x - b)**2 + c
    # returning y
    return y

# synthetic data for least-squares method
data_x   = numpy.linspace (range_min, range_max, n)
data_y   = curve (data_x) + err
data_err = numpy.absolute (err)
for i in range (0, 7):
    data_y[i]   -= 50.0
    data_err[i] += 50.0
for i in range (25, 32):
    data_y[i]   += 50.0
    data_err[i] += 50.0

# opening file for writing
with open (file_output, 'w') as fh:
    # writing generated synthetic data into file
    for i in range (len (data_x)):
        fh.write (f'{data_x[i]:8.3f}  {data_y[i]:8.3f}  {data_err[i]:8.3f}\n')

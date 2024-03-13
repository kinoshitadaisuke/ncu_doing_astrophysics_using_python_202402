#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/08 16:21:54 (CST) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'finding moments of distribution'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-n', '--number', type=int, default=1, \
                     help='number of random numbers (default: 1)')
parser.add_argument ('-m', '--mean', type=float, default=0.0, \
                     help='mean value of distribution (default: 0.0)')
parser.add_argument ('-s', '--stddev', type=float, default=1.0, \
                     help='standard deviation of distribution (default: 1.0)')

# parsing arguments
args = parser.parse_args ()

# input parameters
n_rg      = args.number
mean_rg   = args.mean
stddev_rg = args.stddev

# generating a set of random numbers of Gaussian distribution
rg = scipy.stats.norm.rvs (loc=mean_rg, scale=stddev_rg, size=n_rg)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{rg}')

# finding minimum value
tmin = scipy.stats.tmin (rg)

# finding maximum value
tmax = scipy.stats.tmax (rg)

# calculation of arithmetic mean of distribution
mean = scipy.stats.tmean (rg)

# calculation of variance of distribution
var = scipy.stats.tvar (rg)

# calculation of standard deviation of distribution
stddev = scipy.stats.tstd (rg)

# calculation of zeroth moment about the mean
moment_0 = scipy.stats.moment (rg, moment=0)

# calculation of first moment about the mean
moment_1 = scipy.stats.moment (rg, moment=1)

# calculation of second moment about the mean
moment_2 = scipy.stats.moment (rg, moment=2)

# calculation of third moment about the mean
moment_3 = scipy.stats.moment (rg, moment=3)

# calculation of fourth moment about the mean
moment_4 = scipy.stats.moment (rg, moment=4)

# printing minimum and maximum values
print (f'statistical values:')
print (f'  tmin          = {tmin:15.6f}')
print (f'  tmax          = {tmax:15.6f}')
print (f'  mean          = {mean:15.6f}')
print (f'  var           = {var:15.6f}')
print (f'  stddev        = {stddev:15.6f}')
print (f'  zeroth moment = {moment_0:15.6f}')
print (f'  first moment  = {moment_1:15.6f}')
print (f'  second moment = {moment_2:15.6f}')
print (f'  third moment  = {moment_3:15.6f}')
print (f'  fourth moment = {moment_4:15.6f}')

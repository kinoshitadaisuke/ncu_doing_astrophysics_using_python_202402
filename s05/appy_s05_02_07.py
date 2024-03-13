#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/08 16:30:58 (CST) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'finding statistical values of distribution'
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

# calculation of statistical values
stat_values = scipy.stats.describe (rg)

# printing statistical values
print (f'statistical values:')
print (f'  number of data = {stat_values.nobs}')
print (f'  minimum value  = {stat_values.minmax[0]:15.6f}')
print (f'  maximum value  = {stat_values.minmax[1]:15.6f}')
print (f'  mean           = {stat_values.mean:15.6f}')
print (f'  variance       = {stat_values.variance:15.6f}')
print (f'  std deviation  = {stat_values.variance**0.5:15.6f}')
print (f'  skewness       = {stat_values.skewness:15.6f}')
print (f'  kurtosis       = {stat_values.kurtosis:15.6f}')

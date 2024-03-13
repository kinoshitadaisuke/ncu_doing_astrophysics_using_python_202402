#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/06 10:24:37 (CST) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'generating a set of random numbers of Gaussian distribution'
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
n      = args.number
mean   = args.mean
stddev = args.stddev

# generating a set of random numbers of Gaussian distribution
rg = scipy.stats.norm.rvs (loc=mean, scale=stddev, size=n)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{rg}')

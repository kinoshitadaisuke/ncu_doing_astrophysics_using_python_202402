#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/06 10:06:21 (CST) daisuke>
#

# importing argparse module
import argparse

# importing scipy module
import scipy.stats

# constructing a parser object
descr  = 'generating a set of random numbers of uniform distribution'
parser = argparse.ArgumentParser (description=descr)

# adding arguments
parser.add_argument ('-n', '--number', type=int, default=1, \
                     help='number of random numbers (default: 1)')

# parsing arguments
args = parser.parse_args ()

# input parameters
n = args.number

# generating a set of random numbers of uniform distribution between 0.0 and 1.0
ru = scipy.stats.uniform.rvs (size=n)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{ru}')

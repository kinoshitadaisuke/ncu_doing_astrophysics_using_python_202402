#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:21:04 (UT+8) daisuke>
#

# importing argparse module
import argparse

# making a parser object for command-line argument analysis
parser = argparse.ArgumentParser (description='adding two integers')

# adding arguments
parser.add_argument ('n1', type=int, default=1, help='number 1')
parser.add_argument ('n2', type=int, default=1, help='number 2')

# command-line argument analysis
args = parser.parse_args ()

# input parameters
a = args.n1
b = args.n2

# calculation
c = a + b

# printing result
print (f'{a} + {b} = {c}')

#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/02 08:20:01 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing math module
import math

#
# command-line argument analysis
#

# constructing parser object
descr  = f"calculation of cosine"
parser = argparse.ArgumentParser (description=descr)

# adding options
parser.add_argument ('-a', '--angle', type=float, default=0.0, \
                     help=f"angle in degree (default: 0.0 deg)")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
a_deg = args.angle

#
# calculation
#

# conversion from degree into radian
a_rad = a_deg / 180.0 * math.pi

# calculation of cosine
cos_a = math.cos (a_rad)

# printing result
print (f"a       = {a_deg} deg")
print (f"cos (a) = {cos_a}")

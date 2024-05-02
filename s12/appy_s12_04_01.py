#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/05/02 08:19:57 (UT+8) daisuke>
#

# importing argparse module
import argparse

# importing math module
import math

#
# command-line argument analysis
#

# constructing parser object
descr  = f"calculation of sine"
parser = argparse.ArgumentParser (description=descr)

# adding options
parser.add_argument ('-a', type=float, default=0.0, \
                     help=f"angle in degree (default: 0.0 deg)")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
a_deg = args.a

#
# calculation
#

# conversion from degree into radian
a_rad = a_deg / 180.0 * math.pi

# calculation of sine
sin_a = math.sin (a_rad)

# printing result
print (f"a       = {a_deg} deg")
print (f"sin (a) = {sin_a}")

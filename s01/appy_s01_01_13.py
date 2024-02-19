#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/19 17:12:46 (UT+8) daisuke>
#

# importing math module
import math

# (x, y) coordinate
x = +1.0
y = -1.0

# calculation of arctangent
a_rad = math.atan2 (y, x)

# conversion from radian into degree
a_deg = math.degrees (a_rad)

# printing result of calculation
print (f'x            = {x}')
print (f'y            = {y}')
print (f'atan2 (y, x) = {a_rad} rad = {a_deg} deg')

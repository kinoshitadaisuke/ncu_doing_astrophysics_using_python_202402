#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/25 15:44:56 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# speeed of light in vacuum
c = astropy.constants.c

# calculation
v = 0.01 * c

# printing c and v
print (f'c = {c}')
print (f'v = 0.01 * {c}')
print (f'  = {v}')

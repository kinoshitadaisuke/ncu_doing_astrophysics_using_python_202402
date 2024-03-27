#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/25 16:13:46 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# Solar luminosity
L_S = astropy.constants.L_sun

# printing Solar radius, Jupiter radius, and Earth radius
print (L_S)
print ()

# amount of 10,000 Solar luminosity
print (f'    1 L_S = {L_S:g}')
print (f'10000 L_S = {10000 * L_S:g}')

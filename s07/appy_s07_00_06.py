#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/25 16:12:15 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# Solar radius
R_S = astropy.constants.R_sun

# Jupiter radius
R_J = astropy.constants.R_jup

# Earth radius
R_E = astropy.constants.R_earth

# printing Solar radius, Jupiter radius, and Earth radius
print (R_S)
print ()
print (R_J)
print ()
print (R_E)
print ()

# value of 1 Earth radius in the unit of Solar radius
print (f'1 R_E = {R_E:g}')
print (f'      = {R_E / R_S:g} R_S')

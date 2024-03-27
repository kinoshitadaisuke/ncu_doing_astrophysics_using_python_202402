#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/25 16:09:55 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# Solar mass
M_S = astropy.constants.M_sun

# Jupiter mass
M_J = astropy.constants.M_jup

# Earth mass
M_E = astropy.constants.M_earth

# printing Solar mass, Jupiter mass, and Earth mass
print (M_S)
print ()
print (M_J)
print ()
print (M_E)
print ()

# value of Jupiter mass in the unit of Solar mass
print (f'1 M_J = {M_J}')
print (f'      = {M_J / M_S:g} M_S')

#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/28 08:52:24 (UT+8) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# a quantity object of 900.0 sec
t = 900.0 * u_sec

# printing t
print (f't = {t}')

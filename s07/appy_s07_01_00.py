#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 11:00:51 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# a quantity object of 900.0 sec
t = 900.0 * u_sec

# printing t
print (f't = {t}')

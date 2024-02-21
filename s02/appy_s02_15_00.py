#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:27:45 (UT+8) daisuke>
#

# importing pint module
import pint

# units
ur       = pint.UnitRegistry ()
u_deg    = ur.degree
u_rad    = ur.radian
u_arcmin = ur.arcmin
u_arcsec = ur.arcsec
u_mas    = ur.mas

# angle a in deg
a_deg = 180.0 * u_deg

# converting from deg to rad
a_rad = a_deg.to (u_rad)

# printing result
print (f'a = {a_deg}')
print (f'  = {a_rad}')

# angle b
b_deg    = 1.0 * u_deg
b_arcmin = b_deg.to (u_arcmin)
b_arcsec = b_deg.to (u_arcsec)
b_mas    = b_deg.to (u_mas)

# printing results
print (f'b = {b_deg}')
print (f'  = {b_arcmin}')
print (f'  = {b_arcsec}')
print (f'  = {b_mas}')

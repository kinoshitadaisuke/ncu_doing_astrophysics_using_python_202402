#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/02/21 15:27:56 (UT+8) daisuke>
#

# importing pint module
import pint

# units
ur           = pint.UnitRegistry ()
u_km         = ur.km
u_sec        = ur.sec
u_km_per_sec = u_km / u_sec

# velocity
v = 300.0 * u_km_per_sec

# time
t = 10.0 * u_sec

# calculation of distance travelled
d = v * t

# printing result
print (f'velocity           = {v}')
print (f'time               = {t}')
print (f'distance travelled = {d}')

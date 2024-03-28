#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/28 08:52:42 (UT+8) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s
u_min = astropy.units.min
u_hr  = astropy.units.h
u_m   = astropy.units.m
u_km  = astropy.units.km

# distance travelled
d = 180.0 * u_km

# time elapsed
t = 2.0 * u_hr

# velocity
v = d / t

# unit of metre per sec
u_m_per_sec = u_m / u_sec

# printing distance, time, and velocity
print (f'distance travelled = {d}')
print (f'time elapsed       = {t}')
print (f'average velocity   = {v} = {v.to (u_m_per_sec)}')

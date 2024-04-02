#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/04/02 10:38:52 (UT+8) daisuke>
#

# importing astropy module
import astropy.time

# date/time in UT as a string
time_str = '2024-04-02T12:00:00'

# constructing Astropy's Time object from a string
time = astropy.time.Time (time_str, format='isot', scale='utc')

# calculating JD and MJD
time_jd  = time.jd
time_mjd = time.mjd

# printing JD and MJD
print (f'{time} (UT) = JD {time_jd} = MJD {time_mjd}')

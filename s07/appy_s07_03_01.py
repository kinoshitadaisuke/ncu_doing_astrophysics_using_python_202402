#!/usr/pkg/bin/python3.10

#
# Time-stamp: <2023/10/29 13:23:35 (CST) daisuke>
#

# importing astropy module
import astropy.time

# date/time in UT as a string
time_str = '2023-10-30T12:00:00'

# constructing Astropy's Time object from a string
time = astropy.time.Time (time_str, format='isot', scale='utc')

# calculating JD and MJD
time_jd  = time.jd
time_mjd = time.mjd

# printing JD and MJD
print (f'{time} (UT) = JD {time_jd} = MJD {time_mjd}')

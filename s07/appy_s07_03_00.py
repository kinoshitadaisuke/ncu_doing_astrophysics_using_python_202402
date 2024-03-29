#!/usr/pkg/bin/python3.12

#
# Time-stamp: <2024/03/28 08:54:53 (UT+8) daisuke>
#

# importing astropy module
import astropy.time

# date/time in UT as a string
time_str = '2023-10-30T12:00:00'

# printing "time_str"
print (f'type of "time_str"  = {type (time_str)}')
print (f'value of "time_str" = "{time_str}"')

# constructing Astropy's Time object from a string
time = astropy.time.Time (time_str, format='isot', scale='utc')

# printing "time"
print (f'type of "time"      = {type (time)}')
print (f'value of "time"     = "{time}"')
